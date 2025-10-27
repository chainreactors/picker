---
title: afrog批量扫描优化速度脚本
url: https://forum.90sec.com/t/topic/2509
source: 90Sec - 最新话题
date: 2025-06-22
fetch_date: 2025-10-06T22:52:27.805766
---

# afrog批量扫描优化速度脚本

[90Sec](/)

# [afrog批量扫描优化速度脚本](/t/topic/2509)

[工具资源](/c/tools/8)

[82303224](https://forum.90sec.com/u/82303224)

2025 年6 月 21 日 14:19

1

1. 背景 小青蛙批量扫站 300多个内网资产 扫了15个小时 扫了35%
2. 第二天优化 脚本，大概2个小时左右就扫完了35%
   设置5个线程同时跑，单个目标大概需要请求1719次好像是，-rl 默认是150，5个设的各20，设置单个目标扫描超时时间1500s，25分钟还没扫完，就扫下一个。

第一个扫描脚本是：afrog\_rce.py

```
import subprocess
import concurrent.futures
import os
import chardet

def read_file_auto_encoding(filename):
    with open(filename, 'rb') as f:
        raw = f.read()
        result = chardet.detect(raw)
        encoding = result['encoding'] or 'utf-8'
        try:
            return raw.decode(encoding)
        except Exception:
            return raw.decode('utf-8', errors='replace')

def run_afrog(url, idx):
    out_file = f"result_{idx}.html"
    command = f"afrog.exe -t {url} -oob dnslogcn -o {out_file} -rl 20 -c 5 -timeout 20 -retries 2  "
    try:
        print(f"正在扫描: {url} (任务 {idx + 1})")
        subprocess.run(command, shell=True, check=True, timeout=1500)
        print(f"成功扫描: {url}")
        if os.path.exists(out_file):
            content = read_file_auto_encoding(out_file)
            print(f"扫描结果 for {url}:\n{content}\n")
        else:
            print(f"提示: {url} 扫描完成但未发现漏洞，未生成结果文件")
    except subprocess.TimeoutExpired:
        print(f"错误: {url} 扫描超时未完成。")
    except subprocess.CalledProcessError as e:
        print(f"错误发生在 {url}: {e}")
    except Exception as e:
        print(f"未知错误发生在 {url}: {e}")

def main():
    if not os.path.exists('url.txt'):
        print("错误: url.txt 文件不存在")
        return

    with open('url.txt', 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if line.strip()]

    if not urls:
        print("错误: url.txt 中没有有效的URL")
        return

    total_urls = len(urls)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for idx, url in enumerate(urls):
            futures.append(executor.submit(run_afrog, url, idx))
            print(f"已提交任务 {idx + 1}/{total_urls}: {url}")

        for idx, future in enumerate(concurrent.futures.as_completed(futures)):
            try:
                future.result()
                print(f"任务完成 {idx + 1}/{total_urls}")
            except Exception as e:
                print(f"任务处理异常: {e}")

def merge_html_files():
    all_contents = []
    files_merged = 0
    for filename in os.listdir('.'):
        if filename.startswith('result_') and filename.endswith('.html'):
            try:
                content = read_file_auto_encoding(filename)
                all_contents.append(content)
                files_merged += 1
            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

    if not all_contents:
        print("没有找到要合并的结果文件")
        return

    with open('jieguo_all.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html lang="zh">\n<head>\n<meta charset="UTF-8">\n<title>合并结果</title>\n</head>\n<body>\n')
        for content in all_contents:
            f.write('<div>\n')
            f.write(content)
            f.write('</div>\n')
        f.write('</body>\n</html>')
    print(f"成功合并 {files_merged} 个结果文件到 jieguo_all.html")

if __name__ == "__main__":
    main()
    merge_html_files()
    print("已全部完成。")
```

第2个合并结果脚本是：afrog\_jieguo.py

```
import subprocess
import concurrent.futures
import os
import chardet

def read_file_auto_encoding(filename):
    with open(filename, 'rb') as f:
        raw = f.read()
        result = chardet.detect(raw)
        encoding = result['encoding'] or 'utf-8'
        try:
            return raw.decode(encoding)
        except Exception:
            return raw.decode('utf-8', errors='replace')

def merge_html_files():
    all_contents = []
    files_merged = 0
    for filename in os.listdir('.'):
        if filename.startswith('result_') and filename.endswith('.html'):
            try:
                content = read_file_auto_encoding(filename)
                all_contents.append(content)
                os.remove(filename)
                files_merged += 1
                print(f"已合并并删除文件: {filename}")
            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

    if not all_contents:
        print("没有找到要合并的结果文件")
        return

    with open('jieguo_all.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html lang="zh">\n<head>\n<meta charset="UTF-8">\n<title>合并结果</title>\n</head>\n<body>\n')
        for content in all_contents:
            f.write('<div>\n')
            f.write(content)
            f.write('</div>\n')
        f.write('</body>\n</html>')
    print(f"成功合并 {files_merged} 个结果文件到 jieguo_all.html")

if __name__ == "__main__":
    merge_html_files()
```

* [首页](/)
* [类别](/categories)
* [准则](/guidelines)
* [服务条款](/tos)
* [隐私政策](/privacy)

由 [Discourse](https://www.discourse.org) 提供技术支持，启用 JavaScript 以获得最佳体验