# 課程導讀學習站（原型）

把 repo 根目錄的七份 `overview_*.md` 拆成結構化資料，做成一個純靜態、不依賴任何 CDN 的單頁學習介面。

## 怎麼用

```bash
# 1. 從 Markdown 重新產生資料（改過任何 overview_*.md 或 build/concepts.json 之後都要跑）
python3 build/parse.py

# 2. 開站：直接雙擊 site/index.html，或起一個本機伺服器
python3 -m http.server 8000 -d site
```

不需要安裝任何套件，Python 3.10 以上即可。

## GitHub Pages

`.github/workflows/pages.yml` 會在 push 到 `main` 時重新執行 `build/parse.py`，把 `site/` 部署到
https://wendyhsieh-bigdata.github.io/claude-certified-architect-foundations-prep-courses/ 。
第一次部署若失敗，到 repo 的 Settings → Pages 把 Source 設為 **GitHub Actions** 後重跑即可。

## 檔案

| 路徑 | 角色 |
|---|---|
| `build/parse.py` | 解析器。把每份導讀切成「這門課在講什麼 / 先記住的表 / 各單元 / 學完得到什麼」四段，單元再切成區塊（段落、表格、程式碼、清單、引言），標記含「搞混、陷阱、注意」等字眼的段落為提醒，並抽出「**專有名詞**（中文解釋）」寫法的術語。 |
| `build/concepts.json` | 手工整理的跨課程知識：兩條學習路徑、11 個核心主題（共通要點、三平台差異表、對應到各份導讀的哪個單元）、易搞混卡與數字卡。 |
| `site/data/*.js` | 由 `parse.py` 產生：每門課一個 `course-<id>.js`，加一個 `meta.js`（術語表、學習路徑、核心主題、卡片）。是唯一的資料來源，不要手改。 |
| `site/index.html` `site/app.js` `site/style.css` | 前端。hash 路由：`#/` 首頁、`#/course/<id>` 課程閱讀、`#/core/<topic>` 核心合併視圖、`#/cards` 卡片、`#/glossary` 術語表。 |

## 功能

- **首頁**：非技術軌與開發者軌兩條學習路徑，每門課顯示單元數、預估閱讀時間、陷阱提示數與已讀進度。
- **課程頁**：固定四段結構；各單元收合成手風琴，展開後最上方列出該單元所有陷阱與提醒；右側黏住目錄；可勾「已讀」。
- **核心合併視圖**：Claude API、Amazon Bedrock、Google Cloud 三份課程是同一門課的三個版本。每個主題先看三平台共通核心，再看差異表，原文用分頁切換平台。
- **卡片**：易搞混卡與數字速記卡，點一下翻面，標記熟或不熟，可篩課程、只看不熟、隨機排序。
- **術語表**：自動抽出的術語，附出現在哪幾門課，可搜尋。

已讀進度、卡片標記、平台選擇、深淺色主題都存在瀏覽器的 localStorage，不需後端。

## 已知限制

- 三平台的「共通 / 差異」切分是手工整理在 `concepts.json`，導讀改版時要同步更新。
- 導讀中提到的原始筆記（`../Claude101.md` 等）不在這個 repo，介面只以導讀為素材。
- 三份平台導讀對 prompt caching 存活時間的說法不一致（1 小時 vs 5 分鐘），差異表照原文列出並加註。
