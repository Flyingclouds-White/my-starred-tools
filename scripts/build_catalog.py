#!/usr/bin/env python3
"""Build a deterministic, LLM-free catalog from GitHub starred metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "1.0"
CLASSIFIER_VERSION = "metadata-rules-v1"

# Rules intentionally use only fields already returned by the GitHub API. A repository
# can match more than one category/capability. Earlier rules win score ties.
CATEGORY_RULES = [
    ("ai-agents", "AI Agent 與 Agent Skills", ["ai-agent", "ai-agents", "agentic", "agent skill", "agent-skill", "agent-skills", "claude-code", "codex", "llm", "mcp", "skill"]),
    ("developer-tools", "開發與程式碼工具", ["developer-tools", "codebase", "code-analysis", "code-review", "coding", "programming", "cli", "terminal", "ide", "ast", "tree-sitter", "sdlc"]),
    ("automation-integration", "自動化與整合", ["automation", "workflow", "integration", "integrations", "api", "browser-automation", "browser-use", "webhook", "oauth", "n8n", "scraper", "crawler"]),
    ("design-ui", "設計、UI 與前端", ["design", "ui-design", "ux", "frontend", "landing-page", "figma", "design-system", "prototype", "prototyping", "tailwindcss", "visual-programming"]),
    ("image-creative", "影像與創意生成", ["image-generation", "image-editing", "text-to-image", "image-to-image", "illustration", "photography", "photo", "gpt-image", "visual-ai", "generative-art"]),
    ("video-media", "影片與媒體製作", ["video", "video-generation", "video-editing", "ffmpeg", "capcut", "youtube", "shorts", "subtitles", "film", "render video", "mp4"]),
    ("audio-speech", "語音、音訊與轉錄", ["audio", "voice", "speech", "tts", "text-to-speech", "speech-to-text", "whisper", "transcription", "dubbing", "podcast"]),
    ("presentation-docs", "簡報與文件", ["presentation", "powerpoint", "ppt", "pptx", "slides", "document", "pdf", "office"]),
    ("knowledge-research", "知識、研究與記憶", ["knowledge", "research", "academic", "rag", "memory", "wiki", "knowledge-graph", "notebooklm", "documentation", "document", "pdf", "obsidian"]),
    ("data-ai", "資料、機器學習與分析", ["data", "analytics", "machine-learning", "deep-learning", "forecasting", "dataset", "visualization", "graph", "timeseries", "time-series"]),
    ("productivity", "生產力與工作管理", ["productivity", "task-manager", "tasks", "notes", "career", "resume", "job-search", "email", "calendar", "workspace", "clipboard"]),
    ("web-platform", "Web、桌面與平台", ["web", "nextjs", "react", "html", "cloudflare", "self-hosted", "desktop-app", "webui", "browser", "tauri"]),
    ("finance", "金融與交易", ["finance", "financial", "trading", "investment", "stock-market", "quant", "fintech", "market"]),
    ("security-privacy", "資安、隱私與稽核", ["security", "privacy", "audit", "network", "osint", "packet", "recon", "copyright", "accessibility"]),
    ("education", "學習與教學", ["course", "tutorial", "beginner", "education", "educational", "learning", "study", "lessons", "flashcards"]),
    ("social-content", "社群、行銷與內容", ["social-media", "content-creation", "marketing", "twitter", "instagram", "facebook", "threads", "creator-tools", "viral-content"]),
    ("simulation-robotics", "模擬、3D 與機器人", ["simulation", "robotics", "physics", "3d", "webgl", "webgpu", "embodied-ai", "collision"]),
    ("culture-divination", "文化、命理與宗教", ["astrology", "divination", "fortune-telling", "tarot", "buddhism", "bazi", "ziwei", "紫微", "八字", "塔罗", "命理"]),
    ("reference-collection", "資源清單與參考素材", ["awesome", "awesome-list", "collection", "catalog", "prompt-library", "prompt-collection", "templates", "cookbooks", "reference"]),
    ("home-iot", "家庭、自動化與 IoT", ["home-assistant", "home-automation", "camera", "nvr", "mqtt", "rtsp", "object-detection"]),
]

CAPABILITY_RULES = [
    ("agent-skill", "Agent Skill／提示工作流", ["agent skill", "agent-skill", "agent-skills", "claude-code-skill", "codex-skill", "skills"], ["安裝或調整 Agent Skill", "建立可重用的 AI 工作流程"]),
    ("agent-orchestration", "AI Agent 建構與編排", ["ai-agent", "ai-agents", "agentic", "multiagent", "multi-agent", "orchestration", "agent framework", "langgraph", "crewai"], ["建立或編排 AI Agent", "設計多步驟代理流程"]),
    ("mcp-integration", "MCP／工具整合", ["mcp", "mcp-server", "model-context-protocol"], ["把外部工具接入 AI 助手", "設定 MCP client/server"]),
    ("code-quality", "程式開發、理解與審查", ["codebase", "code-analysis", "code-review", "coding", "developer-tools", "ast", "tree-sitter", "refactoring", "static-analysis"], ["理解或檢查程式碼庫", "改善程式品質與文件"]),
    ("workflow-automation", "工作流程自動化", ["automation", "workflow", "n8n", "task-manager", "webhook", "integration", "integrations"], ["串接服務與自動化重複工作", "規劃可重跑的工作流程"]),
    ("browser-data-collection", "瀏覽器操作與資料蒐集", ["browser-automation", "browser-use", "scraper", "crawler", "web-scraping", "osint", "social-media-crawler"], ["蒐集公開網頁資料", "自動化瀏覽器操作"]),
    ("design-prototyping", "設計系統與原型製作", ["design", "ui-design", "ux", "figma", "prototype", "prototyping", "landing-page", "frontend"], ["設計 UI 或視覺系統", "製作網站與產品原型"]),
    ("image-generation", "圖片生成、編輯與參考", ["image-generation", "image-editing", "text-to-image", "image-to-image", "illustration", "gpt-image", "photography", "photo"], ["產生或編修圖片", "建立視覺提示與參考素材"]),
    ("video-production", "影片生成、剪輯與轉檔", ["video", "video-generation", "video-editing", "ffmpeg", "capcut", "subtitles", "mp4", "film"], ["產生、剪輯或轉檔影片", "建立字幕與短影音流程"]),
    ("audio-speech", "語音生成、辨識與轉錄", ["audio", "voice", "speech", "tts", "text-to-speech", "speech-to-text", "whisper", "transcription", "dubbing"], ["進行語音合成或辨識", "轉錄、翻譯或配音"]),
    ("presentation-docs", "簡報與文件生成", ["presentation", "powerpoint", "ppt", "pptx", "slides", "document", "pdf", "office"], ["產生簡報、報告或文件", "把內容轉成可發佈格式"]),
    ("knowledge-memory", "知識庫、RAG 與記憶", ["knowledge", "rag", "memory", "wiki", "knowledge-graph", "obsidian", "notebooklm", "vector-search"], ["建立可搜尋知識庫", "整理研究資料與長期記憶"]),
    ("research-learning", "研究、學習與教學", ["research", "academic", "course", "tutorial", "learning", "study", "education", "lessons"], ["進行研究或文獻整理", "建立教學與學習材料"]),
    ("data-analysis", "資料分析、視覺化與預測", ["analytics", "data-visualization", "visualization", "forecasting", "time-series", "timeseries", "machine-learning", "dataset"], ["分析或視覺化資料", "建立預測與研究流程"]),
    ("monitoring-observability", "監控、可觀測性與情報", ["monitoring", "observability", "logs", "metrics", "tracing", "news", "radar", "dashboard"], ["監控系統或資訊來源", "彙整事件與趨勢"]),
    ("content-publishing", "內容企劃與社群發布", ["content-creation", "social-media", "marketing", "twitter", "instagram", "facebook", "youtube", "viral-content"], ["規劃與製作內容", "建立社群發布流程"]),
    ("finance-trading", "金融研究與交易分析", ["finance", "financial", "trading", "investment", "stock-market", "quant", "fintech"], ["研究金融市場與策略", "建立投資分析原型"]),
    ("security-audit", "安全檢查與調查", ["security", "audit", "network", "packet", "recon", "osint", "copyright", "accessibility"], ["執行授權範圍內的安全檢查", "進行稽核與調查"]),
    ("self-hosted-app", "本機或自架應用", ["self-hosted", "local-first", "desktop-app", "webui", "private-cloud", "own-your-data"], ["部署本機或自架服務", "評估資料自主方案"]),
    ("simulation-3d", "模擬、3D 與互動視覺", ["simulation", "robotics", "physics", "3d", "webgl", "webgpu", "generative-art"], ["建立模擬或 3D 體驗", "製作互動式視覺內容"]),
    ("reference-resource", "範例、模板與資源索引", ["awesome", "collection", "catalog", "templates", "cookbooks", "prompt-library", "prompt-collection", "reference"], ["查找範例、模板與工具", "比較不同實作方式"]),
    ("culture-divination", "文化、宗教與命理內容", ["astrology", "divination", "fortune-telling", "tarot", "buddhism", "bazi", "ziwei", "紫微", "八字", "塔罗", "命理"], ["整理文化或命理知識", "建立娛樂性分析流程"]),
]

ASSISTANCE_HELP = {
    "agent-skill": "閱讀 Skill 說明、安裝、客製提示與測試",
    "agent-orchestration": "設計 Agent 架構、工具介面與評估案例",
    "mcp-integration": "產生設定範例並排查 MCP 連線",
    "code-quality": "解讀程式碼、規劃修改、測試與文件",
    "workflow-automation": "拆解流程、撰寫自動化設定與除錯",
    "browser-data-collection": "設計合規的蒐集流程與資料清理",
    "design-prototyping": "產生設計規格、元件與原型程式碼",
    "image-generation": "撰寫提示、批次規格與品質檢查表",
    "video-production": "規劃腳本、剪輯與轉檔自動化",
    "audio-speech": "規劃轉錄、TTS、翻譯與音訊處理",
    "presentation-docs": "建立內容大綱、版面與輸出流程",
    "knowledge-memory": "設計資料模型、索引、RAG 與檢索流程",
    "research-learning": "整理資料、設計課程與驗證來源",
    "data-analysis": "清理資料、撰寫分析程式與解讀結果",
    "monitoring-observability": "設計監控、查詢、告警與摘要",
    "content-publishing": "規劃內容、改寫文案與建立排程",
    "finance-trading": "協助資料分析與回測程式，不替代財務建議",
    "security-audit": "在授權範圍內規劃檢查、修復與報告",
    "self-hosted-app": "解讀部署需求、產生設定與排錯步驟",
    "simulation-3d": "協助模型、演算法、場景與效能調整",
    "reference-resource": "搜尋、比較並整理適合的範例",
    "culture-divination": "整理規則與內容；結果僅供文化或娛樂用途",
    "general-resource": "閱讀 README、摘要功能並規劃試用",
}

RISK_ORDER = {"none": 0, "info": 1, "low": 2, "medium": 3, "high": 4, "critical": 5}
RISK_LABELS = {"none": "無明顯提示", "info": "資訊", "low": "低", "medium": "中", "high": "高", "critical": "嚴重"}


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def normalize_generated_at(value: str | None) -> datetime:
    if value:
        parsed = parse_datetime(value)
        if not parsed:
            raise ValueError("--generated-at must be an ISO-8601 timestamp")
        return parsed.astimezone(timezone.utc)
    return datetime.now(timezone.utc)


def metadata_text(repo: dict[str, Any]) -> tuple[str, set[str]]:
    parts = [repo.get("name") or "", repo.get("full_name") or "", repo.get("description") or "", repo.get("language") or ""]
    parts.extend(repo.get("topics") or [])
    haystack = " ".join(str(part).lower() for part in parts)
    tokens = set(re.findall(r"[a-z0-9+#.-]+", haystack))
    return haystack, tokens


def keyword_matches(keyword: str, haystack: str, tokens: set[str]) -> bool:
    keyword = keyword.lower()
    if re.fullmatch(r"[a-z0-9+#.-]{1,3}", keyword):
        return keyword in tokens
    return keyword in haystack


def match_rules(repo: dict[str, Any], rules: list[tuple[str, str, list[str], *tuple[Any, ...]]]) -> list[dict[str, Any]]:
    haystack, tokens = metadata_text(repo)
    matches: list[dict[str, Any]] = []
    for rule in rules:
        rule_id, label, keywords = rule[:3]
        evidence = [keyword for keyword in keywords if keyword_matches(keyword, haystack, tokens)]
        if evidence:
            score = len(evidence)
            matches.append({
                "id": rule_id,
                "label": label,
                "confidence": "high" if score >= 3 else "medium" if score == 2 else "low",
                "score": score,
                "evidence": evidence[:6],
            })
    matches.sort(key=lambda item: (-item["score"], next(i for i, rule in enumerate(rules) if rule[0] == item["id"])))
    return matches


def infer_installation(repo: dict[str, Any], capabilities: list[dict[str, Any]]) -> dict[str, Any]:
    haystack, _ = metadata_text(repo)
    capability_ids = {item["id"] for item in capabilities}
    methods: list[dict[str, str]] = []

    def add(kind: str, label: str, guidance: str) -> None:
        if not any(item["kind"] == kind for item in methods):
            methods.append({"kind": kind, "label": label, "guidance": guidance})

    if "reference-resource" in capability_ids or any(term in haystack for term in ("course", "cookbook", "guide", "prompt library")):
        add("reference", "直接閱讀／複製範例", "這較像資源、課程或範例集合；通常不需要完整安裝。")
    if "agent-skill" in capability_ids:
        add("agent-skill", "Agent Skill 安裝", "依 README 將 Skill 或 plugin 放入目標 AI 工具指定目錄；先核對相容產品與權限。")
    if "mcp-integration" in capability_ids:
        add("mcp", "MCP server 設定", "依 README 安裝 server，並把啟動方式與必要環境變數加入 MCP client 設定。")
    if any(term in haystack for term in ("docker", "self-hosted", "private-cloud")):
        add("container", "容器／自架部署", "優先檢查 README 是否提供 Docker Compose、映像檔與持久化資料說明。")

    language = (repo.get("language") or "").lower()
    language_methods = {
        "python": ("python", "Python 環境", "檢查 pyproject.toml、requirements.txt 或 README；建議使用隔離的虛擬環境。"),
        "javascript": ("node", "Node.js／JavaScript", "檢查 package.json 與鎖定檔，再依 README 選用 npm、pnpm、yarn 或 bun。"),
        "typescript": ("node", "Node.js／TypeScript", "檢查 package.json 與鎖定檔，再依 README 選用 npm、pnpm、yarn 或 bun。"),
        "html": ("web", "靜態網頁／Web 專案", "若為靜態檔可直接預覽；若有 package.json，依 README 啟動建置工具。"),
        "shell": ("shell", "Shell 腳本／設定檔", "先閱讀腳本與權限需求，再於相容 shell 中執行或複製設定。"),
        "go": ("go", "Go 專案", "檢查 go.mod、release binary 與 README 的建置或安裝方式。"),
        "rust": ("rust", "Rust 專案", "檢查 Cargo.toml、release binary 與 README 的 Cargo 安裝方式。"),
        "c": ("native", "原生編譯／Release", "優先使用官方 release；自行編譯前檢查平台、編譯器與系統依賴。"),
        "c++": ("native", "原生編譯／Release", "優先使用官方 release；自行編譯前檢查平台、編譯器與系統依賴。"),
        "haskell": ("haskell", "Haskell 專案", "檢查 Cabal/Stack 設定、系統套件與 README 的建置方式。"),
        "php": ("php", "PHP／WordPress", "檢查是否為 Composer 套件或 WordPress plugin，並依 README 安裝到正確環境。"),
        "jupyter notebook": ("notebook", "Jupyter Notebook", "建立隔離的 Python/Jupyter 環境，依 notebook 或 README 安裝相依套件。"),
        "markdown": ("reference", "文件／Skill 素材", "通常可直接閱讀或複製到相容工具；依 README 確認目錄位置。"),
    }
    if language in language_methods:
        add(*language_methods[language])
    if not methods:
        add("readme", "依 README 判斷", "metadata 不足以可靠推定安裝方式；先檢查 README、Releases 與相依需求。")

    return {
        "confidence": "estimated",
        "methods": methods,
        "note": "僅依 GitHub metadata 推定，未讀取各 repository 的安裝文件；執行前必須核對 README 與 Releases。",
    }


def maintenance_status(repo: dict[str, Any], generated_at: datetime) -> dict[str, Any]:
    if repo.get("disabled"):
        return {"status": "disabled", "label": "已停用", "days_since_push": None, "reason": "GitHub 標示為 disabled。"}
    if repo.get("archived"):
        return {"status": "archived", "label": "已封存", "days_since_push": None, "reason": "GitHub 標示為 archived，通常不再接受功能更新。"}
    pushed_at = parse_datetime(repo.get("pushed_at"))
    if not pushed_at:
        return {"status": "unknown", "label": "未知", "days_since_push": None, "reason": "metadata 沒有可解析的 pushed_at。"}
    days = max(0, (generated_at - pushed_at.astimezone(timezone.utc)).days)
    if days <= 180:
        status, label = "active", "活躍"
    elif days <= 365:
        status, label = "maintained", "近期維護"
    elif days <= 730:
        status, label = "stale", "較久未更新"
    else:
        status, label = "dormant", "長期未更新"
    return {"status": status, "label": label, "days_since_push": days, "reason": f"距離最近 push 約 {days} 天。"}


def infer_risks(repo: dict[str, Any], maintenance: dict[str, Any]) -> dict[str, Any]:
    haystack, _ = metadata_text(repo)
    risks: list[dict[str, str]] = []

    def add(code: str, level: str, message: str) -> None:
        if not any(item["code"] == code for item in risks):
            risks.append({"code": code, "level": level, "label": RISK_LABELS[level], "message": message})

    if maintenance["status"] in {"disabled", "archived"}:
        add("unmaintained", "high", "專案已停用或封存；安全修補、相容性與支援可能中止。")
    elif maintenance["status"] in {"stale", "dormant"}:
        add("stale", "medium", "專案較久未 push；採用前應檢查 issues、相依套件與替代方案。")
    elif maintenance["status"] == "unknown":
        add("maintenance-unknown", "low", "無法由 metadata 判斷最近維護狀態。")
    if not repo.get("license") or str(repo.get("license")).upper() == "NOASSERTION":
        add("license-unknown", "medium", "GitHub metadata 未提供明確授權；使用、修改或商用前需核對 LICENSE。")
    if not (repo.get("description") or "").strip():
        add("metadata-sparse", "low", "描述不足，分類與能力摘要的可信度較低，需直接閱讀 README。")
    if any(term in haystack for term in ("scraper", "crawler", "web-scraping", "media crawler", "download")):
        add("collection-compliance", "high", "資料蒐集或下載可能受網站條款、著作權、robots 規則與地方法律限制。")
    if any(term in haystack for term in ("finance", "financial", "trading", "investment", "stock-market", "quant")):
        add("financial-use", "high", "金融輸出可能失準或過時；不可視為投資建議，需獨立驗證與風險控管。")
    if any(term in haystack for term in ("security", "packet", "network", "recon", "osint", "audit")):
        add("authorized-use", "high", "安全與調查功能只能用於自有或明確授權的系統與資料。")
    if any(term in haystack for term in ("voice-cloning", "voice cloning", "face", "portrait", "personal data", "email", "camera", "clipboard", "memory vault")):
        add("sensitive-data", "high", "可能接觸聲音、影像、信件或個人資料；需取得同意並保護憑證與輸出。")
    if any(term in haystack for term in ("openai", "anthropic", "claude", "elevenlabs", "google cloud", "cloudflare", "api")):
        add("external-service", "medium", "部分功能可能需要第三方帳號、API key、付費額度或受服務條款限制。")
    if any(term in haystack for term in ("cuda", "gpu", "deep-learning", "machine-learning", "video-generation", "voice-cloning", "simulation")):
        add("compute", "medium", "本機執行可能需要較多 GPU、記憶體、儲存空間或平台相依套件。")
    if any(term in haystack for term in ("ai", "llm", "agent", "machine-learning", "gpt", "claude")):
        add("ai-accuracy", "info", "AI 產出可能有幻覺、偏誤或不可重現結果，重要內容需人工驗證。")
    if any(term in haystack for term in ("astrology", "divination", "fortune-telling", "tarot", "bazi", "ziwei", "命理", "塔罗")):
        add("entertainment-only", "info", "命理或占卜輸出僅適合作為文化與娛樂內容，不宜據此做重大決定。")

    risks.sort(key=lambda item: (-RISK_ORDER[item["level"]], item["code"]))
    highest = risks[0]["level"] if risks else "none"
    return {"highest_level": highest, "highest_label": RISK_LABELS[highest], "items": risks}


def infer_assistance(capabilities: list[dict[str, Any]], risks: dict[str, Any]) -> dict[str, Any]:
    capability_ids = [item["id"] for item in capabilities]
    score = 3
    if any(item in capability_ids for item in ("agent-skill", "code-quality", "workflow-automation", "presentation-docs", "reference-resource")):
        score += 1
    if any(item["code"] in {"financial-use", "authorized-use", "sensitive-data"} for item in risks["items"]):
        score -= 1
    score = max(1, min(5, score))
    labels = {1: "很有限", 2: "有限", 3: "中等", 4: "高", 5: "很高"}
    can_help = []
    for capability_id in capability_ids[:5] or ["general-resource"]:
        help_text = ASSISTANCE_HELP.get(capability_id, ASSISTANCE_HELP["general-resource"])
        if help_text not in can_help:
            can_help.append(help_text)
    limitations = ["ChatGPT 未自動讀取該 repository 的 README、程式碼或最新 issues。"]
    if risks["highest_level"] in {"high", "critical"}:
        limitations.append("高風險用途仍需人工授權、專業判斷或獨立驗證。")
    return {"score": score, "max_score": 5, "level": labels[score], "can_help_with": can_help, "limitations": limitations}


def slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return result or "unknown"


def compact_text(value: str | None, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", (value or "").strip())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def build_entry(repo: dict[str, Any], generated_at: datetime) -> dict[str, Any]:
    categories = match_rules(repo, CATEGORY_RULES)
    if not categories:
        categories = [{"id": "uncategorized", "label": "待分類", "confidence": "low", "score": 0, "evidence": []}]
    capabilities = match_rules(repo, CAPABILITY_RULES)
    if not capabilities:
        capabilities = [{"id": "general-resource", "label": "一般工具／待確認", "confidence": "low", "score": 0, "evidence": []}]

    # AI/agent, developer, automation and platform labels are useful cross-cutting tags,
    # but a concrete domain (video, finance, research, etc.) makes a better browse section.
    generic_category_ids = {"ai-agents", "developer-tools", "automation-integration", "web-platform"}
    specific_categories = [item for item in categories if item["id"] not in generic_category_ids]
    primary_source = specific_categories[0] if specific_categories else categories[0]
    primary = {key: value for key, value in primary_source.items() if key != "score"}
    for item in categories:
        item.pop("score", None)
    for item in capabilities:
        item.pop("score", None)

    maintenance = maintenance_status(repo, generated_at)
    risks = infer_risks(repo, maintenance)
    installation = infer_installation(repo, capabilities)
    assistance = infer_assistance(capabilities, risks)
    capability_labels = [item["label"] for item in capabilities[:3]]
    description = compact_text(repo.get("description"))
    capability_summary = "主要能力：" + "、".join(capability_labels) + "。"
    if description:
        capability_summary += "依專案描述：" + description
    else:
        capability_summary += "metadata 描述不足，需閱讀 README 進一步確認。"

    suitable_for: list[str] = []
    capability_use_cases = {rule[0]: rule[3] for rule in CAPABILITY_RULES}
    for capability in capabilities:
        for use_case in capability_use_cases.get(capability["id"], ["進一步閱讀 README 以確認用途"]):
            if use_case not in suitable_for:
                suitable_for.append(use_case)
    suitable_for = suitable_for[:6]

    topics = sorted(set(repo.get("topics") or []), key=str.casefold)
    tags = [f"category:{item['id']}" for item in categories]
    tags += [f"capability:{item['id']}" for item in capabilities]
    if repo.get("language"):
        tags.append(f"language:{slug(str(repo['language']))}")
    tags += [f"topic:{topic}" for topic in topics]
    tags.append(f"maintenance:{maintenance['status']}")
    tags.append(f"risk:{risks['highest_level']}")
    tags = sorted(set(tags), key=str.casefold)

    searchable = [
        repo.get("full_name") or "", repo.get("description") or "", repo.get("language") or "",
        " ".join(topics), " ".join(item["label"] for item in categories),
        " ".join(item["label"] for item in capabilities), " ".join(suitable_for), " ".join(tags),
    ]
    return {
        "full_name": repo.get("full_name"),
        "name": repo.get("name"),
        "url": repo.get("html_url"),
        "homepage": repo.get("homepage"),
        "description": repo.get("description"),
        "language": repo.get("language"),
        "topics": topics,
        "stars": repo.get("stars"),
        "forks": repo.get("forks"),
        "license": repo.get("license"),
        "default_branch": repo.get("default_branch"),
        "starred_at": repo.get("starred_at"),
        "updated_at": repo.get("updated_at"),
        "pushed_at": repo.get("pushed_at"),
        "archived": bool(repo.get("archived")),
        "disabled": bool(repo.get("disabled")),
        "primary_category": primary,
        "categories": categories,
        "capabilities": capabilities,
        "capability_summary": capability_summary,
        "suitable_for": suitable_for,
        "installation": installation,
        "chatgpt_assistance": assistance,
        "maintenance": maintenance,
        "risks": risks,
        "tags": tags,
        "search_text": " ".join(str(part) for part in searchable if part).casefold(),
    }


def add_to_index(index: dict[str, list[str]], key: str, full_name: str) -> None:
    index.setdefault(key, []).append(full_name)


def sorted_mapping(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items(), key=lambda item: (-item[1], item[0].casefold())))


def build_catalog(repos: list[dict[str, Any]], generated_at: datetime) -> dict[str, Any]:
    if not isinstance(repos, list):
        raise ValueError("Input JSON must contain an array of repositories")
    names = [repo.get("full_name") for repo in repos]
    if any(not name for name in names):
        raise ValueError("Every repository must have a non-empty full_name")
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    if duplicates:
        raise ValueError("Duplicate full_name values: " + ", ".join(duplicates))

    entries = [build_entry(repo, generated_at) for repo in repos]
    entries.sort(key=lambda item: (item["primary_category"]["id"], item["full_name"].casefold()))

    indexes: dict[str, dict[str, list[str]]] = {
        "by_category": {}, "by_capability": {}, "by_language": {}, "by_maintenance": {},
        "by_chatgpt_assistance": {}, "by_risk_level": {}, "by_tag": {},
    }
    counters = {key: Counter() for key in indexes}
    for entry in entries:
        full_name = entry["full_name"]
        for category in entry["categories"]:
            add_to_index(indexes["by_category"], category["id"], full_name)
            counters["by_category"][category["id"]] += 1
        for capability in entry["capabilities"]:
            add_to_index(indexes["by_capability"], capability["id"], full_name)
            counters["by_capability"][capability["id"]] += 1
        language = entry["language"] or "Unknown"
        add_to_index(indexes["by_language"], language, full_name)
        counters["by_language"][language] += 1
        add_to_index(indexes["by_maintenance"], entry["maintenance"]["status"], full_name)
        counters["by_maintenance"][entry["maintenance"]["status"]] += 1
        assistance_key = str(entry["chatgpt_assistance"]["score"])
        add_to_index(indexes["by_chatgpt_assistance"], assistance_key, full_name)
        counters["by_chatgpt_assistance"][assistance_key] += 1
        risk_key = entry["risks"]["highest_level"]
        add_to_index(indexes["by_risk_level"], risk_key, full_name)
        counters["by_risk_level"][risk_key] += 1
        for tag in entry["tags"]:
            add_to_index(indexes["by_tag"], tag, full_name)
            counters["by_tag"][tag] += 1

    for index in indexes.values():
        for key in list(index):
            index[key] = sorted(index[key], key=str.casefold)
        ordered = dict(sorted(index.items(), key=lambda item: item[0].casefold()))
        index.clear()
        index.update(ordered)

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at.isoformat().replace("+00:00", "Z"),
        "source": {
            "file": "data/starred-repositories.json",
            "repository_count": len(entries),
            "classifier": CLASSIFIER_VERSION,
            "llm_used": False,
            "basis": ["name", "description", "topics", "language", "license", "archived", "disabled", "pushed_at"],
            "limitations": [
                "Categories, capabilities, installation options and risks are heuristic metadata inferences.",
                "The builder does not read repository README files, releases, issues or source code.",
                "Verify the upstream README, license, security posture and current maintenance before adoption.",
            ],
        },
        "stats": {
            "categories": sorted_mapping(counters["by_category"]),
            "capabilities": sorted_mapping(counters["by_capability"]),
            "languages": sorted_mapping(counters["by_language"]),
            "maintenance": sorted_mapping(counters["by_maintenance"]),
            "chatgpt_assistance_scores": sorted_mapping(counters["by_chatgpt_assistance"]),
            "highest_risk_levels": sorted_mapping(counters["by_risk_level"]),
        },
        "indexes": indexes,
        "repositories": entries,
    }


def markdown_escape(value: Any) -> str:
    return compact_text(str(value or "")).replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")


def render_markdown(catalog: dict[str, Any]) -> str:
    entries = catalog["repositories"]
    category_labels = {item[0]: item[1] for item in CATEGORY_RULES}
    category_labels["uncategorized"] = "待分類"
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        grouped[entry["primary_category"]["id"]].append(entry)

    lines = [
        "# ChatGPT 可理解的個人工具庫",
        "",
        "這份目錄由 GitHub Stars 的公開 metadata 自動產生，**基礎版不使用 LLM，也不需要付費 API**。",
        "",
        f"- Repository 數：**{catalog['source']['repository_count']}**",
        f"- 產生時間（UTC）：`{catalog['generated_at']}`",
        f"- 分類器：`{catalog['source']['classifier']}`",
        "- 判斷依據：name、description、topics、language、license、archived/disabled 與 pushed_at",
        "",
        "> 分類、能力、安裝方式與風險皆是 metadata 推定。採用前請閱讀上游 README、LICENSE、Releases 與 issues。",
        "",
        "## 如何搜尋",
        "",
        "`data/catalog.json` 是給 ChatGPT、程式與 `jq` 使用的完整索引；本頁適合人工瀏覽。可以直接要求 ChatGPT：",
        "",
        "- 找出可做影片自動化、ChatGPT 協助程度至少 4/5、且仍活躍的工具。",
        "- 比較所有簡報工具的安裝路徑、授權與風險提示。",
        "- 從自架工具中挑出不需外部 API 的候選項目，再逐一讀 README 驗證。",
        "",
        "快速查詢範例：",
        "",
        "```sh",
        "jq -r '.indexes.by_capability[\"video-production\"][]' data/catalog.json",
        "jq -r '.repositories[] | select(.chatgpt_assistance.score >= 4 and .maintenance.status == \"active\") | .full_name' data/catalog.json",
        "jq -r '.repositories[] | select(.risks.highest_level == \"high\") | [.full_name, .risks.items[0].message] | @tsv' data/catalog.json",
        "```",
        "",
        "## 分類總覽",
        "",
        "| 主分類 | Repository 數 |",
        "|---|---:|",
    ]
    for category_id, category_entries in sorted(grouped.items(), key=lambda item: (-len(item[1]), category_labels.get(item[0], item[0]))):
        lines.append(f"| [{category_labels.get(category_id, category_id)}](#category-{category_id}) | {len(category_entries)} |")

    install_label = lambda entry: "、".join(method["label"] for method in entry["installation"]["methods"][:2])
    for category_id, category_entries in sorted(grouped.items(), key=lambda item: (category_labels.get(item[0], item[0]), item[0])):
        lines.extend([
            "",
            f'<a id="category-{category_id}"></a>',
            f"## {category_labels.get(category_id, category_id)}",
            "",
            "| Repository | 能力摘要 | 多標籤 | 安裝推定 | ChatGPT | 維護 | 最高風險 |",
            "|---|---|---|---|---:|---|---|",
        ])
        for entry in category_entries:
            extra_categories = [item["label"] for item in entry["categories"] if item["id"] != category_id]
            capability_labels = [item["label"] for item in entry["capabilities"][:3]]
            tags = extra_categories + capability_labels
            lines.append(
                "| "
                + f"[{markdown_escape(entry['full_name'])}]({entry['url']}) | "
                + f"{markdown_escape(entry['capability_summary'])} | "
                + f"{markdown_escape('、'.join(tags[:5]))} | "
                + f"{markdown_escape(install_label(entry))} | "
                + f"{entry['chatgpt_assistance']['score']}/5（{entry['chatgpt_assistance']['level']}） | "
                + f"{entry['maintenance']['label']} | "
                + f"{entry['risks']['highest_label']} |"
            )

    lines.extend([
        "",
        "## 欄位與判讀方式",
        "",
        "- `categories` / `capabilities`：可多選，每一項附 confidence 與命中的 metadata evidence。",
        "- `installation`：只提供可能路徑，不猜測精確套件名稱或安裝命令。",
        "- `chatgpt_assistance`：1–5 分，表示 ChatGPT 對理解、安裝規劃、設定、程式與除錯的可協助程度；不代表工具品質。",
        "- `maintenance`：以 archived、disabled 與距離最近 push 的天數判定。",
        "- `risks`：涵蓋授權不明、維護、資料蒐集、個資、金融、安全、外部服務與運算資源等提示。",
        "- `search_text` 與 `indexes`：提供全文關鍵字及 category/capability/language/maintenance/risk/tag 反向索引。",
        "",
        "可選的 LLM 深度補強方案見 [`docs/OPTIONAL_LLM_ENRICHMENT.md`](docs/OPTIONAL_LLM_ENRICHMENT.md)；它不影響基礎版產生流程。",
        "",
    ])
    return "\n".join(lines)


def validate_catalog(catalog: dict[str, Any]) -> None:
    entries = catalog.get("repositories") or []
    expected = catalog.get("source", {}).get("repository_count")
    if expected != len(entries):
        raise ValueError("Catalog repository_count does not match repositories array")
    names = {entry["full_name"] for entry in entries}
    if len(names) != len(entries):
        raise ValueError("Catalog contains duplicate repository names")
    for entry in entries:
        required = ("categories", "capabilities", "capability_summary", "suitable_for", "installation", "chatgpt_assistance", "maintenance", "risks", "tags", "search_text")
        missing = [key for key in required if key not in entry]
        if missing:
            raise ValueError(f"{entry['full_name']} is missing fields: {', '.join(missing)}")
    for index_name, index in catalog.get("indexes", {}).items():
        for key, indexed_names in index.items():
            unknown = set(indexed_names) - names
            if unknown:
                raise ValueError(f"{index_name}.{key} contains unknown repositories: {sorted(unknown)}")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="data/starred-repositories.json", help="Source metadata JSON")
    parser.add_argument("--json-output", default="data/catalog.json", help="Generated machine-readable catalog")
    parser.add_argument("--markdown-output", default="CATALOG.md", help="Generated human-readable catalog")
    parser.add_argument("--generated-at", help="Fixed ISO-8601 generation time (useful for tests)")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        generated_at = normalize_generated_at(args.generated_at)
        with Path(args.input).open("r", encoding="utf-8") as handle:
            repos = json.load(handle)
        catalog = build_catalog(repos, generated_at)
        validate_catalog(catalog)
        json_output = Path(args.json_output)
        markdown_output = Path(args.markdown_output)
        json_output.parent.mkdir(parents=True, exist_ok=True)
        markdown_output.parent.mkdir(parents=True, exist_ok=True)
        json_output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        markdown_output.write_text(render_markdown(catalog), encoding="utf-8")
        print(f"Built catalog for {len(catalog['repositories'])} repositories: {json_output}, {markdown_output}")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"catalog build failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
