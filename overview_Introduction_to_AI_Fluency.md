# Introduction to AI Fluency — 課程導讀

> 原始筆記：`../Introduction_to_AI_Fluency.md`
> 對象：**還沒看過這門課的人**。讀完這份導讀，你就能掌握課程在教什麼、核心觀念是什麼、以及可以馬上套用的做法。專有名詞保留英文，第一次出現時附中文解釋。

---

## 這門課在講什麼

這是 Anthropic 推出的一門觀念課，主題是「**AI Fluency**」——直譯是「AI 流利度」，意思是**與 AI 協作的能力**，就像語言流利一樣，是可以刻意練習出來的技能。

課程的核心主張：會用 AI 不等於「知道怎麼下指令」，而是能夠**有效（effective）、有效率（efficient）、合乎倫理（ethical）、安全（safe）**地與 AI 系統互動。整門課圍繞一個叫 **4D Framework** 的框架展開，搭配大量與 Claude 對話的實作練習。

- **不需要任何程式背景**，也不需要付費訂閱——用免費的 claude.ai 帳號就能完成所有練習。
- 全課程約 13 個單元加自主練習，多數單元是 4～7 分鐘的影片加練習，總時數不長。
- 這門課教的是「思考方式」而不是特定工具操作，所以官方強調：**就算 AI 技術繼續演進，這套框架依然適用**。

---

## 先記住這兩張表，全課程就懂了一半

### 表一：與 AI 協作的三種模式

| 模式 | 意思 | 例子 |
|---|---|---|
| **Automation**（自動化） | AI 依你的指令完成特定任務 | 「幫我把這段文字翻成英文」 |
| **Augmentation**（增強） | 你和 AI 像夥伴一樣**一起思考、一起產出** | 和 AI 來回討論一份企劃的架構 |
| **Agency**（代理） | 你**事先設定好 AI 的知識與行為模式**，讓它代表你獨立作業 | 設定一個自動回覆客服問題的 AI |

### 表二：4D Framework——課程的主軸

| 競爭力 | 中文意思 | 一句話說明 |
|---|---|---|
| **Delegation**（委派） | 決定「哪些事給 AI 做」 | 想清楚哪些工作自己做、哪些交給 AI、哪些一起做 |
| **Description**（描述） | 把需求「說清楚」 | 與 AI 溝通的表達能力，也就是廣義的 prompt 撰寫 |
| **Discernment**（辨別） | 批判性地「看結果」 | 評估 AI 的產出與行為，不照單全收 |
| **Diligence**（盡責） | 為成果「負責任」 | 使用 AI 時的倫理、透明度與當責 |

之後的每個單元，其實都是在深入這四個 D 的其中一個。

---

## 各單元內容導讀

### 單元 1–3：為什麼需要 AI Fluency？

開場三個單元建立整體觀念：

- AI Fluency 的定義：以**有效、有效率、合乎倫理、安全**的方式與 AI 互動的綜合能力（技能＋知識＋價值觀）。
- 介紹上面表一的三種協作模式（Automation / Augmentation / Agency）。
- 介紹 4D Framework，並說明這四種競爭力**適用於全部三種協作模式**。

### 單元 4–5：Generative AI 基礎知識（Deep Dive 1）

這兩個單元用非技術語言解釋生成式 AI 的原理，重點如下：

- **Generative AI**（生成式 AI）＝會「創造新內容」（文字、圖片、程式碼）的 AI，而不只是分析既有資料。
- 現代 **LLM**（Large Language Model，大型語言模型）能出現，靠三件事：**transformer architecture**（一種神經網路架構的突破）、海量數位訓練資料、運算能力大幅提升。
- 模型學習分兩階段：**pre-training**（預訓練，從數十億筆範例中學規律）與 **fine-tuning**（微調）。
- 目前的能力：任務多元、能理解對話脈絡。
- 目前的限制（考驗 Discernment 的地方）：
  - **knowledge cutoff**：模型的知識有截止日期，不知道之後發生的事。
  - **hallucination**（幻覺）：模型可能一本正經地講出錯誤內容。
  - **context window**（上下文視窗）：一次對話能處理的文字量有上限。

> 課程的結論：最好的應用方式是**人類與 AI 各出所長**，人類負責批判性思考。

### 單元 6–7：Delegation（委派）

Delegation 拆成三個成分：

1. **Problem Awareness**：先想清楚**你的目標**和達成目標需要哪些工作——在找 AI 幫忙之前。
2. **Platform Awareness**：了解**不同 AI 系統各自能做什麼、不能做什麼**。
3. **Task Delegation**：策略性地把工作**分配**給人或 AI，各取所長。

關鍵心態：目標**不是把所有事都自動化**，而是建立最有效的人機分工。單元 7 是實作：挑一個約 1 小時能完成的小專案（例如寫簡報、做研究比較、擬學習計畫），和 Claude 討論出一份「哪些自己做、哪些給 AI 做」的委派計畫，後面的單元會繼續用這個專案。

### 單元 8–9：Description（描述）

AI 不會讀心術——結果的品質往往取決於你**表達得多清楚**。Description 分三種：

| 類型 | 說明什麼 | 例子 |
|---|---|---|
| **Product Description** | 你要的**產出**長什麼樣 | 格式、長度、受眾、風格 |
| **Process Description** | 希望 AI **怎麼做**這件事 | 「先列大綱再展開」 |
| **Performance Description** | 希望 AI 在協作中**表現出什麼行為** | 「回答要簡潔」「主動指出我的盲點」 |

單元 9 給了**六個實用的 prompting 技巧**，是全課程最能直接套用的部分：

1. **給脈絡（Give context）**：說清楚你要什麼、為什麼要、相關背景。
2. **給範例（Show examples）**：示範你要的輸出風格或格式。
3. **給限制（Specify constraints）**：明確定義格式、長度等要求。
4. **拆步驟（Break complex tasks into steps）**：引導 AI 分步推理。
5. **先想再答（Ask the AI to think first）**：給 AI 空間先梳理再回答。
6. **設定角色與語氣（Define the AI's role or tone）**。

還有一個「秘密武器」：**直接請 AI 幫你改良你的 prompt**。而且 prompting 本來就是迭代的過程，預期要來回修改幾次才會滿意。

### 單元 10–11：Discernment（辨別）

拿到 AI 的產出後，怎麼判斷好不好？Discernment 一樣分三種，跟 Description 一一對應：

- **Product Discernment**：產出本身正不正確、合不合適。
- **Process Discernment**：AI 的推理過程有沒有邏輯錯誤、跳步。
- **Performance Discernment**：AI 在互動中的行為表現是否恰當。

單元 11 介紹課程中最重要的工作流程——**Description-Discernment loop**（描述—辨別循環）：

> **Describe**（描述需求）→ **Discern**(評估結果) → **Refine**（給回饋、調整描述、要求修改）→ **Integrate**（加入自己的專業判斷，為最終成果負責）→ 回到 Describe……

這個循環就是實務上與 AI 協作的基本節奏。

### 單元 12：Diligence（盡責）

最後一個 D 談責任，分三種：

- **Creation Diligence**：謹慎選擇你使用的 AI 系統與使用方式。
- **Transparency Diligence**：對「需要知道的人」誠實揭露 AI 在你工作中扮演的角色。
- **Deployment Diligence**：對你交出去的 AI 協作成果**驗證並負責**。

實作是寫一份 **diligence statement**（盡責聲明）——一段透明說明 AI 參與程度的文字，範本開頭像這樣：「*In creating this document, I collaborated with [AI assistant name] to assist with...*」。不同情境（個人、學術、職場）對揭露的期待不同，但負責的原則不變。

### 單元 13–14：總結與自主練習

- 總結重申：最好的成果來自**人與 AI 互補**，而 4D Framework 設計上不會因 AI 演進而過時。
- 建議的延伸練習：
  - 和 Claude 討論這門課本身，盤點自己哪個 D 強、哪個 D 弱。
  - 建立**個人 AI 使用準則**（什麼情境用 AI、機密資訊的界線、揭露方式）。
  - 建立**個人 prompt library**：把 5–10 個常用任務寫成可重複使用的 prompt 範本。
  - 用遊戲練習（猜謎、二十個問題、共同說故事等），輕鬆地磨 Description 和 Discernment。

---

## 讀完這門課你會得到什麼

一句話總結：**把「用 AI」從碰運氣變成有方法。**

- 一個可長期使用的思考框架（4D），適用於任何 AI 工具，不只 Claude。
- 一套馬上能用的 prompt 技巧（六招＋請 AI 改 prompt）。
- 一個實務工作節奏（Description-Discernment loop）。
- 一套負責任使用 AI 的原則與揭露範本（diligence statement）。

如果你是團隊裡推動 AI 導入的人，這門課也很適合當作**非技術同事的第一門課**。

---

*課程版權：Rick Dakan、Joseph Feller 與 Anthropic，CC BY-NC-SA 4.0 授權。*
