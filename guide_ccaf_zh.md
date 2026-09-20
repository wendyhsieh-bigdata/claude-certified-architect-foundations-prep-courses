# Claude Certified Architect — Foundations 認證讀書指南

> 出處：本頁內容翻譯整理自 Paul Larionov 的開源讀書指南 [claude-certified-architect / guide_en.md](https://github.com/paullarionov/claude-certified-architect/blob/main/guide_en.md)（依官方 Exam Guide 撰寫）。中文翻譯僅供學習參考，專有名詞一律保留英文；若與原文有出入，以原文為準。

# 考試總覽

## 考試簡介與應試者輪廓

### 這張證照在驗證什麼

**Claude Certified Architect — Foundations** 認證確認一位專業人士在實作真實世界的 Claude 解決方案時，能做出合理的取捨（trade-off）決策。考試評量的是四項核心技術的基礎知識：**Claude Code**、**Claude Agent SDK**、**Claude API**，以及 **Model Context Protocol（MCP）**——這些是用 Claude 打造 production 應用的核心技術。

考題都建立在真實的產業情境上：為客服建立 agentic 系統、設計多 agent 的研究 pipeline、把 Claude Code 整合進 CI/CD、打造開發者生產力工具，以及從非結構化文件中抽取結構化資料。

### 目標應試者

理想的應試者是一位 **solution architect**，負責設計並交付以 Claude 為基礎的 production 應用。你應該有至少 6 個月以下項目的實作經驗：

- **Claude Agent SDK**：多 agent 編排（orchestration）、委派給 subagent、tool 整合、lifecycle hooks
- **Claude Code**：CLAUDE.md、MCP servers、Agent Skills、planning mode
- **Model Context Protocol（MCP）**：用 tools 與 resources 整合後端系統
- **Prompt engineering**：JSON schema、few-shot 範例、資料抽取模板
- **Context window**：處理長文件、多 agent 之間傳遞 context
- **CI/CD pipeline**：自動化 code review、測試產生
- **Escalation 與可靠性**：錯誤處理、human-in-the-loop

### 考試形式

| 項目 | 內容 |
|---|---|
| 題型 | 單選題（4 選 1） |
| 計分 | 100–1000 分制，及格分數 **720** |
| 猜錯扣分 | 沒有（每一題都要作答！） |
| 情境 | 8 個可能情境中隨機抽 4 個 |

## 五大考試領域（Domains）

| Domain | 權重 |
|---|---|
| 1. Agent 架構與編排（Agent architecture and orchestration） | **27%** |
| 2. Tool 設計與 MCP 整合（Tool design and MCP integration） | **18%** |
| 3. Claude Code 設定與工作流程（Claude Code configuration and workflows） | **20%** |
| 4. Prompt engineering 與結構化輸出（Prompt engineering and structured output） | **20%** |
| 5. Context 管理與可靠性（Context management and reliability） | **15%** |

## 八個考試情境（Scenarios）

### 情境 1：Customer Support Agent（客服 agent）

你用 Claude Agent SDK 建立一個處理退貨、帳單爭議與帳號問題的 agent。Agent 使用 MCP tools（`get_customer`、`lookup_order`、`process_refund`、`escalate_to_human`）。目標是 80% 以上的首次接觸解決率（first-contact resolution），並在適當時機 escalate 給人類。

### 情境 2：Code Generation with Claude Code（用 Claude Code 產生程式碼）

你用 Claude Code 加速開發：產生程式碼、重構、除錯、撰寫文件。你需要整合自訂 slash commands 與 CLAUDE.md 設定，並知道何時該用 planning mode。

### 情境 3：Multi-Agent Research System（多 agent 研究系統）

一個 coordinator agent 把任務委派給專門的 subagents：web research、document analysis、synthesis、report generation。系統必須產出附帶引用來源（citations）的完整報告。

### 情境 4：Developer Productivity Tools（開發者生產力工具）

Agent 協助工程師探索不熟悉的 codebase、產生 boilerplate 程式碼、自動化例行工作。會用到內建 tools（Read、Write、Bash、Grep、Glob）與 MCP servers。

### 情境 5：Claude Code for Continuous Integration（CI 中的 Claude Code）

把 Claude Code 整合進 CI/CD pipeline，做自動化 code review、測試產生與 pull request 回饋。Prompt 設計必須盡量減少 false positive（誤報）。

### 情境 6：Structured Data Extraction（結構化資料抽取）

系統從非結構化文件中抽取資訊、用 JSON schema 驗證輸出，並維持高準確率。必須正確處理邊界案例（edge cases）。

### 情境 7：Conversational AI Architecture Patterns（對話式 AI 架構模式）

你設計多輪對話系統，涵蓋 context window 管理、跨回合的指令持續性（instruction persistence）、記憶策略、安全執行的 tool 設計，以及處理模糊或彼此矛盾的使用者輸入。

### 情境 8：Agentic AI Tools（內容待補）

原作者註：這個情境有考生回報在正式考試中出現，但本指南尚未涵蓋。若你在考試中遇到此情境的題目，原作者邀請你到 [GitHub Issues](https://github.com/paullarionov/claude-certified-architect/issues) 分享，讓指南更完整。

## 官方文件索引

| 資源 | URL |
|---|---|
| **Claude API — Messages** | https://platform.claude.com/docs/en/api/messages |
| **Claude API — Tool Use** | https://platform.claude.com/docs/en/build-with-claude/tool-use |
| **Claude API — Message Batches** | https://platform.claude.com/docs/en/build-with-claude/message-batches |
| **Claude Agent SDK — Overview** | https://platform.claude.com/docs/en/agent-sdk/overview |
| **Claude Agent SDK — Hooks** | https://platform.claude.com/docs/en/agent-sdk/hooks |
| **Claude Agent SDK — Subagents** | https://platform.claude.com/docs/en/agent-sdk/subagents |
| **Claude Agent SDK — Sessions** | https://platform.claude.com/docs/en/agent-sdk/sessions |
| **Model Context Protocol（MCP）** | https://modelcontextprotocol.io/ |
| **MCP — Tools** | https://modelcontextprotocol.io/docs/concepts/tools |
| **MCP — Resources** | https://modelcontextprotocol.io/docs/concepts/resources |
| **MCP — Servers** | https://modelcontextprotocol.io/docs/concepts/servers |
| **Claude Code — Documentation** | https://code.claude.com/docs/en/overview |
| **Claude Code — CLAUDE.md 與 Memory** | https://code.claude.com/docs/en/memory |
| **Claude Code — Skills（含 slash commands）** | https://code.claude.com/docs/en/skills |
| **Claude Code — Hooks** | https://code.claude.com/docs/en/hooks |
| **Claude Code — Sub-agents** | https://code.claude.com/docs/en/sub-agents |
| **Claude Code — MCP 整合** | https://code.claude.com/docs/en/mcp |
| **Claude Code — GitHub Actions CI/CD** | https://code.claude.com/docs/en/github-actions |
| **Claude Code — GitLab CI/CD** | https://code.claude.com/docs/en/gitlab-ci-cd |
| **Claude Code — Headless（非互動模式）** | https://code.claude.com/docs/en/headless |
| **Prompt Engineering Guide** | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview |
| **Extended Thinking** | https://platform.claude.com/docs/en/build-with-claude/extended-thinking |
| **Anthropic Cookbook（程式範例）** | https://github.com/anthropics/anthropic-cookbook |

# 第一部：理論基礎

## 第 1 章：Claude API — 與模型互動的基礎

> 文件：[Messages API](https://platform.claude.com/docs/en/api/messages) | [Prompt Engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

這一部涵蓋通過考試所需的全部理論。內容依技術與概念組織，而不是依考試 domain，這樣比較容易對每個主題建立深入理解。

### 1.1 API 請求結構

Claude API 採 request–response 模型。每一次對 Claude Messages API 的請求包含：

```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 1024,
  "system": "You are a helpful assistant.",
  "messages": [
    {"role": "user", "content": "Hi!"},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "How are you?"}
  ],
  "tools": [...],
  "tool_choice": {"type": "auto"}
}
```

**重要欄位：**

- `model`：模型選擇（`claude-opus-4-6`、`claude-sonnet-4-6`、`claude-haiku-4-5`）
- `max_tokens`：回應的最大 token 數
- `system`：system prompt（定義模型行為）
- `messages`：對話歷史（**必須送出完整歷史**才能維持連貫）
- `tools`：可用 tool 的定義
- `tool_choice`：tool 選擇策略

### 1.2 訊息角色（Message Roles）

`messages` 陣列使用兩個對話角色，加上一個指令角色：

- `user`：使用者訊息，**包含 tool 結果**（tool 結果是以 `user` 角色訊息中的 `tool_result` content block 送出，不是獨立的 `tool` 角色）
- `assistant`：模型回應（送歷史時要包含），包含 tool 呼叫請求（`tool_use` content block）
- `system`：可透過頂層的 `system` 欄位設定（從第一回合就生效），也可以在 `messages` 中以 `{"role": "system", ...}` 內嵌（從該位置起生效，需遵守放置規則，見下方）

Tool 結果**不是**用 `role: "tool"` 的訊息送出。它是放在 `user` 角色訊息裡、內容包含 `tool_result` content block：

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01...",
      "content": "..."
    }
  ]
}
```

`system` 也可以直接作為 `messages` 陣列裡的 role 出現，不只限於頂層的 `system` 參數。這是為了在對話中途加入指令，又不讓頂層 `system` 欄位的 cached prefix 失效。它有特定的放置規則：

- 必須緊接在 `user` 回合（包含含有 `tool_result` block 的回合）之後，或在以 server tool use 結尾的 `assistant` 回合之後。
- 必須在某個 `assistant` 回合之前，或位於陣列結尾。
- 不能夾在 `tool_use` block 與它對應的 `tool_result` 之間，否則回傳 400 錯誤。
- 較後面的 `system` 訊息（包含對話中途的）對其後的回合具有優先權，會覆蓋較早的訊息與頂層 `system` 欄位。

**極為重要：** 每次 API 請求都必須送出**完整的對話歷史**。模型不會在請求之間保存狀態，每次呼叫都是獨立的。

### 1.3 回應中的 `stop_reason` 欄位

Claude API 的回應包含 `stop_reason`，說明模型為什麼停止生成：

| 值 | 說明 | 你該做的事 |
|---|---|---|
| `"end_turn"` | 模型完成回應 | 把結果呈現給使用者 |
| `"tool_use"` | 模型想呼叫 tool | 執行 tool 並回傳結果 |
| `"max_tokens"` | 達到 token 上限 | 回應被截斷，可能需要提高上限 |
| `"stop_sequence"` | 遇到 stop sequence | 依你的應用邏輯處理 |

對 agentic 系統而言，`"tool_use"` 與 `"end_turn"` 最重要，它們控制整個 agent loop。

### 1.4 System Prompt

System prompt 是一段特殊指令，定義 context 與行為規則。它：

- 不屬於 `messages` 陣列，而是另外放在 `system` 欄位
- 優先權高於使用者訊息
- 載入一次，整段對話都適用
- 用來定義角色、限制與輸出格式

**考試重點：** system prompt 的措辭可能造成非預期的 tool 關聯。例如「always verify the customer（一律先驗證客戶）」這類指令，會讓模型過度使用 `get_customer`，即使根本不需要。

### 1.5 Context Window

Context window 是模型一次能處理的文字總量（以 token 計）。它包含：

- System prompt
- 完整的訊息歷史
- Tool 定義
- Tool 結果

**Context window 的關鍵問題：**

1. **Lost-in-the-middle 效應：** 模型能可靠處理長輸入的開頭與結尾，但可能漏掉中間的細節。緩解方式：把關鍵資訊放在開頭或結尾附近。
2. **Tool 結果的累積：** 每一次 tool 呼叫都會把輸出加進 context。若一個 tool 回傳 40 多個欄位、但只有 5 個有用，大部分 context 就被浪費了。
3. **漸進式摘要（progressive summarization）：** 壓縮歷史時，數值、百分比與日期常會遺失，變成模糊的說法（「大約」、「差不多」、「幾個」）。

## 第 2 章：Tools 與 `tool_use`

> 文件：[Tool Use](https://platform.claude.com/docs/en/build-with-claude/tool-use)

### 2.1 什麼是 `tool_use`

`tool_use` 是讓 Claude 呼叫外部函式的機制。模型並不直接執行程式碼，而是產生一個結構化的 tool 呼叫請求；由你的程式執行並回傳結果。

### 2.2 Tool 定義

每個 tool 都用 JSON schema 定義：

```json
{
  "name": "get_customer",
  "description": "Finds a customer by email or ID. Returns the customer profile, including name, email, order history, and account status. Use this tool BEFORE lookup_order to verify the customer's identity. Accepts an email (format: user@domain.com) or a numeric customer_id.",
  "input_schema": {
    "type": "object",
    "properties": {
      "email": {"type": "string", "description": "Customer email"},
      "customer_id": {"type": "integer", "description": "Numeric customer ID"}
    },
    "required": []
  }
}
```

**Tool description 的關鍵要點：**

1. **Description 是 tool 選擇的主要機制。** LLM 依據 description 選擇 tool。過於精簡的描述（例如「Retrieves customer information」）在多個 tool 功能重疊時會導致選錯。
2. **Description 應包含：**
  - Tool 做什麼、回傳什麼
  - 輸入格式與範例值
  - 邊界案例與限制
  - 何時該用這個 tool、何時該用相似的替代 tool
3. **避免**多個 tool 的描述相同或重疊。如果 `analyze_content` 與 `analyze_document` 的描述幾乎一樣，模型會搞混。
4. **內建 tools 與 MCP tools：** agent 可能偏好內建 tools（Read、Grep）而非功能相似的 MCP tools。要避免這點，就強化 MCP tool 的 description：突顯具體優勢、獨有資料，或內建 tool 提供不了的 context。

### 2.3 `tool_choice` 參數

`tool_choice` 控制模型如何選擇 tool：

| 值 | 行為 | 使用時機 |
|---|---|---|
| `{"type": "auto"}` | 模型自行決定要呼叫 tool 還是以文字回答 | 大多數情況的預設 |
| `{"type": "any"}` | 模型**必須**呼叫某個 tool | 需要保證結構化輸出時 |
| `{"type": "tool", "name": "extract_metadata"}` | 模型**必須**呼叫指定的 tool | 需要強制第一步 / 執行順序時 |

**重要情境：**

- `tool_choice: "any"` + 多個抽取用 tool → 模型挑最合適的一個，但你仍然一定會拿到結構化輸出
- 強制指定 → 必須保證特定的第一個動作時（例如先 `extract_metadata` 再做 enrichment）

### 2.4 用 JSON Schema 做結構化輸出

搭配 JSON schema 使用 `tool_use`，是從 Claude 取得結構化輸出**最可靠**的方式。它：

- 保證語法正確的 JSON（不會少括號、不會有多餘逗號）
- 強制要求的結構（required 欄位一定存在）
- **不**保證語意正確（值仍然可能是錯的）

**Schema 設計的關鍵原則：**

```json
{
  "type": "object",
  "properties": {
    "category": {
      "type": "string",
      "enum": ["bug", "feature", "docs", "unclear", "other"]
    },
    "category_detail": {
      "type": ["string", "null"],
      "description": "Details if category = 'other' or 'unclear'"
    },
    "severity": {
      "type": "string",
      "enum": ["critical", "high", "medium", "low"]
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "optional_field": {
      "type": ["string", "null"],
      "description": "Null if the information was not found in the source"
    }
  },
  "required": ["category", "severity"]
}
```

**Schema 設計規則：**

1. **Required 與 optional：** 只有資訊一定存在時才標為 required。Required 欄位會逼模型在資料缺失時捏造（fabricate）值。
2. **Nullable 欄位：** 對可能不存在的資訊使用 `"type": ["string", "null"]`，模型可以回傳 `null` 而不是幻覺（hallucinate）。
3. **Enum 加上 `"other"`：** 加入 `"other"` 與一個 detail 字串，避免預設分類之外的資料流失。
4. **Enum 加上 `"unclear"`：** 模型無法有信心地選出分類時，誠實的 `"unclear"` 比錯誤的分類好。

### 2.5 語法錯誤與語意錯誤

| 錯誤類型 | 例子 | 緩解方式 |
|---|---|---|
| **語法（syntax）** | 不合法的 JSON、欄位型別錯 | 帶 JSON schema 的 `tool_use`（可完全消除） |
| **語意（semantic）** | 總額加不起來、值放錯欄位、幻覺 | 驗證檢查、帶回饋的 retry、self-correction |

## 第 3 章：Claude Agent SDK — 打造 Agentic 系統

> 文件：[Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) | [Hooks](https://platform.claude.com/docs/en/agent-sdk/hooks) | [Subagents](https://platform.claude.com/docs/en/agent-sdk/subagents) | [Sessions](https://platform.claude.com/docs/en/agent-sdk/sessions)

### 3.1 什麼是 Agentic Loop

Agentic loop 是自主執行任務的核心模式。模型不只是回答，而是執行一連串動作：

```
1. 帶著 tools 向 Claude 送出請求
2. 收到回應
3. 檢查 stop_reason：
   - "tool_use" -> 執行 tool，把結果加進歷史，回到步驟 1
   - "end_turn" -> 任務完成，把結果呈現給使用者
4. 重複直到完成
```

**這是 model-driven（由模型驅動）的做法：** Claude 根據 context 與先前的 tool 結果，決定下一個要呼叫的 tool。這和寫死的決策樹（hard-coded decision tree）不同，後者的動作順序是固定的。

**反模式（要避免）：**

- 解析 assistant 的文字來判斷是否完成（例如找「Task completed」）
- 用任意的迭代上限（例如 `max_iterations=5`）作為主要的停止條件
- 用「assistant 是否輸出了文字內容」作為完成訊號

**正確做法：** 唯一可靠的完成訊號是 `stop_reason == "end_turn"`。

### 3.2 `AgentDefinition` 設定

`AgentDefinition` 是 Claude Agent SDK 中的 agent 設定物件：

```python
agent = AgentDefinition(
    name="customer_support",
    description="Handles customer requests for returns and order issues",
    system_prompt="You are a customer support agent...",
    allowed_tools=["get_customer", "lookup_order", "process_refund", "escalate_to_human"],
    # For a coordinator:
    # allowed_tools=["Task", "get_customer", ...]
)
```

**關鍵參數：**

- `name` / `description`：agent 的識別與描述
- `system_prompt`：含指令的 system prompt
- `allowed_tools`：允許使用的 tool 清單（最小權限原則，principle of least privilege）

### 3.3 Hub-and-Spoke：Coordinator 與 Subagents

多 agent 架構通常採 hub-and-spoke（軸輻式）拓樸：

```
         Coordinator
        /     |      \
   Subagent1  Subagent2  Subagent3
    (search)   (analysis)   (synthesis)
```

**Coordinator 負責：**

- 把任務分解（decompose）成子任務
- 決定需要哪些 subagents（動態選擇）
- 把工作委派給 subagents
- 彙整並驗證結果
- 處理錯誤與 retry
- 把結果回報給使用者

**關鍵原則：subagents 的 context 是隔離的。**

- Subagents **不會**自動繼承 coordinator 的對話歷史
- 所有需要的 context 都必須在 subagent 的 prompt 裡**明確傳入**
- Subagents 在不同呼叫之間不共享記憶
- 所有溝通都經過 coordinator（為了可觀測性與錯誤控制）

### 3.4 用 `Task` Tool 產生 Subagents

Subagents 透過 `Task` tool 產生（spawn）：

```python
# The coordinator's allowedTools must include "Task"
coordinator_agent = AgentDefinition(
    allowed_tools=["Task", "get_customer"]
)
```

**必須明確傳遞 context：**

```
# 不好：subagent 沒有任何 context
Task: "Analyze the document"

# 好：prompt 裡有完整 context
Task: "Analyze the following document.
Document: [full document text]
Prior search results: [web search results]
Output format requirements: [schema]"
```

**平行產生：** coordinator 可以在一次回應中呼叫多個 `Task`，subagents 會平行執行：

```
# 一次 coordinator 回應裡包含：
Task 1: "Search for articles about X"
Task 2: "Analyze document Y"
Task 3: "Search for articles about Z"
# 三個同時執行
```

### 3.5 Agent SDK 的 Hooks

Hooks 讓你能在 agent 生命週期的特定時點攔截與轉換。

**PostToolUse** 在 tool 結果送給模型之前攔截：

```python
# Example: normalize date formats from different MCP tools
@hook("PostToolUse")
def normalize_dates(tool_result):
    # Convert Unix timestamp -> ISO 8601
    # Convert "Mar 5, 2025" -> "2025-03-05"
    return normalized_result
```

**攔截外送呼叫的 hook** 可以阻擋違反政策的動作：

```python
# Example: block refunds above $500
@hook("PreToolUse")
def enforce_refund_limit(tool_call):
    if tool_call.name == "process_refund" and tool_call.args.amount > 500:
        return redirect_to_escalation(tool_call)
```

**關鍵差異：hooks 與 prompt 指令**

| 屬性 | Hooks | Prompt 指令 |
|---|---|---|
| 保證程度 | **確定性（deterministic）**（100%） | **機率性（probabilistic）**（>90%，但不是 100%） |
| 使用時機 | 關鍵商業規則、金融操作、法遵 | 一般偏好、建議、格式 |
| 例子 | 阻擋 > $500 的退款 | 「先嘗試解決再 escalate」 |

**規則：** 當失敗會帶來財務、法律或安全後果時，用 hooks，不要靠 prompt。

## 第 4 章：Model Context Protocol（MCP）

> 文件：[MCP](https://modelcontextprotocol.io/) | [Tools](https://modelcontextprotocol.io/docs/concepts/tools) | [Resources](https://modelcontextprotocol.io/docs/concepts/resources) | [Servers](https://modelcontextprotocol.io/docs/concepts/servers)

### 4.1 什麼是 MCP

Model Context Protocol（MCP）是把外部系統接上 Claude 的開放協定。MCP 定義三種主要的資源型別：

1. **Tools**：agent 可呼叫來執行動作的函式（CRUD 操作、API 呼叫、執行命令）
2. **Resources**：agent 可讀取作為 context 的資料（文件、資料庫 schema、內容目錄）
3. **Prompts**：常見任務的預定義 prompt 模板

### 4.2 MCP Servers

MCP server 是實作 MCP 協定、提供 tools/resources 的 process。連上一個 MCP server 時：

- 所有 tools 會被自動探索（discover）
- 所有已連線 server 的 tools 同時可用
- Tool description 決定模型會怎麼使用它們

### 4.3 設定 MCP Servers

**專案設定（`.mcp.json`）**：供團隊共用：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "jira": {
      "command": "npx",
      "args": ["-y", "mcp-server-jira"],
      "env": {
        "JIRA_TOKEN": "${JIRA_TOKEN}"
      }
    }
  }
}
```

**重點：**

- `.mcp.json` 放在專案根目錄，納入版本控制
- 密鑰用環境變數（`${GITHUB_TOKEN}`），token 本身不會被 commit
- 所有專案貢獻者都能使用

**使用者設定（`~/.claude.json`）**：供個人 / 實驗性質的 server：

- 存在使用者的 home 目錄
- 不透過版本控制分享
- 適合個人實驗與測試

**選擇 server：**

- 標準整合（Jira、GitHub、Slack）優先用現有的社群 MCP servers
- 只有團隊獨有的工作流程才自建 server

### 4.4 MCP 的 `isError` 旗標

MCP tool 遇到錯誤時，回應中用 `isError: true`，告知 agent 這次呼叫失敗了。

**結構化錯誤（好）：**

```json
{
  "isError": true,
  "content": {
    "errorCategory": "transient",
    "isRetryable": true,
    "message": "The service is temporarily unavailable. Timeout while calling the orders API.",
    "attempted_query": "order_id=12345",
    "partial_results": null
  }
}
```

**籠統的錯誤（反模式）：**

```json
{
  "isError": true,
  "content": "Operation failed"
}
```

籠統的錯誤讓 agent 無從決策：該 retry、換個查詢，還是 escalate？

### 4.5 MCP Resources

Resources 是 agent 不需要採取動作就能請求、用來取得 context 的資料：

- 內容目錄（例如所有專案任務的清單、階層式導覽）
- 資料庫 schema（理解資料結構）
- 文件（API reference、內部指南）
- Issue / 任務摘要

**Resource 的優勢：** agent 不需要先做探索性的 tool 呼叫來了解有哪些資料。Resource 直接提供一張「地圖」。

## 第 5 章：Claude Code — 設定與工作流程

> 文件：[Claude Code](https://code.claude.com/docs/en/overview) | [Memory / CLAUDE.md](https://code.claude.com/docs/en/memory) | [Skills](https://code.claude.com/docs/en/skills) | [MCP](https://code.claude.com/docs/en/mcp) | [Hooks](https://code.claude.com/docs/en/hooks) | [Sub-agents](https://code.claude.com/docs/en/sub-agents) | [GitHub Actions](https://code.claude.com/docs/en/github-actions) | [Headless](https://code.claude.com/docs/en/headless)

### 5.1 CLAUDE.md 的層級

CLAUDE.md 是 Claude Code 的指令檔。有三個層級：

```
1. User-level：~/.claude/CLAUDE.md
   - 只適用於該使用者
   - 不透過 VCS 分享
   - 個人偏好與工作習慣

2. Project-level：.claude/CLAUDE.md 或根目錄的 CLAUDE.md
   - 適用於所有專案貢獻者
   - 透過 VCS 管理
   - Coding standards、測試標準、架構決策

3. Directory-level：子目錄中的 CLAUDE.md
   - 處理該目錄下的檔案時才適用
   - 該部分 codebase 特有的慣例
```

**常見錯誤：** 新進成員收不到專案指令，因為指令被放在 `~/.claude/CLAUDE.md`（user-level）而不是 `.claude/CLAUDE.md`（project-level）。

### 5.2 `@path` 語法（檔案匯入）

CLAUDE.md 可以用 `@path` 引用外部檔案，讓設定模組化：

```markdown
# Project CLAUDE.md

Coding standards are described in @./standards/coding-style.md
Test requirements are in @./standards/testing-requirements.md
Project overview is in @README.md and dependencies are in @package.json
```

**`@path` 的規則：**

- `@` 緊接在檔案路徑前（中間不能有空格）
- 支援相對與絕對路徑
- 相對路徑以包含該 import 的檔案為基準解析
- 最多巢狀 5 層

這樣可以避免重複，讓每個 package 只引入相關的標準。

### 5.3 `.claude/rules/` 目錄

`.claude/rules/` 是單一巨大 CLAUDE.md 的替代方案，用來依主題組織規則：

```
.claude/rules/
  testing.md          -- 測試慣例
  api-conventions.md  -- API 慣例
  deployment.md       -- 部署規則
  react-patterns.md   -- React 模式
```

**關鍵功能：用 YAML frontmatter 的 `paths` 做條件式載入：**

```yaml
---
paths: ["src/api/**/*"]
---

For API files, use async/await with explicit error handling.
Each endpoint must return a standard response wrapper.
```

```yaml
---
paths: ["**/*.test.tsx", "**/*.test.ts"]
---

Tests must use describe/it blocks.
Use data factories instead of hardcoding.
Do not mock the database—use a test database.
```

**運作方式：**

- 規則**只在** Claude Code 編輯符合 `paths` pattern 的檔案時才載入
- 節省 context 與 token，不相關的規則不會被載入
- Glob pattern 讓你可以依檔案類型套用慣例，不受所在位置限制（很適合散落各處的測試檔）

**何時用帶 `paths` 的 `.claude/rules/`，何時用 directory-level CLAUDE.md：**

- 帶 `paths` 的 `.claude/rules/`：慣例適用於分散在多個目錄的檔案（測試、migration）
- Directory-level CLAUDE.md：慣例綁定特定目錄、其他地方不需要

### 5.4 自訂 Slash Commands 與 Skills

> **注意：** 目前版本的 Claude Code 已把自訂 commands（`.claude/commands/`）與 skills（`.claude/skills/`）統一。兩種格式都會建立 `/name` 命令。Exam guide 提到的是 `.claude/commands/`，該格式仍受支援。

Slash commands 是用 `/name` 呼叫的可重用 prompt 模板：

**`.claude/commands/` 格式（舊格式，仍支援）：**

```
.claude/commands/
  review.md        -- /review -- 標準 code review
  test-gen.md      -- /test-gen -- 產生測試
```

**`.claude/skills/` 格式（目前格式）：**

```
.claude/skills/
  review/SKILL.md  -- /review -- 帶 frontmatter 設定
  test-gen/SKILL.md
```

**專案 commands**（`.claude/commands/` 或 `.claude/skills/`）：

- 納入 VCS，clone repo 的人都能用
- 確保團隊工作流程一致

**使用者 commands**（`~/.claude/commands/` 或 `~/.claude/skills/`）：

- 個人命令，不透過 VCS 分享
- 用於個人工作流程

### 5.5 Skills — `.claude/skills/`

Skills 是透過 SKILL.md frontmatter 設定的進階命令：

```yaml
---
context: fork
allowed-tools: ["Read", "Grep", "Glob"]
argument-hint: "Path to the directory to analyze"
---

Analyze the code structure in the specified directory.
Output a report on dependencies and architectural patterns.
```

**Frontmatter 參數：**

| 參數 | 說明 |
|---|---|
| `context: fork` | 在隔離的 subagent 中執行 skill。冗長的輸出不會污染主 session |
| `allowed-tools` | 限制可用的 tools（安全考量，例如未允許時 skill 就不能刪檔） |
| `argument-hint` | 不帶參數呼叫時提示需要輸入參數 |

**何時用 skill、何時用 CLAUDE.md：**

- **Skill**：針對特定任務按需（on-demand）呼叫（review、分析、產生）
- **CLAUDE.md**：一律載入的一般標準與慣例

**個人 skills（`~/.claude/skills/`）：**

- 用不同名稱建立個人版本，才不會影響隊友

### 5.6 Planning Mode 與直接執行

**Planning mode：**

- 模型只做調查與規劃，不做修改
- 用 Read、Grep、Glob 探索 codebase
- 產出一份實作計畫供使用者核准
- 沒有副作用的安全探索

**何時用 planning mode：**

- 大規模變更（幾十個檔案）
- 有多種合理做法（microservices：服務邊界怎麼切？）
- 架構決策（用哪個框架？什麼結構？）
- 不熟悉的 codebase（必須先理解才能改）
- 影響 45+ 個檔案的 library migration

**何時直接執行：**

- 有明確 stack trace 的單檔修正
- 加一個驗證檢查
- 已充分理解、沒有歧義的變更

**組合做法：**

1. 用 planning mode 調查與設計
2. 使用者核准計畫
3. 直接執行已核准的計畫

**Explore subagent**：專門用來探索 codebase 的 subagent：

- 把冗長的輸出隔離在主 context 之外
- 只回傳摘要
- 避免多階段任務把 context window 耗盡

### 5.7 `/compact` 命令

`/compact` 是內建的 context 壓縮命令：

- 把先前的歷史摘要化，釋放 context window
- 用於長時間調查、context 被冗長 tool 輸出填滿的 session
- 風險：摘要過程中精確的數值、日期與具體細節可能遺失

### 5.8 `/memory` 命令

`/memory` 是內建的跨 session 記憶管理命令：

- 開啟 `CLAUDE.md` 檔案供編輯，讓你保存筆記、偏好與 context
- 資訊跨 session 保留，啟動時自動載入
- 適合存放專案慣例、使用者偏好、常用命令與目前工作的 context
- 不必每個 session 都重新解釋同樣的指令

### 5.9 Claude Code CLI 用於 CI/CD

**`-p`（或 `--print`）旗標：**

```bash
claude -p "Analyze this pull request for security issues"
```

- 非互動模式：處理 prompt、輸出到 stdout、結束
- 不會等待使用者輸入
- 在 CI/CD pipeline 中執行 Claude 的唯一正確方式

**CI 用的結構化輸出：**

```bash
claude -p "Review this PR" --output-format json --json-schema '{"type":"object",...}'
```

- `--output-format json`：以 JSON 輸出
- `--json-schema`：依 schema 驗證輸出
- 結果可被解析，自動貼成 PR 的 inline comment

**Session context 隔離：**

同一個產生程式碼的 Claude session 往往不擅長 review 自己的產出（模型保有自己的推理 context，比較不會質疑自己的決定）。Review 要用獨立的 instance。

**避免重複留言：**

新 commit 之後重新 review 時，把先前的 review 結果放進 context，並指示 Claude 只回報新的或尚未解決的問題。

### 5.10 `fork_session` 與 Session 管理

**`--resume <session-name>`** 恢復一個具名 session：

```bash
claude --resume investigation-auth-bug
```

- 延續先前的對話與保存的 context
- 適合跨多個 session 的長期調查
- 風險：若檔案在上一個 session 之後有變動，tool 結果可能已過時（stale）

**`fork_session`** 從共同的 context 建立獨立分支：

```
Codebase investigation
         |
    fork_session
    /           \
Approach A:      Approach B:
Redux            Context API
```

- 兩個分支都繼承分歧點之前的 context
- 之後各自獨立發展
- 適合比較不同做法或測試策略

**何時開新 session 而非 resume：**

- Tool 結果已過時（檔案變了）
- 時間過了很久、context 已退化
- 用「以下是我們先前發現的簡短摘要：…」重新開始，比帶著舊 tool 資料 resume 更好

## 第 6 章：Prompt Engineering — 進階技巧

> 文件：[Prompt Engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

### 6.1 Few-shot Prompting

Few-shot prompting 是在 prompt 裡放 2–4 組輸入 / 輸出範例，示範預期的行為。

**為什麼 few-shot 比文字描述更有效：**

- 「be more precise（更精確一點）」這種模糊指令可以有很多種解讀
- 範例能毫無歧義地展示預期格式與決策邏輯
- 模型會把模式泛化到新案例（不只是重複範例）

**Few-shot 範例的類型與使用時機：**

#### 1. 針對模糊情境的範例

```
Request: "My order is broken"
Action: Call get_customer -> lookup_order -> check status.
Rationale: "broken" may mean a damaged item; you need order details.

Request: "Get me a manager"
Action: Immediately call escalate_to_human.
Rationale: The customer explicitly requests a human. Do not attempt to solve autonomously.
```

#### 2. 針對輸出格式的範例

```
Finding example:
{
  "location": "src/auth/login.ts:42",
  "issue": "SQL injection in the username parameter",
  "severity": "critical",
  "suggested_fix": "Use a parameterized query"
}
```

#### 3. 區分可接受與有問題程式碼的範例

```
// Acceptable (do not flag):
const items = data.filter(x => x.active);

// Problem (flag):
const items = data.filter(x => x.active == true); // Use strict equality ===
```

#### 4. 從不同文件格式抽取的範例

```
Document with inline citations:
"As shown in the study (Smith, 2023), the rate is 42%."
-> {"value": "42%", "source": "Smith, 2023", "type": "inline_citation"}

Document with bibliography references:
"The rate is 42%. [1]"
-> {"value": "42%", "source": "reference_1", "type": "bibliography"}
```

#### 5. 非正式度量單位的範例

```
Text: "about two handfuls of rice"
-> {"amount": "~100g", "original_text": "two handfuls", "precision": "approximate"}

Text: "a pinch of salt"
-> {"amount": "~1g", "original_text": "a pinch", "precision": "approximate"}
```

Few-shot 對抽取非正式、非標準的度量單位特別有效，因為這些單位種類太多，純規則式指令涵蓋不了。

**Prompt 裡的格式正規化（normalization）規則：**

用嚴格 JSON schema 做結構化輸出時，在 prompt 中加上正規化規則：

```
Normalization:
- Dates: always ISO 8601 (YYYY-MM-DD); "yesterday" -> compute an absolute date
- Currency: numeric amount + currency code; "five bucks" -> {"amount": 5, "currency": "USD"}
- Percentages: decimal fraction; "half" -> 0.5
```

這可以避免 JSON 語法正確、但值不一致的語意錯誤。

### 6.2 明確標準 vs 模糊指令

**不好（模糊）：**

```
Check code comments for accuracy.
Be conservative—report only high-confidence findings.
```

**好（明確標準）：**

```
Flag a comment as problematic ONLY if:
1. The comment describes behavior that CONTRADICTS the actual code behavior
2. The comment references a non-existent function or variable
3. A TODO/FIXME comment refers to a bug that has already been fixed in code

Do NOT flag:
- Comments that are merely stylistically outdated
- Comments with minor wording inaccuracies
- Missing comments (that is a separate category)
```

**用範例定義嚴重度（severity）標準：**

```
CRITICAL: Runtime failure for users
  Example: NullPointerException while processing a payment

HIGH: Security vulnerability
  Example: SQL injection, XSS, missing authorization checks

MEDIUM: Logic bug without immediate impact
  Example: Wrong sorting, off-by-one error

LOW: Code quality
  Example: Duplication, suboptimal algorithm for small data
```

### 6.3 Prompt Chaining

Prompt chaining 把複雜任務拆成一連串聚焦的步驟：

```
Step 1: 分析 auth.ts（只看局部問題）
       -> 輸出：auth.ts 的問題清單

Step 2: 分析 database.ts（只看局部問題）
       -> 輸出：database.ts 的問題清單

Step 3: 整合檢查（跨檔案的依賴）
       -> 輸出：模組邊界上的問題
```

**為什麼重要：**

- 避免**注意力稀釋（attention dilution）**：模型一次收到太多檔案時，可能漏掉某些檔案的 bug，同時對其他檔案給出浮淺的評論
- 確保每個檔案都有一致的分析品質
- 讓跨檔案的互動可以被單獨分析

**何時用 prompt chaining、何時用動態分解（dynamic decomposition）：**

- **Prompt chaining**：可預測、可重複的任務（code review、檔案 migration）
- **動態分解**：開放式調查，子任務要在執行過程中才會浮現

### 6.4 「訪談（Interview）」模式

在實作方案之前，Claude 先問澄清問題：

```
Claude: "Before implementing caching for the API, a few questions:
1. Which cache invalidation strategy do you prefer—TTL or event-based?
2. Is stale data acceptable when the cache is unavailable?
3. Should caching be per-user or global?
4. What is the expected data volume to cache?"
```

**適用時機：**

- 不熟悉的領域（fintech、醫療、法律系統）
- 有非顯而易見影響的任務（快取策略、失敗模式）
- 有多種可行做法，最佳選擇取決於 context

### 6.5 驗證與帶回饋的 Retry（Retry-with-Feedback）

當抽取出的資料沒通過驗證：

```
Step 1: 從文件抽取資料
Step 2: 驗證（Pydantic、JSON Schema、商業規則）
Step 3: 若有錯，帶著 context 重試：
  - 原始文件
  - 前一次（錯誤的）抽取結果
  - 具體錯誤："Field 'total' = 150, but sum(line_items) = 145. Re-check values."
```

**Retry 會有效的情況：**

- 格式錯誤（日期格式錯）
- 結構錯誤（欄位放錯位置）
- 算術不一致（模型可以重新檢查）

**Retry 沒用的情況：**

- 資訊根本不在來源文件裡
- 需要的 context 在外部（資料在另一份沒提供的文件中）

**Pydantic 作為驗證工具：**

Pydantic 是 Python 的 schema 資料驗證 library。考試重點：

- **結構驗證：** 拿到 Claude 的 JSON 後在程式中檢查型別、必填、enum 限制
- **語意驗證：** 自訂 validator 強制商業邏輯（明細加總等於總額；start_date < end_date）
- **驗證–重試迴圈：** Pydantic 驗證失敗時，組出錯誤訊息並帶著錯誤 context 重新 prompt Claude
- **產生 JSON Schema：** Pydantic model 可以產生給 `tool_use` 用的 JSON Schema，成為單一真實來源（single source of truth）

### 6.6 Self-correction（自我修正）

偵測內部矛盾的模式：

```json
{
  "stated_total": "$150.00",
  "calculated_total": "$145.00",
  "conflict_detected": true,
  "line_items": [
    {"name": "Widget A", "price": 75.00},
    {"name": "Widget B", "price": 70.00}
  ]
}
```

模型同時抽出「文件寫的值」與「計算出來的值」，兩者不同時 `conflict_detected` 讓你可以處理這個差異。

## 第 7 章：Message Batches API

> 文件：[Message Batches](https://platform.claude.com/docs/en/build-with-claude/message-batches)

### 7.1 概觀

Message Batches API 讓你一次送出一批請求做非同步處理：

| 屬性 | 值 |
|---|---|
| 省下的費用 | 比同步呼叫便宜 **50%** |
| 處理時間窗 | 最長 **24 小時**（沒有延遲 SLA 保證） |
| 多回合 tool calling | **不支援**（一個請求 = 一個回應） |
| 對應方式 | 用 `custom_id` 欄位對應請求與回應 |

### 7.2 何時用 Batch API、何時用同步 API

| 任務 | API | 原因 |
|---|---|---|
| Pre-merge 的 PR 檢查 | **同步** | 開發者在等；24 小時不可接受 |
| 隔夜的技術債報告 | **Batch** | 早上要結果就好；省 50% |
| 每週安全稽核 | **Batch** | 不急；省 50% |
| 互動式 code review | **同步** | 需要即時回應 |
| 處理 10,000 份文件 | **Batch** | 大量處理；省很多 |

### 7.3 使用 `custom_id`

```json
{
  "custom_id": "doc-invoice-2024-001",
  "params": {
    "model": "claude-sonnet-4-6",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Extract data from: ..."}]
  }
}
```

`custom_id` 讓你可以：

- 把結果對應回原始文件
- 失敗時只重送失敗的文件
- 避免重複處理已成功的文件

### 7.4 處理 Batch 中的失敗

1. 送出一批 100 份文件
2. 95 份成功；5 份失敗（超過 context 上限）
3. 用 `custom_id` 找出失敗的
4. 調整策略（例如把長文件切成 chunk）
5. 只重送那 5 份失敗的文件

### 7.5 SLA 規劃

若你需要在 30 小時內拿到結果，而 Batch API 最長要 24 小時：

- 送出時間窗：30 - 24 = **6 小時**
- 批次最遲要在期限前 24 小時送出
- 若頻繁送出，切成 4 小時一個窗口

## 第 8 章：任務分解策略

### 8.1 固定 Pipeline（Prompt Chaining）

每個步驟事先定義好：

```
Document -> Metadata extraction -> Data extraction -> Validation -> Enrichment -> Final output
```

**適用時機：**

- 任務結構可預測（review 永遠照同一個模板）
- 所有步驟事先已知
- 需要穩定性與可重現性

### 8.2 動態自適應分解（Dynamic Adaptive Decomposition）

子任務依中間結果產生：

```
1. 「為 legacy codebase 加測試」
2. -> 先：描繪結構（Glob、Grep）
3. -> 發現：3 個模組沒有測試、2 個部分覆蓋
4. -> 排優先：先做 payments 模組（高風險）
5. -> 過程中：發現依賴一個外部 API
6. -> 調整：寫測試前先為外部 API 加 mock
```

**適用時機：**

- 開放式的調查任務
- 事先不知道完整範圍
- 每一步都依賴前一步的結果

### 8.3 多輪（Multi-pass）Code Review

針對 10+ 個檔案的 pull request：

```
Pass 1（逐檔）：分析 auth.ts -> 列出局部問題
Pass 1（逐檔）：分析 database.ts -> 列出局部問題
Pass 1（逐檔）：分析 routes.ts -> 列出局部問題
...
Pass 2（整合）：分析檔案之間的關係
  -> 跨檔案問題：型別不一致、循環依賴
```

**為什麼一次看完 14 個檔案不好：**

- 注意力稀釋：某些檔案分析得深、某些淺
- 評論不一致：同一個模式在一個檔案被標記、在另一個被放行
- 漏掉 bug：認知過載導致明顯錯誤被跳過

## 第 9 章：Escalation 與 Human-in-the-Loop

### 9.1 何時該 Escalate 給人類

**Escalation 觸發條件（明確規則）：**

| 情況 | 動作 |
|---|---|
| 客戶明確要求「找主管來」 | 立即 escalate；不要嘗試自己解決 |
| 政策沒涵蓋這個請求 | Escalate（例如政策沒提到的競品價格比對） |
| Agent 無法取得進展 | 合理次數的嘗試後 escalate |
| 金額超過門檻的財務操作 | Escalate（最好用 hook 強制，不要靠 prompt） |
| 查客戶時出現多筆符合 | 要求額外識別資訊；不要猜 |

**不可靠的觸發條件：**

| 不可靠的方法 | 為什麼會失敗 |
|---|---|
| 情緒分析（sentiment analysis） | 客戶情緒與案件複雜度無關 |
| 模型自評信心（1–10 分） | 模型可能「很有信心地錯」；校準（calibration）差 |
| 自動分類器 | 過度工程；可能需要你沒有的訓練資料 |

### 9.2 Escalation 模式

**立即 escalate：**

```
Customer: "I want to speak to a manager"
Agent: [立即呼叫 escalate_to_human]
不要： "I can help with your issue, let me..."
```

**先嘗試解決再 escalate：**

```
Customer: "My refrigerator broke two days after purchase"
Agent: [查訂單，提供保固換貨]
若客戶不滿意 -> escalate
```

**細膩的 escalate（先同理 → 解決 → 客戶再次要求時 escalate）：**

```
Customer: "This is outrageous, I'm very unhappy with the quality!"
Agent: [同理情緒] "I understand your frustration."
       [提出解法] "I can offer a replacement or a refund."
Customer: "No, I want to talk to someone!"
Agent: [客戶再次堅持 -> 立即 escalate]
```

關鍵原則：先承接情緒，再提出具體解法，只有客戶再次表達想找真人時才 escalate。不要在客戶第一次表達不滿時就 escalate（不滿並不等於要求找主管）。

**因政策空缺而 escalate：**

```
Customer: "Competitor X has this item 30% cheaper—give me a discount"
Policy: 只涵蓋自家網站的價格調整
Agent: [escalate — 政策沒涵蓋競品價格比對]
```

### 9.3 結構化的交接（Handoff）協定

Escalate 時，agent 應把結構化摘要交給人類：

```json
{
  "customer_id": "CUST-12345",
  "customer_name": "Ivan Petrov",
  "issue_summary": "Refund request for a damaged item",
  "order_id": "ORD-67890",
  "root_cause": "Item arrived damaged; photos attached",
  "actions_taken": [
    "Verified customer via get_customer",
    "Confirmed order via lookup_order",
    "Offered a standard replacement — customer insists on a refund"
  ],
  "refund_amount": "$89.99",
  "recommended_action": "Approve a full refund",
  "escalation_reason": "Customer requested to speak with a manager"
}
```

人工客服看不到完整的對話紀錄，只看得到這份摘要。因此它必須完整、可獨立理解。

### 9.4 信心校準（Confidence Calibration）與人工監督

針對資料抽取系統：

1. **欄位層級的信心分數：** 模型對每個抽出的欄位輸出信心分數
2. **校準：** 用有標註的驗證集調整門檻
3. **路由：**
  - 高信心 + 穩定準確率 -> 自動處理
  - 低信心或來源模糊 -> 人工審查

**分層隨機抽樣（stratified random sampling）：**

- 即使是高信心的抽取結果，也要定期稽核樣本
- 整體 97% 的準確率可能掩蓋了某類文件 40% 的錯誤率
- 要依文件類型、依欄位分析準確率，不能只看整體

## 第 10 章：多 Agent 系統的錯誤處理

### 10.1 錯誤分類

| 類別 | 例子 | 可 retry | Agent 動作 |
|---|---|---|---|
| **Transient（暫時性）** | Timeout、503、網路故障 | 是 | 用 exponential backoff retry |
| **Validation（驗證）** | 輸入格式錯、缺必填欄位 | 否（要修輸入） | 修改請求後重試 |
| **Business（商業）** | 違反政策、超過門檻 | 否 | 向使用者說明；提出替代方案 |
| **Permission（權限）** | 存取被拒 | 否 | Escalate |

### 10.2 錯誤處理的反模式

| 反模式 | 問題 | 正確做法 |
|---|---|---|
| 籠統狀態「search unavailable」 | Coordinator 無法決定如何復原 | 回傳錯誤類型、查詢內容、部分結果、替代方案 |
| 靜默吞掉（空結果 = 成功） | Coordinator 以為沒有符合的結果，其實是失敗 | 區分「沒有結果」與「搜尋失敗」 |
| 一個失敗就中止整個 workflow | 所有部分結果都丟了 | 帶著部分結果繼續；標註缺口 |
| Subagent 內無限 retry | 延遲與資源浪費 | 本地復原（1–2 次 retry），然後往上傳給 coordinator |

### 10.3 結構化的 Subagent 錯誤

```json
{
  "status": "partial_failure",
  "failure_type": "timeout",
  "attempted_query": "AI impact on music industry 2024",
  "partial_results": [
    {"title": "AI Music Generation Report", "url": "...", "relevance": 0.8}
  ],
  "alternative_approaches": [
    "Try a narrower query: 'AI music composition tools'",
    "Use an alternative data source"
  ],
  "coverage_impact": "Not covered: AI impact on music production"
}
```

這給了 coordinator 決策所需的資訊：

- 用修改後的查詢 retry？
- 使用部分結果？
- 委派給另一個 subagent？
- 略過這一節並標註缺口？

### 10.4 最終 Synthesis 中的覆蓋範圍標註

```markdown
## Report: AI Impact on Creative Industries

### Visual Art (FULL COVERAGE)
[research results]

### Music (PARTIAL COVERAGE — search agent timeout)
[partial results]
⚠️ Note: coverage for this section is limited due to a timeout in the search agent.

### Literature (FULL COVERAGE)
[research results]
```

## 第 11 章：Production 系統的 Context 管理

### 11.1 把事實抽到獨立區塊

不要依賴對話歷史（摘要時會退化），把關鍵事實抽到一個結構化區塊：

```
=== CASE FACTS（每出現新事實就更新）===
Customer ID: CUST-12345
Order ID: ORD-67890
Order Date: 2025-01-15
Order Amount: $89.99
Issue: Damaged item on delivery
Customer Request: Full refund
Status: Pending manager approval
===
```

不論歷史如何被摘要，每個 prompt 都帶上這個區塊。

### 11.2 裁剪 Tool 結果

若 `lookup_order` 回傳 40+ 個欄位，但目前任務只需要 5 個：

```python
# PostToolUse hook: keep only relevant fields
@hook("PostToolUse", tool="lookup_order")
def trim_order_fields(result):
    return {
        "order_id": result["order_id"],
        "status": result["status"],
        "total": result["total"],
        "items": result["items"],
        "return_eligible": result["return_eligible"]
    }
```

這能節省 context、減少雜訊。

### 11.3 考慮位置的輸入（Position-aware Input）

把關鍵資訊的擺放納入 lost-in-the-middle 效應的考量：

```
[KEY FINDINGS — 放最上面]
Found 3 critical vulnerabilities...

[DETAILED RESULTS — 中間]
=== File auth.ts ===
...
=== File database.ts ===
...

[ACTION ITEMS — 放最後]
Priority: fix auth.ts vulnerabilities before merge.
```

### 11.4 Scratchpad 檔案

長時間調查時，agent 可以把關鍵發現寫進 scratchpad 檔案：

```
# investigation-scratchpad.md
## Key findings
- PaymentProcessor in src/payments/processor.ts inherits from BaseProcessor
- refund() is called from 3 places: OrderController, AdminPanel, CronJob
- External PaymentGateway API has a rate limit of 100 req/min
- Migration #47 added refund_reason (NOT NULL) — 2024-12-01
```

當 context 退化時（或在新 session 裡），agent 可以查 scratchpad，不必重新探索。

### 11.5 委派給 Subagents 以保護 Context

```
Main agent: "Investigate dependencies of the payments module"
  -> Subagent (Explore): 讀 15 個檔案、追蹤 imports
  -> 回傳: "Payments depends on AuthService, OrderModel, and the external PaymentGateway API"

Main agent: context 裡只留一行，而不是 15 個檔案
```

**獨立的 context 層：**

在多 agent 系統中，每個 subagent 都在有限的 context 預算內運作，只收到它任務所需的資訊。Coordinator 扮演獨立的 context 層：彙整 subagent 的輸出、保存全域狀態、分配 context。這避免了「context 洩漏（context leakage）」，也就是某個 agent 用其他 agent 不需要的資訊把 window 吃掉。

**Subagent 的受限 context 預算：**

- 只送最少的 context：具體任務 + 必要資料
- 指示 subagent 回傳結構化結果，而不是原始資料傾倒
- 用 `allowedTools` 限制 subagent 的 tool 集合：tool 越少，干擾越少、context 成本越低

### 11.6 結構化的狀態持久化（用於 crash 復原）

每個 agent 把狀態輸出到已知位置：

```json
// agent-state/web-search-agent.json
{
  "status": "completed",
  "queries_executed": ["AI music 2024", "AI music composition"],
  "results_count": 12,
  "key_findings": [...],
  "coverage": ["music composition", "music production"],
  "gaps": ["music distribution", "music licensing"]
}
```

Coordinator 在 resume 時載入一份 manifest：

```json
// agent-state/manifest.json
{
  "web-search": "completed",
  "doc-analysis": "in_progress",
  "synthesis": "not_started"
}
```

## 第 12 章：保存來源（Provenance）

### 12.1 歸屬（Attribution）流失的問題

摘要多個來源的結果時，「主張 → 來源」的連結可能會斷掉：

```
不好："The AI music market is estimated at $3.2B."（沒有來源、沒有年份）

好：
{
  "claim": "The AI music market is estimated at $3.2B.",
  "source_url": "https://example.com/report",
  "source_name": "Global AI Music Report 2024",
  "publication_date": "2024-06-15",
  "confidence": 0.9
}
```

### 12.2 處理互相矛盾的資料

當兩個來源給出不同的值：

```json
{
  "claim": "Share of AI-generated music on streaming platforms",
  "values": [
    {
      "value": "12%",
      "source": "Spotify Annual Report 2024",
      "date": "2024-03",
      "methodology": "Automated classification"
    },
    {
      "value": "8%",
      "source": "Music Industry Association Survey",
      "date": "2024-07",
      "methodology": "Survey of 500 labels"
    }
  ],
  "conflict_detected": true,
  "possible_explanation": "Difference in methodology and time period"
}
```

不要任意挑一個值。兩個都保留並附上歸屬，讓 coordinator 決定。

### 12.3 附上日期以正確解讀

沒有日期，時間差異可能被誤判為矛盾：

```
不好："Source A says 10%, source B says 15%. Contradiction."
好："Source A (2023) says 10%, source B (2024) says 15%. Likely +5% growth over a year."
```

### 12.4 依內容類型呈現

不要把所有東西硬塞進同一種格式：

- 財務資料 -> 表格
- 新聞與分析 -> 散文
- 技術發現 -> 結構化清單
- 時間序列 -> 依時間排序

## 第 13 章：Claude Code 內建 Tools

### 13.1 Tool 選擇速查

| 任務 | Tool | 例子 |
|---|---|---|
| 依名稱 / pattern 找檔案 | **Glob** | `**/*.test.tsx`、`src/components/**/*.ts` |
| 在檔案內容中搜尋 | **Grep** | 函式名稱、錯誤訊息、import |
| 讀取整個檔案 | **Read** | 載入檔案做分析 |
| 寫新檔案 | **Write** | 從零建立檔案 |
| 精確編輯既有檔案 | **Edit** | 透過唯一的文字比對替換特定片段 |
| 執行 shell 命令 | **Bash** | git、npm、跑測試、build |

### 13.2 漸進式調查策略

不要一次讀完所有檔案。逐步建立理解：

```
1. Grep：找進入點（函式定義、export）
2. Read：讀找到的檔案
3. Grep：找使用處（import、呼叫）
4. Read：讀使用方的檔案
5. 重複直到掌握全貌
```

### 13.3 備援：用 Read + Write 取代 Edit

當 Edit 因為文字比對不唯一而失敗：

1. Read：載入完整檔案內容
2. 用程式修改內容
3. Write：寫回更新後的版本

# 第二部：考試 Domain 筆記

## Domain 1：Agent 架構與編排（27%）

### 1.1 設計自主執行任務的 Agentic Loop

**核心知識：**

- Agent loop 的生命週期：送出 Claude 請求、檢查 `stop_reason`（`"tool_use"` vs `"end_turn"`）、執行 tools、把結果回傳給下一次迭代
- Tool 結果要附加到對話歷史，模型才能決定下一步
- Model-driven 決策（Claude 選下一個 tool）vs 寫死的決策樹

**核心技能：**

- 流程控制：`stop_reason = "tool_use"` 時繼續迴圈，`"end_turn"` 時停止
- 在迭代之間把 tool 結果附加進 context
- 要避免的反模式：解析 assistant 文字判斷完成、用任意的迭代上限作為主要停止機制

### 1.2 編排多 Agent 系統（Coordinator–Subagent）

**核心知識：**

- Hub-and-spoke 架構：coordinator 掌握所有 agent 之間的溝通、錯誤處理與路由
- Subagents 在隔離的 context 中運作，不會自動繼承 coordinator 的歷史
- Coordinator 的職責：任務分解、委派、結果彙整、動態選擇 subagents
- Coordinator 分解得太窄的風險

**核心技能：**

- 把研究範圍切分給不同 subagents 以減少重複
- 實作迭代精煉迴圈（coordinator 評估 synthesis 後重新指派任務）
- 讓所有溝通經過 coordinator 以確保可觀測性

### 1.3 設定 Subagent 呼叫、Context 傳遞與產生

**核心知識：**

- `Task` tool 產生 subagents；coordinator 的 `allowedTools` 必須包含 `"Task"`
- Subagent 的 context 必須明確寫進 prompt；subagents 不繼承父層 context
- `AgentDefinition` 設定：description、system prompt、tool 限制
- 用 `fork_session` 做 session 管理以探索不同方案

**核心技能：**

- 把先前 agent 的完整輸出放進 subagent 的 prompt
- 傳遞 context 時用結構化格式把資料與 metadata 分開
- 在一次 coordinator 回合中用多個 `Task` 呼叫平行產生 subagents
- Coordinator 的 prompt 以目標與品質標準來寫，而非逐步指令

### 1.4 實作帶強制執行與交接模式的多步驟 Workflow

**核心知識：**

- **程式化強制（programmatic enforcement）**（hooks、前置條件）與 **prompt 引導**在 workflow 排序上的差別
- 需要確定性保證時（例如財務操作前必須驗證身分），只靠 prompt 不夠
- Escalation 時的結構化交接協定（customer ID、原因、建議動作）

**核心技能：**

- 程式化的前置條件，在前一步完成前封鎖後續呼叫（例如 `get_customer` 回傳已驗證 ID 前封鎖 `process_refund`）
- 把多面向的客戶請求分解成獨立項目
- Escalate 給人類時產出結構化摘要

### 1.5 用 Agent SDK Hooks 攔截 Tool 呼叫與正規化資料

**核心知識：**

- Hook 模式（例如 `PostToolUse`）在模型消費 tool 結果前攔截
- 攔截外送呼叫的 hooks 用來強制法遵規則（例如阻擋超過門檻的退款）
- Hooks 提供**確定性保證**，prompt 指令只提供**機率性遵循**

**核心技能：**

- 用 `PostToolUse` hooks 正規化資料格式（Unix timestamp、ISO 8601、數字狀態碼）
- 用攔截 hooks 阻擋違反政策的動作並轉向 escalation
- 商業規則要求保證遵循時，選 hooks 而不是 prompt

### 1.6 複雜 Workflow 的任務分解策略

**核心知識：**

- **固定 pipeline**（prompt chaining）vs 依中間結果的**動態自適應分解**
- Prompt chaining：順序步驟（先逐檔分析，再做整合檢查）
- 依發現內容產生子任務的自適應調查計畫

**核心技能：**

- 可預測的多面向 review 用 prompt chaining；開放式調查用動態分解
- 把大型 code review 切成逐檔分析加獨立的跨檔整合檢查
- 分解開放式任務：先描繪結構，再建立有優先順序的計畫

### 1.7 Session 狀態、Resume 與 Fork

**核心知識：**

- `--resume <session-name>` 延續具名 session
- `fork_session` 從共同 context 建立獨立的調查分支
- Resume session 時告知 agent 檔案已變動的重要性
- 帶結構化摘要的新 session 可能比帶著過時結果 resume 更可靠

**核心技能：**

- 用 `--resume` 延續具名的調查 session
- 用 `fork_session` 平行比較不同做法
- 在 resume（context 仍有效）與開新 session（結果已過時）之間做選擇

## Domain 2：Tool 設計與 MCP 整合（18%）

### 2.1 設計描述清楚的 Tool 介面

**核心知識：**

- Tool description 是 LLM 選擇 tool 的**主要機制**；描述太少會導致選擇不可靠
- 包含輸入格式、範例查詢、邊界案例與適用範圍的重要性
- 模糊或重疊的描述會造成錯誤路由
- System prompt 的措辭可能造成與 tool 的非預期關聯

**核心技能：**

- 撰寫能清楚區分每個 tool 與相似替代品的描述
- 重新命名 tools 以消除功能重疊（例如 `analyze_content` -> `extract_web_results`）
- 把通用 tools 拆成有明確輸入 / 輸出契約的專用 tools

### 2.2 為 MCP Tools 實作結構化錯誤回應

**核心知識：**

- MCP tool 回應中的 `isError` 旗標
- **Transient 錯誤**（timeout）、**validation 錯誤**（輸入錯）、**business 錯誤**（違反政策）與 **access/permission 錯誤**的差別
- 籠統的錯誤（「Operation failed」）讓正確的復原決策變得不可能
- 可 retry 與不可 retry 錯誤的差別

**核心技能：**

- 回傳結構化 metadata，例如 `errorCategory`（transient/validation/permission）、`isRetryable` 與人類可讀的訊息
- 商業規則違反用 `retryable: false`，並給使用者清楚的說明
- Transient 失敗在 subagent 內做本地復原；只把解決不了的錯誤往上傳
- 區分存取失敗（要做 retry 決策）與有效的空結果（沒有符合）

### 2.3 在 Agents 間分配 Tools 與設定 `tool_choice`

**核心知識：**

- 每個 agent 的 tools 太多（例如 18 個而非 4–5 個）會**降低** tool 選擇的可靠性
- 擁有超出其專業範圍 tools 的 agent 容易誤用它們
- 限縮的 tool 存取：只給角色相關的 tools，加上少量跨角色的共用工具
- `tool_choice`：`"auto"`、`"any"`，以及強制指定 tool（`{"type": "tool", "name": "..."}`）

**核心技能：**

- 把每個 subagent 的 tool 集合限制在其角色相關範圍
- 用受限的替代品取代通用 tools（例如 `fetch_url` -> `load_document`）
- 用 `tool_choice: "any"` 保證呼叫 tool 而不是文字回答
- 強制指定 tool 以確保執行順序

### 2.4 把 MCP Servers 整合進 Claude Code 與 Agent Workflows

**核心知識：**

- MCP server 的範圍：專案（`.mcp.json`）給團隊 vs 使用者（`~/.claude.json`）給實驗
- `.mcp.json` 中的環境變數替換（例如 `${GITHUB_TOKEN}`）用來管理密鑰
- 所有已連線 MCP servers 的 tools 在連線時被探索並同時可用
- MCP resources 作為「內容目錄」（任務摘要、資料庫 schema）以減少探索性 tool 呼叫

**核心技能：**

- 在專案 `.mcp.json` 中設定共用 MCP servers，token 用環境變數
- 個人 / 實驗性 servers 放在 `~/.claude.json`
- 標準整合優先用社群 MCP servers 而非自建

### 2.5 選擇並運用內建 Tools（Read、Write、Edit、Bash、Grep、Glob）

**核心知識：**

- **Grep**：在檔案內容中搜尋（函式名稱、錯誤訊息、import）
- **Glob**：依名稱 / 副檔名 pattern 找檔案
- **Read/Write**：整檔操作；**Edit**：透過唯一文字比對做精確修改
- Edit 因比對不唯一而失敗時，改用 Read + Write

**核心技能：**

- 內容搜尋用 Grep、依 pattern 找檔案用 Glob
- 漸進式建立理解：先 Grep 找進入點，再 Read 追流程
- 穿過 wrapper 模組追蹤函式的使用

## Domain 3：Claude Code 設定與工作流程（20%）

### 3.1 設定 CLAUDE.md 的層級、範圍與模組化組織

**核心知識：**

- CLAUDE.md 層級：user（`~/.claude/CLAUDE.md`）、project（`.claude/CLAUDE.md` 或根目錄 `CLAUDE.md`）與 directory-level（子目錄的 CLAUDE.md）
- User-level 設定只適用於一位使用者，不透過 VCS 分享
- `@path` 語法引用外部檔案（例如 `@./standards/coding-style.md`）讓 CLAUDE.md 模組化
- 用 `.claude/rules/` 目錄放主題式規則檔，取代單一巨大的 CLAUDE.md

**核心技能：**

- 診斷層級問題（新成員收不到指令，因為指令在 user-level 而非 project-level）
- 用 `@path`（例如 `@./standards/testing.md`）在每個 package 的 CLAUDE.md 中選擇性引入標準
- 把大型 CLAUDE.md 拆成多個 `.claude/rules/` 檔案（testing.md、api-conventions.md、deployment.md）

### 3.2 建立與設定自訂 Slash Commands 與 Skills

**核心知識：**

- **專案 commands** 在 `.claude/commands/`（透過 VCS 分享）vs **使用者 commands** 在 `~/.claude/commands/`
- `.claude/skills/` 中的 skills 用 `SKILL.md` frontmatter：`context: fork`、`allowed-tools`、`argument-hint`
- `context: fork` 在隔離的 subagent context 中執行 skill，不污染主 session
- 個人 skill 變體可放在 `~/.claude/skills/`，用不同名稱

**核心技能：**

- 專案 slash commands 放 `.claude/commands/`，整個團隊都拿得到
- 用 `context: fork` 隔離輸出冗長的 skills
- 用 `allowed-tools` 限制 skill 可用的 tools
- 用 `argument-hint` 提示開發者輸入必要參數

### 3.3 用路徑專屬規則做條件式慣例載入

**核心知識：**

- `.claude/rules/` 檔案可以用 YAML frontmatter 的 `paths`，依 glob pattern 啟用規則
- 路徑範圍的規則**只在**編輯符合的檔案時載入，節省 context 與 token
- 當慣例橫跨多個目錄（例如測試）時，glob 路徑規則比 directory-level CLAUDE.md 更合適

**核心技能：**

- 建立帶 `paths: ["terraform/**/*"]` 的 `.claude/rules/` 檔案，只在處理符合檔案時載入
- 用 glob pattern（`**/*.test.tsx`）依檔案類型套用慣例，不受位置限制
- 慣例橫跨 codebase 時，優先用路徑專屬規則而非 directory-level CLAUDE.md

### 3.4 決定何時用 Planning Mode、何時直接執行

**核心知識：**

- **Planning mode**：用於大規模變更、多種可行做法與架構決策的複雜任務
- **直接執行**：用於簡單、已充分理解的變更（例如加一個驗證）
- Planning mode 讓你在修改前安全地探索 codebase
- Explore subagent 隔離冗長的探索輸出

**核心技能：**

- 有架構影響的任務用 planning mode（microservices、影響 45+ 檔案的 migration）
- 有明確 stack trace、單一檔案的修正直接執行
- 用 Explore subagent 避免多階段任務耗盡 context window
- 組合使用：先 plan 做探索，再 execute 做實作

### 3.5 漸進式改善的迭代精煉

**核心知識：**

- 具體的輸入 / 輸出範例是傳達期望最有效的方式
- **測試驅動迭代**：先寫測試，再依失敗迭代
- 「訪談」模式：Claude 提問以揭露非顯而易見的設計考量
- 何時把所有問題放在一則訊息（互相依賴）vs 分批（彼此獨立）

**核心技能：**

- 提供 2–3 個具體的輸入 / 輸出範例以釐清轉換需求
- 實作前先建立含預期行為、邊界案例與效能需求的測試集
- 用訪談模式揭露設計面向（cache invalidation、失敗模式）
- 為邊界案例提供含範例輸入與預期輸出的具體測試案例

### 3.6 把 Claude Code 整合進 CI/CD Pipeline

**核心知識：**

- 在自動化 pipeline 中用 `-p`（或 `--print`）旗標進入非互動模式
- 用 `--output-format json` 與 `--json-schema` 取得 CI 用的結構化輸出
- CLAUDE.md 為 CI 觸發的 Claude Code 提供專案 context（測試標準、review 標準）
- **Session context 隔離**：產生程式碼的同一個 session，review 起來比獨立 instance 差

**核心技能：**

- 在 CI 中用 `-p` 執行 Claude Code，避免卡在互動輸入
- 用 `--output-format json` + `--json-schema` 取得結構化結果（例如 inline PR comment）
- 新 commit 後重新執行時，把先前的 review 結果納入（只回報新的 / 未修的問題）
- 在 CLAUDE.md 中記錄測試標準與可用的 fixtures，提升測試產生品質
- 產生新測試時把既有測試檔納入 context，避免重複並保持風格一致

## Domain 4：Prompt Engineering 與結構化輸出（20%）

### 4.1 用明確標準設計 Prompt 以提升準確率

**核心知識：**

- 明確標準比模糊指令有效（例如「只在註解與程式碼矛盾時標記」vs「檢查註解的準確性」）
- 「be more conservative」這類籠統指引，效果比具體的分類標準差
- False positive 對開發者信任的影響：某些分類的高誤報率會侵蝕對準確分類的信任

**核心技能：**

- 定義 review 標準：該回報什麼（bug、安全）vs 該忽略什麼（次要風格）
- 暫時停用誤報率高的分類
- 用每個等級的程式碼範例定義明確的嚴重度標準

### 4.2 用 Few-shot Prompting 提升輸出一致性

**核心知識：**

- Few-shot 範例是產出格式一致、可執行輸出最有效的方法
- Few-shot 可以示範模糊案例的處理（tool 選擇、測試覆蓋的缺口）
- Few-shot 幫助模型泛化到新模式，而非只重複預設
- Few-shot 可以減少抽取任務中的幻覺

**核心技能：**

- 針對模糊情境提供 2–4 個附理由的範例
- 用 few-shot 範例展示輸出格式（位置、問題、嚴重度、建議修法）
- 提供區分可接受的程式碼模式與真正問題的範例
- 提供從不同結構文件正確抽取的範例

### 4.3 用 `tool_use` 與 JSON Schema 強制結構化輸出

**核心知識：**

- 帶 JSON Schema 的 `tool_use` 是保證輸出符合 schema、消除 JSON 語法錯誤最可靠的方式
- `tool_choice: "auto"` 時模型可回文字；`"any"` 時必須呼叫 tool；強制指定則選特定 tool
- 嚴格的 JSON Schema 消除語法錯誤，但無法防止語意錯誤（總額加不起來；值放錯欄位）
- Schema 設計：required vs optional 欄位；enum 加「other」與 detail 字串以利擴充

**核心技能：**

- 用 JSON Schema 定義抽取 tools，從 `tool_use` 結果解析資料
- 有多個 schema 時用 `tool_choice: "any"` 保證結構化輸出
- 強制呼叫特定 tool：`tool_choice: {"type": "tool", "name": "extract_metadata"}`
- 來源可能沒有該資訊時，把欄位設為 optional/nullable 以避免捏造值
- 用 `"unclear"`、`"other"` 等 enum 值加 detail 欄位做可擴充的分類

### 4.4 為抽取品質實作驗證、Retry 與回饋迴圈

**核心知識：**

- Retry-with-error-feedback：在 retry prompt 中放入具體的驗證錯誤以引導修正
- 資訊根本不在來源中時，retry 無效
- 回饋迴圈設計：追蹤觸發 finding 的模式（`detected_pattern`）
- 語意錯誤（總額不符）vs 語法錯誤（由 `tool_use` 解決）

**核心技能：**

- 後續 prompt 帶上原始文件、錯誤的抽取結果與具體的驗證錯誤
- 辨識 retry 何時無效（所需資訊只在外部文件中）
- 在 findings 中加入 `detected_pattern` 欄位以分析 false positive
- 同時抽取 `calculated_total` 與 `stated_total` 以偵測差異，設計 self-correction

### 4.5 設計高效的批次處理策略

**核心知識：**

- Message Batches API：省 50%、最長 24 小時處理時間窗、沒有延遲 SLA 保證
- 批次處理適合非阻塞任務（隔夜報告、稽核），不適合阻塞任務（pre-merge 檢查）
- Batch API 不支援單一請求內的多回合 tool calling
- `custom_id` 欄位對應批次中的請求 / 回應

**核心技能：**

- 阻塞式檢查用同步 API；隔夜 / 每週的工作用 Batch API
- 依 SLA 需求規劃批次送出節奏（例如處理需 24 小時、保證 30 小時時用 4 小時窗口）
- 只重送失敗的文件（用 `custom_id` 辨識）
- 大規模處理前先用樣本迭代 prompt

### 4.6 設計多 Instance 與多輪 Review 架構

**核心知識：**

- 自我 review 的限制：模型保有自己的推理 context，比較不會質疑自己的決定
- 獨立的 review instance（沒有產生時的 context）更能找出細微問題
- 多輪 review：逐檔的局部分析加跨檔整合檢查，避免注意力稀釋

**核心技能：**

- 用第二個獨立的 Claude instance review 變更，不帶產生時的 context
- 把多檔 review 拆成逐檔的 pass 加整合 pass 以分析跨檔資料流
- 用帶自評信心的驗證 pass 做校準過的 review 路由

## Domain 5：Context 管理與可靠性（15%）

### 5.1 管理對話 Context 以保留關鍵資訊

**核心知識：**

- 漸進式摘要的風險：數值、百分比與日期被濃縮成模糊的摘要
- Lost-in-the-middle 效應：模型能可靠處理長輸入的開頭與結尾，但可能漏掉中間的發現
- Tool 輸出在 context 中的累積可能與其相關性不成比例（需要 5 個欄位卻有 40+ 個）
- 後續 API 請求要送出完整對話歷史的重要性

**核心技能：**

- 把交易事實抽到摘要歷史之外的持久「case facts」區塊
- 把冗長的 tool 輸出裁剪到相關欄位
- 把關鍵發現放在彙整資料的開頭，並加明確的章節標題
- 要求 subagents 在結構化輸出中包含 metadata（日期、來源）

### 5.2 設計有效的 Escalation 模式與解決歧義

**核心知識：**

- 合適的 escalation 觸發條件：明確要求找真人、政策空缺 / 例外、無法取得進展
- 立即 escalate（明確要求）vs 先嘗試解決（在 agent 範圍內）
- 情緒分析與模型自評信心都不是案件複雜度的可靠代理指標
- 客戶多筆符合時要求額外識別資訊，而不是用啟發式猜測

**核心技能：**

- 在 system prompt 中用 few-shot 範例寫明確的 escalation 標準
- 對明確要求找真人的請求立即執行，不做額外調查
- 政策對特定請求模糊或未提及時 escalate
- Tool 結果有多筆符合時要求額外識別資訊

### 5.3 在多 Agent 系統中實作錯誤傳播策略

**核心知識：**

- 結構化的錯誤 context（失敗類型、查詢、部分結果、替代方案）讓 coordinator 能更聰明地復原
- 區分存取失敗（timeout 需要 retry 決策）與有效的空結果（沒有符合）
- 籠統的錯誤狀態（「search unavailable」）向 coordinator 隱藏了寶貴的 context
- 靜默吞掉錯誤或因單一失敗中止整個 workflow 都是反模式

**核心技能：**

- 回傳結構化的錯誤 context：失敗類型、嘗試了什麼、部分結果、可能的替代方案
- 區分存取失敗與有效的空結果
- Transient 失敗在 subagent 內本地復原；只把不可復原的錯誤帶著部分結果往上傳
- 在 synthesis 中標註覆蓋範圍：哪些有充分支持、哪些仍有缺口

### 5.4 調查大型 Codebase 時高效管理 Context

**核心知識：**

- 長 session 中的 context 退化：模型開始給出不穩定的答案，用「典型模式」代替具體的 class
- Scratchpad 檔案跨 context 邊界保存關鍵發現
- 委派給 subagents 隔離冗長的探索輸出
- 結構化的狀態持久化支援 crash 復原

**核心技能：**

- 針對具體問題產生 subagents，主 agent 只保留高層協調
- 用 scratchpad 檔案存關鍵發現並稍後引用
- 產生下一階段 subagents 前先摘要關鍵發現
- 長時間調查中用 `/compact` 降低 context 用量

### 5.5 設計帶人工監督與信心校準的 Workflow

**核心知識：**

- 整體指標（例如 97% 總準確率）可能掩蓋特定文件類型或欄位的差表現
- 分層隨機抽樣量測高信心抽取結果中的錯誤率
- 用有標註的驗證集做欄位層級的信心校準
- 自動化之前先依文件類型與欄位區段驗證準確率

**核心技能：**

- 實作分層隨機抽樣以偵測新的錯誤模式
- 依文件類型與欄位分析準確率以驗證穩定表現
- 輸出欄位層級的信心分數，並用標註資料校準 review 門檻
- 把低信心或來源模糊的抽取結果路由給人工審查

### 5.6 多來源 Synthesis 中保存來源與處理不確定性

**核心知識：**

- 沒有保存「主張 → 來源」對應的話，摘要時歸屬會流失
- 彙整時必須保存結構化的對應
- 互相矛盾的統計數字要附歸屬標註衝突，而不是任意挑一個
- 附上發表 / 收集日期，避免把時間差異誤讀為矛盾

**核心技能：**

- 要求 subagents 輸出「主張 → 來源」對應（URL、文件名稱、引文）
- 把報告結構化，區分穩定的發現與有爭議的發現
- 保留互相矛盾的值並加註，交給 coordinator 調解
- 附上發表日期以正確解讀時間脈絡
- 依內容類型呈現：財務資料用表格、新聞用散文、技術發現用結構化清單

# 試題

## 範例試題與解析
<!-- quiz -->

### 第 1 題（情境：Customer Support Agent）

**情境：** 資料顯示有 12% 的案例中，agent 跳過 `get_customer`，只用客戶名字就呼叫 `lookup_order`，導致錯誤的退款。

**哪個改法最有效？**

- A) 加一個程式化的前置條件，在 `get_customer` 取得 ID 之前封鎖 `lookup_order` 與 `process_refund` **【正確】**
- B) 改善 system prompt
- C) 加 few-shot 範例
- D) 實作一個路由分類器

**為什麼選 A：** 當關鍵商業邏輯需要特定的 tool 順序時，程式碼提供的是**確定性保證**，這是以 prompt 為基礎的做法（B、C）做不到的。D 解決的是可用性問題，不是 tool 順序。

### 第 2 題（情境：Customer Support Agent）

**情境：** Agent 對訂單相關的問題常常呼叫 `get_customer` 而不是 `lookup_order`。Tool descriptions 很精簡且相似。

**第一步該做什麼？**

- A) 加 few-shot 範例
- B) 擴充每個 tool 的 description，加入輸入格式、範例與適用邊界 **【正確】**
- C) 加一層路由層
- D) 合併這兩個 tools

**為什麼選 B：** Tool description 是模型選擇 tool 的主要機制。這是成本最低、影響最大的修法。A 增加 token 卻沒處理根本原因。C 是過度工程。D 的工程量超過需要。

### 第 3 題（情境：Customer Support Agent）

**情境：** Agent 只解決了 55% 的問題，目標是 80%。它會 escalate 簡單案件，卻試圖自主處理需要政策例外的複雜情況。

**如何改善校準？**

- A) 加入明確的 escalation 標準與 few-shot 範例 **【正確】**
- B) 自評信心（1–10）並自動 escalate
- C) 用歷史資料訓練一個獨立的分類器
- D) 情緒分析

**為什麼選 A：** 它直接處理根本原因：決策邊界不清楚。B 不可靠（模型可能很有信心地錯）。C 是過度工程。D 解決的是另一個問題（情緒 ≠ 複雜度）。

### 第 4 題（情境：Code Generation with Claude Code）

**情境：** 你需要一個做標準 code review 的自訂 `/review` command，整個團隊 clone repo 時就能使用。

**Command 檔案該建在哪裡？**

- A) 專案 repo 裡的 `.claude/commands/` **【正確】**
- B) `~/.claude/commands/`
- C) 根目錄的 `CLAUDE.md`
- D) `.claude/config.json`

**為什麼選 A：** 放在 `.claude/commands/` 的專案 commands 受版本控制，所有人自動可用。B 是個人 commands。C 是放指令的，不是 command 定義。D 不存在。

### 第 5 題（情境：Code Generation with Claude Code）

**情境：** 你需要把 monolith 重構成 microservices（幾十個檔案、服務邊界的決策）。

**該用什麼做法？**

- A) Planning mode：探索 codebase、理解依賴、設計做法 **【正確】**
- B) 直接執行，漸進式修改
- C) 直接執行，事先給詳細指令
- D) 直接執行，遇到困難再切到 planning

**為什麼選 A：** Planning mode 就是為大規模變更、多種可能做法與架構決策設計的。B 有昂貴重工的風險。C 假設你已經知道結構。D 是被動反應。

### 第 6 題（情境：Code Generation with Claude Code）

**情境：** Codebase 不同區域有不同慣例（React、API、資料庫）。測試檔與程式碼放在一起。你希望慣例能自動套用。

**該用什麼做法？**

- A) 帶 YAML frontmatter 與 glob pattern 的 `.claude/rules/` 檔案 **【正確】**
- B) 全部放進根目錄 CLAUDE.md
- C) `.claude/skills/` 裡的 skills
- D) 每個目錄都放 CLAUDE.md

**為什麼選 A：** 帶 glob pattern（例如 `**/*.test.tsx`）的 `.claude/rules/` 能依檔案路徑自動套用慣例，最適合散落各處的測試檔。B 依賴模型自行推斷。C 是手動 / 按需。D 在相關檔案分散在多個目錄時效果不好。

### 第 7 題（情境：Multi-agent Research System）

**情境：** 系統研究「AI 對創意產業的影響」，但報告只涵蓋視覺藝術。Coordinator 把主題分解成：「AI in digital art」、「AI in graphic design」、「AI in photography」。

**原因是什麼？**

- A) Synthesis agent 沒有偵測缺口
- B) Coordinator 把任務分解得太窄 **【正確】**
- C) Web search agent 搜得不夠徹底
- D) Document analysis agent 過濾掉了非視覺類的來源

**為什麼選 B：** Log 顯示 coordinator 只把「創意產業」分解成視覺子題，完全漏掉音樂、文學與電影。Subagents 都正確執行了，問題在於它們被指派了什麼。

### 第 8 題（情境：Multi-agent Research System）

**情境：** 一個 web-search subagent 在研究複雜主題時 timeout。你要設計錯誤資訊如何回傳給 coordinator。

**哪種錯誤傳播方式最能支援聰明的復原？**

- A) 回傳結構化的錯誤 context 給 coordinator：失敗類型、查詢、部分結果與替代方案 **【正確】**
- B) 在 subagent 內做 exponential backoff 自動 retry，然後回傳籠統的「search unavailable」狀態
- C) 在 subagent 內接住 timeout，回傳標記為成功的空結果集
- D) 把 timeout exception 傳到最上層的 handler，終止整個 workflow

**為什麼選 A：** 結構化的錯誤 context 給了 coordinator 決定要用修改後的查詢 retry、換方法，還是帶部分結果繼續所需的一切。B 把 context 藏在籠統狀態後面。C 把失敗偽裝成成功。D 不必要地中止整個 workflow。

### 第 9 題（情境：Multi-agent Research System）

**情境：** Synthesis agent 在合併結果時常需要驗證特定主張。目前需要驗證時，synthesis agent 把控制權交回 coordinator，coordinator 呼叫 web-search agent，再帶著新結果重跑 synthesis。這讓每個任務多了 2–3 次往返、延遲增加 40%。你的評估顯示 85% 的檢查是簡單的事實查核（日期、名字、統計數字），15% 需要更深入的調查。

**如何在維持可靠性的同時降低開銷？**

- A) 給 synthesis agent 一個範圍受限的 `verify_fact` tool 做簡單檢查，複雜的驗證繼續經過 coordinator **【正確】**
- B) 把所有驗證需求累積成一批，最後一起交回 coordinator
- C) 給 synthesis agent 所有 web-search tools 的完整存取權
- D) 主動在每個來源周圍快取額外的 context

**為什麼選 A：** 這是最小權限原則的應用：synthesis agent 剛好拿到處理 85% 常見情況（簡單事實查核）所需的能力，同時保留經 coordinator 中介的路徑處理複雜調查。B 引入阻塞依賴（後面的 synthesis 步驟可能依賴先前已驗證的事實）。C 破壞職責分離。D 依賴無法可靠預測需求的推測性快取。

### 第 10 題（情境：Claude Code for CI）

**情境：** Pipeline 執行 `claude "Analyze this pull request for security issues"`，卻卡住等待互動輸入。

**正確做法是什麼？**

- A) 用 `-p` 旗標：`claude -p "Analyze this pull request for security issues"` **【正確】**
- B) 設定 `CLAUDE_HEADLESS=true`
- C) 把 stdin 重導到 `/dev/null`
- D) 用 `--batch`

**為什麼選 A：** `-p`（或 `--print`）是文件記載的非互動模式執行方式。它處理 prompt、輸出到 stdout、然後結束。其他選項要不是不存在的功能，就是 Unix 層的變通法。

### 第 11 題（情境：Claude Code for CI）

**情境：** 團隊想降低自動化分析的 API 成本。Claude 目前即時服務兩個 workflow：(1) 開發者 merge PR 前必須完成的阻塞式 pre-merge 檢查，(2) 隔夜產生、早上檢視的技術債報告。主管提議把兩者都移到 Message Batches API 以省 50%。

**你該如何評估這個提案？**

- A) 只把技術債報告用批次處理；pre-merge 檢查維持即時呼叫 **【正確】**
- B) 兩個 workflow 都移到批次處理並輪詢完成狀態
- C) 兩者都維持即時呼叫，避免批次結果的排序問題
- D) 兩者都移到批次處理，批次太久就 fallback 到即時

**為什麼選 A：** Message Batches API 省 50%，但處理時間最長 24 小時、沒有延遲 SLA 保證。這對開發者在等的阻塞式 pre-merge 檢查不合適，但對隔夜批次工作（如技術債報告）非常理想。

### 第 12 題（情境：Multi-file Code Review）

**情境：** 一個 pull request 改了 inventory tracking 模組的 14 個檔案。一次看完所有檔案的單輪 review 結果不一致：某些檔案評論詳細、某些浮淺、漏掉明顯的 bug，還有互相矛盾的回饋（同一個模式在一個檔案被標記有問題，在另一個檔案的相同程式碼卻被放行）。

**該如何重構這個 review？**

- A) 拆成聚焦的多輪：先逐檔分析局部問題，再獨立跑一輪整合檢查看跨檔資料流 **【正確】**
- B) 要求開發者把大 PR 拆成 3–4 個檔案的提交
- C) 換成 context window 更大的高階模型，一輪看完 14 個檔案
- D) 獨立跑三次完整 PR review，只回報至少兩次都出現的問題

**為什麼選 A：** 聚焦的多輪直接處理根本原因：一次處理太多檔案時的注意力稀釋。逐檔分析確保一致的深度，獨立的整合檢查抓跨檔問題。B 把負擔推給開發者而沒改善系統。C 是誤解：更大的 context 不會修正注意力品質。D 靠不一致偵測之間的共識，反而會壓掉真正的 bug。

## 模擬試題（76 題）
<!-- quiz -->

> 原文為 60 題、涵蓋 4 個情境，後續補充了 Conversational AI Architecture Patterns 情境的 16 題，共 76 題。題型與難度對應真實考試。可用上方的情境篩選，只練某一類。

### 第 1 題（情境：Multi-agent Research System）

**情境：** Document analysis agent 發現兩個可信來源對同一關鍵指標的統計數字直接矛盾：政府報告說成長 40%，產業分析說 12%。兩個來源看起來都可信，而這個差異可能實質影響研究結論。Document analysis agent 該如何最有效地處理？

**哪個做法最有效？**

- A) 用可信度啟發式挑出最可能正確的數字，用該值完成分析，並加註腳提到差異。
- B) 把兩個數字都放進分析輸出但不標記為矛盾，讓 synthesis agent 依更廣的 context 決定用哪個。
- C) 停止分析並立即 escalate 給 coordinator，請它先決定哪個來源更權威再繼續。
- D) 用兩個數字完成分析，明確標註衝突並附上來源歸屬，讓 coordinator 在交給 synthesis 前決定如何調解。 **【正確】**

**為什麼選 D：** 這個做法保持了職責分離：analysis agent 不阻塞地完成核心工作、保留兩個有清楚歸屬的矛盾值，並正確地把調解交給擁有更廣 context 的 coordinator。

### 第 2 題（情境：Multi-agent Research System）

**情境：** Web-search 與 document-analysis agents 完成任務並把結果回傳給 coordinator。產出整合研究報告的下一步是什麼？

**下一步最合適的是？**

- A) 每個 agent 直接把結果送給 report-writing agent，跳過 coordinator。
- B) Document analysis agent 向 web-search 要結果並在內部合併。
- C) Coordinator 把兩組結果交給 synthesis agent 做統一整合。 **【正確】**
- D) Coordinator 把兩個 agent 的原始輸出串接起來，當成最終結果回傳。

**為什麼選 C：** 在 coordinator–subagent 架構中，coordinator 把兩組結果轉交給 synthesis agent 做集中整合，保有控制權並確保高品質的合併。

### 第 3 題（情境：Multi-agent Research System）

**情境：** Document analysis subagent 處理 PDF 時常失敗：有些檔案有損壞區段觸發 parsing exception、有些有密碼保護、有時 parsing library 在大檔案上 hang 住。目前任何 exception 都會立即終止 subagent 並回傳錯誤給 coordinator，由它決定要 retry、跳過還是讓整個任務失敗。這讓 coordinator 過度介入例行的錯誤處理。哪個架構改善最有效？

**哪個改善最有效？**

- A) 建一個專門的 error-handling agent，透過共用 queue 監控所有失敗並決定復原動作，直接對 subagents 下重啟命令。
- B) 設定 subagent 永遠回傳帶成功狀態的部分結果，把錯誤細節嵌在 metadata；coordinator 把所有回應都視為成功。
- C) 讓 coordinator 在送給 subagent 前先驗證所有文件，拒絕可能造成失敗的文件。
- D) 在 subagent 內對 transient 失敗實作本地復原，只把它解決不了的錯誤 escalate 給 coordinator，並附上已嘗試的步驟與部分結果。 **【正確】**

**為什麼選 D：** 在有能力解決的最低層級處理錯誤。本地復原減少 coordinator 的負擔，同時仍把真正不可復原的問題帶著完整 context 與部分進度往上 escalate。

### 第 4 題（情境：Multi-agent Research System）

**情境：** 在「AI 對創意產業的影響」跑完系統後，你觀察到每個 subagent 都成功完成：web-search agent 找到相關文章、document analysis agent 正確摘要、synthesis agent 產出連貫的文字。但最終報告只涵蓋視覺藝術，完全漏掉音樂、文學與電影。Coordinator log 顯示它把主題分解成三個子任務：「AI in digital art」、「AI in graphic design」、「AI in photography」。最可能的根本原因是？

**最可能的根本原因是？**

- A) Synthesis agent 缺少偵測覆蓋缺口的指令。
- B) Document analysis agent 因為過嚴的相關性標準過濾掉了非視覺類來源。
- C) Coordinator 的任務分解太窄，指派給 subagents 的工作沒有涵蓋所有相關領域。 **【正確】**
- D) Web-search agent 的查詢不夠，應該擴大以涵蓋更多產業。

**為什麼選 C：** Coordinator 只把一個廣泛主題分解成視覺藝術子任務，完全漏掉音樂、文學與電影。既然 subagents 都正確執行了指派的工作，太窄的分解就是明顯的根本原因。

### 第 5 題（情境：Multi-agent Research System）

**情境：** Web-search subagent 只回傳了 5 個要求的來源類別中的 3 個（競品網站與產業報告成功，新聞檔案與社群 feed timeout）。Document analysis subagent 成功處理了所有提供的文件。Synthesis subagent 必須從品質不一的上游輸入產出摘要。哪個錯誤傳播策略最有效？

**哪個錯誤傳播策略最有效？**

- A) 只用成功的來源繼續 synthesis，輸出中不提哪些資料不可用。
- B) Synthesis subagent 回傳錯誤給 coordinator，因資料不完整觸發整體 retry 或任務失敗。
- C) Synthesis subagent 要求 coordinator 用更長的 timeout retry 失敗的來源，再開始 synthesis。
- D) 在 synthesis 輸出中加上覆蓋範圍標註，指出哪些結論有充分支持、哪些因來源不可用而有缺口。 **【正確】**

**為什麼選 D：** 覆蓋範圍標註實作了帶透明度的優雅降級（graceful degradation），保留已完成工作的價值，同時把不確定性往下傳，讓人能對信心做出有依據的判斷。

### 第 6 題（情境：Multi-agent Research System）

**情境：** Document analysis subagent 遇到一個無法解析的損壞 PDF。設計系統的錯誤處理時，處理這個失敗最有效的方式是？

**哪個做法最有效？**

- A) 帶著 context 回傳錯誤給 coordinator agent，讓它決定如何繼續。 **【正確】**
- B) 靜默跳過損壞的文件並繼續處理其餘檔案，避免中斷 workflow。
- C) 用 exponential backoff 自動重試解析三次，再回報失敗。
- D) 丟出 exception 終止整個研究 workflow。

**為什麼選 A：** 帶著 context 回傳錯誤給 coordinator 最有效，因為它讓 coordinator 能做出有依據的決定：跳過檔案、嘗試其他解析方法，或通知使用者，同時保有對失敗的可見度。

### 第 7 題（情境：Multi-agent Research System）

**情境：** Production log 顯示一個持續的模式：像「analyze the uploaded quarterly report」這樣的請求有 45% 被路由到 web-search agent 而不是 document analysis agent。檢視 tool 定義後，你發現 web-search agent 有一個 `analyze_content` tool，描述是「analyzes content and extracts key information」，而 document analysis agent 有一個 `analyze_document` tool，描述是「analyzes documents and extracts key information」。該如何修正錯誤路由的問題？

**該如何修正錯誤路由？**

- A) 加一個前置路由分類器，在 coordinator 決定委派前先偵測使用者指的是上傳檔案還是網頁內容。
- B) 把 web-search 的 tool 改名為 `extract_web_results`，並把描述改成「processes and returns information retrieved from web search and URLs」。 **【正確】**
- C) 在 coordinator prompt 加 few-shot 範例展示正確路由：「使用者上傳季報 → document analysis agent」、「使用者問網頁 → web-search agent」。
- D) 擴充 document analysis tool 的描述，加入「Use for uploaded PDFs, Word docs, and spreadsheets」等用法範例，web-search tool 不動。

**為什麼選 B：** 把 web-search tool 改名為 `extract_web_results` 並把描述改為明確指涉 web search 與 URL，直接消除兩個 tool 名稱與描述之間的語意重疊，移除了根本原因。這讓每個 tool 的用途毫無歧義，coordinator 能可靠地區分 document analysis 與 web search。

### 第 8 題（情境：Multi-agent Research System）

**情境：** 同事提議 document analysis agent 應直接把結果送給 synthesis agent，跳過 coordinator。維持 coordinator 作為 subagents 之間所有溝通中樞的主要優點是什麼？

**維持 coordinator 作為中樞的主要優點是？**

- A) Coordinator 可以觀察所有互動、統一處理錯誤，並決定每個 subagent 該收到什麼資訊。 **【正確】**
- B) Coordinator 把多個請求批次送給 subagents，減少總 API 呼叫數與整體延遲。
- C) 經過 coordinator 路由能啟用 agent 直接互相呼叫無法支援的自動 retry 邏輯。
- D) Subagents 使用隔離的記憶，直接溝通需要只有 coordinator 能做的複雜序列化。

**為什麼選 A：** Coordinator 模式提供對所有互動的集中可見度、跨系統統一的錯誤處理，以及對每個 subagent 收到什麼資訊的精細控制，這些是星狀溝通拓樸的主要優勢。

### 第 9 題（情境：Multi-agent Research System）

**情境：** Web-search subagent 在研究複雜主題時 timeout。你需要設計這個失敗的資訊如何回傳給 coordinator。哪個錯誤傳播方式最能支援聰明的復原？

**哪個錯誤傳播方式最能支援聰明的復原？**

- A) 回傳結構化的錯誤 context 給 coordinator，包含失敗類型、執行的查詢、任何部分結果，以及可能的替代做法。 **【正確】**
- B) 在 subagent 內接住 timeout，回傳標記為成功的空結果集。
- C) 在 subagent 內實作 exponential backoff 自動 retry，用完 retry 後只回傳籠統的「search unavailable」狀態。
- D) 把 timeout exception 直接傳到最上層 handler，終止整個研究 workflow。

**為什麼選 A：** 回傳結構化的錯誤 context（失敗類型、執行的查詢、部分結果與替代做法）給了 coordinator 做聰明復原決策所需的一切（例如用修改後的查詢 retry，或帶部分結果繼續）。它為協調層級的決策保留了最多的 context。

### 第 10 題（情境：Multi-agent Research System）

**情境：** 系統設計時，你給 document analysis agent 一個通用的 `fetch_url` tool，讓它能依 URL 下載文件。Production log 顯示這個 agent 現在常下載搜尋引擎結果頁來做臨時的 web search，這種行為本應經過 web-search agent，結果造成不一致。哪個修法最有效？

**哪個修法最有效？**

- A) 把 `fetch_url` 換成會驗證 URL 指向文件格式的 `load_document` tool。 **【正確】**
- B) 從 document analysis agent 移除 `fetch_url`，所有 URL 抓取都經過 coordinator 路由到 web-search agent。
- C) 實作過濾，阻擋對已知搜尋引擎網域的 `fetch_url` 呼叫，允許其他 URL。
- D) 在 document analysis agent 的 prompt 加指令，`fetch_url` 只能用來下載文件 URL，不能用來搜尋。

**為什麼選 A：** 用會依文件格式驗證 URL 的文件專用 tool 取代通用 tool，在介面層級限制了能力，修正了根本原因。這遵循最小權限原則，讓不想要的搜尋行為變成不可能，而不只是被勸阻。

### 第 11 題（情境：Multi-agent Research System）

**情境：** 研究一個廣泛主題時，你觀察到 web-search agent 與 document analysis agent 調查了相同的子題，導致輸出大量重複。Token 用量幾乎翻倍，研究的廣度或深度卻沒有相應增加。最有效的處理方式是？

**最有效的處理方式是？**

- A) 讓兩個 agent 平行完成，再由 coordinator 在交給 synthesis agent 前去除重疊的結果。
- B) Coordinator 在委派前明確劃分研究空間，指派每個 agent 不同的子題或來源類型。 **【正確】**
- C) 實作共用狀態機制，讓 agents 記錄目前的焦點區域，其他 agent 在執行中動態避免重複。
- D) 改成順序執行：document analysis 在 web search 完成後才跑，用 web-search 結果作為 context 來避免重複。

**為什麼選 B：** 由 coordinator 在委派前明確劃分研究空間最有效，因為它在任何工作開始前就處理了根本原因：不清楚的任務邊界。它保留了平行性，同時避免重複的工作與浪費的 token。

### 第 12 題（情境：Multi-agent Research System）

**情境：** 研究時，web-search subagent 查了三類來源，結果不同：學術資料庫回傳 15 篇相關論文、產業報告回傳「0 results」、專利資料庫回傳「Connection timeout」。設計對 coordinator 的錯誤傳播時，哪個做法能帶來最好的復原決策？

**哪個做法能帶來最好的復原決策？**

- A) 把結果彙整成單一成功百分比指標（例如「67% source coverage」），詳細 log 可按需查看。
- B) 把「timeout」與「0 results」都當成需要 coordinator 介入的失敗回報。
- C) 在內部 retry transient 失敗，只回報持續的錯誤。
- D) 區分需要 retry 決策的存取失敗（timeout）與代表查詢成功的有效空結果（「0 results」）。 **【正確】**

**為什麼選 D：** Timeout（存取失敗）與「0 results」（有效的空結果）是語意不同的結果，需要不同的回應。區分它們讓 coordinator 能 retry 專利資料庫，同時把產業報告的「0 results」當成有效、有資訊量的發現接受。

### 第 13 題（情境：Multi-agent Research System）

**情境：** Production 監控顯示 synthesis 品質不一致。當彙整結果約 75K tokens 時，synthesis agent 能可靠引用前 15K tokens（web-search 標題 / 摘錄）與最後 10K tokens（document analysis 結論）的資訊，卻常漏掉中間 50K tokens 的關鍵發現，即使它們直接回答了研究問題。該如何重構彙整後的輸入？

**該如何重構彙整後的輸入？**

- A) 在彙整前把所有 subagent 輸出摘要到 20K tokens 以下，讓內容落在模型可靠處理的範圍內。
- B) 把 subagent 結果漸進式串流給 synthesis agent，先把 web-search 結果處理完，再加 document analysis 結果。
- C) 在彙整輸入的開頭放一份關鍵發現摘要，並用明確的章節標題組織詳細結果以利導覽。 **【正確】**
- D) 實作輪替，在不同研究任務中交替哪個 subagent 的結果排在前面，確保兩個來源長期下來都有均等的頂端位置。

**為什麼選 C：** 在開頭放關鍵發現摘要利用了 primacy 效應，讓關鍵資訊落在最可靠被處理的位置。加上明確的章節標題幫助模型導覽並關注中段內容，直接緩解「lost in the middle」現象。

### 第 14 題（情境：Multi-agent Research System）

**情境：** 測試中，web-search agent（85K tokens，含網頁內容）與 document analysis agent（70K tokens，含思考鏈）的合併輸出共 155K tokens，但 synthesis agent 在輸入低於 50K tokens 時表現最好。哪個解法最有效？

**哪個解法最有效？**

- A) 修改上游 agents，讓它們回傳結構化資料（關鍵事實、引文、相關性分數）而不是冗長的內容與推理。 **【正確】**
- B) 加一個中間的摘要 agent，在交給 synthesis 前濃縮發現。
- C) 讓 synthesis agent 分批順序處理發現，在呼叫之間維持狀態。
- D) 把發現存進 vector database，給 synthesis agent 搜尋 tools 在工作中查詢。

**為什麼選 A：** 修改上游 agents 回傳結構化資料，在來源端減少 token 量，同時保留關鍵資訊，修正了根本原因。它避免傳遞會膨脹 token、卻無助於 synthesis 步驟的大量網頁內容與推理軌跡。

### 第 15 題（情境：Multi-agent Research System）

**情境：** 測試中，你觀察到 synthesis agent 在合併結果時常需要驗證特定主張。目前需要驗證時，synthesis agent 把控制權交回 coordinator，coordinator 呼叫 web-search agent，再帶結果重新呼叫 synthesis。這每個任務多了 2–3 次迴圈、延遲增加 40%。你的評估顯示 85% 的驗證是簡單事實查核（日期、名字、統計），15% 需要更深入的研究。哪個做法最能在維持系統可靠性的同時降低開銷？

**哪個做法最有效？**

- A) 給 synthesis agent 所有 web-search tools 的存取權，讓它不經 coordinator 迴圈直接處理任何驗證需求。
- B) 讓 synthesis agent 累積所有驗證需求，最後批次交回 coordinator，再一次全部送給 web-search agent。
- C) 讓 web-search agent 在初始研究時主動快取每個來源周圍的額外 context，預期 synthesis 會需要驗證。
- D) 給 synthesis agent 一個範圍受限的 `verify_fact` tool 做簡單檢查，複雜驗證則經 coordinator 路由到 web-search agent。 **【正確】**

**為什麼選 D：** 範圍受限的事實驗證 tool 讓 synthesis agent 直接處理 85% 的簡單檢查，消除大多數迴圈，同時保留 coordinator 委派路徑處理 15% 的複雜驗證。這在大幅降低延遲的同時應用了最小權限原則。

### 第 16 題（情境：Claude Code for Continuous Integration）

**情境：** 你的 CI pipeline 以 `--print` 模式執行 Claude Code CLI，用 CLAUDE.md 提供 code review 的專案 context，開發者普遍認為 review 有料。但他們回報把 findings 整合進工作流程很困難：Claude 輸出的是敘述性段落，得手動複製到 PR 留言。團隊想把每個 finding 自動貼成程式碼相關位置的獨立 inline PR comment，這需要含檔案路徑、行號、嚴重度與建議修法的結構化資料。哪個做法最有效？

**哪個做法最有效？**

- A) 在 CLAUDE.md 加一節「Output Format for Review」，附結構化 finding 的範例，讓 Claude 從專案 context 學到預期格式。
- B) 用 CLI 旗標 `--output-format json` 與 `--json-schema` 強制結構化 findings，再解析輸出透過 GitHub API 貼 inline comment。 **【正確】**
- C) 在 review prompt 中放明確的格式指令，要求每個 finding 遵循像 `[FILE:path] [LINE:n] [SEVERITY:level] ...` 的可解析模板。
- D) 維持敘述性 review 格式，但加一個摘要步驟，用 Claude 產生 findings 的結構化 JSON 摘要。

**為什麼選 B：** 用 `--output-format json` 搭配 `--json-schema` 在 CLI 層級強制結構化輸出，保證含所需欄位（檔案路徑、行號、嚴重度、建議修法）的良構 JSON，可被可靠地解析並透過 GitHub API 貼成 inline PR comment。它利用了專為結構化輸出設計的內建 CLI 能力。

### 第 17 題（情境：Claude Code for Continuous Integration）

**情境：** 團隊用 Claude Code 產生程式碼建議，但你注意到一個模式：非顯而易見的問題（會破壞邊界案例的效能優化、意外改變行為的清理）只有在另一位團隊成員 review PR 時才被抓到。Claude 在產生時的推理顯示它有考慮過這些案例，但結論是自己的做法正確。哪個做法直接處理了這個自我檢查限制的根本原因？

**哪個做法直接處理了根本原因？**

- A) 用第二個獨立的 Claude Code instance review 變更，不讓它存取產生者的推理。 **【正確】**
- B) 在產生階段啟用 extended thinking 模式，讓它在產出建議前更徹底地思考。
- C) 在產生 prompt 加明確的自我 review 指令，要 Claude 在定稿前批評自己的建議。
- D) 在 prompt context 中放完整的測試檔與文件，讓 Claude 在產生時更了解預期行為。

**為什麼選 A：** 第二個不能存取產生者推理的獨立 Claude Code instance 直接處理了根本原因：避免確認偏誤（confirmation bias）。這種「新鮮眼光」的觀點對應人類的 peer review，另一位 reviewer 會抓到作者自己合理化掉的問題。

### 第 18 題（情境：Claude Code for Continuous Integration）

**情境：** 你的 code review 元件是迭代式的：Claude 分析變更的檔案，然後可能透過 tool 呼叫請求相關檔案（imports、base classes、tests）以理解 context，再給出最終回饋。你的應用定義了一個讓 Claude 請求檔案內容的 tool；Claude 呼叫 tool、拿到結果、繼續分析。你在評估用批次處理降低 API 成本。考慮批次處理這個 workflow 時，主要的技術限制是什麼？

**主要的技術限制是什麼？**

- A) 批次處理沒有 correlation ID 可以把輸出對應回輸入請求。
- B) 非同步模型無法在請求中途執行 tools 並回傳結果讓 Claude 繼續分析。 **【正確】**
- C) Batch API 不支援在請求參數中放 tool 定義。
- D) 批次處理最長 24 小時的延遲對 pull request 回饋太慢，但 workflow 其他部分可以運作。

**為什麼選 B：** 「射後不理（fire-and-forget）」的非同步 Batch API 模型沒有機制能在請求中攔截 tool 呼叫、執行 tool、再回傳結果讓 Claude 繼續分析。這與需要在單一邏輯互動中多回合 tool 請求 / 回應的迭代式 tool-calling workflow 根本上不相容。

### 第 19 題（情境：Claude Code for Continuous Integration）

**情境：** 你的 CI/CD 系統跑三種 Claude 分析：(1) 每個 PR 都跑、完成前阻擋 merge 的快速風格檢查，(2) 每週對整個 codebase 的全面安全稽核，(3) 每晚對最近變更模組的測試案例產生。Message Batches API 省 50%，但處理最長 24 小時。你想在維持可接受的開發者體驗下優化 API 成本。哪個組合正確地把每個任務對應到 API 做法？

**哪個組合正確？**

- A) 三個任務都用 Message Batches API 以最大化 50% 節省，設定 pipeline 輪詢批次完成。
- B) PR 風格檢查用同步呼叫；每週安全稽核與每晚測試產生用 Message Batches API。 **【正確】**
- C) 三個任務都用同步呼叫以維持一致的回應時間，依賴 prompt caching 降低各工作負載的成本。
- D) PR 風格檢查與每晚測試產生用同步呼叫；只有每週安全稽核用 Message Batches API。

**為什麼選 B：** PR 風格檢查阻擋開發者，需要同步呼叫的即時回應；每週安全稽核與每晚測試產生是期限彈性的排程任務，可容忍最長 24 小時的批次窗口，兩者都能省 50%。

### 第 20 題（情境：Claude Code for Continuous Integration）

**情境：** 你的自動化 review 找到真實問題，但開發者回報回饋不可執行。Findings 包含「complex ticket routing logic」或「potential null pointer」這類措辭，卻沒說到底該改什麼。當你加上「always include concrete fix suggestions」這類詳細指令時，模型仍產出不一致的輸出：有時詳細、有時模糊。哪個 prompting 技巧最能可靠地產出一致可執行的回饋？

**哪個 prompting 技巧最可靠？**

- A) 進一步精煉指令，對回饋格式的每個部分（位置、問題、嚴重度、建議修法）給更明確的要求。
- B) 擴大 context window 以納入更多周邊 codebase，讓模型有足夠資訊提出具體修法。
- C) 實作兩階段做法：一個 prompt 找問題、第二個產生修法，讓各自專精。
- D) 加 3–4 個 few-shot 範例展示確切要求的格式：找到的問題、程式碼位置、具體修法建議。 **【正確】**

**為什麼選 D：** 當指令本身產生不穩定結果時，few-shot 範例是達成一致輸出格式最有效的技巧。提供 3–4 個展示確切結構（問題、位置、具體修法）的範例，給模型一個可遵循的具體模式，比抽象指令更可靠。

### 第 21 題（情境：Claude Code for Continuous Integration）

**情境：** 你的 CI pipeline 有兩種 Claude code review 模式：一個 pre-merge-commit hook 在完成前阻擋 PR merge，另一個「deep analysis」在夜間執行、輪詢批次完成、再把詳細建議貼到 PR。你想用省 50% 但需要輪詢、最長 24 小時的 Message Batches API 降低 API 成本。哪個模式該用批次處理？

**哪個模式該用批次處理？**

- A) 只有 pre-merge-commit hook。
- B) 只有 deep analysis。 **【正確】**
- C) 兩個模式都用。
- D) 兩個都不用。

**為什麼選 B：** Deep analysis 是批次處理的理想候選，因為它本來就在夜間執行、能容忍延遲，而且在發布結果前用輪詢模型，正好對應 Message Batches API 非同步、輪詢式的架構，同時省下 50%。

### 第 22 題（情境：Claude Code for Continuous Integration）

**情境：** 你的自動化 review 分析註解與 docstring。目前 prompt 指示 Claude「check that comments are accurate and up to date」。Findings 常標記可接受的模式（TODO 標記、簡單描述），卻漏掉描述程式碼已不再實作行為的註解。什麼改變能處理這種不一致分析的根本原因？

**什麼改變能處理根本原因？**

- A) 提供 `git blame` 資料，讓 Claude 能辨識早於最近程式碼變更的註解。
- B) 加誤導性註解的 few-shot 範例，幫模型辨識 codebase 中的類似模式。
- C) 在分析前過濾掉 TODO、FIXME 與描述性註解模式以減少雜訊。
- D) 指定明確標準：只在註解宣稱的行為與程式碼實際行為矛盾時才標記。 **【正確】**

**為什麼選 D：** 明確標準（只在宣稱行為與實際程式碼行為矛盾時標記）直接處理根本原因：用精確的問題定義取代模糊指令。這減少對可接受模式的誤報，也減少漏掉真正誤導性註解。

### 第 23 題（情境：Claude Code for Continuous Integration）

**情境：** 你的自動化 code review 系統嚴重度評級不一致：類似的問題（如 null pointer 風險）在某些 PR 被評「critical」、在其他 PR 只有「medium」。開發者調查顯示不信任感增加：很多人開始不看就忽略 findings，因為「一半是錯的」。高誤報率的分類侵蝕了對準確分類的信任。哪個做法最能在改善系統的同時恢復開發者信任？

**哪個做法最能恢復開發者信任？**

- A) 暫時停用高誤報率的分類（風格、命名、文件），只保留高精確度的分類，同時改善 prompt。 **【正確】**
- B) 保留所有分類，但在每個 finding 顯示信心分數，讓開發者決定要調查什麼。
- C) 保留所有分類，並在接下來幾週加 few-shot 範例改善每個分類的準確率。
- D) 對所有分類一致地降低嚴格度，把整體誤報率壓下來。

**為什麼選 A：** 暫時停用高誤報率的分類能立即停止信任的侵蝕，移除讓開發者忽略一切的雜訊 findings，同時保留安全與正確性等高精確度分類的價值。它也為在重新啟用前改善問題分類的 prompt 創造空間。

### 第 24 題（情境：Claude Code for Continuous Integration）

**情境：** 你的自動化 review 為每個 PR 產生測試案例建議。Review 一個新增課程完成追蹤的 PR 時，Claude 建議了 10 個測試案例，但開發者回饋顯示其中 6 個重複了既有測試套件已涵蓋的情境。什麼改變最能有效減少重複建議？

**什麼改變最有效？**

- A) 把既有測試檔放進 context，讓 Claude 能判斷哪些情境已被涵蓋。 **【正確】**
- B) 把要求的建議數從 10 降到 5，假設 Claude 會優先提出最有價值的案例。
- C) 加指令要 Claude 只專注於邊界案例與錯誤條件，而非成功路徑。
- D) 實作後處理，用關鍵字重疊過濾掉描述與既有測試名稱相符的建議。

**為什麼選 A：** 放入既有測試檔修正了重複的根本原因：只有知道已有哪些測試，Claude 才能避免建議已涵蓋的情境。這給了 Claude 提出真正新穎、有價值測試所需的資訊。

### 第 25 題（情境：Claude Code for Continuous Integration）

**情境：** 初始自動化 review 找出 12 個 findings 後，開發者推了新 commit 處理問題。重跑 review 產生 8 個 findings，但開發者回報其中 5 個重複了先前的評論，而那些程式碼已在新 commit 中修好。在維持徹底性的同時消除這種多餘回饋最有效的方式是？

**消除多餘回饋最有效的方式是？**

- A) 只在 PR 建立時與最終 pre-merge 狀態跑 review，跳過中間的 commit。
- B) 加後處理過濾器，在貼留言前移除檔案路徑與問題描述與先前相符的 findings。
- C) 把 review 範圍限制在最近一次 push 變更的檔案，排除較早 commit 的檔案。
- D) 把先前的 review findings 放進 context，並指示 Claude 只回報新的或仍未解決的問題。 **【正確】**

**為什麼選 D：** 把先前的 review findings 放進 context 讓 Claude 能區分新問題與已在最近 commit 處理的問題。這保留了 review 的徹底性，同時用 Claude 的推理避免對已修好的程式碼給多餘回饋。

### 第 26 題（情境：Claude Code for Continuous Integration）

**情境：** 你的 pipeline 腳本執行 `claude "Analyze this pull request for security issues"`，但 job 無限期卡住。Log 顯示 Claude Code 在等待互動輸入。在自動化 pipeline 中執行 Claude Code 的正確做法是？

**正確做法是？**

- A) 加 `--batch` 旗標：`claude --batch "Analyze this pull request for security issues"`。
- B) 加 `-p` 旗標：`claude -p "Analyze this pull request for security issues"`。 **【正確】**
- C) 把 stdin 重導到 `/dev/null`：`claude "Analyze this pull request for security issues" < /dev/null`。
- D) 執行命令前設定環境變數 `CLAUDE_HEADLESS=true`。

**為什麼選 B：** `-p`（或 `--print`）旗標是文件記載的非互動執行方式。它處理 prompt、把結果印到 stdout，然後不等待使用者輸入就結束，最適合 CI/CD pipeline。

### 第 27 題（情境：Claude Code for Continuous Integration）

**情境：** 一個 pull request 改了 inventory tracking 模組的 14 個檔案。一次分析所有檔案的單輪 review 結果不一致：某些檔案回饋詳細、某些浮淺、漏掉明顯 bug，還有矛盾的回饋（一個模式在某檔案被標記，同一 PR 另一檔案的相同程式碼卻被放行）。該如何重構 review？

**該如何重構 review？**

- A) 獨立跑三次完整 PR review，只標記三次中至少兩次出現的問題。
- B) 拆成聚焦的多輪：先逐檔 review 局部問題，再跑一輪獨立的整合導向檢查看跨檔資料流。 **【正確】**
- C) 要求開發者在跑自動化 review 前把大 PR 拆成 3–4 個檔案的小提交。
- D) 換成 context window 更大的模型，讓它能在一輪中對 14 個檔案都投入足夠注意力。

**為什麼選 B：** 聚焦的逐檔 pass 處理了根本原因（注意力稀釋），確保一致的深度與可靠的局部問題偵測。獨立的整合導向 pass 再涵蓋跨檔的關注點，例如依賴與資料流的互動。

### 第 28 題（情境：Claude Code for Continuous Integration）

**情境：** 你的自動化 code review 每個 pull request 平均 15 個 findings，開發者回報 40% 的誤報率。瓶頸在調查時間：開發者必須點進每個 finding 讀 Claude 的理由，才能決定要修還是忽略。你的 CLAUDE.md 已經有完整的可接受模式規則，而利害關係人拒絕任何在開發者看到前過濾 findings 的做法。什麼改變最能處理調查時間？

**什麼改變最能處理調查時間？**

- A) 要求 Claude 在每個 finding 中直接附上理由與信心估計。 **【正確】**
- B) 加一個後處理器分析 finding 模式，自動壓掉符合歷史誤報特徵的 findings。
- C) 把 findings 分成「blocking issues」與「suggestions」，各層級有不同的 review 要求。
- D) 設定 Claude 只顯示高信心的 findings，在開發者看到前過濾掉不確定的標記。

**為什麼選 A：** 在每個 finding 直接附上理由與信心，讓開發者不必點開每個 finding 就能快速分流，減少調查時間。它滿足「不過濾」的限制，因為所有 findings 仍然可見，同時加速開發者的決策。

### 第 29 題（情境：Claude Code for Continuous Integration）

**情境：** 分析你的自動化 code review 顯示不同 finding 分類的誤報率差異很大：安全 / 正確性 findings 8%、效能 findings 18%、風格 / 命名 findings 52%、文件 findings 48%。開發者調查顯示不信任感增加：很多人開始不看就忽略 findings，因為「一半是錯的」。高誤報率的分類侵蝕了對準確分類的信任。哪個做法最能在改善系統的同時恢復開發者信任？

**哪個做法最能恢復開發者信任？**

- A) 暫時停用高誤報率的分類（風格、命名、文件），只保留高精確度的分類，同時改善 prompt。 **【正確】**
- B) 保留所有分類，但在每個 finding 顯示信心分數，讓開發者決定要調查什麼。
- C) 保留所有分類，並在接下來幾週加 few-shot 範例改善每個分類的準確率。
- D) 對所有分類一致地降低嚴格度，把整體誤報率壓下來。

**為什麼選 A：** 暫時停用高誤報率的分類能立即停止信任的侵蝕，移除讓開發者忽略一切的雜訊 findings，同時保留安全與正確性等高精確度分類的價值。它也為在重新啟用前改善問題分類的 prompt 創造空間。

### 第 30 題（情境：Claude Code for Continuous Integration）

**情境：** 團隊想降低自動化分析的 API 成本。目前同步的 Claude 呼叫支撐兩個 workflow：(1) 開發者 merge 前必須完成的阻塞式 pre-merge 檢查，(2) 夜間產生、隔天早上檢視的技術債報告。主管提議把兩者都移到 Message Batches API 省 50%。你該如何評估這個提案？

**你該如何評估這個提案？**

- A) 兩者都移到批次處理，批次太久就 fallback 到同步呼叫。
- B) 兩個 workflow 都移到批次處理，用狀態輪詢確認完成。
- C) 只把技術債報告用批次處理；pre-merge 檢查維持同步呼叫。 **【正確】**
- D) 兩個 workflow 都維持同步呼叫，避免批次結果排序的問題。

**為什麼選 C：** Message Batches API 處理最長 24 小時、沒有延遲 SLA，這對夜間技術債報告可接受，但對開發者在等的阻塞式 pre-merge 檢查不可接受。這依延遲需求把每個 workflow 對應到正確的 API。

### 第 31 題（情境：Code Generation with Claude Code）

**情境：** 你請 Claude Code 實作一個把 API 回應轉成內部正規化格式的函式。兩次迭代後，輸出結構仍不符預期：某些欄位巢狀方式不同、timestamp 格式錯誤。你用散文描述需求，但 Claude 每次解讀都不一樣。

**下一次迭代哪個做法最有效？**

- A) 寫一份描述預期輸出結構的 JSON schema，每次迭代後用它驗證 Claude 的輸出。
- B) 提供 2–3 個具體的輸入–輸出範例，展示代表性 API 回應的預期轉換。 **【正確】**
- C) 用更精確的技術語言重寫需求，明確指定欄位對應、巢狀規則與 timestamp 格式字串。
- D) 請 Claude 解釋它目前對需求的理解，找出解讀分歧的地方。

**為什麼選 B：** 具體的輸入–輸出範例透過直接展示預期的轉換結果，消除了散文描述固有的歧義。這直接處理了根本原因（對文字需求的誤解），為欄位巢狀與 timestamp 格式提供毫無歧義的模式。

### 第 32 題（情境：Code Generation with Claude Code）

**情境：** 你需要新增 Slack 作為通知管道。既有 codebase 對 email、SMS 與 push 管道有清楚、成熟的模式。但 Slack 的 API 提供根本不同的整合方式：incoming webhooks（簡單、單向）、bot tokens（支援送達確認與程式化控制）、Slack Apps（雙向事件、需要 workspace 核准）。你的任務只說「add Slack support」，沒指定整合方式，也沒要求送達追蹤等進階功能。

**該如何處理這個任務？**

- A) 用 incoming webhooks 直接在執行模式開始，對應既有的單向通知模式。
- B) 切到 planning mode 探索整合選項與架構影響，在實作前提出建議。 **【正確】**
- C) 直接在執行模式開始，用既有模式建 Slack channel class 的骨架，延後整合方式的決定。
- D) 用 bot-token 做法直接在執行模式開始，確保送達確認可行。

**為什麼選 B：** Slack 整合有多個合理做法，架構影響差異顯著，而需求模糊。Planning mode 讓你能評估 webhooks、bot tokens 與 Slack Apps 之間的取捨，在實作前先對齊做法。

### 第 33 題（情境：Code Generation with Claude Code）

**情境：** 你的 CLAUDE.md 已長到 400+ 行，包含 coding standards、測試慣例、詳細的 PR review checklist、部署指令與資料庫 migration 程序。你希望 Claude 永遠遵守 coding standards 與測試慣例，但只在做那些任務時才套用 PR review、部署與 migration 的指引。

**哪個重構做法最有效？**

- A) 把所有指引移到依 workflow 類型組織的獨立 Skills 檔案，CLAUDE.md 只留簡短的專案描述。
- B) 全部留在 CLAUDE.md，但用 `@import` 語法組織成依類別分開維護的檔案。
- C) 把 CLAUDE.md 拆成 `.claude/rules/` 下帶路徑綁定 glob pattern 的檔案，每條規則只為相關檔案類型載入。
- D) 通用標準留在 CLAUDE.md，為 workflow 專屬的指引（PR review、部署、migration）建立帶觸發關鍵字的 Skills。 **【正確】**

**為什麼選 D：** CLAUDE.md 的內容在每個 session 都載入，確保 coding standards 與測試慣例永遠適用；Skills 則在 Claude 偵測到觸發關鍵字時按需呼叫，最適合 PR review、部署與 migration 等 workflow 專屬指引。

### 第 34 題（情境：Code Generation with Claude Code）

**情境：** 你負責把團隊的 monolith 應用重構成 microservices。這會影響幾十個檔案的變更，需要對服務邊界與模組依賴做決策。

**該選哪個做法？**

- A) 切到 planning mode 探索 codebase、理解依賴，並在修改前設計實作做法。 **【正確】**
- B) 直接在執行模式開始，實作中遇到意外複雜度才切到 planning。
- C) 直接在執行模式開始做漸進式修改，讓實作揭露自然的服務邊界。
- D) 直接執行，事先給指定每個服務結構的詳細指令。

**為什麼選 A：** Planning mode 是拆 monolith 這類複雜架構重構的正確策略：它允許在對許多檔案做出可能很昂貴的變更前，安全探索並對邊界做出有依據的決策。

### 第 35 題（情境：Code Generation with Claude Code）

**情境：** 團隊建了一個 `/analyze-codebase` skill 做深度程式碼分析：依賴掃描、測試覆蓋計數與程式碼品質指標。執行後，團隊成員回報 Claude 在該 session 變得比較不靈敏，還會忘記原本任務的 context。

**如何在保留完整分析能力的同時最有效地修正？**

- A) 在 skill frontmatter 加 `context: fork`，在隔離的 subagent context 中執行分析。 **【正確】**
- B) 在 frontmatter 加 `model: haiku`，用更快更便宜的模型做分析。
- C) 把 skill 拆成三個較小的 skills，各自產生較少輸出。
- D) 在 skill 加指令，顯示前把所有結果壓成簡短摘要。

**為什麼選 A：** `context: fork` 在隔離的 subagent context 中執行分析，大量輸出不會污染主 session 的 context window，Claude 也不會忘記原本任務。它保留完整分析能力，同時讓主 session 保持靈敏。

### 第 36 題（情境：Code Generation with Claude Code）

**情境：** 團隊在 `.claude/skills/commit/SKILL.md` 用一個 `/commit` skill。一位開發者想為自己的個人工作流程客製它（不同的 commit message 格式、額外檢查），又不影響隊友。

**你會建議什麼？**

- A) 在 `~/.claude/skills/` 下用不同名稱建立個人版本，例如 `/my-commit`。 **【正確】**
- B) 在專案 skill frontmatter 加依使用者名稱的條件邏輯。
- C) 在 `~/.claude/skills/commit/SKILL.md` 建立同名的個人版本。
- D) 在個人 skill frontmatter 設 `override: true`，讓它優先於專案版本。

**為什麼選 A：** 同名的個人 skill 會優先於專案 skill，所以沿用 `commit` 這個名字會讓這位開發者默默遮蔽（shadow）團隊的 skill：團隊改善 `/commit` 時他收不到更新，還得記住自己跑的是同名的不同 skill。把個人變體命名為 `/my-commit` 完全避開衝突：開發者繼續使用團隊維護的 `/commit`，同時有一個名稱清楚的個人 skill，不會混淆也不會漏掉團隊更新。

### 第 37 題（情境：Code Generation with Claude Code）

**情境：** 團隊用 Claude Code 好幾個月了。最近三位開發者回報 Claude 遵守「always include comprehensive error handling」這條指引，但剛加入的第四位開發者說 Claude 不遵守。四人在同一個 repo 工作，程式碼都是最新的。

**最可能的原因與修法是？**

- A) 指引在原本三位開發者的 user-level `~/.claude/CLAUDE.md` 裡，不在專案的 `.claude/CLAUDE.md`。把指令移到 project-level 檔案，所有團隊成員都會收到。 **【正確】**
- B) 新開發者的 `~/.claude/CLAUDE.md` 有衝突的指令覆蓋了專案設定；他們應該刪掉衝突的段落。
- C) Claude Code 會隨時間學習每位使用者的偏好；新開發者必須重複這個要求直到 Claude「記住」。
- D) Claude Code 第一次讀取後會快取 CLAUDE.md；原本的開發者用的是快取版本。所有人都應該清除 Claude Code 快取。

**為什麼選 A：** 如果指引只加在原本開發者的 user-level 設定，而沒放進 project-level 的 `.claude/CLAUDE.md`，新成員就收不到。移到 project-level 設定確保現在與未來的所有團隊成員自動收到這條指引。

### 第 38 題（情境：Code Generation with Claude Code）

**情境：** 你發現把 2–3 個完整的 endpoint 實作範例當 context，能顯著提升產生新 API endpoint 的一致性。但這個 context 只在建立新 endpoint 時有用，在 API 目錄裡除錯、review 程式碼或做其他工作時沒用。

**哪個設定做法最有效？**

- A) 把 endpoint 範例與模式文件加進專案 CLAUDE.md，讓它們永遠可用。
- B) 每次產生請求都手動引用 endpoint 範例，把程式碼複製進 prompt。
- C) 在 `.claude/rules/api/` 設定路徑專屬規則，包含 endpoint 範例，在 API 目錄工作時啟用。
- D) 建一個引用 endpoint 範例、包含遵循模式指令的 skill，透過 slash command 按需呼叫。 **【正確】**

**為什麼選 D：** 按需呼叫的 skill 只在產生新 endpoint 時載入範例 context，除錯或 review 等無關任務時不會。這讓主 context 保持乾淨，同時在需要時保留高品質的產生。

### 第 39 題（情境：Code Generation with Claude Code）

**情境：** 團隊建了一個產生資料庫 migration 檔的 `/migration` skill。它透過 `$ARGUMENTS` 接收 migration 名稱。Production 中你觀察到三個問題：(1) 開發者常不帶參數執行 skill，導致檔名很差，(2) skill 有時會用到無關的先前對話中的資料庫 schema 細節，(3) 一位開發者在 skill 有廣泛 tool 存取權時意外執行了破壞性的測試清理。

**哪個設定做法能修正全部三個問題？**

- A) 用位置參數 `$1` 與 `$2` 取代 `$ARGUMENTS` 以強制特定輸入，用 `@` 語法明確引用 schema 檔以控制 context，並在 frontmatter description 加破壞性操作的警告。
- B) 在 frontmatter 加 `argument-hint` 要求必要參數，用 `context: fork` 隔離執行，並把 `allowed-tools` 限制在檔案寫入操作。 **【正確】**
- C) 拆成 `/migration-create` 與 `/migration-apply` 兩個 skills，加驗證指令在缺名稱時要求輸入，並為各自使用不同的 `allowed-tools` 範圍。
- D) 在 skill 的 SKILL.md 加驗證指令確保 `$ARGUMENTS` 是有效名稱，加 prompt 要它忽略先前對話 context，並列出要避免的禁止操作。

**為什麼選 B：** 這用三個獨立的設定功能分別處理每個問題：`argument-hint` 改善參數輸入、減少缺參數的情況，`context: fork` 防止先前對話的 context 洩漏，`allowed-tools` 把 skill 限制在安全的檔案寫入操作，防止破壞性動作。

### 第 40 題（情境：Code Generation with Claude Code）

**情境：** 你的 codebase 有不同 coding 慣例的區域：React components 用帶 hooks 的函式式風格、API handlers 用 async/await 搭配特定錯誤處理、資料庫 models 遵循 repository pattern。測試檔散布在 codebase 各處、與受測程式碼相鄰（例如 `Button.test.tsx` 在 `Button.tsx` 旁），你希望所有測試不論位置都遵循相同慣例。

**確保 Claude 產生程式碼時自動套用正確慣例，最受支援的方式是？**

- A) 把所有慣例放在根目錄 CLAUDE.md、各區域用標題分開，依賴 Claude 推斷哪一節適用。
- B) 在 `.claude/skills/` 為每種程式碼類型建 skills，把慣例嵌在各 SKILL.md。
- C) 在每個子目錄放一份包含該區域慣例的獨立 CLAUDE.md。
- D) 在 `.claude/rules/` 建立帶 YAML frontmatter 指定 glob pattern 的規則檔，依檔案路徑條件式套用慣例。 **【正確】**

**為什麼選 D：** 帶 YAML frontmatter 與 glob pattern（例如 `**/*.test.tsx`、`src/api/**/*.ts`）的 `.claude/rules/` 檔案能不受目錄結構限制、依路徑確定性地套用慣例。這是散布各處的測試檔這類橫切模式最受支援的做法。

### 第 41 題（情境：Code Generation with Claude Code）

**情境：** 你想建立一個自訂 slash command `/review`，執行團隊的標準 code review checklist。它應該在每位開發者 clone 或更新 repo 時就可用。

**Command 檔案該建在哪裡？**

- A) 每位開發者 home 目錄的 `~/.claude/commands/`。
- B) 專案 repo 的 `.claude/commands/`。 **【正確】**
- C) `.claude/config.json` 裡的 commands 陣列。
- D) 專案根目錄的 CLAUDE.md。

**為什麼選 B：** 把自訂 slash commands 放在專案 repo 的 `.claude/commands/`，確保它們受版本控制，並自動對每位 clone 或更新 repo 的開發者可用。這是 Claude Code 中 project-level 自訂 commands 的預定位置。

### 第 42 題（情境：Code Generation with Claude Code）

**情境：** 團隊的 CLAUDE.md 長到超過 500 行，混雜 TypeScript 慣例、測試指引、API 模式與部署程序。開發者覺得很難找到並更新正確的段落。

**Claude Code 支援用什麼做法把 project-level 指令組織成聚焦的主題模組？**

- A) 定義一個 `.claude/config.yaml` 對應檔，把檔案 pattern 對應到 CLAUDE.md 內的特定段落。
- B) 在 `.claude/rules/` 建立獨立的 Markdown 檔，每個涵蓋一個主題（例如 `testing.md`、`api-conventions.md`）。 **【正確】**
- C) 把指令拆成相關子目錄的 README.md 檔，Claude 會自動載入為指令。
- D) 在目錄樹不同層級建立多個名為 CLAUDE.md 的檔案，各自覆蓋父層指令。

**為什麼選 B：** Claude Code 支援 `.claude/rules/` 目錄，你可以為主題式指引建立獨立的 Markdown 檔（例如 `testing.md`、`api-conventions.md`），讓團隊把大型指令集組織成聚焦、可維護的模組。

### 第 43 題（情境：Code Generation with Claude Code）

**情境：** 你建了一個自訂 skill `/explore-alternatives`，團隊用它在選定方案前腦力激盪並評估實作做法。開發者回報執行 skill 後，Claude 後續的回應會受替代方案討論影響：有時引用被否決的做法，或保留干擾實際實作的探索 context。

**該如何最有效地設定這個 skill？**

- A) 在 skill 中用 `!` 前綴把探索邏輯當 bash 子程序執行。
- B) 在 skill frontmatter 加 `context: fork`。 **【正確】**
- C) 拆成兩個 skills（`/explore-start` 與 `/explore-end`）標記探索 context 該被丟棄的邊界。
- D) 把 skill 建在 `~/.claude/skills/` 而不是 `.claude/skills/`。

**為什麼選 B：** `context: fork` 在隔離的 subagent context 中執行 skill，探索討論不會污染主對話歷史。這防止被否決的做法與腦力激盪 context 影響後續的實作工作。

### 第 44 題（情境：Code Generation with Claude Code）

**情境：** 團隊想加一個 GitHub MCP server，透過 Claude Code 搜尋 PR 與查 CI 狀態。六位開發者各有自己的個人 GitHub access token。你想在不把憑證 commit 進版本控制的前提下，讓團隊有一致的工具。

**哪個設定做法最有效？**

- A) 讓每位開發者用 `claude mcp add --scope user` 在 user scope 加 server。
- B) 建一個 MCP server wrapper，從 `.env` 檔讀 token 並代理 GitHub API 呼叫，再把 wrapper 加進專案 `.mcp.json`。
- C) 把 server 加進專案 `.mcp.json`，用環境變數替換（`${GITHUB_TOKEN}`）做認證，並在專案 README 記錄需要的環境變數。 **【正確】**
- D) 在 project scope 用佔位 token 設定 server，再告訴開發者在本機設定覆蓋它。

**為什麼選 C：** 帶環境變數替換的專案 `.mcp.json` 是慣用做法：它為 MCP 設定提供單一受版本控制的真實來源，同時讓每位開發者透過環境變數提供憑證。記錄該變數讓 onboarding 容易，又不會 commit 密鑰。

### 第 45 題（情境：Code Generation with Claude Code）

**情境：** 你要在一個 120 個檔案的 codebase 中，為外部 API 呼叫加上錯誤處理 wrapper。工作分三階段：(1) 找出所有呼叫點與模式，(2) 協作設計錯誤處理做法，(3) 一致地實作 wrapper。在階段 1，Claude 產生大量輸出列出數百個帶 context 的呼叫點，在探索完成前就快速填滿 context window。

**哪個做法最能在維持實作一致性的同時完成任務？**

- A) 階段 1 用 Explore subagent 隔離冗長的探索輸出並回傳摘要，然後在主對話繼續階段 2–3。 **【正確】**
- B) 所有階段都在主對話進行，處理檔案時定期用 `/compact` 降低 context 用量。
- C) 切到 headless 模式搭配 `--continue`，在批次呼叫之間傳遞明確的 context 摘要以維持連續性。
- D) 在 CLAUDE.md 定義錯誤處理模式，然後跨多個 session 分批處理檔案，依賴共用的記憶檔維持一致性。

**為什麼選 A：** Explore subagent 把冗長的探索輸出隔離在獨立 context 中，只回傳簡潔摘要給主對話。這為協作設計與一致實作階段保留了主 context window，而那正是保留 context 最有價值的地方。

### 第 46 題（情境：Customer Support Agent）

**情境：** 測試時你注意到，使用者問訂單狀態時 agent 常呼叫 `get_customer`，儘管 `lookup_order` 更合適。要處理這個問題，你該先檢查什麼？

**該先檢查什麼？**

- A) 實作前處理分類器偵測訂單相關請求，直接路由到 `lookup_order`。
- B) 減少 agent 可用的 tools 數量以簡化選擇。
- C) 在 system prompt 加涵蓋所有可能訂單請求模式的 few-shot 範例以改善 tool 選擇。
- D) 檢查 tool descriptions，確保它們清楚區分每個 tool 的用途。 **【正確】**

**為什麼選 D：** Tool descriptions 是模型決定呼叫哪個 tool 的主要輸入。當 agent 持續選錯 tool 時，第一個診斷步驟是確認 tool descriptions 清楚地區分了每個 tool 的用途與使用邊界。

### 第 47 題（情境：Customer Support Agent）

**情境：** 你的 agent 處理單一問題請求的準確率是 94%（例如「I need a refund for order #1234」）。但當客戶在一則訊息中包含多個問題時（例如「I need a refund for order #1234 and also want to update the shipping address for order #5678」），tool 選擇準確率掉到 58%。Agent 通常只解決一個問題，或把參數在請求之間搞混。哪個做法最能有效提升多問題請求的可靠性？

**哪個做法最有效？**

- A) 實作一個前處理層，用獨立的模型呼叫把多問題訊息分解成獨立請求、各自獨立處理、再合併結果。
- B) 把相關的 tools 合併成較少的通用 tools。
- C) 在 prompt 加 few-shot 範例，示範多問題請求的正確推理與 tool 順序。 **【正確】**
- D) 實作回應驗證偵測不完整的答案，自動重新 prompt agent 解決漏掉的問題。

**為什麼選 C：** 示範多問題請求正確推理與 tool 順序的 few-shot 範例最有效，因為 agent 在單一問題上已經表現良好，它需要的是分解與路由多個問題、並把參數分開的模式引導。

### 第 48 題（情境：Customer Support Agent）

**情境：** Production log 顯示，像「refund for order #1234」的簡單請求，agent 用 3–4 次 tool 呼叫就解決、成功率 91%。但像「I was billed twice, my discount didn't apply, and I want to cancel」的複雜請求，agent 平均 12+ 次 tool 呼叫、成功率只有 54%，常常順序地調查問題、並為每個問題重複抓取客戶資料。什麼改變最能有效改善複雜請求的處理？

**什麼改變最有效？**

- A) 在階段之間加明確的驗證檢查點，要求 agent 每解決一個問題就記錄進度再進到下一個。
- B) 把 `get_customer`、`lookup_order` 與帳單相關 tools 合併成單一 `investigate_issue` tool 以減少 tools 數量。
- C) 把請求分解成獨立問題，然後用共享的客戶 context 平行調查每一個，再綜合成最終解決方案。 **【正確】**
- D) 在 system prompt 加 few-shot 範例，示範各種多面向帳單情境的理想 tool 呼叫順序。

**為什麼選 C：** 分解成獨立問題並用共享客戶 context 平行調查，同時修正了兩個關鍵問題：透過跨問題重用共享 context 消除重複的資料抓取，並在綜合單一解決方案前平行化調查，減少總 tool 呼叫迴圈。

### 第 49 題（情境：Customer Support Agent）

**情境：** 你的 agent 首次接觸解決率 55%，遠低於 80% 的目標。Log 顯示它會 escalate 簡單案件（有照片證明的損壞商品標準換貨），卻試圖自主處理需要政策例外的複雜情況。改善 escalation 校準最有效的方式是？

**改善 escalation 校準最有效的方式是？**

- A) 要求 agent 在每次回應前自評 1–10 的信心，信心低於門檻時自動轉給人工。
- B) 部署一個用歷史工單訓練的獨立分類器模型，在主 agent 開始處理前預測哪些請求需要 escalation。
- C) 在 system prompt 加明確的 escalation 標準，附 few-shot 範例展示何時 escalate、何時自主解決。 **【正確】**
- D) 實作情緒分析判斷客戶的挫折程度，超過負面情緒門檻時自動 escalate。

**為什麼選 C：** 帶 few-shot 範例的明確 escalation 標準直接處理了根本原因：簡單與複雜案件之間不清楚的決策邊界。這是最相稱、最有效的第一步介入，教 agent 何時 escalate、何時自主解決，不需要額外的基礎設施。

### 第 50 題（情境：Customer Support Agent）

**情境：** 呼叫 `get_customer` 與 `lookup_order` 之後，agent 已擁有所有可用的系統資料，但仍面臨不確定性。哪個情況最有理由呼叫 `escalate_to_human`？

**哪個情況最有理由 escalate？**

- A) 客戶想取消一個昨天出貨、明天送達的訂單。Agent 應該 escalate，因為客戶收到包裹後可能改變心意。
- B) 客戶聲稱沒收到訂單，但追蹤顯示三天前已送達並在其住址簽收。Agent 應該 escalate，因為提出矛盾證據可能傷害客戶關係。
- C) 客戶要求競品價格比對。你的政策允許自家網站 14 天內降價的價格調整，但完全沒提到競品價格。Agent 應該 escalate 以取得政策解釋。 **【正確】**
- D) 客戶訊息同時包含帳單問題與商品退貨。Agent 應該 escalate，讓人工在一次互動中協調兩個問題。

**為什麼選 C：** 這是真正的政策空缺：公司規則涵蓋自家網站的降價，但沒處理競品價格比對。Agent 不能自創政策，應該 escalate 讓人工判斷如何解釋或延伸既有規則。

### 第 51 題（情境：Customer Support Agent）

**情境：** Production log 顯示 12% 的案例中，agent 跳過 `get_customer`，只用客戶提供的名字直接呼叫 `lookup_order`，有時導致帳號誤判與錯誤退款。什麼改變最能有效修正這個可靠性問題？

**什麼改變最有效？**

- A) 加 few-shot 範例展示 agent 永遠先呼叫 `get_customer`，即使客戶主動提供訂單細節。
- B) 實作路由分類器分析每個請求，只啟用適合該請求類型的 tools 子集。
- C) 加程式化的前置條件，在 `get_customer` 回傳已驗證的客戶識別碼前封鎖 `lookup_order` 與 `process_refund`。 **【正確】**
- D) 強化 system prompt，聲明任何訂單操作前透過 `get_customer` 驗證客戶是強制的。

**為什麼選 C：** 程式化的前置條件提供確定性保證，確保必要的順序被遵守。這是最有效的做法，因為不論 LLM 行為如何，它都消除了跳過驗證的可能性。

### 第 52 題（情境：Customer Support Agent）

**情境：** Production 指標顯示，處理複雜帳單爭議或多訂單退貨時，即使解決方案技術上正確，客戶滿意度仍比簡單案件低 15%。根因分析顯示 agent 給出準確的解法，但解釋理由不一致：有時省略相關政策細節，有時漏掉時程資訊或下一步。具體的 context 缺口因案而異。你想在不增加人工監督的前提下改善解法品質。哪個做法最有效？

**哪個做法最有效？**

- A) 加一個 self-critique 階段，agent 評估草稿回應的完整性：確保它解決了客戶的問題、包含相關 context、並預先回答後續問題。 **【正確】**
- B) 加一個確認階段，agent 在結案前問「Does this fully resolve your issue?」，讓客戶能要求更多資訊。
- C) 複雜案件把模型從 Haiku 升級到 Sonnet，依定義的複雜度指標路由。
- D) 在 system prompt 實作 few-shot 範例，展示五種常見複雜案件類型的完整解釋，示範如何包含政策 context、時程與下一步。

**為什麼選 A：** Self-critique 階段（evaluator-optimizer 模式）直接處理解釋完整性不一致的問題，強迫 agent 在呈現前依具體標準（政策 context、時程、下一步）評估自己的草稿。這能在沒有人工監督下抓到因案而異的缺口。

### 第 53 題（情境：Customer Support Agent）

**情境：** Production 指標顯示你的 agent 每次解決平均 4+ 次 API 迴圈。分析顯示 Claude 常在分開的順序回合請求 `get_customer` 與 `lookup_order`，即使一開始就兩者都需要。減少迴圈數最有效的方式是？

**減少迴圈最有效的方式是？**

- A) 實作推測性執行，與任何被請求的 tool 平行地自動呼叫可能需要的 tools，不論請求了什麼都回傳所有結果。
- B) 提高 `max_tokens`，給 Claude 更多空間規劃並自然地合併 tool 請求。
- C) 建立像 `get_customer_with_orders` 的複合 tools，把常見的查詢組合綑成單一呼叫。
- D) 在 prompt 指示 Claude 把 tool 請求綑成一個回合，在下一次 API 呼叫前一起回傳所有結果。 **【正確】**

**為什麼選 D：** 用 prompt 要 Claude 把相關 tool 請求綑成單一回合，利用了它一次請求多個 tools 的原生能力。這以最小的架構變動直接修正順序呼叫的模式。

### 第 54 題（情境：Customer Support Agent）

**情境：** Production log 顯示一個模式：客戶引用特定金額（例如「the 15% discount I mentioned」），但 agent 回應了錯誤的值。調查顯示這些細節在 20+ 回合前提過，被濃縮成像「promotional pricing was discussed」的模糊摘要。哪個修法最有效？

**哪個修法最有效？**

- A) 把摘要門檻從 70% 提高到 85%，讓對話在觸發摘要前有更多空間。
- B) 把完整對話歷史存在外部儲存，agent 偵測到「as I mentioned」等引用時實作檢索。
- C) 把交易事實（金額、日期、訂單編號）抽到一個持久的「case facts」區塊，放在摘要歷史之外、每個 prompt 都包含。 **【正確】**
- D) 修改摘要 prompt，明確要求逐字保留所有數字、百分比、日期與客戶陳述的期望。

**為什麼選 C：** 摘要本質上會丟失精確細節。把交易事實抽到摘要歷史之外的結構化「case facts」區塊，保留了關鍵資訊，讓它不論已摘要多少回合，都能在每個 prompt 中可靠取得。

### 第 55 題（情境：Customer Support Agent）

**情境：** 你的 `get_customer` tool 依名字搜尋時回傳所有符合的結果。目前有多筆結果時，Claude 會挑最近有訂單的客戶，但 production 資料顯示對於模糊的比對，這有 15% 選到錯的帳號。該如何處理？

**該如何處理？**

- A) 實作信心評分系統，信心高於 85% 時自主行動、低於門檻時要求釐清。
- B) 指示 Claude 在 `get_customer` 回傳多筆結果時，採取任何客戶專屬動作前先要求額外的識別資訊（email、電話或訂單編號）。 **【正確】**
- C) 修改 `get_customer`，依排名演算法只回傳單一最可能的結果，消除歧義。
- D) 在 prompt 加 few-shot 範例，示範模糊比對的正確推理與 tool 順序。

**為什麼選 B：** 向使用者要額外的識別資訊是解決歧義最可靠的方式，因為使用者對自己的身分有確切的知識。多一個對話回合是很小的代價，卻能消除因選錯帳號造成的 15% 錯誤率。

### 第 56 題（情境：Customer Support Agent）

**情境：** Production log 顯示一個一致的模式：當客戶訊息包含「account」這個詞（例如「I want to check my account for an order I made yesterday」），agent 有 78% 先呼叫 `get_customer`。當客戶用不含「account」的類似說法（例如「I want to check an order I made yesterday」），它有 93% 先呼叫 `lookup_order`。Tool descriptions 清楚且無歧義。這個差異最可能的根本原因是？

**最可能的根本原因是？**

- A) System prompt 包含對「account」等詞敏感的關鍵字式指令，造成非預期的 tool 選擇模式。 **【正確】**
- B) 模型的基礎訓練在「account」術語與客戶相關操作之間建立了凌駕 tool descriptions 的關聯。
- C) 模型需要更多多概念訊息的訓練資料，應該用同時含 account 與 order 術語的範例做 fine-tune。
- D) Tool descriptions 需要額外的負面範例，指定何時不該用每個 tool，以防止這種關鍵字引起的混淆。

**為什麼選 A：** 系統性的關鍵字驅動模式（78% vs 93%）強烈顯示 system prompt 中有對「account」反應、把 agent 導向客戶相關 tools 的明確路由邏輯。既然 tool descriptions 已經清楚，這個差異指向 prompt 層級的指令造成了非預期的行為引導。

### 第 57 題（情境：Customer Support Agent）

**情境：** Production log 顯示，使用者問訂單時（例如「check my order #12345」），agent 常呼叫 `get_customer` 而不是 `lookup_order`。兩個 tools 的描述都很精簡（「Gets customer information」/「Gets order details」），且接受看起來相似的識別碼格式。改善 tool 選擇可靠性最有效的第一步是？

**最有效的第一步是？**

- A) 實作路由層，在每回合前分析使用者輸入，依偵測到的關鍵字與 ID 模式預選正確的 tool。
- B) 把兩個 tools 合併成單一 `lookup_entity`，接受任何識別碼並在內部決定查哪個後端。
- C) 在 system prompt 加 few-shot 範例示範正確的 tool 選擇模式，用 5–8 個範例把訂單相關查詢路由到 `lookup_order`。
- D) 擴充每個 tool 的描述，加入輸入格式、範例查詢、邊界案例，以及說明何時該用它而非相似 tools 的邊界。 **【正確】**

**為什麼選 D：** 用輸入格式、範例查詢、邊界案例與清楚的邊界擴充 tool descriptions，直接修正了根本原因：精簡的描述沒給 LLM 足夠資訊區分相似的 tools。這是低成本、高影響的第一步，改善了 LLM 選擇 tool 的主要機制。

### 第 58 題（情境：Customer Support Agent）

**情境：** 你在為客服 agent 實作 agent loop。每次 Claude API 呼叫後，你必須決定是繼續迴圈（執行請求的 tools 並再呼叫 Claude）還是停止（把最終答案呈現給客戶）。什麼決定這個判斷？

**什麼決定這個判斷？**

- A) 檢查 Claude 回應中的 `stop_reason` 欄位：是 `tool_use` 就繼續、是 `end_turn` 就停止。 **【正確】**
- B) 解析 Claude 的文字找像「I'm done」或「Can I help with anything else?」的句子，自然語言訊號代表任務完成。
- C) 設定最大迭代數（例如 10 次呼叫），達到就停止，不論 Claude 是否表示還有工作。
- D) 檢查回應是否含 assistant 文字內容，若 Claude 產生了說明文字，迴圈就該終止。

**為什麼選 A：** `stop_reason` 是 Claude 用於迴圈控制的明確結構化訊號：`tool_use` 表示 Claude 想執行 tool 並取回結果，`end_turn` 表示 Claude 已完成回應、迴圈該結束。

### 第 59 題（情境：Customer Support Agent）

**情境：** Production log 顯示 agent 誤解你的 MCP tools 的輸出：`get_customer` 的 Unix timestamp、`lookup_order` 的 ISO 8601 日期，以及數字狀態碼（1=pending、2=shipped）。有些 tools 是你無法修改的第三方 MCP servers。哪種資料格式正規化的做法最好維護？

**哪種做法最好維護？**

- A) 用 PostToolUse hook 攔截 tool 輸出，在 agent 處理前套用格式轉換。 **【正確】**
- B) 修改你控制的 tools 回傳人類可讀的格式，並為第三方 tools 建 wrapper。
- C) 建一個 `normalize_data` tool，agent 在每次取資料後呼叫它轉換值。
- D) 在 system prompt 加詳細的格式文件，說明每個 tool 的資料慣例。

**為什麼選 A：** PostToolUse hook 提供一個集中、確定性的攔截點，在 agent 處理前正規化所有 tool 輸出，包含第三方 MCP server 的資料。它更好維護，因為轉換寫在程式碼裡、一致地套用，而不是依賴 LLM 的解讀。

### 第 60 題（情境：Customer Support Agent）

**情境：** Production log 顯示 agent 有時在 `lookup_order` 更合適時選了 `get_customer`，特別是像「I need help with my recent purchase」這類模糊的查詢。你決定在 system prompt 加 few-shot 範例改善 tool 選擇。哪個做法最能有效處理這個問題？

**哪個做法最有效？**

- A) 在每個 tool description 加涵蓋模糊案例的明確「use when」與「don't use when」指引。
- B) 依 tool 分組加範例：所有 `get_customer` 情境放一起，再放所有 `lookup_order` 情境。
- C) 加 4–6 個針對模糊情境的範例，每個附上為什麼選這個 tool 而非其他合理選項的理由。 **【正確】**
- D) 加 10–15 個清楚、無歧義請求的範例，示範每個 tool 典型情境的正確選擇。

**為什麼選 C：** 把 few-shot 範例瞄準錯誤發生的特定模糊情境，並明確說明為何一個 tool 比其他選項更合適，能教模型邊界案例所需的比較式決策過程。這比泛用的範例或宣告式規則更有效。

### 第 61 題（情境：Conversational AI Architecture Patterns）

**情境：** 你的 `remove_team_member` tool 用 `dry_run: boolean` 參數在執行前預覽影響。Production 監控顯示 agent 直接用 `dry_run=false` 呼叫，跳過預覽步驟。你需要確保每次移除前都有一次使用者明確確認的預覽。

**最可靠的做法是？**

- A) 加 server-side 驗證，只在過去 60 秒內有一次參數相同的 `dry_run=true` 呼叫時才允許 `dry_run=false`。
- B) 把 tool 標註為需要確認，並設定 orchestration 層在轉送任何呼叫給已標註的 tools 前先提示使用者核准。
- C) 在 tool description 加詳細指令與 few-shot 範例，要求 agent 永遠先用 `dry_run=true` 呼叫、等使用者確認後再呼叫一次。
- D) 換成兩個 tools：`preview_remove_member` 回傳影響細節與一次性的確認 token；`execute_remove_member` 需要該 token，把執行綁定到預覽。 **【正確】**

**為什麼選 D：** 兩個 tool 加 token 綁定的做法讓「沒有先預覽就執行」在架構上不可能：execute tool 確實需要一個只有 preview tool 能產生的 token。這是唯一在程式碼層級強制限制的做法，而不是依賴 LLM 遵守指令（C）、時間啟發式（A）或 orchestration 基礎設施（B）。

### 第 62 題（情境：Conversational AI Architecture Patterns）

**情境：** Production 監控顯示你的 `search_catalog` tool 有 12% 的失敗率：8% 是重試就會成功的網路 timeout，4% 是不論重試多少次都不會成功的查詢語法錯誤。目前兩種錯誤以相同方式回傳，造成浪費的重試。

**該如何修改 tool 的錯誤處理？**

- A) 在 system prompt 加 few-shot 範例，示範如何區分網路錯誤與語法錯誤。
- B) 對所有錯誤一致地套用 exponential backoff 重試邏輯。
- C) 在 tool 內部對網路 timeout 實作帶 backoff 的自動重試；語法錯誤立即回傳並附參數驗證細節。 **【正確】**
- D) 所有錯誤都回傳帶 `retryable` boolean 旗標與錯誤類型細節。

**為什麼選 C：** 在 tool 層級處理 transient 錯誤的重試是正確的抽象邊界：tool 對錯誤類型有確切的知識，能實作確定性的重試邏輯，不必依賴 agent 解讀旗標（D）或遵守 prompt 層級的指令（A）。一致的 backoff（B）在永遠不會成功的語法錯誤上浪費時間。

### 第 63 題（情境：Conversational AI Architecture Patterns）

**情境：** 討論投資策略的幾個回合中，使用者說過「I have a very low risk tolerance」，後來又說「I want to maximize my returns」。現在他們問：「What should I invest in?」

**哪個做法最能確保建議符合使用者的真正優先順序？**

- A) 點出矛盾，請使用者釐清哪個更重要。 **【正確】**
- B) 為兩種情境分別提供建議。
- C) 依最近陳述的偏好進行。
- D) 建議平衡型投資組合，不處理衝突。

**為什麼選 A：** 當使用者的偏好直接矛盾時，點出衝突並請求釐清是唯一能保證建議符合使用者真實意圖的方式。任何其他做法都涉及可能錯誤的假設：最大化報酬與低風險承受度是根本上不相容的目標，需要人類做決定。

### 第 64 題（情境：Conversational AI Architecture Patterns）

**情境：** 使用者在多個對話回合中精煉播放清單偏好。使用者說「I love jazz」的兩則訊息之後，Claude 問「What genres do you enjoy?」

**最可能的原因是？**

- A) Claude 需要連接 vector database 才能維持對話記憶。
- B) 模型的 context window 已被超過。
- C) Claude API 需要 `session_id` 參數。
- D) 你的應用沒有把先前的訊息放進 `messages` 陣列。 **【正確】**

**為什麼選 D：** Claude 沒有 server-side 記憶，每次 API 呼叫都是無狀態的。若沒在每次請求的 `messages` 陣列中放入完整對話歷史，Claude 就不知道先前的回合。Vector database（A）與 `session_id`（C）都不是 Claude 架構的一部分；兩則訊息的交換不可能溢出 context window（B）。

### 第 65 題（情境：Conversational AI Architecture Patterns）

**情境：** 一段 40 分鐘的烹飪 session 後，對話達到 78,000 tokens。歷史包含過敏資訊、食譜換算、釐清過的烹飪術語與一般討論。你必須在保留重要資訊的同時減少 tokens。

**哪個做法最能平衡保留與 token 減量？**

- A) 摘要整段對話歷史。
- B) 只保留最近的 20,000 tokens。
- C) 抽出關鍵的結構化資料（過敏、份量、偏好），摘要一般討論，並逐字保留最近的交流。 **【正確】**
- D) 把完整對話存在外部，透過語意搜尋檢索相關部分。

**為什麼選 C：** 混合做法以最低成本保留最高價值的資訊。過敏與食譜份量等關鍵事實被抽到緊湊的結構化區塊（避免摘要時的精度流失），一般討論被摘要，最近的交流則逐字保留以維持對話連貫性。A 與 B 有丟失關鍵飲食資訊的風險；D 對單一烹飪 session 來說是架構上的過度設計。

### 第 66 題（情境：Conversational AI Architecture Patterns）

**情境：** 使用者回報在長對話中，助理會忘記較早的話題與偏好。你目前的實作只保留最近 25 組訊息。

**最有效的解法是？**

- A) 混合做法：摘要較舊的訊息，同時逐字保留最近的訊息。 **【正確】**
- B) 對完整對話歷史做 vector 相似度搜尋。
- C) 把 window 增加到 50 組訊息。
- D) 每回合都摘要被丟棄的訊息，並把累積的摘要放在最前面。

**為什麼選 A：** 混合做法處理了問題的兩個面向：保留精確的最近 context（對話連貫性的關鍵），同時維持較早偏好的壓縮表示（防止訊息組被丟棄時完全流失）。增加 window（C）只是延後同樣的問題。Vector 搜尋（B）可能漏掉與當前查詢語意不相似的重要 context。每回合完整摘要（D）增加開銷並累積摘要錯誤。

### 第 67 題（情境：Conversational AI Architecture Patterns）

**情境：** 使用者回報對話超過 50 回合後延遲增加、成本上升。

**主要原因是？**

- A) 每次 API 請求都包含整段對話歷史。 **【正確】**
- B) 模型產生的回應越來越長。
- C) 歷史增長時資料庫操作變慢。
- D) 模型在建立需要更多處理的內部使用者檔案。

**為什麼選 A：** Claude 的 API 完全無狀態，每次請求都必須在 `messages` 陣列中包含完整的對話歷史。對話增長時，每次請求攜帶更多 tokens，直接增加處理延遲與成本。模型在呼叫之間不維持任何內部狀態（D 錯誤），回應長度本質上也不與對話長度綁定（B）。

### 第 68 題（情境：Conversational AI Architecture Patterns）

**情境：** 三個月的每週 session 後，對話歷史增長到 85,000 tokens。當使用者問「What did we conclude about the theme of isolation?」時，助理給出泛泛的答案，而不是引用先前的討論。

**最有效的做法是？**

- A) Rolling window 截斷。
- B) 捕捉關鍵結論的漸進式摘要。
- C) 語意 embeddings 搭配相關交流的檢索。 **【正確】**
- D) 加結構化 XML 標籤標記討論結論。

**為什麼選 C：** 對對話歷史做語意搜尋是唯一能擴展到三個月討論、又能按需浮現特定相關交流的做法。Rolling window（A）會丟棄大部分歷史。漸進式摘要（B）把討論壓成抽象概念，失去使用者詢問的具體結論。XML 標籤（D）需要重構所有過去內容，且無法在這個規模解決檢索問題。

### 第 69 題（情境：Conversational AI Architecture Patterns）

**情境：** QA 測試中，Claude 在前 10–15 回合遵守 system prompt 的指引，但之後的回應開始偏離。對話仍在 token 限制內。

**最好的解法是？**

- A) 把行為指引移到第一則使用者訊息。
- B) 20 回合後開始新對話。
- C) 在對話的斷點插入 user 角色的訊息，重申指引。 **【正確】**
- D) 用回應後驗證重新產生不合規的回應。

**為什麼選 C：** 定期注入行為提醒，透過在對話歷史累積時定期重新確立限制，直接對抗指令飄移（instruction drift）。把指引移到第一則使用者訊息（A）降低了它們的權威性。開始新對話（B）摧毀 context。回應後驗證（D）是矯正而非預防，且增加顯著延遲。

### 第 70 題（情境：Conversational AI Architecture Patterns）

**情境：** 你的 AI 家教有一段 2,800 tokens 的 system prompt，定義教學方法與適應規則。12 回合後，助理開始忽略程度等級。

**最有效的修法是？**

- A) 每 4–5 回合注入提醒。
- B) 用示範程度等級適應的 few-shot 範例取代冗長的規則。 **【正確】**
- C) 把關鍵規則放在 system prompt 的結尾。
- D) 評估回應，難度等級不符就重新產生。

**為什麼選 B：** 一段 2,800 tokens、由宣告式規則組成的 system prompt 容易飄移，因為抽象規則要求模型每回合都對它們推理。用示範正確程度等級適應的具體 few-shot 範例取代冗長規則，給模型清楚的行為模式可比對，這在多回合中比抽象指令更能被可靠遵守。注入提醒（A）有幫助但處理的是症狀；放在結尾（C）一開始有幫助但無法應對回合層級的飄移；重新產生（D）昂貴且是矯正性的。

### 第 71 題（情境：Conversational AI Architecture Patterns）

**情境：** 你的助理必須維持熱情的語氣、解釋它的推理，並提出釐清問題。這些行為指引該定義在哪裡？

**這些行為指引該定義在哪裡？**

- A) 放在每則使用者訊息的前面。
- B) 放在 system prompt。 **【正確】**
- C) 放在第一則 assistant 訊息。
- D) 放在環境變數。

**為什麼選 B：** System prompt 就是專為適用於整段對話的持續行為限制與指引設計的。放在每則使用者訊息前面（A）是多餘的開銷。第一則 assistant 訊息（C）不可靠，因為模型可能偏離自己先前的陳述。環境變數（D）對模型行為沒有影響。

### 第 72 題（情境：Conversational AI Architecture Patterns）

**情境：** 使用者回報回應開頭重複出現像「Certainly!」與「I'd be happy to help!」的句子。

**最有效的做法是？**

- A) 附加一則以直接回答開頭的部分 assistant 訊息（prefill）。 **【正確】**
- B) 降低 temperature 設定。
- C) 後處理回應以移除問候語。
- D) 在 system prompt 加指令避免那些句子。

**為什麼選 A：** 用直接答案的開頭預填（prefill）assistant 的回應，在生成層級防止了問候模式：模型會從 prefill 接續，而不是產生新的開場句。System prompt 指令（D）有幫助但較不可靠，因為模型仍可能產生變體。後處理（C）是脆弱的變通法。Temperature（B）控制隨機性，不是特定的句子模式。

### 第 73 題（情境：Conversational AI Architecture Patterns）

**情境：** 使用者正在聊天時，一個 webhook 通知你的系統該使用者的包裹已出貨。你希望助理在下一次回應中自然地帶入這個資訊。

**最好的做法是？**

- A) 把出貨狀態加進 system prompt。
- B) 立即送一則合成的使用者訊息。
- C) 強制助理每回合呼叫狀態 tool。
- D) 把狀態更新當前綴附加到下一則使用者訊息。 **【正確】**

**為什麼選 D：** 把狀態更新前綴到下一則使用者訊息，在自然的對話邊界注入即時 context，不打斷流程。修改 system prompt（A）需要重建 session，或在架構上很笨重。合成的使用者訊息（B）可能打斷自然對話流並混淆歸屬。每回合強制 tool 呼叫（C）在事件罕見時很浪費。

### 第 74 題（情境：Conversational AI Architecture Patterns）

**情境：** 使用者常送出像「Book a venue for the party」的請求。助理會問 4 個以上的釐清問題，造成 35% 的放棄率。

**哪個做法最能改善這個取捨？**

- A) 用隱藏的預設值直接進行。
- B) 在一則複合訊息中問所有釐清問題。
- C) 明確陳述假設並進行，同時邀請修正。 **【正確】**
- D) 使用結構化的填表流程。

**為什麼選 C：** 明確陳述假設並進行，給使用者立即、有用的回應，同時保留他們修正錯誤假設的能力。隱藏的預設值（A）讓使用者不知道假設了什麼。複合問題清單（B）仍要求使用者先付出努力。結構化表單（D）增加而非減少摩擦，與降低放棄率的目標相悖。

### 第 75 題（情境：Conversational AI Architecture Patterns）

**情境：** 你的助理使用一個承包商人設（persona）的 system prompt。早期回合遵守規則，但到第 7 回合助理開始給泛泛的建議。對話長度只有 2,500 tokens。

**最可能的原因是？**

- A) System prompt 只建立初始行為。
- B) 模型注意力隨回合累積而減弱。
- C) 累積的 assistant 回應稀釋了 system prompt 的影響力。 **【正確】**
- D) System prompt 只送一次。

**為什麼選 C：** 隨著 assistant 回應在對話歷史中累積，反映 system prompt 行為限制的文字比例，相對於越來越多的 assistant 產生內容而下降。模型越來越比對自己先前的輸出而非 system prompt，即使在很短的 token 長度也會加劇飄移。System prompt 在每次 API 呼叫都包含（D 作為單獨解釋是錯的），模型注意力退化（B）在 2,500 tokens 時不會發生。

### 第 76 題（情境：Conversational AI Architecture Patterns）

**情境：** 使用者提出像「Can you help with the report?」的模糊請求。助理回應多個問題（哪份報告？什麼幫助？期限？），造成 40% 的放棄率。

**最好的解法是？**

- A) 做出合理假設、明確陳述它們，並表示可以調整。 **【正確】**
- B) 回應前用較小的模型分類模糊性。
- C) 使用預定義的解讀而不陳述假設。
- D) 限制助理每回合只問一個釐清問題。

**為什麼選 A：** 用陳述過的合理假設進行，完全消除了來回往返，同時讓使用者知情並掌控。預定義的靜默解讀（C）在回應不符意圖時讓使用者困惑。單一問題限制（D）仍需要多回合往返。較小的分類模型（B）增加延遲與基礎設施複雜度，卻沒解決核心的 UX 問題。

# 練習與附錄

## 實作練習

### 練習 1：帶 Escalation 邏輯的多 Tool Agent

**目標：** 設計一個有 tool 整合、結構化錯誤處理與 escalation 的 agent loop。

**步驟：**

1. 定義 3–4 個帶詳細描述的 MCP tools（放兩個相似的 tools 來測試 tool 選擇）
2. 實作檢查 `stop_reason`（`"tool_use"` / `"end_turn"`）的 agent loop
3. 加結構化錯誤回應：`errorCategory`、`isRetryable`、描述
4. 實作攔截 hook，阻擋超過門檻的操作並轉向 escalation
5. 用多面向的請求測試

**涵蓋 Domain：** 1（Agent 架構）、2（Tools 與 MCP）、5（Context 與可靠性）

### 練習 2：為團隊開發設定 Claude Code

**目標：** 設定 CLAUDE.md、自訂 commands、路徑專屬規則與 MCP servers。

**步驟：**

1. 建立含通用標準的 project-level CLAUDE.md
2. 為不同程式碼區域建立帶 YAML frontmatter 的 `.claude/rules/` 檔案（`paths: ["src/api/**/*"]`、`paths: ["**/*.test.*"]`）
3. 在 `.claude/skills/` 建一個帶 `context: fork` 與 `allowed-tools` 的專案 skill
4. 在 `.mcp.json` 用環境變數設定一個 MCP server，加一個 `~/.claude.json` 的個人覆蓋
5. 在不同複雜度的任務上測試 planning mode 與直接執行

**涵蓋 Domain：** 3（Claude Code 設定）、2（Tools 與 MCP）

### 練習 3：結構化資料抽取 Pipeline

**目標：** JSON schema、用 `tool_use` 做結構化輸出、驗證 / retry 迴圈、批次處理。

**步驟：**

1. 用 JSON schema 定義一個抽取 tool（required/optional 欄位、帶「other」的 enum、nullable 欄位）
2. 建立驗證迴圈：出錯時帶著文件、錯誤的抽取結果與具體驗證錯誤 retry
3. 為不同結構的文件加 few-shot 範例
4. 用 Message Batches API 做批次處理：100 份文件，用 `custom_id` 處理失敗
5. 路由給人工：欄位層級的信心分數、依文件類型分析

**涵蓋 Domain：** 4（Prompt engineering）、5（Context 與可靠性）

### 練習 4：設計並除錯多 Agent 研究 Pipeline

**目標：** Subagent 編排、context 傳遞、錯誤傳播、帶來源追蹤的 synthesis。

**步驟：**

1. 一個 coordinator 加 2+ 個 subagents（`allowedTools` 包含 `"Task"`，context 在 prompt 中明確傳遞）
2. 在單一回應中用多個 `Task` 呼叫平行執行 subagents
3. 要求結構化的 subagent 輸出：主張、引文、來源 URL、發表日期
4. 模擬 subagent timeout：回傳結構化錯誤 context 給 coordinator，帶部分結果繼續
5. 用矛盾資料測試：保留兩個值並附歸屬；區分已確認與有爭議的發現

**涵蓋 Domain：** 1（Agent 架構）、2（Tools 與 MCP）、5（Context 與可靠性）

## 附錄：技術與概念速查

| 技術 | 關鍵面向 |
|---|---|
| **Claude Agent SDK** | AgentDefinition、agent loops、`stop_reason`、hooks（PostToolUse）、透過 Task 產生 subagents、`allowedTools` |
| **Model Context Protocol（MCP）** | MCP servers、tools、resources、`isError`、tool descriptions、`.mcp.json`、環境變數 |
| **Claude Code** | CLAUDE.md 層級、帶 glob pattern 的 `.claude/rules/`、`.claude/commands/`、帶 SKILL.md 的 `.claude/skills/`、planning mode、`/compact`、`--resume`、`fork_session` |
| **Claude Code CLI** | 非互動模式的 `-p` / `--print`、`--output-format json`、`--json-schema` |
| **Claude API** | 帶 JSON schema 的 `tool_use`、`tool_choice`（"auto"/"any"/強制）、`stop_reason`、`max_tokens`、system prompts |
| **Message Batches API** | 省 50%、最長 24 小時窗口、`custom_id`、不支援多回合 tool calling |
| **JSON Schema** | Required vs optional、nullable 欄位、enum 型別、「other」+ detail、strict mode |
| **Pydantic** | Schema 驗證、語意錯誤、驗證 / retry 迴圈 |
| **內建 tools** | Read、Write、Edit、Bash、Grep、Glob：用途與選擇標準 |
| **Few-shot prompting** | 針對模糊情境的範例、泛化到新模式 |
| **Prompt chaining** | 順序分解成聚焦的多輪 |
| **Context window** | Token 預算、漸進式摘要、「lost in the middle」、scratchpad 檔案 |
| **Session 管理** | Resume、`fork_session`、具名 sessions、context 隔離 |
| **信心校準** | 欄位層級評分、用標註集校準、分層抽樣 |

## 不考的範圍

以下相鄰主題**不會**出現在考試中：

- Fine-tuning Claude 模型或訓練自訂模型
- Claude API 的認證、計費或帳號管理
- 特定程式語言或框架的細節實作（超出 tool / schema 設定所需的部分）
- 部署或託管 MCP servers（基礎設施、網路、容器編排）
- Claude 的內部架構、訓練過程或模型權重
- Constitutional AI、RLHF 或安全訓練方法
- Embedding 模型或 vector database 的實作細節
- Computer use（瀏覽器自動化、桌面互動）
- 影像分析能力（Vision）
- Streaming API 或 server-sent events
- Rate limiting、配額或詳細的 API 成本計算
- OAuth、API key 輪替或認證協定細節
- 雲端供應商專屬設定（AWS、GCP、Azure）
- 效能 benchmark 或模型比較指標
- Prompt caching 的實作細節（知道它存在即可）
- Token 計數演算法或 tokenization 細節

## 準備建議

1. **用 Claude Agent SDK 建一個 agent**：實作完整的 agent loop，包含 tool calling、錯誤處理與 session 管理。練習 subagents 與明確的 context 傳遞。
2. **為真實專案設定 Claude Code**：使用 CLAUDE.md 層級、`.claude/rules/` 的路徑專屬規則、帶 `context: fork` 與 `allowed-tools` 的 skills，以及 MCP server 整合。
3. **設計並測試 MCP tools**：撰寫能區分相似 tools 的描述、回傳帶類別與 retry 旗標的結構化錯誤，並用模糊的使用者請求測試。
4. **建一個資料抽取 pipeline**：使用帶 JSON schema 的 `tool_use`、驗證 / retry 迴圈、optional/nullable 欄位，以及透過 Message Batches API 的批次處理。
5. **練習 prompt engineering**：為模糊情境加 few-shot 範例、明確的 review 標準，以及大型 code review 的多輪架構。
6. **研讀 context 管理模式**：從冗長輸出抽取事實、使用 scratchpad 檔案，並把探索委派給 subagents 以應對 context 限制。
7. **理解 escalation 與 human-in-the-loop**：何時 escalate（政策空缺、使用者明確要求、無法取得進展）以及基於信心的路由 workflow。
8. **正式考試前做一次模擬考**。它使用相同的情境與形式。

---

本頁翻譯整理自 [paullarionov/claude-certified-architect — guide_en.md](https://github.com/paullarionov/claude-certified-architect/blob/main/guide_en.md)，感謝原作者的整理與分享。
