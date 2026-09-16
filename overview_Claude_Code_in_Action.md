# Claude Code in Action — 課程導讀

> 原始筆記：`../Claude_Code_in_Action.md`
> 對象：**還沒看過這門課的人**。讀完這份導讀，你就能掌握課程在教什麼、核心觀念是什麼、以及可以馬上套用的做法。專有名詞保留英文，第一次出現時附中文解釋。

---

## 這門課在講什麼

這是 Anthropic 針對 **Claude Code**（官方 CLI 開發代理工具）的進階實戰課，重點是：**怎麼讓 Claude 跑得越久、越自動，你介入越少，卻仍能信任結果**。全課回答四個問題：

1. **長任務怎麼掌舵**——跑數小時的工作，怎麼事前規劃、事中修正？
2. **規則怎麼真的被遵守**——CLAUDE.md（專案指引檔，Claude 啟動時載入）裡的規則是「請求」不是「保證」；哪些該改用 hooks（掛在固定時機、必定執行的程式碼）強制執行？
3. **重複工作怎麼交出去**——routines（雲端排程任務）、headless mode（無互動介面的一次性執行模式）、GitHub Actions 各適合什麼？
4. **沒人盯著的結果怎麼驗證、整套設定怎麼分享給 team？**

中心思想一句話：**信任不是感覺，是機制。** 給 Claude 越多自由，就要有越強的自動化驗證補位——事前用 plan mode（只讀不寫的規劃模式）定範圍，事中用 permission modes（權限模式）把關意圖，事後用 hooks 與測試把關正確性。

---

## 先記住這張表：六種 permission modes

Permission modes 決定「哪些動作 Claude 不用問你就能做」。日常用 **shift-tab** 循環常用模式，狀態列永遠顯示目前模式。

| 模式 | 不用問就能做的事 | 適合場景 |
|---|---|---|
| **Manual** | 只有讀取；其他都先問 | 高風險、逐步核准 |
| **Accept edits** | 讀取、編輯檔案、常見檔案系統 bash 指令 | 日常寫程式，事後 review |
| **Plan** | 只能讀取，研究並提案，不改東西 | 動工前的規劃調查 |
| **Auto** | 全部接受，但每個動作執行前由**另一個 classifier 模型**（分類器）審查意圖 | 半放手的長任務 |
| **Don't ask** | 只允許**事先核准**的工具，其餘自動拒絕、不跳詢問 | CI、排程等**無人在場**的執行 |
| **Bypass permissions** | 跳過所有檢查（等同 dangerously-skip-permissions flag） | **只能**在隔離的 container 或 VM 裡 |

兩個最易誤解的點：

- **Auto mode 的 classifier 只看「意圖」，不看「正確性」。** Claude 把 authentication 改壞了它照樣放行——「壞掉」不等於「危險」。所以 auto mode 要配跑測試的 Stop hook：一個執行前把關意圖，一個收工時把關正確性。
- **Don't ask 不是客氣版的 auto。** 名單外的動作是**直接拒絕而非等待核准**，pipeline 才不會卡在沒人回答的詢問上。

---

## 各單元內容導讀

### 第一部分：Steer the Work

#### Steering Long Sessions（掌舵長時間工作階段）

心法：事前定範圍、事中做修正。**事前用 plan mode**：讓 Claude 以唯讀方式讀程式碼、交計畫給你審。**計畫要真的讀，不要掃過去**——在計畫階段來回修改，遠比跑完再收拾殘局便宜。

**事中四個工具：**

- **Compact**（壓縮，`/compact`）：把對話摘要成新的 context（上下文）、刪掉舊訊息騰出空間。風險是重要細節被丟掉，解法是**在指令後面加指示**，例如 `/compact Focus on the --version flag implementation`——那段話就是你對 context 的方向盤。
- **Rewind**（倒帶）：每個 user prompt 都建立 checkpoint（還原點），空白輸入列**連按兩下 Escape** 開選單：

  | 選項 | 效果 |
  |---|---|
  | Restore code and conversation | 程式碼和對話一起回滾 |
  | Restore conversation | 只回滾對話 |
  | Restore code | 只回滾檔案 |
  | Summarize from here | 摘要 checkpoint **之後**的內容（岔題後釋放空間） |
  | Summarize up to here | 摘要 checkpoint **之前**的內容（壓縮冗長前置、保留實作） |

- **Goal**（完成條件，`/goal`）：描述「做完長什麼樣」，Claude 跨回合工作直到快速 evaluator（評估器）確認達成，不會自己覺得完成就停。例：`/goal all tests in src/billing pass, and the type checker reports zero errors`；取消用 `/goal clear`。**限制：evaluator 只讀 transcript（對話逐字稿）**，條件必須從 Claude 的實際輸出就能檢查（如測試結果），不能是外部狀態。
- **Loop**（循環）：按固定或自訂步調重複執行一個 prompt，適合輪詢外部狀態（CI、部署）；按 Escape 停止。

**平行工作：worktrees**（工作樹，git 的獨立檔案樹機制）。兩個 session 搶同一批檔案會互相衝突；worktree 讓每個 agent 有自己的檔案樹，session 結束時乾淨的 worktree 自動移除。repo 根目錄的 **`.worktreeinclude`** 列出要複製進每個 worktree 的 git-ignored 檔案（環境變數檔、本機設定這類不想 commit 但每個 worktree 都要的東西）。

### 第二部分：Configure Claude

#### A CLAUDE.md That Follows（一份真的會被遵守的 CLAUDE.md）

常見陷阱：CLAUDE.md 越寫越長，Claude 開始忽略內容。這不是 bug——CLAUDE.md 是「指引」不是「強制設定」，**每一行都在競爭注意力，檔案越精簡，被遵守的比例越高**。

**先問這條規則該不該放這裡。**「never push to main」這種硬規則放 CLAUDE.md 只是「希望 Claude 尊重它」；它該放進能在動作發生前真正**擋下**的 **PreToolUse hook**。硬規則進 hooks，軟性慣例留 CLAUDE.md。

**四個存放位置**（啟動時全部載入、彼此疊加）：

| 位置 | 誰管的 | 用途 |
|---|---|---|
| Managed policy | 組織平台團隊 | 組織政策，**無法排除** |
| User | 你自己 | 跨所有專案的個人偏好 |
| Project | 團隊共用，進版控 | 團隊慣例 |
| Local | 你自己，git 忽略 | 只屬於這個 repo 的個人筆記（如自己 branch 的架構決策） |

**Imports 拆檔，但要知道它買到什麼。** 檔案太長可用 `@路徑` 語法拆開（如 `@.claude/conventions/code-style.md`）。**注意：imports 只幫你整理，不會減少 context**——啟動時所有引用的檔案都原地展開、全部載入。

**措辭決定規則會不會被遵守：**

- **具體、可檢查**：不寫「follow best practices」，寫「Put new API routes in src/api/handlers, one per file」——看結果就能判斷對不對。
- **禁止時給替代方案**：「Don't use default exports」留了一扇門；「Use named exports, not default exports」才把門關上。
- **強調語是預算**：每條都寫「IMPORTANT」「YOU MUST」等於沒人在喊，留給那兩三條違反了最痛的規則。
- **持續修訂**：Claude 做錯事就當成對 CLAUDE.md 的 bug report，直接說「add that to the CLAUDE.md file」讓它自己補規則。

#### Verification Skills（驗證用的 skill）

Skill（技能，一個帶著觸發描述與操作程序的資料夾）適合固定重複的多步驟工作，而**第一個該建的 skill 就是「驗證自己的工作」**。

平常的檢查靠**你記得去要求**——記得叫它跑測試、記得讀 diff，漏一次壞程式碼就溜過去。驗證 skill 把這依賴拿掉：變更符合 skill 的 description（描述，即觸發條件）時自動觸發，固定走同一套流程——跑測試、讀 diff、**確認沒有測試被偷偷放寬只為了讓它通過**、附證據回報 pass/fail。注意最後那項：測試全綠不等於安全，測試可能被弱化成怎樣都會過；「做完」不是「diff 看起來對」，而是**閘門真的跑過、結果被明確陳述**。

**Skill 資料夾不只放指令**：`skill.md` 本體精簡（名字、description、程序）；詳細材料放旁邊的 `reference.md`，需要時 Claude 才讀；**scripts**（如跑所有閘門的 `check.sh`）由 Claude **執行**而非載入 context，所以 skill 可以自帶工具。

**三個指令表面各管什麼**（易混淆）：

| 表面 | 性質 | 放什麼 |
|---|---|---|
| CLAUDE.md | Claude 遵循的指引 | 隨時適用的慣例（命名、檔案放哪） |
| Skill | Claude 遵循的指引 | 綁定特定任務的程序與參考資料 |
| Hook | **實際執行的程式碼** | **不容許被跳過**的規則 |

成本觀念：skill 被用到前**只有 descriptions 載入 context**，包成 skill 幾乎沒代價。建好 check 進 `.claude/skills`，全 team 繼承同一套檢查。經驗法則：**同一段多步驟指示打過兩次，就該做成 skill。**

#### Permission Modes（權限模式）

六種模式見前面的表。本課補充：shift-tab 循環的是日常四種（manual、accept edits、plan、auto）；classifier 會擋 production 部署與 migration、force push、把下載的程式碼直接 pipe 進 shell、外傳敏感資料、刪除 session 期間存在的檔案，會放行專案內本機編輯、從 lock file 裝依賴、唯讀請求、push 到自己的 branch——護欄仍在演進，實際清單以官方文件為準。Bypass permissions 只該出現在隔離的 container 或 VM，沒有例外。

#### Hooks（掛鉤）

CLAUDE.md 是請求不是保證——「always format after editing」Claude *通常*會聽，但無人監督的長 run 裡「通常」不夠。Hook 是**在流程固定時機執行的決定性程式碼**，把規則從「通常會聽」變成「沒辦法跳過」。

**值得認識的事件**（全部約 30 個，常用這幾個）：

| 事件 | 觸發時機 | 典型用途 |
|---|---|---|
| **PreToolUse** | 工具呼叫**之前** | 強制執行核心——唯一能在事前擋下動作的事件 |
| **PostToolUse** | 工具呼叫成功**之後** | 自動 format、自動 lint |
| **Stop** | Claude 想結束回合時 | 條件不滿足就拒絕收工；子代理有對應的 SubagentStop |
| **PreCompact / PostCompact** | 壓縮前／後 | 壓縮前後處理 |
| **InstructionsLoaded** | CLAUDE.md 或規則檔載入時 | 稽核哪些東西真的進了 context |
| **SessionStart** | session 開始時 | 準備環境；只想在全新啟動跑就用 startup source |

**最易踩的坑：壓縮後想把 context 塞回去，不要用 PostCompact，要用 SessionStart 搭配 compact matcher**——那才是輸出會真正回到對話裡的事件。

**PreToolUse 用 JSON 回覆決定**：印出 JSON 並以 0 結束，關鍵欄位 `permissionDecision` 三個值：`allow`（放行）、`deny`（擋下）、`ask`（交回使用者決定）；還有個 `defer` 只適用於非互動的 `-p` 執行，很少用。更有趣的是 **`updatedInput`**：與其擋下不如**改寫**呼叫。**注意：`updatedInput` 會取代整個 input 物件**，沒改的欄位也要原樣回傳，否則遺失。

**Exit codes**（給不回 JSON 的簡單 hook）：

| Exit code | 效果 |
|---|---|
| **0** | 成功。stdout 是 JSON 就解析；純文字多數事件忽略，但在 **SessionStart、UserPromptSubmit、UserPromptExpansion** 會加進 context |
| **2** | **blocking error**。stderr 回饋給 Claude 當 context；幾乎所有事件的「擋下」靠它 |
| 其他 | 非阻擋。stderr 記 log，Claude 照常繼續 |

**最常搞錯：exit code 1 感覺像錯誤，但它不會 block**——Claude 照樣執行；想擋就 exit 2。其他細節：exit 2 連 Stop 都能擋（「你還沒做完」的機制）；PostToolUse 因為工具已跑完，擋也來不及，但仍可回饋文字；Notification、SessionStart 等少數事件完全忽略 blocking。

**兩個實戰範式**：(1) **redact 而不是 block**——PreToolUse hook 用 matcher 挑監看的工具（可加 if 條件縮到特定指令），偵測到 `sk_live_` 這類 secret pattern 時用 `updatedInput` 換成占位符，**指令照跑、secret 永遠出不去**；(2) **跨 compact 保存狀態**——SessionStart hook 配 compact matcher，壓縮後立刻印出「最近在改哪些檔案」的簡短摘要回到 context，Claude 接著做而不是冷啟動。

### 第三部分：Automate Repeat Work

#### Routines and Headless（例行任務與無介面模式）

信任 Claude 做某件事之後，就別再手動觸發。這是一條「自建程度」光譜：

| 工具 | 跑在哪 | 適合什麼 |
|---|---|---|
| **Routines** | Anthropic 管理的雲端 | 重複工作的**預設選項**，什麼都不用 host |
| **Headless mode**（`claude -p`） | 你的環境／腳本 | 需要你的 pipeline、用 shell 管線串資料 |
| **`--bare`** | 同上，決定性模式 | CI 需要每次結果**完全一致** |
| **Agent SDK** | 你的 TypeScript / Python 應用內 | 工作屬於你自己的產品 |

**Routine** 打包一個 prompt、作用的 repository、需要的 connectors（連接器）、一個觸發條件。觸發三種：cron 排程、對其 API endpoint 發 HTTP POST、GitHub 事件（如新 PR）。建立兩種方式：網頁 claude.ai/code/routines，或終端機直接 `/schedule daily dependency audit at 9am`。

**依賴前的三個限制**：(1) research preview（研究預覽版），行為會變；(2) 週期排程**最頻繁一小時一次**；(3) 每次執行從 default branch 的**全新 clone** 開始，**只能 push 到 `claude/` 開頭的 branch**（除非逐 repo 放寬）——防止自主執行改寫 main 的護欄。

**Headless mode** 核心是 `-p` flag（`--print` 縮寫）：一次性執行、無互動 UI、讀 stdin 寫 stdout，像任何 shell 工具一樣可 pipe。**關鍵特性：`-p` 跳過 hooks、skills、plugins、MCP servers 和 CLAUDE.md 的自動載入**——你得到 Claude 加上明確允許的工具，本機環境一概不載，好處是啟動快很多。

要結構化資料就用 `--output-format json` 搭配 `--json-schema` 傳入你的 JSON schema，符合 schema 的物件落在回應的 `structured_output` 欄位，可以直接 `| jq '.structured_output.functions'` 抽出來接進資料庫或下一個腳本。多步驟不必塞一條指令：從 JSON 輸出抓 session ID，之後 `claude --resume "$(jq -r .session_id /tmp/plan.json)"` 帶完整 context 接續——第一個腳本產計畫，第二個執行它。

**Agent SDK** 是 TypeScript 與 Python 函式庫，提供 `query` 函式與跟 CLI 相同的 primitives：傳 prompt 加選項（`allowedTools`、system prompt、permission mode），迭代 Claude 串流回來的訊息。同一顆引擎，從你的產品裡呼叫。

課程建議：**從 routines 開始，真的需要更多控制才往光譜下方走。**

#### GitHub Actions and Code Review

Pull request 是交接重複工作最好的地方，有兩條路。

**託管路線：Code Review。** Anthropic 託管的服務，透過 Claude GitHub app 審 PR，不用建不用 host。組織管理員從 admin settings 啟用、裝 app、挑 repo、選時機（PR 開啟時一次／每次 push／有人留言 `@claude review` 時）。審查代理**對照整個 codebase 分析 diff**，不只看被改的行；findings 以 inline comment 貼在確切的行上、標嚴重程度，並去重與排序——你讀到的是幾個真問題，不是一牆 nitpick。

**邊界要記清楚：**

- **它永遠不會 approve 或 block PR**——判斷權留在人類，Claude 只標記。
- **沒有託管 autofix**。套用修正是**本機動作**：終端機跑 `/code-review`，加 `--fix` 把 findings 套進 working tree。
- 目前是 research preview，適用 team 與 enterprise 方案。

**自建路線：GitHub Action。** 工作超出 review 就用它——留言觸發實作、排程報告、任何你本來會寫 workflow 的事。設定：在 Claude Code 裡跑 `/install-github-app`（需 repo admin）。Action 本體是 `anthropics/claude-code-action@v1`，常用 inputs：`anthropic_api_key`（選填）、`github_token`（預設 `secrets.GITHUB_TOKEN`）、`trigger_phrase`（留言觸發詞，預設 `@claude`）、`use_bedrock` / `use_vertex`、`prompt`、`claude_args`（原樣傳給 Claude Code 的 CLI 參數字串）。Workflow 放 `.github/workflows/claude.yaml` 就會監聽 PR 與 issue 留言的 `@claude`，Claude 接手 push commits 並留言說明；加 cron trigger 可做每日 rollup，加 `workflow_dispatch` 可手動觸發。

**用 `claude_args` 調校無人執行的三個旋鈕**：`--max-turns 5` 給 agent loop 硬上限；permission mode 選不會停下來問的；allowed tools 只給剛好需要的（報告類就唯讀）。

決策準則：**PR review 走託管路線；要 Claude 在 CI 裡真的動手做事（不只留言）才換 action。**

### 第四部分：Verify and Share

#### Trust It: Verifying Unsupervised Runs（驗證無人監督的執行）

原則一句話：**驗證強度和放手程度成正比**——盯著跑完的短 session 掃一眼就好；無人在場的 CI run 就得事後完整重建。四個做法：

1. **無人執行留在 auto mode，不要 bypass permissions。** Classifier 仍審查每個動作的危險性，這張網值得留；但它不判斷正確性，驗證標準一分不能降。
2. **從 diff 開始，不是從摘要開始。** 先跑 `/code-review` 掃變更，再親眼看 `git diff`。陷阱：讀起來完美的摘要底下，diff 可能動到你沒預期的檔案——摘要不會說，diff 會。**乾淨的文字報告不是乾淨程式碼的證明。**
3. **把測試變成閘門，不是承諾。** 關卡是測試有沒有過、以及 Claude 是**真的跑了**還是只是聲稱。用 hook 讓它跳不過：Stop hook 跑測試、失敗就拒絕結束回合；PostToolUse hook 每次編輯後 lint 和 type check。關鍵是 **exit 2**——失敗直接回饋給 Claude，它讀到就自己修，而且每次都觸發。headless run 用它的 JSON 結果和 exit code 驗證。
4. **找一雙冷眼睛。** 開全新 session 或 sub-agent review 改過的程式碼——它不知道程式碼怎麼寫出來的、對原做法沒有立場，能抓到原執行「自己說服自己」放過的問題。

#### Plugins（外掛）

調校出值得信任的 `.claude` 目錄後，怎麼給全 team 用？**Plugin 就是 Claude Code 打包與搬運整套設定的單位**：一個可安裝的整體，含 skills、subagents、hooks、MCP server 設定，還有 LSP servers、背景監控、themes 和一小片 settings.json。一個版本、一次安裝。

**使用別人的 plugin：**

- 直接安裝：`/plugin install org-name@plugin-name`，裝完跑 `/reload-plugins` 生效。
- Team 更好的做法是加一次私有 **marketplace**（外掛市集）：`/plugin marketplace add your-org/claude-plugins`，之後所有安裝經過它，集中探索、版本追蹤與更新；Discover tab 可瀏覽搜尋。

**本課最重要的警告：先讀再裝。** Plugin 是**以你的權限在你機器上執行的程式碼**——你為了 skill 裝的 plugin，附帶的 PreToolUse 和 Stop hooks 也一併生效。一個社群 plugin 完全可以夾帶每次都往外連網的 Stop hook，你的設定不會有任何警示。安裝前 Claude Code 會顯示將安裝什麼、估算 context 成本，並警告 Anthropic 不控制第三方 plugin 內容。in-app 提交的 plugin 經 Anthropic **自動化審查**後上社群 marketplace，官方 marketplace 是獨立策展軌道——但**「審查過」不等於「可信」**，只從真正信任的來源安裝。

**元件是「並行」不是「覆蓋」：**

- **Hooks 會疊加**：plugin 的 PreToolUse hook 和你自己的**都會**觸發，誰也不取代誰。
- Skills、agents、commands 以 plugin 名稱作 namespace，不會撞名。
- Plugin 可帶 settings.json，但 Claude Code 只認**兩個 key**：agent 與 subagent status line。其中 **agent key 要特別警覺**——設定它會把 plugin 的某個 subagent 連同 system prompt、工具限制與模型**提升為主執行緒**，等於啟用 plugin 就改變了 Claude Code 的預設行為。
- 裝好後可從 plugin panel 檢視、管理與解除安裝。

**打包自己的 plugin：** 不需要重構，plugin 就用你已有的 `.claude` 結構——每個 skill 一個資料夾、agents 底下每個 subagent 一個 markdown 檔、`hooks/hooks.json` 與 `.mcp.json` 放 plugin 根目錄，靠目錄慣例自動發現。可選的 manifest 放 `.claude-plugin/plugin.json`（name、version、description、author）。**Manifest 是選配的，但如果寫，name 是唯一必填欄位**——它把 skills 命名成 `company-name:skill-name` 避免撞名；version 像其他依賴一樣管理，讓 team 的版本追蹤能運作。

#### Course Quiz

原始筆記中此頁為測驗題型頁面，無內容記錄。

---

## 讀完這門課你會得到什麼

一句話總結：**把「盯著 Claude 做事」升級成「設計一套讓 Claude 自己把事做對的系統」。**

- 長任務操作節奏：plan mode 定範圍 → 帶指示的 `/compact` 控制 context → rewind 修正路線 → `/goal` 定義完成 → worktrees 平行開工。
- 規則放置的決策框架：慣例進 CLAUDE.md、任務程序進 skill、**不容跳過的硬規則進 hook**。
- Hooks 實戰模式：`permissionDecision` 與 `updatedInput`（redact 而非 block）、exit 2 才會擋（**exit 1 不會！**）、Stop hook 把測試變成收工閘門、SessionStart + compact matcher 跨壓縮保存狀態。
- 自動化選型直覺：routines → `claude -p` → `--bare` → Agent SDK，按需要往光譜下方走。
- 無人執行的驗證紀律：auto mode 保底、diff 優先於摘要、測試 hook 化、冷眼 sub-agent 複審。
- Team 規模化機制：`.claude` 打包成 plugin、加私有 marketplace——以及「先讀再裝」的安全意識。

如果入門課教的是「怎麼用 Claude Code」，這門課教的是「**怎麼在放手的同時仍然掌控品質**」——想把 AI coding agent 導入 team 日常流程的人，這是必修的一門。
