---
title: CircleCI、LastPass、Okta和Slack安全事件：攻击者正瞄准核心企业工具
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515307&idx=1&sn=523e28bb38f65a8485643de1d2a6417e&chksm=ea948dc1dde304d7e527c8f68c097d4979443d791948fa938c52fa758751c2841916dd70448f&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-17
fetch_date: 2025-10-04T04:03:26.894345
---

# CircleCI、LastPass、Okta和Slack安全事件：攻击者正瞄准核心企业工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSlngPzia2I5ciaHW5n0W5guxXH37o5WGGmdX5iaYnNAbRDRVCCQqvaetUsfs1qzJiaSzbcak6PCKgYQw/0?wx_fmt=jpeg)

# CircleCI、LastPass、Okta和Slack安全事件：攻击者正瞄准核心企业工具

Robert Lemos

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

![](https://mmbiz.qpic.cn/mmbiz_png/FIBZec7ucCiaWtRttKahE4rd7icPBW6mLiaWubZBfibktxAlCMH6dwLG1225lH4Xo8nmA5ENG7I4o905Qq23icpkHwg/640?wx_fmt=png)

**1月初，开发管道服务提供商CircleCI 提醒用户称注意安全泄露事件，督促企业立即更改密码、SSH密钥和其它存储在该DevOps平台或由该平台管理的其它机密。调查结果显示，其工程师遭恶意软件感染但其反病毒软件并未检测出，导致基于2FA的SSO会话cookie被盗，公司内部系统遭访问。**

这起事件导致CircleCI 立即判断事件影响范围、限制攻击者修改软件项目的能力并判断哪些开发机密受陷。与此同时，CircleCI更改了认证令牌、修改了配置变量、和其它提供商携手处理密钥过期事件并继续开展调查。

CircleCI 公司在上周发布的安全公告中指出，“目前，我们可以肯定地说，系统中并不存在越权方；然而，处于谨慎考虑，我们想要确保所有客户已采取某些防御措施，保护数据安全。”

CircleCI 受陷事件说明攻击者将注意力转向根本的企业服务。身份服务如Okta和LastPass 在去年披露了系统受陷事件，而开发者聚焦服务如Slack 和 GitHub也匆忙应对针对源代码和基础设施的攻击活动。

云安全公司F5的工程师兼布道者 Lori MacVittie指出，针对核心企业工具的攻击说明企业应当预料到这类提供商将来会变成常规目标。她表示，“随着我们越来越多地依赖于服务和软件进行自动化，从开发build到测试、部署等不一而足。这些服务成为具有吸引力的攻击面。我们认为它们并非攻击者的目标应用，但事实并非如此。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSlngPzia2I5ciaHW5n0W5guxLhoDKsjRzuo9dUozAgoJNMGfCxurNSrz4YExrBpIQKtWororAPTIIA/640?wx_fmt=png)

**身份和开发者服务遭攻击**

最近，攻击者盯上了两种主要的服务类型：身份和访问管理系统以及开发者和应用基础设施。这两种服务类型增强了企业基础设施的重要方面。

NetWitness 公司的首席技术官 Ben Smith指出，身份是连接组织机构每部分以及该组织机构与合作伙伴以及客户之间的胶水。他指出，“不管你用的是什么产品和平台，攻击者认为比从事认证服务的组织机构更好的是为其它客户进行认证服务的组织机构。”

开发者服务和工具同时也成为遭攻击的另外一种企业服务。九月份，某威胁人员获得对Rockstar Games开发者Slack频道的访问权限，下载即将上线的Grand Theft Auto 6游戏的视频、截屏和代码。1月9日，Slack公司表示发现“数量有限的Slack员工令牌被盗且被滥用于访问外部托管的GitHub仓库。”

由于身份和开发者服务通常会访问大量企业资产如应用服务、运营、源代码等，攻陷这些服务可成为闯入公司其它部分的万能钥匙。

他提到，“它们是非常非常具有吸引力的目录，是唾手可得的。这些都是典型的供应链攻击，一种管道攻击，因为管道不是每天都能看到的。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSlngPzia2I5ciaHW5n0W5guxLhoDKsjRzuo9dUozAgoJNMGfCxurNSrz4YExrBpIQKtWororAPTIIA/640?wx_fmt=png)

**合理管理机密并建立相关手册**

Bishop Fox 公司的管理顾问 Ben Lincoln指出，组织机构应当为最坏场景做好准备，并认识到不存在防御此类大规模、影响大的事件的简单方法。他提到，“防御措施的方法有很多，但确实存在一些费用。所以我能理解在事情变得明朗且必要之前，开发者不愿意执行这些方法的顾虑。”Lincoln 建议综合管理机密信息。企业应当能够“按下某个按钮”并修改所有必要的密码、秘钥和敏感的配置文件。你需要限制暴露，但如果存在泄露事件，那你希望可以按下某个按钮，立即修改所有凭据。企业应当提前做好规划并部署相关措施以防不时之需。”

组织机构还可以为攻击者设置陷阱。很多蜜罐类型的战略可使安全团队提前收到关于攻击者位于网络或服务中的警报。创建虚假的账户和凭据有助于检测威胁人员访问敏感资产的时间。

另外，企业需要部署零信任原则，不仅降低机器、软件和服务的攻击面，还应降低运营的攻击面。她提到，“从传统意义上来讲，运营是隐藏且安全的，因此企业不会太关注它们。应用程序和数字化服务当前的构建方式、运营涉及很多app到app、机器到app的身份，攻击者已开始认识到这些身份也是有价值的。”

---

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSZu3o6N7v8IvXlaSpv9pqrC38BdYic1GvE8xzpEraJy9nHYRGk5rCC0dHKEfBr2rC1nJ8gMCDIvIw/640?wx_fmt=jpeg)

**推荐阅读**

[在线阅读版：《2022中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&chksm=ea94853cdde30c2a963cfa00a536764ea55cdee7ba6ef4a7716a28f82a97ca630dc271ee5224&scene=21#wechat_redirect)

[在线阅读版：《2021中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505380&idx=1&sn=01d2f5af200abc6bb20411ee8f17b6b5&chksm=ea94e48edde36d98f20b66aecf9f359e49226b411872bcea527fcca0a5de018f407415313800&scene=21#wechat_redirect)

[PyTorch 披露恶意依赖链攻陷事件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515167&idx=1&sn=24c07a386819db63dc889fa9bfe7b382&chksm=ea948d75dde304635dd31a7b3deeb1ff296b25b6ac462e35546afa8779e3ff455b3cd475dff4&scene=21#wechat_redirect)

[速修复！这个严重的 Apache Struts RCE 漏洞补丁不完整](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511361&idx=1&sn=540cad65022d11423a868f977b4fe663&chksm=ea949c2bdde3153d70ed1c43058c67f7e846f30ea1d2f562389edf804ace5c6bf19621f5bf6e&scene=21#wechat_redirect)

[Apache Cassandra 开源数据库软件修复高危RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510538&idx=2&sn=1d92fa67b48167800ad01baa90c58cbd&chksm=ea949b60dde312765657b9d469ce2b1b6befbad085737df863891995b40982a6109939fb82b2&scene=21#wechat_redirect)

[美国国土安全部：Log4j 漏洞的影响将持续十年或更久](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512944&idx=1&sn=003f4935476be99ce0be8caa3fe086fe&chksm=ea94821adde30b0c5b96de8d9948d479b7a6f59ff1ba75271057b28e17faa26b43c701a5f1fe&scene=21#wechat_redirect)

[Apache Log4j任意代码执行漏洞安全风险通告第三次更新](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509646&idx=1&sn=34bc8208994380969cd89045067150b7&chksm=ea9497e4dde31ef2991a59f30171df1f69368c1951483d97f3de41d81a5717bb03e234491f5d&scene=21#wechat_redirect)

[PHP包管理器Composer组件 Packagist中存在漏洞，可导致软件供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514137&idx=1&sn=347691413dc7ecfc2a2dedd365115329&chksm=ea948973dde3006553ae4c52ee22cd9f9c1eb480c80a59e78eaf25d9f9c974ed002d8e053488&scene=21#wechat_redirect)

[LofyGang 组织利用200个恶意NPM包投毒开源软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514172&idx=1&sn=271b12e7a37da40fb7ddc58a30cf4135&chksm=ea948956dde300402d1d9ef54ea22519931efbfc852b82816c893892b876166c39063af581fc&scene=21#wechat_redirect)

[软件和应用安全的六大金科玉律](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514145&idx=1&sn=639a349a140d429c996a51949fec0a92&chksm=ea94894bdde3005d6eeb0e37e7a3f81c6518bdce555fd5d9fff4418c5b305e17c5fb7916cb58&scene=21#wechat_redirect)

[美国政府发布关于“通过软件安全开发实践增强软件供应链安全”的备忘录（全文）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514050&idx=1&sn=14f44208b38382e14a3f4562615bedb5&chksm=ea9486a8dde30fbe2b0ef3231a0a73e44579f710c6bede1cd4eb563d0545476d5ef3607ea39d&scene=21#wechat_redirect)

[OpenSSF发布4份开源软件安全指南，涉及使用、开发、漏洞报告和包管理等环节](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514034&idx=1&sn=51f02a3110acce0dbd53196876ef1fad&chksm=ea9486d8dde30fce4995e5734ad507e889b4c58c0d3ff8d777f66119f2d5fb3f1c7d0e064726&scene=21#wechat_redirect)

[美国政府发布联邦机构软件安全法规要求，进一步提振IT供应链安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513979&idx=1&sn=66625cf062357864cf86053f868d8bb7&chksm=ea948611dde30f0758522e7694b72c9f1abdcbf9c7de8eece909dcdf444e2ce7cf19d357db91&scene=21#wechat_redirect)

[美国软件供应链安全行动中的科技巨头们](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513936&idx=1&sn=ffd61a99532c853e13587e17ccb3e9a1&chksm=ea94863adde30f2cbc1141ebad6ae15d7b5ec09ee3c8337db26c9bda2b26c2914cdde4757ffb&scene=21#wechat_redirect)

[Apache开源项目 Xalan-J 整数截断可导致任意代码执行](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513963&idx=4&sn=8f7f84190a33593bda1e3d6c86470af6&chksm=ea948601dde30f178f02bdcc42ac15f052526722f31417ec3cc51f2b92cde6a84be7894c8fe8&scene=21#wechat_redirect)

[谷歌推出开源软件漏洞奖励计划，提振软件供应链安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513721&idx=1&sn=9ccc0511cb8d6c7134eb54700130f1b7&chksm=ea948713dde30e0503874ed6e5ebcd5a90933ef86048fd21466e73431420b799a861f800164a&scene=21#wechat_redirect)

[黑客攻陷Okta发动供应链攻击，影响130多家组织机构](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513692&idx=2&sn=9edbf81f8e756e90d33627cdfe3796f3&chksm=ea948736dde30e20a3b8750b3189dd23d0baf268f08e98448ec6421a9d7649d3cfc08f11f960&scene=21#wechat_redirect)

[Linux和谷歌联合推出安全开源奖励计划，最高奖励1万美元或更多](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513617&idx=2&sn=4f50589d2631ebc4ee55cbbb21d52fbd&chksm=ea94877bdde30e6db6623e64b233c7a81ddcaa9a50d7211c608a26c1e48cf51a1ee2101991d5&scene=21#wechat_redirect)

[开源web应用中存在三个XSS漏洞，可导致系统遭攻陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513307&idx=2&sn=4a99112b9efeb2e33add05f94b1dd1d5&chksm=ea9485b1dde30ca77b26b217f677ed8a3be57d9c8750d39780781015e46520db5185da5bd1dc&scene=21#wechat_redirect)

[开源软件 LibreOffice 修复多个与宏、密码等相关的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513283&idx=1&sn=5fbd02e0f95926cab449829326e0a8a1&chksm=ea9485a9dde30cbf0fb5e64dcbabdcbc1486306bbf93...