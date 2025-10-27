---
title: 新型NPM计时攻击可导致供应链攻击，GitHub 不打算修复
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514198&idx=1&sn=896500007d3b6e8878a313e75f4f0440&chksm=ea94893cdde3002ab918f2937fefc42dece54a931457ca7274fbea4258224d4cc93342f08b7d&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-10-14
fetch_date: 2025-10-03T19:50:44.586392
---

# 新型NPM计时攻击可导致供应链攻击，GitHub 不打算修复

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuF0iaALltZwCp35627oWoJyU5lTkXUBBtpibn95k3G50wONAwxByx4AGAacVDKibynlibADTJp6F6rQ/0?wx_fmt=jpeg)

# 新型NPM计时攻击可导致供应链攻击，GitHub 不打算修复

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

![](https://mmbiz.qpic.cn/mmbiz_png/FIBZec7ucCiaWtRttKahE4rd7icPBW6mLiaWubZBfibktxAlCMH6dwLG1225lH4Xo8nmA5ENG7I4o905Qq23icpkHwg/640?wx_fmt=png)

**网络安全研究员发现一起npm计时攻击泄露了私有程序包的名称，导致威胁行动者可快速发布并诱骗开发人员使用恶意克隆。**

该攻击利用的是人们在搜索仓库中私有程序包时与搜索不存在的程序包时返回 “404未找到”错误之间的微小时间差。虽然该响应时间差仅仅是数百毫秒，但足以判断是否存在执行程序包模拟攻击的私有程序包。

组织机构为内部项目和某些软件产品创建私有程序包，将开发人员面临typosquatting攻击的风险最小化，并使其代码和函数保持私密状态。

保持私有程序包为私密状态对于其组织机构用户而言至关重要。否则，攻击者可创建克隆或遭typosquat的程序包，诱骗员工下载并用于软件项目中。如果开发人员和内部软件测试人员未发现攻陷情况，则产品可交付给最终用户，从而实现供应链攻击。

发布该研究成果的Aqua Security 公司的威胁研究团队表示，供应链攻击越来越频繁，2021年相关攻击活动增长了300%。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQuF0iaALltZwCp35627oWoJvzYfeTeiaWWelKklTqic1pibVt42wxnSYd17W71HoXR8QcW9kcKolNWmQ/640?wx_fmt=png)

**0****1**

**计时攻击详情**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQuF0iaALltZwCp35627oWoJmqJgzdh1bwibGzXr2vic1au2iaTsGMs3LiacWKBxeQwgRBnHcOOLYnNR2w/640?wx_fmt=gif)

Npm 中包含一个 registry API，可使用户下载已有程序包，检查是否存在该程序包并接受某个特定范围内所有程序包的信息。

当使用该npm registry 下载并不存在或设置为私密状态的程序包时，该网站将访问一个404 HTTP错误信息，说明无法找到该程序包。研究人员通过该API检查自己在npm上创建的私有程序包是否存在，并对比了检查不存在程序包时所返回的404 HTTP 错误消息后，发现了这次npm 计时攻击。

研究人员五次检查某程序包名称进行测试，发现npm响应请求所需平均时间存在一个可衡量的差距，从而觉察出该程序包是私有程序包还是不存在的程序包。

更具体而言，检查私有程序包是否存在的平均响应时长是648毫秒，而检查是否不存在的平均响应时长降低至101毫秒。研究人员认为这种差别在于npm API的缓存机制和架构，从而引入了信息泄露的可能性。黑客可尝试“盲”字典攻击或查找目标组织机构公有仓库中的命名模式和组合，衍生出可能的私有仓库名称。此外，网络信息中包含历史程序包信息，因此攻击者可利用这些信息判断哪些公有程序包后续会转变为私有程序包。在后一种情况下，通过克隆程序包实现潜在攻陷可能会非常隐秘，因为曾被公开的程序包的老旧副本可能仍然保留足够多的功能，在软件产品中实现预期目标。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQuF0iaALltZwCp35627oWoJvzYfeTeiaWWelKklTqic1pibVt42wxnSYd17W71HoXR8QcW9kcKolNWmQ/640?wx_fmt=png)

**0****2**

**GitHub不打算修复**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQuF0iaALltZwCp35627oWoJmqJgzdh1bwibGzXr2vic1au2iaTsGMs3LiacWKBxeQwgRBnHcOOLYnNR2w/640?wx_fmt=gif)

研究人员在2022年3月8日将该漏洞披露给GitHub，不过在3月25日得到回复称由于架构限制问题，该漏洞将不会被修复。

GitHub 指出，“由于这些架构性限制条件，我们无法阻止计时攻击判断某个特定的私有程序包是否存在于npm上。”研究人员表示，组织机构可采取预防措施，经常搜索 npm 中欺骗具有复制或类似名称的私有程序包的可疑程序包。另外，组织机构也可创建欺骗其私有程序包为占位符的公共程序包，因为npm不允许在公开仓库中上传同一名称的程序包。

---

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSZu3o6N7v8IvXlaSpv9pqrC38BdYic1GvE8xzpEraJy9nHYRGk5rCC0dHKEfBr2rC1nJ8gMCDIvIw/640?wx_fmt=jpeg)

**推荐阅读**

[在线阅读版：《2022中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&chksm=ea94853cdde30c2a963cfa00a536764ea55cdee7ba6ef4a7716a28f82a97ca630dc271ee5224&scene=21#wechat_redirect)

[在线阅读版：《2021中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505380&idx=1&sn=01d2f5af200abc6bb20411ee8f17b6b5&chksm=ea94e48edde36d98f20b66aecf9f359e49226b411872bcea527fcca0a5de018f407415313800&scene=21#wechat_redirect)

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

[开源软件 LibreOffice 修复多个与宏、密码等相关的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513283&idx=1&sn=5fbd02e0f95926cab449829326e0a8a1&chksm=ea9485a9dde30cbf0fb5e64dcbabdcbc1486306bbf9305df01d0f12022f30b84421fe09b167c&scene=21#wechat_redirect)

[Juniper Networks修复200多个第三方组件漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512960&idx=1&sn=0df41cf06e3efd8089ec6d6d6b03fc20&chksm=ea9482eadde30bfc407cd490459c7c947bbf2496475946f0379eb8e76c8f4e47f2063742ef87&scene=21#wechat_redirect)

[美国国土安全部：Log4j 漏洞的影响将持续十年或更久](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512944&idx=1&sn=003f4935476be99ce0be8caa3fe086fe&chksm=ea94821adde30b0c5b96de8d9948d479b7a6f59ff1ba75271057b28e17faa26b43c701a5f1fe&scene=21#wechat_redirect)

[美国国土安全部：Log4j 漏洞的影响将持续十年或更久](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512944&idx=1&sn=003f4935476be99ce0be8caa3fe086fe&chksm=ea94821adde30b0c5b96de8d9948d479b7a6f59ff1ba75271057b28e17faa26b43c701a5f1fe&scene=21#wechat_redirect)

[PyPI 仓库中的恶意Python包将被盗AWS密钥发送至不安全的站点](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512575&idx=2&sn=5af81a53d9263bf10273d86868a77287&chksm=ea948095dde309830949a85914d18a896ce49535f37a9c0cf802e2d84d4dbf264c0e5795396b&scene=21#wechat_redirect)

[开源项目 Parse Server 出现严重漏洞，影响苹果 Game Center](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512551&idx=1&sn=a3dc5a12724c0b9b230eedf1455dbf23&chksm=ea94808ddde3099bc99f14a224f4836cc7d9419f056f982dd29238ebf945806f58f2989225bc&scene=21#wechat_redirect)

[奇安信开源软件供应链安全技术...