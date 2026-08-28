---
title: Yakit与Claude全链路AI渗透
url: https://mp.weixin.qq.com/s/HlIbBc_3eG4xqHebc4AnZQ
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:35:11.504825
---

# Yakit与Claude全链路AI渗透

# Yakit与Claude全链路AI渗透

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于动物园守夜人
，作者owl

![](https://wx.qlogo.cn/mmhead/AYfn0IKjIIMPgcJ2qtzNzuUWLFb3G5PFA0shlo6j8pGTgK1NYAXlOFpxqBrMVRwbpH3FTaEBouU/0)

**动物园守夜人**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XpUnIhOHch9O6VhqhzfUzPyb5AoEmUib4pjrnibiaEy2IQzwmalUWtEppKiaiaTIWryXP26rCt1Qxsn1Ns7XMibn2vg4w5IyTQnTibofVNrTdmc64I/640?wx_fmt=png&from=appmsg)

背景

---

本篇文章是在AI的冲击下，并且已经习惯了AI自动化渗透测试的捡洞日常，但各类APP转发的流量依旧需要的使用古法渗透而变得心有余而力不足。在古法渗透测试里，手机端APP的流量分析(绝大数app)一直是个体力活——抓包、转发流量、人肉看请求、手动测试。效率低，且高度依赖经验。

现在换一种思路：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XpUnIhOHchibibMKzLTGbhxnicZ4l6biaAOEXojNBW4SOIuAuKdr5PRjibTHbegCMzc8hMe2GP1KibNBZYHOnrHskWubmlLMx7ycn7fBueWUlRh6k/640?wx_fmt=png&from=appmsg)

另外声明，本文将不在再介绍APP抓包细节问题、代理问题、及绕过SSL Pinning、hook等细节。

具体实现

1、Yakit设置

设置代理后，APP转发或代理的流量已被yakit抓取，请谅解厚码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XpUnIhOHch8mRFw888IWDSWIjhXUf0xKpAyMDMNTlibsRa09DXkyxWZrzyuJC3dYhiaa2ll80jPasTZR5PeCclH6szwRvcLahOm268tADV5KU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XpUnIhOHchib7f6YFuSwUvAvo16dw0ic4p9gJUxVOJ33zwCj8T4sn7h39H8YQ2HjNveAlcoicBCcCNv0pUZRn079w1FEmJxT1ze3tXl7waOYicg/640?wx_fmt=png&from=appmsg)

流量到了Yakit之后，需要过滤一些数据，当然前提时需要做一个大致梳理，如果使用白名单过滤单一域名、单一规则等，可能会遗漏关联域名跳转的资产，其中跳转的资产同样属于测试范围。过滤规则不过多叙述。

2、Claude抓流量

---

通过Claude 桥接yakit mcp，让claude获取流量数据包，这是整个过程中遇到问题最多的过程，其中包括Context上下文爆炸、MCP权限问题、乱码问题，后面会介绍并解答。

其中claude与yakit工作原理。Yakit实现了MCP Server，Claude Code支持MCP Client。两者对接后，Claude就能直接调用Yakit的能力——查询历史流量、发送请求、读取响应等操作。yakit开启mcp

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XpUnIhOHchibdPDyjiaDhibX0Xvnu6Xle8YoTcTbWdSWXhC3vA0hLibJg9pq0KmVNiblDyjrLrXAmQYAs0j2APLov4kbyp2nuiaic6HRjW9DFxT3iak/640?wx_fmt=png&from=appmsg)

yakit mcp配置详情：

![](https://mmbiz.qpic.cn/mmbiz_png/XpUnIhOHchiclClXLrsAH7z9H4rNibHDZKOLKwGHxINGu0amrGTUAib1XzDQIHqL3hE8xljNsIOT7fNE9icU9yhibvKZWI0NXXvwiaJTU1eaLyeMU/640?wx_fmt=png&from=appmsg)

在Claude Code的MCP设置中添加Yakit的MCP Server：

![](https://mmbiz.qpic.cn/mmbiz_png/XpUnIhOHch9osqHNqW3bD7dicHZ1T6djtWxk9haPO9hBvjFHtibGEGKEt8PFJnibNTfqMch5BW5iccDWmicXarQat2x692yicGzvq17oeqEOZibtJI/640?wx_fmt=png&from=appmsg)

配置成功后，新建会话并调用MCP命令即可查看，这时Claude就能通过MCP工具直接与Yakit交互了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XpUnIhOHchib9oBKDkTFP5H9QQ1nKreXicMVPkTAAc8g9XeX3HPWZl9pb9fCd1N5hIQibz60bic7yWvmN7fcjK2zVUqrt9yk1F3icAC3oQKfLr9E/640?wx_fmt=png&from=appmsg)

3、核心问题

---

1)上下文过长，导致Claude code 输出质量下降。

APP随便点几下，就能产生上百条HTTP请求。每条请求包含完整的Header、Body、Response——一条POST请求的完整内容轻松几KB，100条就是几百KB的纯文本，这样导致上下文被撑爆 ，前面的对话被压缩/丢失，分析逻辑断裂，输出质量暴跌。或直接响应超时

解决方案：

1、固定输出输入文件大小、读取总结每个关联文件作用范围、按照过滤规则，不发散想象

2、让Claude只读取流量的元数据，再通过读取1-2条完整的数据进行测试

3、手动标记yakit关键流量，让Claude辅助分析，即单条流量完整分析

自动化挖洞截图

![](https://mmbiz.qpic.cn/mmbiz_png/XpUnIhOHch8g4BkCxOJ33nGNYZOUm73hzzDrOgMRYBUEo7GXNuSf32ZYaOHPr1owqiadzNiaAMUibibgvylmHKkibn7HDp59Ac4a1F9Pafh9sG84/640?wx_fmt=png&from=appmsg)

2)乱码问题

手机APP的请求体经常有，Protobuf序列化（看起来是乱码）、自定义加密/编码、gzip压缩的Response

解决方案：

先让Yakit做解码（Yakit本身有codec能力），解码后再通过Claude进行分析，避免Claude对于二进制数据读取偏差，无法获取准确数据

3)MCP权限、安全对齐问题

Claude Code默认对MCP工具调用会有询问权限。如果需要批量分析，mcp与正常对话直接放行不同，它每条都需确认。并且有些提问的问题、以及测试的流量会有安全规则问题，所有需要去绕过安全对齐问题，才能正常开始自动化测试。

解决方案：

可以在settings中配置allow规则，对Yakit的的数据进行自定义操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XpUnIhOHch9rsNETKAGC8iaWSuGJFj01abibcVChk3I5v4xOkiaY4z4xvbjo4vBLGibse3XAuVFPAicKSmaFbUrjd4VfCeLTheqCFgvKPJMhLPfw/640?wx_fmt=png&from=appmsg)

至于安全对齐就看各位的手法了；"绕过访问控制"，即可直达目标。

人类创造AI,AI提升人类；

人类再创造\_\_\_,\_\_\_再提升人类。

---

*本文所述技术仅用于合法授权的安全测试。未经授权的网络攻击行为违反法律，后果自负*

###

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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