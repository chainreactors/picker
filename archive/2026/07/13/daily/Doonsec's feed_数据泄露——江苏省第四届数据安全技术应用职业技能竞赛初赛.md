---
title: 数据泄露——江苏省第四届数据安全技术应用职业技能竞赛初赛
url: https://mp.weixin.qq.com/s/HALhDzzBmtegBNsT4AS1gQ
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:43:10.502102
---

# 数据泄露——江苏省第四届数据安全技术应用职业技能竞赛初赛

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RJrNBTwulveW9lOStWOqkHRFKxUxE93NgibibibNSjl2LHChtfoHe3r9JTqtxYp9U2vJeB56uEESz7d6vzq0nb7kbMKtO8kIIIxFAzFLZYM7JI/0?wx_fmt=jpeg)

# 数据泄露——江苏省第四届数据安全技术应用职业技能竞赛初赛

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 数据泄露——江苏省第四届数据安全技术应用职业技能竞赛初赛

## 缘起

其实这次赛事组织的真不咋地，一会儿没插座，一会儿附件无法下载，还有题目是奇奇怪怪的，比如这题，附件使用usb拷贝的，有三问，但是实际试卷却只有俩问……

总的来说，这是一道经典的题目，就是sql注入日志分析,这题还算简单————因为题目常规，脚本是备好的，

可惜，还是没得分，第一问做出来了，但是题目没有，第二问也做出来了，但是一直答案不对……，第三问就没做了

## 题干

先说，题目附件我放在cnb了：https://cnb.cool/netvvorm/items/datasecurity26

第一问：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvdToZWWON1DDNf7ToTfic1XtARFPrrTOl9yzKmygMSblgLtysSByjdtbFcVjlxAbfphl6ic6icMlLLjmXoaFyrpW9EicDVgiakjUafg/640?wx_fmt=png&from=appmsg)

但是附件下载后，第一问实际是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvc5TpCaVTfztNXjMaB0d00c1KeoFnkKUTVDrsXqaaBLFuRzccUIxlvXdkzbOLet3r8niaoglrNMUX4t7xzxxMicnxzf4xia841Zwk/640?wx_fmt=png&from=appmsg)

## 分析

这种sql注入是经典题目，有时候还会套一层流量分析：就是先要从流量包里面导出这些日志，notepad打开是这样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvcGwMjuB0xoNLvJJOXbsntLkPRibCPPG6YnHHaVlQLV6wn1tEwibxY9tibY20SelXCbKHdaF9LQGeqgekwfyNodeJ3GcOyM3x9WPE/640?wx_fmt=png&from=appmsg)

有个小技巧，使用notepad++自带的工具进行url decode：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvcGRzm2FNjQYTUuoibSDzicptDrAbAHrKibjUqTbamGlVZG2ibY1sKbXNaiaaMfLiarHNbrC3Xderxvv4ogHJHrDQLK5JJOypd2O90pE/640?wx_fmt=png&from=appmsg)

这样比较容易看得清楚：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvd9THibTSVBwkDoSTCwcuVBToHF2y10cymQluktRMEmyHDrPhdDtvpUEA6YNW4FB3qer6UjPvfscZQef9p00EFZibIxupc6ic7zro/640?wx_fmt=png&from=appmsg)

### 布尔盲注

什么叫盲注：就是select的信息内容不会实际返回

什么叫布尔：即使返回结果根据对错有无，返回只有2中情况，所以借以判断注入结果

一般数据库、表、字段命名，大部遵循ascii码，而ascii码的值的范围是0-127，所以有一种简单的办法就是将想要查询的字段的每个字符与所有的ascii码进行比较，如果返回的结果与预期不符，则说明该字符不存在，否则存在，这样就可以逐个字符的查询了，当然实用的方法是二分法，而不是真的顺序查询。

以本题的第一个字符为例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvcrC06wyU14zNzud3Gvnv6fvgIdiaXEv4kqibfbaiaqAXG7hezAp4nzWYjpccbxZnZn7zmNbTvgeCon4Q39aEYhVuGxR4kbyHSyqo/640?wx_fmt=png&from=appmsg)

实际执行的sql是这样的：

```
sql

-- 布尔条件：第1个字符的ASCII码是否大于97？
-- 注入字段
ORD(MID((SELECT IFNULL(CAST(username AS NCHAR),0x20) FROM user_data.`user` ORDER BY id LIMIT 0,1),1,1))>63 AND 'CWkt'='CWkt

-- 后台执行的sql（例）
SELECT * FROM user WHERE id = 1 AND ORD(MID((SELECT username FROM user LIMIT 0,1),1,1))>63
```

然后来分析日志：

1. 先确认true和false

返回的结果都是http code=200，但是长短只有2个，一个是24，一个47，看一眼（这一眼是指根据二分法查找的值的变化来判断的），24=true，47=false，

小知识：判断一般有这几种情况

| 信号类型 | 示例 |
| --- | --- |
| **响应体长度不同** | True→24字节, False→47字节 |
| HTTP状态码不同 | True→200, False→302 |
| 响应时间差异 | True→<100ms, False→>500ms（时间盲注） |
| 页面特征文本 | True含"Welcome", False含"Error" |

2. 二分法轮询

```
code

第1轮：> 63 ?  →  True → 值在 (63, 127]
第2轮：> 95 ?  →  True → 值在 (95, 127]
第3轮：> 111 ? →  False → 值在 (95, 111]
第4轮：> 103 ? →  False → 值在 (95, 103]
第5轮：> 99 ?  →  False → 值在 (95, 99]
第6轮：> 97 ?  →  False → 值在 (95, 97]
第7轮：> 96 ?  →  True  → 值 = 97  ✓
```

asscii码的值是97，所以第一个字符是a

后面就简单的了，最终结果：

```
+----------+------------+
| 字段     | 值         |
+----------+------------+
| username | admin      |
| password | Adm1n@2026 |
+----------+------------+
```

脚本：

这个脚本是AI给的，因为他比我的脚本好看，就提供这个了：

```
python

#!/usr/bin/env python3
"""
SQL Boolean Blind Injection Log Analyzer
========================================
从Web访问日志中还原SQL布尔盲注（二分搜索模式）窃取的数据库内容。

适用场景：
  - CTF取证题：给定access.log，还原被盲注窃取的数据
  - 应急响应：分析攻击者通过盲注读取了哪些敏感字段

支持的Payload格式（sqlmap常见风格）：
  ORD(MID((SELECT IFNULL(CAST(field AS NCHAR),0x20)
         FROM database.`table` ORDER BY col LIMIT row,1),pos,1))>threshold

用法：
  python sqli_blind_log_analyzer.py -f access.log [--true-size 24] [--false-size 47] [--auto-detect]

作者：CTF Log Forensics Tool
"""

import re
import sys
import argparse
import urllib.parse
from collections import defaultdict

# ──────────────────────── 正则模式 ────────────────────────

# 匹配sqlmap风格的布尔盲注payload
PAYLOAD_PATTERN = re.compile(
    r"ORD\(MID\(\(SELECT IFNULL\(CAST\((\w+) AS NCHAR\),0x20\)"
    r" FROM (\w+)\.`(\w+)` ORDER BY \w+ LIMIT (\d+),1\)"
    r",(\d+),1\)\)>(\d+)"
)

# 更宽松的匹配：不要求ORD/MID/IFNULL的具体格式，只要有关键结构
LOOSE_PATTERN = re.compile(
    r"(?:ORD|ASCII)\(.*?MID\(.*?(?:SELECT|select).*?"
    r"(\w+).*?LIMIT\s+(\d+),1.*?,(\d+),1\).*?>(\d+)",
    re.IGNORECASE | re.DOTALL
)

# 日志行解析
LOG_PATTERN = re.compile(
    r'(\S+).*?"(\w+)\s+(\S+)\s+HTTP[^"]*"\s+(\d+)\s+(\d+)'
)

# ──────────────────────── 核心逻辑 ────────────────────────

def parse_log(filepath, true_size=None, false_size=None, auto_detect=True):
    """
    解析日志文件，提取所有盲注请求并还原数据。

    参数:
        filepath:    日志文件路径
        true_size:   响应True时的body长度（已知时传入）
        false_size:  响应False时的body长度（已知时传入）
        auto_detect: 是否自动检测True/False对应的响应长度

    返回:
        dict: {(field, db, table, row): {position: char}}
    """
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    print(f"[*] 日志行数: {len(lines)}")

    # 第一遍：收集所有请求信息
    requests = []
    size_counter = defaultdict(int)

    for line in lines:
        m = LOG_PATTERN.search(line)
        if not m:
            continue

        ip, method, url, status_code, body_size = m.groups()
        if method != 'GET' or int(status_code) != 200:
            continue

        body_size = int(body_size)
        decoded_url = urllib.parse.unquote(url)

        # 尝试匹配payload
        pm = PAYLOAD_PATTERN.search(decoded_url)
        if not pm:
            continue

        field = pm.group(1)       # 字段名
        db = pm.group(2)          # 数据库名
        table = pm.group(3)       # 表名
        row = int(pm.group(4))    # 行偏移
        pos = int(pm.group(5))    # 字符位置
        threshold = int(pm.group(6))  # 比较阈值

        requests.append((field, db, table, row, pos, threshold, body_size))
        size_counter[body_size] += 1

    print(f"[*] 有效盲注请求数: {len(requests)}")
    print(f"[*] 响应长度分布: {dict(sorted(size_counter.items(), key=lambda x: -x[1]))}")

    # ── 自动检测 True/False 对应的响应长度 ──
    if true_size is None or false_size is None:
        if auto_detect and len(size_counter) == 2:
            sizes = sorted(size_counter.keys())
            # 启发式：较小的size通常对应True（页面返回简化内容）
            # 但这不总是成立，需要验证
            print(f"[!] 响应只有两种长度: {sizes[0]} 和 {sizes[1]}")
            print(f"[!] 需要确定哪个是True，哪个是False")

            # 尝试两种方向，用逻辑一致性验证
            for ts, fs in [(sizes[0], sizes[1]), (sizes[1], sizes[0])]:
                if verify_consistency(requests, ts, fs):
                    true_size, false_size = ts, fs
                    print(f"[+] 验证通过: True={true_size}, False={false_size}")
                    break
            else:
                # 两种方向都无法完美验证，默认取较小值为True
                true_size, false_size = sizes[0], sizes[1]
                print(f"[!] 无法自动验证，默认 True={true_size}, False={false_size}")
                print(f"[!] 如结果不正确，请用 --true-size 和 --false-size 手动指定")
        else:
            print("[!] 无法自动检测，请用 --true-size 和 --false-size 指定")
            return {}

    # ── 按字符位置分组，执行二分搜索还原 ──
    char_tests = defaultdict(list)
    for field, db, table, row, pos, threshold, body_size in requests:
        is_true = (body_size == true_size)
        char_tests[(field, db, table, row, pos)].append((threshold, is_true))

    reconstructed = defaultdict(dict)
    for key, tests in char_tests.items():
        field, db, table, row, pos = key
        ascii_val = resolve_binary_search(tests)
        if ascii_val > 0:
            reconstructed[(field, db, table, row)][pos] = chr(ascii_val)

    return reconstructed

def verify_consistency(requests, true_size, false_size, sample_limit=50):
    """
    验证True/False方向是否逻辑一致。

    原理：二分搜索的True/False序列应当形成合理的区间——
    所有True的阈值应当 < 所有False的阈值。
    """
    consistent = 0
    total = 0

    # 按字符分组
    groups = defaultdict(list)
    for field, db, table, row, pos, threshold, body_size in requests[:sample_limit * 7]:
        is_true = (body_size == true_size)
        groups[(field, db, table, row, pos)].append((threshold, is_true))

    for key, tests in groups.items():
        if len(tests) <...