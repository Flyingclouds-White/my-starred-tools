# my-starred-tools

把 `Flyingclouds-White` 的 GitHub Stars 每日同步成可供人與 ChatGPT 搜尋的個人工具庫。

## 主要輸出

- [`STARRED.md`](STARRED.md)：依加星時間排列的原始易讀清單。
- [`data/starred-repositories.json`](data/starred-repositories.json)：GitHub API metadata 快照。
- [`CATALOG.md`](CATALOG.md)：依主分類瀏覽的工具目錄，包含能力、用途、安裝推定、ChatGPT 可協助程度、維護與風險提示。
- [`data/catalog.json`](data/catalog.json)：完整多標籤資料與可搜尋反向索引，適合交給 ChatGPT、程式或 `jq` 查詢。

## 自動更新方式

`.github/workflows/sync-stars.yml` 保留原有 Stars 同步流程，並在抓取 metadata 後執行：

```sh
python scripts/build_catalog.py
python -m unittest discover -s tests -v
```

整個基礎版只使用 GitHub API、`jq` 與 Python 標準函式庫，**不需要 LLM、付費 API 或額外 Python 套件**。GitHub Actions 每天執行，也可從 Actions 頁面手動執行。

## 如何交給 ChatGPT 使用

優先提供 `data/catalog.json`，然後直接描述條件，例如：

> 從我的工具庫找可在 Windows 自架的語音轉錄工具。只看仍活躍的項目，列出安裝推定、風險與你能協助的部分。

> 比較 capability 為 presentation-docs 的項目，優先選 ChatGPT assistance 4/5 以上者。

JSON 內含下列索引：

- `indexes.by_category`
- `indexes.by_capability`
- `indexes.by_language`
- `indexes.by_maintenance`
- `indexes.by_chatgpt_assistance`
- `indexes.by_risk_level`
- `indexes.by_tag`

所有推定都保留命中的 metadata evidence。安裝資訊不會憑空產生套件名稱或指令，而是提示應檢查的檔案與可能路徑；真正採用前仍要核對上游 README、LICENSE、Releases 與 issues。

## 本機重建

```sh
python scripts/build_catalog.py \
  --input data/starred-repositories.json \
  --json-output data/catalog.json \
  --markdown-output CATALOG.md
```

可選的 LLM 深度補強設計見 [`docs/OPTIONAL_LLM_ENRICHMENT.md`](docs/OPTIONAL_LLM_ENRICHMENT.md)。基礎 workflow 不會呼叫它，也不需要任何模型金鑰。
