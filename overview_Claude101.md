# Claude 101 — 課程導讀

> 原始筆記：`../Claude101.md`
> 對象：**還沒看過這門課的人**。讀完這份導讀，你就能掌握課程在教什麼、核心觀念是什麼、以及可以馬上套用的做法。專有名詞保留英文，第一次出現時附中文解釋。

---

## 這門課在講什麼

這是 Anthropic 官方的 Claude 入門課，對象是**一般知識工作者**——不需要任何程式背景。整門課圍繞 claude.ai 展開，帶你從「第一次跟 Claude 對話」一路走到「接上公司工具、讓 Claude 替你跑完整個任務」。

課程分成五個部分，由淺入深：

1. **Meet Claude**：Claude 是什麼、怎麼下 prompt（提示詞，你給 AI 的指令與描述）、結果不理想怎麼修、桌面版的三種工作型態。
2. **Organizing your work and knowledge**：用 **Projects**（專案）、**Artifacts**（成品）、**Skills**（技能）組織工作——三者的定義見下方表一。
3. **Expanding Claude's reach**：用 **Connectors**（連接器）、**Enterprise Search**（企業搜尋）、**Research**（深度研究）讓 Claude 接觸你的工具和全網資料。
4. **Putting it all together**：依職務別列出可直接照做的 use case，並介紹 claude.ai 之外的其他 Claude 產品。
5. **Conclusion & certificate**：總結與測驗，通過後取得可放上 LinkedIn 的完課證書。

課程反覆強調一個心態：**Claude 是 thinking partner（思考夥伴），不是搜尋框**。你帶脈絡與專業判斷，Claude 帶智慧與速度，最好的結果來自反覆迭代。

---

## 先記住這兩張表

### 表一：功能地圖——每個功能解決什麼問題

| 功能 | 一句話定位 | 解決的痛點 |
|---|---|---|
| **Projects** | 有自己知識庫、指示與記憶的工作區 | 不用每次重新上傳檔案、重講背景 |
| **Artifacts** | 對話旁獨立視窗中的可互動成品 | 產出不埋在聊天紀錄裡，可編輯、分享、發布 |
| **Skills** | 教 Claude 特定工作流程的指令包 | 重複性流程每次都用同一套步驟執行 |
| **Connectors** | 透過 **MCP**（Model Context Protocol，讓 AI 連接各種工具的開放標準）接上你的工具 | Claude 直接讀寫你的 Gmail、Slack、Notion 等真實資料 |
| **Enterprise Search** | 側邊欄的「Ask {你的組織名}」，全公司知識的預建專案 | 跨工具找公司內部資訊（限 Team / Enterprise） |
| **Research** | 代理式（agentic）多步驟調查，產出附引用的報告 | 原本要花數小時的多來源研究 |

### 表二：三個最容易搞混的對照

| 容易搞混的一組 | 差別 |
|---|---|
| **Projects vs. Skills** | 課程口訣：**projects store knowledge, skills perform tasks**。Project 存「知識」（what），Skill 存「流程」（how），兩者可搭配使用。 |
| **Artifacts vs. 檔案產出** | Word、Excel、PowerPoint、PDF **不是** artifact——它們走另一套 file creation 能力，以可下載檔案交付。Artifact 是在對話旁視窗即時渲染的內容。 |
| **Web search vs. Research vs. Enterprise Search** | 快查單一事實用 web search；跨多來源、附引用的深度報告用 Research；答案在**公司內部**資料時用 Enterprise Search。 |

---

## 各單元內容導讀

### 第一部分：Meet Claude

#### 單元 1：What is Claude?

開場定義 Claude 是什麼：

- Claude 的設計原則是 **helpful, harmless, and honest**（有幫助、無害、誠實），背後的訓練方法叫 **Constitutional AI**（憲法式 AI）——讓模型對齊人類價值觀、行為透明。
- Claude 擅長五大類任務：寫作、研究分析、寫程式、問題解決與推理、學習新事物。兩個關鍵能力值得記：
  - **context window**（上下文視窗，模型一次能處理的文字量）可達 **200K+ tokens**（token 是模型處理文字的基本單位，200K 約等於 500 頁以上的文字）；Pro、Max、Team、Enterprise 方案搭配支援的模型時可達 **1M tokens**。
  - **Thinking**：Claude 可以近乎即時回答，也可以先逐步推理再回答。另有 **Learning mode**，引導你自己思考而不是直接給答案。
- 入口很多：Claude.ai（本課程主軸）、Claude Code、Claude Tag（Slack）、Claude Design、Claude for Microsoft 365。所有方案（Free、Pro、Max、Team、Enterprise）都能用網頁／桌面／手機 app，登入後對話、專案、記憶與偏好跨裝置同步。

#### 單元 2：Your first conversation with Claude

教你寫出有效的 prompt。核心是三要素框架（改編自 AI Fluency 課程的 4D Framework）：

| 要素 | 問自己 | 例子 |
|---|---|---|
| **Setting the stage**（鋪陳背景） | 我的角色、目標、相關背景？ | 「我是新創行銷主管，正準備 Series A 募資簡報」 |
| **Defining the task**（定義任務） | 我要 Claude 採取什麼行動？ | 「研究獨立電影串流市場的趨勢、競品與機會」 |
| **Specifying rules**（指定規則） | 風格、格式、範例？ | 「用最新網路研究並附引用，寫成不超過 5 頁的報告」 |

其他重點：

- 跟 Claude 說話**就像跟同事說話**——自然、簡潔、口語即可。
- 上傳檔案給脈絡：支援 PDF、DOCX、CSV、TXT 及 PNG、JPEG 等圖片，連 PDF 裡的圖表都能分析。
- 對話是迭代的：追問、給回饋、必要時開新對話重來；點自己訊息上的鉛筆圖示可**編輯並重送 prompt**。想讓偏好套用到每次對話：Settings > General > 'What personal preferences should Claude consider?'。

#### 單元 3：Getting better results

第一次的 prompt 很少一次到位，這個單元教你怎麼修：

- **迭代心態**：把第一版當起點；回饋要具體（「刪掉前兩段、結論改成行動導向」比「短一點」好）；對話歪掉時，開新對話往往比拉回來快。
- 正式介紹 **AI Fluency** 與 **4D Framework**（Delegation 委派、Description 描述、Discernment 辨別、Diligence 盡責）——上一單元的三要素就是 Description 的應用。
- **Evals**（evaluations 的縮寫，系統性測試 AI 在特定任務上表現的方法），四步驟：蒐集 5–10 個平常工作的實例 → 寫測試 prompt → 比較 Claude 的結果與原版 → 調整 prompt、補範例，或判斷哪些環節必須人工把關。

#### 單元 4：How you'll work with Claude on your desktop

桌面 app 上的工作分**三種型態**，辨認任務屬於哪一種就是本單元的全部技能：

| 型態 | 什麼時候用 | 在產品裡的位置 |
|---|---|---|
| **一來一往（turn by turn）** | 答案會改變你下一個問題、你想全程參與、任務很小 | **Chat** 分頁。桌面版加值：Mac 雙擊 Option 鍵快速呼叫、截圖／分享視窗、語音口述、桌面 connectors |
| **整件事交辦（handing work off）** | 任務有多個步驟、產出是真正的檔案、橫跨多個工具、要定時執行 | **Cowork** 分頁（Pro、Max、Team、Enterprise）：本機資料夾存取、排程任務、subagents（拆給平行的背景工作者）、瀏覽器操作、computer use（直接操作電腦，research preview）、plugins |
| **在程式碼庫裡開發** | 你寫程式 | **Code** 分頁（Pro、Max、Team、Enterprise）。可選 Local 或 Cloud（連 GitHub repo、關掉 app 也繼續跑）；自主程度可設 Manually approve、Accept edits、Plan |

Chat 與 Cowork 的具體差別：Chat 的成品是**下載連結**；Cowork 直接**存回你的資料夾**。交辦不等於放手不管——Claude 會先給你看計畫，執行中可隨時介入，重要動作（寄信、分享檔案）會先徵求同意。

### 第二部分：Organizing your work and knowledge

#### 單元 5：Introduction to projects

Project 是自成一格的工作區，有自己的記憶、對話紀錄、知識庫與自訂指示。適合**持續性的工作**：有會重複使用的參考資料、對回應有固定要求、或團隊需要共用脈絡時。

建立三步驟：

1. 側邊欄點 "Projects"（或到 claude.ai/projects）→ "+ New Project"，取個描述性的名字。
2. 寫 **project instructions**（專案指示）：工作背景、語氣風格、具體要求，套用到專案內**每一則對話**，還能自動化流程（「當我上傳會議逐字稿時，用這個範本做結構化摘要」）。
3. 建 **knowledge base**（知識庫）：上傳 PDF、DOCX、CSV、TXT、HTML 或直接連結文件。**檔名要有意義**——Claude 靠檔名找資料，"Q4-2024-Brand-Guidelines.pdf" 比 "document1.pdf" 有用得多。

知識庫變大怎麼辦？逼近 context window 上限時，專案自動切換成 **RAG**（Retrieval Augmented Generation，檢索增強生成）：改成搜尋並只取用相關部分，**容量最多擴大 10 倍**、體驗不變。

Team / Enterprise 可分享專案，三種權限：**Can view**（可看可聊不可改）、**Can edit**（完整協作）、**Owner**（控制一切）。

#### 單元 6：Creating with artifacts

Artifact 是 Claude 在對話旁**專屬視窗**裡建立的獨立、可互動產出。當內容夠大（通常超過 15 行）、自成一體、你會想編輯或重複使用時，Claude 會自動建立 artifact；沒有的話直接說「Create this as an artifact」。

常見類型：文件、程式碼片段、HTML 網頁、SVG 圖像、Mermaid 圖表、React 元件（有真實邏輯的計算機、儀表板、遊戲）。Word / Excel / PowerPoint / PDF 則不是 artifact（見表二）。

分享方式三種：複製或下載；組織內分享（Team / Enterprise）；**公開發布**（Free / Pro / Max）——只有選定版本公開、對話保持私密，有連結就能看（不需帳號），不被搜尋引擎索引，隨時可下架。

用得好的訣竅：需求講具體（「能按類別輸入支出、有圓餅圖、超支會警告的月度預算追蹤器」）、描述最終使用者是誰、**一次改一個地方**。

#### 單元 7：Working with skills

Skill 是一個資料夾，裝著指令、腳本與資源，Claude 會**動態載入**來提升特定任務的表現——可以想成「專業知識包」。你如果用過 Claude 做 Excel 或 PPT，其實已經用過 Skills 了。

兩類 Skills：**Anthropic Skills**（官方建立維護，如 Excel、Word、PowerPoint、PDF 產出，付費用戶皆可用，Claude 判斷相關時自動呼叫）與 **Custom Skills**（你或組織自建，把可重複的流程固化下來——季度差異分析方法、品牌語氣審查、法遵檢查清單）。

啟用路徑：Settings > Capabilities，先確認 **Code execution and file creation** 開啟（Skills 需要沙箱環境），再逐一開關。Enterprise 要 Owner 先在 Admin settings 開啟；Team 預設開啟。目前是 Pro、Max、Team、Enterprise 的 feature preview。

**建立自訂 Skill 最簡單的方式是直接跟 Claude 對話**：告訴它「我想建一個寫季度業務回顧的 skill」，回答它的訪談問題、上傳範本或範例，Claude 就會生成結構正確的 skill 檔，存檔即可用，之後在 Customize 分頁查看與編輯。安全提醒：Skills 可能含可執行程式碼——**只安裝信任來源的 custom Skills**。

### 第三部分：Expanding Claude's reach

#### 單元 8：Connecting your tools

Connectors 讓 Claude 從「助理」變成「掌握你實際資料的協作者」。背後標準是 **MCP**——課程比喻成「AI 界的 USB-C」：一個通用介面，任何開發者都能為任何工具建 connector。

兩種類型：**web connectors**（雲端服務：Google Drive、Notion、Slack、Gmail、Stripe 等）與 **desktop extensions**（跑在本機、需要 Claude Desktop app，如本機檔案存取、瀏覽器控制、Figma）。官方目錄在 **claude.ai/directory**，或在對話視窗左下角點 + > Connectors。連接流程：Connect → 登入驗證 → 授權權限 → 回 Claude 用「Can you access my [tool name]?」測試。

安全三原則：權限**細分且可個別開關**；**Claude 只看得到你本來就看得到的東西**（接了公司信箱不代表能看 CEO 的信）；隨時可以斷開連接。

#### 單元 9：Enterprise search

限 **Team / Enterprise** 方案（其他方案可跳過）。Enterprise Search 在側邊欄加一個「Ask {你的組織名}」入口——可以想成**替全公司預建好的 project**，知識庫已載入、開箱即問。它專為資訊查找設計，用的是 Anthropic 調校過的自訂指示。

適合的問法：「我休假昨天發生了什麼？」「公司的遠端工作政策是什麼？」——Claude 會跨 SharePoint、Slack、Gmail、Google Drive 等所有已連接工具搜尋、綜合成單一回應，**且一定附引用來源**。

設定分兩段：組織 **Owner** 先完成初始設定（命名、描述），個別使用者再依引導驗證要搜尋的服務。安全性：只顯示你本來就有權限看的內容，對話私密，資料不另行索引或儲存。

#### 單元 10：Research for deep dives

Research 把 Claude 從對話助理變成**系統性調查員**：先用 Thinking 規劃路徑，再多輪彼此累積地搜尋（有時同時跨數百個來源），自主決定下一步查什麼，最後綜合成**每個論點都附引用**的報告。代價是時間——幾分鐘起跳。

什麼時候用哪個（本課最實用的判斷表之一）：

| 需求 | 用什麼 |
|---|---|
| 快查單一事實、一兩個來源就夠、速度優先 | web search |
| 跨多來源的完整報告、競品／供應商比較、需要可驗證引用 | **Research** |
| 答案在公司內部知識（文件、Slack、email、會議紀錄） | Enterprise Search |

啟用方式：對話框左下 + 按鈕 → 選 Research（**前提是 web search 已開啟**）。因為一跑就是幾分鐘，prompt 值得寫好：目標講具體（不要「Tell me about the EV market」，要「分析電動車電池市場——關鍵玩家、技術趨勢、供應鏈挑戰」）、指定報告章節結構、給預算／時程等限制，甚至可**先請 Claude 幫你改 Research prompt**。接上 Google Workspace 後可同時撈 email、行事曆、文件與網路資料，例如「檢視我下週的行事曆，研究每一家要開會的公司」。

### 第四部分：Putting it all together

#### 單元 11：Claude in action: use-cases by role

依職務別（通用、業務、行銷、財務、HR、法務、研究）列出可直接照做的 use case，每個都連到官方 Use Case Gallery 的逐步指南。例如：把品牌指南包成 skill、建競品 battle card 庫、分析 campaign 成效、看懂接手的複雜試算表、做新人 onboarding 指南、追蹤 discovery 時間線、規劃文獻回顧。

#### 單元 12：Other ways to work with Claude

claude.ai 之外的 Claude 產品巡禮，各自對應「工作實際發生的地方」：

| 產品 | 場景 |
|---|---|
| **Claude Code** | 終端機／IDE 裡用自然語言開發：寫功能、跑測試、建 commit、修 lint |
| **Claude Tag** | Slack 裡 tag Claude：摘要討論串、備會、從 bug 回報直接開 Claude Code session |
| **Claude Design** | 從描述、草圖或截圖生成可互動 UI 原型，可套用團隊 design system |
| **Claude for Excel / PowerPoint / Word / Outlook** | 側邊欄直接在文件裡工作：Excel debug #REF! / #VALUE! 等公式錯誤、建 pivot table；PPT 大綱變初稿並保留範本樣式；Word 起草改寫、處理 tracked changes；Outlook 分類收件匣、擬回信（beta，需另外安裝） |
| **Claude in Chrome** | 瀏覽器側邊欄：摘要網頁、自動填表、跨分頁維持脈絡（public beta，建議用於信任網站的低風險任務，高風險動作會先徵求同意） |

#### 單元 13–14：What's next? 與 Certificate of completion

總結全課要點，附延伸資源（AI Fluency 課程、Use Case Gallery、Anthropic Help Center、Claude Code in Action、Introduction to Claude Cowork 等），最後完成測驗取得證書。收尾建議很務實：**從一件本週就會做的小事開始**——擬一封 email、摘要會議紀錄、分析一張試算表——做了、迭代、長出手感。

---

## 讀完這門課你會得到什麼

一句話總結：**一張 Claude 全功能地圖，加上「什麼任務用什麼功能」的判斷力。**

- 馬上能用的 prompt 三要素框架（setting the stage / defining the task / specifying rules）＋迭代修正的方法。
- 三組關鍵判斷力：Projects vs. Skills、Artifacts vs. 檔案產出、web search vs. Research vs. Enterprise Search。
- 桌面工作的三種型態（Chat 一來一往／Cowork 整件交辦／Code 開發），以及辨認眼前任務屬於哪一種的直覺。
- 一套簡易 evals 方法，用你自己的工作實例驗證 Claude 在特定任務上行不行。
- 依職務可直接照做的 use case 清單，以及 claude.ai 之外八種 Claude 產品的適用場景。

如果你負責在團隊裡推動 Claude 導入，這門課適合當作**所有人的第一門產品課**——觀念課搭配 Introduction to AI Fluency，開發者再接 Claude Code in Action。

---

*課程版權：Copyright 2025 Anthropic. All rights reserved.*
