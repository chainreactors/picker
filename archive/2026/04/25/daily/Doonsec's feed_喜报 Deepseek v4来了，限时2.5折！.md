---
title: 喜报 Deepseek v4来了，限时2.5折！
url: https://mp.weixin.qq.com/s/k4IKIlA6LaTkFJKigxJ_EA
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:54:39.277085
---

# 喜报 Deepseek v4来了，限时2.5折！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfN3ia4mQcaspa1mqibQppoXnmjK07rYDjgg3yyrNMiaPKKRTEjy9boJ6BJFKJKIRBwWmwqPvFiatibLgJVZOPgRVREGib0oiadsD6d1ss/0?wx_fmt=jpeg)

# 喜报 Deepseek v4来了，限时2.5折！

原创

仙草里没有草噜丶
仙草里没有草噜丶

泷羽Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfN4xKchHS4AuujZgJ2G73uqXRYYqHibuxnyavPj8oSDnW7ox2Xx5bbFK0zaC7FlK4Q9iaCPKvaibmBNZ1eYpFiaWl8IqZt6FkC9w5I/640?wx_fmt=png&from=appmsg)

从去年开始就说要发布v4，一直到现在，快去玩玩

![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfMCxuIIjDgictnzibrqFjgBia0ibTEkMZoWBia4ndk9qfeUFvXsGlNBaQXXm9xSTzuYkujezu7RqUuoF8E0kLaN43Oic7vFgTFpXW7Zc/640?wx_fmt=png&from=appmsg)

api接口地址：https://platform.deepseek.com/

如何调用？找到api keys，点击创建一个 API key

![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfPAEtOCJl2eRXTAsWCzE7CPDiaJuLYjMMycADXZv0p8z6wic35ibksJAOaKicHI3Poibo9FiajTTTYp2TWx1niat5rH9mGheLvQLQPGBY/640?wx_fmt=png&from=appmsg)

名字随便填

![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfOCOIlP0VbGlgpOfwN3FCBn30e7IK3ROY3LCC0BrupLtSTic5kybWkutCiaOfeWjFGbPDyoKtKLziaB7D1pPkGvLJGj3AA4xomibho/640?wx_fmt=png&from=appmsg)

点击复制

![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfN9EVg51sDCsjnzgicrnLDnzhiaZEOM3tDbDW6eY5FSuwL1BRTqhnGwFQWCo5iagIr46x3YuzFMo9AEZmh6JDs5GlUKcVQO63oMTQ/640?wx_fmt=png&from=appmsg)

完整代码如下

```
# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-c2db472174d14d1e884542136f9db5d4",
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个乐于助人的助手"},
        {"role": "user", "content": "你好"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)
```

![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfPUZmbKOAhByn2YAziafj2l3FugHaDyyibw3DsPL4YnrGUDjjFOCxnRsic9kT8ZZRuaN5YiaO6dDPgib5ZE7nMoogYiaBoKJuGwGRCt0/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWG2YeKibdOsJywysp4aTnLsvRodjpEhfhbPXvica7364Dn6VO7Ybtpma6IUaFciaiaZG8Sr9yJ2Dwuv1Q/0?wx_fmt=png)

泷羽Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWG2YeKibdOsJywysp4aTnLsvRodjpEhfhbPXvica7364Dn6VO7Ybtpma6IUaFciaiaZG8Sr9yJ2Dwuv1Q/0?wx_fmt=png)

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