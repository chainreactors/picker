---
title: 当钓鱼邮件盯上 AI Agent，风险不止点错链接
url: https://mp.weixin.qq.com/s/Y3AOkKimWLrwLUBhqctTZg
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:40.647041
---

# 当钓鱼邮件盯上 AI Agent，风险不止点错链接

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/NFUgVR5BdTUf7iaiaQqrpmoyHxZ74Ck65ibFyNx0XGEficHn2go33Bibag6VL5NAGYrAMYuKlHW9JNsup8m1dFX0W9TkykMwbxswt4MdwZia67BGQ/0?wx_fmt=jpeg)

# 当钓鱼邮件盯上 AI Agent，风险不止点错链接

原创

塞讯科技
塞讯科技

塞讯科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/D3YzQzbXJGZ6TpQTg6aLIewNELxKrkCmmRjaIWsIQNYpH196pAcAOaJ5p6FqRU3xpOqeibIk7Sh7eFEPbHRlQaw/640?wx_fmt=gif&from=appmsg)

钓鱼邮件不只骗员工，也开始骗 AI Agent了。

更麻烦的是，AI Agent 一旦被骗，就不像点错链接这么简单。

它可能直接去你的邮箱、云盘、CRM 里找资料，再替攻击者把数据发出去。

上周，一个针对 OpenClaw 邮件代理的模拟测试就发现了这个问题，当 AI Agent 接入邮箱、浏览器工具和业务系统后，传统钓鱼攻击的目标，正在从“人”扩展到“会自动执行任务的系统”。

研究人员将一个 AI 邮件代理接入 Gmail、Google Workspace API 和模拟企业数据，并让它处理日常邮件请求。结果显示，在部分场景中，攻击者只需要伪装成同事，提出一个看起来合理又紧急的业务请求，AI Agent 就会执行高风险动作。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/NFUgVR5BdTU9FK3okvyGicNaYoaHOUQg1HXuGOAUJ2HK4zc7HP2yiaZiau1Ie2kbPeicLXtHjqttTkOP1IcDKrekFvMDicXHSfrIDUTEw2BXibt8s/640?wx_fmt=png&from=appmsg)

问题不在链接，而在身份核验

这件事真正值得警惕的地方，不是 AI 没有识别钓鱼链接。

恰恰相反，它在一些技术型钓鱼场景里表现还不错，比如恶意 OAuth 授权、假登录页面、可疑跳转地址，在这些场景里，它都能做出判断，甚至拒绝继续执行。

问题出在另一层：身份核验和业务上下文。

在测试中，攻击者假装成团队成员，请求发送测试环境凭据。AI Agent 查找邮件和数据后，把 AWS IAM 密钥、数据库连接信息、SSH 访问细节发到了外部邮箱。

另一个场景里，攻击者以“在家做季度汇报”为理由，请求导出文件，AI Agent 同样完成了外发动作。即使在更严格的安全配置下，AI Agent 仍然因为“请求看起来紧急、业务上说得通”而跳过了身份确认。

这说明一个很现实的问题：AI Agent 不是更聪明的邮箱插件。它更像一个带权限的数字员工。

它能读内部数据，能理解外部输入，还能把结果发送出去。只要这三件事同时存在，钓鱼攻击就不再只是“诱导点击”，而是可能变成“诱导执行”。

演练对象，不能只看人了

过去我们做钓鱼防护，重点通常放在人身上：员工有没有点击链接、有没有输入账号密码、有没有打开附件。

但 AI Agent 进入业务流程后，演练对象也要变。

你需要验证的不只是“人会不会被骗”，还要验证这几个问题：

AI Agent 收到外部邮件后，能不能访问内部敏感数据？

它能不能代表员工发送邮件、导出文件、调用业务系统？

涉及凭据、客户数据、财务信息、权限变更时，有没有强制人工确认？

来自邮件、IM、网页、工单的任务，是否有不同的信任级别？

如果这些边界没有提前定义，单靠“请谨慎处理邮件”这类提示词是不够的。因为 AI Agent 的默认倾向，是完成任务。攻击者利用的也正是这一点：把恶意请求包装成正常工作，把异常动作藏在“帮同事处理一下”的语境里。

这也是钓鱼演练接下来要变化的地方。

![](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTXhIrzxkAV3ibaibygvC3AxnxbiaxPGSBVZb8BQGd9Nbam6qoucMNHZl7J9A5yOW3cOcvnQjDibOKqYrWKn7kvMcqxFqibK8TYAtlNc/640?wx_fmt=png&from=appmsg)

自动化流程，也要有刹车

做钓鱼演练这几年，我们发现重点其实从来不是“测试谁会点链接”。

是把攻击还原到企业真实业务场景里，用真实诱导方式去验证人会不会被骗、在哪个环节会松动。

热门会议通知、物流提醒、办公系统登录、文件协作请求，这些场景之所以有效，是因为它们本来就像日常工作的一部分。通过发送率、打开率、点击率、提交率，企业能看到风险真正集中在哪里。

这套逻辑放在人身上，是钓鱼演练。放在AI Agent身上，同样成立。

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaZjRayJQVCia5yvdcedgJ5QmBXLTmID64BvtUygia2Z5Vtue9yAzWEmAKvtdXDRqr7Ria5k2KoPbdFhw/640)

过去，验证的是"人会不会被骗"。接下来，企业还需要多问一步：如果同样的请求交给AI Agent处理，它会不会把这件事当成一个正常任务继续执行？

比如，一封"请帮我导出客户清单"的邮件，发给员工，员工可能会迟疑，会问一句"你怎么换邮箱了"。但如果AI Agent被接入了邮箱和业务系统，又缺少明确的操作边界，它可能只会判断：这是一个可以完成的任务。

所以，AI Agent带来的变化，不是钓鱼邮件突然变得更高级，而是被诱导的对象变了。

企业以后做钓鱼防护，不能只看有没有人点击链接、提交账号，还要开始关注：外部请求进入组织后，会不会被自动化流程继续放大；涉及客户数据、凭据、财务信息、权限变更时，是否仍然有人能停下来确认。

现阶段企业能做的，更多是流程上的补救，哪些动作必须有人工确认，给AI Agent的权限划清边界，而不是等工具成熟了再补课。

真正需要被纳入视野的，不只是员工有没有安全意识，也包括自动化流程里有没有刹车。

![](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTUxX3ox1fbbztnt9ZxyH2jxeicrzL4ntw30OBXMjvoTHIpvjTWIrDyxJglRRINy0XibdZBLT2262gIibiaqUGtxdqezRh2fxsl2b4I/640?wx_fmt=png&from=appmsg)

AI Agent 未来会越来越多地进入邮箱、工单、知识库、代码仓库和业务系统。它的价值在于能执行，但风险也来自执行。

所以，钓鱼防护的下一步，不是把所有员工训练成安全专家，也不是指望 AI 天然能判断每一次伪装。

更现实的做法是：把人、系统权限和业务流程一起纳入风险复盘。

> 参考来源
>
> BleepingComputer，OpenClaw AI agent found falling for phishing attacks, spills user data，2026-06-09。(bleepingcomputer.com)
>
> 全球安全研究团队公开实验，Phishing for Lobsters: How We Tricked OpenClaw into Spilling Secrets，2026-06-09。(varonis.com)
>
> CSO Online，Autonomous AI agents duped into leaking sensitive data in phishing test，2026-06-10。(csoonline.com)

**情报驱动运营，AI构建闭环**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/D3YzQzbXJGZc61MO7yLs2nJa9K6ndfaocica0SmniasTB10oR41lBMfPRlT9mtF0ku3GdRO30Mj4UMs0YCw8Y0cQ/640?wx_fmt=other&wxfrom=10005&wx_lazy=1&wx_co=1&randomid=vedmokhe&tp=webp#imgIndex=36)

[![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/NFUgVR5BdTVxwYyVaCFWrgbq32lMaFqricUcud6IFiaTcWibwJy3KLAib6rdJibLSjpvoO9ctqlbibJK8QSBK0pdurZOPA3IdmtLHeqkAzg21smpg/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508606&idx=1&sn=1650fb9825a179cc3c9fb9c706b74881&scene=21#wechat_redirect)

[![](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTXH2ibdfvvLMpTpm11tseXs0Rbm7vxWMWNKTClqyTS3ZQMZp3qenUOpBEoTSBC0BeFk3yibhViaGict9CIo6mX5RiaXP43oKBgNR6k4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508585&idx=1&sn=c8bfe367ef6f538d977d119c4361fb19&scene=21#wechat_redirect)

[![](https://mmecoa.qpic.cn/sz_mmecoa_png/NFUgVR5BdTXPvtkWicDibZ7jJQMCw6uPBADSV82YUwLaHowHzRka565CEDecibe73fY8AuPDH6m5hqkWN7Cuc7BzlcicldQ89b1iaYk6PtWGF29s/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508585&idx=2&sn=1714d56ece7a226c1a5906520c8af678&scene=21#wechat_redirect)

[![]()](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508585&idx=2&sn=1714d56ece7a226c1a5906520c8af678&scene=21#wechat_redirect)

▶▶关注【塞讯科技】，了解AI闭环的实战型安全运营，获取更多产品动态与安全实战资讯

▶▶关注【塞讯威胁情报】，解锁一线视角的深度威胁情报与漏洞分析，获取第一手安全研究内容

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/D3YzQzbXJGZc61MO7yLs2nJa9K6ndfaoNibXIPyqgxsL4PVXQrtQL6FKEsI4OlGzg4Z2d2trjibqfsW9qf8y16PA/0?wx_fmt=png)

塞讯科技

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