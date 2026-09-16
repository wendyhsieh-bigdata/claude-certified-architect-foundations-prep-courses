# Building with the Claude API — 課程導讀

> 原始筆記：`../Building_with_the_Claude_API.md`
> 對象：**還沒看過這門課的人**。讀完這份導讀，你就能掌握課程在教什麼、核心觀念是什麼、以及可以馬上套用的做法。專有名詞保留英文，第一次出現時附中文解釋。

---

## 這門課在講什麼

這是 Anthropic 的官方開發者課程，講師是 Anthropic 技術團隊成員 Stephen Grider。主題只有一個：**如何用 Anthropic API（應用程式介面）把 Claude 做進你自己的應用程式裡**——從發出第一個 API request 開始，一路教到 tool use（工具呼叫）、RAG、MCP，最後收在 agent（代理）與 workflow（工作流程）的架構選擇。

課程的路線圖是：認識 Claude 的三個模型家族 → 用 API 存取模型 → prompt evaluation（提示詞評估）→ prompt engineering（提示詞工程）→ tool use → RAG（Retrieval Augmented Generation，檢索增強生成）→ Claude 的進階功能（extended thinking、圖片、PDF、citations、prompt caching、code execution）→ MCP（Model Context Protocol）→ Claude Code 與 Computer Use → workflows vs. agents。

幾件先知道會比較好的事：

- **需要 Python 基礎**。幾乎所有程式碼都寫在 Jupyter notebook 裡執行，你需要一個能跑 notebook 的 Python 環境，以及一組 Anthropic API key（金鑰）。
- 這是「動手做」的課，講師強調要**跟著影片一起寫程式**，光看是吸收不了的；卡住就直接問 Claude。
- 課程大多使用 **Claude Sonnet**（`claude-sonnet-4-0`），因為它在智力、速度、成本之間最平衡。
- 全課程講師反覆強調的一句話：**prompt evaluation 是最重要的一件事**。自己手動測十次覺得沒問題，不代表上了 production（正式環境）不會壞。

---

## 先記住這兩張表

### 表一：Claude 三個模型家族怎麼選

三個家族的核心能力（文字生成、寫程式、圖片分析）都一樣，差別只在**各自為什麼而優化**：

| 模型 | 優化方向 | 特性 | 適合場景 |
|---|---|---|---|
| **Opus** | 最高智力 | 支援 reasoning（推理），可獨立跑數小時的多步驟任務；延遲較高、最貴 | 需要大量規劃的複雜任務 |
| **Sonnet** | 平衡 | 智力、速度、成本三者平衡；擅長寫程式、能精準修改複雜 codebase 而不弄壞既有功能 | 大多數實務應用的預設選擇 |
| **Haiku** | 速度與成本 | 最快、最便宜；**不支援 reasoning** | 需要即時回應的使用者介面、高流量處理 |

實務上團隊常**混用**：Haiku 處理面向使用者的即時互動、Sonnet 跑主要商業邏輯、Opus 留給真正需要深度推理的任務。

### 表二：Workflows vs. Agents——課程最後的核心抉擇

| | **Workflow（工作流程）** | **Agent（代理）** |
|---|---|---|
| 定義 | 預先設計好的一連串 Claude 呼叫，按固定步驟解決已知問題 | 給 Claude 一個目標和一組工具，讓它自己想辦法完成 |
| 何時用 | 你**事先就能畫出解題步驟**時 | 你**無法預知**使用者會丟什麼任務時 |
| 優點 | 每步聚焦、準確率高、容易測試與評估、行為可預測 | 彈性極大、能用工具的意外組合處理沒預想過的情境 |
| 缺點 | 不靈活、只能解特定問題 | 完成率較低、難以測試與監控、行為較不可預測 |

課程的明確建議：**能用 workflow 就用 workflow，真的必要才用 agent**。使用者不在乎你的 agent 多炫，只在乎產品穩不穩。

---

## 各單元內容導讀

### 單元 1：Course introduction——模型總覽

開場介紹課程路線與上面表一的三模型選擇框架。判斷方式很簡單：想清楚你的應用**最在乎什麼**——智力選 Opus、速度選 Haiku、要平衡選 Sonnet。

### 單元 2：Accessing Claude with the API——API 基礎

這是全課程的地基，內容最多，拆開來看：

**（1）Request 的完整生命週期。** 每次互動都走五步：client（客戶端）→ 你的 server（伺服器）→ Anthropic API → 回到 server → 回到 client。關鍵觀念：**絕對不要從前端程式直接呼叫 Anthropic API**，因為 request 需要秘密 API key，放在 client 端等於公開讓人盜用。模型內部處理則分四階段：tokenization（把文字切成 token，即模型處理的最小文字單位）→ embedding（把 token 轉成代表語意的數字向量）→ contextualization（依上下文修正語意）→ generation（逐 token 生成輸出）。

**（2）第一個 request。** 用官方 Python SDK（軟體開發套件），API key 放在 `.env` 檔（記得加進 `.gitignore`）：

```python
from anthropic import Anthropic
client = Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-0",
    max_tokens=1000,
    messages=[{"role": "user", "content": "What is quantum computing?"}]
)
message.content[0].text  # 取出生成的文字
```

容易搞混的點：`max_tokens` 是**安全上限，不是目標長度**。Claude 只會寫它覺得該寫的量，碰到上限才被截斷。

**（3）Multi-turn conversations（多輪對話）。** 最重要的觀念：**API 是 stateless（無狀態）的，Claude 完全不記得上一次對話**。要讓它「記得」，你必須自己維護一份 message list，每次 request 都把完整歷史送過去——user message 和 assistant message 輪流堆疊。課程寫了三個貫穿全課的 helper：`add_user_message()`、`add_assistant_message()`、`chat()`。

**（4）System prompts（系統提示詞）。** 用 `system` 參數給 Claude 一個角色與行為準則，例如「你是有耐心的數學家教，不直接給答案，一步步引導」。同一個問題，有沒有 system prompt 的回答天差地遠。練習題示範：只加一句 `system="You are a Python engineer who writes very concise code."` 就能把冗長的程式碼輸出變得極精簡。

**（5）Temperature（溫度）。** 0 到 1 的小數，控制選字的隨機程度：接近 0 幾乎總是挑機率最高的 token（穩定、可預測），接近 1 機率分布攤平（多樣、有創意）。

| 範圍 | 適用 |
|---|---|
| 0.0–0.3 | 事實問答、寫程式、資料萃取、內容審核 |
| 0.4–0.7 | 摘要、教學內容、問題解決 |
| 0.8–1.0 | brainstorming、創意寫作、行銷文案 |

注意：高 temperature 不**保證**輸出不同，它只改變機率。

**（6）Response streaming（串流回應）。** 一次生成可能要 10–30 秒，讓使用者盯著轉圈很糟。加上 `stream=True` 後 API 會以一連串 event 送回文字碎片（`MessageStart`、`ContentBlockDelta`、`MessageStop` 等）。SDK 有簡化介面：

```python
with client.messages.stream(model=model, max_tokens=1000, messages=messages) as stream:
    for text in stream.text_stream:
        print(text, end="")
    final_message = stream.get_final_message()  # 串流完仍可拿到完整訊息
```

**（7）Structured data（結構化輸出）——本單元最實用的技巧。** Claude 天生愛加解說文字，但你常常只要乾淨的 JSON。解法是 **assistant message prefilling（預填）＋ stop sequences（停止序列）** 的組合拳：

```python
add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")          # 預填：讓 Claude 以為自己已開了 code block
text = chat(messages, stop_sequences=["```"])       # 它想關閉 code block 時立刻停止
```

練習題進一步示範：prefill 不限於符號，可以直接預填一整句引導文字（如 "Here are all three commands in a single block without any comments:"）——**prefill 是強迫輸出格式最有力的槓桿**。

### 單元 3：Prompt evaluation——先學會量測，再談改進

講師視為全課最重要的單元。寫完 prompt 後你有三條路：測一次就上線（會炸）、手測幾次修修補補（還是會炸）、或**跑一條 evaluation pipeline 拿到客觀分數再迭代**。課程教你自己動手蓋第三條路，五個步驟：

1. **Draft a prompt**：寫初版 prompt。
2. **Create an eval dataset**：準備測試輸入集。可以手寫，也可以**用 Claude 生**（此時用便宜快速的 Haiku 就好）——生成時同樣用 prefill＋stop sequence 拿乾淨 JSON，存成 `dataset.json`。
3. **Feed through Claude**：把每筆測資塞進 prompt 模板、送給 Claude。
4. **Feed through a grader（評分器）**：對每個輸出打 1–10 分，算平均。
5. **Change prompt and repeat**：改 prompt、重跑、比分數。

Grader 有三種，各有適用場景：

| 類型 | 做法 | 適合檢查 |
|---|---|---|
| **Code grader** | 用程式邏輯驗證 | 輸出長度、格式、JSON/Python/regex 語法是否合法 |
| **Model grader** | 再用一個模型當評審 | 品質、是否遵循指示、完整度、有用性 |
| **Human grader** | 人工審 | 最靈活但最耗時 |

Model grader 的關鍵訣竅：**別只要分數，要同時要求 strengths、weaknesses、reasoning**——不給脈絡，模型評分會傾向給出無意義的中間值（6 分左右）。練習題再加一招：在生成測資時就順便產生 `solution_criteria`（好答案的判準），再把它插進 grader 的 prompt，評分理由會明顯變扎實。

### 單元 4：Prompt engineering——四招把 2.3 分變 9.5 分

方法論是迭代循環：設目標 → 寫初版 → 評估 → 套技巧 → 再評估。課程用「幫運動員排一日餐單」的例子，展示每招對 eval 分數的實際影響：

1. **Being clear and direct（清楚直接）**：prompt 第一行最重要。用祈使句、動作動詞開頭（Write / Create / Generate），別用模糊的問句。範例從 "What should this person eat?" 改成 "Generate a one-day meal plan for an athlete that meets their dietary restrictions."，分數 2.32 → 3.92。
2. **Being specific（具體明確）**：兩種手段——**output quality guidelines**（列出輸出該有的性質：長度、格式、必含元素）幾乎每個 prompt 都該有；**process steps**（列出思考步驟）用在複雜問題。加上六條 guidelines 後分數 3.92 → 7.86。
3. **Structure with XML tags（用 XML 標籤劃界）**：prompt 裡混了大量資料時，用 `<sales_records>`、`<my_code>`、`<docs>` 這類自訂標籤把「指令」和「資料」清楚隔開。標籤名稱越具體越好。
4. **Providing examples（給範例，one-shot / multi-shot prompting）**：給輸入/輸出配對示範，特別適合處理 corner case（例如反諷語氣的情感判斷）、定義複雜輸出格式。訣竅：從 eval 裡挑最高分的輸出當範例，並**解釋這個範例為什麼好**。

綜合練習（從學術文章段落萃取主題成 JSON array）示範了正確的除錯順序：**先開 report.html 看 grader 的 reasoning 再動手**，光是第一招「清楚直接」就把 2.8 分拉到 9.5。

### 單元 5：Tool use with Claude——課程份量最重的單元

Claude 預設只知道訓練資料裡的東西。tool use 讓它能以結構化方式**請你的程式**去拿外部資料或執行動作。專案是做一個提醒（reminder）系統，需要三個工具：`get_current_datetime`、`add_duration_to_datetime`、`set_reminder`。

完整流程（務必記熟，這是後面 MCP 與 agent 的基礎）：

1. 你送出問題＋**tool schema**（用 JSON Schema 描述每個工具的名稱、用途、參數）。
2. Claude 判斷需要工具，回覆一個含 **ToolUse block** 的 assistant message（`stop_reason` 會是 `"tool_use"`）。
3. 你的程式執行對應函式，把結果包成 **tool_result block** 放進 user message 送回去——`tool_use_id` 必須對上 ToolUse block 的 id。
4. Claude 拿到結果，生成最終回答（或再要求下一個工具，形成多輪循環）。

實作上的重點與陷阱：

- **Tool function 要驗證輸入、丟出有意義的錯誤訊息**——Claude 看得到 error，可能會修正參數重試。錯誤時 tool_result 設 `is_error: True`，千萬不要讓整個 loop 崩掉。
- **Tool schema 可以請 Claude 幫你寫**：把函式原始碼加上官方 tool use 文件丟給它，要求產出符合最佳實務的 JSON schema。description 建議 3–4 句，講清楚工具做什麼、何時用、回傳什麼。
- 對話 loop 的骨架：`while True` → 呼叫 API → append assistant message → 若 `stop_reason != "tool_use"` 就 break → 否則執行所有 tool 請求、append tool results、繼續。一個回應裡可能有**多個** ToolUse block，要逐一處理。
- **後續 request 仍然要帶 tools 參數**，即使你預期 Claude 不會再呼叫工具。
- **Fine-grained tool calling**：streaming 模式下 API 預設會 buffer 並驗證 JSON，等一個完整的 top-level key-value 才吐出來，所以你會看到「停頓後突然一大段」。加 `fine_grained=True` 可以拿到最即時的碎片，但**JSON 驗證被關掉**，你的程式要自己處理不合法的 JSON。

兩個內建工具，差異容易混淆：

| 工具 | schema | 實作（執行端） |
|---|---|---|
| **Text editor tool**（`text_editor_20250124` / `str_replace_editor`） | 內建在 Claude，你只給一個小 stub | **你自己寫**——檢視、建立、取代、插入檔案內容的函式都要自己實作 |
| **Web search tool**（`web_search_20250305`） | 你給 stub | **Anthropic 伺服器端全包**，你完全不用實作 |

Web search 記得設 `max_uses` 限制搜尋次數，可用 `allowed_domains`（如 `["nih.gov"]`）把來源限制在權威網站；回應裡的 citation blocks 讓你能在 UI 中呈現引用來源。

### 單元 6：Retrieval Augmented Generation——讓 Claude 讀 800 頁文件

文件太大塞不進 prompt（塞得進也會又貴又慢又不準）時，RAG 的做法是：**預處理時把文件切塊（chunking），查詢時只挑最相關的塊放進 prompt**。

**Chunking 策略比較：**

| 策略 | 做法 | 優缺點 |
|---|---|---|
| **Size-based** | 固定長度切，加 overlap（重疊）避免切斷語意 | 最簡單可靠、任何文件都能用；但可能切斷句子，是 production 常見的預設選擇 |
| **Structure-based** | 依標題/段落切（如 Markdown 的 `## `） | 語意最完整；但只適用於格式有保證的文件 |
| **Sentence-based** | 先切句、再幾句一組 | 大多數文字文件的折衷選擇 |
| **Semantic-based** | 用 NLP 判斷相鄰句子的相關性再分組 | 品質最好但計算成本最高 |

**Semantic search（語意搜尋）與 embeddings。** embedding 是一段文字的「語意數字化」——一長串 -1 到 1 之間的數字。Anthropic 本身不提供 embedding 服務，課程使用 **VoyageAI**（需另外註冊拿 API key，模型如 `voyage-3-large`）。流程：所有 chunk 先算好 embedding 存進 vector database（向量資料庫）→ 使用者提問時把問題也算成 embedding → 用 **cosine similarity（餘弦相似度）** 找最接近的 chunk → 把 chunk 和問題組成 prompt 給 Claude。

容易搞混：cosine **similarity** 越接近 1 越相似；cosine **distance** = 1 − similarity，越接近 **0** 越相似。看文件時先確認用的是哪一個。

**BM25 lexical search（詞彙搜尋）補語意搜尋的洞。** 語意搜尋對「INC-2023-Q4-011」這種精確代號很不可靠——它找的是「意思相近」不是「字面相同」。BM25 反過來：把查詢 tokenize、統計詞頻、**罕見詞給高權重**，精準命中含有特定術語、ID、代號的段落。

**Multi-Index pipeline：兩者合體。** 讓 VectorIndex 和 BM25Index 共用相同介面（`add_document()` / `search()`），包進一個 `Retriever`，同時查兩邊，再用 **RRF（Reciprocal Rank Fusion）** 合併排名：

```
RRF_score(d) = Σ( 1 / (k + rank_i(d)) )
```

在兩種索引都排前面的文件自然浮到最上面。這個架構的好處是可擴充——之後想加任何新索引，只要實作同一組介面即可。

### 單元 7：Features of Claude——六個進階功能

**Extended thinking（延伸思考）。** 讓 Claude 先在「草稿紙」上推理再作答，回應會多出 thinking block。啟用方式：

```python
params["thinking"] = {"type": "enabled", "budget": thinking_budget}
```

規則與陷阱：budget 最小 **1024** tokens，且 `max_tokens` 必須大於 budget；thinking tokens 要付費、延遲增加；thinking block 附有 cryptographic signature（加密簽章），**不可竄改**；偶爾會收到 redacted thinking（被安全系統加密遮蔽的思考），程式要能優雅處理。**與 message prefilling、temperature 等功能不相容**。使用時機的判斷很務實：先把 prompt 優化到底、跑 eval，準確率還是不夠才開 thinking。

**Image support（圖片）。** 在 user message 裡放 image block（base64 或 URL）。限制：單一 request 最多 100 張、每張 5MB；token 計費約 `(寬 × 高) / 750`。重點：**對圖片一樣要做 prompt engineering**——「數一下彈珠有幾顆」常會數錯，給它一套逐步方法論（先逐顆編號、再換個方向驗算）準確率大增。課程給了一個完整的實戰範例：用衛星影像做房屋火險評估的五步驟結構化 prompt。

**PDF support。** 與圖片幾乎相同，改用 `"type": "document"`、`media_type: "application/pdf"`。Claude 能理解 PDF 裡的文字、圖表、表格與結構。

**Citations（引用）。** 在 document block 加上 `"citations": {"enabled": True}` 和 `title`，Claude 的回答就會帶引用資訊：`cited_text`、`document_title`、起訖頁碼（純文字來源則是字元位置）。用途是把 Claude 從黑盒子變成「會標明出處的研究助理」。

**Prompt caching（提示詞快取）——最重要的成本優化。** Claude 每次都要對輸入做大量前處理，做完即丟；快取讓後續 request 重用這些工作，更快也更便宜。規則整理：

- **不是自動的**——要在 block 上手動加 `"cache_control": {"type": "ephemeral"}`，該 breakpoint（快取斷點）**之前**的所有內容才會被快取。
- 命中條件嚴苛：內容必須**一字不差**，多加一個 "please" 就整段失效。
- 快取只活 **1 小時**；被快取的內容合計至少 **1024 tokens**。
- 最多 **4 個** breakpoints；處理順序固定為 **tools → system → messages**，所以最佳候選是很少變動的 tool schemas 和 system prompt。
- 從回應的 `cache_creation_input_tokens`（寫入）與 `cache_read_input_tokens`（讀取）可以驗證快取是否生效。

**Code execution ＋ Files API。** Code execution 是伺服器端工具（給 schema `{"type": "code_execution_20250522", "name": "code_execution"}` 即可，不用實作），讓 Claude 在隔離的 Docker container 裡執行 Python；container **沒有網路**，所以要靠 Files API 把資料送進去：先上傳檔案拿到 file ID，訊息裡放 `container_upload` block 引用。典型應用：丟一個 CSV 請 Claude 做完整的 churn（流失）分析並產出圖表，生成的檔案再用 Files API 下載回來。

### 單元 8：Model Context Protocol——別人寫好的工具，接上就能用

**MCP 是什麼？** 一個通訊協定層，把「定義與執行工具」的負擔從你的 server 移到專門的 MCP server。想接 GitHub？不用自己寫幾十個 tool schema 和函式，接上現成的 GitHub MCP server 就好。

最常見的誤解，課程特別澄清：**MCP 不是 tool use 的替代品，兩者互補**。tool use 是 Claude 呼叫工具的機制；MCP 解決的是「**誰來寫和維護這些工具**」——MCP server 裡已經有人幫你寫好了。

**架構與訊息流。** 你的應用程式裡跑一個 MCP client，透過 stdio 或 HTTP 等傳輸方式（transport agnostic，不挑通訊方式）連到 MCP server。核心訊息就兩對：`ListToolsRequest/Result`（問有哪些工具）和 `CallToolRequest/Result`（執行某個工具）。你的 server 先向 MCP client 要工具清單、連同使用者問題送給 Claude；Claude 要求呼叫工具時，再透過 MCP client 轉給 MCP server 執行。

**用 Python SDK 寫 MCP server 非常簡單**——decorator（裝飾器）＋型別註記，JSON schema 自動生成：

```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("DocumentMCP")

@mcp.tool(name="read_doc_contents", description="Read the contents of a document...")
def read_document(doc_id: str = Field(description="Id of the document to read")):
    ...
```

開發時用內建的 inspector 測試：`mcp dev mcp_server.py` 會開一個瀏覽器介面，不用接上完整應用就能單獨測工具、資源與 prompt。

**MCP 的三種 primitives（基本元件），用「誰控制」來記：**

| Primitive | 誰控制 | 用途 | 課程對應的 Claude.ai 例子 |
|---|---|---|---|
| **Tools** | **model controlled**——Claude 自己決定何時呼叫 | 幫 Claude 加能力 | 「用 JavaScript 算 3 的平方」 |
| **Resources** | **app controlled**——你的應用程式碼決定何時取用（類似 HTTP GET；分 direct 如 `docs://documents` 與 templated 如 `docs://documents/{doc_id}`） | 把資料拿進 app（UI autocomplete、@mention 注入文件內容） | 「add from Google Drive」的文件清單 |
| **Prompts** | **user controlled**——使用者點按鈕或打 slash command 觸發 | 預先寫好、測試過的高品質工作流程 | 聊天輸入框下的建議按鈕 |

一句話總結：**tools 服務 model、resources 服務 app、prompts 服務 user。**

### 單元 9：Anthropic apps——Claude Code 實戰

這個單元把 Claude Code（跑在終端機的 agentic coding assistant）當成「agent 的活教材」。

- 安裝：`npm install -g @anthropic-ai/claude-code`，執行 `claude` 登入。
- **`/init`**：掃描整個 codebase，產出 `CLAUDE.md`——之後每次對話自動帶入的專案脈絡（分 project / local / user 三種 scope）。用 `#` 開頭可以隨手把準則寫進去。
- **最有效的工作流是三段式**：先餵 context（請它讀相關檔案）→ 要求**先規劃、明說先不要寫 code** → 確認計畫後才實作。也可以走 TDD（測試驅動）版本：想測試案例 → 寫測試 → 寫通過測試的程式。
- Claude Code 內建 MCP client，`claude mcp add <名稱> <啟動指令>` 就能外掛工具。課程列舉的熱門整合：sentry-mcp（自動修 production bug）、playwright-mcp（瀏覽器自動化）、mcp-atlassian（Confluence/Jira）、slack-mcp 等——把你既有的開發流程整套接給 Claude。

### 單元 10：Agents and workflows——收尾的架構課

先回到表二的抉擇，然後給了三個可直接套用的 **workflow patterns（工作流程模式）**，外加 agent 設計的兩條心法：

**Workflow patterns：**

| Pattern | 做法 | 適用時機 |
|---|---|---|
| **Evaluator-Optimizer** | Producer 產出 → Grader 評分 → 不合格就帶著回饋重做，直到通過 | 產出品質需要迭代收斂（例：從零件照片生成 3D 模型再對照原圖評分） |
| **Parallelization** | 同一任務拆成多個**平行**子任務（各有專屬 prompt/判準），最後彙整 | 複雜決策可拆成獨立面向（例：同一張零件圖分別用金屬/聚合物/陶瓷各自的判準評估，再彙整選材） |
| **Chaining** | 大任務拆成**依序**的小步驟，步驟之間還能插非 LLM 處理 | 單一長 prompt 老是漏掉某些限制時——先讓它寫，再用第二步專門修（移除 AI 自稱、刪 emoji、修語氣） |
| **Routing** | 先用一次 Claude 呼叫把輸入分類，再送進該類別專屬的 pipeline | 不同類型的請求需要不同處理（例：教學型 vs. 娛樂型影片腳本） |

**Agent 設計心法：**

1. **工具要抽象、可組合，不要過度特化。** Claude Code 只有 `bash`、`read`、`write`、`edit`、`glob`、`grep` 這類泛用工具，沒有「refactor code」這種特化工具——複雜任務由 Claude 自己組合基本工具完成，這正是它能處理開發者沒預想過的情境的原因。
2. **Environment inspection（環境檢視）：Claude 是盲的，要讓它看得到自己動作的結果。** Computer Use 每次點擊後都回傳截圖；改檔案前先讀檔；影片生成 agent 可在 system prompt 裡要求它用 whisper.cpp 產字幕驗證對白位置、用 FFmpeg 抽畫格檢查畫面。設計 agent 時永遠自問：「Claude 怎麼知道這步有沒有成功？」

### 單元 11：Wrap up——講師的臨別提醒

重點重申：**prompt evaluation 是你最該帶走的一件事**，而且 eval 不必用什麼大框架——課程用的評估工具本身大部分就是 Claude 寫的。prompt engineering 眾多技巧中最重要的仍是清楚直接。agent 很迷人，但 **workflow 往往給你更好的結果和更高的準確率**。建議自修的延伸主題：agent orchestration（多 agent 協作）、agent 的評估與監控、agentic RAG、RAG evaluation，以及 tool evaluation（用 eval 的思路驗證你的工具描述真的有幫到 Claude）。

---

## 讀完這門課你會得到什麼

一句話總結：**從「會呼叫 API」升級到「能把 Claude 做成可靠的產品功能」。**

- 一套完整的 API 基本功：stateless 對話管理、system prompt、temperature、streaming，以及 prefill＋stop sequences 這個控制輸出格式的殺手鐧。
- 一條自己蓋得起來的 **prompt evaluation pipeline**（dataset 生成 → 跑 prompt → grader 評分 → 迭代），和四招經過分數驗證的 prompt engineering 技巧。
- 完整的 **tool use** 實作能力：schema、多輪工具循環、錯誤處理，以及 text editor / web search / code execution 三種內建工具的正確用法。
- 一套可上手的 **RAG** 工法：chunking 策略選擇、embeddings＋BM25 雙索引、RRF 融合排名。
- 成本與品質的進階槓桿：prompt caching 的精確規則、extended thinking 的取捨、citations 帶來的可驗證性。
- **MCP** 的雙邊視角（會寫 server 也會寫 client），和「tools/model、resources/app、prompts/user」這個選型口訣。
- 最後也是最值錢的：**workflows vs. agents 的判斷力**，加上四個現成的 workflow patterns 當作日後設計功能的食譜。

如果你是要準備 Anthropic 相關認證、或是團隊裡負責把 Claude 整合進產品的工程師，這門課就是那條從 hello world 到 production 思維的完整路徑。
