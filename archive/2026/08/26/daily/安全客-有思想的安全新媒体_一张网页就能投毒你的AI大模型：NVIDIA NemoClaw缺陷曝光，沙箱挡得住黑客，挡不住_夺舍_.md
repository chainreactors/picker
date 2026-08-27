---
title: 一张网页就能投毒你的AI大模型：NVIDIA NemoClaw缺陷曝光，沙箱挡得住黑客，挡不住"夺舍"
url: https://www.anquanke.com/post/id/316021
source: 安全客-有思想的安全新媒体
date: 2026-08-26
fetch_date: 2026-08-27T12:12:32.825019
---

# 一张网页就能投毒你的AI大模型：NVIDIA NemoClaw缺陷曝光，沙箱挡得住黑客，挡不住"夺舍"

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 一张网页就能投毒你的AI大模型：NVIDIA NemoClaw缺陷曝光，沙箱挡得住黑客，挡不住"夺舍"

阅读量**42819**

发布时间 : 2026-08-26 10:28:49

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

Oasis Security披露NVIDIA NemoClaw缺陷：恶意网页可通过DNS重绑定接管本地Ollama，向AI模型植入隐藏指令，用户毫无感知。

你让AI助手帮你读一份文件，它乖乖照做，顺便把你的API密钥发了出去——这不是科幻片的桥段。Oasis Security刚披露了一个让人后背发凉的攻击链：受害者只是打开了一张普通网页，本地跑的AI大模型就被悄悄”夺舍”了，从此每一轮对话都带着攻击者埋下的隐藏指令，而你和AI客户端都完全察觉不到。

# **一、攻击链还原：浏览器是怎么变成跳板的**

这次的靶子是NVIDIA NemoClaw——英伟达开源的AI Agent参考运行栈，不少团队拿它在本地沙箱里跑OpenClaw这类智能体，后端用Ollama做本地推理。

问题出在一个看似无害的配置上：在Windows宿主机路径下，NemoClaw会用OLLAMA\_HOST=0.0.0.0:11434启动Ollama，把模型API绑到了所有网卡上。这个API本身没有鉴权，只靠两层中间件拦浏览器请求。可一旦绑定地址不是127.0.0.1，Host头校验直接跳过，CORS又把攻击者域名的请求当成同源放行。

最后的点睛之笔是DNS重绑定：攻击者的域名先解析到自己的服务器，再解析到127.0.0.1，浏览器全程以为自己在跟”同一个网站”聊天。你点开一张网页的功夫，页面里的脚本就已经摸到了你本地的Ollama API。这个手法不新鲜——Ollama在2024年就修过类似问题（CVE-2024-28224），但NemoClaw的配置把老坑又挖开了。

# **二、真正的杀招：聊天模板投毒**

拿到API访问权后，攻击者干的事比直接偷数据阴得多：通过/api/create接口写入一个改过的Go模板。

这个模板管的是消息数组渲染成原始文本的过程。被动过手脚的版本，会在推理时往每一条系统消息后面偷偷追加攻击者写的指令。从此，这个模型的每一轮对话、每一个新会话，都带着这颗雷——就算Agent换了自己的系统提示词也没用。

Oasis Security的原话很扎心：”客户端无法检测也无法阻止——模板是模型层面的属性，对API调用方完全不可见。”更扎心的是另一句：”沙箱保护了终端，但接管Agent，就接管了它所有的访问权限和工具。”你给AI配的代码执行、文件读写、内网访问权限，全成了攻击者的嫁妆。

# **三、现状与自查：没有CVE，没有补丁，怎么防**

这次披露最让人不舒服的一点是：没有CVE编号、没有影响版本范围、没有修复版本。跑NemoClaw的团队现在连”我在不在射程内”都没法直接确认。好消息是截至8月25日还没有在野利用报告；The Hacker News复查代码发现，8月10日的v0.0.106版本加了绑定探测，代理遇到非回环绑定的Ollama会拒绝启动——但这个检查恰好覆盖不到设了0.0.0.0绑定的Windows宿主机路径，也可以被环境变量手动关掉。

给正在用本地AI Agent栈的团队几条实操建议：第一，立刻检查Ollama的OLLAMA\_HOST配置，绑回127.0.0.1，别图省事用0.0.0.0；第二，不要把11434端口暴露给局域网或公网；第三，关注NemoClaw仓库更新，别手动设置NEMOCLAW\_OLLAMA\_PROXY\_SKIP\_BIND\_PROBE=1绕过绑定检查；第四，有条件的给模型文件和聊天模板做完整性校验，启动时比对哈希。

# **四、写在最后**

这已经是Oasis Security第三次用类似路径拿下本地AI Agent了——2月劫持本地OpenClaw，8月初投毒Paperclip，现在轮到了NemoClaw。套路一脉相承：浏览器是跳板，本地API是缺口，模型模板是持久化阵地。

整个行业都在忙着给AI Agent接工具、放权限，却很少有人问一句：这个跑在本地、握着你全部钥匙的”员工”，它的脑子会不会被别人悄悄换掉？AI落地的第一课不是提示词工程，是先想清楚——你的模型，还是你的模型吗？

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/316021](/post/id/316021)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **52**

* 粉丝
* **3**

### TA的文章

* ##### [Redis补丁被绕过了：最新RCE的PoC已全网公开，你的缓存服务器还在裸奔吗](/post/id/316025)

  2026-08-27 11:00:32
* ##### [一张网页就能投毒你的AI大模型：NVIDIA NemoClaw缺陷曝光，沙箱挡得住黑客，挡不住"夺舍"](/post/id/316021)

  2026-08-26 10:28:49
* ##### [Zoom高危漏洞曝光：你的屏幕共享正在被黑客远程接管](/post/id/316016)

  2026-08-25 11:04:42
* ##### [2.45亿次下载的Rust crate被投毒：编译时恶意代码自动执行，朝鲜黑客又出手了](/post/id/316013)

  2026-08-24 14:12:38
* ##### [保镖成了内鬼：微软Defender再曝零日漏洞，普通账户一键提权SYSTEM，补丁还没用](/post/id/316003)

  2026-08-21 11:29:21

### 相关文章

* ##### [Zoom高危漏洞曝光：你的屏幕共享正在被黑客远程接管](/post/id/316016)

  2026-08-25 11:04:42
* ##### [2.45亿次下载的Rust crate被投毒：编译时恶意代码自动执行，朝鲜黑客又出手了](/post/id/316013)

  2026-08-24 14:12:38
* ##### [三维架构、四种盈利、五重赋能：纳米Work企业版渠道生态正式起航](/post/id/315983)

  2026-08-18 13:33:11
* ##### [一张恶意SIM卡，就能接管你的充电桩：1981年的"祖传命令"正在物联网里复活](/post/id/315962)

  2026-08-13 12:24:33
* ##### [Linux服务器注意了：勒索病毒已经盯上你，国家正式预警](/post/id/315959)

  2026-08-13 12:22:14
* ##### [这次真不是吓你：搞勒索的，一个判了16年，一个要蹲32年](/post/id/315956)

  2026-08-11 13:04:35
* ##### [1755枚比特币一夜蒸发：1.1亿美元"冷存储"神话，碎在一个不随机的随机数上](/post/id/315945)

  2026-08-10 18:04:25

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)