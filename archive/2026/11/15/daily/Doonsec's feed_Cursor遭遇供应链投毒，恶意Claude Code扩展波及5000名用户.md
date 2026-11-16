---
title: Cursor遭遇供应链投毒，恶意Claude Code扩展波及5000名用户
url: https://mp.weixin.qq.com/s/BpHUFepq1BJK6_BloqGwYQ
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:44:08.203394
---

# Cursor遭遇供应链投毒，恶意Claude Code扩展波及5000名用户

# Cursor遭遇供应链投毒，恶意Claude Code扩展波及5000名用户

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3Wf5Vvnu1Fibdao9l2qL2yV1Q3a9KnPERn0ov9KYsTKLQvPsrWPxZxoFYy5lfricH6uAkuC7MQiaovQ4wuRaH58Udg3kAPwkFmDY/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2ODwC0SU6vHJRCfy7YLhPY71G95A3t2uc7ZiaNLoSWLdq8qv9sMB2yqhmAlvDG5CgUAfdS5QxKLIwGaaDYKGibx4owiaYqUk4DD4/640?wx_fmt=png&from=appmsg)

Cursor将10月发生的安全事件溯源至Fireworks AI泄露的一枚访问密钥。攻击者利用该密钥窃取历史coding agent记录，找到更多凭证，最终在Cursor的市场缓存中植入了带后门的Claude Code扩展。Cursor在11月13日发布的更新中，将此次供应商侧密钥泄露与10月29日发现的恶意包事件关联起来。

这枚被盗密钥是Cursor颁发给Fireworks的，仅拥有共享存储桶的只读权限。存储桶内保存了少量coding agent运行轨迹，大部分生成于2025年，均来自非隐私模式下的会话——Cursor原本有权使用这些会话数据进行模型训练。部分记录中残留了未被清理的凭证信息。

Cursor表示，仅不到0.05%的用户存在coding agent运行轨迹泄露，不到0.01%的客户出现API凭证泄露。上述数据对应事件的不同影响范围，不能等同于安装了恶意软件的用户数量。

攻击者利用记录中找到的凭证，访问了Cursor使用的部分软件服务。泄露的信息包括归档的非生产环境源代码仓库、少量客服记录与邮件、使用指标、联系方式、对话摘要，以及部分用户发送给客服的凭证。

10月29日，攻击者利用从泄露内部数据中窃取的一枚凭证，将篡改后的Claude Code包直接上传至Cursor VS Code扩展市场的缓存中。Cursor表示，这些恶意包并非Anthropic发布，Anthropic的产品本身不存在漏洞，Open VSX平台也从未托管过该恶意软件。这一结论更正了此前报道中称恶意包出现在Open VSX上的错误信息。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2WNskt62lqvNxh3xsxEzCB1TG4y3UZcRpIpXzMiboocjVjDuiatc4teibApwyRibxHicbIQNSv6To9dKwlNpkIO0GESqRhuSThQcoU/640?wx_fmt=png&from=appmsg)

Part01

Claude Code后门加载即执行

潜在波及5000名用户

根据Cursor发布的事件更新，在约11小时的时间窗口内，最多有5000名请求特定缓存版本的用户可能收到恶意构建包。受影响的包为适用于Windows和macOS平台的Anthropic.claude-code 2.1.312与2.1.313版本。上述数字为潜在分发规模，并不代表已有5000台设备成功建立后门连接。

Cyber Security News的初步技术分析显示，恶意包中注入了JavaScript代码，扩展加载时就会自动执行，无需用户发起Claude对话。代码会收集主机信息，添加名为svc-telemetry的SSH密钥，并尝试向134[.]209[.]82[.]225建立反向SSH隧道。初始上传的数据仅包含环境变量名称，不涉及变量值。

后续针对Cursor确认信息的跟进分析显示，恶意代码会通过macOS LaunchAgent实现持久化，在Windows系统下则通过计划任务实现持久化，若权限不足则退化为通过启动文件夹驻留。恶意脚本会每隔约60秒重试一次连接。Cursor表示，由于代码存在编写错误，且多数主机缺少管理员权限，攻击者未能在大部分设备上完成远程登录，但这并未阻止其他恶意修改操作或主机数据收集行为。

Part02

Fireworks AI泄露范围更广

多家客户受独立影响

Fireworks AI发布的泄露报告显示，此次事件的暴露范围更广，涉及账户与账单记录、部分数据集以及不完整的模型权重。Fireworks在11月的安全更新中还提到，攻击者通过托管开发机的云服务商实现了访问。这些更广泛的泄露情况并不代表所有客户都丢失了相同类型的数据。

目前已有其他客户披露了各自受影响的情况。Notion披露的影响涉及Insights功能使用的AI聊天记录，覆盖不到1%的工作区，Notion自身系统并未被攻破。Uber披露的影响涉及数千名美国司机的个人信息，包括驾照详情。这两家企业的泄露事件均与Cursor的扩展投毒攻击无关联。

Cursor已将推理流量从Fireworks平台切走，撤销了Fireworks的供应商访问权限，轮换了所有内部凭证，重建了扩展市场，并扩大了密钥扫描范围与网络访问限制。为防范潜在风险，Cursor还重新部署了生产基础设施。Cursor认为目前事件已得到控制，最后一次观测到攻击者活动是在11月1日，相关行为已被拦截。隐私模式下的提示词、客户代码仓库以及Cursor官方更新均未受影响。

受影响的开发者应按照Cursor发布的清理指引操作。仅删除扩展可能会残留SSH密钥与启动脚本。Cursor建议用户检查端点痕迹，隔离受影响设备，清除持久化机制，在可信设备上轮换所有可访问的凭证，并评估是否需要重建环境。

参考来源：

Cursor Reveals How a Leaked Fireworks AI Key Led to a Backdoored Claude Code Extension

https://cybersecuritynews.com/cursor-data-breach/

### **推荐阅读** [![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Wh05Z0rN9nVQTjUXnyXs6uYnM9oo6THt2FhXmXzcuMkHbceiatCbhz8mR2zDd0yicfXLAnN2mwPzVRz1C0ibPQ0ocMnNt16QAkg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651349303&idx=1&sn=86458815b0d0b880c32e19864a449a98&scene=21#wechat_redirect) **电报讨论** ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg) ![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png) ![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过