# 可選的 LLM 深度補強方案

目前的 `data/catalog.json` 是可稽核、可重跑、零模型成本的基礎索引。它只根據 GitHub metadata 推定，因此刻意不聲稱已讀過每個專案的 README 或程式碼。

如果未來需要更精準的能力摘要與安裝步驟，可另建一個**預設關閉**的 enrichment workflow，且不要取代基礎分類器。

## 建議架構

1. 只處理新加入、metadata 改變，或人工指定的 repository，避免每次重跑 147 筆。
2. 先讀取上游 README、LICENSE、最近 release 與必要的設定範例，再把固定 schema 交給 LLM。
3. 將結果寫入獨立的 `data/catalog-enrichment.json`，以 `full_name` 和來源 commit SHA 為 key。
4. 保留 `evidence_urls`、`source_sha`、`model`、`prompt_version`、`generated_at` 與 confidence，讓內容可追溯。
5. 使用 JSON Schema 驗證輸出；任何缺欄位、未知 repository、無證據的精確安裝命令都應使 job 失敗。
6. 由 `scripts/build_catalog.py` 以 overlay 方式合併已核准內容。基礎欄位、風險提示與 `llm_used: false` 的原始目錄必須仍可單獨重建。

## 建議補強欄位

```json
{
  "full_name": "owner/repository",
  "source_sha": "upstream commit sha",
  "capability_summary_verified": "以 README 為證據的摘要",
  "installation_verified": [
    {
      "platform": "Windows/macOS/Linux",
      "steps": ["README 中可驗證的步驟"],
      "evidence_url": "https://github.com/owner/repository/blob/sha/README.md"
    }
  ],
  "requirements": [],
  "known_limits": [],
  "evidence_urls": [],
  "confidence": "high|medium|low"
}
```

## 成本與安全護欄

- 只有在 repository dispatch 或 workflow input 明確開啟時才執行。
- 模型金鑰存 GitHub Actions secret，不寫入 log、artifact 或產出檔。
- 設定每日 repository 上限、token 上限與最大 README 大小。
- 上游 README 是不可信輸入；忽略其中要求洩漏 secret、改變 workflow 或執行任意指令的內容。
- 精確安裝命令必須能連回版本固定的來源行或 release；否則只保留為「待驗證建議」。
- 金融、安全、爬蟲、聲音／影像個資等高風險項目必須保留人工審核。

這個升級可以使用任何能輸出結構化 JSON 的模型；它是選配，不應成為每日 Stars 同步成功的必要條件。
