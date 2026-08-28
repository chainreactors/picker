---
title: 一个 Agent，如何操控另一个 Agent
url: https://mp.weixin.qq.com/s/dLgy18cS-zysP9kSTfJkpQ
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:34:34.862005
---

# 一个 Agent，如何操控另一个 Agent

# 一个 Agent，如何操控另一个 Agent

塞讯科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/D3YzQzbXJGZ6TpQTg6aLIewNELxKrkCmmRjaIWsIQNYpH196pAcAOaJ5p6FqRU3xpOqeibIk7Sh7eFEPbHRlQaw/640?wx_fmt=gif&from=appmsg&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=0)

以前做自动化，流程大多比较直白：机器人收集信息，管理员账号执行操作，碰到敏感动作，再由人确认。现在一个任务可能要经过好几个 Agent，真正麻烦的地方也随之出现了：前面接触到的内容，会不会一路传到后面更有权限的 Agent 手里？

比如，一个 Agent 负责读取公开 Issue，另一个 Agent 负责处理代码仓库里的维护任务。前者看到了什么，后者就可能接着处理什么。只要 Issue、代码或任务说明里混进了诱导内容，原本只给维护者使用的操作，就可能被前面的低权限入口带起来。

8 月初，The Register 报道了 Google Agent Development Kit 相关代码仓库中的一条攻击路径。公开 Issue 或 Pull Request 中的内容，可能影响低权限 Agent 的判断，进而让它把任务交给权限更高的维护 Agent。事情的关键，不在于 Agent 突然多了一项权限，而在于它们之间的交接没有被看清楚。

![正文配图 1](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTXRibBsHz0K6XAu3ibumrXEIPZfAloPmYCGicPib0QczNiaxvxSIv3fovnz6LQbB0XQicdA84G3q2JXlo7HgKdFZVKQOXcyC6RIMdRV8/640?wx_fmt=png&from=appmsg)

图｜The Register 关于 Agent-to-Agent exploitation 的报道页面 图源：The Register

![](https://mmbiz.qpic.cn/mmbiz_png/QKbPUqDZvAX7rolb3eXw6wK4W8Rm3wiap3oqzkeGAwMxhicMb2e4GKb56nBna4K7OibRBRgnqiaOMdicnKcq4P0Wib1CaXJYYfL0y9752Dr2uibIQQ/640?from=appmsg)

低权限入口，怎么碰到了高权限动作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Eibbr5sSwJ92bAz4ewn3qBKe4tlZaibwLPvyqxBibz6nrwNw6FYN6AvKhicIpicCUIBnGqe2oxbgMIibQeanZnkUJRTBb4MIZWL7crbtgbn2G69jI/640?from=appmsg)

低权限 Agent 本身可能只能读 Issue、分析代码，或者整理工单。问题在于，它读到的内容会进入上下文，随后又被带给下一个 Agent。后者一旦连接着更多工具和代码仓库，就可能把这段内容当成正常任务继续往下做。

从表面看，前后两个动作都像系统设计好的流程：一个 Agent 负责读取，一个 Agent 负责处理。真正改变方向的内容，可能只藏在一条 Issue、一段代码注释，或者一份 Pull Request 描述里。普通日志往往只记下“任务已转交”，很难直接看出是谁把任务带到了这一步。

所以这类问题和常见的账号越权不完全一样。账号权限没有突然变大，Agent 也不一定绕过了登录和授权。风险更像是藏在交接过程中：什么内容可以传过去，谁有权继续处理，转交之前有没有人或规则看过一眼。

![正文配图 2](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTWlCyvJH7Zxnhaj2tyI0ibnBLtw9T3GXOJJK8t0rOecfAicYOHpq78cT86aJRY1zoT2eCbHQDS5ARV18wvpJpOYmTZowd9HDz2jw/640?wx_fmt=png&from=appmsg)

图｜Google Agent Development Kit Python 开源项目页面 图源：GitHub

![](https://mmbiz.qpic.cn/mmbiz_png/QKbPUqDZvAX7rolb3eXw6wK4W8Rm3wiap3oqzkeGAwMxhicMb2e4GKb56nBna4K7OibRBRgnqiaOMdicnKcq4P0Wib1CaXJYYfL0y9752Dr2uibIQQ/640?from=appmsg)

一个 Token，说明不了 Agent 的身份

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Eibbr5sSwJ92bAz4ewn3qBKe4tlZaibwLPvyqxBibz6nrwNw6FYN6AvKhicIpicCUIBnGqe2oxbgMIibQeanZnkUJRTBb4MIZWL7crbtgbn2G69jI/640?from=appmsg)

给 Agent 配一个 Token，只能知道它拿着什么凭证去访问系统，不能说明它此刻是在替谁办事，也不能说明它应该把事情做到哪一步。

Agent 可以读取代码、分析工单或发起检查，但涉及合并代码、修改流水线、确认检查结果等动作时，仍要回到明确的授权流程。重点不在于把权限一律收紧，而是让每次任务交接都对应到清楚的身份和用途。

人工确认也不能只剩一个“允许”按钮。确认之前，至少要知道请求来自哪个 Agent，前面读过什么内容，准备调用什么工具，以及这次操作会碰到哪些资源。否则人只是替自动化流程补了一下确认，实际发生了什么仍然说不清。

![正文配图 3](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTXs6koiaQ0bVkAUJqgudvbxkqUkVbUZOauuFfziaEBtibFicceqib7zCvbUHLoicUIksX0exDabBFaKKCuLwKUQmycZ0V7rI8Yghwurc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QKbPUqDZvAX7rolb3eXw6wK4W8Rm3wiap3oqzkeGAwMxhicMb2e4GKb56nBna4K7OibRBRgnqiaOMdicnKcq4P0Wib1CaXJYYfL0y9752Dr2uibIQQ/640?from=appmsg)

安全团队得看见任务是怎么走的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Eibbr5sSwJ92bAz4ewn3qBKe4tlZaibwLPvyqxBibz6nrwNw6FYN6AvKhicIpicCUIBnGqe2oxbgMIibQeanZnkUJRTBb4MIZWL7crbtgbn2G69jI/640?from=appmsg)

Agent 会不断接入新的工具和数据源，原来的工作流也会跟着调整。上线时看着没问题，运行一段时间后，权限关系和任务路径很可能已经变了。只看最初那份设计文档，往往对不上现场。

可以拿真实任务做几次检查：给低权限 Agent 一段带有诱导内容的输入，看它会不会把内容交给更高权限的 Agent；让它碰一下高风险工具，看拦截和人工确认有没有真正生效；再翻日志、告警和工单，确认这次调用能不能还原出来。

普通功能测试只关心流程能不能跑通。安全验证还要专门试试那些容易出问题的地方，看看输入、身份、权限、工具调用和告警之间有没有断点。这样复盘时，团队手里有记录可查，不用只靠聊天记录和现场人员回忆。

**复盘时至少要说清楚：**请求从哪里来，哪个 Agent 接到过，拿的是什么身份，调用了什么工具，哪一步被拦住，哪一步还可以继续。

Agent 接得越多，任务交接就越容易绕出新的路径。把这些路径实际跑一遍，看看权限有没有越界、异常动作能不能被发现，出了问题也能更快找到是哪一环出了偏差。对安全团队来说，这比上线时确认一句“配置没问题”更有用。

> 参考来源 1. The Register：Google dev kit spurs first-ever agent-on-agent exploitation 2. GitHub：google/adk-python

---

**情报驱动运营，AI 构建闭环**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/D3YzQzbXJGZc61MO7yLs2nJa9K6ndfaocica0SmniasTB10oR41lBMfPRlT9mtF0ku3GdRO30Mj4UMs0YCw8Y0cQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=vedmokhe&tp=wxpic#imgIndex=36)

[![](https://mmecoa.qpic.cn/sz_mmecoa_png/NFUgVR5BdTWIsXr7YA9xSnWq3XWeOzabPhQ3muYIHovcctAMoztXILlpZDZop8lUUQsQSeA1icBOjPBKqkia4ib6MheGJVsWCZzQcHZpQicK1ibc/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508817&idx=1&sn=f048856a614c8ced0a222fd9f252e937&scene=21#wechat_redirect)

[![](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTXL1NtyNkboOic4Szic4Td9Mk8lhpsMDfQ4XE6bl8iaf6xa9Yia3pSzjCrVDM3P02PQCt84jjK2IcLBzWiaeElfoNvwPQufsibBtwXjw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508817&idx=2&sn=ac36dd4eb6386d3e28033b8152c32357&scene=21#wechat_redirect)

[![](https://mmecoa.qpic.cn/sz_mmecoa_png/NFUgVR5BdTWYb4NY1XXZ87AGvMz45Wdmn7OJZWKDsTWNyx8nOqRuGURsf8WCibW1mZ5iczBqk2tVepDSaUOjh2zpsjqA0FE7oiabItNdPsZrYw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508783&idx=1&sn=25319c50ea4c976a568308d1c7138ebc&scene=21#wechat_redirect)

[![]()](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508783&idx=3&sn=ddfdab183c3341db6e7ae6842daf2b9c&scene=21#wechat_redirect)

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/NFUgVR5BdTUkvIS7LwoyL3iaIedgQLREP25DtDib65BUnWoBfTGzYiaRicl2bzzzEjTf5JNnRFFGrwoobMiaOskfOmVdcibCicIaiaw9Qr1IEwVGWzM/640?wx_fmt=png&from=appmsg&wxfrom=10005&wx_lazy=1&tp=wxpic#imgIndex=11)

▶▶关注【塞讯科技】，了解 AI 闭环的实战型安全运营，获取更多产品动态与安全实战资讯

▶▶关注【塞讯威胁情报】，解锁一线视角的深度威胁情报与漏洞分析，获取第一手安全研究内容

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/D3YzQzbXJGZc61MO7yLs2nJa9K6ndfaoNibXIPyqgxsL4PVXQrtQL6FKEsI4OlGzg4Z2d2trjibqfsW9qf8y16PA/0?wx_fmt=png)

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