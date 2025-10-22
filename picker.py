#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import argparse
import datetime
from urllib import parse
import listparser
import feedparser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml

from bot import *
from utils import *
from ai import ArticleProcessor, process_articles_batch, save_articles_batch, save_article_markdown

import requests
requests.packages.urllib3.disable_warnings()

today = datetime.datetime.now().strftime("%Y-%m-%d")
yesterday = str(datetime.date.today() + datetime.timedelta(-1))
root_path = Path(__file__).absolute().parent

# Category to GitHub Label mapping
CATEGORY_LABELS = {
    'Red Team': {'name': 'red-team', 'color': 'b60205', 'description': '红队技术 - Red Team techniques'},
    'Blue Team': {'name': 'blue-team', 'color': '0e8a16', 'description': '蓝队防御 - Blue Team defense'},
    'Web Security': {'name': 'web-security', 'color': '1d76db', 'description': 'Web安全 - Web Security'},
    'Binary Security': {'name': 'binary-security', 'color': '5319e7', 'description': '二进制安全 - Binary Security'},
    'Mobile Security': {'name': 'mobile-security', 'color': 'fbca04', 'description': '移动安全 - Mobile Security'},
    'Cloud Security': {'name': 'cloud-security', 'color': '0075ca', 'description': '云安全 - Cloud Security'},
    'AI Security': {'name': 'ai-security', 'color': 'd93f0b', 'description': 'AI安全 - AI Security'},
    'Vulnerability Analysis': {'name': 'vulnerability', 'color': 'c5def5', 'description': '漏洞分析 - Vulnerability Analysis'},
    'Reverse Engineering': {'name': 'reverse-engineering', 'color': 'e99695', 'description': '逆向工程 - Reverse Engineering'},
    'Code Audit': {'name': 'code-audit', 'color': 'bfd4f2', 'description': '代码审计 - Code Audit'},
    'Security Tools': {'name': 'security-tools', 'color': 'c2e0c6', 'description': '安全工具 - Security Tools'},
    'Security Research': {'name': 'security-research', 'color': 'fef2c0', 'description': '安全研究 - Security Research'},
    'Others': {'name': 'others', 'color': 'cccccc', 'description': '其他 - Others'}
}


def init_labels():
    """
    Initialize GitHub labels for article categories
    Creates labels if they don't exist, updates them if they do
    """
    Color.print_focus('[*] Initializing category labels...')

    created_count = 0
    updated_count = 0
    skipped_count = 0

    for category, label_info in CATEGORY_LABELS.items():
        label_name = label_info['name']
        label_color = label_info['color']
        label_desc = label_info['description']

        try:
            # Check if label exists
            result = popen(f'gh label list --json name,color,description')
            existing_labels = json.loads(result)

            label_exists = any(label['name'] == label_name for label in existing_labels)

            if label_exists:
                # Check if update is needed
                existing = next(label for label in existing_labels if label['name'] == label_name)
                if existing.get('color') != label_color or existing.get('description') != label_desc:
                    # Update label
                    popen(f'gh label edit "{label_name}" --color "{label_color}" --description "{label_desc}"')
                    Color.print_success(f'[+] Updated label: {label_name}')
                    updated_count += 1
                else:
                    Color.print_focus(f'[~] Label already exists: {label_name}')
                    skipped_count += 1
            else:
                # Create label
                popen(f'gh label create "{label_name}" --color "{label_color}" --description "{label_desc}"')
                Color.print_success(f'[+] Created label: {label_name}')
                created_count += 1

        except Exception as e:
            Color.print_failed(f'[-] Failed to process label {label_name}: {e}')

    Color.print_focus(f'\n[*] Label initialization complete:')
    Color.print_success(f'    Created: {created_count}')
    Color.print_success(f'    Updated: {updated_count}')
    Color.print_focus(f'    Skipped: {skipped_count}')


def get_archive_paths(date: str):
    """
    Get standardized archive paths for a given date
    Returns dict with paths for daily, pick, summary, and json

    New structure:
        archive/{year}/{month}/{day}/
        ├── daily.json        # 当日所有文章数据
        ├── daily.md          # 每日资讯汇总
        ├── pick.md           # 精选汇总
        ├── daily/            # 当日所有文章的 Markdown
        ├── summary/          # 当日 AI 摘要
        └── pick/             # 当日精选文章的 Markdown
    """
    year, month, day = date.split('-')
    base_path = root_path.joinpath(f'archive/{year}/{month}/{day}')

    return {
        'base': base_path,
        'daily_dir': base_path.joinpath('daily'),
        'pick_dir': base_path.joinpath('pick'),
        'summary_dir': base_path.joinpath('summary'),
        'daily_md': base_path.joinpath('daily.md'),
        'pick_md': base_path.joinpath('pick.md'),
        'json': base_path.joinpath('daily.json'),
    }


def update_today(data: dict = {}):
    """更新today"""
    paths = get_archive_paths(today)
    today_path = root_path.joinpath('today.md')

    if not data and paths['json'].exists():
        with open(paths['json'], 'r', encoding="utf-8") as f1:
            data = json.load(f1)

    # Create necessary directories
    paths['daily'].mkdir(parents=True, exist_ok=True)

    with open(today_path, 'w+', encoding="utf-8") as f1, open(paths['daily_md'], 'w+', encoding="utf-8") as f2:
        content = f'# 每日安全资讯（{today}）\n\n'
        for feed, articles in data.items():
            content += f'- {feed}\n'
            for title, article_data in articles.items():
                # Support both old format (string) and new format (dict with url and summary)
                if isinstance(article_data, str):
                    url = article_data
                    summary = None
                else:
                    url = article_data.get('url', '')
                    summary = article_data.get('summary')

                content += f'  - [ ] [{title}]({url})\n'
                if summary:
                    content += f'    > {summary}\n'
        f1.write(content)
        f2.write(content)


def update_rss(rss: dict, proxy_url=''):
    """更新订阅源文件"""
    proxy = {'http': proxy_url, 'https': proxy_url} if proxy_url else {
        'http': None, 'https': None}

    (key, value), = rss.items()
    rss_path = root_path.joinpath(f'rss/{value["filename"]}')

    result = None
    if url := value.get('url'):
        r = requests.get(value['url'], proxies=proxy)
        if r.status_code == 200:
            with open(rss_path, 'w+', encoding="utf-8") as f:
                f.write(r.text)
            print(f'[+] 更新完成：{key}')
            result = {key: rss_path}
        elif rss_path.exists():
            print(f'[-] 更新失败，使用旧文件：{key}')
            result = {key: rss_path}
        else:
            print(f'[-] 更新失败，跳过：{key}')
    else:
        print(f'[+] 本地文件：{key}')

    return result


def update_pick():
    yesterday_issues = json.loads(popen(
        f"gh issue list --label \"pick\" --search \"{yesterday}\" --json title,url,author,body"))
    today_path = root_path.joinpath('today_pick.md')
    if not yesterday_issues:
        Color.print_failed("not found any picker articles")
        for bot in picker_bots:
            bot.send_raw(
                f"[{yesterday} 精选汇总]", f"昨日({yesterday})没有精选文章, 别忘了阅读[每日信息流]({conf['repo']}/issues), 并点击`convert to issue` 挑选优质文章^v^")
        with open(today_path, "w+", encoding="utf-8") as f:
            f.write(f"昨日({yesterday})没有精选文章")
        return

    # Use new path structure
    paths = get_archive_paths(yesterday)
    data = {}
    if paths['json'].exists():
        with open(paths['json'], 'r', encoding="utf-8") as f1:
            data = json.load(f1)

    # Initialize AI processor for pick mode
    ai_processor = None
    ai_mode = conf.get('ai', {}).get('mode', 'pick')
    proxy_ai = conf['proxy']['url'] if conf.get('proxy', {}).get('ai', False) else ''
    if conf.get('ai', {}).get('enabled', False) and ai_mode == 'pick':
        ai_processor = ArticleProcessor(conf['ai'], proxy_ai)
        Color.print_focus('[+] AI summarization enabled for picked articles')

    picker = {}
    pick_urls = {}  # Store URLs for AI processing
    for issue in yesterday_issues:
        found = False
        issue_title = issue["title"].lstrip(f"[{yesterday}] ").strip()
        for feed, articles in data.items():
            for title, article_data in articles.items():
                # Support both old format (string) and new format (dict)
                if isinstance(article_data, str):
                    link = article_data
                else:
                    link = article_data.get('url', '')

                if issue_title == title:
                    found = True
                    if not picker.get(feed, ""):
                        picker[feed] = []
                    picker[feed].append((f"[{title}]({link})", issue["url"], None))
                    pick_urls[title] = link
        if not found:
            custom_feed = f"{issue['author']['login']} 手动精选"
            if not picker.get(custom_feed, ""):
                picker[custom_feed] = []
            title = issue["title"].lstrip(f"[{yesterday}]").strip()
            link = issue["body"]
            picker[custom_feed].append((f'[{title}]({link})', issue["url"], None))
            pick_urls[title] = link

    # Generate AI summaries for picked articles
    summaries = {}
    if ai_processor and ai_processor.enabled:
        Color.print_focus(f'[+] Generating summaries for {len(pick_urls)} picked articles...')
        for title, url in pick_urls.items():
            result = ai_processor.process_article(title, url)
            if result.get('summary'):
                summaries[title] = result['summary']

    # Update picker with summaries
    for feed in picker:
        updated_articles = []
        for link, issue_url, _ in picker[feed]:
            # Extract title from link markdown
            title = link.split('[')[1].split(']')[0] if '[' in link else ''
            summary = summaries.get(title)
            updated_articles.append((link, issue_url, summary))
        picker[feed] = updated_articles

    # Create pick directory
    paths['pick'].mkdir(parents=True, exist_ok=True)
    with open(today_path, 'w+', encoding="utf-8") as f1, open(paths['pick_md'], 'w+', encoding="utf-8") as f2:
        content = f'# 昨日精选汇总（{yesterday}）\n\n'
        for feed, articles in picker.items():
            content += f'- {feed}\n\n'
            for link, issue_url, summary in articles:
                content += f'  - {link} - [discussion]({issue_url})\n'
                if summary:
                    content += f'    > {summary}\n'

        f1.write(content)
        f2.write(content)

        for bot in picker_bots:
            bot.send_raw(f"[{yesterday} 精选汇总]", content)


def push_issue(issue_number):
    issue = json.loads(
        popen(f"gh issue view {issue_number} --json title,url,author,body"))
    issue_title = issue["title"].lstrip(f"[{today}]").strip()
    success = False
    paths = get_archive_paths(today)
    if paths['json'].exists():
        with open(paths['json'], 'r', encoding="utf-8") as f1:
            data = json.load(f1)

        text = ""
        for feed, articles in data.items():
            for title, link in articles.items():
                if title == issue_title:
                    success = True
                    body = feed + f": [{issue_title}]({link})"
                    print(body)
                    popen(f"gh issue edit {issue_number} --body \"{body}\"")
                    body = issue["author"]["login"] + " 挑选了精选文章:\n\n" + body
                    body += f"\n\n可以在[discussion]({issue['url']})讨论"
                    for bot in picker_bots:
                        bot.send_raw(issue_title, body)
                    break
            if success:
                break
    if not success:
        Color.print_focus(f"{issue_title} not found title in {today}.json")
        body = issue["author"]["login"] + " 新增了精选文章:\n\n" + issue_title + \
            " - " + issue["body"] + f"\n\n可以在 [discussion]({issue['url']}) 讨论"
        for bot in picker_bots:
            bot.send_raw(issue_title, body)


def push_comment(issue_number):
    issue = json.loads(
        popen(f"gh issue view {issue_number} --json title,url,comments"))
    issue_title = issue["title"].lstrip(f"[{today}]").strip()

    comment = issue["comments"][-1]
    text = f"{comment['author']['login']} 评论了 [{issue_title}]({issue['url']}): \n\n" + \
        comment["body"]
    for bot in picker_bots:
        bot.send_raw(f"{comment['author']['login']} 评论了 {issue_title}", text)


def parse_rss(url: str, proxy_url=''):
    """获取文章线程"""
    proxy = {'http': proxy_url, 'https': proxy_url} if proxy_url else {
        'http': None, 'https': None}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    title = ''
    result = {}
    try:
        r = requests.get(url, timeout=10, headers=headers,
                         verify=False, proxies=proxy)
        r = feedparser.parse(r.content)
        title = r.feed.title
        for entry in r.entries:
            d = entry.get('published_parsed')
            if not d:
                d = entry.updated_parsed
            yesterday = datetime.date.today() + datetime.timedelta(-1)
            pubday = datetime.date(d[0], d[1], d[2])
            if pubday == yesterday:
                print(entry.title)
                result[entry.title] = entry.link
        Color.print_success(
            f'[+] {title}\t{url}\t{len(result.values())}/{len(r.entries)}')
    except Exception as e:
        Color.print_failed(f'[-] failed: {url}, {e}')

    return title, result


# init_bot function is now imported from bot.py - removed duplicate


def init_rss(conf: dict, update: bool = False, proxy_url=''):
    """初始化订阅源"""
    rss_list = []
    enabled = [{k: v} for k, v in conf.items() if v['enabled']]
    for rss in enabled:
        if update:
            if rss := update_rss(rss, proxy_url):
                rss_list.append(rss)
        else:
            (key, file), = rss.items()
            rss_list.append(
                {key: root_path.joinpath(f'rss/{file["filename"]}')})

    # 合并相同链接
    feeds = []
    for rss in rss_list:
        (_, file), = rss.items()
        try:
            rss = listparser.parse(open(file, encoding="utf-8").read())
            for feed in rss.feeds:
                url = feed.url.strip().rstrip('/')
                short_url = url.split('://')[-1].split('www.')[-1]
                check = [feed for feed in feeds if short_url in feed]
                if not check:
                    feeds.append(url)
        except Exception as e:
            Color.print_failed(f'[-] 解析失败：{file}')
            print(e)

    Color.print_focus(f'[+] {len(feeds)} feeds')
    return feeds


def rssjob(args, conf):
    """定时任务"""

    proxy_rss = conf['proxy']['url'] if conf['proxy']['rss'] else ''
    proxy_ai = conf['proxy']['url'] if conf.get('proxy', {}).get('ai', False) else ''
    feeds = init_rss(conf['rss'], args.update, proxy_rss)
    count = 0
    results = {}

    # Initialize AI processor
    ai_processor = None
    ai_mode = conf.get('ai', {}).get('mode', 'pick')  # Default to 'pick' mode
    if conf.get('ai', {}).get('enabled', False):
        ai_processor = ArticleProcessor(conf['ai'], proxy_ai)
        Color.print_focus(f'[+] AI summarization enabled (mode: {ai_mode})')

    if args.test:
        # 测试数据 - 使用正确的格式
        results = {
            "测试订阅源A": {
                f"测试文章{i}": f"https://example.com/article{i}"
                for i in range(5)
            },
            "测试订阅源B": {
                f"另一篇测试文章{i}": f"https://example.com/test{i}"
                for i in range(5)
            }
        }
        count = sum(len(articles) for articles in results.values())

        # Save test data to new structure
        paths = get_archive_paths(today)
        paths['base'].mkdir(parents=True, exist_ok=True)
        with open(paths['json'], 'w+', encoding="utf-8") as f:
            f.write(json.dumps(results, indent=4, ensure_ascii=False))
            Color.print_focus(f'[+] JSON data: {paths["json"]}')

        # 更新today
        update_today(results)
    else:
        # 获取文章
        tasks = []
        with ThreadPoolExecutor(100) as executor:
            tasks.extend(executor.submit(parse_rss, url, proxy_rss)
                         for url in feeds)
            for task in as_completed(tasks):
                feed, result = task.result()
                if result:
                    count += len(result.values())
                    results[feed] = result
        Color.print_focus(f'[+] {len(results)} feeds, {count} articles')

        # AI处理：为文章生成摘要（仅在daily模式下）
        if ai_processor and ai_processor.enabled and ai_mode == 'daily':
            Color.print_focus('[+] Starting AI summarization for all articles...')
            processed_results = {}
            total_articles = sum(len(articles) for articles in results.values())
            processed_count = 0

            for feed, articles in results.items():
                Color.print_focus(f'[+] Processing {feed}: {len(articles)} articles')
                processed_articles = process_articles_batch(ai_processor, articles)
                processed_results[feed] = processed_articles
                processed_count += len(articles)
                Color.print_focus(f'[+] Progress: {processed_count}/{total_articles}')

                # Save articles as markdown files
                saved_count = save_articles_batch(
                    articles_data=processed_articles,
                    source=feed,
                    date=yesterday,
                    processor=ai_processor
                )
                Color.print_success(f'[+] Saved {saved_count}/{len(articles)} articles from {feed}')

            results = processed_results
            Color.print_success('[+] AI summarization completed')
        else:
            # Even if AI is disabled, we can still save articles as markdown
            # Only if MarkItDown conversion is needed
            if conf.get('save_articles_markdown', False):
                Color.print_focus('[+] Saving articles as markdown (without AI)...')
                # Initialize processor for markdown conversion only
                temp_processor = ArticleProcessor({'enabled': True}, proxy_ai)
                for feed, articles in results.items():
                    saved_count = save_articles_batch(
                        articles_data={title: {'url': url} for title, url in articles.items()},
                        source=feed,
                        date=yesterday,
                        processor=temp_processor
                    )
                    Color.print_success(f'[+] Saved {saved_count}/{len(articles)} articles from {feed}')

        # Use new path structure for JSON
        paths = get_archive_paths(today)
        paths['base'].mkdir(parents=True, exist_ok=True)
        with open(paths['json'], 'w+', encoding="utf-8") as f:
            f.write(json.dumps(results, indent=4, ensure_ascii=False))
            Color.print_focus(f'[+] JSON data: {paths["json"]}')

        # 更新today
        update_today(results)

    for bot in bots:
        bot.send(bot.parse_results(results))
        bot.send_raw(
            f"{today} 信息流摘要", f"今日({today})信息流推送完毕, 从{len(feeds)} feeds抓取到{yesterday}日共新增了{count}文章, 可在[issues]({conf['repo']}/issues)中查看")


def fetch_articles(date):
    """Fetch all articles for a given date and save as Markdown (without AI summary)"""
    paths = get_archive_paths(date)

    if not paths['json'].exists():
        Color.print_failed(f'[-] JSON file not found: {paths["json"]}')
        return

    with open(paths['json'], 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Count total articles
    total_articles = sum(len(articles) for articles in data.values())
    Color.print_focus(f'[+] Found {len(data)} feeds with {total_articles} articles for {date}')

    # Initialize processor (AI disabled, only for HTML->Markdown conversion)
    proxy_ai = conf['proxy']['url'] if conf.get('proxy', {}).get('ai', False) else ''
    processor = ArticleProcessor({'enabled': True}, proxy_ai)

    # Process each feed
    processed_count = 0
    saved_count = 0
    failed_count = 0

    for feed_name, articles in data.items():
        Color.print_focus(f'\n[+] Processing feed: {feed_name} ({len(articles)} articles)')

        for title, article_data in articles.items():
            # Support both old format (string) and new format (dict)
            if isinstance(article_data, str):
                url = article_data
            else:
                url = article_data.get('url', '')

            processed_count += 1
            print(f'  [{processed_count}/{total_articles}] {title[:60]}...')

            try:
                # Fetch HTML
                html_content = processor.fetch_article_content(url)
                if not html_content:
                    failed_count += 1
                    Color.print_failed(f'    [-] Failed to fetch HTML')
                    continue

                # Convert to Markdown
                markdown_content = processor.html_to_markdown(html_content)
                if not markdown_content:
                    failed_count += 1
                    Color.print_failed(f'    [-] Failed to convert to Markdown')
                    continue

                # Save (without summary)
                saved_path = save_article_markdown(
                    title=title,
                    url=url,
                    source=feed_name,
                    date=date,
                    markdown_content=markdown_content,
                    summary=None,  # No AI summary
                    category=None  # No category
                )

                if saved_path:
                    saved_count += 1
                    Color.print_success(f'    [+] Saved: {saved_path.name}')
                else:
                    failed_count += 1
                    Color.print_failed(f'    [-] Failed to save')

            except Exception as e:
                failed_count += 1
                Color.print_failed(f'    [-] Error: {e}')

    # Summary
    print('\n' + '='*80)
    Color.print_focus('Summary')
    print('='*80)
    print(f'Total articles:    {total_articles}')
    print(f'Processed:         {processed_count}')
    Color.print_success(f'Saved:             {saved_count}')
    Color.print_failed(f'Failed:            {failed_count}')
    print('='*80)


def summarize_issue(issue_number):
    """Generate AI summary for an issue and update it"""
    issue = json.loads(popen(f"gh issue view {issue_number} --json title,url,body,labels,author"))
    issue_title = issue["title"]
    issue_url = issue["url"]
    issue_body = issue["body"]

    Color.print_focus(f'[+] Summarizing issue #{issue_number}: {issue_title}')

    # Check if it's a pick issue (should have a URL in the body)
    # Extract URL from first line (handle both real newlines and literal \n)
    if not issue_body:
        Color.print_failed(f'[-] Issue body is empty')
        return

    # Handle both literal '\n' and actual newlines
    import re
    # Extract first line before any whitespace/markdown content
    # Split on real newlines or literal backslash-n sequences
    lines = re.split(r'[\n\r]+|\\n', issue_body.strip())
    article_url = lines[0].strip()

    if not article_url.startswith('http'):
        Color.print_failed(f'[-] Issue body does not contain a valid URL: {article_url[:100]}')
        return

    # Initialize AI processor
    proxy_ai = conf['proxy']['url'] if conf.get('proxy', {}).get('ai', False) else ''
    if not conf.get('ai', {}).get('enabled', False):
        Color.print_failed(f'[-] AI is not enabled in config')
        return

    ai_processor = ArticleProcessor(conf['ai'], proxy_ai)

    # Process the article
    Color.print_focus(f'[+] Fetching and processing: {article_url}')
    result = ai_processor.process_article(issue_title, article_url)

    if not result.get('summary'):
        Color.print_failed(f'[-] Failed to generate summary')
        return

    summary = result['summary']
    category = result.get('category')
    markdown_content = result.get('markdown_content', '')

    # Build new issue body with markdown content and summary
    new_body = f"{article_url}\n\n"

    if markdown_content:
        # Truncate markdown content if too long (GitHub issue limit is ~65536 chars)
        max_content_length = 30000
        if len(markdown_content) > max_content_length:
            markdown_content_truncated = markdown_content[:max_content_length] + "\n\n...(内容已截断)"
        else:
            markdown_content_truncated = markdown_content

        new_body += f"## 文章内容\n\n{markdown_content_truncated}\n\n"

    new_body += f"## AI 摘要\n\n{summary}"

    # Save as markdown file if content is available
    if markdown_content:
        # Extract source from labels or use default
        labels = [label['name'] for label in issue.get('labels', [])]
        source = next((label for label in labels if label not in ['pick', 'daily', 'dailypick']), 'Unknown')

        # Extract date from title [YYYY-MM-DD]
        import re
        date_match = re.search(r'\[(\d{4}-\d{2}-\d{2})\]', issue_title)
        date = date_match.group(1) if date_match else today

        # Clean title
        clean_title = re.sub(r'\[\d{4}-\d{2}-\d{2}\]\s*', '', issue_title).strip()

        saved_path = save_article_markdown(
            title=clean_title,
            url=article_url,
            source=source,
            date=date,
            markdown_content=markdown_content,
            summary=summary,
            category=category
        )

        if saved_path:
            Color.print_success(f'[+] Saved article markdown: {saved_path}')
            new_body += f"\n\n*文章已保存为 markdown: `{saved_path.relative_to(root_path)}`*"

    # Update issue
    try:
        # Write body to a temporary file to avoid escaping issues
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.md', delete=False) as tmp_file:
            tmp_file.write(new_body)
            tmp_file_path = tmp_file.name

        try:
            popen(f'gh issue edit {issue_number} --body-file "{tmp_file_path}"')
            Color.print_success(f'[+] Updated issue #{issue_number} with summary')
            Color.print_success(f'[+] Issue URL: {issue_url}')
        finally:
            # Clean up temporary file
            import os
            os.unlink(tmp_file_path)

        # Add category label if available
        if category and category in CATEGORY_LABELS:
            label_name = CATEGORY_LABELS[category]['name']
            try:
                popen(f'gh issue edit {issue_number} --add-label "{label_name}"')
                Color.print_success(f'[+] Added category label: {label_name}')
            except Exception as e:
                Color.print_failed(f'[-] Failed to add label {label_name}: {e}')

        # Push summary to picker bots
        bot_message = f"{issue['author']['login']} 的精选文章 AI 摘要已生成:\n\n"
        bot_message += f"**{issue_title}**\n\n"
        bot_message += f"🔗 {article_url}\n\n"
        bot_message += f"## AI 摘要\n\n{summary}\n\n"
        bot_message += f"可以在 [discussion]({issue_url}) 讨论"

        for bot in picker_bots:
            bot.send_raw(f"AI 摘要: {issue_title[:50]}...", bot_message)
        Color.print_success(f'[+] Sent summary to picker bots')

    except Exception as e:
        Color.print_failed(f'[-] Failed to update issue: {e}')


def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--update', help='Update RSS config file',
                        action='store_true', required=False)
    parser.add_argument(
        '--config', help='Use specified config file', type=str, required=False)
    parser.add_argument('--test', help='Test bot',
                        action='store_true', required=False)
    parser.add_argument('--push-issue', help="update issue")
    parser.add_argument("--update-pick", help="update pick",
                        action='store_true')
    parser.add_argument("--push-comment", help="update comment")
    parser.add_argument("--check", help="check bots", action='store_true')
    parser.add_argument("--init", help="Initialize GitHub labels for categories", action='store_true')
    parser.add_argument("--summarize-issue", help="Generate AI summary for issue", type=str, metavar="ISSUE_NUMBER")
    parser.add_argument("--fetch-articles", help="Fetch all articles for a date and save as Markdown (without AI summary)", type=str, metavar="DATE")
    return parser.parse_args()


if __name__ == '__main__':
    args = argument()
    global bots, picker_bots
    conf = {}
    if args.config:
        config_path = Path(args.config).expanduser().absolute()
    else:
        config_path = root_path.joinpath('config.yml')
    with open(config_path, encoding="utf-8") as f:
        conf = yaml.safe_load(f)

    proxy_bot = conf['proxy']['url'] if conf['proxy']['bot'] else ''
    bots = init_bot(conf['bot'], proxy_bot)
    picker_bots = init_bot(conf["pick_bot"], proxy_bot, True)
    if args.init:
        init_labels()
    elif args.push_issue:
        push_issue(args.push_issue)
    elif args.update_pick:
        update_pick()
    elif args.push_comment:
        push_comment(args.push_comment)
    elif args.summarize_issue:
        summarize_issue(args.summarize_issue)
    elif args.fetch_articles:
        fetch_articles(args.fetch_articles)
    elif args.check:
        for bot in bots:
            bot.send_raw("test title", "test content")
        for bot in picker_bots:
            bot.send_raw("test picker title", "test picker content")
    else:
        rssjob(args, conf)
