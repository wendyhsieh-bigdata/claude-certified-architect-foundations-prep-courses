# Introduction to Model Context Protocol — 課程導讀

> 原始筆記：`../Introduction_to_Model_Context_Protocol.md`
> 對象：**還沒看過這門課的人**。讀完這份導讀，你就能掌握課程在教什麼、核心觀念是什麼、以及可以馬上套用的做法。專有名詞保留英文，第一次出現時附中文解釋。

---

## 這門課在講什麼

這是 Anthropic 的入門實作課，主題是 **MCP**（Model Context Protocol，模型上下文協定）——讓 Claude 取得外部工具與資料的**標準化通訊層**。

課程要解決的痛點很具體：假設你在做一個聊天應用，使用者問 Claude「我所有 repo 裡有哪些 open 的 pull request？」，Claude 就需要能存取 GitHub API 的工具。但 GitHub 功能極多，如果每個功能都要你自己寫 tool schema（工具規格定義）和對應函式，再自己測試、維護，工作量非常可觀。

MCP 的做法是**把「定義工具」和「執行工具」的負擔，從你的應用程式移到專門的 MCP server**（提供工具與資料的伺服端程式）上：由一個 GitHub 的 MCP server 把大量 GitHub 功能包裝成一組標準化的 tools（工具），你的應用程式透過 MCP client（負責與 MCP server 溝通的客戶端元件）連上它，就能直接使用現成工具，不必從零實作。

兩個常見誤解先釐清：

- **和自己直接呼叫 API 的差別**：tool schema 和函式已有人幫你定義好，省下實作與維護的工。
- **MCP 不等於 tool use**（Claude 的工具呼叫機制）——兩者互補但不同：MCP server 負責「提供」已定義好的工具，tool use 是 Claude「實際呼叫」工具的方式。關鍵差異在**由誰做工**。

課程主體是動手做：用 Python 打造一個 **CLI 聊天機器人**，同時包含自製的 MCP server 和小型 MCP client，讓你完整看到兩邊如何協作。需要基本 Python 能力，並會用到 `uv`（Python 的套件與環境管理工具）。

---

## 先記住這張表：三個 server primitives 由誰控制

MCP server 對外提供三種東西，稱為 **server primitives**（伺服端基本元件）。整門課最核心的觀念：**三者分別由應用程式堆疊中不同的角色控制**。

| Primitive | 由誰控制 | 一句話說明 | 典型用途 |
|---|---|---|---|
| **Tools**（工具） | **Model-controlled**（模型控制） | Claude 自己決定何時呼叫 | 給 Claude 新能力，讓它自主完成任務 |
| **Resources**（資源） | **App-controlled**（應用程式控制） | 你的程式碼決定何時抓資料、怎麼用 | 填 UI（如自動完成選單）、把資料塞進 prompt 當上下文 |
| **Prompts**（提示範本） | **User-controlled**（使用者控制） | 使用者透過 UI 動作主動觸發 | 預先寫好、測試過的工作流程（如斜線指令、按鈕） |

快速判斷：**想給 Claude 新能力？** 用 tools。**想把資料抓進你的 app 做 UI 或補充上下文？** 用 resources。**想給使用者一鍵觸發的預定義流程？** 用 prompts。

Claude 官方介面就同時示範了三者：輸入框下方的工作流程按鈕是 prompts、「Add from Google Drive」整合是 resources、Claude 執行程式碼時背後用的是 tools。後面每個單元其實都在具體實作其中一種 primitive。

---

## 各單元內容導讀

### Introducing MCP：MCP 解決什麼問題

開場講基本架構：一個 MCP client（在你的應用程式這邊）連向一個或多個 MCP server，每個 server 是通往某個外部服務的介面，裝著 tools、resources、prompts。MCP server **任何人都可以寫**，服務提供者也常自己出官方版（例如 AWS 可能釋出涵蓋自家服務的官方 MCP server）。

### MCP clients：訊息怎麼流動

MCP client 是你的應用程式與 MCP server 之間的**溝通橋樑**，處理訊息交換與協定細節。兩個重點：

1. **Transport agnostic**（不綁定傳輸方式）：最常見的配置是 client 和 server 在同一台機器上透過標準輸入輸出溝通，但也可以走 HTTP、WebSockets 或其他網路協定。
2. **主要訊息類型**只有兩對：
   - `ListToolsRequest` / `ListToolsResult`——client 問 server「你提供哪些工具？」
   - `CallToolRequest` / `CallToolResult`——client 請 server 用指定參數執行某個工具，拿回結果。

這個單元用「使用者問：我有哪些 repo？」走完一次完整流程：**使用者提問 → 透過 MCP client 向 MCP server 要工具清單 → 問題＋工具清單送給 Claude → Claude 決定呼叫某個工具 → 再透過 MCP client 請 MCP server 執行（由它去打真正的 GitHub API）→ 結果送回 Claude → Claude 整合出最終回答**。步驟多但每個元件職責清楚，之後動手寫時會一直看到這些角色。

### Project setup：動手做的專案長什麼樣

實作專案是一個 CLI 聊天機器人，操作一批**只存在記憶體裡的假文件**；server 一開始有兩個工具：讀文件內容、更新文件內容。

一個重要提醒：**真實專案通常只做其中一邊**——要嘛做 MCP server 發布出去讓別的開發者接你的服務，要嘛做 client 去接別人已發布的 server。這門課兩邊都做，純粹是為了讓你看清楚兩邊怎麼搭在一起。

設定流程：下載影片附件 `CLIproject.zip`、解壓縮、照 `README.md` 把 API key 放進 `.env`、安裝依賴，然後執行：

```
uv run main.py
```

（沒用 uv 就 `python main.py`。）出現聊天提示、問「what's one plus one」能快速得到回答，環境就沒問題。

### Defining tools with MCP：用 decorator 定義工具

用官方 Python SDK 建 server 非常精簡，一行初始化：

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")
```

文件存在普通的 dict 裡（key 是文件 ID、value 是內容）。定義工具**不必手寫 JSON schema**：用 decorator（裝飾器，Python 中包裝函式、附加行為的語法）搭配型別提示，SDK 自動生成 Claude 看得懂的 schema。例如讀文件的工具：

```python
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

分工：decorator 給工具命名與描述，函式參數定義引數，Pydantic 的 `Field` 提供參數描述幫 Claude 理解用途。第二個工具 `edit_document` 依同樣模式做字串取代（參數 `doc_id`、`old_str`、`new_str`）。錯誤處理直接用 Python 例外，工具註冊由 decorator 自動完成。

### The server inspector：不用寫測試腳本的除錯工具

SDK 內建**瀏覽器介面的 Inspector**（檢查器），不必接上完整應用就能即時測試 server。啟動指令：

```
mcp dev mcp_server.py
```

它會給你一個本機網址（通常像 `http://127.0.0.1:6274`），在瀏覽器打開後：先按 **Connect** 啟動 server，再到 **Tools** 分頁按「List Tools」，選一個工具、填入參數（例如 `read_doc_contents` 填 `deposition.md`）、按「Run Tool」看結果。

Inspector 會**在多次工具呼叫之間保留 server 狀態**，所以可以先用編輯工具改文件、馬上再用讀取工具驗證改動生效。這個即時回饋迴圈是 MCP server 開發的日常：快速迭代、測邊界情況、即時除錯。

### Implementing a client：實作 MCP client

換到 client 這邊。client 由兩層組成：**Client Session**（SDK 提供、真正連到 server 的連線物件）和自己包的 **MCP Client** 類別——因為 session 的連線用完要正確清理，所以包一層類別自動處理資源管理。

核心只有兩個函式，都很短：

```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

```python
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

client 檔案底部附有測試程式，直接 `uv run mcp_client.py` 就能連上 server 並印出可用工具。之後跑 `uv run main.py`，問「What is the contents of the report.pdf document?」，就能看到完整流程：app 拿工具清單 → 連同問題送給 Claude → Claude 決定用 `read_doc_contents` → app 透過 client 執行 → 結果回給 Claude → Claude 回答你。

### Defining resources：像 GET endpoint 一樣暴露資料

Resources 讓 server **對外暴露資料**，角色類似 HTTP server 的 GET handler——適合「取資料」而非「做動作」的場景。課程範例是 `@文件名` 的 mention 功能：打 `@` 跳出文件清單（自動完成），選定後把文件內容**直接注入 prompt**，Claude 不需要再呼叫工具去撈。

每個 resource 用 **URI**（Uniform Resource Identifier，統一資源識別碼）識別，分兩種：

**Direct resources**（固定 URI，不帶參數）：

```python
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())
```

**Templated resources**（URI 裡帶參數，SDK 自動解析並當作關鍵字引數傳給函式）：

```python
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    ...
```

`mime_type`（MIME type，標示資料格式的標準字串，如 `application/json`、`text/plain`、`application/pdf`）是給 client 的格式提示。回傳值的序列化由 SDK 自動處理，不用自己轉 JSON 字串。測試一樣用 Inspector（`uv run mcp dev mcp_server.py`），**Resources** 列固定資源、**Resource Templates** 列帶參數的資源。

### Accessing resources：client 端讀取資源

client 端實作 `read_resource`：發出 `ReadResourceRequest`，拿回 `ReadResourceResult` 後**依 MIME type 決定怎麼解析**：

```python
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]

    if isinstance(resource, types.TextResourceContents):
        if resource.mimeType == "application/json":
            return json.loads(resource.text)

    return resource.text
```

回傳結果裡有個 `contents` 清單，通常取第一個元素；是 `application/json` 就 parse 成物件，否則回傳原始文字。完成後在 CLI 打 `@` 會出現資源自動完成清單，選定內容直接併入 prompt 送出——比讓 Claude 另外呼叫工具去撈更順、更即時。

### Defining prompts：把 prompt 工程封裝給使用者

Prompts 是 server 作者預先寫好、**測試打磨過**的指令範本。核心洞察：使用者自己打「reformat the report.pdf in markdown」也能得到還可以的結果，但由 server 作者精心設計、處理過邊界情況的 prompt，能讓使用者不必變成 prompt 工程專家就得到穩定的高品質結果。

課程範例是 `/format doc_id` 指令，把文件重排成 markdown。定義方式同一套 decorator 模式，差別是**回傳一串要送給 Claude 的訊息**：

```python
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""Your goal is to reformat a document ..."""
    return [base.UserMessage(prompt)]
```

可以回傳多則 user／assistant 訊息組成更複雜的對話流。好處：**一致性**、**專業封裝**（領域知識寫進 prompt）、**可重用**（多個 client 共用）、**好維護**（改一處，所有 client 受益）。一樣可用 Inspector 驗證變數插入後實際送給 Claude 的訊息長什麼樣。

### Prompts in the client：client 端使用 prompts

client 端補上最後兩個方法：`list_prompts()`（列出所有 prompts）和 `get_prompt(prompt_name, args)`（取回指定 prompt 並把引數插進範本）：

```python
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

例如 format prompt 需要 `doc_id`，client 傳 `{"doc_id": "plan.md"}`，這個值就會插入範本。完成後在 CLI 打斜線 `/` 會列出可用的 prompts 當指令，選了 `format` 再選文件，完整 prompt 就送給 Claude，由它用現有工具讀取並重排文件。

### MCP review：收尾複習

最後回到「三個 primitives 由誰控制」那張表，把整個專案串起來：**tools 服務模型、resources 服務你的 app、prompts 服務使用者**——這是這門課最值得帶走的一句話。

---

## 讀完這門課你會得到什麼

一句話總結：**看懂 MCP 生態的分工，並且親手把 server 和 client 兩邊都做過一遍。**

- 一個清楚的心智模型：MCP 是把工具整合的負擔外移到 MCP server 的標準化通訊層；MCP 與 tool use 互補而非重疊。
- 一張決策表：tools = model-controlled、resources = app-controlled、prompts = user-controlled，遇到「該用哪個 primitive」時直接套。
- 一套可複製的實作模式：`FastMCP` ＋ decorator 定義三種 primitives，不必手寫 JSON schema；client 端的 `list_tools` / `call_tool` / `read_resource` / `get_prompt` 四個方法。
- 一個實用的開發流程：用 `mcp dev mcp_server.py` 開 Inspector 即時測試，不必先接上完整應用。

之後不論是替自家服務出官方 MCP server，還是在自己的 AI 應用裡接入現成的 MCP servers，這門課都是「兩邊都摸過一次」的最短路徑。延伸閱讀：https://modelcontextprotocol.io/introduction 。
