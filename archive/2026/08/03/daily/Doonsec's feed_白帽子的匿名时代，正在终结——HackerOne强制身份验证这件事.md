---
title: 白帽子的匿名时代，正在终结——HackerOne强制身份验证这件事
url: https://mp.weixin.qq.com/s/AYEkWUTpDxNQn3XDDvwu2A
source: Doonsec's feed
date: 2026-08-03
fetch_date: 2026-08-04T04:59:06.194969
---

# 白帽子的匿名时代，正在终结——HackerOne强制身份验证这件事

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH2UeACyduOy9U3icbuEPVk6s044JlXKJ31yKH8oEuzI1ibxrSw9OrNb3ragHzNh6IfgJ8Y0scHMDTCg5PsIYaSp9bIbpWl0uoaew/0?wx_fmt=jpeg)

# 白帽子的匿名时代，正在终结——HackerOne强制身份验证这件事

安全客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如果你是一名安全研究员，过去几年大概率注册过 HackerOne。注册的时候你不需要填真实姓名，不需要上传身份证，甚至不需要绑定手机号——一个邮箱，一个昵称，一个 PGP 密钥，就够了。你提交漏洞，企业确认，你拿赏金，平台抽成。整个链条里，没人知道你是谁，你在哪个国家，你今年几岁。你靠漏洞质量说话。

这套匿名体系运行了十多年，是漏洞赏金经济的地基之一。现在，地基要动一动了。

01

强制身份验证：不是建议，是硬门槛

8月1日，HackerOne 正式确认：所有黑客在向任何 Bug Bounty Program提交漏洞报告之前，必须先完成身份验证。没有验证，你的报告发不出去；没有验证，你拿不到一分钱赏金。

不是部分项目，是所有项目。不是可选项，是强制。

但有一个例外：Vulnerability Disclosure Program（VDP），也就是不涉及金钱奖励的漏洞披露项目，仍然对未验证的研究者开放。说白了——你要拿钱，就得露脸；你不拿钱，只做贡献，平台暂时不卡你。

这个区分很关键，后面会展开。

02

验证流程：把身份证交给一家爱沙尼亚公司

具体怎么验证？HackerOne 的流程是这样的：

进入个人资料页面，点击"ID Verification"标签，先签署一份叫 Rules of Engagement 的文件——里面是关于"验证后你会获得更高权限，所以要遵守额外条款"的规定。勾选同意后，点击"Start Verification"，然后把整个验证过程交给第三方公司 Veriff。

Veriff 是爱沙尼亚的身份验证服务商，做的事情很简单：要求你用摄像头实时拍摄一张政府签发的有效身份证件，在大多数情况下还需要拍一张实时自拍，和证件照片做比对。

注意几个硬限制：不能用 VPN，不能用流量匿名工具，不能用越狱设备，不能用 SDK 模拟器，不能开 Apple Private Relay。用了任何一个，自动拒绝。只接受实体证件，扫描件和电子证件不行。护照、国民身份证、居留证、驾照都可以，但具体接受哪些证件因国家而异。

验证提交后，通常 3 个工作日内通过邮件通知结果。如果进入审核队列，最长 48 小时。之后你才能开始提交漏洞。

而且不是验一次就终身有效。身份验证需要每年续一次，到期前大约一个月会提醒你重新验证。过期了？赏金项目的提交权限没了，个人资料上的绿色验证标志也没了。

03

H1 Clear：比普通验证更狠的"安检"

HackerOne 还有一个更严格的层级，叫 H1 Clear。这个项目在普通身份验证的基础上，额外加了一层犯罪背景调查，面向的是经过筛选的少数精英黑客，通常对接企业的内部安全项目。

但注意——就算你已经是 Clear 状态，每年一次的普通身份验证续期仍然不能落下。过期了，Clear 特权也会受影响。

换句话说，HackerOne 的身份验证体系是分层的：普通验证是"你证明你是你"，Clear 是"你还得证明你干净"。但对于大多数靠赏金吃饭的研究员来说，普通验证这道门槛已经足够改变游戏规则了。

04

为什么被拒？大部分是自己坑自己

Veriff 的自动审核系统拒绝申请，原因往往不是身份造假，而是一些技术细节没做好：

证件正面文字模糊、机读区看不清、条形码缺失或被裁掉、证件已过期、用了复印件而不是原件拍摄。这些都是最常见的拒绝原因。

HackerOne 的建议也很直白：光线要好，摘掉眼镜和头饰，用 Chrome 或 Safari 浏览器。听起来像是在教你拍证件照，但确实能省去不少被拒重来的麻烦。

05

这件事真正值得关注的，不是流程，是信号

流程本身不算复杂。真正值得聊的是这背后的信号。

HackerOne 是全球最大的漏洞赏金平台之一，连接着全球数万名白帽黑客和众多世界 500 强企业。它选择在这个时间点强制身份验证，官方说法是"满足监管要求"。监管什么？反洗钱、了解你的客户，以及越来越多的司法管辖区对跨境资金流动的审查要求。

当你向 HackerOne 提交一个漏洞，企业付赏金给你，这笔钱经过 HackerOne 的平台流转——在监管眼里，这就是一笔跨境支付。平台有义务知道钱打给了谁。

这其实不是 HackerOne 的原创动作。竞争对手 Bugcrowd 早就在赏金项目中推行类似的验证要求，Intigriti 等欧洲平台也在跟进。整个行业都在往"去匿名化"的方向走，HackerOne 只是把时间线拉得更紧了。

06

匿名文化的消亡：有人欢迎，有人警觉

安全研究员圈子对这件事的反应是分裂的。

欢迎的人认为，身份验证能筛掉低质量报告、恶意提交和投机者，提升平台的整体质量。企业也更愿意向"验明正身"的研究员开放更高奖金的项目——H1 Clear 的存在就是证明。

但警觉的人有自己的理由。

白帽社区一直有一种"meritocracy"传统——你行不行，看你提的漏洞，不看你是谁。匿名让很多身处高压地区、网络审查严格国家的研究员能安全地参与全球安全生态。身份验证一旦成为硬门槛，这些人怎么办？

更现实的问题是：Veriff 要求上传政府签发的身份证件，拍摄实时自拍，这些数据存在哪里？保存多久？谁能访问？HackerOne 说验证由 Veriff 处理，但数据流转的透明度并不高。对于一个以"保护信息安全"为使命的社区来说，把自己的身份信息交给第三方，多少有点讽刺。

07

对普通研究员的实际影响

如果你是已经在 HackerOne 上活跃、有稳定赏金收入的研究员，这个变化的影响是有限的——花点时间走一遍验证流程，每年续一次，不算大事。

但如果你是新入行的、还没拿到第一笔赏金的，或者在隐私敏感地区的研究员，这道门槛可能会让你重新考虑：值不值得为了一笔可能拿不到的赏金，把身份证件交给一个海外平台。

还有一个实操层面的影响：验证结果最长 48 小时、通知最长 3 个工作日。如果你发现了一个高危漏洞，想第一时间提交抢首发——对不起，没验证过的账号连报告都发不出去。这意味着，对于想参与"赏金竞赛"的研究员来说，提前完成验证变成了基本准备动作，不能再等发现了漏洞再临时搞。

08

写在最后

HackerOne 强制身份验证，表面上是平台政策调整，实质上是整个漏洞赏金生态在合规化路上迈出的一步。匿名白帽子的黄金时代，可能真的在收尾。

这不一定是坏事——更规范的平台意味着更可持续的赏金经济、更高的企业信任度、更大的项目金额。但代价是，社区里那种"任何人都可以靠技术匿名参与"的开放精神，正在被一点一点置换掉。

以后想靠漏洞赚钱，光有技术不够了，你还得愿意证明"你是谁"。

这个问题留给每一位正在做安全研究的人：你愿意为了参与这个生态，把自己的真实身份交出去吗？

信息来源：https://cybersecuritynews.com

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/o0buL62hK7M8RnVz7mqRVDRkqm2sJeT2icM4WyR7kMkHpLVaicR3tJ4gr5kIb4zje9lXgd5PuOw42Z5KtathltcQ/640?from=appmsg)

**END**

推荐阅读

[纳米Work企业版正式启动全国各级渠道城市合伙人招募](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790316&idx=1&sn=6773dfc0acbbadb37727c65e062943cf&scene=21#wechat_redirect)

2026-08-01

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH2vAtj7RDNefiaW3RkYzibELXMIX6qiaTKiaMHjwFwQsNb03ADKbr7uRicZTG910fEHV2UrB40dY8cbK3Y3Lyib48QRiczbnrSQzVNKr0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790316&idx=1&sn=6773dfc0acbbadb37727c65e062943cf&scene=21#wechat_redirect)

[Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790311&idx=1&sn=a773abac86f33c0a66bb3bba70e39a8c&scene=21#wechat_redirect)

2026-07-31

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH06nOCLudiamA24SmoxydWjShIJonsyLIyZKkLJnM0B1lk95micJkibwNjcbY0iagZq9taMw8Yq00OATQ00ewoox6af7kJwSODT79Y/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790311&idx=1&sn=a773abac86f33c0a66bb3bba70e39a8c&scene=21#wechat_redirect)

[新一轮银狐攻击\_管控终端再成控制工具](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790305&idx=1&sn=59d3131871f875930282f72a5fc17ed2&scene=21#wechat_redirect)

2026-07-30

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH1YsSmllGfNbYKRF8ia7TNdTwicuXzRrALA0ic5iaiauRmxy06z62Fmx0TIJ60PYXepzwORyiahTBXCrkNQsCibPFzkbvQAPMEWbR1hkk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790305&idx=1&sn=59d3131871f875930282f72a5fc17ed2&scene=21#wechat_redirect)

[OpenAI开源Codex Security CLI：用于发现、验证和修复安全漏洞](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790293&idx=1&sn=3dafe8f68a7666a50c6edd26cfbe7932&scene=21#wechat_redirect)

2026-07-29

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH26Kib6ibyib3ia8icicIPOshAWDvBPBQA1veicBNbsXzcicvMdThKHuljsuqBwmcY79W9tmSnNia2UoOWrYGRG6OHwzWIVnfKGlvicGdicVs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790293&idx=1&sn=3dafe8f68a7666a50c6edd26cfbe7932&scene=21#wechat_redirect)

[OpenAI 的模型刚黑了 Hugging Face，微软就拿出了"反黑"模型](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790281&idx=1&sn=291dced849b77c06190f144d1f5165c9&scene=21#wechat_redirect)

2026-07-28

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH0rvn9NQEXCQAch9HNzdRBQrlqwT3uLG9zjZVUtiaJ9trrFnL8Lw9M8T2hTuePLPU2hsNLDRR9Qu69TApaiaQf1yC0hUsPy1nNWY/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790281&idx=1&sn=291dced849b77c06190f144d1f5165c9&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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