---
title: 记一次基于Fastjson反序列化内存马应急指导
url: https://mp.weixin.qq.com/s/X55BW34OuB1AKrbOQE_42A
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:13:17.511152
---

# 记一次基于Fastjson反序列化内存马应急指导

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/16lHuWzRRduSYG777tiacdftOdS4OQwxuhZgQkHXiaQbcjoVuC4dW8dNPnjA05ODkbWWVHRgictia58DkUgGQmHaTvJr7EGhz3zAol0btEGFNBU/0?wx_fmt=jpeg)

# 记一次基于Fastjson反序列化内存马应急指导

原创

阿杰谈技术
阿杰谈技术

轩公子谈技术

![]()

在小说阅读器中沉浸阅读

在遇到应急事情时，应急响应的效率往往取决于日志记录的完整性与分析思路的清晰度。本文以一次 Fastjson 反序列化漏洞导致的内存马攻击事件为例，记录从日志分析到攻击链还原的全过程，希望能为类似场景的处置提供参考。

    攻击路径如下：先通过目录扫描定位后台接口地址，再爆破密码登录后台。由于后台存在 JSON 数据传输，攻击者探测 DNSlog，实现命令回显，随后写入内存马，并对内存马进行检测。

    环境为云主机上搭建的靶场。

    为便于观察数据包，我在 Nginx 默认配置基础上，增加了请求参数、Cookie、XFF 以及请求体中的参数等记录变量。这样在查询日志时，可以更清晰地查看相关内容。

    首先登录系统，由于目标明确，因此先对 Web 日志进行分析。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdvTpdyBgWqMdT46ia1fTCictlbAFqEkWG6u53ZJCplnPjCK1BtF50gicAjicHsofYs6VAcly1SCob5aLgZjpY6KYBAUiaS3iaHERbD1M/640?wx_fmt=png)

    打开日志后，发现均为扫描流量。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRduaNRzejWVTAwu5YXhUZhV8ciamLsyE4cGuBXMFo5Ye35avqkgLqkC2mOcadiaibJnzuhPxOJckRQWiaF58dY0zLdezBibCyAWENTto/640?wx_fmt=png)

    随后进行漏洞探测，扫描 Log4j2 漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdtPhphiasb9jstDhUL3Ifspc2aibkYZ09DZBQPK1VAic9REEFpGcSIvlAibS1NLcUgFpGV05qjmOoDbS68sB7sU1yamJjDice10b5sE/640?wx_fmt=png)

    接着查看日志，发现登录接口存在密码爆破行为。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdswFVicgcaLwoAibtn5QXrF7AVT3hgYyF9uM8hNufvoKJg8OkLFogWVibFzn0BnauCT4USVznTCianfDzFuEWgbJtLvMu63TF2kzqU/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdtQg2dibZdjsSXib5oguiczsibwIo10Wo8ezAXVdtFMX76sIU120JvluOdg6F5s0fYpP2IB9mkZDicd17nNiaLt8JPZWTz963dr0ib324/640?wx_fmt=png)

由于验证码未参与登录认证校验，导致可绕过并实施爆破。

日志中出现登录成功记录，疑似攻击者爆破密码成功并登录。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdtnoSf1t3lO90J3Z9bC9LmNAJvicnzCpUlfjWjGpLibbvEynFcwblaQZwOgR9qPsDwB91E7JUfuJnib58KNycrLLRaiaibb3hcKTwiaw/640?wx_fmt=png)

随后攻击者探测 DNSlog，根据日志记录，DNSlog 成功收到请求。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdtqt16VU8grEPFmy3IdOdiarktWzGxsp0ORLmJsN6QOuhLcembfMTnl8A2hh7oPTYK4mIaztZia6LxNWS6HORwXF5tm20Q5ibiavlM/640?wx_fmt=png)

随后进行 Fastjson 攻击，返回状态码 200，表明攻击成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduBMlgbMJeF2l0hKv7hEfd9SJncShDzHqZ8P57ydicsKH7C1UHVibz62O28jib11Rb7DsTJUSrExyibvB8EYpRNibBc5zywlSyIQ0Sw/640?wx_fmt=png)

其中包含一段以 $BCEL 开头的加密数据，通过 BCEL 编码工具可还原出 Class 字节码内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRds0x84PS76U7sSYDdAXraibc3k9O1yQgzmeiaVpKRkxSUicy7V3sfvGuEobYgmdXrFXRrpJCCvAibn6WkxCmrdBt19eTzprKfiblJLU/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsUgOgbHQ02B38Aruu8YPvUhFTDnSLwetLDickUC59ibrYFz62pVPBFcZ4LmgStyHu19MiahZQcVaBTdwxvoiateY6HbtVNPp8hyDU/640?wx_fmt=png&from=appmsg)

攻击者以 Tomcat 中间件为载体，通过反射调用 org.apache.tomcat.util.buf.ByteChunk，并在请求头中添加 Testecho: whoami 执行命令，命令执行结果直接回显在返回包中。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdvcAzJn2a8XRXDQJP9UzWqT781dmffw8eoLQWYFTRx9JZtNV3SdbuJWuqWUQHja61SJicx585DCItibZ9SrbHVu2psheicPicczdgQ/640?wx_fmt=png)

接着又发现一段疑似 Base64 加密的数据，遂再次进行解码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdvjZvUG4NFWic76LF3uozBEZHFLdL80ljibZALUfJAU7iamlP7BibmHpxYUHo16fp4v9XB5PlL0n3JuFbVBdJ7oK7muSHuFMibShDqA/640?wx_fmt=png)

接着进行内存马写入操作，执行系统命令后确认注入成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtbnM9jVLRs6vvTL50DAasmCP4y1F5RnJM8ara0ADHQHHFCBQlib1c0dvMCic0d86gA0FLVHVfIEDZIXO1yNBNq7koVowQxZlibUA/640?wx_fmt=png)

登录服务器后，进行内存镜像导出。

方法一

执行 jps -l 获取 Java 进程列表

定位目标进程 PID 为 510767

随后使用 jmap 命令导出堆转储

jmap -dump:live,format=b,file=/tmp/dump.hprof 510767。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsvUYpIUgeeenssCurWQcUjSZribXYFszjiaoZibr7zDhAReA4YWGU4WTv23A7aPypBmvmCxHnhgUuwJI6xySiaFxleItKu4g1LKyk/640?wx_fmt=png)

导出完成后，下载本地，将 dump 文件导入 MAT 内存分析工具进行分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtZVqmldb3Lyx0YELwYUsPc3Ibl3o8MQHvQxk6URUUibSAEwh6bDREq7LOa97Wic9UUwbLuKiaQnpynGgICiabDt5A2NicAcjFelWnE/640?wx_fmt=png)

找到搜索按钮，下拉-> java basics -> show as histogram

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduEPCLEgiaV30ePwGS9ThvWr9icuRibdT22bqH4207KoXx4axztbBlJcT4C8k2o7hicUzpcG7ibbGmTiconraVEmgx40rdxjcXIFCeibQ/640?wx_fmt=png)

即可分析内存中运行的所有类名称。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsXpFH6T2biapZaMhdjmRhxXr555ckDRq7eHKLj6ydsOzK3Up5xISiaNfPj97icA3otdE8v0oiakkkOkl9U8B50Qev2ZEEERP8BKE0/640?wx_fmt=png)

点击 java.lang.Object，可列出其所有引用对象，约九千余个。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsekdxf5bIm4vGwWQrNtrRxl1Eo3R4nPsb7Crv0jREJK4VW9xskYc6ExFXzQTyXjgSib2x0LrBN93HtDzPjIoCvwdLZ8f32Cibvc/640?wx_fmt=png)

将这些引用对象全选并复制到文本编辑器中，通过检索 shell、cmd 等恶意关键词进行筛选。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdt08Fvf3jsBbmaVwvtFicgVzFD2p6fSnDD9ngKq66ia4x10RVNZX4Xnr6XrOAJSBDiciaYlRmDMA7KnS7nzoET5RzKeuQre5lUwOnc/640?wx_fmt=png)

最终成功定位到被注入的类及其路由路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsUsFXGibfLQibv15u4JnJ1touzwfEoVdOhTXlK4Yia8x7mJ45yZDUMHibpxhbQlWVbTP2Zb7cyAwv0o6Xwa9FpJcFFzN8OfGcp7mw/640?wx_fmt=png)

方法2

此前借助 AI 编写的一键内存马检测工具，发布三月以来反响良好，具体可跳转至下方文章。

[Java内存马检测工具-跨平台通用](https://mp.weixin.qq.com/s?__biz=MzU3MDg2NDI4OA==&mid=2247491685&idx=1&sn=1f8f78737e67c077eb934bd41bc03c61&scene=21#wechat_redirect)

使用 -h 参数可查看使用说明。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdt7EdQyJQVHsibribwQkkicF6JxcibwkpGfmR1UicQrde8PialR1oUvHJfd4hlAeUVn9Ag9sMbSYQsUtoVmt9ZV71bGWib55CC1sicIHibY/640?wx_fmt=png)

运行后，数秒内即可输出结果，经筛选后结果一目了然。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtAVoEicxW5f9c2E6qyiaCxSZpVZJ56DrlmzLgEtnCW8ic7mmtX9xm1ibGRBdlXSYHWC55xaQiaYFNVVI04oHmpyzpVnVRZyGXo3zTw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdu3IteYbE7T7Iy6m0KdXGEY6NnUbR3w5nkB2259AxHatP2MdmPybY4ypiavXGSFjRyjJ0iaYibSHXd59hFfwZgRpCkpB4ibEFMvfsw/640?wx_fmt=png)

每一次攻击都会在系统中留下痕迹，沿着蛛丝马迹层层推导，便如柯南探案般抽丝剥茧。只要记录未被清除，便可通过细致分析还原真相。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

轩公子谈技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

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