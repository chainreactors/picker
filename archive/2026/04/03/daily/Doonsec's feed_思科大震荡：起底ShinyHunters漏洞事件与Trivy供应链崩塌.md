---
title: 思科大震荡：起底ShinyHunters漏洞事件与Trivy供应链崩塌
url: https://mp.weixin.qq.com/s/rymmWmyeE6qiKcHiQusgZg
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:11:01.716745
---

# 思科大震荡：起底ShinyHunters漏洞事件与Trivy供应链崩塌

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/0ibcazEYyMzoG1GF3iaD0WeU3TBFicNrUWqvAP9d1b5zgfMzOYtxlggmibqUKib0XrRpjMQDlRY7le28yIPslOOw6VOHUBS66rIvY0Eo6f7jnNWc/0?wx_fmt=jpeg)

# 思科大震荡：起底ShinyHunters漏洞事件与Trivy供应链崩塌

夯磅棱

![]()

在小说阅读器中沉浸阅读

> 2026年初春，一场针对开源容器扫描工具Trivy的供应链攻击，让科技巨头思科蒙受了史上最严重的知识产权失窃之一。攻击者团伙窃取了超过300个私有代码仓库、300万份客户关系管理记录及核心云凭证。这场由安全工具沦陷引发的灾难，折射出当前软件开发链条中的致命弱点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ibcazEYyMzqOEHPuOAtordA2Uk7l2MGx6icSlsOjwWQcdXZ6GK6iaFIw1dMSgmNIzibaOlztcibia7zxdjU7ZjutRwSVNjibv9hQV5LsiaL4J3hM88/640?wx_fmt=png&from=appmsg)

## 01 最后通牒：3月31日的暗网公告

最早的公开信号来自暗网论坛。2026年3月31日，一个叫ShinyHunters的组织更新了他们的博客，声称已经拿到了思科内部环境，包括与UNC6040、Salesforce Aura和公司亚马逊云（AWS）账户相关的所有东西。他们甚至还贴出“收据”——一张思科Crosswork网络控制台在AWS管理界面里的实时截图，里面清楚地罗列着数百个内部存储卷。

ShinyHunters给出了最后期限：2026年4月3日。要么交钱，要么数据公开。

## 02 祸起萧墙：Trivy沦陷始末

真正出事的时间还得往前推。2026年3月19日，攻击者攻陷了开源漏洞扫描工具Trivy在GitHub上的发布流水线（pipeline）。他们在那里面植入了一个恶意的GitHub Action插件。从那一天开始，任何在此期间更新了自身持续集成/持续部署（CI/CD）工作流程的企业，都会在不知不觉中把“云凭证窃取器”拖回自家系统中。

一个检测安全漏洞的工具，自己变成了最大的攻击载体。

根据安全分析，这次攻击的技术团队是一个叫TeamPCP的组织。他们开发并散布了名为“TeamPCP Cloud Stealer”的恶意软件，攻击范围覆盖GitHub、PyPI、NPM和Docker等一系列开发者平台。他们还拿下了LiteLLM的PyPI包以及安全公司Checkmarx的KICS工具。一旦这些“上游水源”被污染，恶意软件就顺着工具与组织之间的信任关系向下蔓延。思科，成了那个最终靶子。

![](https://mmbiz.qpic.cn/mmbiz_png/0ibcazEYyMzqH1E7nFsvwbxoibd7ZW7YmDY64serNta6gictdwwvszuLI9kKCo4p2owDoibiaUOVAl4Zkbbj8hL31OfXvq2npTAAEfNic38xVBibUM/640?wx_fmt=png&from=appmsg)

## 03 损失清单：思科到底丢了什么

思科的损失大体可以分为三类，一个比一个严重。

### 1. Salesforce数据泄露

300万份记录被曝光。这里面很可能包含员工个人身份信息（PII）、合作伙伴数据，甚至一些客户信息。这件事指向了一个问题：思科内部的客户关系管理系统与其云应用程序之间的集成可能存在疏漏。

### 2. AWS权限失守

攻击者获取了思科“少量”AWS账户的密钥。泄露的截图显示，里面有超过100个虚拟存储驱动器，部分存储了数百GB的数据，创建日期一直到2026年3月中旬。这说明攻击者不只是成功“潜入”，他们已经在那里“住”了段时间。

### 3. GitHub代码仓库失窃（最致命）

据媒体BleepingComputer确认，有超过300个思科的私有GitHub仓库被克隆。其中包括：思科AI助手的核心代码、其企业威胁防护产品“AI Defense”背后的算法、以及尚未发布的硬件和软件的蓝图设计方案。

更要命的是，其中一些仓库据称属于思科的客户——包括银行、业务流程外包公司和美国政府机构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ibcazEYyMzr5VxUcII5DIpicmjlnfSyZ224vgPPAEbKJpVHmlwrWQSOiap6ryiax8j0AXsO9tMAAy5nDnLk4Yj1G16X1Tp33ibYspkOlLwfsxh0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0ibcazEYyMzqVqQ0XLiaTicTXKbiaJCxLdxaLweSvJTmO9D8v7ovLTRiaeWXE5se1GWSbWiaB93Wzr2nLgn6Bndz2q2K0ichLtHcM7kZfibcjSgcmgA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0ibcazEYyMzqUEMjqQqlPwXWeicNZicibwT5rF333JOZonIlrmwthBOgP3gGDtGBeP9E9vHic4niaPbNcEfe1qcwZBaPQJ3ww1IJoZVAQicZoo4hJ8/640?wx_fmt=png&from=appmsg)

## 04 为何AI源代码失窃如此棘手

偷防御工具的代码，和偷其他商业软件完全是两码事。AI产品的核心竞争力在于特定的逻辑、训练数据和决策机制。一旦你拿到了思科“AI Defense”的代码，你就能仔细研究它是如何检测威胁的，然后有针对性地设计能绕过它检测的东西。

这不是一个可以简单打个补丁（patch）就能修复的漏洞。这相当于整个底层的逻辑模型都暴露了，想要重建安全体系，几乎得从头再来。

## 05 思科的应对与公众疑问

事发后，思科开始在其开发环境中紧急轮换所有凭证，对疑似被感染的工作站进行擦除和重装系统，并隔离了受影响的AWS账户。这算是标准操作。

但代码是追不回来了。仓库一旦被克隆，就意味着数据已经外流。现在大伙儿更关心几个问题。

* **我的个人信息泄露了吗？**如果你是思科员工，或者使用了他们与Salesforce集成的服务，那么你的名字和邮箱地址有很大概率在那300万条记录里。
* **思科的硬件还安全吗？**这次攻击主要针对开发环境和云服务。目前没有证据表明路由器或交换机的固件（firmware）被动了手脚。但用户未来在更新软件时，需要多留个心眼。
* **什么是供应链攻击？**简单说，就是攻陷一个大家都在用的工具。所有更新这个工具的人，都会亲手把恶意软件请进门。
* **4月3日之后会怎样？**如果思科不妥协，ShinyHunters表示他们会把数据全部公开。
* **政府机构怎么办？**思科为很多美国联邦机构提供网络基础设施。如果这些机构的配置信息也在失窃的代码仓库里，那将是一个没有简单解决方案的长期隐患。

## 06 ShinyHunters：他们是谁？

这个组织从2019年就活跃至今。过去的受害者名单上包括微软、印尼电商Tokopedia和在线阅读平台Wattpad。他们的套路一直没变：窃取海量数据，在BreachForums或自建网站上贴出证据，设下最后期限，然后等待。看起来，这更像是一场为了钱（financial play）的行动，而不是间谍活动——尽管其技术伙伴TeamPCP的动机依然不明。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8eMUeOw7iaF6r78Oo4vichG5ARUN5BVQVibCwGCbEQ7DVUDLdvIgPTqian6D6rojmzfzxXIwE5pJtjvuTDHqAYC1XQ/0?wx_fmt=png)

夯磅棱

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8eMUeOw7iaF6r78Oo4vichG5ARUN5BVQVibCwGCbEQ7DVUDLdvIgPTqian6D6rojmzfzxXIwE5pJtjvuTDHqAYC1XQ/0?wx_fmt=png)

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