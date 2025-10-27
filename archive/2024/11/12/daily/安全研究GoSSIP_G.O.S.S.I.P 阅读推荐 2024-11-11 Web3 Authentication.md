---
title: G.O.S.S.I.P 阅读推荐 2024-11-11 Web3 Authentication
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499182&idx=1&sn=9bc5c77f43cc61fad1df125421ecf3a7&chksm=c063d377f7145a6151bf11cfc7d528d6b1803f6f5b289a4d0f834b4359c2b2824fbf596fb762&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-11-12
fetch_date: 2025-10-06T19:19:31.249160
---

# G.O.S.S.I.P 阅读推荐 2024-11-11 Web3 Authentication

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FibfYhrwllDKbhicXhGlJzic0TgMI3A3jAAT6RnMnePfIibsTbW50XX5U9LeEeQr6emMqbs0GHK1ygfA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-11-11 Web3 Authentication

Kailun@SDU

安全研究GoSSIP

今天推荐的论文由山东大学刁文瑞老师课题组和乔治梅森大学张晓宽老师课题组联合完成，题目为**Stealing Trust: Unraveling Blind Message Attacks in Web3 Authentication**。该研究系统性地分析了Web3登录认证流程中的潜在安全风险，提出并验证了一种新的攻击方式——盲消息攻击（Blind Message Attack）。研究成果已发表在ACM CCS 2024会议上，并获得了杰出论文奖（Distinguished Paper Award）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibfYhrwllDKbhicXhGlJzic0leVFkXeKhvMBiaddUdydmpsIUd1T3ekIaEE0oXuefcDL6BbJZEw93rw/640?wx_fmt=png&from=appmsg)

**Web3认证**

Web3认证是一项广泛应用于Web3网站的技术，用于保护用户链下数据的安全。它基于非对称加密技术，服务端（Web3网站）要求客户端（用户和加密钱包）对特定的消息进行签名，然后通过验证消息的签名来完成身份验证。然而，研究发现，现有的Web3认证在设计和实现上存在许多漏洞。例如在消息设计方面，许多消息缺少关键字段（如域名），这使得客户端难以验证消息的来源；在验证环节，一些服务端仅检查签名，而不验证消息本身，从而为攻击者篡改消息提供了机会

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibfYhrwllDKbhicXhGlJzic03djDmTPtUDowzD4YJOMKwSCiaBRJJ8yUfcDCC6qhstT8M5xP5cuswXg/640?wx_fmt=png&from=appmsg)

**盲消息攻击**

文章提出了盲消息攻击（Blind Message Attack），利用Web3认证中的漏洞，恶意网站（Mal Website）在Web3认证过程中让用户签署其他网站（Victim Website）的消息，从而获得目标应用的未授权访问权限。具体来说，当用户访问恶意网站并连接加密钱包时，恶意网站会选取一个受害网站（Step 1-2）。然后，恶意网站假装成用户向受害网站获取一条消息，接着要求用户签署该消息进行Web3认证（Step3-10）。一旦获得用户签名，恶意网站即可利用此签名登录并访问用户在受害网站上的账户（Step11-14）。

盲消息攻击的核心在于用户无法有效辨别消息的来源。基于盲消息攻击，研究进一步提出了两种扩展攻击：**盲多消息攻击**（Blind Multi-Message Attack）和**重放攻击**（Replay Attack）。盲多消息攻击利用多个网站的漏洞，通过一次攻击获得用户在多个网站的账户访问权；而重放攻击则通过回放已获取的签名持续保持对账户的控制。

**Web3AuthChecker检测工具**

为了识别和分析这些漏洞，作者开发了一个动态检测工具Web3AuthChecker，通过与Web3认证相关API的交互，并注入不同的攻击负载来检测潜在的漏洞。具体来说，Web3AuthChecker根据配置的API，自动化进行多轮Web3登录测试，每轮测试都会使用不同的攻击负载，并检测是否登录成功。如果登录成功，则说明Web3登录存在此项漏洞。

**检测结果**

作者从27个知名网站中收集了29个Web3认证API，涵盖NFT市场、社区、游戏等类型。研究结果显示，75.8%的API（共22个）存在盲消息攻击漏洞，另外7个存在盲多消息攻击风险，11个则易遭受重放攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibfYhrwllDKbhicXhGlJzic0nRXMSfgzUiaue9Cs5aycDgmrbJUsL158DMt6LvW22Wia2U2rvNtEg3ag/640?wx_fmt=png&from=appmsg)

**Web3AuthGuard防御工具**

针对盲消息攻击，作者在开源加密钱包MetaMask中实现了用户端防御工具Web3AuthGuard。Web3AuthGuard会自动记录用户签署的消息，将静态字段作为模板与网站的域名一起保存在本地。当用户尝试登录新网站时，Web3AuthGuard会对当前消息与已存模板进行匹配，若消息内容一致但域名不匹配，即可提示用户潜在的攻击风险。Web3AuthGuard的优势在于实现简单、检测及时，能够有效防范由消息设计引发的风险，但其不足之处在于无法抵御服务端层面的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibfYhrwllDKbhicXhGlJzic0sszOssqn59wYNGCWiarzSSfLibSQjibWDP2bXzAxI1loRN1yePdspHv1w/640?wx_fmt=png&from=appmsg)

作者已将其发现的安全问题通报至相关厂商，其中部分厂商已采取措施修复漏洞，并获得了CVE-2023-50053和CVE-2023-50059等安全编号，以及厂商的致谢。

论文链接：https://arxiv.org/pdf/2406.00523

Web3AuthChecker开源代码：

https://github.com/d0scoo1/Web3AuthChecker

Web3AuthGuard开源代码：

https://github.com/d0scoo1/Web3AuthGuard

投稿作者介绍：

（1）闫凯伦，山东大学博士生，导师为刁文瑞教授。他的主要研究方向是区块链和Web3安全。他的成果发表于国际学术会议ACM CCS、WWW。他曾获得山东大学海外学术交流基金赴美国乔治梅森大学访学交流，导师为Xiaokuan Zhang助理教授。他曾获得ACM CCS 杰出论文奖、博士研究生国家奖学金、网安学院学生创新资助计划等。

（2）张晓宽，乔治梅森大学（GMU）计算机科学系助理教授。他的研究兴趣涵盖系统安全和隐私的广泛领域,最近专注于扩展现实（XR）安全、Web3安全和侧信道安全。他的研究成果经常发表在顶级安全会议上，包括ACM CCS、IEEE Security and Privacy、USENIX Security和NDSS。他的论文曾获得ACM CCS杰出论文奖、ACM SIGSOFT杰出论文奖、Springer网络安全奖（最佳实用研究论文），并在2016年、2018年和2022年入围纽约大学网络安全意识周（CSAW）最佳应用安全论文竞赛前10名。

（3）刁文瑞，山东大学网络空间安全学院教授、博士生导师，山东省泰山学者青年专家。2017年博士毕业于香港中文大学，师从张克环教授。主要研究方向为软件与系统安全，特别是移动与物联网安全，关注现实世界系统与设备的安全问题。研究成果发表于IEEE S&P、USENIX Security、ACM CCS、NDSS、ICSE等系统安全与软件工程领域知名国际学术会议。曾获得ACM SIGSAC中国新星奖、ACM CCS杰出论文奖等荣誉。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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