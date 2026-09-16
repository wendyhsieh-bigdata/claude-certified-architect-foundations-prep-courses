# Claude on Google Cloud — 課程導讀

> 原始筆記：`../Claude_on_Google_Cloud.md`
> 對象：**還沒看過這門課的人**。讀完這份導讀，你就能掌握課程在教什麼、核心觀念是什麼、以及可以馬上套用的做法。專有名詞保留英文，第一次出現時附中文解釋。

---

## 這門課在講什麼

這是 Anthropic 的技術人員 Stephen Grider 主講的一門**動手實作課**，主題是：如何透過 Google Cloud 的 **Vertex AI**（Google Cloud 上的 AI 平台服務）呼叫 Claude 模型，並一路從最基本的 API 呼叫，蓋到 production 等級的 AI 應用。

課程的完整路線是：認識 Anthropic 的模型家族 → 透過 Vertex AI 呼叫 API → **prompt evaluation**（提示詞評測）→ **prompt engineering**（提示詞工程）→ **tool use**（工具呼叫）→ **RAG**（Retrieval Augmented Generation，檢索增強生成）→ **MCP**（Model Context Protocol）→ Anthropic 自家的兩個應用 **Claude Code** 與 **Computer Use** → 最後收在 **agent 與 workflow** 的設計模式。

上課前需要知道的事：

- **需要基本的 Python 能力**，以及能跑 notebook（如 Jupyter）的環境——課程幾乎所有程式碼都寫在 notebook 裡。
- 需要一個能使用 Vertex AI 與 Anthropic 模型的 Google Cloud 帳號。
- 課程大多數示範使用 **Claude Sonnet**（智慧、速度、成本最平衡）。
- 官方學習建議：跟著影片一起打程式碼、加速播放、自己改寫 notebook 做延伸、卡住就問 Claude。

這門課份量很足，但骨架清楚：**前半段教你「怎麼把 Claude 叫起來、怎麼確認它做得好」，後半段教你「怎麼把 Claude 接上外部世界、組成更大的系統」。**

---

## 先記住這兩張表，全課程就懂了一半

### 表一：Claude 的三個模型家族

三個家族核心能力相同（文字生成、寫程式、影像分析都會），差別只在**優化方向**：

| 模型 | 優化方向 | 特性 | 適合場景 |
|---|---|---|---|
| **Opus** | 最高智慧 | 能獨立執行數小時的多步驟任務；支援 reasoning（推理，簡單問題快答、困難問題深思）；延遲較高、成本較貴 | 需要大量規劃的複雜任務 |
| **Sonnet** | 平衡 | 智慧、速度、成本的甜蜜點；擅長寫程式、能精準修改複雜 codebase 而不弄壞既有功能 | 大多數實際應用的主要商業邏輯 |
| **Haiku** | 速度與成本 | 最快、最省；**不支援 reasoning** | 需要即時互動的使用者介面 |

實務上常在同一個應用裡混用：Haiku 對付面向使用者的即時互動，Sonnet 跑主要邏輯，Opus 處理真正困難的推理。

### 表二：Workflow vs Agent——課程最後的核心抉擇

| | **Workflow**（工作流） | **Agent**（代理） |
|---|---|---|
| 定義 | 由你**預先寫死步驟**的一連串 Claude 呼叫 | 給 Claude 一個目標和一組工具，**讓它自己想辦法** |
| 適用時機 | 你能事先想像出解題的確切步驟 | 你無法預知使用者會丟什麼任務進來 |
| 優點 | 每步聚焦、準確率高、容易測試評估 | 彈性極大、能以意想不到的方式組合工具 |
| 缺點 | 只能解特定類型的問題 | 成功率較低、難以測試與監控 |

課程的明確建議：**能用 workflow 就用 workflow，真的必要才用 agent**。使用者不在乎你的 agent 多炫，他們只要一個 100% 能動的產品。

---

## 各單元內容導讀

### 單元 1：Course introduction——模型總覽

開場介紹課程路線與三個模型家族（見表一）。選型軸線很簡單：一端是智慧（Opus，貴又慢一點），另一端是成本與速度（Haiku，智慧中等），Sonnet 在中間取平衡，依場景挑最重要的特質。

### 單元 2：Accessing Claude with the API——把 Claude 叫起來

這是全課程的地基，內容最多，分幾塊來看。

**（1）一次請求的完整生命週期。** 使用者輸入 → 你的 server → Vertex → 模型處理 → 回到 server → 回到 client。重點觀念：**永遠不要從 client 端（瀏覽器等）直接呼叫 API**——請求需要祕密憑證（credentials），寫在 client 程式碼等於公開，一定要經過你自己控制的 server。模型內部處理經過四個階段：**tokenization**（斷詞，把文字切成 token）→ **embedding**（把 token 轉成一長串數字）→ contextualization（依上下文調整語意）→ generation（逐 token 生成，直到碰到 max tokens 上限、自然結尾的 end-of-sequence token、或 stop sequence）。

**（2）Vertex AI 環境設定。** 到 Google Cloud Console 的 Vertex AI 頁面，進入 **Model Garden**（模型市集），搜尋「Anthropic」，點進模型按「Enable」啟用（沒有 Enable 按鈕代表已有權限）。接著安裝 gcloud CLI 並認證：

```bash
gcloud init
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```

之後 Anthropic SDK 會自動使用這組憑證。

**（3）第一個請求。** 安裝 SDK 要帶 vertex 附加元件：`%pip install "anthropic[vertex]"`，然後建立專用 client：

```python
from anthropic import AnthropicVertex

client = AnthropicVertex(region="global", project_id="your-project-id")
model = "claude-sonnet-4@20250514"
```

呼叫 `client.messages.create()` 需要三個關鍵參數：`model`、`max_tokens`、`messages`。**易搞混：`max_tokens` 是「預算」不是「目標」**——設 1000 不代表會寫滿，只代表超過就砍斷。取回文字用 `message.content[0].text`。

**（4）多輪對話。** 最重要的觀念：**Claude 完全不儲存對話歷史，每個請求都是獨立的**。想讓它「記得」前文，你必須自己維護 messages 清單（role 為 `user` 或 `assistant`），並且**每次請求都送完整歷史**。課程寫了三個貫穿全場的輔助函式：`add_user_message`、`add_assistant_message`、`chat`。

**（5）System prompt（系統提示詞）。** 透過 `system` 參數指定角色與行為準則（例如「你是有耐心的數學家教，不直接給答案，一步步引導」），不必動使用者的提問就能大幅改變回應風格。

**（6）Temperature（溫度）。** 0 到 1 的小數，控制隨機程度：低溫幾乎總是挑機率最高的 token（可預測），高溫把機率分散（有創意）。參考區間：

| 範圍 | 適用 |
|---|---|
| 0.0–0.3 | 事實性回答、寫程式、資料抽取、內容審核 |
| 0.4–0.7 | 摘要、教學內容、解題 |
| 0.8–1.0 | 腦力激盪、創意寫作、行銷文案 |

注意：temperature 只改變機率分布，**高溫也不保證每次輸出都不同**。

**（7）Streaming（串流回應）。** 完整回應可能要等 10–30 秒，開 `stream=True` 可以讓文字一塊塊送回來改善體驗。SDK 的簡化介面 `client.messages.stream(...)` 搭配 `for text in stream.text_stream:` 就能逐塊印出；結束後用 `stream.get_final_message()` 拿完整訊息物件供儲存。

**（8）控制輸出的兩把刀。** 一是 **message prefilling**（預填助手訊息）：在 messages 最後放一則 assistant 訊息當「開頭」，Claude 從那裡接著寫（預填「Coffee is better because」就會論證咖啡比較好）。二是 **stop sequences**：給一組字串，Claude 一生成到就停。兩招合體是課程的招牌技巧——**取得乾淨的結構化資料**：

```python
add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])
```

Claude 以為自己已經開始寫 markdown code block，只補中間的 JSON，寫到收尾的 ``` 就被停掉——你拿到的正好是純 JSON，沒有解說文字。這個 pattern 之後在 eval 與 grader 裡反覆使用。

### 單元 3：Prompt evaluation——別靠感覺，用數據改 prompt

課程的靈魂單元。寫完 prompt 有三條路：測一次就上線（風險最高）、手動測幾次修修補補（還是會漏）、或**跑一條 evaluation pipeline 拿客觀分數再迭代**。第三條前期成本較高，但你會「知道」而不是「猜」你的修改有沒有變好。

典型的 eval workflow 五步驟：

1. **Draft a prompt**：寫初版 prompt。
2. **Create an evaluation dataset**：準備測試輸入。可手工做，也可**請 Claude 自動生成**（產測資用 Haiku 就夠快夠省）——用 prefill＋stop sequence 拿回乾淨 JSON，存成 `dataset.json`。
3. **Feed through Claude**：把每筆測資合併進 prompt、送給 Claude、收集輸出。
4. **Feed through a grader**（評分器）：對每筆輸出打分（例如 1–10）再平均。
5. **Change prompt and repeat**：改 prompt、重跑、比分數。

Grader 有三種，各有用途、常常混用：

| 類型 | 做法 | 適合檢查 |
|---|---|---|
| **Code grader** | 用程式驗證 | 輸出長度、格式、語法是否合法（例如 `json.loads`、`ast.parse`、`re.compile` 三個驗證函式：解析成功給 10 分、失敗 0 分） |
| **Model grader** | 再呼叫一次模型來評分 | 回答品質、有沒有照指示、完整性、安全性 |
| **Human grader** | 人工看 | 什麼都能評，但最慢最累 |

Model grader 的實務要訣：**不要只要分數，還要要求 strengths、weaknesses、reasoning**，逼模型認真評估而不是通通給 6 分；並把「好解答的標準」（`solution_criteria`）生成在測資裡、插進 grader 的 prompt，評分理由會明顯更扎實。最後把 model 分數與 syntax 分數平均（或加權）成總分。

### 單元 4：Prompt engineering——有評測撐腰的改寫技巧

有了 eval，改 prompt 就變成「一次改一個地方、看分數有沒有上升」的科學過程。課程用「幫運動員產生一日餐飲計畫」的例子展示每招的威力：

1. **Being clear and direct（清楚直接）**：prompt 第一行最重要。用祈使句不用疑問句、用動作動詞開頭（Write、Create、Generate）。把「What should this person eat?」改成「Generate a one-day meal plan for an athlete that meets their dietary restrictions.」，分數就從 2.32 跳到 3.92。
2. **Being specific（具體明確）**：兩種做法——列出**輸出應有的品質**（quality guidelines，如「熱量要準確」「份量用公克」），或給**執行步驟**（process steps，如「先腦力激盪三個選項再挑一個」）。加了 guidelines 之後分數從 3.92 跳到 7.86。
3. **Structure with XML tags（用 XML 標籤結構化）**：prompt 裡塞大量資料時，用自訂標籤（如 `<sales_records>`、`<athlete_information>`）把「指示」和「資料」明確隔開，Claude 才不會搞混哪段是要分析的內容、哪段是說明文件。
4. **Providing examples（提供範例，one-shot / multi-shot prompting）**：直接示範理想輸入輸出，特別能治**邊角案例**——例如諷刺推文表面正面實則負面，給一個 `<sample_input>` / `<ideal_output>` 範例就能教會它。訣竅：從 eval 報告挑滿分輸出當範例，並附一句「為什麼這是好範例」。

### 單元 5：Tool use with Claude——讓 Claude 伸手碰外部世界

Claude 預設只知道訓練資料裡的東西，不知道現在幾點、也沒辦法真的「設一個提醒」。**Tool use** 是解法：你在請求裡描述可用的工具，Claude 判斷需要時「開口要求」你替它執行。

課程用「設定提醒」專案貫穿，需要三個工具：`get_current_datetime`（取得現在時間）、`add_duration_to_datetime`（日期加減——Claude 自己算日期常出錯，交給工具最可靠）、`set_reminder`。關鍵零件：

- **Tool function**：一般的 Python 函式。名稱要有描述性、驗證輸入、**錯誤訊息要有意義**——Claude 看得到錯誤內容，會據此修正參數重試。
- **Tool schema**：一份 JSON Schema，含 `name`、`description`（建議 3–4 句：做什麼、何時用、回傳什麼）、`input_schema`。偷吃步：把函式貼給 Claude、附上官方 tool use 文件，**請它幫你寫 schema**。
- **多區塊訊息**：帶著 `tools` 參數呼叫後，回應可能同時含 text block 與 **tool_use block**（含 id、工具名、輸入參數）。你執行工具後用 **tool_result block** 回傳結果，`tool_use_id` 必須對上原本的 id。
- **對話迴圈**：看回應的 `stop_reason` 是否等於 `"tool_use"`；是就執行工具、把結果加回 messages、再呼叫一次，直到它給出最終文字答案。這個 `while True` 迴圈就是後面「agent」的雛形。
- **Batch tool**：Claude 理論上能一次發多個 tool_use，實務上常一個一個來。解法是定義一個 `batch_tool`，參數是「一串工具呼叫」，鼓勵它打包平行執行，減少來回。
- **用工具取結構化資料**：比 prefill 更可靠——把要的資料結構寫成 tool schema，用 `tool_choice={"type": "tool", "name": "..."}` **強制**呼叫該工具，從 `response.content[0].input` 直接取出資料。`tool_choice` 三檔：`auto`（模型自行決定）、`any`（必須用某個工具）、`tool`（必須用指定工具）。
- **兩個內建工具，行為不一樣，容易搞混**：
  - **Text editor tool**（`type: "text_editor_20250124"`、`name: "str_replace_editor"`，版本隨模型而異）：schema 內建在 Claude 裡（你只送一小段 stub），但**實際的檔案讀寫程式碼要你自己寫**——檢視、取代、建立、插入、復原檔案，等於給 Claude 當軟體工程師的手。
  - **Web search tool**（`type: "web_search_20250305"`）：**整個搜尋由 Anthropic 端代勞**，完全不用實作，用 `max_uses` 限制搜尋次數、`allowed_domains`（例如 `["nih.gov"]`）限制來源網域。回應帶引用（citations），可做成能驗證來源的 UI。

### 單元 6：Retrieval Augmented Generation——大文件的正確打開方式

想針對一份 800 頁的財報問問題，把全文塞進 prompt 有三個問題：長度上限、prompt 越長效果越差、又貴又慢。**RAG** 的做法：預先把文件切塊（chunking），提問時**只找出相關的塊**放進 prompt。

**Chunking（切塊）三策略：**

| 策略 | 做法 | 取捨 |
|---|---|---|
| **Size-based** | 固定長度切，塊與塊之間留 overlap（重疊）避免句子被腰斬 | 最保險，但可能切掉語境（如標題） |
| **Structure-based** | 按文件結構切（如 markdown 的 `## ` 標題） | 結構一致時效果最乾淨，但很多文件沒有結構 |
| **Semantic-based** | 用 NLP 把語意相近的句子聚成塊 | 品質最高但最貴最複雜 |

切壞的代價很具體：醫學章節裡剛好出現「bug」一字，問「工程師今年修了幾個 bug」就可能撈到醫學內容。

**Embeddings（向量嵌入）。** 要找「語意相關」的塊，先把文字轉成一長串數字（每個數字介於 -1 到 1，代表模型學到的某種特徵——人類看不懂，但可以做數學比較）。**Claude 本身不會產生 embedding**，在 Vertex AI 上要用專門的 embedding 模型 **`text-embedding-005`**，透過 Google GenAI SDK（`pip install google-genai`）呼叫 `client.models.embed_content(...)`。

**完整 RAG 流程**：切塊 → 對每塊做 embedding → 存入 **vector database**（向量資料庫）→ 提問時把問題也 embedding → 用 **cosine similarity**（餘弦相似度）找最接近的塊 → 把問題＋相關塊組成 prompt 給 Claude。**易搞混**：cosine similarity 是 1 最像、-1 最不像；很多資料庫文件寫的是 **cosine distance** ＝ 1 − similarity，**數字越小越像**。

進階四招：

1. **BM25 lexical search（字面檢索）**：語意搜尋會漏掉「INC-2023-Q4-011」這種精確編號。BM25 依「詞在文件集中的稀有度」加權——罕見詞比 the、a 重要得多——專治精確比對。
2. **Multi-index pipeline＋RRF**：把 vector index 和 BM25 index 包進同一個 `Retriever`，平行查詢後合併。兩者分數制不同不能直接相加，改用 **Reciprocal Rank Fusion**（互惠排名融合）：只看名次不看分數，公式 `RRF_score(d) = Σ 1/(k + rank_i(d))`（k 通常取 60），兩邊都名列前茅的文件自然勝出。
3. **Reranking（重排序）**：搜尋結果再丟給 Claude 一次，請它依問題把最相關的 k 份文件 **id**（不傳全文，省時間）依相關度排序回傳。代價是多一次 LLM 呼叫的延遲與成本，換取更準的排序。
4. **Contextual retrieval（脈絡化檢索）**：切塊後每一塊都失去「我來自哪份文件的哪裡」的資訊。入庫前請 Claude 為每塊寫一小段脈絡說明，接在塊前面再索引。文件太大放不進 context window 時，用「文件開頭幾塊＋當前塊前面幾塊」當替代脈絡。

### 單元 7：Features of Claude——五個進階功能

**Extended thinking（延伸思考）。** 讓 Claude 先「想」再答，回應會多出一個 **thinking block**（思考區塊）＋原本的 text block。適用原則：**先用 eval 確認一般 prompt 優化已到瓶頸，再開 thinking**——思考的 token 也要收費、延遲也會變長。實作要點：`thinking_budget` 最小 1024 token，且 `max_tokens` 必須大於 budget（實務上留足餘裕，例如 budget 1024 配 max_tokens 4000）。每個 thinking block 帶一個**加密簽章**，確保放回對話歷史時內容沒被竄改；若思考內容被安全系統攔下，會改回傳 **redacted thinking**（加密後的思考內容）——不可讀，但仍應原封不動放回歷史。

**Image support（影像輸入）。** 在 user message 裡加 image block（base64 或 URL）。限制：單一請求最多 100 張圖、每張最大 5MB、單圖長寬上限 8000px（多圖時 2000px），token 消耗約 `寬 × 高 / 750`。**最重要的心得：視覺任務照樣吃 prompt engineering**——直接問「圖裡有幾顆彈珠」會數錯，給一套方法論（逐一編號、換方式驗算）或 one-shot 範例就會對。課程實戰範例是用衛星影像＋五步驟結構化 prompt，自動評估房屋的火災風險等級（1–4 級）。

**PDF support。** 與影像幾乎同一套程式碼，只把 block 的 `type` 改成 `document`、`media_type` 改成 `application/pdf`。Claude 不只讀文字，PDF 內的圖表、表格也讀得到。

**Citations（引用）。** 在 document block 加上 `"title"` 與 `"citations": {"enabled": True}`，回答就會附上結構化引用：`cited_text`（被引用的原文）、`document_title`、起迄頁碼（純文字文件則是字元位置）。適合需要讓使用者驗證出處的應用。

**Prompt caching（提示詞快取）。** Claude 每次都要對輸入做完整前處理，處理完就丟掉；對話式應用每輪都在重送同樣的歷史，等於重複付費。快取規則：

- 初次請求**寫入**快取，後續請求**讀取**快取；快取壽命 **5 分鐘**。
- 不會自動快取——要在 block 上手動放 **cache breakpoint**：`"cache_control": {"type": "ephemeral"}`（必須用 longhand 的 block 寫法），breakpoint 之前的內容都會被快取。
- 送進模型的順序固定是 **tools → system → messages**，breakpoint 放哪就快取到哪；最多 **4 個** breakpoint。最常見的快取對象是幾乎不變的 tool schema 和 system prompt。
- 被快取的內容合計**至少 1024 token**。
- **快取極度敏感：差一個字元就 miss**。從 `usage` 的 `cache_creation_input_tokens` / `cache_read_input_tokens` 可觀察寫入與命中。

### 單元 8：Model Context Protocol——工具的「外包」協定

**MCP 是一個通訊層**：與其自己為 GitHub 之類的服務手寫幾十個 tool schema 和函式，不如連上一台別人（往往是服務商自己）寫好的 **MCP server**，工具的定義與執行都包好了；你的應用程式扮演 **MCP client**。**易搞混：MCP 不是 tool use 的替代品**——tool use 是 Claude「怎麼呼叫工具」的機制，MCP 解決的是「工具由誰來寫、誰來維護」。

client 與 server 之間 transport agnostic（不限傳輸方式）：同機常用 standard input/output，也可走 HTTP、WebSocket。主要訊息兩對：`ListToolsRequest/Result`（問有哪些工具）與 `CallToolRequest/Result`（執行工具）。

課程用一個 CLI 文件聊天機器人同時實作兩端（實務上通常只寫一端，這裡是教學目的）。用官方 Python SDK 寫 server 非常省力：

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")

@mcp.tool(name="read_doc_contents", description="Read the contents of a document...")
def read_document(doc_id: str = Field(description="Id of the document to read")):
    ...
```

裝飾器（decorator）＋型別提示就能自動生出完整 JSON schema，不必手寫。開發時用內建的瀏覽器版 inspector（`mcp dev mcp_server.py`）直接列出並試跑工具、resources、prompts。

MCP server 有三種 primitive（基本元件），**用「誰控制它」來記最不會混**：

| Primitive | 由誰控制 | 用途 | 例子 |
|---|---|---|---|
| **Tools** | 模型（Claude 自己決定何時呼叫） | 擴充 Claude 的能力 | 讀取、編輯文件 |
| **Resources** | 你的應用程式碼 | 把資料拿進 app（做 UI、補脈絡），類似 HTTP 的 GET | `@` 提及文件時的自動完成清單；直接把文件內容塞進 prompt |
| **Prompts** | 使用者（按鈕、slash 指令觸發） | 預先打磨好的高品質提示詞工作流 | `/format doc_id` 把文件重排成 Markdown |

Resources 分兩種：**direct resource**（固定 URI，如 `docs://documents`）與 **templated resource**（URI 帶參數，如 `docs://documents/{doc_id}`），並用 `mime_type` 提示回傳的資料型態。

### 單元 9：Anthropic apps——Claude Code 與 Computer Use

**Claude Code** 是跑在終端機的 coding assistant。心法先於操作：**別把它當成「幫你打字的工具」，把它當成共事的工程師**——專案設定、功能規劃、寫測試、部署、維運都能整包委派。重點：

- 安裝：裝 Node.js、`npm install` 安裝 Claude Code、設三個環境變數（詳見 docs.anthropic.com）。
- **`/init`** 指令掃描 codebase，把架構、常用指令、程式風格寫進 **`CLAUDE.md`**，之後每次啟動都自動當作 context 帶入。輸入 `#` 加一句話可把備註寫進三種記憶範圍之一：**project / local / user**（要與團隊共享就選 project memory）。
- **Claude Code 是效果放大器（effort multiplier）**：隨便下指令它也會盡力，但多給一點結構回報會好很多。課程示範兩套工作流：
  1. **讀檔 → 規劃 → 實作**：先指名相關檔案要它讀，再描述功能並要求「**先規劃、不要寫程式**」，最後才叫它實作。示範中它還自己補上了沒被要求的錯誤處理。
  2. **測試驅動開發（TDD）**：先 `/clear` 清掉 context（免得抄前一次的答案），要它先提出候選測試（一樣先不寫程式），你挑出有用的幾個實作，再要求「寫程式直到測試全過」。
- **接上 MCP server 動態擴充能力**：`claude mcp add documents "uv run main.py"`——Claude Code 內建 MCP client，馬上能用你剛寫好的工具。實務上值得接的 server：Sentry（撈 production 錯誤）、Jira（讀 ticket）、Slack（做完通知你）。
- **平行化**：多個 Claude Code 同時改同一份檔案會打架，解法是 **git worktree**——每個 worktree 是專案在獨立目錄的完整副本、對應一條 branch，各實例在隔離環境工作，完成後像普通 branch 一樣 merge 回 main。繁瑣流程可做成**自訂 slash 指令**：把 prompt 存進 `.claude/commands/createWorkTree.md`，用 `$ARGUMENTS` 佔位，之後 `/project:createWorkTree feature_B` 一行搞定。課程示範四個 worktree 平行開發四個功能，merge 衝突 Claude 自己解掉了。
- **自動化除錯**：一個只在 production 壞掉的 bug（本機正常、部署到 AWS Amplify 後試算表回傳空白），交給每天凌晨排程的 **GitHub Action**：checkout 專案 → 安裝 Claude Code 與 AWS CLI → 請 Claude 從 CloudWatch 撈出過去 24 小時的錯誤（去重、縮減到 context window 塞得下）→ 逐一嘗試修復 → commit 並**自動開 pull request**。示範中的根因是 production 專用的 model ID 打錯字。這個「監控—修復」pattern 可以自由改造。

**Computer Use** 讓 Claude 操作電腦畫面。示範場景是自動化 QA：一個支援 `@` 提及的文字框元件，按 Backspace 時自動完成選單會跑到螢幕左上角。把測試計畫（三個 test case＋要求最後給簡明報告）交給 Claude，讓它操作跑在 **Docker container 裡的隔離瀏覽器**逐一驗證——結果測試 1、2 通過、3 失敗，直接指出要查哪裡。

**它的原理就是 tool use，沒有魔法**：你送出一小段特殊 schema，背後被展開成一個大 schema，告訴 Claude 可以呼叫帶 `mouse_move`、`left_click`、`screenshot` 等動作的 action 函式。**Claude 從未直接操作電腦**——它只發出 tool_use 請求，由你提供實際執行鍵鼠操作的環境。Anthropic 有現成的 reference implementation（Docker container），跑一條 Docker 指令就能得到示範中的聊天＋瀏覽器介面。

### 單元 10：Agents and workflows——組合出更大的系統

**Workflow** 是預先定義好的一連串 Claude 呼叫。課程整理了四個可複用的 pattern：

| Pattern | 做法 | 適用時機 |
|---|---|---|
| **Evaluator-optimizer** | Producer 產出 → Grader 評分 → 不合格就帶回饋重做，直到通過 | 輸出品質可以被客觀檢驗時（例：影像轉 CAD 模型，渲染圖與原圖比對評分） |
| **Parallelization** | 把複雜任務拆成多個特化子任務**平行**執行，最後由一個 aggregator 請求彙整 | 一個 prompt 要同時顧太多面向時（例：對六種材質各跑一個專屬分析，最後比較） |
| **Chaining** | 把大任務拆成**依序**的小步驟，步驟間還能插入非 LLM 的處理 | Claude 老是違反你的一長串「不准…」限制時——第一步先產出、第二步用聚焦的修訂 prompt 專門清理（去 emoji、去 AI 自白、修語氣） |
| **Routing** | 先用一次呼叫替輸入分類，再送進該類別的專屬 pipeline | 應用要處理明顯不同類型的請求（教學型 vs 娛樂型腳本），能定義出 3–10 個有意義的類別時 |

**Agent** 則是「給目標與工具，路徑自己想」。兩條最佳實務：

1. **工具要適度抽象**。Claude Code 就是典範：它只有 `bash`、`glob`、`grep`、`read`、`write`、`edit`、`webfetch` 這類通用工具，**沒有**「Refactor」「Run Tests」這種特化工具——安裝依賴是它自己讀專案設定檔再用 bash 跑指令完成的。通用工具才能被創意組合。
2. **Environment inspection（環境觀察）**。Claude 是「盲的」，每個動作之後都需要觀察結果：computer use 每次操作後自動回傳截圖；改程式前先讀檔案現況；影片生成 agent 可在 system prompt 裡指示它用 whisper.cpp 產字幕驗證對白時間、用 FFmpeg 抽截圖確認品質。**每個動作之後都應該跟著某種驗證。**

單元收尾回到表二的抉擇：workflow 準確、可測；agent 彈性、難測。**預設選 workflow，必要才上 agent。**

### 單元 11：Wrap up——回顧與延伸

講師的收尾重點：全課程**最重要的習慣是 prompt evaluation**——手動跑十次覺得沒問題不算數，production 使用者一定會打出你沒看過的結果；而且 eval 不必用大框架，課程用的評測工具大半就是請 Claude 自己寫的。prompt engineering 諸多技巧中，最關鍵的仍是清楚直接。建議自學方向：agent orchestration（多 agent 協作）、agent 的評估與監控、agentic RAG、RAG evaluation，以及 tool evaluation（用 eval 的思路驗證工具描述真的有幫到 Claude）。

---

## 讀完這門課你會得到什麼

一句話總結：**從「會呼叫 Claude API」進化到「能在 Google Cloud 上把 Claude 組進一個可靠的系統」。**

- Vertex AI 上的完整起手式：Model Garden 啟用模型、gcloud 認證、`AnthropicVertex` client、多輪對話的正確寫法。
- 立刻可用的輸出控制技巧：system prompt、temperature、streaming、message prefilling＋stop sequences 取乾淨結構化資料。
- 一條自己就能搭起來的 **eval pipeline**（資料集生成 → 跑 prompt → code/model grader 打分 → 迭代），以及有數據佐證的四大 prompt engineering 技巧。
- 完整的 **tool use** 開發能力：schema、對話迴圈、batch tool、`tool_choice` 強制結構化輸出、text editor 與 web search 兩個內建工具。
- 從基本到進階的 **RAG** 路線：chunking → embedding（`text-embedding-005`）→ vector search → BM25 → RRF 混合檢索 → reranking → contextual retrieval。
- Claude 的進階功能地圖：extended thinking、影像、PDF、citations、prompt caching 的完整規則。
- **MCP** 的兩端實作經驗與三種 primitive 的取捨（tools 服務模型、resources 服務 app、prompts 服務使用者）。
- 把 **Claude Code** 用成團隊戰力的工作流（`/init`、CLAUDE.md、TDD、git worktree 平行開發、CI 自動修 bug），以及 Computer Use 的原理。
- 四個 workflow pattern 與 agent 設計原則，還有那條最重要的工程判斷：**能 workflow 就不要 agent。**

如果你是要在 GCP 環境導入 Claude 的工程師，這門課幾乎就是官方路線圖；就算你用的是 Anthropic 直連 API 或其他雲，除了 Vertex 設定那一小段，其餘內容全部通用。
