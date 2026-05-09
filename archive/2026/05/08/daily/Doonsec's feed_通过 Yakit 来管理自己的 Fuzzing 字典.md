---
title: 通过 Yakit 来管理自己的 Fuzzing 字典
url: https://mp.weixin.qq.com/s/lFwqmgDFLbpU3_5a2opgAw
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:04:53.311326
---

# 通过 Yakit 来管理自己的 Fuzzing 字典

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVnSK7bXgP510xEWJ3QJIqwePUBxOQlFkXTT6AibiadxHIhyGOa06NM8yUNxLicGhD0kNgcegYcxETLyWicmnibvl6BA3M63Pfu2YAQ0/0?wx_fmt=jpeg)

# 通过 Yakit 来管理自己的 Fuzzing 字典

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 774，阅读大约需 4 分钟

## 前言

有师傅私信问我，Fuzzing 的字典是有什么好的管理办法。

他是采用用文件夹管理的，用 maye + 标题区分。但随着字典越来越大，单纯的 txt 文件，很容易遗忘。五一回来之后，他看着密密麻麻的字典和莫名起来的拼音缩写命名，找不到需要的字典文件。

我目前是用 Yakit 来管理的，因为 Yakit 的 fuzz 功能很强大，放在 Yakit 的**字典管理**中更方便些。

## Yakit 字典管理

位置：Yakit 右上角
![826f6646b930cbd708c9f0c0d7b0e17b.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkld4zibfNibyBW9weY1Ry38vnNUgAJBsl4Quym2yd1Xw4oicNK1Jb4WCPWfanxsz4icFmvDibPVBm7P1wSOPVVJA51aNZdibUM5ul2M/640?from=appmsg "null")

826f6646b930cbd708c9f0c0d7b0e17b.png

管理自己的字典，我一般分成两个部分

1. 1. 通用字典
2. 2. xxx 系统特用字典

![1f811e7c3cb1f5f78228213ff973eb9a.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkGAB8aXm9Re5ZXsMWTbMAhAd2sSI7BKkVAXUGq49TLrHTY7t6K5ysbesAvF5ibg3tvzbhptgVa5tQJf9hoH4xZ91oOYK1V13fU/640?from=appmsg "null")

1f811e7c3cb1f5f78228213ff973eb9a.png

一类存放常见的参数、API、用户名密码。
新建文件夹放渗透测试中遇到的系统，把从 JS 中收集到的 API、或者获取到的敏感信息放在里面。等后续扩大战果的时候使用。

最后再把特殊字典里比较常用的放在通用字典里面。

## 路径提取保存到字典

Yakit 插件 **提取历史流量包的参数和路径**
![0ddaa4febd240cf997fa6ea297b54a4f.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVktJ8vWvF48TrS1Fzric8iaGlHBNQ8tF5Moxb1cL9pOLJSYzuX3xdKqs9jR3x3M7LZ3lh6zYx8wwQwNMtGCQHBtZheFVywVdS5fI/640?from=appmsg "null")

0ddaa4febd240cf997fa6ea297b54a4f.png

整理保存，推荐用**数据库存储**
虽然可以保存到不同的文件夹下，但是字典名要求是唯一的。可以在字典前面增加前缀来区分
![724fb4837b1ce2c24e5e44cb84bb205e.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkrPNb0zgIFY1G6DLAm2oy0bxzezzBR4gA0yEEL5z8pWIQibPec6jT1d9ar4pJox5kEX5ErRBZguj5tEoJI26CqEA7FcnyR2zSk/640?from=appmsg "null")

724fb4837b1ce2c24e5e44cb84bb205e.png

复制 fuzztag
![67c7dadee35cb5e88d44549796784cb6.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkiawJZjqRTHKibC46UniccL81ckB3A3gMG42HW7H3hzwEjia0CjvXWhmGKwxtibXy1yHrWRAIa0AGWicuojaxD2abFwvG0UY5I7quxY/640?from=appmsg "null")

67c7dadee35cb5e88d44549796784cb6.png

在 web fuzzer 中使用即可
![4e4361fa892aee8b403c61a76ed348c6.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlmgsC5PyZR9Saade6d7raicnWkcg7nnolrWmpNArfkGbGTibZUxmyibhLpY6VeAVebBuoI3K93WQrSbiaE6kFXM2twY7WCllbEVcI/640?from=appmsg "null")

4e4361fa892aee8b403c61a76ed348c6.png

有需要也可以导出使用
![47ecab6b23f4ee60012a87ef39acea44.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk7Syic7uWDTyfCYvxtPALg5Fb79KiaQBNicC9qnYc187J3wB7saATNVn2nGOGrlQFWibJSHw1nm3EialmKt1iadia3hzOiaichNLSwj1OQ/640?from=appmsg "null")

47ecab6b23f4ee60012a87ef39acea44.png

选中指定序号，可以复制或移动到其他字典
![be983f7de52f5c16a22a4c5f140ea6e8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlUaurmCh7MH4aKfVFCfic9Eu52Tt68M0muhcWW6tfsQ7TNqEB5RO54bpMIY55aD0g09UsQWrNoCBKIDye5rHrJeM1PWzvtgw4o/640?from=appmsg "null")

be983f7de52f5c16a22a4c5f140ea6e8.png

## 字典保存在哪？

在 yakit-profile-plugin.db 当中，数据库为 sqlite
![fe82118bc61f6723cfc495649b931f51.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVleTEllsiaCnE16GfRdde04eJbNrTibbictydVkWImAqH8kBCF2lC7m7UyBKgMAlgibqAicibwQVgKEkqhr8POfkUs99pVy4icoZNW6AY/640?from=appmsg "null")

fe82118bc61f6723cfc495649b931f51.png

navicat 打开，在 payloads 表中
![399cb18050784856e60f648d1aaa336d.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk2BxZYHwpKQW3CfibAIXCntsDst2vdQ0ric4WnTfeOF9DI4L9qrOwXV85YhToU2Eib3zqF9b3e9icGlaBlwJRNqKMtLfkNRYXe4G8/640?from=appmsg "null")

399cb18050784856e60f648d1aaa336d.png

## 增加命中次数

我试了一下，虽然 Yakit 字典管理中有命中次数，但似乎并不会自动增加，需要手动操作。
手动一个个点，遇到批量的情况就比较麻烦，既然知道了数据库和数据表的位置，不如直接在里面改，让大模型帮忙写个脚本

如何使用

```
usage: add_hit_count.py [-h] [--db DB] group txt_file
add_hit_count.py: error: the following arguments are required: group, txt_file
```

案例

```
python add_hit_count.py --db D:\路径\yakit-projects\yakit-profile-plugin.db "ruoyi-完整路径" hit_count.txt
```

结果：
![d081894d2814eecc9630f8d0cbeedf52.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn3sXRKc7s0LkF6EuYwEpuxeo0rHuUF2f71VNvABURZjc4KE1N46u8Csib4zTESosKeKut1mB582fJc9Jber28GUjzTgOkN0upU/640?from=appmsg "null")

d081894d2814eecc9630f8d0cbeedf52.png

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import argparse
import os

def update_hit_count(db_path, target_group, txt_path):
    # 1. 读取路径
    if not os.path.exists(txt_path):
        print(f"错误：文件 {txt_path} 不存在！")
        return

    paths = set()
    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                paths.add(line)

    if not paths:
        print("错误：txt无有效路径")
        return

    print(f"成功读取 {len(paths)} 条路径")

    # 2. 连接数据库
    if not os.path.exists(db_path):
        print(f"错误：数据库 {db_path} 不存在")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    update_count = 0

    try:
        update_sql = '''
        UPDATE payloads
        SET hit_count = hit_count + 1
        WHERE "group" = ? AND content = ?
        '''

        for path in paths:
            # 给路径前后加上双引号，和数据库一致
            payload_with_quote = f'"{path}"'
            cursor.execute(update_sql, (target_group, payload_with_quote))
            update_count += cursor.rowcount

        conn.commit()
        print(f"更新完成！成功更新 {update_count} 行！")

    except Exception as e:
        conn.rollback()
        print(f"失败：{str(e)}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="若依payload hit_count更新脚本")
    parser.add_argument("group", help="分组名，例如：ruoyi-完整路径")
    parser.add_argument("txt_file", help="路径txt文件")
    parser.add_argument("--db", required=True, help="数据库完整路径")

    args = parser.parse_args()
    update_hit_count(args.db, args.group, args.txt_file)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过