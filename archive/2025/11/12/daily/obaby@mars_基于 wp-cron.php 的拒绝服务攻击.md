---
title: 基于 wp-cron.php 的拒绝服务攻击
url: https://h4ck.org.cn/2025/11/21970
source: obaby@mars
date: 2025-11-12
fetch_date: 2025-11-13T03:13:40.706247
---

# 基于 wp-cron.php 的拒绝服务攻击

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

黑客程序媛 / 逆向工程师 / 人工智能学徒 / 用爱发电的独立开发者

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# 基于 wp-cron.php 的拒绝服务攻击

2025年11月12日
[45 条评论](https://h4ck.org.cn/2025/11/21970#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/微信图片_20251112133651_375_42.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20251112133651_375_42.jpg)

这几天不知道是发生什么事了，说是不知道什么事情，但是大概率是被打了。只是这次打的挺高级的，外层的 eo 貌似也没什么反应。只是那个访问量通过 umami 看，直接爆炸了。

平常几百的访问量，昨天的时候，结果到了 2000 多，当然这不是最奇怪的，奇怪的是服务器过了会儿卡死了。之前都是因为请求太多 php-fpm 耗尽 cpu 资源卡死了，这次以为还是同样的问题。然而，并不是，发现 mysql 把 cpu 跑满了，查看日志的时候发现大量的 wp-cron.php 的请求，这尼玛，请求直接透传过来了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Screenshot-2025-11-12-074653-scaled.png)](https://h4ck.org.cn/wp-content/uploads/2025/11/Screenshot-2025-11-12-074653.png)

另外还有一大堆 bot 的请求，包括 bing 以及一些乱起八糟的爬虫遍历。

最开始没想到什么好办法，简单粗暴的把 wp-cron.php 改名了，暂时解决了这个问题。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Screenshot-2025-11-12-075200-scaled.png)](https://h4ck.org.cn/wp-content/uploads/2025/11/Screenshot-2025-11-12-075200.png)

不过这个方法的确是高明，带着参数透传过来，wp 就是疯狂的执行，一条没执行完就到了下一条。然而，对于这种事情直接改名的确是可以解决办法，不过后来想了一下还是直接从 eo 下手吧。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251112-134435-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251112-134435.jpg)

尽管 eo 防住了 22 万次的攻击，但是，这些透传的请求，直接让 mysql 耗尽了 cpu 资源，也是个不错的办法，甚至请求频率都不用太高。流量到了 144g，这也不知道是哪个哥们又闲的蛋疼了，**如果真的蛋疼来找姐姐啊，姐姐帮你治疗，直接给你割下来，塞你自己嘴里！**

昨天晚上发现这个情况的时候，本来是想去处理下的，结果对象在用电脑，自己又不想去开笔记本，就用手机处理了一下，简单的改下了文件名。

今天早上才处理了一下，加到了 eo 的访问规则里：

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251112-134908.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251112-134908.jpg)

尽管如此，还是对这几天的访问记录比较好奇，想看看请求了多少次。去拉 nginx 日志的时候发现文件已经 1.5G 了。直接截取这几天的记录，用 goaccess 跑了一下，但是比较奇怪的是这个 wp-cron.php 的请求竟然没有。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251112-085552-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251112-085552.jpg)

暂时放弃 goaccess 直接使用 ngxtop 进行数据分析：

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用ngxtop分析Nginx日志中的POST请求
提供交互式菜单和多种分析选项
"""

import subprocess
import sys
import os
from pathlib import Path

def run_ngxtop(cmd_args):
    """运行ngxtop命令"""
    venv_python = Path(__file__).parent / "venv" / "bin" / "python"
    ngxtop_script = Path(__file__).parent / "venv" / "bin" / "ngxtop"

    if not ngxtop_script.exists():
        print("错误: ngxtop未安装，请先运行: source venv/bin/activate && pip install ngxtop")
        sys.exit(1)

    try:
        result = subprocess.run(
            [str(ngxtop_script)] + cmd_args,
            capture_output=True,
            text=True,
            check=False
        )
        print(result.stdout)
        if result.stderr and "error" in result.stderr.lower():
            print(result.stderr, file=sys.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        return False

def show_menu():
    """显示菜单"""
    print("\n" + "="*60)
    print("Nginx日志POST请求分析 - ngxtop工具")
    print("="*60)
    print("1. POST请求总览")
    print("2. 按URL统计POST请求 (Top 20)")
    print("3. 按IP统计POST请求 (Top 20)")
    print("4. 按状态码统计POST请求")
    print("5. POST请求中状态码为404的URL")
    print("6. POST请求中状态码为200的URL")
    print("7. 可疑POST请求 (xmlrpc, wp-login等)")
    print("8. POST请求详情示例")
    print("9. 自定义查询")
    print("0. 退出")
    print("="*60)

def analyze_post_requests(log_file):
    """分析POST请求"""
    if not os.path.exists(log_file):
        print(f"错误: 日志文件 {log_file} 不存在")
        return

    base_args = ["-l", log_file, "--no-follow", "-i", 'request.startswith("POST")']

    while True:
        show_menu()
        choice = input("\n请选择分析选项 (0-9): ").strip()

        if choice == "0":
            print("退出分析")
            break
        elif choice == "1":
            print("\n【POST请求总览】")
            print("-" * 60)
            run_ngxtop(base_args + ["--limit", "0"])
        elif choice == "2":
            print("\n【按URL统计POST请求 (Top 20)】")
            print("-" * 60)
            run_ngxtop(base_args + ["--group-by", "request_path", "--limit", "20"])
        elif choice == "3":
            print("\n【按IP统计POST请求 (Top 20)】")
            print("-" * 60)
            run_ngxtop(base_args + ["--group-by", "remote_addr", "--limit", "20"])
        elif choice == "4":
            print("\n【按状态码统计POST请求】")
            print("-" * 60)
            run_ngxtop(base_args + ["--group-by", "status", "--limit", "0"])
        elif choice == "5":
            print("\n【POST请求中状态码为404的URL (Top 10)】")
            print("-" * 60)
            run_ngxtop(["-l", log_file, "--no-follow",
                       "-i", 'request.startswith("POST") and status == 404',
                       "--group-by", "request_path", "--limit", "10"])
        elif choice == "6":
            print("\n【POST请求中状态码为200的URL (Top 10)】")
            print("-" * 60)
            run_ngxtop(["-l", log_file, "--no-follow",
                       "-i", 'request.startswith("POST") and status == 200',
                       "--group-by", "request_path", "--limit", "10"])
        elif choice == "7":
            print("\n【可疑POST请求统计】")
            print("-" * 60)
            run_ngxtop(["-l", log_file, "--no-follow",
                       "-i", 'request.startswith("POST") and (request_path == "/xmlrpc.php" or request_path == "/wp-login.php" or request_path.startswith("/wp-admin"))',
                       "--group-by", "request_path", "--limit", "0"])
        elif choice == "8":
            print("\n【POST请求详情示例 (前10条)】")
            print("-" * 60)
            run_ngxtop(base_args + ["print", "remote_addr", "time_local", "request", "status", "bytes_sent", "--limit", "10"])
        elif choice == "9":
            print("\n【自定义查询】")
            print("-" * 60)
            print("示例查询:")
            print("  - 查看特定URL: ngxtop -l <file> -i 'request.startswith(\"POST\") and request_path == \"/wp-cron.php\"'")
            print("  - 查看特定IP: ngxtop -l <file> -i 'request.startswith(\"POST\") and remote_addr == \"114.66.247.160\"'")
            print("  - 查看错误请求: ngxtop -l <file> -i 'request.startswith(\"POST\") and status >= 400'")
            print("\n请输入自定义ngxtop命令参数 (用空格分隔):")
            custom_args = input("> ").strip().split()
            if custom_args:
                run_ngxtop(["-l", log_file, "--no-follow"] + custom_args)
        else:
            print("无效的选择，请重试")

        input("\n按回车键继续...")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        # 查找默认日志文件
        log_files = list(Path(".").glob("*.txt"))
        if log_files:
            default_log = str(log_files[0])
            print(f"未指定日志文件，使用默认: {default_log}")
            log_file = default_log
        else:
            print("用法: python analyze_with_ngxtop.py <日志文件路径>")
            print("示例: python analyze_with_ngxtop.py 11-08_org.txt")
            sys.exit(1)
    else:
        log_file = sys.argv[1]

    analyze_post_requests(log_file)

if __name__ == "__main__":
    main()
```

运行命令：

```
python3 analyze_with_ngxtop.py 11-08_org.txt
```

分析结果：

```
【按URL统计POST请求 (Top 20)】
------------------------------------------------------------

running for 7 seconds, 23670 records processed: 3508.50 req/sec

Summary:
|   count |   avg_bytes_sent |   2xx |   3xx |   4xx |   5xx |
|---------+------------------+-------+...