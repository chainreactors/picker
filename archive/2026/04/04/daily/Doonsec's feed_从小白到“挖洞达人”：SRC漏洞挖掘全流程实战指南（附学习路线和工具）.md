---
title: 从小白到“挖洞达人”：SRC漏洞挖掘全流程实战指南（附学习路线和工具）
url: https://mp.weixin.qq.com/s/WvQCPuwBpNSWi__B6ZzosA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:59.302800
---

# 从小白到“挖洞达人”：SRC漏洞挖掘全流程实战指南（附学习路线和工具）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj56cRcOcPzdeFibPImNemmCtbyMnCgPbsIc86YtdrgyChq4MenabdkeNY5DA7t8H4Po9UpXQVQeHL6oIn4kFeDckpXVq9JjEibsMY/0?wx_fmt=jpeg)

# 从小白到“挖洞达人”：SRC漏洞挖掘全流程实战指南（附学习路线和工具）

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj55PjxpoPFYtgKd65wuUpOVX4uhlurdxiaSDmM0c3SQQTziaHjs8pFm96cNXJLC71y0VyuHkacU2TAEzdwmn1xHt1gDjTUmhAvyRg/640?wx_fmt=png&from=appmsg)

## 开篇：为什么说SRC挖洞是安全新手的最佳起点？

---

##

## 凌晨两点，大学生张三盯着电脑屏幕突然跳出的「高危漏洞奖励到账」提示，手抖得差点打翻泡面——这是他挖到人生第一个SRC漏洞（某电商平台的越权访问漏洞）后收到的第一笔奖金，金额足够支付三个月生活费。这样的故事，在安全圈每天都在发生。

##

SRC（Security Response Center，安全应急响应中心）是各大企业（如阿里、腾讯、字节、美团等）官方设立的平台，专门接收外部白帽子提交的漏洞并给予现金奖励。对零基础的安全爱好者来说，SRC挖洞是最友好的入门路径：

* **目标明确（企业真实业务）**
* **规则清晰（有明确的漏洞评级和奖励标准）**
* **反馈直接（提交后几天内就能收到回复）**
* 甚至不需要你懂复杂的逆向或内核漏洞，只要掌握基础思路，就能快速上手

这里简单说一下，我对SRC漏洞挖掘的思路技巧。

可能很多人对于SRC往往无从下手，感觉自己挖不到SRC漏洞，这里其实最重要的问题还是自己的心理问题（当然必须还有一定的技术能力）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj54D995plWsXN3Fe9qibGe0DibxLiaNEq2rpAZcK7wr8WjsiaqUhQGJciaoCDhye5buCNziceicoZP8AvUGibxvw1sfj69lsWH4FyoxpwhI/640?wx_fmt=jpeg)![]()

很多人挖上一两个小时或者半个小时就不挖了，没什么进展，其实对于一些src漏洞挖掘和别的站点漏洞挖掘都大差不大，但是为什么都感觉自己挖不倒，这里说下我的认为，还是因为你不够细。挖SRC一定要细，慢慢的去分析，不能着急往往越着急越挖不倒，这里可以给大家一些建议，在挖掘SRC期间

* 不要着急出洞，先去慢慢摸索厂商的各种信息，了解每个功能点（做好信息搜集）
* 去分析每一个数据包，知道每个数据包对应的功能点在哪儿，去知道数据包对应鉴权的地方在哪一块
* 多去关注厂商的活动，一般新上线的项目或者活动漏洞比较好挖一些
* 关注厂商信息，比如一些活动期间奖励翻倍等信息
* 千万要记住去看人家厂商的漏洞收录范围，不看范围挖漏洞=白干

SRC逻辑漏洞一般产出比较高的漏洞就在于逻辑漏洞，别的漏洞也有但是相比起来逻辑漏洞的价值更高

# 一、入门第一步：搞懂「游戏规则」

### （1）常见SRC平台有哪些？

#### ① 补天漏洞响应平台：

![](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj55L1SibCBWmTy7u5qKpAH8Q2nyox1eTdat6a3icxUsa2F1DdADNKLWG1vcD9WKXccJwc0XkzNaKVh8qJN0nuFQVd7vI03J18wtaQ/640?wx_fmt=jpeg)![]()

* **奖励：** 中等，可以给现金和kb，kb可以兑换实物奖励
* **通过门槛：** 高，需要收录移动百度权重大于等于1或者百度pc权重大于等于1或者谷歌权重大于等于3的网站，edu和gov的站不需要权重
* **审核速度：** 快

#### ②漏洞盒子：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj56kcqXgTWOEMMuE47cVjazger1Kz1ia5bXERNQcVL5X2PTK1RfVGPw05jeWRMTkphHvy3kJ9qLDj68WScBSoCsnGgy2D9qCzOMc/640?wx_fmt=jpeg)![]()

* **奖励：** 中等，奖励的话有现金还有积分，积分可以在商城内兑换礼物
* **通过门槛：** 门槛比较低，只要是漏洞都收，没有权重或者公司的一些要求，审核不是很严格，刚入门的师傅可以提交到漏洞盒子，练练手，积累一下经验和技巧
* **审核速度：** 一般吧，有时候快有时候慢

#### ③CNNVD信息安全漏洞库：

![](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj55AqHv9iaNCPyLvmaU0iaKxRPxfgXfQr5g2TTYJ3tq5huib7EHCdcHUy4quNpqv7v5MxnibEnFPiaLr0iauSQbwLbQNCOLCm1T7Id4I8/640?wx_fmt=jpeg)![]()

* **奖品：** 高，可以给你证书
* **通过门槛：** 极高，不仅仅要看权重，而且还要看公司的注册资金，好像是通用型的漏洞，厂商注册资金要超过五千万，而且还不能只提交一个，要提交十个案例才可以
* **审核速度：** 一般

#### ④教育漏洞提交平台：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj57qkwOeIM2UhR2GRHQg8QA13qkqGYBJs3Sk8VhgczP0bBX2OKoPLTsNr6L2maEx2qPRBTNzicQAeH9qFwArOQWshz4RoYUhKZmU/640?wx_fmt=jpeg)![]()

* **奖品：** 高，有大学专门给的证书，和一些礼品
* **通过门槛：** 高，必须要edu和教育相关的网站，例如说大学，中学，高中这些
* **审核速度**： 一般

这里只列举最简单并且比较知名的一些公益src提交平台，还有一些其他的公益src提交平台，就不一一列举了

### （2）漏洞类型与奖励等级（以主流SRC为例）

###

不同企业的评级标准略有差异，但核心逻辑相通。常见的高价值漏洞类型包括：

* **高危**：远程代码执行、SQL注入、任意文件上传、严重越权（直接操作他人账号资金/数据）、敏感信息泄露（数据库配置、用户手机号等）。
* **中危**：普通越权（如普通用户查看管理员信息）、反射型XSS（需诱导点击）、CSRF（、敏感信息泄露（非核心数据）。
* **低危**：信息泄露、弱口令、XSS。

💡 **新手提示**：优先从「低门槛高危漏洞」入手，比如越权访问、信息泄露、简单的SQL注入/XSS——这些漏洞在企业业务中常见，且验证逻辑相对直接。

# 二、前期的准备工作

#### 一些在线的搜索引擎网站：

##### （一）资产测绘引擎

* fofa资产测绘引擎：https://fofa.info/
* 鹰图资产测绘引擎：https://hunter.qianxin.com/
* shodan资产测绘引擎：https://www.shodan.io/
* 360资产测绘引擎：https://quake.360.net/
* 零零信安资产测绘引擎：https://0.zone/
* 谷歌hacker语法：https://codeleading.com/article/8526777820/

以上的搜索引擎网站都是用来收集目标网站信息的一些网络空间资产测绘，可以帮助我们快速的定位到目标的资产，批量获取url进行漏洞挖掘

##### （二）企业信息查询

* 爱企查：https://aiqicha.baidu.com
* 天眼查：https://www.tianyancha.com
* 企查查：https://www.qcc.com
* 小蓝本：https://www.xiaolanben.com

以上的网站是为了查询网站所属的企业的一些信息，为了方便在提交漏洞的时候填写详细联系方式和公司的地址

##### （三）域名信息查询

* 爱站：https://www.aizhan.com
* 站长工具：https://tool.chinaz.com

以上的网站是为了查询网站备案信息、网站权重信息、网站的ip信息等

##### （四）保持一个良好的心态

一个好的心态，和一个灵活的脑袋，心态很重要，保持一个良好的心态，挖洞的时候细心一点，不怕漏洞挖不到。正所谓心细则能挖天下！！！

**注意：任何未授权的测试都要点到为止，表明出漏洞的危害就好了，再往下就不礼貌了。**

![](https://mmbiz.qpic.cn/mmbiz_png/weRiaQxEYtIE88631b0baaacmrxDNFlLEIicMpAxxzezleSIjDz7KSLzbDmicvuqXSnydOhE2dxSIvOYKxPBxqicPw/640?wx_fmt=png&from=appmsg#imgIndex=5)

拿到有漏洞的url之后，我们需要处理一下这些数据，大概一个思路就是：

->漏洞url

->根据url（因为有些网站是ip站）反查域名

->根据域名反查域名权重

->根据有权重的域名反查域名备案名称

->根据备案名称查询公司的基本信息，例如公司的所在地方和行业等等

# 三.挖漏洞需要掌握的知识

1.计算机组成原理、计算机网络、计算机体系结构、计算机操作系统，密码学,多媒体技术等等。这些都需要掌握，总之一句话就是大学计算机的基础课程。

2.编程: HTML、CSS、JavaScript、 PHP、 Java、 Python、 sql、 C、C++、 shell，汇编、nosql. powershell等等常见的语言基础都需要掌握，至少要熟练使用Python和sq|

3.漏洞方面，漏洞分很多种，根据不同的标准也会有交叉，黑客要掌握大部分漏洞的形成原理，检测方法，利用方法，修复方法，常见的网站漏洞有sq|注入，XSS, 文件包含，目录遍历，文件上传，信息泄露，CSRF, 账号爆破，各种越权等等，常见的二进制漏洞有缓冲区溢出，堆溢出，整形溢出，格式化字符串等等，分析的时候还要绕过操作系统的保护机制。

协议的话也是存在漏洞的，比如TCP、UDP什么的拒绝服务，DNS劫持，ARP欺骗等等, 现在工控、物联网、AI什么的也都有各种各样的漏洞。

# 四.学习资料分享

因为入门学习阶段知识点比较杂，所以我讲得比较笼统，大家如果有不懂的地方可以找我咨询，我保证知无不言言无不尽，需要相关资料也可以找我要，我的网盘里一大堆资料都在吃灰呢。

干货主要有：

① 网络安全学习路线图（告别不入流的学习，快速掌握知识）

② 网络安全各方面大佬分享的笔记等（网络安全、应急响应、代码审计等）

③ 渗透测试常用工具、字典

④ 网络安全入门基础视频（从0教起，适合小白学习）

⑤ 网络安全高频面试题大全

⑥ ......

扫码领取

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAmQO922RsJH8oNVNo28hujdEqkbnrZTKI5IXibkbQGT3Es1s6wruZu9giczEsvg0Qr6G06ldEuVGFPg/640?wx_fmt=png&from=appmsg)

## 结语：挖洞不是「黑客攻击」，而是「帮助世界更安全」

SRC挖洞的本质是「以白帽子的身份帮助企业发现安全隐患」。每一次提交，都可能避免一次数据泄露或资金损失；每一笔奖励，都是对企业安全建设的正向反馈。更重要的是，这个过程会让你真正理解「安全的本质是信任」——而你的每一次挖掘，都在让这份信任更坚固。

现在，打开Burp Suite，找一个目标网站（记得先确认在SRC范围内！），开始你的第一次抓包吧！你的第一个漏洞，可能就在下一个请求里。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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