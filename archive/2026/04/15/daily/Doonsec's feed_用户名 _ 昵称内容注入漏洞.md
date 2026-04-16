---
title: 用户名 / 昵称内容注入漏洞
url: https://mp.weixin.qq.com/s/SzeDpY60Ywdg1WxF7-H-bw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:46:16.909638
---

# 用户名 / 昵称内容注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/F4N4AId99XfmcA8uJRJpl4zccYUwc11YXls0PiaTsz5a7xRYg6vMn8jXzcLQYGwFQygBFbydicsjqUOYPLZwc5RIe19ojTYEjcpyhXEG7JLxI/0?wx_fmt=jpeg)

# 用户名 / 昵称内容注入漏洞

原创

小帅安全
小帅安全

小帅安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XcPAHeE5c9M5ZC1tUJ61B8W4HrbfCh3nRmfPJKNPicLbaABsbCbJKFI3n9GeDp89ap3a4wiamLnuSibzLXxU9aQcvYdC7NqOsVkQU/640?wx_fmt=png&from=appmsg)

免责声明

```
本公众号“小帅安全”旨在分享网络安全领域的相关知识，仅限于学习和研究之用。本公众号并不鼓励或支持任何非法活动。本公众号中提供的所有内容都是基于作者的经验和知识，并仅代表作者个人的观点和意见。这些观点和意见仅供参考，不构成任何形式的承诺或保证。本公众号不对任何人因使用或依赖本公众号提供的信息、工具或技术所造成的任何损失或伤害负责。本公众号提供的技术和工具仅限于学习和研究之用，不得用于非法活动。任何非法活动均与本公众号的立场和政策相违背，并将依法承担法律责任。本公众号不对使用本公众号提供的工具和技术所造成的任何直接或间接损失负责。使用者必须自行承担使用风险，同时对自己的行为负全部责任。本公众号保留随时修改或补充免责声明的权利，而不需事先通知。
```

----往期推荐-----

[EDU实战之巧用Google Hacking语法接管全站用户](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483760&idx=1&sn=4aac2031ac62a4f8bf0ee40114874bc9&scene=21#wechat_redirect)

[一次从证书站到证书站的通杀](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483799&idx=1&sn=366d6ac4c5c1fc7a4f6e482c5a9c194a&scene=21#wechat_redirect)

[EDU挖掘到的简单满分漏洞之Vue框架实战加资产收集语法](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483745&idx=1&sn=210b474b3666c4b90564400c388ad46a&scene=21#wechat_redirect)

[最近挖到的几个存储桶相关的edu实战案例分享](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483938&idx=1&sn=4e4a6dc0505e9bda8bef734290a5993a&scene=21#wechat_redirect)

这次分享的是一个关于用户名可控的漏洞

没有对用户输入的姓名字段做过滤和限制，导致邮箱发送的内容可控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xd7m3cOxkOJUo4QIV8aDAuvYpochGtV54ZANaCGuDGuSu7xRqOvrBRs0QYRYxkeZDSTw7mibFk8rNx1AEbBiaRfbiaiap2H5Q4vjEs/640?wx_fmt=png&from=appmsg)

危害

## **钓鱼攻击：**

**HTML注释或隐藏标签（如果支持HTML）**

姓名修改为：吴斌

\r\n\r\n【系统通知】您的账户存在安全风险，请立即点击链接重置密码，<a href="https://www.attacker.com">xxx统一认证</a><!--

**实际效果**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XdxMZeOtgIr4SwJiaaVQ3F2NVh5G0mQW0fZJWhcicVIbrKsAKuLJ4iadLZBy6j7kkfrQHu7BE9Qb1DbRUNgWd2FEYqcYpA5srCDGA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XdAEg2WvKY2hPialafV1z7licwRiafacXE85ibib5icRq8ibJBWN0bk8WBb5aOdTxGYHicPiaKe05qdpJ1NGIibxDb4ZfPQfmRzjK8y6nz6w/640?wx_fmt=png&from=appmsg)

可以看到xxx统一认证指向的是攻击者的恶意钓鱼网址，但是“您好：

您的邮件验证码为：824662；验证码有效期15分钟。”这样的内容已经被注释掉，并且发送人的邮箱是学校官方邮箱在实际中用户更容易相信并点击钓鱼链接。

![](https://mmbiz.qpic.cn/mmbiz_gif/F4N4AId99Xe9PeTWgOEyj8doHC5ia6Neiap9keSwoyeNw1rvQG0933PCnVrV0vgn6UibxCVia9OibDwjavu8sTcIfa0LCO6w5ibnBzXVTSjMc332c/640?wx_fmt=gif)

## **发布不良信息**

姓名处可控，攻击者精心制作内容，修改为yellow、暴力、zhengzhi、谣言等内容散布，会造成很大的社会影响。

例子，https://www.huangxxx.com网址代表yellow网址

姓名处输入：【同城xxx，xx姐妹x】加我微信138xxxxxxxx，邀请好友更得好礼，<a href="https://www.huangsxx.com">邀请好友更得好礼</a><!--

实际效果

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XeqrffLgRnnnh9ImV3J4pZWGrKIIFXia91nm5ibNynsoJHBgxiaGlgPWk2uXDJRZQDicVH2icjHo2rCIQ2DN7raadjIEd1DIM2slicGM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XcdudlPdXGFFjwx3N7m8NpvoyhFfs4w6aaudWyLfgYfj9jI202Jsl6ibPxicECVdctgEfA6GKmE3C7ibz1XmFmRaxT4icYlsgyRr7M/640?wx_fmt=png&from=appmsg)

像修改密码，注册用户、换绑手机号、忘记密码这些地方都是高发区。

### 修复方案（后端必做，前端为辅）

#### 1. 白名单过滤（强推荐，优先用）

只允许**中文、字母、数字、下划线**，禁止特殊符号、空格

* 长度：**2–10 字符**（防止超长刷屏）
* 禁止：`!@#$%^&*()_+-=[]{}|;':",./<>?` 及空格、换行

#### 2. 敏感词库拦截（必备）

* 自建或接入**第三方词库**（色情、暴力、辱骂、政治）；
* 后端**全匹配 + 模糊匹配**，匹配到直接拒绝注册 / 修改，返回 “昵称包含违规内容”；

#### 3. 特殊字符转义 / 删除

* 入库前：**移除 HTML/JS 标签**（防 XSS）

#### 4. 前端校验（仅挡小白，不能替代后端）

* 注册页加**正则 + 敏感词**实时校验，不符合直接禁用提交；
* 后端**必须二次校验**（前端可被绕过）。

#### 5. 人工审核 + 日志（合规必备）

* 新注册 / 修改昵称**先审后发**（高危平台）；

文章中提及漏洞已提交漏洞平台并已修复，请勿恶意复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XcTibnY0Ifb6TIAiamAmSSjPMyicwDCetOvMeXNib0OicBcGbicAouvgDgkpwr9aYOicUHvEMb0xiabvjTU8f13sV1TZ3iaPdB635YkToXI/640?wx_fmt=png&from=appmsg)

获取更多工具和实战技巧

关注 小帅安全

如果文章对你有帮助，欢迎一键三连，点赞，关注加转发，后续我会更新更多优质文章。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xd9Nbt3OIoHdW8397TLDEpw56RIGjuvl0yibyiaF509zluBKQnk8pFFa7WiaAEebAyEvyibicu7ddTIkcMWtvODFZJuAbo4HQrOticAw/0?wx_fmt=png)

小帅安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xd9Nbt3OIoHdW8397TLDEpw56RIGjuvl0yibyiaF509zluBKQnk8pFFa7WiaAEebAyEvyibicu7ddTIkcMWtvODFZJuAbo4HQrOticAw/0?wx_fmt=png)

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