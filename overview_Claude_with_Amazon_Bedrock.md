# Claude with Amazon Bedrock — 課程導讀

> 原始筆記：`../Claude_with_Amazon_Bedrock.md`
> 對象：**還沒看過這門課的人**。讀完這份導讀，你就能掌握課程在教什麼、核心觀念是什麼、以及可以馬上套用的做法。專有名詞保留英文，第一次出現時附中文解釋。

---

## 這門課在講什麼

這是 Anthropic 為合作夥伴開設的實作課，主題是：**如何透過 Amazon Bedrock（AWS 上的託管生成式 AI 服務）用程式呼叫 Claude，一路做到可上線的 AI 應用**。課程用 Python 加 **boto3**（AWS 官方 Python SDK）在 Jupyter notebook 裡動手寫程式，從「發出第一個 API request」開始，逐步疊加到多輪對話、提示詞評測、tool use（工具使用）、RAG（Retrieval Augmented Generation，檢索增強生成）、MCP（Model Context Protocol）與 agent（代理）。知識密度非常高，講師自己在結尾都說「這門課的內容抵得上三、四門課」。

課程有一條主軸貫穿所有模組：

> **寫 prompt 只是起點，「用客觀數據評測 prompt」才是可靠 AI 應用的基礎。** 課程結尾再三強調：evaluations（評測）絕對不能省，「不要讓客戶說服你跳過它」。

全課程共十個部分：課程介紹（模型家族）、Working with the API、Prompt evaluations、Prompt engineering、Tool use、Retrieval Augmented Generation、Features of Claude、Model Context Protocol、Agents，最後是總結，各配有練習與測驗（quiz）。

---

## 先記住這兩張表

### 表一：Claude 模型家族——選型是所有決策的起點

| 模型 | 定位 | 特性 | 適用情境 |
|---|---|---|---|
| **Claude Fable 5** | 位於 Opus 之上的新層級（2026 年 6 月推出） | 能力最強，但成本明顯高於 Opus | 只保留給「Opus 也扛不住、且結果值得多花錢」的最難任務 |
| **Claude Opus** | 三大核心家族中最強 | 擅長長時間獨立處理複雜多步驟任務、支援 reasoning | 需要深度推理與規劃的複雜工作 |
| **Claude Sonnet** | 平衡點（sweet spot） | 智力、速度、成本三者均衡；寫程式能力強 | 大多數應用的主力與商業邏輯 |
| **Claude Haiku** | 最快、最便宜 | 速度優先；**不支援 reasoning** | 即時互動、面向使用者的高流量場景 |

在 Bedrock 上，Fable 5 的 model ID（模型識別碼）是 `anthropic.claude-fable-5`。實務上很多團隊**混用多個模型**：Haiku 顧使用者介面、Sonnet 跑主要邏輯、Opus 處理難題、Fable 5 只在最棘手的問題上偶爾出場。

### 表二：課程地圖——每個模組在解決什麼問題

| 模組 | 解決的問題 |
|---|---|
| Working with the API | 怎麼發 request、維持對話、控制輸出 |
| Prompt evaluations | 怎麼「客觀地」知道 prompt 好不好 |
| Prompt engineering | 怎麼有系統地改進 prompt |
| Tool use | 怎麼讓 Claude 取得外部資料、執行動作 |
| RAG | 文件太大放不進 prompt 怎麼辦 |
| Features of Claude | extended thinking、影像、PDF、citations、prompt caching |
| MCP | 不想自己寫一堆工具整合程式碼 |
| Agents | 從 Claude Code 與 Computer Use 學「什麼是好 agent」 |

---

## 各單元內容導讀

### 模組 1：課程介紹與 Claude 模型總覽

開場說明課程結構與適合對象，接著就是上面表一的模型家族介紹。所有 Claude 模型共享核心能力（文字生成、寫程式、影像分析），差別在**智力、速度、成本的權衡**。這個模組的重點只有一個：**依任務選型，而不是一律用最強的模型**。

### 模組 2：Working with the API——打好所有基礎

這是全課程最基礎也最重要的模組，之後所有東西都建立在這裡的 helper functions 之上。

**發出第一個 request。** 需要三個要素：Bedrock Runtime Client、model ID、user message。用 boto3 建立 client：

```python
import boto3
client = boto3.client("bedrock-runtime", region_name="us-west-2")
```

**region 陷阱與 inference profile。** 不是每個模型在每個 AWS region 都有部署——在 us-east-1 呼叫只部署在 us-west-2 的模型，會收到很難懂的「model doesn't exist」錯誤。解法是 **inference profile**（推論設定檔）：它知道模型部署在哪些 region，會自動把 request 路由過去。注意：inference profile ID 要去 Bedrock console 的「**Cross-region inference**」（跨區域推論）區找，**不是**模型目錄頁上的 model ID——課程特別點名的易錯處。

**訊息結構。** user message 的 `content` 是一個 list，因為一則訊息可以同時包含文字、圖片等多種內容（多模態）：

```python
user_message = {"role": "user", "content": [{"text": "What's 1+1?"}]}
response = client.converse(modelId=model_id, messages=[user_message])
response["output"]["message"]["content"][0]["text"]
```

課程主要使用 **Converse API**（`client.converse`，Bedrock 提供的統一對話介面）。另一個更底層的 **InvokeModel**（`client.invoke_model`，直接傳原始 JSON body 給模型）在課程後段呼叫 embedding 模型時才會用到。兩者的差異值得先分清楚：

| | Converse API | InvokeModel |
|---|---|---|
| 呼叫方式 | `client.converse(modelId=..., messages=[...])` | `client.invoke_model(modelId=..., body=json_string)` |
| 輸入格式 | 統一的 messages 結構，跨模型一致 | 各模型自訂的原始 JSON body |
| 課程中的用途 | 與 Claude 的所有對話、tool use | 呼叫 Titan embedding 模型產生向量 |

**多輪對話：API 不會幫你記任何東西。** 這是初學者最常誤解的一點——Bedrock 和 Claude **完全不儲存訊息**，每次 API 呼叫都是獨立的。要維持脈絡，必須自己維護完整的 messages list，每次 request 都把**整段歷史**傳回去。課程為此寫了三個貫穿全課的 helper：`add_user_message`、`add_assistant_message`、`chat`。另一個硬規則：訊息角色必須**嚴格交替**（user → assistant → user → assistant），不能連續兩則同角色。

**System prompts（系統提示）。** 與其在 user message 裡塞一長串「要提 AWS、不要提競品」的規則，不如給 Claude 一個**角色**，以獨立參數傳入：`system=[{"text": "You are an AWS cloud support specialist. ..."}]`。有了角色，Claude 會自然遵守該角色的行為框架——問它麵包食譜，它會禮貌婉拒並留在角色內。技術細節：system prompt 不能是空字串、在所有 user messages 之前被處理、可在對話之間更換但不能在中途換。

**Temperature（溫度）。** 一個 0 到 1 的參數，控制選字隨機性：接近 0 幾乎每次都選機率最高的 token（模型處理文字的最小單位），輸出穩定；接近 1 讓低機率的字也有機會出線，輸出更有變化。**預設值是 1.0**，寫法是放進 `inferenceConfig`：`{"inferenceConfig": {"temperature": temperature}}`。參考區間：

| 範圍 | 適用 |
|---|---|
| 0.0–0.3 | 事實回答、寫程式、資料抽取、內容審核 |
| 0.4–0.7 | 摘要、教學內容、問題解決 |
| 0.8–1.0 | 腦力激盪、創意寫作、行銷文案 |

**Streaming（串流）。** 用 `client.converse_stream(...)` 取代等待完整回覆（可能 3～30 秒），讓文字邊生成邊顯示。事件順序固定：`messageStart` →（`contentBlockStart`）→ 多個 `contentBlockDelta` → `contentBlockStop` → `messageStop` → `metadata`。**純文字生成時只需關心 `contentBlockDelta`**，從 `event["contentBlockDelta"]["delta"]["text"]` 取出片段、用 `print(chunk, end="")` 印出即可。

**控制輸出的兩把刀：prefill 與 stop sequences。**

- **Prefilled assistant message（預填助理訊息）**：在 messages 結尾放一則你寫好開頭的 assistant message，Claude 會認為「我已經開始回答了」，**從你寫的地方接著寫、不會重複你寫的內容**。例如預填 `"Coffee is better because"`，回覆就順著這個立場展開。
- **Stop sequences（停止序列）**：給一組字串，Claude 一生成到其中任何一個就立刻停止，且**停止序列本身不會出現在回覆裡**。例如 `stop_sequences=["5"]` 讓「數到 10」的回答停在 `1, 2, 3, 4,`。

**結構化資料：兩招合體。** Claude 預設喜歡在 JSON 外面包一層說明文字和 markdown 標頭，對程式化使用很礙事。解法是把上面兩招組合：

```python
add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])
```

預填的 ` ```json ` 讓 Claude 直接跳進 JSON 內容，stop sequence 在它要收尾時立刻截斷——拿到的就是乾淨、可直接 `json.loads()` 的內容。這招不限於 JSON，任何有明確定界符的格式（Python 程式碼、CSV、設定檔）都適用。練習裡還示範：prefill 不只能放定界符，也能放一整句引導語（如 `Here are all three commands in a single block without any comments:`）來穩定輸出。

### 模組 3：Prompt evaluations——先學會量測，再談改進

課程刻意把「評測」放在「prompt engineering」**之前**教，理由是：不能量測，就無法知道改進是否真的有效。

**寫完 prompt 之後的三條路：**測一次就上線（會在正式環境炸掉）；手動測幾次、修幾個 corner case（還是會被使用者的意外輸入打爆）；或**跑一套評測 pipeline 拿到客觀分數，據此迭代**。前兩條是所有工程師（包括講師本人）都掉過的陷阱。

**典型評測工作流（五步）：**草擬初版 prompt（先有 baseline）→ 建立 evaluation dataset（評測資料集；可手寫，也可用 Claude 產生——建議用快又便宜的 Haiku，配「prefill ` ```json ` ＋ stop sequence」拿乾淨 JSON）→ 逐筆餵給 Claude 收集輸出 → 交給 grader（評分器）打 1–10 分並取平均 → 改 prompt、重跑、比分數。程式結構是三個函式：`run_prompt`（併模板、呼叫模型）、`run_test_case`（跑單一案例並評分）、`run_eval`（跑完整個 dataset、算平均）。

**三種 grader：**

| 類型 | 做法 | 適合評估 |
|---|---|---|
| **Code grader** | 用程式邏輯檢查 | 輸出長度、關鍵字、**語法有效性**（`json.loads` 驗 JSON、`ast.parse` 驗 Python、`re.compile` 驗 regex：能解析給 10 分，失敗給 0 分） |
| **Model grader** | 再發一次 API 請另一個模型評分 | 回答品質、指令遵循度、完整性、有用性 |
| **Human grader** | 人工審閱 | 最靈活但最耗時 |

Model grader 有個重要技巧：**不要只要分數，要同時要求 strengths、weaknesses、reasoning**——沒有這些脈絡，模型評分會傾向給出千篇一律的 6 分左右。練習裡再加一層：產生 dataset 時順便要求每筆案例附上 `solution_criteria`（好答案的判準），插進 grader 的 prompt 讓評分更有依據。最後把 model 分數與 syntax 分數平均成綜合分：`score = (model_score + syntax_score) / 2`。記住課程的提醒：**單一分數本身意義不大，價值在於迭代之間的比較**。

### 模組 4：Prompt engineering——四個可量測的改進技巧

這個模組把評測 pipeline 包裝成 `PromptEvaluator` class（支援併發、輸出 `output.html` 報告），用一個實例貫穿：替運動員產生一日餐飲計畫。初版 prompt 只拿 **2.3/10**——課程強調這很正常，重點是有了 baseline。四個技巧依序上場：

1. **Being clear and direct（清楚直接）**：prompt 第一行最重要。用祈使句、以動詞開頭（Write / Create / Generate）。光是把「What should this person eat?」改成「Generate a one-day meal plan for an athlete that meets their dietary restrictions.」，分數就從 2.32 升到 3.92。
2. **Being specific（給明確規範）**：分兩種——**quality guidelines**（規定輸出長什麼樣：熱量、巨量營養素、用餐時間、份量用公克……）與 **process steps**（規定模型怎麼想：先算熱量、再算巨量營養素、再排時間……）。前者把分數推到 **7.86**，後者也有 7.3。process steps 特別適合疑難排解、決策、需要模型「看得更廣」的任務。
3. **XML tags（XML 標籤）**：prompt 裡插入大量資料時，用 `<athlete_information>...</athlete_information>` 這類自訂標籤把「指令」和「資料」清楚隔開。標籤名稱不必符合任何正式規範，**描述性越強越好**，且最好與指令用詞呼應（指令說 a passage of text，標籤就叫 `<text>`）。
4. **Providing examples（給範例，one-shot / multi-shot prompting）**：給一到多組「範例輸入＋理想輸出」，特別適合 corner case（如推文情緒分析中的**反諷**）與複雜輸出格式。實用技巧：從評測報告挑得分最高的輸出直接當範例，並補一句「為什麼這是好範例」。

模組結尾的練習（從文章段落抽取主題成 JSON 字串陣列）示範了威力：光第一招就把 2.8 分拉到 **9.5**。

### 模組 5：Tool use——讓 Claude 伸手進外部世界

Claude 預設只知道訓練資料裡的東西，不知道現在幾點、今天天氣。**Tools（工具）在 Claude 與外部資料/動作之間搭橋**：你在 request 裡附上工具說明 → Claude 判斷需要外部資料時回覆「請幫我跑這個工具」 → 你的伺服器執行、把結果傳回 → Claude 用結果組出最終回答。課程直言：tool use 一開始讓人混亂，是因為**程式碼的撰寫順序和邏輯流程的順序不一致**。

你要準備兩樣東西：

- **工具函式本身**：普通的 Python 函式。最佳實務：參數命名要有描述性、驗證輸入、**回傳有意義的錯誤**（Claude 收到錯誤會聰明地調整再試一次）。
- **JSON Schema（一種通用的資料格式描述規範）**：告訴 Claude 工具叫什麼、做什麼、參數長什麼樣。課程給了偷懶流程：寫一個帶範例值的 dict → 轉成 JSON → 丟給線上「JSON to JSON Schema」轉換器 → **補上詳細的 description**（工具描述建議 3–4 句：做什麼、何時用、回傳什麼）。卡住就把函式貼給 Claude 請它幫你寫。

**Claude 想用工具時的回覆長怎樣？** 一則 assistant message 裡有多個 content parts：一個 text part（人話說明）＋一或多個 **toolUse part**，後者含三個關鍵欄位：`toolUseId`（唯一識別碼，回傳結果時必須帶上）、`name`、`input`。判斷依據是回覆的 **`stopReason`**：

| stopReason | 意義 |
|---|---|
| `tool_use` | 模型想呼叫工具 |
| `end_turn` | 正常講完了 |
| `max_tokens` | 撞到輸出上限 |
| `stop_sequence` | 碰到你設的停止序列 |

執行工具後，把結果包成 **toolResult part**（含對應的 `toolUseId`、字串化的 `content`、`status` 為 `"success"` 或 `"error"`），以 user message 身分連同**完整對話歷史與原本的工具 schemas** 一起送回——漏掉 schemas，Claude 會看不懂歷史裡的工具引用。把這一切包成 `while` 迴圈（stop reason 不是 `tool_use` 就跳出），就得到能同時應付兩類問題的對話引擎；之後**加新工具只要兩步**：schema 放進 tools 陣列、`run_tool` 加一個分支。

這個模組還有幾個進階主題：

- **toolChoice 參數**：`{"auto": {}}`（模型自行決定）、`{"any": {}}`(必須用某個工具)、`{"tool": {"name": "..."}}`（強制用指定工具）。
- **Batch tool**：Claude 有時不會主動平行呼叫多個工具。自己定義一個 `batch_tool`（參數是一串 invocations，每個含工具名與 JSON 字串化的參數），就能「誘導」它把多個獨立操作合併成一次呼叫。
- **用 tools 拿結構化資料**：比 prefill＋stop sequence 更可靠的做法——定義一個 input schema 恰好等於你要的資料結構的工具，用 `toolChoice` 強制呼叫，然後**直接從工具呼叫的參數裡取出結構化資料，對話到此為止**。兩種做法的取捨：

| | Prefill ＋ stop sequence | Tool-based 抽取 |
|---|---|---|
| 設定成本 | 低，幾行就能動 | 高，要寫完整 schema |
| 可靠度 | 不錯 | 更高，結構有保證 |
| 適合 | 快速原型、簡單任務 | 正式環境的關鍵資料抽取 |

- **Flexible tool extraction**：折衷方案——定義一個萬用的 `to_json` 工具（schema 允許任意屬性），把想要的欄位結構直接寫在 prompt 裡（如 `"title": str # title of the article`）。改結構只要改 prompt，「九成的品質、一成的設定工作」。
- **Text editor tool**：Claude **內建 schema** 的官方工具，給它檔案系統存取能力（view、str_replace、create、insert、undo_edit）。特別之處：schema 內建，但**實作仍要你自己寫**。工具 ID 依模型版本不同（Claude 3.7 用 `text_editor_20250124`、3.5 用 `text_editor_20241022`），最新 ID 要查 AWS 文件。

### 模組 6：Retrieval Augmented Generation——大文件的正解

**問題**：800 頁的財報塞不進 prompt——有 token 上限、太長會讓 Claude 變鈍、又貴又慢。**RAG 的思路**：預先把文件切成小塊（chunks），使用者提問時只挑出最相關的幾塊放進 prompt。

**Chunking（切塊）策略**——切得爛，整個系統就答錯題（課程例子：醫學研究段落裡剛好有「bug」這個字，害工程部門的問題撈到醫學內容）：

| 策略 | 做法 | 適合 |
|---|---|---|
| Size-based（依大小） | 等長切割，可加 overlap（重疊）補脈絡 | 最保險的萬用款，面對格式無保證的使用者上傳文件 |
| Structure-based（依結構） | 依標題、段落、章節切（如 `re.split(r"\n## ", text)`） | 格式一致的文件，效果最好 |
| Semantic-based（依語意） | 用 NLP 技術把相關句子分成一組 | 需要更高品質時 |

**Text embeddings（文字向量嵌入）**：把文字餵進 embedding 模型，得到一長串數字（通常 1024 個、介於 -1 到 +1），代表這段文字的語意。課程用 Amazon 的 Titan 模型（`amazon.titan-embed-text-v2:0`），透過 `client.invoke_model` 呼叫。**語意相近的文字，embedding 也相近**——這就是 semantic search（語意搜尋）能超越關鍵字比對的原因。

**完整 RAG 流程（六步）**：切塊 → 每塊算 embedding → 存進 vector database（向量資料庫；**原文要一起存**，不然搜出來只有數字）→ 使用者提問時把問題也算成 embedding → 用 **cosine similarity（餘弦相似度）** 找最接近的塊 → 把相關塊和問題組成 prompt 給 Claude。cosine similarity 介於 -1 到 1，越接近 1 越相似；文件裡也常見 **cosine distance** ＝ 1 − cosine similarity，**越接近 0 越相似**——方向相反，讀結果時別搞混。

接著課程逐步補強這條 pipeline：

- **BM25 lexical search（詞彙搜尋）**：語意搜尋對「INC-2023-Q4-011」這種精確識別碼很不拿手。BM25 演算法把查詢斷詞、依「詞的稀有度」加權（罕見詞比 a、the 重要得多），做精確關鍵字比對。
- **Hybrid search ＋ RRF**：同時跑 vector 與 BM25 兩路搜尋，用 **Reciprocal Rank Fusion（RRF，倒數排名融合）** 合併：每份文件的分數是 `Σ 1/(k + rank)`（k 常取 60），只看名次不看原始分數，所以能公平合併兩套計分不同的系統。包成 `Retriever` class 後，加新搜尋法只要符合同樣的 `add_document` / `search` 介面。
- **Reranking（重排序）**：搜尋結果出來後，再請 Claude 依使用者的問題重排相關性。效率技巧：**事先給每個 chunk 一個短 ID，只要求 Claude 回傳 ID 列表**（如 `["1p5g", "51n3", "ab83"]`），別讓它重抄整段文字。代價是多一次 API 呼叫的延遲，換來更準的排序。
- **Contextual retrieval（情境化檢索）**：切塊會讓 chunk 失去「它在整份文件中的位置感」。做法：入庫前請 Claude 為每個 chunk 寫一小段定位說明，接在 chunk 前面再存進索引。文件太大放不進 prompt 時，改附「文件開頭幾塊＋目標 chunk 前面幾塊」當脈絡。交叉引用越複雜的文件，這招越有價值。

### 模組 7：Features of Claude——五個進階功能

**Extended thinking（延伸思考）**：讓 Claude 先「想」再答，回覆會多出一個 reasoning content part（思考過程）。開啟方式：

```python
additional_model_fields["thinking"] = {"type": "enabled", "budget_tokens": thinking_budget}
```

`budget_tokens` 最少 **1024**。代價是更貴（思考的 token 也要錢）、更慢。兩個特殊機制：思考內容附有**加密簽章（signature）** 防止竄改後回傳；被安全系統攔下的思考會變成 `redactedContent`（加密但仍可原樣傳回、不失脈絡）。決策準則很務實：**先跑評測、先優化 prompt，還是不夠準再考慮 extended thinking**。

**Image support（影像支援）**：限制——單一 request 最多 20 張圖、每張最大 3.75MB、長寬最大 8000px、token 消耗 ≈ 寬 × 高 ÷ 750。圖片作為 message 的一種 part 傳入（`{"image": {"format": "png", "source": {"bytes": image_bytes}}}`）。**最重要的觀念：所有 prompt engineering 技巧對影像同樣適用**——與其問「圖裡有幾顆彈珠」，不如給明確的計數方法與驗證步驟，也可以用 one-shot 範例圖。課程的實戰例子是保險業用衛星影像做火災風險評估。

**PDF support**：與影像類似但用 `"document"`：`{"document": {"format": "pdf", "name": "earth", "source": {"bytes": file_bytes}}}`，注意多了 `name` 欄位（檔名去掉副檔名）。

**Citations（引用）**：解決「使用者只能盲信 AI 讀對了文件」的信任問題。在 document 設定加一行 `"citations": {"enabled": True}`，回覆就會多出 citations content parts，標明每句話出自哪份文件、哪一頁、哪段原文。對學術、研究、專業場景特別重要。

**Prompt caching（提示詞快取）**：Claude 每次處理 request 都要對輸入做大量前置運算，做完即丟；下一輪又把同樣的歷史傳回來，等於重算一遍。快取把運算結果存起來重用，**更便宜也更快**。規則要記清楚：

- 不會自動開啟——要手動插入 **cache point**：`{"cachePoint": {"type": "default"}}`。cache point **之前**的內容全部被快取，之後的不會。
- 命中條件苛刻：cache point 之前的內容必須**一字不差**，開頭多加一個 "Please" 就 cache miss；反之，改 cache point **之後**的內容（例如 user message）不影響命中。
- 被快取的內容合計至少 **1024 tokens**；快取存活 **5 分鐘**（期間沒有 request 就清掉）。
- 最划算的快取對象：**system prompt 和工具 schemas**——通常夠長、又幾乎不變。寫法都是在列表最後附一個 cache point。
- 觀察是否命中：看回應的 `usage` 欄位——第一次出現 `cacheWriteInputTokens`（寫入），之後是 `cacheReadInputTokens`（讀取）。

### 模組 8：Model Context Protocol——別再自己寫整合程式碼

**MCP 解決什麼問題？** 想讓 Claude 操作 GitHub，你得為 repo、PR、issue……寫幾十個工具 schema 與函式，然後自己維護。MCP（Model Context Protocol，一個開放的通訊協定）把這個負擔轉移給 **MCP server**：由服務方（或任何人）事先把工具實作好，你的應用程式作為 **MCP client** 連上去直接用。課程特別澄清常見誤解：**MCP 不是取代 tool use，而是改變「工具由誰提供」**——執行流程完全一樣，差別是 schema 和實作不再由你撰寫；這也是它和「直接呼叫服務 API」的差異（直接呼叫時 schema 和函式還是得自己寫）。

**MCP client 與訊息類型**：client 是你的應用與 MCP server 之間的橋，transport agnostic（不挑通訊方式：同機用標準輸入輸出、跨網路用 HTTP、WebSockets 都行）。核心訊息兩對：`ListToolsRequest/Result`（問 server 有哪些工具）與 `CallToolRequest/Result`（請 server 執行某工具）。流程：使用者提問 → client 向 server 要工具清單 → 連同問題送給 Claude → Claude 回覆 toolUse → client 請 server 執行 → 結果回傳 Claude → 最終回答。

**動手做一個文件聊天 CLI**（課程同時實作 client 和 server 純為教學；實務上通常**只做其中一邊**）。用官方 Python SDK 的 **FastMCP**（`mcp = FastMCP("DocumentMCP", log_level="ERROR")`），定義工具只要裝飾器＋型別註記，SDK 自動生成 JSON schema：

```python
@mcp.tool(name="read_doc_contents", description="Read the contents of a document...")
def read_document(doc_id: str = Field(description="Id of the document to read")):
    ...
```

配套工具是 **MCP Inspector**：`mcp dev mcp_server.py` 啟動一個瀏覽器介面，不用接上完整應用就能單測工具、resources、prompts。client 端核心只有幾行（`session.list_tools()`、`session.call_tool(...)`）；一個小陷阱：**MCP 的工具 schema 格式和 Bedrock 要的略有不同**，專案裡有 `to_bedrock_tools` 函式負責轉換。

除了 tools，MCP server 還有兩個 primitives（基本元件）：

- **Resources**：唯讀資料端點，類似 HTTP GET。分 direct（固定 URI，如 `docs://documents`）與 templated（含參數，如 `docs://documents/{doc_id}`）。用 `@mcp.resource()` 定義、標 `mime_type`。用途：自動補全清單、把文件內容直接注入 prompt（CLI 的 `@文件名` mention 功能就靠它）。
- **Prompts**：server 作者預先寫好、測好的高品質 prompt 模板，用 `@mcp.prompt` 定義、回傳一組 messages，client 帶參數取用（CLI 的 `/指令` 就是它）。

模組收尾的心智模型是全課程最好記的一張表——**三個 primitives 各由誰控制**：

| Primitive | 控制者 | 使用時機 |
|---|---|---|
| **Tools** | 模型（Claude 自行決定何時呼叫） | 想擴充 Claude 的能力 |
| **Resources** | 應用程式（你的程式碼決定何時抓） | 想把資料放進 app 的 UI 或對話脈絡 |
| **Prompts** | 使用者（點按鈕、下 slash 指令觸發） | 想提供預先定義好的工作流程 |

### 模組 9：Agents——從 Claude Code 與 Computer Use 反推「什麼是好 agent」

Agent 領域連統一定義都還沒有，所以課程的策略是**倒著學**：拆解 Anthropic 實際做出來的兩個 agent——Claude Code 和 Computer Use——從中萃取原則。

**Claude Code** 是跑在終端機裡的 coding assistant，有搜尋/讀取/編輯檔案等基本工具，也有抓網頁、操作終端機等進階工具，而且**本身就是一個 MCP client**。在 Bedrock 上使用需要：裝 Node.js → `npm install` 裝 Claude Code → 設三個環境變數把它從 Anthropic API 導向 Bedrock（外加 AWS credentials）。

使用上的重點：

- **`/init` 指令**掃描專案，把結構、相依、慣例寫進 `CLAUDE.md`，之後每次對話自動讀取。CLAUDE.md 有三種範圍：project（進 git、團隊共用）、local（不進 git、個人筆記）、user（跨專案）。`#` 快捷鍵可隨手補筆記。
- **兩種高效工作流**：*Planning-first*（先餵相關檔案 → 要求先規劃**不要寫程式** → 確認計畫後才實作）與 *Test-driven*（餵脈絡 → 先想測試案例 → 實作測試 → 再寫通過測試的程式碼）。共同精神：**Claude 是效率放大器，給的脈絡與結構越多，結果越好**。
- **接 MCP servers**：`claude mcp add documents uv run main.py` 一行接上自訂 server。生態系裡現成的有 sentry-mcp、playwright-mcp、figma-context-mcp、mcp-atlassian、slack-mcp 等，可組合成貼合團隊的工作流。
- **平行化**：多個實例最怕改到同一份檔案。解法是 **git worktrees**（git 的功能，為不同分支各建一份完整的專案目錄），每個實例在自己的 worktree 裡隔離作業，完成後合併回主幹——建 worktree、開 VS Code、合併、解衝突都可寫成 custom slash commands（在 `.claude/commands` 放 `.md` 檔，用 `$ARGUMENTS` 接參數）交給 Claude 自動化。效果等於「一個人指揮一隊虛擬工程師」。
- **自動化除錯**：用 GitHub Action 每天定時執行——AWS CLI 撈過去 24 小時的 CloudWatch logs → Claude 分析、去重、找出錯誤 → 嘗試修復 → 自動開 pull request 供人審核。課程實例：production 用了打錯字的 model ID，Claude 自己找到並修好。

**Computer Use** 讓 Claude 像人一樣操作桌面環境：截圖「看」畫面、點擊、打字、切換應用程式。課程的殺手級範例是**自動化 QA 測試**：給 Claude 一組測試案例（輸入 `@` 要出現自動補全、按 Enter 要正確插入 mention……），它逐項執行、截圖驗證、寫成報告——還真的抓到一個下拉選單位置錯誤的 bug。技術上，**Computer Use 就是 tool use**：你送出一個極簡的特殊 schema，背後自動展開成滑鼠、鍵盤、截圖等完整介面；Claude 只是發出工具請求，由你的基礎設施（官方 Docker 參考實作，內含 Firefox 與隔離桌面）轉譯成實際操作。**務必在隔離環境中執行**。

**好 agent 的四個特質**（兩個案例的共同點）：

1. **精簡的工具組＋迴圈執行**：少量、定義清楚的工具，反覆執行直到達成目標、出錯或到達迭代上限。
2. **脈絡就是一切**：Claude 對你的環境一無所知，靠工具「先觀察、再動手」——課程分析過一次任務的四個工具呼叫，有三個在讀環境、只有一個在改東西。
3. **高價值、低錯誤成本的任務**：寫程式是完美例子（需要專業、但錯了可以修）；錯誤代價高昂的決策不要交給 agent。
4. **持續評測**：又回到全課程的主旋律。

### 模組 10：課程總結

回顧之外給了幾個延伸方向：追蹤 Anthropic 的研究、**LLM orchestration**（多模型協作，例如讓較慢但較聰明的 Sonnet 指揮一群便宜的 Haiku）、RAG 的替代方案、持續演進中的 agentic workflows。以及最後一次耳提面命：**evaluations 不能省**。

---

## 讀完這門課你會得到什麼

一句話總結：**從「會呼叫 Claude」到「能在 AWS 上打造一套可量測、可維運的 Claude 應用」的完整路徑。**

- 一組可重用的基礎程式模式：boto3 ＋ Converse API 的對話管理、system prompt、temperature、streaming、prefill ＋ stop sequences。
- 一套評測方法論（dataset → grader → 平均分 → 迭代），以及四個被數據驗證過的 prompt engineering 技巧。
- 完整的 tool use 實作能力：從 JSON Schema、對話迴圈到 batch tool 與結構化資料抽取的多種手段。
- 一條從陽春到進階的 RAG 演進路線：chunking → embeddings → hybrid search（BM25 ＋ RRF）→ reranking → contextual retrieval。
- Claude 進階功能的正確用法與省錢之道（尤其是 prompt caching 的 cache point 規則）。
- MCP 的雙邊視角（client 與 server）與「tools／resources／prompts 各由誰控制」的心智模型。
- 對 agent 的務實理解：不追框架名詞，而是從 Claude Code 與 Computer Use 反推出的四個設計原則。

如果你的目標是在 AWS 環境導入 Claude，或準備 Anthropic 相關認證，這門課大概是目前最完整的一條龍教材；但也因為內容量大，建議搭配原始筆記裡的程式碼實際跑過每個模組的練習，再回頭看各模組的 quiz。
