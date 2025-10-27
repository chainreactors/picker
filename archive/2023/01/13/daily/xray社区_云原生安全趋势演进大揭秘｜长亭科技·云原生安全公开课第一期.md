---
title: 云原生安全趋势演进大揭秘｜长亭科技·云原生安全公开课第一期
url: https://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247494949&idx=1&sn=72a3c3ece72df8ea82d70f30a1460012&chksm=e92cf986de5b70905331cf6a82819a28ab14180fdf8a05b34ab3272cd71abc1bd8937e3bb8da&scene=58&subscene=0#rd
source: xray社区
date: 2023-01-13
fetch_date: 2025-10-04T03:45:42.338889
---

# 云原生安全趋势演进大揭秘｜长亭科技·云原生安全公开课第一期

![cover_image]()

# 云原生安全趋势演进大揭秘｜长亭科技·云原生安全公开课第一期

CT Stack 安全社区

以下文章来源于长亭百川云平台
，作者D\_infinite

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM56bWiaa6ic0ZJu9qGoOKP5dobAVNOxcfxgial7YI8dpTLwg/0)

**长亭百川云平台**
.

百川云平台（Rivers）是长亭面向企业开放的在线安全产品服务，包含了多个安全产品，如问脉容器安全产品，关山WebShell检测产品，牧云主机安全产品，以及其他第三方安全公司提供的安全产品等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibfwvBLa5EzL0vvLwibgM2ibMpBeNg2vJZ2ax9QzorCqabpaZjoe0BBfGw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibEKMFic4OOtXB3ZMQRmxXQicYReA1nWtshBPq53TYGjy3xmLXO2VuibP4Q/640?wx_fmt=png)

讲师介绍

D\_infinite

长亭科技安全研究员，擅长云安全/主机安全/Web安全/Java安全，多个开源项目贡献者：

▪  veinmind-tools

▪  log4j2-vaccine

---

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibuwumhQTSNgOvPbc2PHYiafjoicwg7jvibHOFYicOicawX3M83jFl9nrcyvQ/640?wx_fmt=png)
> ❝
>
> Hello 大家好，首先来做个自我介绍，我叫陈靖远，来自长亭科技，既从事安全研发的工作也担任 PM 产品经理。今天的分享大致分为三个部分：云原生的发展历程，云原生的安全治理，以及安全产品介绍。
>
> ❞

---

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibHsqRqh7WRsbwQfRnJMcRabGBOibtpGI1BB9S0qmXian6TNRjj47bgzQg/640?wx_fmt=png)关于发展历程这一部分，主要会从云原生历史的角度出发进行讲述，以及从历史中我们学习到了什么。第二部分安全治理，主要就目前的形势，我们应该怎样做好安全治理这方面入手。这两大点都是从一个宏观的视角出发，在之后的云原生安全公开课中会更多从微观角度去分析，包括：问脉底层的 SDK 到底怎么实现；我们做一些比较难的技术挑战时，是怎么解决问题的······大家可以关注一下之后的课程。

---

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibCY85ibek1cB4pnLEq7Pic5M1osnvliarAmUUqHf9Pbw5qctUOicM387exg/640?wx_fmt=png)那么我们来到第一部分“云原生的发展历程”，说到云原生，大家会想到什么东西呢？有的人可能会想到 K8s ，有的人可能会想到 Docker。但其实最早的都不是这两个东西。最早是来源于 Linux 内核所提供的两个特性：一个叫 Cgroup 、一个叫 Namespace。这是 Linux 内核很早就提供了的功能：Cgroup 支持对于进程资源的使用限制，Namespace 提供了对于进程资源的隔离限制。在 Kernel 层我们发现 Cgroup 做了限制，比如你想占用多少 CPU 资源、内存资源，都是由 Cgroup 决定的。而 Cgroup 上是由 Namespace 限制的，对进程信息、网络信息等不同力度等资源做了限制。这两个核心的能力，就是我们所谓的容器化，是最基础的基石。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhib8sa30pwhNVM9biciaDU7A7Vbco25A2I43QWBjeUDNTPovnUFWyIM9PZg/640?wx_fmt=png)2009年的时候就诞生了一个项目，叫 Linux Container，俗称 LXC。这个项目就是最早的沙盒化应用，它允许使用者以一个虚拟化的方式去运行自己的应用。但有的同学可能会比较疑惑，“为什么2009年就有 LXC 了，可是我感觉云原生是最近几年才火起来的。”我觉得这是一个很好的问题，为什么 LXC 在2009年的时候一直没有得到广泛的推广或应用呢？原因很简单，因为 LXC 它只用了 Cgroup 和 Namespace ，就导致了我在一台机器上用 LXC 跑起来了某个 application，在另外一台机器上可能跑不起来了。因为一个 application 可能会存在一些 libc 的依赖，在动态编译的情况下必须跟另外一台机器保持一致才能用这个 LXC。所以 LXC 在2009年推出来之后没有实现大范围推广。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhib5ZB7Y48w6A7ZB0T3E1HibbWsDdy18P09U9oJncXbOdpibiciaPaj5ycVww/640?wx_fmt=png)直到2014年 Docker 的横空出世，它在 Github 上面开源 ，改变了云原生领域的发展历程。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibacSuKYUvm0X236rYF8WFvC7nbxzP0D7OdEGTJdojHMYiaicedvpMZAgA/640?wx_fmt=png)Docker 本质上和当时的其他容器化项目没有特别大的区别，但是却做了一个非常巧妙的微创新，那就是将操作系统的文件系统也打包到应用当中。这个微创新使得所有基于 Docker 打包的 application，真正做到了 build once, run everywhere。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhib1qUu1w4AcASic0Wtlqp8eib2Ix35tnFdib7NExEkgOelDg84y7geCmK7g/640?wx_fmt=png)然而 Docker 这个项目，即使收获了大量的社区关注，依然被外界认为仅仅只是玩具。原因在于，Docker 本身并没有办法帮助开发者实现大规模场景下的应用部署。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibibYsQUED64xBHcHFgHmJciceYq9fcEB4iaZZFicblTSzWT2tEWrIAODWYQ/640?wx_fmt=png)很明显，刚才那个问题很多厂商都注意到了，于是纷纷推出自家的集群产品。其中以两个产品最为突出，一个是 Google 开源的 Kubernetes，一个是 Docker 开源的 Docker Swarm。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibELuQZNlC8U6KFCT6z2My2rPngPO1r6icXVUl9A2czQq9nQxXQ8lXibkw/640?wx_fmt=png)这场战争的胜负也显而易见，目前 Kubernetes 以统治级的地位成为了开源集群的佼佼者。上图为 Kubernetes 的架构，不难看出，对于容器运行时的管理，使得大规模的容器化部署变成了可能。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibFom5xMJIIxiaicgXicOM5kVibSxRp3icezaKDwAFtFNSQRBJ7R3amNrUFfQ/640?wx_fmt=png)随着云原生技术的发展，越来越多的项目被盖章到 CNCF 当中，整个社区生态也逐渐丰富，渐渐呈现出百家争鸣的态势。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhib8pFibibxodCSjBSfLtHWglHnfsLOyFSILBRGjrQgZG7cSNvWhg4pJs2g/640?wx_fmt=png)云原生普及的根本在于生产力的提高，而提高生产力的核心在于 “标准化”。镜像使得应用标准化，容器又可以运行标准化的镜像，集群又可以调度标准化的容器。这一系列流程降低了开发的成本，从而提高了生产效率。在肉眼可见的未来当中，基础设施的技术栈只会越来越统一，最终形成业界通用的标准。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibgm3s2TCNcGSYcCC6IXdmPzG9iaSsfV1l11JCCJD2bH5YpwdY56EtGSw/640?wx_fmt=png)2017年，正式发布了开放容器标准 (OCI)。这个标准的公布也意味着，容器的全生命周期都被纳入到标准化轨道当中。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibjdN7wLNMOnfZ9tQyPcIoz73dWJY8mG6ZUnJgVYlHwiaZY6SGjibJKrgg/640?wx_fmt=png)

---

接下来是第二部分“安全治理”，为什么讲这一部分呢？我个人认为云原生是一个比较新兴技术。现在很多甲方企业也好，乙方企业也好，在推进云原生过程当中，还是处于一个相当进行时的状态。不是所有业务线都能够完全涌入到这套生态里面。所以不管是甲方还是乙方的安全部门，我们要去做标准化的产品，都会发现这中间有很多很多的坑和问题。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibotw4tnJ5mTaG5H1xDtWWpxyrNbL45Sxtymwju8aknznhCXO5Qu2ibcg/640?wx_fmt=png)

1. 针对每一个问题都用一个特定的方式去解决，比如：针对镜像就拿一个服务器专门去扫描镜像；针对容器就给每一个机器单独部署一个 agent；针对仓库就拿一个专门的工具扫描远程仓库镜像。
2. 通过产品去解决云原生安全的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhiblnAB0lHfibQPeKcAxL0F6cucbpnAfWiafYjABoPwa1zricKtjNHdTqOKQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhib6qAQoGydOgYF0YY9tTr0r2G0DapZKVLdMA1WK1tGdtcTFmyWA0CUzw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibhEH78v5xlk2kA4H2VicsJPMH0Q6rfBzoIUYbLqZkZ25Dvq5MBQKeKiaQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibu3ABQMq8XrqtYkKOy0Q6QKEa5zcRhMPKzE88kIbt4W9qyMETHTQKMg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibnhKbw4Q3U3CvqbSMHQuLnq95FfZQfC6G32xhMhjvLs1nicT9t6fq4WA/640?wx_fmt=png)

我们往左边看，可以看到最上面是集群相关的，集群的话它可能会关联到镜像、IAC，以及集群本身的组件，比如说 api server。针对 api server 我们可以做审计分析，举个例子，现在我们用一个叫 CDK 的工具去创建一个后门，那我们可以用 api server 的 audit 去发现有人用 CDK 去创建这么一个后门，这个更多是抛砖引玉。又比如说 IAC，它本身也是个对象，包含了 dockerfile、docker-compose、K8s、nomad 等等。针对 IAC 做配置检测，有没有将一些我们认为敏感的目录挂载进去。以及最后是基础设施，我个人认为检测视角更多的需要放到主机层面的检测视角，以上就是关于安全治理的一些想法。

---

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibQ0Of8bzaoDO2tf8xdD1ZemNY01s2nicicQ79CNN65m6aWDrQxYNvOKuQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibopOlmVvHn8rD9xONhR2F3hHfQNpdAeicR2CMJwuUx85R9bE6ScoLSng/640?wx_fmt=png)

这次分享是从一个宏观的角度，大致跟大家介绍和讨论了云原生安全趋势的演进，在今后的分享中，我们会从微观角度讲一些技术方面细节的干货！希望营造云原生社区良好的讨论氛围，让我们一起学习，共同进步！大家可以持续追更，敬请期待！我们下期见！

---

> ❝
>
> 需要直播录屏、PPT的小伙伴请私信微信公众号“长亭百川云平台”： **「第一期直播录屏」**、**「第一期PPT」**即可获取。
>
> ❞

**扫码添加小助手，一起学习、共同进步！**

![](https://mmbiz.qpic.cn/mmbiz_png/NtPFQib0CNabiaAiaCKn4Gj60LeAJYhtWJsgBAUnxFUV0dsqtlkOuhibUOglQKeXslRqkB3PNKbSH5BJHDLK0azkSw/640?wx_fmt=png)

若有收获，就点个赞吧～

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

CT Stack 安全社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

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