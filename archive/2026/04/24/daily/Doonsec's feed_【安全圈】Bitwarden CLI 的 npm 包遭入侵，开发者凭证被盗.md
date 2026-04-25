---
title: 【安全圈】Bitwarden CLI 的 npm 包遭入侵，开发者凭证被盗
url: https://mp.weixin.qq.com/s/mbTz2usX7BQqOULE8RBoJg
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:32:22.673317
---

# 【安全圈】Bitwarden CLI 的 npm 包遭入侵，开发者凭证被盗

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyECBROE8RfSnqep5EmmnkjFQqKj0sAFjzIqgRpfexv7coF0BvxUHgGdLRiawYYG1dAwb4HzYnJfvDdLDI4ZuTAZa12TYq0L4R4Y/0?wx_fmt=jpeg)

# 【安全圈】Bitwarden CLI 的 npm 包遭入侵，开发者凭证被盗

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

入侵

攻击者将一个含有窃取凭证有效载荷的恶意 @bitwarden/cli 包上传至 npm，致使 Bitwarden CLI 在短时间内遭入侵，且该恶意有效载荷具备传播至其他项目的能力。

据 Socket、JFrog 和 OX Security 报告，这个恶意包以 2026.4.0 版本发布，于美国东部时间 2026 年 4 月 22 日下午 5 点 57 分至 7 点 30 分期间存在，随后被移除。

Bitwarden 证实了这一事件，**并表示此次入侵仅影响其 CLI npm 包在 npm 上的分发渠道，且只有下载了恶意版本的用户受到影响。**

Bitwarden 在一份声明中表示：“调查未发现终端用户保险库数据被访问或面临风险的证据，也未发现生产数据或生产系统遭入侵的情况。问题一经发现，我们立即撤销了受入侵的访问权限，弃用了恶意的 npm 版本，并即刻启动修复措施。该问题仅在有限时间内影响了 CLI 在 npm 上的分发机制，并未影响合法的 Bitwarden CLI 代码库完整性或存储的保险库数据。”

Bitwarden 称已撤销受入侵的访问权限，并弃用了受影响的 CLI npm 版本。

### Bitwarden 供应链攻击详情

据 Socket 分析，威胁行为者似乎利用了 Bitwarden 持续集成 / 持续交付（CI/CD）管道中被入侵的 GitHub Action，将恶意代码注入到 CLI npm 包中。

JFrog 指出，该 npm 包被修改，使得预安装脚本和 CLI 入口点使用了一个名为 bw\_setup.js 的自定义加载器。此加载器会检查 Bun 运行时环境是否存在，若不存在则进行下载。

随后，加载器利用 Bun 运行时启动一个经过混淆的 JavaScript 文件 bw1.js，该文件实则为窃取凭证的恶意软件。

恶意软件一旦执行，便会从受感染系统中收集各类机密信息，包括 npm 令牌、GitHub 身份验证令牌、SSH 密钥，以及亚马逊网络服务（AWS）、微软 Azure 和谷歌云的云凭证。

恶意软件使用 AES - 256 - GCM 对收集到的数据进行加密，并通过在受害者账户下创建公开的 GitHub 仓库来渗出数据，加密后的数据就存储在这些仓库中。

OX Security 表示，这些新建仓库包含字符串 “Shai - Hulud: The Third Coming”，这与此前 npm 供应链攻击渗出被盗数据时采用的类似方法和文本字符串相关。

该恶意软件还具备自我传播能力。OX Security 报告称，它可利用窃取的 npm 凭证，识别受害者能够修改的包，并向其中注入恶意代码。

Socket 还观察到，该有效载荷针对 CI/CD 环境，试图获取可重复使用以扩大攻击范围的机密信息。

此次攻击发生前一天，Checkmarx 披露了另一起供应链事件，涉及其 KICS Docker 镜像、GitHub Actions 和开发者扩展。

虽然尚不清楚攻击者的确切入侵方式，但 Bitwarden 告诉 BleepingComputer，**此次事件与 Checkmarx 供应链攻击相关，受入侵的 Checkmarx 相关开发工具使得攻击者在有限时间内能够滥用 CLI 的 npm 交付路径。**

Socket 向 BleepingComputer 透露，Checkmarx 入侵事件与此次攻击存在重叠的指标。

Socket 告诉 BleepingComputer：“这种关联体现在恶意软件和基础设施层面。在 Bitwarden 事件中，恶意有效载荷使用了与 Checkmarx 事件中相同的 audit.checkmarx [.] cx/v1/telemetry 端点。它还使用了相同的带有种子 0x3039 的\_\_decodeScrambled 混淆例程，并呈现出相同的窃取凭证、基于 GitHub 渗出数据以及供应链传播行为的总体模式。这种重叠并非表面相似，Bitwarden 有效载荷包含与我们在早期恶意软件中看到的相同类型的嵌入式 gzip + base64 组件，包括用于凭证收集和下游滥用的工具。”

这两次攻击活动均与名为 TeamPCP 的威胁行为者有关，该组织此前在大规模的 Trivy 和 LiteLLM 供应链攻击中，也曾针对开发者包发动攻击。

安装了受影响版本的开发者应将其系统和凭证视为已遭入侵，并轮换所有暴露的凭证，尤其是用于 CI/CD 管道、云存储和开发者环境的凭证。

***END***

阅读推荐

[【安全圈】《王者荣耀》惊现逆天bug](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=1&sn=87382d2f57b8f0b6d5e7f3203b830e4d&scene=21#wechat_redirect)

[【安全圈】理想汽车严正声明：系统遭黑客破解、配合走私均为不实信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=2&sn=ef4ca71b65ec892a68ab6e5aeb1ab6df&scene=21#wechat_redirect)

[【安全圈】Claude Mythos 发现 271 个火狐浏览器漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=3&sn=d88245ccf278317f520a1fdb52cbc91b&scene=21#wechat_redirect)

[【安全圈】未受保护的 Perforce 服务器暴露主要组织的敏感数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075943&idx=1&sn=473119abec6a4c6ed316801316b3723b&scene=21#wechat_redirect)

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