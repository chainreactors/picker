---
title: 如何实现「红牛自由」— 一次 LFI 漏洞挖掘的完整复盘
url: https://mp.weixin.qq.com/s/dE2v9q3BdmvRDBme_R5sSg
source: Doonsec's feed
date: 2026-08-11
fetch_date: 2026-08-12T04:00:47.891454
---

# 如何实现「红牛自由」— 一次 LFI 漏洞挖掘的完整复盘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GVAVvm742xPHXn5kqlSDN4sxTE30Cjrk4lfrxpesFOWnxIX4RvTImKMFCicTwF0iaTVfYiaicUwCJiajyXqrzAt1jHEibN3SFLjribCCDWjvYNxpa8/0?wx_fmt=jpeg)

# 如何实现「红牛自由」— 一次 LFI 漏洞挖掘的完整复盘

Ms08067安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文投稿作者：遂宁市安居区  李勇

## 一、缘起

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xODwENnu1of3PkZ2KYrrV0rdPCYhLvEftmIUh9erzcwh5u3aK7fa1CwIx5osj70YL1mibwC02nsJZjlamANqhYV3gewYI4ay5IM/640?wx_fmt=png)

图：当年提交的其中一个 LFI 报告截图（一个较为少见的路径穿越场景）

最后的奖励是十大件红牛，被搞安全的朋友戏称实现了「红牛自由」。

这是四年前的一个故事。那时在 YouTube 上看到几个世界上非常出名的赏金猎人站在一大堆红牛后面拍照—那是他们参加红牛赏金计划所获得的奖励。

在赏金猎人的圈子里，「实现XX自由」是一种带点自嘲又带点荣誉感的说法：用一次高质量的漏洞挖掘，换来对应品牌的实物奖励。这背后其实也是对一套测试方法论是否成熟的检验—奖励只是结果，真正值得复盘的是从「毫无头绪」到「找到突破口」之间走过的路径。

![](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xOTygpIibJZo0cDqvwsNuakaeTbvYgMJ92hAgrFSyC4LpxK5aciau1cRafyU7cibPvWoQb69UicW7YDCBZwXDUTiaX1n2A2n7x8kUjI/640?wx_fmt=png)

感觉很酷，于是我想：我是否也能做到？能否获得红牛？

可想到这样的赏金计划对全球安全界是公开的，参与测试的各路大神很多，难度极大是肯定的，没有简单的果子。但是又想，测试一下又如何？即使没有得到奖品，也能提高自己的测试能力。

当然，在这件事情过后，也体会到了赏金猎人在思维方式上的一次突破。

## 二、关于目标：红牛的赏金计划

查了一下，红牛公司在欧洲赏金平台 Intigriti 上有一个计划，也才知道红牛公司的总部是在欧洲和泰国，而不在中国。找到漏洞后，奖品是发红牛，对于爱熬夜的安全爱好者来说，挺合适的。

Intigriti 是欧洲主要的众测/赏金平台之一，企业发布的计划通常会明确限定资产范围（scope），排除掉市场活动类的临时落地页，聚焦在核心业务系统上。在正式动手测试之前，我做的第一件事是把 scope 说明完整读了两遍，把明确排除的资产、允许的测试方式（是否允许自动化扫描、并发限制、是否允许对生产环境做写操作等）整理成一份清单，避免因为触碰规则导致提交被拒，甚至被平台警告——这一步很多新手容易跳过，但对赏金猎人来说，规则本身也是「攻击面」的一部分，理解规则的边界，往往决定了你能测试到多深。

## 三、资产测绘与信息收集

Web 方面有很多域名，我先锁定了主域名 \*.redbull.com，先走一波标准化的侦查程序。

子域名枚举我用的是被动加主动结合的方式：被动层面，通过证书透明度日志、DNS历史解析记录，以及第三方聚合接口去拉取尽可能全的子域名清单；主动层面，再用字典爆破和基于已知子域的词根组合（permutation）做补充—大型品牌的子域名命名往往有一定规律，比如dev-、staging-、api-v2-这类前缀，值得针对性生成字典去撞。拿到清单后统一丢进批量探活，标注状态码、页面标题、技术栈指纹，方便后面按「看起来像内部系统」「看起来像老旧遗留系统」这类特征做优先级排序。子域名劫持方面，主要是核对 CNAME 记录指向的第三方服务是否处于「未认领」状态，原理并不复杂，但排查起来需要耐心，得一个个核对。

我的方法是这样的，在推特上看到的方法。我用的情报收集方法是下面如图中的方法，是推特上找到的方法。可以自己添加修改代码，加入自己常用的工具，把收集的流程定义为一个函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GVAVvm742xP85Juuh6Pc1Uoic7A60zXQOeVVJ6XP800ae2rY8nes0L9pO1JMFXp13ialAUmB5PqibEiaE0hmAUNjibrFD1AbYbVmYiaRiaG4ltGiafI/640?wx_fmt=jpeg)

图：在 Twitter 上找到并改编的信息收集流程

最后收集全部子域名的 JavaScript 文件，使用工具查找JavaScript里面的敏感端点、文件路径和 API 路径。

JS 文件分析这一块，光靠肉眼翻代码效率太低。做法是批量抓取所有可达的 .js 文件后，用正则和现成工具组合去提取里面出现的接口路径、参数名，以及看起来像内部使用的关键字（比如 admin、internal、debug，或是带版本号的 v1/v2 路径），再手动挑出高置信度的目标逐条验证。这一步的产出不是漏洞本身，而是「接下来该重点测试什么」的候选清单——对于大型资产而言，信息收集阶段花的时间，往往比实际测试漏洞的时间还长，这也是很多新手容易低估的地方。

## 四、常规漏洞测试与瓶颈

手动分析了很长时间，查找了XSS、IDOR、SQL注入、重定向等很多常规型漏洞，没有发现任何安全漏洞，陷入困顿之中。

这里想多说一句方法论上的取舍。广度覆盖（把常见漏洞类型都过一遍）适合快速摸底，但对于一个已经被大量赏金猎人反复测试过的成熟资产，常规漏洞往往早就被扫过、修过，继续用同样的思路很难有产出。真正的突破点通常来自「深度」：选定一个漏洞类型，把它的成因、变种、绕过手法研究透，再回头系统性地覆盖目标。

期间经常查阅国外赏金猎人的博客文章，他们强调要深入某一个漏洞。于是有个想法：深入测试某个漏洞。我想到专注测试 LFI 漏洞。

这也是为什么后来选择放弃广撒网，转而专注 LFI（本地文件包含/路径穿越类漏洞）：一方面，LFI的根因相对固定——服务端在拼接或解析文件路径时，对用户可控输入的过滤或规范化不彻底；另一方面，它的绕过手法有很强的「可复用性」，一旦手上有一套成熟的思路和payload体系，可以直接迁移到不同资产上去验证，边际成本会越来越低。

把GitHub上面全部有关的LFI payload下载到本地Ubuntu VPS，去重、合并为一个巨大的 payload 文件。

我从多个攻击面对 redbull 各个子域名发起了测试：

GET 层面：除了常规的自动化测试外，还做了 GET 参数的拆分后组合、GET 型隐藏参数的测试。

POST 层面：重点测试了 Web 系统需要手动交互后生成的新参数。

Cookie 层面：在可能的参数位置也做了 LFI 测试。

跑了几天后，没有任何发现，精疲力尽了，休息，想放弃。

搞过赏金猎人的人一定知道，这种情况是常态，因为这不是「拿现成 payload 打一下就中」的漏洞利用，很多时候需要针对目标的特点去构建一套方法论和工具，这个难度是极大的。

读了很多赏金猎人写的文章，有很多感悟。Facebook赏金计划里的白帽第一人 Youssef Sammouda 在推特上有这样的感悟：

让我们在这里谈谈逻辑，如果您正在使用您在某处找到的工具/技巧/提示发现错误。下一步是什么？如果该工具被弃用怎么办？如果技术发生变化怎么办？如果 sec 团队开始使用他们的 S|DAST 工具这样做怎么办？最重要的是，如果没有人再分享怎么办？

这段话对我触动很大：依赖别人现成的工具和payload，只能解决「已经被公开过」的那部分问题；一旦目标的防护策略更新，或者社区里不再有人分享新的思路，这种依赖就会失效。真正可持续的能力，是自己有能力去分析、去构造、去验证——哪怕慢，也是自己的。

## 五、转向：构建自己的 LFI Payload 体系

那段时间也一直在关注路径穿越型的漏洞，直接在子域名的根目录下和子目录路径下测试 payload。

想到：如何找到或者创造一种全新的 LFI payload，可行吗？

一周后的某一天，看到一篇国外黑客写的 blog，其中这样写到：

我做的第一件事就是尝试跳出API调用，以便加载其他路径，我通过发送以下有效负载来实现这一点：

```
/bff/proxy/orchestra/get-user/..%2f/bff/proxy/orchestra/get-user/..;//bff/proxy/orchestra/get-user/..//bff/proxy/orchestra/get-user/..%00//bff/proxy/orchestra/get-user/..%0d//bff/proxy/orchestra/get-user/..%5c/bff/proxy/orchestra/get-user/..\\/bff/proxy/orchestra/get-user/..%ff//bff/proxy/orchestra/get-user/%2e%2e%2f/bff/proxy/orchestra/get-user/.%2e//bff/proxy/orchestra/get-user/%3f /bff/proxy/orchestra/get-user/%26/bff/proxy/orchestra/get-user/%23 (#)
```

看到后面的payload，感觉到很奇妙的感觉。我心中有个想法：如果把这些 payload 用来测试路径型的 LFI，效果会如何？

这些变体本质上都是在利用同一个矛盾：不同处理层（CDN、反向代理、Web 框架路由、文件系统）对「路径分隔符」和「特殊字符」的解析规则并不完全一致。比如某一层会把百分号编码后的字符解码还原成 ../，而过滤逻辑只匹配了字面量的 ../，就会出现「过滤了明文形式，却漏掉了编码后的等价形式」的情况；再比如某些框架在处理路径时会对相邻的分隔符做合并或折叠，也可能被特殊构造的分隔符组合绕过。当时想的是：既然单个绕过手法已经被广泛测试过，那能不能把「层与层之间解析差异」这个思路，转化成一批可以批量验证的 payload，而不是依赖手工一个个去试。

我手动添加这样的 payload.txt 列表：

```
/..%00/..%00/..%00/..%00/..%00/..%00/etc/passwd/..;/..;/..;/..;/..;/..;/etc/passwd/..%00/..%00/..%00/..%00/..%00/..%00/etc/passwd/..%0d/..%0d/..%0d/..%0d/..%0d/..%0d/etc/passwd/..%ff/..%ff/..%ff/..%ff/..%ff/..%ff/etc/passwd/..%3f/..%3f/..%3f/..%3f/..%3f/..%3f/etc/passwd/..%5c/..%5c/..%5c/..%5c/..%5c/..%5c/etc/passwd
```

大概长这样，当然还加入了一些自己改编的 payload，比如：

```
/..+/..+/..+/etc/passwd/..+../..+../..+../..+../etc/passwd/..++../..++../..++../..++../etc/passwd
```

##

## 六、自动化验证与命中

最后构建的命令如下：

```
httpx -l host.txt -paths /root/payload.txt -threads 100 -random-agent -x GET,POST,PUT -tech-detect -status-code -follow-redirects -title -mc 200 -match-regex "root:[x*]:0:0:"
```

命令里几个参数是刻意选的：-mc 200，把状态码收窄到200，减少对404/403 这类噪音结果的关注；-match-regex 直接在响应体里匹配 /etc/passwd 文件的特征字符串（root用户对应的 UID/GID 字段），这样即使某个响应包很长，也能第一时间从成千上万条结果里筛出真正命中的那几条，而不用逐个人工翻看响应内容。-threads 100 是在测试速度和目标服务器压力之间找的一个折衷值——始终要考虑不能因为并发过高影响目标的正常服务，这既是平台规则的要求，也是赏金猎人的基本职业素养。

放在 VPS 里跑了一晚。

第二天起来，看到心中想要的结果了。有四个域名命中了。

从原理上来说，感觉是一种路径穿越型的漏洞。

我打开其中一个子域名，显示的居然是 401。想不到401的子域名还会存在这样的漏洞，这是以前想不到的情况。

这类「401状态码下依然存在路径穿越」的现象，在赏金猎人社区里其实并不罕见。常见的原因是身份验证与文件服务逻辑分处不同组件：网关或反向代理层的权限校验，往往只针对特定的、「规整」的路径模式生效；而路径穿越构造出的畸形路径，在网关看来可能匹配不到既定的鉴权规则，被直接透传到后端，后端在做路径归一化处理后再返回文件内容。换句话说，「页面显示需要登录」和「这个路径实际有没有做鉴权」，在多层架构里未必是一回事——这也是为什么，赏金猎人往往不会因为看到一个401，就轻易放弃对该端点的深入测试。

## 七、写在最后

回头看这次挖掘，真正起作用的不是某一条「神奇」的payload，而是几个方法论层面的选择：在常规测试无果时，主动收窄范围、深耕单一漏洞类型；把别人分享的思路（哪怕是来自完全不同场景的 API 路径穿越技巧）迁移、改造，变成适合自己目标的 payload 体系；把重复性的验证工作自动化，让机器去跑「体力活」，把人的精力留给对结果的分析和判断；以及，在遇到看似「已排除」的信号（比如 401）时，仍然保留怀疑和二次验证的习惯。

赏金猎人这条路，枯燥和困顿是常态，「跑了几天没有任何发现」远比「一击即中」更接近真实节奏。能坚持把方法论沉淀下来，比拿到某一次具体的奖励更重要——工具会过时，技术会变化，但分析问题、构建验证体系的能力，是可以一直带着走的。

—  关于我们 —

江苏刺掌信息科技有限公司成立于2021年，公司旗下MS08067安全实验室，专注于网络安全领域教育、培训、认证产品及服务提供商。近两年，线上培训人数近10万人次，培养网络安全人才近6000名。

公司被认定为国家高新技术企业、镇江市创新性中小企业、江苏省科技型中小企业、江苏省民营科技企业、江苏省软件企业。并荣获机械工业出版社“年度最佳合作伙伴”、电子工业出版社-博文视点“优秀合作伙伴”、镇江市企业发展服务中心优质合作伙伴、镇江市网络安全应急支撑服务单位等荣誉称号。

实验室出版图书：

![](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xOW7SVDicXck1AqNicwhoCtaOpBpB5ZI3CrpG41kCOAdFgkaoKZdiczeUw38ItZyT0K4dT7wetKWiciccIJkqpiaickAiazby2uJDpibwT8/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaibvYpHN9LYFOebXFfldqqPibeicFj6KbfoI2xNya3Q5pgAeGPolfhjIlCsdt9TC19DE1CQ41loqtCAA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

```
![图片](https://mmbiz.qpic.cn/mmbiz_png/ddqrZtAEBOj4xTcIKUfImvRJW3QEEJCaNqRTwr9WEqXjnoaQ54wf9BbUE3HqNN7PIOxTDRNRb3e6bsJlSZP6Yw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/PW0wIHxgg3ntPMYAJur3UuYzhSDgO7Pu8DQL5f0FQIuDZC87yrAuNLy4frEdlMeWkthrlzczb0RbMOBQCAwDrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

如果喜欢本文

欢迎在看丨留言丨分享至朋友圈 三连

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/XWPpvP3nWa90pEp3iaRLqIghzI7eJdSJLep6zBaRDKVC6ibGLOlT9TqriaVck7icnvExOuMOCFhVAyVcyJ0JucvrnQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)
```

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWa9xKtQcyickhdgvJx9bWxpSjSqS4AwI7o804CbiazVQqTnMibp7ZC6fyxmJ7kgfMyA2rHgHkShs3M7bA/0?wx_fmt=png)

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