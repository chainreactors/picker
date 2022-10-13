#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import json
import time
import schedule
import pyfiglet
import argparse
import datetime
import listparser
import feedparser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from bot import *
from utils import Color, Pattern, popen

import requests
requests.packages.urllib3.disable_warnings()

today = datetime.datetime.now().strftime("%Y-%m-%d")
yesterday = str(datetime.date.today() + datetime.timedelta(-1))
root_path = Path(__file__).absolute().parent


def update_today(data: dict= {}):
    """更新today"""
    data_path = root_path.joinpath(f'archive/tmp/{today}.json')
    today_path = root_path.joinpath('today.md')
    archive_path = root_path.joinpath(f'archive/daily/{today.split("-")[0]}/{today}.md')

    if not data and data_path.exists():
        with open(data_path, 'r', encoding="utf-8") as f1:
            data = json.load(f1)

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with open(today_path, 'w+', encoding="utf-8") as f1, open(archive_path, 'w+', encoding="utf-8") as f2:
        content = f'# 每日安全资讯（{today}）\n\n'
        for feed, articles in data.items():
            content += f'- {feed}\n'
            for title, url in articles.items():
                content += f'  - [ ] [{title}]({url})\n'
        f1.write(content)
        f2.write(content)


def update_rss(rss: dict, proxy_url=''):
    """更新订阅源文件"""
    proxy = {'http': proxy_url, 'https': proxy_url} if proxy_url else {'http': None, 'https': None}

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
    today_issues = json.loads(popen(f"gh issue list --label \"pick\" --search \"{yesterday}\" --json title,url"))
    if not today_issues:
        return

    today_path = root_path.joinpath('yesterday_pick.md')
    archive_path = root_path.joinpath(f'archive/daily_pick/{yesterday.split("-")[0]}/{yesterday}.md')
    data_path = root_path.joinpath(f'archive/tmp/{yesterday}.json')
    data = {}
    if data_path.exists():
        with open(data_path, 'r', encoding="utf-8") as f1:
            data = json.load(f1)

    picker = {}
    for issue in today_issues:
        issue_title = issue["title"].lstrip(f"[{yesterday}] ").strip()
        for feed, articles in data.items():
            for title, link in articles.items():
                if issue_title == title:
                    if not picker.get(feed, ""):
                        picker[feed] = []
                    picker[feed].append((title, link, issue["url"]))

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with open(today_path, 'w+', encoding="utf-8") as f1, open(archive_path, 'w+', encoding="utf-8") as f2:
        content = f'# 每日精选汇总（{yesterday}）\n\n'
        for feed, articles in picker.items():
            content += f'- {feed}\n'
            for title, link, issue_url in articles:
                content += f'  - [{title}]({link}) - [discussion]({issue_url})\n'

        f1.write(content)
        f2.write(content)

        for bot in bots:
            bot.send_raw(f"[{yesterday} 精选汇总]", content)


def update_issue(issue_number):
    issue = json.loads(popen(f"gh issue view {issue_number} --json title,url,author"))
    issue_title = issue["title"].lstrip(f"[{today}]").strip()
    data_path = root_path.joinpath(f'archive/tmp/{today}.json')
    if data_path.exists():
        with open(data_path, 'r', encoding="utf-8") as f1:
            data = json.load(f1)
        success = False
        text = ""
        for feed, articles in data.items():
            for title, link in articles.items():
                if title == issue_title:
                    success = True
                    body = feed + f": [{title}]({link})"
                    print(body)
                    popen(f"gh issue edit {issue_number} --body \"{body}\"")
                    body = issue["author"]["login"] + " 挑选了精选文章:\n\n" + body
                    body += f"\n\n可以在[discussion]({issue['url']})讨论"
                    for bot in bots:
                        bot.send_raw(title, body)
                    break
            if success:
                break
        if not success:
            Color.print_failed(f"{issue_title} not found title in {today}.json")


def update_comment(issue_number):
    pass


def parseThread(url: str, proxy_url=''):
    """获取文章线程"""
    proxy = {'http': proxy_url, 'https': proxy_url} if proxy_url else {'http': None, 'https': None}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    title = ''
    result = {}
    try:
        r = requests.get(url, timeout=10, headers=headers, verify=False, proxies=proxy)
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
        Color.print_success(f'[+] {title}\t{url}\t{len(result.values())}/{len(r.entries)}')
    except Exception as e:
        Color.print_failed(f'[-] failed: {url}')
        print(e)

    return title, result


def init_bot(bot_conf: dict, proxy_url=''):
    """初始化机器人"""
    bots = []
    for name, v in bot_conf.items():
        if v['enabled']:
            key = os.getenv(v['secrets']) or v['key']
            bot_name = globals()[f'{name}Bot']
            if name == 'mail':
                receiver = os.getenv(v['secrets_receiver']) or v['receiver']
                bot = bot_name(v['address'], key, receiver, v['from'], v['server'])
                bots.append(bot)
            elif name == 'qq':
                bot = bot_name(v['group_id'])
                if bot.start_server(v['qq_id'], key):
                    bots.append(bot)
            elif name == 'telegram':
                bot = bot_name(key, v['chat_id'], proxy_url)
                if bot.test_connect():
                    bots.append(bot)
            elif name == 'dingtalk':
                bot = bot_name(key, os.getenv("DINGTALK_SECRET", "") or v['secret'], proxy_url)
                bots.append(bot)
            else:
                bot = bot_name(key, proxy_url)
                bots.append(bot)
    return bots


def init_rss(conf: dict, update: bool=False, proxy_url=''):
    """初始化订阅源"""
    rss_list = []
    enabled = [{k: v} for k, v in conf.items() if v['enabled']]
    for rss in enabled:
        if update:
            if rss := update_rss(rss, proxy_url):
                rss_list.append(rss)
        else:
            (key, value), = rss.items()
            rss_list.append({key: root_path.joinpath(f'rss/{value["filename"]}')})

    # 合并相同链接
    feeds = []
    for rss in rss_list:
        (_, value), = rss.items()
        try:
            rss = listparser.parse(open(value,encoding="utf-8").read())
            for feed in rss.feeds:
                url = feed.url.strip().rstrip('/')
                short_url = url.split('://')[-1].split('www.')[-1]
                check = [feed for feed in feeds if short_url in feed]
                if not check:
                    feeds.append(url)
        except Exception as e:
            Color.print_failed(f'[-] 解析失败：{value}')
            print(e)

    Color.print_focus(f'[+] {len(feeds)} feeds')
    return feeds


def job(args, conf):
    """定时任务"""

    proxy_rss = conf['proxy']['url'] if conf['proxy']['rss'] else ''
    feeds = init_rss(conf['rss'], args.update, proxy_rss)

    results = {}
    if args.test:
        # 测试数据
        results = {"a":"i+1" for i in range(100)}
    else:
        # 获取文章
        numb = 0
        tasks = []
        with ThreadPoolExecutor(100) as executor:
            tasks.extend(executor.submit(parseThread, url, proxy_rss) for url in feeds)
            for task in as_completed(tasks):
                feed, result = task.result()
                if result:
                    numb += len(result.values())
                    results[feed] = result
        Color.print_focus(f'[+] {len(results)} feeds, {numb} articles')

        temp_path = root_path.joinpath(f'archive//tmp//{today}.json')
        with open(temp_path, 'w+', encoding="utf-8") as f:
            f.write(json.dumps(results, indent=4, ensure_ascii=False))
            Color.print_focus(f'[+] temp data: {temp_path}')

        # 更新today
        update_today(results)

    for bot in bots:
        bot.send(bot.parse_results(results))


def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--update', help='Update RSS config file', action='store_true', required=False)
    parser.add_argument('--cron', help='Execute scheduled tasks every day (eg:"11:00")', type=str, required=False)
    parser.add_argument('--config', help='Use specified config file', type=str, required=False)
    parser.add_argument('--test', help='Test bot', action='store_true', required=False)
    parser.add_argument('--update-issue', help="update issue")
    parser.add_argument("--update-pick", help="update pick", action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = argument()
    global bots
    print(f'{pyfiglet.figlet_format("yarb")}\n{today}')
    conf = {}
    if args.config:
        config_path = Path(args.config).expanduser().absolute()
    else:
        config_path = root_path.joinpath('config.json')
    with open(config_path, encoding="utf-8") as f:
        conf = json.load(f)

    proxy_bot = conf['proxy']['url'] if conf['proxy']['bot'] else ''
    bots = init_bot(conf['bot'], proxy_bot)

    if args.cron:
        schedule.every().day.at(args.cron).do(job, args)
        while True:
            schedule.run_pending()
            time.sleep(1)
    elif args.update_issue:
        update_issue(args.update_issue)
    elif args.update_pick:
        update_pick()
    else:
        job(args, conf)
