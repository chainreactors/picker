---
title: noip2025 candy和noi 2026 binary
url: https://mp.weixin.qq.com/s/JIk2xP_OBD_S7pcM3Bx1NA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:35:54.442941
---

# noip2025 candy和noi 2026 binary

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xyspsQs8n7z26ugKuKchcM77ZCVjUdWYcMmW1kvcEGOALJD8oUQ86YBYPOGvaXoooYbuvOPiaiaJ1QLUNnjicapdzemr2sLAibZeiceeXuQiccGG4/0?wx_fmt=jpeg)

# noip2025 candy和noi 2026 binary

原创

Uysieot
Uysieot

简单读写

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xyspsQs8n7wvfpZYj3e7WSUzMu23umIcDx4pAibcOlkDWDXWYzm4Dyt025b01icUQ2q7CGuBnRXzx67cLaQNjgDjiawjdPpaic7ib1Ryn4AkQctU/640?wx_fmt=png&from=appmsg)

```
def solve(inp):    data = inp.split()
    it = iter(data)    n = int(next(it))    m = int(next(it))
    x_list = []    min_pair = 10**18
    for _ in range(n):        x = int(next(it))        y = int(next(it))        x_list.append(x)        min_pair = min(min_pair, x + y)
    x_list.sort()    prefix = [0]    for x in x_list:        prefix.append(prefix[-1] + x)
    res = 0    for t in range(n + 1):        if prefix[t] > m:            break        rem = m - prefix[t]        pairs = rem // min_pair        res = max(res, t + 2 * pairs)
    return str(res)
```

![](https://mmbiz.qpic.cn/mmbiz_png/xyspsQs8n7xFaNkkkI2LNjPtEwL7ib30x7e0gAPG0yAI7lHnXJIfK0GAvD4P5sbBDrFeXqGdYXCVoGx3ZWtRa2jIomfuzInZOyibFz44iaEh9s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xyspsQs8n7wNxpHC7Hw6qMMER176bib9icbh7ZEOjJqU5sKOwLsria6LiaKC37rX72CvHicMrlLsTKXgoNcWoicB4lshdZctcU1ApGSianuBBFqbZ4/640?wx_fmt=png&from=appmsg)

```
def min_ops_binary(x, y):    ops = 0    while x != y:        if x > y:            if x % 2 == 0 and x // 2 >= y:                x //= 2            else:                y += 1            ops += 1        elif y > x:            if y % 2 == 0 and y // 2 >= x:                y //= 2            else:                x += 1            ops += 1        else:            break    return ops
def main():    input = sys.stdin.read    data = input().split()
    index = 0    c = int(data[index])    index += 1    t = int(data[index])    index += 1
    results = []    for _ in range(t):        x = int(data[index])        index += 1        y = int(data[index])        index += 1        results.append(min_ops_binary(x, y))
    for res in results:        print(res)
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OCOHF928I9a7kKm699bm7hDv8HmzINwuiaytTT1Id92xDSIcRMYKwlo5K9yDeCr2aPoWKxpibdsEn6pqGPpnaclA/0?wx_fmt=png)

简单读写

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OCOHF928I9a7kKm699bm7hDv8HmzINwuiaytTT1Id92xDSIcRMYKwlo5K9yDeCr2aPoWKxpibdsEn6pqGPpnaclA/0?wx_fmt=png)

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