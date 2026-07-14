---
title: 研究人员详细介绍了利用 OpenClaw 三个漏洞实现 WhatsApp 到主机攻击链的过程
url: https://mp.weixin.qq.com/s/Zk0WrX1Kaucq8a_PSlrnFQ
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:45:47.177196
---

# 研究人员详细介绍了利用 OpenClaw 三个漏洞实现 WhatsApp 到主机攻击链的过程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs8lRzCxWQmibyOicjQawHE60fVL0pMkMAxXeFia8Qq2FrQiaYH27sTbOZmr9MNcib9byB5J3AafE6zjdYw6DGQ82YgpApBpHpcUKZzc/0?wx_fmt=jpeg)

# 研究人员详细介绍了利用 OpenClaw 三个漏洞实现 WhatsApp 到主机攻击链的过程

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs9tOPMYsTeK7y2N1EBnu1iczXR6QEm2wrKYZ8RrR0bIs2Q5TldxS5h6Qnqq4icCuiad37bmJIfRqjhXaE1L0sj0u9vhUgX02iaHNrg/640?wx_fmt=jpeg&from=appmsg)

关于OpenClaw个人人工智能（AI）助手中现已修补的三个安全漏洞的细节浮出水面，如果成功利用，可能导致凭证盗窃、权限升级以及对主机的任意代码执行。

对这些高严重性漏洞的简要描述如下——

* **GHSA-hjr6-g723-hmfm**

  （CVSS 评分：8.8）——操作系统命令注入和不完整的不允许输入列表漏洞，影响主机执行环境过滤机制，可能导致执行或持久执行超出调用者预授权范围的操作。
* **GHSA-9969-8g9h-rxwm**

  （CVSS 评分：8.8）——操作系统命令注入和不完整的不允许输入列表漏洞，影响主机执行环境过滤机制，可能导致执行或持久执行超出调用者预授权范围的操作。
* **GHSA-575v-8hfq-m3mc**

  （CVSS 评分：8.4）——一个路径遍历和链路跟踪的漏洞，可能允许沙箱绑定挂载绕过父目录的拒绝列表检查，执行本应通过更强授权或策略检查来保护的操作。

这三个缺点均在 OpenClaw 2026.6.6 版本中得到解决。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADsib0wYYhMusMVC512dd6ZNVuQHkauVxjYTpJktrwwzaZ759yubnNURVnYAfWBiaH5MjA33DbQz0ibghzgMy5pdL63CcmxNehlWJqA/640?wx_fmt=jpeg&from=appmsg)

在上周发布的一系列公告中，OpenClaw维护者表示，“实际影响取决于运营商的配置以及低信任度输入是否能达到该路径。”

然而，安全研究员Chinmohan Nayak（被认为发现并报告了这些问题）在与《黑客新闻》分享的一份报告中表示，这些漏洞可以用来通过WhatsApp发送的外部消息触发主机代码执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADsics6uaLgaca7a1QvC27BfmtyQ5t1WscficDhT7yCjgxQmO6AZ3mNEXT3cnFCxFGdialug8Zic6XzU0da9lQwQuKs7qshUqxpDbAjs/640?wx_fmt=jpeg&from=appmsg)

与Cyera今年五月披露的Claw Chain漏洞不同，这些新发现的漏洞不需要攻击者先建立立足点即可提取敏感数据、放置持久后门、获得任意远程代码执行，并协助逃逸到主机。

“'getBlockedReasonForSourcePath（）'检查源路径是否处于阻塞路径之下，”这位研究人员解释了GHSA-575v-8hfq-m3mc。“但它从不反向检查——被阻挡的路径是否位于源（父目录绕过）之下。”

具体来说，绑定挂载拒绝列表会阻挡像“~/.ssh”、“~/.aws”和“~/.gnupg”这样的目录，但允许挂载父目录“/home”或“/var”，从而有效地削弱了单个块的使用。

“将 /home 挂载到你的容器中，你就能读取每个用户的 SSH 密钥、AWS 凭证和 GPG 机密，”Nayak 说。“挂载 /var 就能获得 Docker socket——这意味着完全脱离'沙箱'内部的主机。”

除了将 OpenClaw 更新到最新版本外，建议为所有非主会话启用沙箱模式，将“exec”从面向通道代理的工具允许列表中移除，并监控包含“ext：：”外部协议辅助工具的 git 克隆命令，避免被滥用以运行任意系统命令。

OpenClaw表示：“升级前，将受影响功能限制在可信运营商之间，或在不需要时禁用该功能。”“作为一般的加固措施，保持通道和工具允许列表的范围，避免在互不信任的用户之间共享同一个网关，并在不需要时禁用受影响的功能。”

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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