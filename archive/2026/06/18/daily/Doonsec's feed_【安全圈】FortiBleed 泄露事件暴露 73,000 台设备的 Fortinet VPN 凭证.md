---
title: 【安全圈】FortiBleed 泄露事件暴露 73,000 台设备的 Fortinet VPN 凭证
url: https://mp.weixin.qq.com/s/pKSqk81RFBiVtMDVvhA8jA
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:01:19.878592
---

# 【安全圈】FortiBleed 泄露事件暴露 73,000 台设备的 Fortinet VPN 凭证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEdw0QknMG3pjxIpfLXFczzI5xnR52EjM7MpxZCIKJ5K3FZfsnx4ZzbgZIfYlYuicWbOrhgD75vOuwMAC7sW9GibficA5dKZ22b4M/0?wx_fmt=jpeg)

# 【安全圈】FortiBleed 泄露事件暴露 73,000 台设备的 Fortinet VPN 凭证

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

泄露

一个名为 "FortiBleed" 的新发现的数据泄露事件，**暴露了全球组织中 73,932 个防火墙 URL 的 Fortinet 和 FortiGate VPN 凭证集合。**

暴露的数据最初由安全研究员 Bob Diachenko 发现，**他表示发现了一台服务器，其中包含看似有效的 Fortinet VPN 凭证，包括用户名、电子邮件地址和明文密码。**

根据 Diachenko 分享的截图和信息，该数据库包含 Chevron、Samsung、Foxconn、Comcast、AT&T、Mercedes-Benz、Toyota等众多企业的条目。

Diachenko 在 LinkedIn 上发帖称：“一场大规模的 Fortinet/FortiGate 暴力破解/主动利用活动被现场捕获。文件中列出了数千个顶级供应商的实例（见截图）。仅这一个文件就包含 21,634 个域名——从 Chevron 到 Fortinet 本身。所有域名都附有通过多种方式获得的、可能有效的 FortiGate 设备密码。”

暴露的数据还包括列出每个组织所属行业、收入和员工数量的注释，很可能用于规划攻击。

Diachenko 后来分享了更多信息，声称该行动由一个讲俄语的多操作者威胁组织进行，该组织收集了 FortiGate SSL VPN 设备的凭证。

根据 Diachenko 的调查，攻击者据称对 320,777 个 FortiGate 目标进行了约 11.6 亿次凭证尝试，并对 163,650 个 Microsoft SQL Server 系统进行了额外的 21 亿次尝试。

他进一步声称，威胁行为者截获了 SSL VPN 身份验证哈希，使用通过 Hashtopolis 管理的 45-GPU 集群进行破解，并利用恢复的凭证横向移动到内部的 Active Directory 环境中。

Diachenko 告诉 BleepingComputer，他在分析了同一服务器上无意中暴露的额外文件后获得了这些细节。

Diachenko 解释说：“他们意外地留下了一个开放的目录，其中包含工件、连接字符串、工具、脚本和数据。分析数据来自他们的 cron 任务、bash 历史记录、日志等。”

该研究员还表示，日本、台湾、越南、伊拉克和土耳其的多个组织已被完全入侵，其中包括一家土耳其的北约国防承包商，据称其机密文件被盗。

威胁情报公司 Hudson Rock 在从 Diachenko 处获得数据集后，已发布了自己的分析报告。该公司将该集合描述为已知最大的受损 Fortinet 相关凭证库之一。

据 Hudson Rock 称，该数据集包含横跨 194 个国家的 73,932 个唯一防火墙 URL，影响 21,632 个唯一域名。

该公司表示，攻击者维护了成功入侵的详细日志，并建立了一个包含几乎所有主要行业领域组织的已验证凭证的数据库。

Hudson Rock 表示出现在数据集中的组织包括 Foxconn、Samsung、Comcast、Siemens、Lenovo、PwC、Accenture、Oracle 以及众多政府机构和关键基础设施运营商。

该公司还发布了统计数据，显示受影响设备数量最多的国家是印度、美国、台湾、墨西哥、土耳其、泰国、哥伦比亚、马来西亚、智利和阿拉伯联合酋长国。

所列公司最常见的行业是电信、IT 服务、金融服务、政府组织、医疗保健提供商、教育机构和制造业。

此次泄露的一个奇怪之处在于，许多暴露的凭证是长而复杂的密码，通常被认为难以破解。

**据信从 Fortinet 配置中提取**

网络安全研究员 Kevin Beaumont 独立审查了部分暴露数据，并告诉 BleepingComputer 其中一些凭证是真实的。

Beaumont 表示：“我已经能够确认部分管理员登录名和密码的真实性——这看起来是一个真实的转储。”

在进一步审查了 Hudson Rock 分享的数据后，Beaumont 发布了更多发现，表明该数据集包含大约 75,000 台 Fortinet 设备的凭证，其中大部分设备仍在线。

据 Beaumont 称，这些数据似乎源自导出的 Fortinet 配置，因为它包含通常只能通过配置才能访问的信息，包括电子邮件地址。

他还表示，受影响的 IP 地址与 2025 年 Belsen Group Fortinet 泄露事件中的 IP 地址不同，进一步表明这是更近期且规模更大的受损设备集合。

Beaumont 表示，他验证了数据集中列出的多个组织正在使用有效的凭证，并观察到许多受影响设备运行着相对较新的 FortiOS 版本。

Beaumont 写道：“数据是真实的。涉及约 75,000 台设备。几乎所有设备仍在线，且都是 Fortinet 设备。这似乎是近期数据。”

根据来自 Shodan 的网络数据，Beaumont 表示此次泄露包含了所有互联网可访问的 Fortinet 防火墙中约一半的数量，并称大多数受影响设备将其 FortiGate 管理界面直接暴露在互联网上。

配置数据的来源仍然未知，尚不清楚是通过先前披露的 Fortinet 漏洞、新发现的漏洞还是其他方法被盗取的。Diachenko、Hudson Rock 和 Beaumont 均未确定配置数据最初是如何获取的。

Hudson Rock 创建了一个免费的 FortiBleed 查询工具，用于检查您的组织是否受到影响。

数据集中的组织应立即轮换与 Fortinet VPN 和管理界面相关的密码，强制启用 MFA，检查网关日志中的可疑活动，并监控暴露的员工凭证。

在发布本文后，Fortinet 告诉 BleepingComputer，其调查表明这些凭证集合是通过先前的事件和暴力破解攻击获得的，与任何新披露的漏洞、入侵或安全公告无关。

Fortinet 告诉 BleepingComputer：“Fortinet 已知悉一起报道的针对 Fortinet 防火墙和 VPN 网关的第三方凭证收集活动。我们致力于保护客户安全，并勤勉且持续地监控威胁行为者的暗网活动。根据我们的分析，所涉及的数据是先前事件数据的再次分享以及暴力破解的凭证，与任何近期事件或公告无关。遵循常规最佳实践的组织，包括按照今年 3 月博客中的指导定期刷新安全凭证，面临来自报道中提及的凭证泄露细节的风险极小。Fortinet 将继续调查这些报告，并将客户安全作为我们的首要任务。”

***END***

阅读推荐

[【安全圈】紧急预警！哪吒监控面板曝 9.1 分高危漏洞，仅需 2 次请求即可免密接管！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077453&idx=1&sn=dcf088b926d0cc3dd13df3ed9b648787&scene=21#wechat_redirect)

[【安全圈】ClickFix 活动通过新加载器和虚假更新诱饵扩大恶意软件投递](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077453&idx=2&sn=1799420aeb8144065e9317cfef8dca8e&scene=21#wechat_redirect)

[【安全圈】Google Vertex AI SDK 漏洞允许攻击者通过存储桶抢占劫持模型上传](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077453&idx=3&sn=8609933c2ae9419836b855460349c8ce&scene=21#wechat_redirect)

[【安全圈】高德地图崩了！！！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077442&idx=1&sn=362b0f0b5d8818cd98df9a84c93c851b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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