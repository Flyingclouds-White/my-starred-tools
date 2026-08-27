# ChatGPT 可理解的個人工具庫

這份目錄由 GitHub Stars 的公開 metadata 自動產生，**基礎版不使用 LLM，也不需要付費 API**。

- Repository 數：**147**
- 產生時間（UTC）：`2026-08-27T14:06:35.863631Z`
- 分類器：`metadata-rules-v1`
- 判斷依據：name、description、topics、language、license、archived/disabled 與 pushed_at

> 分類、能力、安裝方式與風險皆是 metadata 推定。採用前請閱讀上游 README、LICENSE、Releases 與 issues。

## 如何搜尋

`data/catalog.json` 是給 ChatGPT、程式與 `jq` 使用的完整索引；本頁適合人工瀏覽。可以直接要求 ChatGPT：

- 找出可做影片自動化、ChatGPT 協助程度至少 4/5、且仍活躍的工具。
- 比較所有簡報工具的安裝路徑、授權與風險提示。
- 從自架工具中挑出不需外部 API 的候選項目，再逐一讀 README 驗證。

快速查詢範例：

```sh
jq -r '.indexes.by_capability["video-production"][]' data/catalog.json
jq -r '.repositories[] | select(.chatgpt_assistance.score >= 4 and .maintenance.status == "active") | .full_name' data/catalog.json
jq -r '.repositories[] | select(.risks.highest_level == "high") | [.full_name, .risks.items[0].message] | @tsv' data/catalog.json
```

## 分類總覽

| 主分類 | Repository 數 |
|---|---:|
| [AI Agent 與 Agent Skills](#category-ai-agents) | 25 |
| [知識、研究與記憶](#category-knowledge-research) | 24 |
| [設計、UI 與前端](#category-design-ui) | 13 |
| [影片與媒體製作](#category-video-media) | 11 |
| [影像與創意生成](#category-image-creative) | 8 |
| [生產力與工作管理](#category-productivity) | 8 |
| [簡報與文件](#category-presentation-docs) | 7 |
| [資安、隱私與稽核](#category-security-privacy) | 6 |
| [待分類](#category-uncategorized) | 5 |
| [語音、音訊與轉錄](#category-audio-speech) | 5 |
| [資源清單與參考素材](#category-reference-collection) | 5 |
| [文化、命理與宗教](#category-culture-divination) | 4 |
| [模擬、3D 與機器人](#category-simulation-robotics) | 4 |
| [自動化與整合](#category-automation-integration) | 4 |
| [資料、機器學習與分析](#category-data-ai) | 4 |
| [金融與交易](#category-finance) | 4 |
| [學習與教學](#category-education) | 3 |
| [Web、桌面與平台](#category-web-platform) | 2 |
| [社群、行銷與內容](#category-social-content) | 2 |
| [開發與程式碼工具](#category-developer-tools) | 2 |
| [家庭、自動化與 IoT](#category-home-iot) | 1 |

<a id="category-ai-agents"></a>
## AI Agent 與 Agent Skills

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | 主要能力：AI Agent 建構與編排、Agent Skill／提示工作流。依專案描述：Structured multi-perspective deliberation for hard decisions. Run full councils, focused triads, or duo debates across Claude Code, Codex, Gemini CLI, and OpenCode. | 開發與程式碼工具、AI Agent 建構與編排、Agent Skill／提示工作流 | Agent Skill 安裝、Shell 腳本／設定檔 | 4/5（高） | 活躍 | 中 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 主要能力：Agent Skill／提示工作流、程式開發、理解與審查。依專案描述：Production-grade engineering skills for AI coding agents. | 開發與程式碼工具、Agent Skill／提示工作流、程式開發、理解與審查 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [anthropics/skills](https://github.com/anthropics/skills) | 主要能力：Agent Skill／提示工作流。依專案描述：Public repository for Agent Skills | Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |
| [b-nnett/codex-plusplus](https://github.com/b-nnett/codex-plusplus) | 主要能力：一般工具／待確認。依專案描述：Codex++ tweak system for the Codex desktop app | 一般工具／待確認 | Node.js／JavaScript | 3/5（中等） | 已封存 | 高 |
| [binghe1980/AI-Canvas](https://github.com/binghe1980/AI-Canvas) | 主要能力：一般工具／待確認。依專案描述：Codex-integrated infinite canvas for AI image generation, annotation, and iterative editing. | 一般工具／待確認 | Node.js／TypeScript | 3/5（中等） | 活躍 | 資訊 |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 主要能力：MCP／工具整合、瀏覽器操作與資料蒐集。依專案描述：The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra | 自動化與整合、Web、桌面與平台、MCP／工具整合、瀏覽器操作與資料蒐集 | MCP server 設定、Node.js／TypeScript | 3/5（中等） | 活躍 | 資訊 |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 主要能力：Agent Skill／提示工作流、MCP／工具整合、本機或自架應用。依專案描述：Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifa… | 自動化與整合、Web、桌面與平台、Agent Skill／提示工作流、MCP／工具整合、本機或自架應用 | Agent Skill 安裝、MCP server 設定 | 4/5（高） | 活躍 | 中 |
| [DavidBB-L/cinema-manager](https://github.com/DavidBB-L/cinema-manager) | 主要能力：Agent Skill／提示工作流。依專案描述：Hermes Agent skill - Movie/TV resource search + Quark cloud drive auto-save | Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 主要能力：Agent Skill／提示工作流、AI Agent 建構與編排、程式開發、理解與審查。依專案描述：Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 開發與程式碼工具、Agent Skill／提示工作流、AI Agent 建構與編排、程式開發、理解與審查 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [Dimillian/Skills](https://github.com/Dimillian/Skills) | 主要能力：Agent Skill／提示工作流。依專案描述：My Codex Skills | Agent Skill／提示工作流 | Agent Skill 安裝、Shell 腳本／設定檔 | 4/5（高） | 活躍 | 無明顯提示 |
| [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | 主要能力：Agent Skill／提示工作流。依專案描述：dontbesilent 的商业诊断 Skills | Agent Skill／提示工作流 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [Felo-Inc/felo-skills](https://github.com/Felo-Inc/felo-skills) | 主要能力：Agent Skill／提示工作流。metadata 描述不足，需閱讀 README 進一步確認。 | Agent Skill／提示工作流 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [google/skills](https://github.com/google/skills) | 主要能力：Agent Skill／提示工作流。依專案描述：Agent Skills for Google products and technologies | Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 資訊 |
| [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | 主要能力：程式開發、理解與審查、Agent Skill／提示工作流。依專案描述：AI code reviews grounded in 12 classic engineering books — decay risk diagnostics with book citations, severity labels, and 6 analysis modes including full-sweep auto-fix | 開發與程式碼工具、程式開發、理解與審查、Agent Skill／提示工作流 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 主要能力：一般工具／待確認。依專案描述：🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman | 一般工具／待確認 | Go 專案 | 3/5（中等） | 活躍 | 中 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 主要能力：Agent Skill／提示工作流。依專案描述：Skills for Real Engineers. Straight from my .agents directory. | Agent Skill／提示工作流 | Agent Skill 安裝、Shell 腳本／設定檔 | 4/5（高） | 活躍 | 資訊 |
| [maylogger/AGI](https://github.com/maylogger/AGI) | 主要能力：AI Agent 建構與編排。依專案描述：Agentic Guideline Intelligence | AI Agent 建構與編排 | 直接閱讀／複製範例、Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [Ming-H/yinyuan-skills](https://github.com/Ming-H/yinyuan-skills) | 主要能力：Agent Skill／提示工作流。依專案描述：yinyuan-skills | Agent Skill／提示工作流 | Agent Skill 安裝 | 4/5（高） | 活躍 | 中 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 主要能力：Agent Skill／提示工作流、程式開發、理解與審查。依專案描述：A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. | 開發與程式碼工具、Agent Skill／提示工作流、程式開發、理解與審查 | Agent Skill 安裝 | 4/5（高） | 活躍 | 中 |
| [obra/superpowers](https://github.com/obra/superpowers) | 主要能力：Agent Skill／提示工作流、AI Agent 建構與編排、程式開發、理解與審查。依專案描述：An agentic skills framework & software development methodology that works. | 開發與程式碼工具、Agent Skill／提示工作流、AI Agent 建構與編排、程式開發、理解與審查 | Agent Skill 安裝、Shell 腳本／設定檔 | 4/5（高） | 活躍 | 資訊 |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 主要能力：Agent Skill／提示工作流。依專案描述：Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。 | Agent Skill／提示工作流 | Agent Skill 安裝 | 4/5（高） | 近期維護 | 中 |
| [stablyai/orca](https://github.com/stablyai/orca) | 主要能力：AI Agent 建構與編排、程式開發、理解與審查。依專案描述：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS. | 開發與程式碼工具、AI Agent 建構與編排、程式開發、理解與審查 | Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | 主要能力：監控、可觀測性與情報、MCP／工具整合、工作流程自動化。依專案描述：📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. \| 用 AI 构建你专属的新闻雷达 | 自動化與整合、監控、可觀測性與情報、MCP／工具整合、工作流程自動化 | MCP server 設定、Python 環境 | 4/5（高） | 活躍 | 資訊 |
| [vibeshotclub/vsc-skills](https://github.com/vibeshotclub/vsc-skills) | 主要能力：Agent Skill／提示工作流。metadata 描述不足，需閱讀 README 進一步確認。 | Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |
| [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | 主要能力：Agent Skill／提示工作流、AI Agent 建構與編排、工作流程自動化。依專案描述：YAO = Yielding AI Outcomes. A rigorous engineering, evaluation, governance, and portability system for reusable agent skills. | 自動化與整合、Agent Skill／提示工作流、AI Agent 建構與編排、工作流程自動化 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 資訊 |

<a id="category-web-platform"></a>
## Web、桌面與平台

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [baojie/shiji-kb](https://github.com/baojie/shiji-kb) | 主要能力：一般工具／待確認。metadata 描述不足，需閱讀 README 進一步確認。 | 一般工具／待確認 | 靜態網頁／Web 專案 | 3/5（中等） | 活躍 | 中 |
| [monoscope-tech/monoscope](https://github.com/monoscope-tech/monoscope) | 主要能力：監控、可觀測性與情報、本機或自架應用。依專案描述：Monoscope lets you ingest and explore your logs, traces and metrics. We store these in S3 compatible buckets. Query in natural language via LLMs. | 監控、可觀測性與情報、本機或自架應用 | 容器／自架部署、Haskell 專案 | 3/5（中等） | 活躍 | 資訊 |

<a id="category-education"></a>
## 學習與教學

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [bryanyzhu/agentic-ai-system-course](https://github.com/bryanyzhu/agentic-ai-system-course) | 主要能力：AI Agent 建構與編排、研究、學習與教學、工作流程自動化。依專案描述：Use agent to learn agent - A skeleton course on how to design, build, and operate production AI agents | AI Agent 與 Agent Skills、自動化與整合、設計、UI 與前端、AI Agent 建構與編排、研究、學習與教學 | 直接閱讀／複製範例、Node.js／JavaScript | 4/5（高） | 活躍 | 資訊 |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 主要能力：AI Agent 建構與編排、研究、學習與教學。依專案描述：18 Lessons to Get Started Building AI Agents | AI Agent 與 Agent Skills、AI Agent 建構與編排、研究、學習與教學 | Jupyter Notebook | 3/5（中等） | 活躍 | 資訊 |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | 主要能力：研究、學習與教學、AI Agent 建構與編排。依專案描述：Bash is all you need - A nano claude code–like 「agent harness」, built from 0 to 1 | AI Agent 與 Agent Skills、研究、學習與教學、AI Agent 建構與編排 | Python 環境 | 3/5（中等） | 活躍 | 中 |

<a id="category-home-iot"></a>
## 家庭、自動化與 IoT

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate) | 主要能力：工作流程自動化。依專案描述：NVR with realtime local object detection for IP cameras | 自動化與整合、工作流程自動化 | Node.js／TypeScript | 3/5（中等） | 活躍 | 高 |

<a id="category-image-creative"></a>
## 影像與創意生成

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | 主要能力：圖片生成、編輯與參考、範例、模板與資源索引。依專案描述：GPT-Image-2 API and Prompts | 資源清單與參考素材、自動化與整合、圖片生成、編輯與參考、範例、模板與資源索引 | 直接閱讀／複製範例、Python 環境 | 4/5（高） | 活躍 | 中 |
| [liyue-aigc/female-portrait-director](https://github.com/liyue-aigc/female-portrait-director) | 主要能力：Agent Skill／提示工作流、圖片生成、編輯與參考。依專案描述：A modular Codex Skill for directing and expanding detailed AI female portrait prompts. | AI Agent 與 Agent Skills、Agent Skill／提示工作流、圖片生成、編輯與參考 | Agent Skill 安裝 | 3/5（中等） | 活躍 | 高 |
| [op7418/guizang-material-illustration](https://github.com/op7418/guizang-material-illustration) | 主要能力：圖片生成、編輯與參考、資料分析、視覺化與預測、內容企劃與社群發布。依專案描述：归藏的材质插画 skill：生成带字解释图、图表美化和参考辅助配图。 | AI Agent 與 Agent Skills、資料、機器學習與分析、社群、行銷與內容、圖片生成、編輯與參考、資料分析、視覺化與預測 | 依 README 判斷 | 3/5（中等） | 活躍 | 中 |
| [photoprism/photoprism](https://github.com/photoprism/photoprism) | 主要能力：圖片生成、編輯與參考、本機或自架應用、研究、學習與教學。依專案描述：AI-Powered Photos App 🌈💎✨ | 資料、機器學習與分析、Web、桌面與平台、學習與教學、圖片生成、編輯與參考、本機或自架應用 | 容器／自架部署、Go 專案 | 3/5（中等） | 活躍 | 中 |
| [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | 主要能力：Agent Skill／提示工作流、圖片生成、編輯與參考、範例、模板與資源索引。依專案描述：GPT Image 2 prompt gallery, image prompt library, agentic skill, and CLI for OpenAI image generation/editing | AI Agent 與 Agent Skills、資源清單與參考素材、開發與程式碼工具、知識、研究與記憶、Agent Skill／提示工作流 | 直接閱讀／複製範例、Agent Skill 安裝 | 4/5（高） | 活躍 | 中 |
| [yangchuansheng/visual-ip-illustrations](https://github.com/yangchuansheng/visual-ip-illustrations) | 主要能力：圖片生成、編輯與參考。依專案描述：Codex Skill for consistent 16:9 hand-drawn article illustrations with selectable visual IP routes: Openclaw, Xiaohei, Littlebox, Tom, Ferris, Seal and Gopher. | AI Agent 與 Agent Skills、圖片生成、編輯與參考 | Node.js／JavaScript | 3/5（中等） | 活躍 | 無明顯提示 |
| [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | 主要能力：圖片生成、編輯與參考、範例、模板與資源索引。依專案描述：🚀 World's largest GPT Image 2 prompt library, updated daily — 2000+ curated prompts with preview images, 16 languages. OpenAI's next-gen image model with pixel-perfect text rendering, cr… | 資源清單與參考素材、圖片生成、編輯與參考、範例、模板與資源索引 | 直接閱讀／複製範例、Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [zhouwei713/gpt-image-2-prompting-skill](https://github.com/zhouwei713/gpt-image-2-prompting-skill) | 主要能力：圖片生成、編輯與參考、範例、模板與資源索引。依專案描述：A high-quality GPT-Image-2 prompting skill with bilingual README, structured prompting methods, templates, and examples. | AI Agent 與 Agent Skills、資源清單與參考素材、圖片生成、編輯與參考、範例、模板與資源索引 | 直接閱讀／複製範例 | 4/5（高） | 活躍 | 資訊 |

<a id="category-video-media"></a>
## 影片與媒體製作

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [Agentchengfeng/chengfeng-videocut-skills](https://github.com/Agentchengfeng/chengfeng-videocut-skills) | 主要能力：Agent Skill／提示工作流、影片生成、剪輯與轉檔。依專案描述：用 Claude Code Skills 做的视频剪辑 Agent | AI Agent 與 Agent Skills、Agent Skill／提示工作流、影片生成、剪輯與轉檔 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 主要能力：影片生成、剪輯與轉檔、語音生成、辨識與轉錄、Agent Skill／提示工作流。依專案描述：World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding as… | AI Agent 與 Agent Skills、語音、音訊與轉錄、開發與程式碼工具、影像與創意生成、知識、研究與記憶 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |
| [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) | 主要能力：影片生成、剪輯與轉檔。依專案描述：skill to create best prompts for generating videos with seedance2.0 | AI Agent 與 Agent Skills、影片生成、剪輯與轉檔 | 依 README 判斷 | 3/5（中等） | 近期維護 | 無明顯提示 |
| [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | 主要能力：影片生成、剪輯與轉檔、內容企劃與社群發布、工作流程自動化。依專案描述：Fill-in-your-own-data framework for YouTube / short-form video automation: CapCut JSON + ffmpeg tooling + an onboarding questionnaire. Ships with zero private data. | 社群、行銷與內容、自動化與整合、資料、機器學習與分析、影片生成、剪輯與轉檔、內容企劃與社群發布 | Python 環境 | 4/5（高） | 活躍 | 資訊 |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 主要能力：影片生成、剪輯與轉檔、內容企劃與社群發布、工作流程自動化。依專案描述：利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | 自動化與整合、語音、音訊與轉錄、社群、行銷與內容、AI Agent 與 Agent Skills、影片生成、剪輯與轉檔 | Python 環境 | 4/5（高） | 活躍 | 資訊 |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 主要能力：影片生成、剪輯與轉檔、MCP／工具整合。依專案描述：Write HTML. Render video. Built for agents. | AI Agent 與 Agent Skills、Web、桌面與平台、影片生成、剪輯與轉檔、MCP／工具整合 | MCP server 設定、Node.js／TypeScript | 3/5（中等） | 活躍 | 資訊 |
| [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | 主要能力：影片生成、剪輯與轉檔、AI Agent 建構與編排。依專案描述："ViMax: Agentic Video Generation (Director, Screenwriter, Producer, and Video Generator All-in-One)" | AI Agent 與 Agent Skills、影片生成、剪輯與轉檔、AI Agent 建構與編排 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [NarratorAI-Studio/narrator-ai-cli-skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) | 主要能力：Agent Skill／提示工作流、影片生成、剪輯與轉檔、AI Agent 建構與編排。依專案描述：AI 解说大师 — Agent skill；封装 narrator-ai-cli 供 Claude/Codex 等工具调用 | AI Agent 與 Agent Skills、社群、行銷與內容、Agent Skill／提示工作流、影片生成、剪輯與轉檔、AI Agent 建構與編排 | Agent Skill 安裝 | 4/5（高） | 活躍 | 中 |
| [nexu-io/html-video](https://github.com/nexu-io/html-video) | 主要能力：影片生成、剪輯與轉檔、AI Agent 建構與編排、程式開發、理解與審查。依專案描述：Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apach… | AI Agent 與 Agent Skills、開發與程式碼工具、設計、UI 與前端、資料、機器學習與分析、Web、桌面與平台 | 直接閱讀／複製範例、靜態網頁／Web 專案 | 4/5（高） | 活躍 | 中 |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 主要能力：內容企劃與社群發布、AI Agent 建構與編排、MCP／工具整合。依專案描述：Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees. | AI Agent 與 Agent Skills、自動化與整合、開發與程式碼工具、社群、行銷與內容、內容企劃與社群發布 | MCP server 設定、Python 環境 | 4/5（高） | 活躍 | 高 |
| [xiaohuailabs/xiaohu-video-translate](https://github.com/xiaohuailabs/xiaohu-video-translate) | 主要能力：影片生成、剪輯與轉檔。依專案描述：对 AI 说一句话，把外语视频自动配上中文字幕 —— 下载/转写/翻译/润色/烧录一条龙，全程本地，转写零 API 费 | 自動化與整合、影片生成、剪輯與轉檔 | Python 環境 | 3/5（中等） | 活躍 | 中 |

<a id="category-uncategorized"></a>
## 待分類

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [ayuhamaro/Startup-Contradictions](https://github.com/ayuhamaro/Startup-Contradictions) | 主要能力：一般工具／待確認。metadata 描述不足，需閱讀 README 進一步確認。 | 一般工具／待確認 | 依 README 判斷 | 3/5（中等） | 活躍 | 中 |
| [joeseesun/qiaomu-artist-style](https://github.com/joeseesun/qiaomu-artist-style) | 主要能力：一般工具／待確認。metadata 描述不足，需閱讀 README 進一步確認。 | 一般工具／待確認 | Node.js／TypeScript | 3/5（中等） | 活躍 | 中 |
| [limuloo/RefineAnything](https://github.com/limuloo/RefineAnything) | 主要能力：一般工具／待確認。metadata 描述不足，需閱讀 README 進一步確認。 | 一般工具／待確認 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | 主要能力：一般工具／待確認。依專案描述：A lightweight gallery of mathematical curve based loading animations with modal previews, formulas, and copyable code snippets. | 一般工具／待確認 | Node.js／JavaScript | 3/5（中等） | 活躍 | 中 |
| [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | 主要能力：一般工具／待確認。metadata 描述不足，需閱讀 README 進一步確認。 | 一般工具／待確認 | Node.js／JavaScript | 3/5（中等） | 活躍 | 低 |

<a id="category-culture-divination"></a>
## 文化、命理與宗教

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [daman-ovo-0404/tarot-skill](https://github.com/daman-ovo-0404/tarot-skill) | 主要能力：文化、宗教與命理內容、Agent Skill／提示工作流。依專案描述：AI 塔罗占卜 Agent Skill — 78 牌完整牌义、6 种牌阵、牌间关系理论体系、真随机抽牌脚本 | AI Agent 與 Agent Skills、文化、宗教與命理內容、Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |
| [FANzR-arch/Numerologist_skills](https://github.com/FANzR-arch/Numerologist_skills) | 主要能力：文化、宗教與命理內容、Agent Skill／提示工作流。依專案描述：🔮 An engineering framework to stop LLM hallucinations in Chinese astrology. / 给“赛博半仙”戴上紧箍咒：减少幻觉、固定排盘步骤的奇门遁甲与紫微斗数 AI skills。 | AI Agent 與 Agent Skills、文化、宗教與命理內容、Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |
| [jinchenma94/bazi-skill](https://github.com/jinchenma94/bazi-skill) | 主要能力：文化、宗教與命理內容。依專案描述：四柱八字命理分析 | AI Agent 與 Agent Skills、文化、宗教與命理內容 | Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | 主要能力：文化、宗教與命理內容。依專案描述：紫微斗数开源排盘引擎 — 基于倪海夏《天纪》体系，含完整排盘算法、四化系统、格局知识库、古籍原文数据 | Web、桌面與平台、文化、宗教與命理內容 | Node.js／TypeScript | 3/5（中等） | 活躍 | 資訊 |

<a id="category-simulation-robotics"></a>
## 模擬、3D 與機器人

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [Genesis-Embodied-AI/genesis-world](https://github.com/Genesis-Embodied-AI/genesis-world) | 主要能力：模擬、3D 與互動視覺、研究、學習與教學。依專案描述：Simulation platform for general-purpose robotics & embodied AI learning. | 學習與教學、模擬、3D 與互動視覺、研究、學習與教學 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [oso95/scroll-world](https://github.com/oso95/scroll-world) | 主要能力：模擬、3D 與互動視覺。依專案描述：A skill that turn any brand into a scrollable 3D world landing page | AI Agent 與 Agent Skills、模擬、3D 與互動視覺 | Node.js／JavaScript | 3/5（中等） | 活躍 | 無明顯提示 |
| [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | 主要能力：模擬、3D 與互動視覺。依專案描述：A contact solver for physics-based simulations involving 👚 shells, 🪵 solids, 🪢 rods, 🧱 rigid bodies and ⏳ sand. | 模擬、3D 與互動視覺 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [yazelin/red-cliffs-3d](https://github.com/yazelin/red-cliffs-3d) | 主要能力：模擬、3D 與互動視覺。依專案描述：赤壁之戰 208 全 3D 戰場重現 — 單一 HTML + Three.js,九幕時間軸、電影運鏡、計策與火攻特效(demo 由 Claude Fable 5 產生) | Web、桌面與平台、模擬、3D 與互動視覺 | 靜態網頁／Web 專案 | 3/5（中等） | 已封存 | 高 |

<a id="category-productivity"></a>
## 生產力與工作管理

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 主要能力：AI Agent 建構與編排、瀏覽器操作與資料蒐集、工作流程自動化。依專案描述：🌐 Make websites accessible for AI agents. Automate tasks online with ease. | AI Agent 與 Agent Skills、自動化與整合、Web、桌面與平台、AI Agent 建構與編排、瀏覽器操作與資料蒐集 | Python 環境 | 4/5（高） | 活躍 | 資訊 |
| [cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox) | 主要能力：AI Agent 建構與編排、本機或自架應用。依專案描述：A self-hosted email client with an AI agent, running entirely on Cloudflare Workers | Web、桌面與平台、AI Agent 與 Agent Skills、AI Agent 建構與編排、本機或自架應用 | 容器／自架部署、Node.js／TypeScript | 2/5（有限） | 活躍 | 高 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 主要能力：AI Agent 建構與編排。依專案描述：Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. | AI Agent 與 Agent Skills、AI Agent 建構與編排 | Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 主要能力：工作流程自動化。依專案描述：An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. | 工作流程自動化 | Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [lijigang/copy-notes](https://github.com/lijigang/copy-notes) | 主要能力：一般工具／待確認。依專案描述：Copy text anywhere on macOS → auto-append it to a single Apple Notes note. A tiny bun/TypeScript launchd clipboard agent. | 一般工具／待確認 | Node.js／TypeScript | 2/5（有限） | 活躍 | 高 |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | 主要能力：AI Agent 建構與編排。依專案描述：The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it. | AI Agent 與 Agent Skills、AI Agent 建構與編排 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus) | 主要能力：本機或自架應用。依專案描述：Self-hosted AI workspace. | Web、桌面與平台、本機或自架應用 | 容器／自架部署、Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck) | 主要能力：一般工具／待確認。依專案描述：Task-oriented AI Agent productivity platform | 一般工具／待確認 | Node.js／TypeScript | 3/5（中等） | 活躍 | 資訊 |

<a id="category-knowledge-research"></a>
## 知識、研究與記憶

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | 主要能力：Agent Skill／提示工作流、AI Agent 建構與編排、MCP／工具整合。依專案描述：Independent directory of useful skills, plugins, memory providers, tools, surfaces, and guides for Nous Research's open-source Hermes Agent. | AI Agent 與 Agent Skills、資源清單與參考素材、Agent Skill／提示工作流、AI Agent 建構與編排、MCP／工具整合 | 直接閱讀／複製範例、Agent Skill 安裝 | 3/5（中等） | 活躍 | 高 |
| [activeloopai/hivemind](https://github.com/activeloopai/hivemind) | 主要能力：AI Agent 建構與編排、知識庫、RAG 與記憶、Agent Skill／提示工作流。依專案描述：Hivemind turns your traces into reusable skills across agents | AI Agent 與 Agent Skills、AI Agent 建構與編排、知識庫、RAG 與記憶、Agent Skill／提示工作流 | Agent Skill 安裝、Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 主要能力：AI Agent 建構與編排、Agent Skill／提示工作流、MCP／工具整合。依專案描述：The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and be… | AI Agent 與 Agent Skills、開發與程式碼工具、生產力與工作管理、資安、隱私與稽核、AI Agent 建構與編排 | Agent Skill 安裝、MCP server 設定 | 3/5（中等） | 活躍 | 高 |
| [aliyun/hermes-tablestore-memory](https://github.com/aliyun/hermes-tablestore-memory) | 主要能力：知識庫、RAG 與記憶。metadata 描述不足，需閱讀 README 進一步確認。 | 知識庫、RAG 與記憶 | Python 環境 | 3/5（中等） | 活躍 | 低 |
| [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | 主要能力：知識庫、RAG 與記憶、Agent Skill／提示工作流。依專案描述：Framework for AI agents to build and maintain a digital brain through Obsidian wiki | AI Agent 與 Agent Skills、資料、機器學習與分析、知識庫、RAG 與記憶、Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 資訊 |
| [beltromatti/get-it](https://github.com/beltromatti/get-it) | 主要能力：知識庫、RAG 與記憶、研究、學習與教學、簡報與文件生成。依專案描述：Read it. See it. Get it. Built at GDG AI Hack Milan 2026 for "Learn Different" track. | 學習與教學、AI Agent 與 Agent Skills、資料、機器學習與分析、Web、桌面與平台、簡報與文件 | Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 主要能力：程式開發、理解與審查、MCP／工具整合、知識庫、RAG 與記憶。依專案描述：High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer toke… | 開發與程式碼工具、AI Agent 與 Agent Skills、資料、機器學習與分析、程式開發、理解與審查、MCP／工具整合 | MCP server 設定、原生編譯／Release | 4/5（高） | 活躍 | 中 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 主要能力：知識庫、RAG 與記憶、程式開發、理解與審查、Agent Skill／提示工作流。依專案描述：Graphs that teach &gt; graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Co… | AI Agent 與 Agent Skills、開發與程式碼工具、資料、機器學習與分析、知識庫、RAG 與記憶、程式開發、理解與審查 | Agent Skill 安裝、Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | 主要能力：知識庫、RAG 與記憶、範例、模板與資源索引。依專案描述：Google Cloud Knowledge Catalog Tools and Samples | 資源清單與參考素材、知識庫、RAG 與記憶、範例、模板與資源索引 | 直接閱讀／複製範例、Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 主要能力：程式開發、理解與審查、知識庫、RAG 與記憶、AI Agent 建構與編排。依專案描述：Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: loca… | AI Agent 與 Agent Skills、開發與程式碼工具、資料、機器學習與分析、程式開發、理解與審查、知識庫、RAG 與記憶 | Agent Skill 安裝、MCP server 設定 | 4/5（高） | 活躍 | 中 |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 主要能力：研究、學習與教學。依專案描述：AI agents running research on single-GPU nanochat training automatically | 研究、學習與教學 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [kdsz001/OpenWiki](https://github.com/kdsz001/OpenWiki) | 主要能力：知識庫、RAG 與記憶、本機或自架應用。依專案描述：OpenWiki — Mac desktop AI knowledge management tool. Capture clipboard, build personal wiki, get AI insights. | Web、桌面與平台、生產力與工作管理、知識庫、RAG 與記憶、本機或自架應用 | Rust 專案 | 2/5（有限） | 活躍 | 高 |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 主要能力：Agent Skill／提示工作流、知識庫、RAG 與記憶。依專案描述：Agent skills for Obsidian. Teach your agent to use Obsidian CLI and open formats including Markdown, Bases, JSON Canvas. | AI Agent 與 Agent Skills、開發與程式碼工具、Agent Skill／提示工作流、知識庫、RAG 與記憶 | Agent Skill 安裝 | 4/5（高） | 活躍 | 中 |
| [langchain-ai/agents-from-scratch](https://github.com/langchain-ai/agents-from-scratch) | 主要能力：知識庫、RAG 與記憶。依專案描述：Build an email assistant with human-in-the-loop and memory | 生產力與工作管理、知識庫、RAG 與記憶 | Jupyter Notebook | 2/5（有限） | 活躍 | 高 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 主要能力：AI Agent 建構與編排、知識庫、RAG 與記憶。依專案描述：Build resilient agents. | AI Agent 與 Agent Skills、資料、機器學習與分析、AI Agent 建構與編排、知識庫、RAG 與記憶 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [lokikill123/codex-token-skills](https://github.com/lokikill123/codex-token-skills) | 主要能力：Agent Skill／提示工作流、程式開發、理解與審查、知識庫、RAG 與記憶。依專案描述：⚡ Cut 60-80% token cost for DeepSeek V4 Pro on Codex CLI. token-saver + memory skills with prefix-cache optimization. | AI Agent 與 Agent Skills、開發與程式碼工具、Agent Skill／提示工作流、程式開發、理解與審查、知識庫、RAG 與記憶 | Agent Skill 安裝 | 4/5（高） | 活躍 | 資訊 |
| [mcncarl/agent-memory-vault](https://github.com/mcncarl/agent-memory-vault) | 主要能力：知識庫、RAG 與記憶、安全檢查與調查。依專案描述：Markdown-first shared memory vault for Claude Code and Codex with SQLite, Zvec, Git, closeout, and audit | AI Agent 與 Agent Skills、資安、隱私與稽核、知識庫、RAG 與記憶、安全檢查與調查 | Python 環境 | 2/5（有限） | 活躍 | 高 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | 主要能力：MCP／工具整合、知識庫、RAG 與記憶。依專案描述：The best-benchmarked open-source AI memory system. And it's free. | AI Agent 與 Agent Skills、MCP／工具整合、知識庫、RAG 與記憶 | MCP server 設定、Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | 主要能力：AI Agent 建構與編排、知識庫、RAG 與記憶。依專案描述：Memory that AI Agents Love! | AI Agent 與 Agent Skills、AI Agent 建構與編排、知識庫、RAG 與記憶 | Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | 主要能力：AI Agent 建構與編排、研究、學習與教學、本機或自架應用。依專案描述：Hermes WebUI: The best way to use Hermes Agent from the web or from your phone! | AI Agent 與 Agent Skills、Web、桌面與平台、AI Agent 建構與編排、研究、學習與教學、本機或自架應用 | Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 主要能力：AI Agent 建構與編排、研究、學習與教學。依專案描述：The agent that grows with you | AI Agent 與 Agent Skills、AI Agent 建構與編排、研究、學習與教學 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [oh-my-mermaid/oh-my-mermaid](https://github.com/oh-my-mermaid/oh-my-mermaid) | 主要能力：程式開發、理解與審查、Agent Skill／提示工作流、簡報與文件生成。依專案描述：Turn complex codebases into clear, navigable architecture diagrams with Claude Code. | 開發與程式碼工具、AI Agent 與 Agent Skills、簡報與文件、資料、機器學習與分析、程式開發、理解與審查 | Agent Skill 安裝、Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 主要能力：Agent Skill／提示工作流、知識庫、RAG 與記憶、範例、模板與資源索引。依專案描述：100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source. | AI Agent 與 Agent Skills、資源清單與參考素材、Agent Skill／提示工作流、知識庫、RAG 與記憶、範例、模板與資源索引 | 直接閱讀／複製範例、Agent Skill 安裝 | 4/5（高） | 活躍 | 資訊 |
| [xr843/Master-skill](https://github.com/xr843/Master-skill) | 主要能力：Agent Skill／提示工作流、知識庫、RAG 與記憶、文化、宗教與命理內容。依專案描述：FoJin-powered Buddhist AI persona framework — source-grounded, boundary-aware, fidelity-tested, runtime-ready. | AI Agent 與 Agent Skills、文化、命理與宗教、Agent Skill／提示工作流、知識庫、RAG 與記憶、文化、宗教與命理內容 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |

<a id="category-social-content"></a>
## 社群、行銷與內容

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [Hao0321/claude-skill-social-post](https://github.com/Hao0321/claude-skill-social-post) | 主要能力：內容企劃與社群發布、AI Agent 建構與編排、工作流程自動化。依專案描述：A Claude Code skill by Hao (駱君昊) that learns your Facebook voice and auto-posts to FB / IG / Threads / X with a 14-day content calendar. Mega-viral validated: 80K reach / 448… | AI Agent 與 Agent Skills、自動化與整合、語音、音訊與轉錄、生產力與工作管理、內容企劃與社群發布 | Python 環境 | 3/5（中等） | 活躍 | 高 |
| [qiayue/Twitter-Trend-Radar](https://github.com/qiayue/Twitter-Trend-Radar) | 主要能力：監控、可觀測性與情報、內容企劃與社群發布。依專案描述：Twitter Trend Radar | Web、桌面與平台、監控、可觀測性與情報、內容企劃與社群發布 | 靜態網頁／Web 專案 | 3/5（中等） | 活躍 | 無明顯提示 |

<a id="category-presentation-docs"></a>
## 簡報與文件

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | 主要能力：簡報與文件生成。依專案描述：Codex 橙皮书：从安装到实战案例的全链路 Codex 使用指南（非官方开源，含可下载 PDF） | AI Agent 與 Agent Skills、知識、研究與記憶、Web、桌面與平台、簡報與文件生成 | 靜態網頁／Web 專案 | 4/5（高） | 活躍 | 無明顯提示 |
| [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | 主要能力：簡報與文件生成、Agent Skill／提示工作流、AI Agent 建構與編排。依專案描述：An AI-agent skill that generates browser-editable presentations from multiple visual themes, exportable to HTML, PDF, and PPTX. | AI Agent 與 Agent Skills、Web、桌面與平台、知識、研究與記憶、簡報與文件生成、Agent Skill／提示工作流 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 主要能力：簡報與文件生成、AI Agent 建構與編排、語音生成、辨識與轉錄。依專案描述：AI turns documents or topics into real, native PowerPoint decks—with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from… | AI Agent 與 Agent Skills、語音、音訊與轉錄、知識、研究與記憶、資料、機器學習與分析、生產力與工作管理 | 直接閱讀／複製範例、Python 環境 | 4/5（高） | 活躍 | 資訊 |
| [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | 主要能力：簡報與文件生成、MCP／工具整合、工作流程自動化。依專案描述：Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc. | AI Agent 與 Agent Skills、知識、研究與記憶、自動化與整合、影片與媒體製作、語音、音訊與轉錄 | MCP server 設定、Python 環境 | 4/5（高） | 活躍 | 中 |
| [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | 主要能力：簡報與文件生成。依專案描述：HTML PPT Studio — AgentSkill with 24 themes, 31 layouts, 20+ animations for building professional HTML presentations | AI Agent 與 Agent Skills、Web、桌面與平台、簡報與文件生成 | 靜態網頁／Web 專案 | 4/5（高） | 活躍 | 資訊 |
| [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | 主要能力：Agent Skill／提示工作流、簡報與文件生成、AI Agent 建構與編排。依專案描述：AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime. | AI Agent 與 Agent Skills、設計、UI 與前端、影像與創意生成、Web、桌面與平台、模擬、3D 與機器人 | Agent Skill 安裝、靜態網頁／Web 專案 | 4/5（高） | 活躍 | 中 |
| [zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills) | 主要能力：簡報與文件生成、研究、學習與教學、Agent Skill／提示工作流。依專案描述：本仓库包含三个面向学术科研人员的Skills，覆盖从文献阅读、论文写作到科学计算的完整研究工作流。office-academic-skill 负责论文阅读报告与学术 PPT/Word 文档生成；research-writing-skill 提供论文写作、润色与审稿回复辅助；scientific-toolkit-skill 整合 MATLAB/P… | AI Agent 與 Agent Skills、知識、研究與記憶、簡報與文件生成、研究、學習與教學、Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |

<a id="category-automation-integration"></a>
## 自動化與整合

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [cloudflare/agents](https://github.com/cloudflare/agents) | 主要能力：工作流程自動化。依專案描述：Build and deploy AI Agents on Cloudflare | Web、桌面與平台、工作流程自動化 | Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [NangoHQ/nango](https://github.com/NangoHQ/nango) | 主要能力：工作流程自動化。依專案描述：Build product integrations with AI. | 工作流程自動化 | Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 主要能力：瀏覽器操作與資料蒐集。依專案描述：小红书笔记 \| 评论爬虫、抖音视频 \| 评论爬虫、快手视频 \| 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 \| 知乎问答文章｜评论爬虫 | 瀏覽器操作與資料蒐集 | Python 環境 | 3/5（中等） | 活躍 | 高 |
| [Salomondiei08/oh-my-hermes](https://github.com/Salomondiei08/oh-my-hermes) | 主要能力：工作流程自動化。依專案描述：An opinionated workflow layer for building, shipping, and operating apps with Hermes Agent | 工作流程自動化 | Shell 腳本／設定檔 | 4/5（高） | 活躍 | 中 |

<a id="category-design-ui"></a>
## 設計、UI 與前端

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | 主要能力：Agent Skill／提示工作流、設計系統與原型製作。依專案描述：Skills for Designers and Engineers. | AI Agent 與 Agent Skills、Agent Skill／提示工作流、設計系統與原型製作 | Agent Skill 安裝、文件／Skill 素材 | 4/5（高） | 活躍 | 無明顯提示 |
| [frank890417/WebToe](https://github.com/frank890417/WebToe) | 主要能力：模擬、3D 與互動視覺、程式開發、理解與審查、設計系統與原型製作。依專案描述：Web-native dataflow engine for real-time visuals — patch in the browser, TouchDesigner-style, and import your .toe projects. WebGL2 + WebGPU, zero dependencies. | 開發與程式碼工具、模擬、3D 與機器人、影像與創意生成、資料、機器學習與分析、Web、桌面與平台 | Node.js／TypeScript | 4/5（高） | 活躍 | 中 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 主要能力：設計系統與原型製作。依專案描述：Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA | 設計系統與原型製作 | Node.js／TypeScript | 3/5（中等） | 活躍 | 中 |
| [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 主要能力：AI Agent 建構與編排、程式開發、理解與審查、Agent Skill／提示工作流。依專案描述：Clone any website with one command using AI coding agents | AI Agent 與 Agent Skills、開發與程式碼工具、Web、桌面與平台、自動化與整合、AI Agent 建構與編排 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 高 |
| [jinggreen15/ai-design-team](https://github.com/jinggreen15/ai-design-team) | 主要能力：設計系統與原型製作、研究、學習與教學。依專案描述：A multi-role AI design team skill for research, planning, scripting, design, and content production. | AI Agent 與 Agent Skills、知識、研究與記憶、設計系統與原型製作、研究、學習與教學 | 依 README 判斷 | 3/5（中等） | 活躍 | 中 |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 主要能力：設計系統與原型製作、Agent Skill／提示工作流、程式開發、理解與審查。依專案描述：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop | AI Agent 與 Agent Skills、開發與程式碼工具、設計系統與原型製作、Agent Skill／提示工作流、程式開發、理解與審查 | Agent Skill 安裝、Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 主要能力：設計系統與原型製作。依專案描述：A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes,… | 設計系統與原型製作 | Shell 腳本／設定檔 | 3/5（中等） | 活躍 | 資訊 |
| [nevertoday/100-layout-compositions](https://github.com/nevertoday/100-layout-compositions) | 主要能力：設計系統與原型製作、範例、模板與資源索引。依專案描述：100 layout composition images for design and typography reference | 資料、機器學習與分析、資源清單與參考素材、設計系統與原型製作、範例、模板與資源索引 | 直接閱讀／複製範例 | 4/5（高） | 活躍 | 中 |
| [nevertoday/zhongguo-traditional-colors](https://github.com/nevertoday/zhongguo-traditional-colors) | 主要能力：設計系統與原型製作、範例、模板與資源索引。依專案描述：中华传统色演示、色卡浏览与颜色知识科普开源项目 | Web、桌面與平台、資源清單與參考素材、設計系統與原型製作、範例、模板與資源索引 | 直接閱讀／複製範例、靜態網頁／Web 專案 | 4/5（高） | 活躍 | 無明顯提示 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 主要能力：設計系統與原型製作、Agent Skill／提示工作流。依專案描述：An AI skill that provides design intelligence for building professional UI/UX across multiple platforms. | AI Agent 與 Agent Skills、Web、桌面與平台、設計系統與原型製作、Agent Skill／提示工作流 | Agent Skill 安裝、Python 環境 | 4/5（高） | 活躍 | 中 |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | 主要能力：設計系統與原型製作、Agent Skill／提示工作流、簡報與文件生成。依專案描述：🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, la… | AI Agent 與 Agent Skills、簡報與文件、影片與媒體製作、Web、桌面與平台、開發與程式碼工具 | Agent Skill 安裝 | 4/5（高） | 活躍 | 中 |
| [Paidax01/web-to-design-md](https://github.com/Paidax01/web-to-design-md) | 主要能力：設計系統與原型製作、簡報與文件生成。依專案描述：Convert any official website to design.md document | 簡報與文件、知識、研究與記憶、設計系統與原型製作、簡報與文件生成 | Node.js／JavaScript | 4/5（高） | 活躍 | 中 |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 主要能力：設計系統與原型製作、範例、模板與資源索引、程式開發、理解與審查。依專案描述：A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI. | 資源清單與參考素材、開發與程式碼工具、設計系統與原型製作、範例、模板與資源索引、程式開發、理解與審查 | 直接閱讀／複製範例 | 4/5（高） | 活躍 | 資訊 |

<a id="category-audio-speech"></a>
## 語音、音訊與轉錄

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [abus-aikorea/voice-pro](https://github.com/abus-aikorea/voice-pro) | 主要能力：語音生成、辨識與轉錄、影片生成、剪輯與轉檔、內容企劃與社群發布。依專案描述：Gradio WebUI for creators and developers, featuring key TTS (Edge-TTS, kokoro) and zero-shot Voice Cloning (E2 & F5-TTS, CosyVoice), with Whisper audio processing, YouTube down… | 影片與媒體製作、Web、桌面與平台、語音生成、辨識與轉錄、影片生成、剪輯與轉檔、內容企劃與社群發布 | Python 環境 | 2/5（有限） | 活躍 | 高 |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 主要能力：語音生成、辨識與轉錄、工作流程自動化、設計系統與原型製作。依專案描述：VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages. | 自動化與整合、設計、UI 與前端、影片與媒體製作、Web、桌面與平台、語音生成、辨識與轉錄 | Python 環境 | 3/5（中等） | 活躍 | 高 |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 主要能力：語音生成、辨識與轉錄。依專案描述：Open-Source Frontier Voice AI | 語音生成、辨識與轉錄 | Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 主要能力：語音生成、辨識與轉錄。依專案描述：💖🧸 Self hosted, you-owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minec… | Web、桌面與平台、語音生成、辨識與轉錄 | Node.js／TypeScript | 3/5（中等） | 活躍 | 資訊 |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | 主要能力：語音生成、辨識與轉錄、設計系統與原型製作、研究、學習與教學。依專案描述：VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning | 設計、UI 與前端、學習與教學、語音生成、辨識與轉錄、設計系統與原型製作、研究、學習與教學 | Python 環境 | 2/5（有限） | 活躍 | 高 |

<a id="category-security-privacy"></a>
## 資安、隱私與稽核

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 主要能力：安全檢查與調查、Agent Skill／提示工作流、程式開發、理解與審查。依專案描述：A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings | AI Agent 與 Agent Skills、開發與程式碼工具、Web、桌面與平台、安全檢查與調查、Agent Skill／提示工作流 | Agent Skill 安裝、Node.js／JavaScript | 3/5（中等） | 活躍 | 高 |
| [dongmingxuan2012-crypto/ai-copyright-self-check-skill](https://github.com/dongmingxuan2012-crypto/ai-copyright-self-check-skill) | 主要能力：安全檢查與調查。metadata 描述不足，需閱讀 README 進一步確認。 | AI Agent 與 Agent Skills、安全檢查與調查 | Shell 腳本／設定檔 | 3/5（中等） | 活躍 | 中 |
| [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | 主要能力：安全檢查與調查、監控、可觀測性與情報。依專案描述：Comfortably monitor your network traffic 🕵️‍♂️ | 安全檢查與調查、監控、可觀測性與情報 | Rust 專案 | 2/5（有限） | 活躍 | 高 |
| [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 主要能力：監控、可觀測性與情報、MCP／工具整合、瀏覽器操作與資料蒐集。依專案描述：Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface | AI Agent 與 Agent Skills、監控、可觀測性與情報、MCP／工具整合、瀏覽器操作與資料蒐集 | MCP server 設定、Node.js／TypeScript | 2/5（有限） | 活躍 | 高 |
| [nczz/freego-wp](https://github.com/nczz/freego-wp) | 主要能力：安全檢查與調查、工作流程自動化。依專案描述：WordPress accessibility assistant aligned with Freego checks, with repair, audit workflow, AAA targets, and GitHub updates. | 自動化與整合、安全檢查與調查、工作流程自動化 | PHP／WordPress | 3/5（中等） | 活躍 | 高 |
| [reconurge/flowsint](https://github.com/reconurge/flowsint) | 主要能力：安全檢查與調查、瀏覽器操作與資料蒐集。依專案描述：A modern platform for visual, flexible, and extensible graph-based investigations. For cybersecurity analysts and investigators. | 資料、機器學習與分析、安全檢查與調查、瀏覽器操作與資料蒐集 | Node.js／TypeScript | 2/5（有限） | 活躍 | 高 |

<a id="category-data-ai"></a>
## 資料、機器學習與分析

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | 主要能力：資料分析、視覺化與預測。依專案描述：A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visua… | 生產力與工作管理、Web、桌面與平台、資料分析、視覺化與預測 | Node.js／TypeScript | 3/5（中等） | 活躍 | 資訊 |
| [google-research/timesfm](https://github.com/google-research/timesfm) | 主要能力：資料分析、視覺化與預測、研究、學習與教學。依專案描述：TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. | 知識、研究與記憶、資料分析、視覺化與預測、研究、學習與教學 | Python 環境 | 3/5（中等） | 活躍 | 資訊 |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 主要能力：工作流程自動化、MCP／工具整合、本機或自架應用。依專案描述：Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. | 自動化與整合、AI Agent 與 Agent Skills、開發與程式碼工具、Web、桌面與平台、工作流程自動化 | MCP server 設定、容器／自架部署 | 4/5（高） | 活躍 | 中 |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 主要能力：本機或自架應用。依專案描述：Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 | 本機或自架應用 | Node.js／TypeScript | 3/5（中等） | 活躍 | 中 |

<a id="category-reference-collection"></a>
## 資源清單與參考素材

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [AICMO/AiCMO-Marketing-Prompt-Collection](https://github.com/AICMO/AiCMO-Marketing-Prompt-Collection) | 主要能力：範例、模板與資源索引、知識庫、RAG 與記憶、內容企劃與社群發布。依專案描述：AI CMO Prompts Collection and Knowledge Base | 知識、研究與記憶、金融與交易、社群、行銷與內容、範例、模板與資源索引、知識庫、RAG 與記憶 | 直接閱讀／複製範例 | 4/5（高） | 活躍 | 資訊 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | 主要能力：範例、模板與資源索引。依專案描述：A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. | 範例、模板與資源索引 | 直接閱讀／複製範例、Jupyter Notebook | 4/5（高） | 活躍 | 中 |
| [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | 主要能力：Agent Skill／提示工作流、程式開發、理解與審查、工作流程自動化。依專案描述：A curated list of practical Codex skills for automating workflows across the Codex CLI and API. | AI Agent 與 Agent Skills、開發與程式碼工具、自動化與整合、Agent Skill／提示工作流、程式開發、理解與審查 | 直接閱讀／複製範例、Agent Skill 安裝 | 4/5（高） | 活躍 | 中 |
| [openai/skills](https://github.com/openai/skills) | 主要能力：Agent Skill／提示工作流、範例、模板與資源索引。依專案描述：Skills Catalog for Codex | AI Agent 與 Agent Skills、Agent Skill／提示工作流、範例、模板與資源索引 | 直接閱讀／複製範例、Agent Skill 安裝 | 4/5（高） | 活躍 | 中 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 主要能力：MCP／工具整合、範例、模板與資源索引。依專案描述：A collection of MCP servers. | AI Agent 與 Agent Skills、MCP／工具整合、範例、模板與資源索引 | 直接閱讀／複製範例、MCP server 設定 | 4/5（高） | 活躍 | 資訊 |

<a id="category-finance"></a>
## 金融與交易

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [anthropics/financial-services](https://github.com/anthropics/financial-services) | 主要能力：金融研究與交易分析。metadata 描述不足，需閱讀 README 進一步確認。 | 金融研究與交易分析 | Python 環境 | 2/5（有限） | 活躍 | 高 |
| [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | 主要能力：金融研究與交易分析、AI Agent 建構與編排、研究、學習與教學。依專案描述：FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and dat… | 資料、機器學習與分析、AI Agent 與 Agent Skills、開發與程式碼工具、設計、UI 與前端、知識、研究與記憶 | 原生編譯／Release | 2/5（有限） | 活躍 | 高 |
| [microsoft/qlib](https://github.com/microsoft/qlib) | 主要能力：金融研究與交易分析、研究、學習與教學、資料分析、視覺化與預測。依專案描述：Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML m… | 資料、機器學習與分析、知識、研究與記憶、學習與教學、金融研究與交易分析、研究、學習與教學 | Python 環境 | 2/5（有限） | 活躍 | 高 |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 主要能力：金融研究與交易分析、AI Agent 建構與編排、研究、學習與教學。依專案描述：TradingAgents: Multi-Agents LLM Financial Trading Framework | AI Agent 與 Agent Skills、知識、研究與記憶、Web、桌面與平台、金融研究與交易分析、AI Agent 建構與編排 | Python 環境 | 2/5（有限） | 活躍 | 高 |

<a id="category-developer-tools"></a>
## 開發與程式碼工具

| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |
|---|---|---|---|---:|---|---|
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 主要能力：一般工具／待確認。依專案描述：aider is AI pair programming in your terminal | 一般工具／待確認 | Python 環境 | 3/5（中等） | 活躍 | 中 |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 主要能力：程式開發、理解與審查。依專案描述：🙌 OpenHands: AI-Driven Development | AI Agent 與 Agent Skills、程式開發、理解與審查 | Node.js／TypeScript | 4/5（高） | 活躍 | 中 |

## 欄位與判讀方式

- `categories` / `capabilities`：可多選，每一項附 confidence 與命中的 metadata evidence。
- `installation`：只提供可能路徑，不猜測精確套件名稱或安裝命令。
- `chatgpt_assistance`：1–5 分，表示 ChatGPT 對理解、安裝規劃、設定、程式與除錯的可協助程度；不代表工具品質。
- `maintenance`：以 archived、disabled 與距離最近 push 的天數判定。
- `risks`：涵蓋授權不明、維護、資料蒐集、個資、金融、安全、外部服務與運算資源等提示。
- `search_text` 與 `indexes`：提供全文關鍵字及 category/capability/language/maintenance/risk/tag 反向索引。

可選的 LLM 深度補強方案見 [`docs/OPTIONAL_LLM_ENRICHMENT.md`](docs/OPTIONAL_LLM_ENRICHMENT.md)；它不影響基礎版產生流程。
