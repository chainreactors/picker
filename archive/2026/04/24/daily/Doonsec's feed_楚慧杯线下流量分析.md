---
title: 楚慧杯线下流量分析
url: https://mp.weixin.qq.com/s/mrKT7XWb2OCtrmVkji5tRQ
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:29:52.690116
---

# 楚慧杯线下流量分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmoSzLfPyB0YkPmFRQg2YTJol4kgqAeakIHbeuuHia2libaoVcU8q6KOzN1XWc67RNYmicYxLwjwAtUc3ibLVLpiajXeVTfMG5qgPM4/0?wx_fmt=jpeg)

# 楚慧杯线下流量分析

原创

江思澄
江思澄

云晞科技Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 楚慧杯线下流量分析

## 找到冰蝎马的绝对路径

过滤http流量可以看到主要来源是.shE11.php和behind.php

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmiauEnUKWRzO0QV8BjlEdZxaDCCo0ogEEYv8ryS0En6NwGFqNoxiasDIWEFGWFQbvGEyco8b5JMcN27qLapI6NCt8AuwkqQYV04/640?wx_fmt=png&from=appmsg)

.shE11.php 疑似蚁剑的特征流量

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVkNBlPGCT5YcNYRglc8aZI6uE4hv21SeyTyKJzcPibC43Q4ficOjVxYvJpn79yS6AWp1m4a4YntSpf3OEmel98xVYjibDA2ZDQbYI/640?wx_fmt=png&from=appmsg)

behind.php 疑似是冰蝎3.x的流量特征

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVkXDra6vuXnPVo7twuyEMy9aVNUh94Gfibbh2ekYse67P1dtoFgmAeuuAxnKYecNVg7aJicZKYMbJPicicEg3GEicsZHZSFhkicFEynw/640?wx_fmt=png&from=appmsg)

打开第一条behind.php流量，发现存在冰蝎马的绝对路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlvluG4EI2EhhDzg4JsAfMd5l12lp0vG1icuIKJy5FicZl54icWicibNQksjbM7U0mRXjdce1ec4V0IiaRng3biaODCPqrIKdPpibk3x9Y/640?wx_fmt=png&from=appmsg)

## 找到冰蝎的key

设想冰蝎马可能是通过蚁剑连接上传的

蚁剑流量特性（通常会使用base64编码)，找到最后的base64密文，把开头两位去掉进行base64解密 就是黑客执行的命令了

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVkKq0B3FsETibBxMSGXcrE3WmyFv52qibHDHGC8KdjONemfVukicibiatHw66C0zNLBwKibczxqVWXPAC4Az29icVVcL9p22eC7vk9UsE/640?wx_fmt=png&from=appmsg)

接着向下翻流挨个解密蚁剑流量

30流解密发现冰蝎马的绝对路径，而且该流有一串疑似十六进制编码的字符

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVlTsspvAickP9v2k49ukPHf5QDx0tGamicx1TlTMthjiaaYWaskEA4UNKXn4XFqaUTp7krjMcgdLqkjSsAZ85icZVfQIia7CrExeBick/640?wx_fmt=png&from=appmsg)

找到key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlP1d7Uv6Sm1ia6vsZicAjwzmkVd8EHm4WRNeGWhm83aHpmjotmL3WxFOEVIU8V6cF5hRxbxiaAflL8tVpMeGahBUlXeq2sMo4464/640?wx_fmt=png&from=appmsg)

## 找到流量包中的flag

接下来开始解密冰蝎马的流量，拿flag只需解密响应体的加密数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVn7yZ2SYaXVdgGVw7ic1njx4PFO9BpUXImtUbIxeFxPXYpRvMicK8ykJqYPTEfic4T1FrEiceNZeRXHuPeyRAL3FtxvibtcbhcFnuibo/640?wx_fmt=png&from=appmsg)

还有一层base64编码，从解密的json数据上看疑似ls命令执行的结果

```
import sys, json, base64

if len(sys.argv) > 1:
raw = open(sys.argv[1], "r", encoding="utf-8").read()
else:
raw = sys.stdin.read()
data = json.loads(raw)

for idx, entry in enumerate(data, start=1):
name = base64.b64decode(entry["name"]).decode()
size_bytes = int(base64.b64decode(entry["size"]))
last_modified = base64.b64decode(entry["lastModified"]).decode()
perm = base64.b64decode(entry["perm"]).decode()
ftype = base64.b64decode(entry["type"]).decode()
print(f"{idx}. name={name}, type={ftype}, size={size_bytes} bytes, "
f"lastModified={last_modified}, perm={perm}")
```

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVnK232pGWuwr5B4qeaUibenlphUz1WFBLic1QgeLMTry5LVbr2UWwcXd2Q1YoMneY2X7VtHwAVibKT3f4Q07st9NKEBWymRibL1LOM/640?wx_fmt=png&from=appmsg)

接着向下解密，重复操作

在第39流 解密出flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnlicQodiaPHTvlVic1955f4DXTJ21ngibEw2TOBSNv21qfeNib4H5mDG782TsdgHfXDePuHGXMyrrJPALNQfZarS7JYOjmsuE5Miapk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkWxldunh4v5P4wAW730iaLF1pibwIibreYHictv8TrDeafP54d2lLJH0xUay45qs5pbL2u95vicnk1I9WGUKvCjgDkakQ4AoHiaGjEk/640?wx_fmt=png&from=appmsg)

## 找到黑客上传至/tmp目录下的扫描器

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVltBibadOEFU8SeuEXVibib8Efdia4yA8aExav8icATTB6Tm1RRsbpzl4IWFQ5fv79uLAVw7qwS5icA9FALQhKHVK1giaOQo9k6ebF6P4/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVnXb2P8AKicTCKVc88Z2uXau4IllfPv91MQe7qz9LH1W5EibcVKQ4yszYIUlHIiaXkQjc43sJw7iahDrYVFmlJKadFjrMHTq5VaD5M/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlA6sbuI3ZM8QjMLeyxMTm36E47R95Gaic6rDibpYicyia9HIRgAAtQibGSnNvHIiaPmSNHJmmESqD2hUsFl474g9e9mMS9VrVo27yvY/0?wx_fmt=png)

云晞科技Sec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlA6sbuI3ZM8QjMLeyxMTm36E47R95Gaic6rDibpYicyia9HIRgAAtQibGSnNvHIiaPmSNHJmmESqD2hUsFl474g9e9mMS9VrVo27yvY/0?wx_fmt=png)

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