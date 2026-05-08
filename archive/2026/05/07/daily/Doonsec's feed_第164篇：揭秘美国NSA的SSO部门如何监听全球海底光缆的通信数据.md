---
title: 第164篇：揭秘美国NSA的SSO部门如何监听全球海底光缆的通信数据
url: https://mp.weixin.qq.com/s/2Sd3WCwOwon9vJ2CJ8M72Q
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:50:36.704814
---

# 第164篇：揭秘美国NSA的SSO部门如何监听全球海底光缆的通信数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2aq4vrpdKL8cqdjq5ghHeCNQVhQv37cyJ6OxlbnB4n9qshMecVl6262vbXBUTgEFwlEw1otMc70pJSnKZ2NvRAyxVu32kYrUdc/0?wx_fmt=jpeg)

# 第164篇：揭秘美国NSA的SSO部门如何监听全球海底光缆的通信数据

原创

abc123info
abc123info

希潭实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcaA8wBFW4icTiaL7ELd8ia04Olh40TBx7CquHZyCicicl4eYJno2y0oZ0H4A/640?wx_fmt=png)

Part1 前言

大家好，我是ABC\_123。去年下半年我连续写了9篇文章详细介绍了美国NSA关于苹果手机的三角测量后门攻击事件，今天我们继续解析美国NSA的重要情报收集部门——SSO（Special Source Operations，特殊资源行动处）。该部门是NSA内部的一个对全球互联网基础设施进行大规模监听的情报收集部门，因斯诺登公布机密文件而广为人知；它通过有线光纤通信链路获取的情报，已经成为美国总统每日简报最重要的信息来源之一，占整体情报来源的60%以上。SSO相关行动通常由NSA下属的NTOC（National Threat Operations Center 国家威胁行动中心）负责统筹协调与运行管理，其任务涵盖全球通信链路接入、流量采集、数据转发以及跨部门情报协同等多个方面。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450Dq1Q8s4COc7InkMO0jIGjiaGho1fcJicpibWB4vzvIM1wAib9TiakVECbIM5S0mHCTTeGJJibWtCe25vXw/640?wx_fmt=jpeg&from=appmsg)

Part2 技术研究过程

如下图所示，Special Source Operations 简称 SSO。配图为一只手握着发光的光纤电缆，象征着该机构负责对全球光纤通信网络的监控，从全球高速通信基础设施中获取信号情报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2brbP9uJeGMfic1pPaIJwPiaW5xGEtTLraR8tE9wuERnlox9VibOFXIG9mn7IKw3Qzaz8CBLY57DO2qzic414pVpJk3TjkMtyhjkg8/640?wx_fmt=png&from=appmsg)

如下图所示，展示了NSA的SSO部门从光纤电缆中获取数据的三种途径：

**1. 企业合作（Corporate）**：即NSA通过与商业通信企业合作获取数据接入能力。这类合作对象通常包括大型电信运营商、互联网服务提供商以及国际骨干网络运营商。图中列出的监听项目包括BLARNEY（基于FISA《外国情报监视法》授权）、FAIRVIEW、STORMBREW、OAKSTAR，以及广为人知的PRISM（棱镜计划）项目和FAA（FISA Amendments Act 《外国情报监视法修正案》）相关体系。这说明美国情报部门不仅依赖技术手段，还大量依托法律授权与企业协作，实现对国际通信流量的持续接入与数据获取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YJ2KSyIc0GcxCGfia1gb5g80vkc3A2lMazzmYH6leOicHYqQHnUJwDnVVVYH0iaD6vxtrlqefwaruBNvUhpRJxqvRDEgApUF6YpM/640?wx_fmt=png&from=appmsg)

**2. 国外合作（Foreign）**：NSA即通过与外国盟友情报机构建立伙伴关系来共享和获取通信情报。图中明确提到WINDSTOP（2nd Party），其中 Second Party 通常是美国情报体系对“五眼联盟”成员的内部称呼，主要包括英国、加拿大、澳大利亚和新西兰等盟国情报机构。这类合作意味着NSA能够通过盟友在不同国家和地区的通信基础设施中获得额外接入点，从而扩大全球监听覆盖范围。

**3. 单边行动（Unilateral）**：指NSA在没有外国政府或相关企业配合、甚至在其不知情的情况下，独立单方面采取的秘密数据截获行动。图中的项目名称已被大量黑色色块遮盖，表明这是更为敏感的单边行动，这凸显了此类行动的绝密性质。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YZbswvxLibcA6hQyh2D3PbVRrIODM3w0NmbKrm6c6z8bsgvEH4QjFnE519icpHGQIgpFSUxg0UWbWiajOUf3YwZjjUushWKkKQjo/640?wx_fmt=png&from=appmsg)

图中展示了一张全球海底光纤通信网络分布图，标注了世界范围内“已铺设（In Place）”与“规划中（Planned）”的海底光缆线路。图中可以看到，跨越大西洋、太平洋、印度洋以及欧洲、中东和东亚等关键区域的海底光缆密集交织，构成了全球互联网与国际通信的核心物理基础设施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2aA81oibth2WsRfibe12LZy1QGzIlPNicFt2A9NqW3iaxcxKiapUWSp5PehAz8IWVgEh8IZ8KXlcQPwBq0M0D93D4iaYnLBBAK1UENY0/640?wx_fmt=png&from=appmsg)

这类海底光纤电缆承载着全球绝大多数跨境互联网流量、国际电话通信、金融数据交换以及政府与企业间的数据传输，因此也成为信号情报（SIGINT）体系最具价值的监控目标之一。上面这张图通过这一全球网络拓扑，强调了NSA实施大规模通信监听与数据获取的基础条件，即对国际骨干通信链路的接入与控制能力。海底光缆不仅决定了全球数据流动的路径，也决定了国家级网络监控与数据采集体系的战略布局重点。

从如下图中的饼状图可以看出，基于国际通信电缆的情报采集（CABLE）占比最高，达到61%，是最主要的信息来源；其次为无线电频率情报（RF），占27%；此外，受保护网络（PROTECTED）与终端设备（ENDPOINT）相关来源分别占6%。这表明美国情报体系在当时高度依赖全球骨干通信链路的数据获取能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZUibkxP6BucVfMiaAXs0XoUJdDNI6RdDPlvNpicwTvMPpnGt06gftCUSyAvTExOpDfjiazMvMjLmtpkqcicuyRicZxYCVfRYLd6eWI0/640?wx_fmt=png&from=appmsg)

左侧条形图则列出了具体贡献情报的项目与行动体系，包括BLARNEY、FAIRVIEW、STORMBREW等大规模通信接入项目，以及TAO（特定入侵行动办公室）所实施的网络入侵行动。此外，还包括“NSA Reporting of GCHQ – DS-200”，即NSA基于英国GCHQ特殊来源收集形成的情报报告体系。整体上，该图反映出美国国家级情报产品主要来源于跨国通信监听、合作伙伴情报共享以及定向网络渗透等多种SIGINT（信号情报）能力的综合支撑。

图中的 2nd Party Accesses 主要涉及与英国情报机构的合作。其中，DS-200被定义为NSA针对英国GCHQ“特殊来源”（special source）情报收集活动所形成的报告体系。DS-200B对应的项目代号为“MUSCULAR”，其核心能力包括具备20 Gbit容量的TURMOIL被动流量采集系统，并由NSA与GCHQ相关团队协同执行任务。MUSCULAR与英国政府通信总部（GCHQ）合作，在雅虎和谷歌的专用服务器之间窃取海量用户数据，可以从 Yahoo Mail、Google Mail 收集数以亿计的用户账户详细信息。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bx3wTm6IFrKHJbLBtkYibib1nucZ2MKcMFl6ib9W0pT3U7DtCdn432GiaxiaAYwN3ZkdjdBcE6cQUGjnBzIeqzEJfroEY100w7Jzuo/640?wx_fmt=png&from=appmsg)

图中详细介绍了MUSCULAR (DS-200B)项目的技术细节。MUSCULAR（DS-200B）项目于2009年7月正式投入运营，部署于英国境内一个大型国际通信接入点。系统初期配置了4台TURMOIL T16设备，每台处理能力为2.5Gb，总数据摄入能力达到10Gb；在2010年5月完成LPT安装后，整体摄入能力进一步提升至20Gb。该项目的任务协同工作由美国与英国GCHQ方面联合开展，其中系统的全面控制与运维责任主要由英方合作伙伴承担。此外，项目已完成IP子网升级，并正在推进VoIP（网络语音通信）相关功能的开发与部署。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YBcF2BRtekicawT0EBAEfLVZxRVZd9rZRUF3vtWsonl7OEB1icCAxF4ST2SxCQvIOkEomYj87TfjT5XQFapvV2M1pqRiciaOoeBWE/640?wx_fmt=png&from=appmsg)

Part3 总结

1.  未完待续，后续继续分享关于美国NSA的武器库介绍，敬请期待。

2.  欢迎大家扫码加入知识星球，一起学习进步。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2YTJ9dImJ9UdewBNa3L56nlB2ficSS9JN6EDSMhauz0eFctKfNKI4Mpjxq8Qru4rJibHibeGdedicuzwde6SU29rngLmSwibXKdtlZU/640?wx_fmt=jpeg&from=appmsg)

知识星球分为以下几个板块：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2ZfryY1bZ0B2l4nLy2wXPgusTHe22zvdrpAibh8lx2jITONhoytjzoHkS7Tf8j6FeurfUTdORxYdNxFcOBy0DHVzPoO3nSfnT5w/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

知识星球的每一个工具都是精心筛选，都附带有实测评价及使用说明。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2ZWpO3Ao3P5kIoiaUiamEfZ7WbYBZzgR5pRgWgFMMRUCjvfuxibNEeIfIftokxL0QtH2rhR903lYbn5xMCUv2QVticXhuX6gico0gXw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

知识星球的每一篇PDF文档、PPT文档都细心整理，配有3到9张关键截图。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2asOuDN4oUOteG005XfBSKeHicvaPJVKv679ywAYOaeicyLNYk2y2JotQS6jnxzPrOPzFmxk6qLzpGN9MxkBxiacjjQ7pV40kUZhg/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

欢迎大家扫码加入知识星球，一起学习进步！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2bgaavcGNZASQ8d78cQDOVlaO8Fgg2w2zTrDNjuECzZ1FQeic1kbY4RPjcbNFCAysuCWJPlp0A22JRl84qz5MOdjhj5tD0ZHfcM/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**OR 2332887682#qq.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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