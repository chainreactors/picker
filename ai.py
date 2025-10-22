#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
AI integration module for article summarization
Supports OpenAI-compatible APIs including OpenAI, Claude, and local models
"""

from __future__ import annotations
import os
import re
import requests
from io import BytesIO
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

from markitdown import MarkItDown
from utils import Color


class ArticleProcessor:
    """Process articles: fetch content, convert to markdown, and generate summaries"""

    def __init__(self, ai_config: Dict[str, Any], proxy_url: str = '', fallback_proxy: str = '') -> None:
        """
        Initialize article processor

        Args:
            ai_config: AI configuration dictionary
            proxy_url: Optional proxy URL for requests
            fallback_proxy: Fallback proxy to try if primary method fails
        """
        self.enabled: bool = ai_config.get('enabled', False)
        self.proxy: Optional[Dict[str, str]] = (
            {'http': proxy_url, 'https': proxy_url} if proxy_url else None
        )
        self.fallback_proxy: Optional[Dict[str, str]] = (
            {'http': fallback_proxy, 'https': fallback_proxy} if fallback_proxy else None
        )
        self.md: Optional[MarkItDown] = MarkItDown() if self.enabled else None

        # AI configuration - support environment variables
        self.api_key = os.getenv(ai_config.get('secrets', 'OPENAI_API_KEY')) or ai_config.get('api_key', '')
        self.api_base = os.getenv('AI_API_BASE') or ai_config.get('api_base', 'https://api.openai.com/v1')
        self.model = os.getenv('AI_MODEL') or ai_config.get('model', 'kimi-k2-0905-preview')
        self.max_tokens = int(os.getenv('AI_MAX_TOKENS', ai_config.get('max_tokens', 2000)))
        self.temperature = float(os.getenv('AI_TEMPERATURE', ai_config.get('temperature', 0.7)))
        self.timeout = int(os.getenv('AI_TIMEOUT', ai_config.get('timeout', 60)))

        # Content limits
        self.max_content_length = int(os.getenv('AI_MAX_CONTENT_LENGTH', ai_config.get('max_content_length', 8000)))
        self.fetch_timeout = int(os.getenv('AI_FETCH_TIMEOUT', ai_config.get('fetch_timeout', 15)))

        # System prompt for summarization - support environment variable
        default_system_prompt = """你是一名专业的技术文档分析师，擅长从复杂的技术文章中提取核心内容。请阅读以下技术文章（或提供的文本），并生成一份简洁、结构化的总结，包含以下内容：

1. 文章主题：文章的核心主题或主要讨论的技术/问题是什么？
2. 关键点：列出文章中3-5个最重要的观点、方法、技术或结论。
3. 应用场景：文章提到的技术或方案的潜在应用领域或实际用途。
4. 局限性或挑战：文章中提到的技术限制、挑战或未来改进方向（如有）。
5. 总结评价：对文章内容的简短评价，例如其创新性、实用性或对技术领域的贡献。"""

        self.system_prompt = os.getenv('AI_SYSTEM_PROMPT') or ai_config.get('system_prompt', default_system_prompt)

        default_user_prompt = "请分析以下技术文章：\n\n标题：{title}\n\n内容：\n{content}"
        self.user_prompt_template = os.getenv('AI_USER_PROMPT') or ai_config.get('user_prompt_template', default_user_prompt)

    def fetch_article_content(self, url: str) -> Optional[str]:
        """Fetch article HTML content from URL with auto-retry (with/without proxy)"""
        if not self.enabled:
            return None

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        # Attempt 1: Try with configured proxy (if any)
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=self.fetch_timeout,
                verify=False,
                proxies=self.proxy
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            first_error = str(e)

            # Attempt 2: If primary method failed, try alternative
            if self.proxy:
                # Primary was with proxy, try without proxy
                Color.print_focus(f'[*] Fetch failed with proxy, retrying without proxy...')
                try:
                    response = requests.get(
                        url,
                        headers=headers,
                        timeout=self.fetch_timeout,
                        verify=False,
                        proxies=None
                    )
                    response.raise_for_status()
                    Color.print_success(f'[+] Succeeded without proxy')
                    return response.text
                except Exception as e2:
                    Color.print_failed(f'[-] Failed both with and without proxy')
                    Color.print_failed(f'    With proxy: {first_error}')
                    Color.print_failed(f'    Without proxy: {str(e2)}')
                    return None
            else:
                # Primary was without proxy, try with fallback proxy (if configured)
                if self.fallback_proxy:
                    Color.print_focus(f'[*] Fetch failed without proxy, retrying with fallback proxy...')
                    try:
                        response = requests.get(
                            url,
                            headers=headers,
                            timeout=self.fetch_timeout,
                            verify=False,
                            proxies=self.fallback_proxy
                        )
                        response.raise_for_status()
                        Color.print_success(f'[+] Succeeded with fallback proxy')
                        return response.text
                    except Exception as e2:
                        Color.print_failed(f'[-] Failed both without proxy and with fallback proxy')
                        Color.print_failed(f'    Without proxy: {first_error}')
                        Color.print_failed(f'    With fallback: {str(e2)}')
                        return None
                else:
                    Color.print_failed(f'[-] Failed to fetch content from {url}: {first_error}')
                    return None

    def html_to_markdown(self, html_content: str) -> Optional[str]:
        """Convert HTML content to Markdown using MarkItDown"""
        if not self.enabled or not html_content:
            return None

        try:
            # MarkItDown expects a file-like object in bytes mode
            html_bytes = html_content.encode('utf-8')
            html_stream = BytesIO(html_bytes)
            result = self.md.convert_stream(html_stream)
            markdown_text = result.text_content if hasattr(result, 'text_content') else str(result)

            # Truncate if too long
            if len(markdown_text) > self.max_content_length:
                markdown_text = markdown_text[:self.max_content_length] + "..."

            return markdown_text
        except Exception as e:
            Color.print_failed(f'[-] Failed to convert HTML to Markdown: {e}')
            return None

    def generate_summary(self, title: str, markdown_content: str) -> Optional[str]:
        """Generate article summary using AI"""
        if not self.enabled or not self.api_key or not markdown_content:
            return None

        try:
            user_prompt = self.user_prompt_template.format(
                title=title,
                content=markdown_content
            )

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}'
            }

            data = {
                'model': self.model,
                'messages': [
                    {'role': 'system', 'content': self.system_prompt},
                    {'role': 'user', 'content': user_prompt}
                ],
                'max_tokens': self.max_tokens,
                'temperature': self.temperature
            }

            response = requests.post(
                f'{self.api_base}/chat/completions',
                headers=headers,
                json=data,
                timeout=self.timeout,
                proxies=self.proxy
            )
            response.raise_for_status()

            result = response.json()
            summary = result['choices'][0]['message']['content'].strip()

            Color.print_success(f'[+] Generated summary for: {title[:50]}...')
            return summary

        except Exception as e:
            Color.print_failed(f'[-] Failed to generate summary: {e}')
            return None

    def generate_category(self, title: str, summary: str) -> str:
        """
        Generate category based on title and summary using AI

        Args:
            title: Article title
            summary: Article summary

        Returns:
            Category string (e.g., "Red Team", "Web Security", "AI Security", etc.)
        """
        try:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}'
            }

            category_prompt = f"""基于以下文章标题和摘要，选择一个最合适的技术分类。

标题：{title}

摘要：
{summary}

请从以下分类中选择一个最合适的（只返回分类名称，不要其他内容）：
- 红队技术 (Red Team)
- 蓝队防御 (Blue Team)
- Web安全 (Web Security)
- 二进制安全 (Binary Security)
- 移动安全 (Mobile Security)
- 云安全 (Cloud Security)
- AI安全 (AI Security)
- 漏洞分析 (Vulnerability Analysis)
- 逆向工程 (Reverse Engineering)
- 代码审计 (Code Audit)
- 安全工具 (Security Tools)
- 安全研究 (Security Research)
- 其他 (Others)

返回格式：只返回分类的英文名称（括号内的部分），例如："Red Team" 或 "Web Security"
"""

            data = {
                'model': self.model,
                'messages': [
                    {'role': 'user', 'content': category_prompt}
                ],
                'max_tokens': 50,
                'temperature': 0.3
            }

            response = requests.post(
                f'{self.api_base}/chat/completions',
                headers=headers,
                json=data,
                timeout=self.timeout,
                proxies=self.proxy
            )
            response.raise_for_status()

            result = response.json()
            category = result['choices'][0]['message']['content'].strip()

            # Clean up the response
            category = category.replace('"', '').replace("'", '').strip()

            Color.print_success(f'[+] Generated category: {category}')
            return category

        except Exception as e:
            Color.print_failed(f'[-] Failed to generate category: {e}')
            return 'Others'

    def process_article(self, title: str, url: str) -> Dict[str, Any]:
        """
        Complete workflow: fetch → convert → summarize → categorize
        Returns dict with url, optional summary, category, and markdown_content
        """
        result = {'url': url, 'summary': None, 'category': None, 'markdown_content': None}

        if not self.enabled:
            return result

        try:
            # Step 1: Fetch HTML content
            html_content = self.fetch_article_content(url)
            if not html_content:
                return result

            # Step 2: Convert to Markdown
            markdown_content = self.html_to_markdown(html_content)
            if not markdown_content:
                return result

            # Store markdown content
            result['markdown_content'] = markdown_content

            # Step 3: Generate summary
            summary = self.generate_summary(title, markdown_content)
            if summary:
                result['summary'] = summary

                # Step 4: Generate category based on summary
                category = self.generate_category(title, summary)
                result['category'] = category

        except Exception as e:
            Color.print_failed(f'[-] Error processing article {title}: {e}')

        return result


def process_articles_batch(
    processor: ArticleProcessor,
    articles: Dict[str, str]
) -> Dict[str, Dict[str, Any]]:
    """
    Process multiple articles (without threading for now)

    Args:
        processor: ArticleProcessor instance
        articles: Dict mapping article titles to URLs

    Returns:
        Dict mapping title to processed result with url, summary, markdown_content
    """
    results: Dict[str, Dict[str, Any]] = {}

    if not processor.enabled:
        # Return simple format if AI is disabled
        return {title: {'url': url, 'summary': None} for title, url in articles.items()}

    for title, url in articles.items():
        result = processor.process_article(title, url)
        results[title] = result

    return results


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing or replacing invalid characters
    """
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove control characters
    filename = re.sub(r'[\x00-\x1f\x7f]', '', filename)
    # Limit length
    if len(filename) > 200:
        filename = filename[:200]
    return filename.strip()


def extract_links_from_markdown(markdown_content: str) -> list[str]:
    """
    Extract all URLs from markdown content

    Args:
        markdown_content: Markdown text content

    Returns:
        List of unique URLs found in the content
    """
    # Pattern to match markdown links [text](url) and plain URLs
    md_link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    plain_url_pattern = r'https?://[^\s<>"\')]+[^\s<>"\').,;!?]'

    links = set()

    # Extract markdown links
    for match in re.finditer(md_link_pattern, markdown_content):
        url = match.group(2)
        if url.startswith('http'):
            links.add(url)

    # Extract plain URLs
    for match in re.finditer(plain_url_pattern, markdown_content):
        url = match.group(0)
        links.add(url)

    return sorted(list(links))


def save_article_markdown(
    title: str,
    url: str,
    source: str,
    date: str,
    markdown_content: str,
    summary: Optional[str] = None,
    category: Optional[str] = None,
    base_path: Path = None
) -> Optional[Path]:
    """
    Save article as markdown file with metadata
    If summary is provided, saves it in a separate {filename}_summary.md file with YAML frontmatter

    Args:
        title: Article title
        url: Article URL
        source: Feed source name
        date: Publication date (YYYY-MM-DD)
        markdown_content: Article content in markdown
        summary: Optional AI-generated summary (saved in separate file)
        category: Optional AI-generated category (included in summary metadata)
        base_path: Base path for saving (default: archive/{year}/{month}/{day}/summary/)

    Returns:
        Path to saved file, or None if failed
    """
    try:
        # Create directory structure - archive/{year}/{month}/{day}/daily/ and summary/
        root_path = Path(__file__).absolute().parent
        year, month, day = date.split('-')
        base_path = root_path.joinpath(f'archive/{year}/{month}/{day}')

        # Save article markdown to daily/ directory
        daily_dir = base_path.joinpath('daily')
        daily_dir.mkdir(parents=True, exist_ok=True)

        # Sanitize filename
        safe_source = sanitize_filename(source)
        safe_title = sanitize_filename(title)
        filename = f"{safe_source}_{safe_title}.md"
        filepath = daily_dir.joinpath(filename)

        # Prepare metadata (without summary)
        fetch_date = datetime.now().isoformat()
        metadata = f"""---
title: {title}
url: {url}
source: {source}
date: {date}
fetch_date: {fetch_date}
---

"""

        # Combine metadata and content
        full_content = metadata + f"# {title}\n\n" + markdown_content

        # Save main article file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)

        Color.print_success(f'[+] Saved article: {filename}')

        # Save summary in summary/ directory if provided
        if summary:
            summary_dir = base_path.joinpath('summary')
            summary_dir.mkdir(parents=True, exist_ok=True)

            summary_filename = f"{safe_source}_{safe_title}_summary.md"
            summary_filepath = summary_dir.joinpath(summary_filename)

            # Add YAML frontmatter with metadata and category
            summary_metadata = f"""---
title: {title}
url: {url}
source: {source}
date: {date}
fetch_date: {fetch_date}
category: {category if category else 'Others'}
---

"""
            full_summary = summary_metadata + f"# {title} - 摘要\n\n{summary}\n"

            # Extract and append reference links from markdown content
            links = extract_links_from_markdown(markdown_content)
            if links:
                full_summary += "\n## 参考链接\n\n"
                for i, link in enumerate(links, 1):
                    full_summary += f"{i}. {link}\n"

            with open(summary_filepath, 'w', encoding='utf-8') as f:
                f.write(full_summary)

            Color.print_success(f'[+] Saved summary: {summary_filename}')
            if links:
                Color.print_success(f'    [+] Extracted {len(links)} reference links')

        return filepath

    except Exception as e:
        Color.print_failed(f'[-] Failed to save article {title}: {e}')
        return None


def save_articles_batch(
    articles_data: Dict[str, Any],
    source: str,
    date: str,
    processor: Optional[ArticleProcessor] = None
) -> int:
    """
    Save multiple articles as markdown files

    Args:
        articles_data: Dict of {title: {url, summary, markdown_content}} or {title: url}
        source: Feed source name
        date: Publication date (YYYY-MM-DD)
        processor: Optional ArticleProcessor for fetching content if not available

    Returns:
        Number of successfully saved articles
    """
    saved_count: int = 0

    for title, data in articles_data.items():
        # Handle both dict and string formats
        if isinstance(data, dict):
            url = data.get('url', '')
            summary = data.get('summary')
            category = data.get('category')
            markdown_content = data.get('markdown_content')
        else:
            url = str(data)
            summary = None
            category = None
            markdown_content = None

        # Fetch and convert if markdown content not available
        if not markdown_content and processor:
            html = processor.fetch_article_content(url)
            if html:
                markdown_content = processor.html_to_markdown(html)

        if markdown_content:
            saved_path = save_article_markdown(
                title=title,
                url=url,
                source=source,
                date=date,
                markdown_content=markdown_content,
                summary=summary,
                category=category
            )
            if saved_path:
                saved_count += 1

    return saved_count
