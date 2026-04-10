---
title: AI Agent沙箱之ANOLISA内置沙箱
url: https://mp.weixin.qq.com/s/NYSUVq8lINtxBFc8hqSyMA
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:40:54.725722
---

# AI Agent沙箱之ANOLISA内置沙箱

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bJmDO3bwicPV0pJBYw5mvm9IesqUmhrh4033PGd65RoOsSXwnuzcOxcWSQ0sjKDnVdOaBReS6jSo64icWpkNf5Na7ywXzlwaIorSJia9KrzED0/0?wx_fmt=jpeg)

# AI Agent沙箱之ANOLISA内置沙箱

原创

瓜田里的猹
瓜田里的猹

不吃猹的瓜

![]()

在小说阅读器中沉浸阅读

今年以来AI Agent在业内掀起了一股浪潮，由于LLM的不可预测性及Agent的完全授权特性，使得我们需要通过沙箱确保Agent运行时处于一个"可控"的状态，作为一个古法安全研究员，笔者对于各类沙箱程序都有着浓厚的研究兴趣，因此打算记录一下对于当前较为知名的各大Agent沙箱进行分析学习的过程，笔者会将整个过程整理为一个系列，希望能对大家有所帮助，当然行文之中有不对之处，也希望各位读者批评指出。

我们首次研究的对象是某厂的ANOLISA内置沙箱，因为正好它近期开源了。从官网上来看，ANOLISA是一款Agent-first 系统，其内置的沙箱也是系统级别的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bJmDO3bwicPWS3OfR8j6vkJ5vCn6yk9uQnvUFK2O3cewhubSV6XPibh3uV81flcDdkoicp518xYwGsyBuJZ6qD96ROJICIicLhqrNibLAltUztmw/640?wx_fmt=png&from=appmsg)

开发一款系统级别的Agent沙箱，这是一个较新的业务场景，笔者对于这样一款产品心中充满了好奇与疑问(首先明确的是，以下思考的业务场景是该Agent-first 系统面向的是tob业务，为企业提供一个Agent运行环境，适配企业所需的各类业务Agent)：

(1)系统如何保证第三方Agent处于沙箱保护中？笔者的考量是这样几种方案：Agent通过某种机制通知系统，系统得知后主动进行沙箱化；系统内置常见的Agent名单，并且提供用户配置接口，系统基于一个list对目标进行沙箱化；提供sdk接口，Agent开发人员基于sdk接口获得沙箱能力；基于渠道控制，认为特定渠道(如Agent商店)获取的才是Agent。

(2)沙箱如何实现适配兼容各类Agent，确保能在相关的业务场景稳定运行？(比如一个通用的Agent和一个适用于CI/CD场景的Agent其权限控制策略必然不一样)对于这个问题，笔者的考量是系统将权限细粒度拆分供Agent选择，Agent默认按最小权限集运行，同时提供各类业务场景权限配置模板供用户自主配置，对于因权限不足无法完成业务的情况LLM决策需补充授予的最小权限，并通知用户自主选择是否授予相关权限，同时告知潜在风险。

接下来我们便带着两个疑问去研究这套系统源码，该项目主要模块如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bJmDO3bwicPX05yFqIAFcSIgliayVEicWItqGyVTy6k6rAsJiauCLic7ic4rOTY2icYJicQajgjuykV9TgQujtzPdSsiaibaOY78bMUcVbhRHxQaovvLM/640?wx_fmt=png&from=appmsg)

其中agent-sec-core部分是保证"安全"的核心模块，该模块中最核心的便是linux-sandbox，linux-sandbox是基于bubblewrap封装的沙箱模块，被"保护"的进程作为命令行参数传递给bubblewrap，同时linux-sandbox根据配置信息生成其他参数传递给bubblewrap，最终bubblewrap拉起被"保护"的进程。有了这些大体的了解后，我们还需要继续细读源码以探究这么2个细节从而回答我们开始的两个疑问：

细节一：linux-sandbox何时以何种方式被唤起

细节二：linux-sandbox以何种方式做了哪些权限控制？是否有做各种业务场景的兼容适配？

细节一

对于细节一，笔者猜测开发者的构想应该是有两种唤起场景(为什么用"猜测"这样一个词呢，后续会提到):

场景一：和claude code类似，通过hooks机制在copilot-shell(这是系统内置的AI Agent)调用run\_shell\_command工具前执行\src\copilot-shell\hooks\sandbox-guard.py，当被执行的tools为非block场景时，便会通过linux-sandbox拉起tools:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bJmDO3bwicPXpd2j0Lblbmx1WTH8s6GFfexvqGkzibkpfKEPZHHHShfeSdoGU7iaQtSDiaWareIehNf0MntrU0bSvOBDzib7hLfEdW85ZqAN4QOw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/bJmDO3bwicPWAQ9mGb1sOcwzUz9L3oJQJmlRTqtwVfOgFKa8sDUPNHibD4f8lvTxg1xkoRzzK9J4mQo7YabibZX3lIicoBqicwh6T4rHRxeDefmk/640?wx_fmt=png&from=appmsg)

场景二：通过skills(\src\agent-sec-core\skill\references\agent-sec-sandbox.md)加载，该skills的description如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bJmDO3bwicPXuVVFemdUYBQrg4wHMdklY1bBMmmxb8y7MEFlRaClibbuSWQnHVBfmiapqXk2zCCsDu2Oww7B3Erk0nbrfwHRaT5OzHESVl5wOk/640?wx_fmt=png&from=appmsg)

skills会通过linux-sandbox拉起目标程序：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bJmDO3bwicPWkuO7icqTm7AuiaZickPeWrUuejImcYZSwwLpXSyjOHianeIeM3I2y9c6jTnhQqpicyqTnvAlpr1iaPr7wFWhc03Qpw3GICv6Y70Fts/640?wx_fmt=png&from=appmsg)

从设计上来说，研发人员似乎想通过description让LLM首先采纳该skills，但该skills文件并不在默认发送的目录里，真正默认发送的\src\agent-sec-core\skill\SKILL.md其中并没有任何对于agent-sec-sandbox.md的引用，所以这个skills并不会生效。

从上述两个场景我们可以知道，唯一能让沙箱起作用的场景只有copilot-shell调用run\_shell\_command工具时才会生效。

细节二

对于细节二，linux-sandbox主要通过seccomp限制系统调用，借助bubblewrap实现命名空间隔离，但seccomp采用的是黑名单模式，只有特定几个网络相关系统调用被限制：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bJmDO3bwicPWErCgQ15Y7MpPw0oibAehM9Mf2icYf45XCMqBxIa4zEMfeT1UWMO3JWMnPLIy3icdxzjKU5s1yh93RBrhnicCGpng7z1WviaqWma3o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/bJmDO3bwicPVyIictoAtU2gaLHRrxFahr4Dm53XJsQiaMEhXNYZXNMrvPoEDYIhPefEjWJyuXtiaTq85UtESTfoLvkkcu9EN3licn7ZynOYXuCpQ/640?wx_fmt=png&from=appmsg)

对于兼容业务场景的考虑，当前似乎只有考虑到某些配置了网络代理的情况，在沙箱中有一个名为allow\_network\_for\_proxy的配置参数，若是设置了该参数，在配置了网络代理的场景下，沙箱会构建这样一条网络通路：沙箱内程序<->local bridge<->host bridge<->网络代理<->互联网。

其中local bridge为沙箱内的转发程序，沙箱通过替换内部网络代理配置，使得内部程序将流量发送给local bridge，local bridge通过unix socket将流量转发给沙箱外部的转发程序 host bridge，最后host bridge将流量转发给真正的代理服务器。

在掌握这些细节后，笔者的感受是这套系统更像是一个为copilot-shell打造的应用级别的agent沙箱，安全保障的生效较为依赖于LLM是否采纳相关skills，缺乏系统级别的兜底机制，也无法保障第三方Agent的"安全"，这可能是由于开源部分更多的是一个框架性质的项目，需要广大社区人员共同参与构建，往里面填充内容。当然项目依旧是一个优秀的框架，笔者在学习时收获甚多，在阅读的过程中，脑子中很多模糊的想法概念也慢慢有了一些初步的轮廓，非常感谢相关组织的开源举动。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LeOoxbgTFQuGziabgfiaGkrPIicYUSzvuDpsrGGdFvXDE1RCv8vATeSOYXVNtqu2MY5yicq1FR2zoVFLWELRYBpx7g/0?wx_fmt=png)

不吃猹的瓜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LeOoxbgTFQuGziabgfiaGkrPIicYUSzvuDpsrGGdFvXDE1RCv8vATeSOYXVNtqu2MY5yicq1FR2zoVFLWELRYBpx7g/0?wx_fmt=png)

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