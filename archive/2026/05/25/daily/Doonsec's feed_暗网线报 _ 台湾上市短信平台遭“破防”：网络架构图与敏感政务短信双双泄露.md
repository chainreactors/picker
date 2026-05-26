---
title: 暗网线报 | 台湾上市短信平台遭“破防”：网络架构图与敏感政务短信双双泄露
url: https://mp.weixin.qq.com/s/FO9kuJgzuIQGkFPI1-RZtg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:05:28.464275
---

# 暗网线报 | 台湾上市短信平台遭“破防”：网络架构图与敏感政务短信双双泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m7SEcCOKaqaaABdNPHTJVxzZVib28OFcu0jHbticJ60pDiauyytn99762dtUD05U7mb0tfT5ictpyPm6wicLbpTR1sYuC3kQs70OU6nanMpXID9c/0?wx_fmt=jpeg)

# 暗网线报 | 台湾上市短信平台遭“破防”：网络架构图与敏感政务短信双双泄露

原创

懒虫零信噪
懒虫零信噪

懒虫零信噪

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在数字化高度发达的今天，一条短信可能承载着验证码、通知，甚至是不为人知的私密对话。然而，当承载这些信息的底层平台被攻破时，后果将不堪设想。

近日，懒虫零信噪威胁情报中心监测到某网络安全论坛出现了一则题为“出售台湾上市公司 (teamplus.tech) 域名控制器账户”的帖子。该帖子不仅详细披露了台湾知名短信服务商 TeamPlus（Every8D）的内部网络架构，更附带了大量疑似通过该平台发送的短信内容样本。令人震惊的是，这些样本中包含了大量涉及台湾地区政府高层、政治人物及敏感政务活动的私人通信记录。

一、核心基础设施“裸奔”：网络架构一览无余

根据泄露帖文显示，攻击者声称已获取了 TeamPlus的域名控制器账户权限，并公开了详细的网络拓扑图。

从图片中可以看到，攻击者对目标网络的渗透程度极深：

公网入口暴露：清晰列出了多个公网 IP 地址，并标注了其用途，包括 HAProxy 公共入口、传统 Web 服务等。

内网细节详尽：内部服务器 IP、数据库端口、监控端口以及具体的业务路由规则（如 every8d.com -> teamplus.tech）均被完整披露。

SSH 管理通道：甚至列出了用于远程管理的 SSH 端口及其对应的后端服务器。

对于一家服务于众多企业和政府机构的短信运营商而言，这种级别的核心架构泄露意味着其整个防御体系在攻击者面前几乎透明，潜在风险极大。

![](https://mmbiz.qpic.cn/mmbiz_png/m7SEcCOKaqYL4Cf7N4DF1gNGU1ViaNKCmuXib25RYibcBwMYmbOkXWOLjVibp8Y66HwPicicfP9KzSxJ71Erm9PnjDiazUBDusiaElRgibNskYOHjw20/640?wx_fmt=png&from=appmsg)

二、短信内容触目惊心：涉及高层政治与政务运作

比技术架构泄露更令人担忧的，是帖文中展示的短信内容样本。这些短信的时间跨度主要集中在 2026 年 1 月至 2 月，内容极其敏感，直接指向台湾地区的政治核心圈层。泄露信息主要涉及以下几个方面：

1.政治人物的私密互动与建议

有短信直接提及“陈宜蓁”、“赖清德”等具体政治人物姓名。内容涉及对政治人物公开表现的私下评价，如建议其“找机会跟‘赖总统’道歉”，以免“以后的路才会有议论”。

还有短信讨论党内事务，提到“绝对不能让谢龙介占便宜”，并涉及选举策略和人际关系的协调，显示出极高的政治敏感度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m7SEcCOKaqZfefxhA8TR5moqibIxCV3ZHf2tDazPQTkJ1VZpgfzp4c48B2qf0vcMsDvw1B6qAM0961FVicyz4CibBsxzFsu4LoJRUEsfQSp7lY/640?wx_fmt=png&from=appmsg)

2.政府政策与行政运作的幕后沟通

样本中出现了关于“300亿元中央扩大养老专案”的讨论，涉及内政部受理申请流程及自愿调查表的填写，这属于典型的政府行政事务沟通。

另有短信提及“财政划分法通过对台南市是好事”，以及要求“行政院编列预算”等内容，反映了地方政府与中央部门之间的利益博弈和政策游说过程。

3.敏感的社会议题与个人健康隐私

部分短信内容涉及极为私人的话题，例如讨论“往生这件事”、“如何让台湾的老人们能够好好的往生”，甚至提及具体的医疗急救情况（如“急性腹膜炎”、“开刀”）。

更有甚者，出现了诸如“生化食物”、“孩童受洗”等带有特定宗教或阴谋论色彩的言论，并请求“总统协助到美国的诚意”，内容荒诞却真实存在于通信记录中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m7SEcCOKaqbpFZicDzebhvTBUSZOc0wIatsnb7uMS8EGwB9rBLBYfiamrCN0udyia3z8jROaaFUZ0icxysDaA1KTola1XsYEHRrrTGZqVTuF8ks/640?wx_fmt=png&from=appmsg)

4.选举动员与派系支持

多条短信内容围绕选举展开，包括“祝委员市长选票冲破赖总统当市长的选系”、“加油8年后更上一层楼，到总统”等明显的政治站队和动员话语。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m7SEcCOKaqZdb3ibY2jaq2HTWkNR9sVpSB6PPcmvOnskeYRrwMh92uI7gDG4Qn71mjmvPozEOUk5PIGlSgxaoutc0zhNy4wOY9ocyP0fOWZg/640?wx_fmt=png&from=appmsg)

三、警钟长鸣：第三方服务商成安全短板

此次事件再次暴露了供应链安全的脆弱性。TeamPlus作为台湾主要的企业级短信服务商，其客户群体必然包含大量政府机关、金融机构及大型企业。

数据汇聚风险：短信平台作为信息流转的枢纽，汇聚了海量的高价值数据。一旦失守，不仅仅是用户隐私泄露，更可能导致国家机密、商业机密乃至政治内幕的外流。

社会工程学隐患：泄露的网络架构图和具体的短信交互模式，为攻击者后续发动更精准的钓鱼攻击、冒充诈骗提供了完美的素材。

免责声明：本文基于暗网监测信息整理，所涉攻击声明及数据细节均源自黑客单方面宣称，尚未获官方证实；内容仅作安全预警参考，不构成事实认定，请以权威通报为准。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vMByMwrmicRJuiblD41h1JXI8fg8OIgE0Doz0GqFMeoGxmZI0q4XfxFmM3YM25Q3mrKy7Up92YOL1XpEI3S3xFgg/0?wx_fmt=png)

懒虫零信噪

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vMByMwrmicRJuiblD41h1JXI8fg8OIgE0Doz0GqFMeoGxmZI0q4XfxFmM3YM25Q3mrKy7Up92YOL1XpEI3S3xFgg/0?wx_fmt=png)

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