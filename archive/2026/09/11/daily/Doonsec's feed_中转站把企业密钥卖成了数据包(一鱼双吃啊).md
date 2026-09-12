---
title: 中转站把企业密钥卖成了数据包(一鱼双吃啊)
url: https://mp.weixin.qq.com/s/svtqINwp4vLr1kYa18nhEw
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:43:52.457863
---

# 中转站把企业密钥卖成了数据包(一鱼双吃啊)

# 中转站把企业密钥卖成了数据包(一鱼双吃啊)

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 为了避免不必要的麻烦，不会提及所有企业的名称。要查随便一搜就可以查到。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAhbvJhaO5UDXnuoCOMoaWPlibtLUcdibZH3iaHByEOGhKhP2wWvfW8djhXQNcNaXrAGhTSqibqIIg93IkLmLbh6BlibUQeTYqA6BAno/640?wx_fmt=webp&from=appmsg)

2026 年 9 月 10 日，安全研究员 Chaofan Shou（之前披露过Claude 代码源代码已通过其 npm 注册表中的 map 文件泄露！） 披露，他从一家中文大模型中转站购买了（花费在万刀级别，也可能是万元级别，不确定，反正是五位数）约 6TB 的 Fable 流量数据，从中找出了 SSH 私钥、VPN 配置、阿里云密钥和 GitLab 令牌。他表示，这些凭据已经过验证，可用于接管 7 家政府机构和 19 家企业。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAjasXm7KsLtngXJGNEibLxwD0F5EeJ1nWoCFWdAS45rffuKzGu1uwllP6qlUFgeYib6M7O7RwBhaWIf0xrd0SyM1RicSDRhcsZANU/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAhhHomALrNyUmj9uRCh5ZbyiclLW0s3WYOf4kiaroC3BLUsbIic6Xjx0sHmzXA2hV1qibIoiaSfZL3SCDZqpjwD63hhESh3FhX2SOew/640?wx_fmt=webp&from=appmsg)

按照他的披露，这批材料以模型流量数据的形式出售，企业的访问凭据混在其中。开发者用来写代码、排查故障的工作记录，到了买家手里，也成了进入企业系统的线索。

中转能看到什么、这些内容能被怎样利用，以及企业能够控制哪些环节。

## 加密连接不代表中转看不到内容

大模型中转服务接收客户端请求，再转发给上游模型。对于需要解析请求、处理返回内容的应用层中转，客户端的加密连接在中转端终止，再由中转建立通往上游的连接。

因此，即使两段连接都使用 HTTPS，中转仍能读取自己处理的请求。加密可以防止传输途中被旁观者读取，却不会让接收请求的服务商看不到内容。

## 密钥不一定是用户亲手贴进去的

编程代理可以读取项目文件、分析错误日志、执行排障命令。为了完成任务，它可能把部分读取结果加入后续模型请求。

假设一份配置文件包含数据库密码，代理读取后将其内容发送给模型，密码便进入了请求。同样的问题也可能出现在环境变量输出、部署脚本和包含认证信息的连接地址中。

所以，防范措施不能只停留在「不要把密码粘贴到聊天框」。还需要限制代理能读取哪些文件，检查工具输出是否包含敏感内容。

## 一份工作记录可能同时包含入口和操作说明

不同凭据能够访问的资源不同。代码托管令牌可能用于读取仓库，云平台密钥可能用于操作存储和计算资源，SSH 私钥可能用于登录服务器。实际影响取决于权限范围、有效期和访问限制。

如果凭据与会话记录一起外流，风险还会增加。记录中可能同时出现主机地址、项目名称、部署步骤和报错信息，帮助接收者判断凭据的用途。

撤销凭据可以阻止它继续被使用，却无法收回已经复制的源码和内部配置。这些材料可能继续暴露系统结构、技术组件和业务关系。

因此，处理此类事件需要分别判断：哪些授权应当撤销，哪些业务信息已经失去控制。只换密码，可能留下后一部分问题。

## 企业可以先把三件事做清楚

第一，查清请求的实际去向。统一管理编程代理和网关配置，确认谁处理请求、是否继续转发，以及数据处理安排能否满足业务要求。

第二，减少进入会话的敏感材料。限制代理读取生产密钥和无关目录，对日志、配置和命令输出进行必要脱敏；需要访问系统时，使用范围受限、有效期较短的凭据。

第三，保留处置能力。如果发现凭据进入不可信渠道，应撤销相关授权，核查异常访问，并评估同时暴露的代码和配置。SSH 私钥需要更换时，还要移除服务端对旧公钥的授权。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgXRic9RtibiacWmphsuSkETtkmkibFTiaicUjRicLp9YGLqc3eOj4WvaqmlalxlwwkJV7vOxueRlwBBFAw7L0z98KTDjXcIn75WpLib4g/0?wx_fmt=png)

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