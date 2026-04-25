import os
from dataclasses import dataclass
from typing import Dict, Any

import requests


@dataclass
class JiraConfig:
    base_url: str
    email: str
    api_token: str
    project_key: str
    issue_type: str = "Task"


@dataclass
class ConfluenceConfig:
    base_url: str
    email: str
    api_token: str
    space_key: str
    parent_page_id: str | None = None


@dataclass
class XrayConfig:
    base_url: str
    client_id: str
    client_secret: str


def _basic_auth_headers(email: str, token: str) -> Dict[str, str]:
    return {"Content-Type": "application/json"}


def get_jira_config() -> JiraConfig:
    return JiraConfig(
        base_url=os.getenv("JIRA_BASE_URL", ""),
        email=os.getenv("JIRA_EMAIL", ""),
        api_token=os.getenv("JIRA_API_TOKEN", ""),
        project_key=os.getenv("JIRA_PROJECT_KEY", ""),
        issue_type=os.getenv("JIRA_ISSUE_TYPE", "Task"),
    )


def get_confluence_config() -> ConfluenceConfig:
    return ConfluenceConfig(
        base_url=os.getenv("CONFLUENCE_BASE_URL", ""),
        email=os.getenv("CONFLUENCE_EMAIL", ""),
        api_token=os.getenv("CONFLUENCE_API_TOKEN", ""),
        space_key=os.getenv("CONFLUENCE_SPACE_KEY", ""),
        parent_page_id=os.getenv("CONFLUENCE_PARENT_PAGE_ID"),
    )


def get_xray_config() -> XrayConfig:
    return XrayConfig(
        base_url=os.getenv("XRAY_BASE_URL", ""),
        client_id=os.getenv("XRAY_CLIENT_ID", ""),
        client_secret=os.getenv("XRAY_CLIENT_SECRET", ""),
    )


def create_jira_issue(summary: str, description: str) -> Dict[str, Any]:
    cfg = get_jira_config()
    if not all([cfg.base_url, cfg.email, cfg.api_token, cfg.project_key]):
        return {"status": "skipped", "reason": "JIRA env vars are not fully configured."}

    endpoint = f"{cfg.base_url.rstrip('/')}/rest/api/3/issue"
    payload = {
        "fields": {
            "project": {"key": cfg.project_key},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": description}],
                    }
                ],
            },
            "issuetype": {"name": cfg.issue_type},
        }
    }
    res = requests.post(
        endpoint,
        json=payload,
        headers=_basic_auth_headers(cfg.email, cfg.api_token),
        auth=(cfg.email, cfg.api_token),
        timeout=30,
    )
    return {"status": res.status_code, "body": res.text}


def create_confluence_page(title: str, content_markdown: str) -> Dict[str, Any]:
    cfg = get_confluence_config()
    if not all([cfg.base_url, cfg.email, cfg.api_token, cfg.space_key]):
        return {"status": "skipped", "reason": "Confluence env vars are not fully configured."}

    endpoint = f"{cfg.base_url.rstrip('/')}/wiki/rest/api/content"
    payload: Dict[str, Any] = {
        "type": "page",
        "title": title,
        "space": {"key": cfg.space_key},
        "body": {
            "storage": {
                "value": f"<pre>{content_markdown}</pre>",
                "representation": "storage",
            }
        },
    }
    if cfg.parent_page_id:
        payload["ancestors"] = [{"id": cfg.parent_page_id}]

    res = requests.post(
        endpoint,
        json=payload,
        headers=_basic_auth_headers(cfg.email, cfg.api_token),
        auth=(cfg.email, cfg.api_token),
        timeout=30,
    )
    return {"status": res.status_code, "body": res.text}


def import_xray_test_execution(test_execution_payload: Dict[str, Any]) -> Dict[str, Any]:
    cfg = get_xray_config()
    if not all([cfg.base_url, cfg.client_id, cfg.client_secret]):
        return {"status": "skipped", "reason": "Xray env vars are not fully configured."}

    auth_endpoint = f"{cfg.base_url.rstrip('/')}/api/v2/authenticate"
    auth_res = requests.post(
        auth_endpoint,
        json={"client_id": cfg.client_id, "client_secret": cfg.client_secret},
        timeout=30,
    )
    if auth_res.status_code != 200:
        return {"status": auth_res.status_code, "body": auth_res.text}

    token = auth_res.text.strip('"')
    import_endpoint = f"{cfg.base_url.rstrip('/')}/api/v2/import/execution"
    res = requests.post(
        import_endpoint,
        json=test_execution_payload,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        timeout=30,
    )
    return {"status": res.status_code, "body": res.text}
