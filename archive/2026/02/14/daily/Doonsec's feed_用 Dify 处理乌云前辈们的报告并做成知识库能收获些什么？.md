---
title: 用 Dify 处理乌云前辈们的报告并做成知识库能收获些什么？
url: https://mp.weixin.qq.com/s/_Ha8d0SYpj3-Dp6LdIYK-A
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:23:07.766293
---

# 用 Dify 处理乌云前辈们的报告并做成知识库能收获些什么？

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/ULOszTo2RiaAibzenrAYib3Y3SY95fqPkciaXn59icrMvsf4xxK0o6femaQZVdBLbsUzE0EETE633qEibbgkaNgOupLlh1Vc7Fbo5ibDZeL61n5bJA/0?wx_fmt=jpeg)

# 用 Dify 处理乌云前辈们的报告并做成知识库能收获些什么？

原创

IceCliffs
IceCliffs

Gh0xE9

![]()

在小说阅读器中沉浸阅读

> 前排提醒：吃水不忘挖井人，现在能挖出漏洞，大多数都是靠的前辈们那些数不清的技巧和手法，这些宝贵的经验不仅缩短了后者学习的路径，更让我们在面对日益复杂的防御机制时，能够站在巨人的肩膀上，观察到更远的安全边界

早在 Dify 刚出来时，我就已经着手用自己报告做 RAG 了，不过那时候报告很少，搞出来的东西基本上没什么用，于是在 2025 年初，用前辈们的乌云报告搓出了一个 bot，现在跟各位师傅汇报一下这一年使用下来的一些感受

在开始之前，需要把乌云的报告弄到手，我在很早之前写过一个爬乌云报告并转换成 pdf 的脚本，详见如下，当时是用来爬线上公开的乌云报告，后面有百度网盘会员了才下了乌云镜像导本地的报告

```
import os
import re
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
from pathlib import Path
import html2text
import hashlib
import pdfkit
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

class WooYunCrawler:
    def __init__(self, base_url="http://192.168.50.103", output_dir="output"):
        self.base_url = base_url
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        self.images_dir = os.path.join(self.output_dir, 'images')
        Path(self.images_dir).mkdir(parents=True, exist_ok=True)
        self.wkhtmltopdf_path = self._find_wkhtmltopdf()
        self.file_lock = threading.Lock()

    def _find_wkhtmltopdf(self):
        import shutil
        common_paths = [
            '/usr/local/bin/wkhtmltopdf',
            '/usr/bin/wkhtmltopdf',
            '/opt/homebrew/bin/wkhtmltopdf',
            shutil.which('wkhtmltopdf')
        ]

        for path in common_paths:
            if path and os.path.exists(path):
                return path
        return None

    def get_page(self, url, retry=3):
        for i in range(retry):
            try:
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                response.encoding = 'utf-8'
                return response.text
            except Exception as e:
                if i == retry - 1:
                    print(f"获取页面失败 {url}: {e}")
                    return None
                time.sleep(2)
        return None

    def get_total_pages(self):
        url = f"{self.base_url}/bugs.php?page=1500"
        html = self.get_page(url)
        if not html:
            return 1

        soup = BeautifulSoup(html, 'lxml')
        max_page = 1

        pagination = soup.find('div', class_=re.compile('page|pagination', re.I))
        if not pagination:
            pagination = soup.find(string=re.compile('末页|下一页|上一页', re.I))
            if pagination:
                pagination = pagination.find_parent()

        if pagination:
            page_links = pagination.find_all('a')
            for link in page_links:
                href = link.get('href', '')
                if 'page=' in href:
                    try:
                        page_num = int(re.search(r'page=(\d+)', href).group(1))
                        max_page = max(max_page, page_num)
                    except:
                        pass

        if max_page == 1:
            page_text = soup.get_text()
            page_match = re.search(r'共\s*\d+\s*条记录[，,]\s*(\d+)\s*页', page_text)
            if page_match:
                max_page = int(page_match.group(1))

        if max_page == 1:
            last_page_link = soup.find('a', string=re.compile('末页|最后一页', re.I))
            if not last_page_link:
                for link in soup.find_all('a'):
                    if '末页' in link.get_text() or '最后一页' in link.get_text():
                        last_page_link = link
                        break

            if last_page_link:
                href = last_page_link.get('href', '')
                match = re.search(r'page=(\d+)', href)
                if match:
                    max_page = int(match.group(1))

        if max_page == 1:
            print("无法自动检测总页数，将尝试递增查找...")
            for page in range(2, 100):
                test_url = f"{self.base_url}/bugs.php?page={page}"
                html = self.get_page(test_url)
                if html:
                    test_soup = BeautifulSoup(html, 'lxml')
                    test_links = test_soup.find_all('a', href=re.compile(r'bug_detail\.php.*wybug_id='))
                    if test_links:
                        max_page = page
                    else:
                        if page > 5:
                            break
                else:
                    break
                time.sleep(0.2)

        if max_page > 1000:
            print(f"检测到页数: {max_page}，正在验证...")
            test_pages = [1, 100, 500, 1000, max_page]
            actual_max = 1
            for test_page in test_pages:
                if test_page > max_page:
                    break
                test_url = f"{self.base_url}/bugs.php?page={test_page}"
                html = self.get_page(test_url)
                if html:
                    test_soup = BeautifulSoup(html, 'lxml')
                    test_links = test_soup.find_all('a', href=re.compile(r'bug_detail\.php.*wybug_id='))
                    if test_links:
                        actual_max = test_page
                        print(f"  第{test_page}页有内容")
                    else:
                        print(f"  第{test_page}页无内容，停止验证")
                        break
                else:
                    break
                time.sleep(0.1)

            if actual_max >= 100:
                print(f"验证通过，将爬取所有 {max_page} 页")
            else:
                print(f"验证失败，将爬取前 {actual_max * 2} 页")
                max_page = actual_max * 2

        return max(1, max_page)

    def get_article_links_from_page(self, page_num):
        url = f"{self.base_url}/bugs.php?page={page_num}"
        html = self.get_page(url)
        if not html:
            return []

        soup = BeautifulSoup(html, 'lxml')
        links = []
        seen_urls = set()

        article_links = soup.find_all('a', href=re.compile(r'bug_detail\.php\?wybug_id='))

        if not article_links:
            article_links = soup.find_all('a', href=re.compile(r'bug_detail\.php'))

        if not article_links:
            all_links = soup.find_all('a', href=True)
            for link in all_links:
                href = link.get('href', '')
                if 'bug_detail.php' in href and 'wybug_id=' in href:
                    article_links.append(link)

        for link in article_links:
            href = link.get('href', '')
            if not href.startswith('http'):
                href = urljoin(url, href)

            id_match = re.search(r'wybug_id=([^&]+)', href)
            if id_match:
                article_id = id_match.group(1)
                full_url = urljoin(self.base_url, href)

                if full_url in seen_urls:
                    continue
                seen_urls.add(full_url)

                title = link.get_text(strip=True)
                if not title or len(title) < 3:
                    parent = link.parent
                    if parent:
                        parent_text = parent.get_text(strip=True)
                        if parent_text and parent_text != title:
                            title = parent_text

                    if not title or len(title) < 3:
                        next_sibling = link.find_next_sibling()
                        if next_sibling:
                            title = next_sibling.get_text(strip=True)

                if title:
                    title = re.sub(r'\s+', ' ', title).strip()

                if title and len(title) > 3 and title not in ['首页', '登录', '注册', '上一页', '下一页', '末页', '搜索']:
                    links.append({
                        'url': full_u...