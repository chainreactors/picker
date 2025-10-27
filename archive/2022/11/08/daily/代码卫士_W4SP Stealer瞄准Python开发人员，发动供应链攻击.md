---
title: W4SP Stealer瞄准Python开发人员，发动供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514414&idx=2&sn=04e04c2acb029f4232895de2f58ae419&chksm=ea948844dde30152cde88117c034776924648f472995c0f3e61e0ad0a2cafa85f683191d85cd&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-11-08
fetch_date: 2025-10-03T21:56:53.785956
---

# W4SP Stealer瞄准Python开发人员，发动供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRib1W60OwVsAUicpkzzfC9EIp5nEaO0wAdY876YpleFN0vsricUWA1wcmleCVeoJDrFRCjFslm3eGUw/0?wx_fmt=jpeg)

# W4SP Stealer瞄准Python开发人员，发动供应链攻击

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

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRib1W60OwVsAUicpkzzfC9EIYfoIBPnb1PsdkP6hlC1bppKjfsEWwb9vN0EyNGZaBWEJ5MCC2ykIwg/640?wx_fmt=gif)

攻击者继续创建虚假的 Python 包和初级混淆技术，通过 W4SP Stealer 感染开发人员系统。该木马旨在从开发人员系统中窃取密币信息、提取敏感数据并收集凭据。

软件供应链公司 Phylum 发布安全报告指出，威胁行动者已经在PyPI 上创建了29个热门软件包克隆，包名称听起来非恶意或者类似于合法软件包的名称，即利用了typosquatting技术。如开发人员下载并加载了这些恶意包，则开始脚本也通过一系列混淆步骤安装W4SP Stealer 木马。研究人员指出，这些包的下载来那个已达到5700次。

虽然W4SP Stealer 针对的是密币钱包和金融账户，但当前攻击活动最重要的目标是窃取开发人员的机密信息。Phylum 公司的联合创始人兼首席技术官 Louis Lang 指出，“它和我们常看到的邮件钓鱼活动没有什么不同，只不过攻击者这次仅针对开发人员。鉴于开发人员通常拥有对机密信息的访问权限，对于组织机构而言，如遭成功攻击会带来灾难性后果。”

未知攻击者或攻击者组织对PyPI 发动的攻击，仅仅是最近针对软件供应链的威胁。开源软件组件通过仓库服务如 PyPI 和 NPM 分发，是热门攻击向量，从导入软件的依赖数量急剧增长即可看出。攻击者尝试利用这些生态系统将恶意软件分发到不知情的开发人员系统中，如2020年发生的针对 Ruby Gems 生态系统和Docker Hub 镜像生态系统攻击事件那样。8月份，Check Point 公司的研究人员发现10个PyPI 包释放窃取信息的恶意软件。

在最新发生的攻击活动中，研究人员分析指出，“这些程序包更致力于将 W3SP Stealer 传播到 Python 开发人员的机器中。随着这种不断变换攻击技术的活动的发展，未来将看到更多类似的恶意软件出现。”

**PyPI 攻击是“数字游戏”**

这起攻击利用了错误拼写常见程序包名称、或者在未正确审查软件来源的情况下就使用新程序包的开发人员。恶意包 “typesutil” 是热门Python 包 “datetime2” 的副本，只是做了一些修改。

最初，导入该恶意软件的程序都会在Python 加载依赖时，运行命令，在设置阶段下载恶意软件。然而，由于PyPI 执行了某些检查，因此攻击者开始通过whitespace推送超出多数代码编辑器正常可查看范围的可疑命令。分析指出，“攻击者对攻击技术稍作修改，并没有将导入转出到明显地方，而是放在远离屏幕的地方，利用Python 很少使用的分号，将恶意代码像合法代码那样插入同样的行。”

虽然 typosquatting 是一种低效的攻击方式，成功率极低，但相比潜在回报而言，投入几乎不值一提。研究人员指出，“这是和日常通过恶意包污染包生态系统的攻击者的一场数字游戏。遗憾的是，和潜在回报相比，部署其中一个恶意包的成本极低。”

**W4SP Stealer 木马**

该攻击的最终目标是安装“窃取信息的木马 W4SP Stealer，该木马枚举手哈子和系统、窃取存储在浏览器中的密码、攻击密币钱包并通过关键字如‘银行’和‘机密’来搜索相关文件。除了常见的金钱奖励外，收集到的信息还可被用于访问关键基础设施或获取开发人员的其它凭据。”

研究人员已在识别攻击者方面取得一定进展并将报告发送给相关企业。

---

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSZu3o6N7v8IvXlaSpv9pqrC38BdYic1GvE8xzpEraJy9nHYRGk5rCC0dHKEfBr2rC1nJ8gMCDIvIw/640?wx_fmt=jpeg)

**推荐阅读**

[在线阅读版：《2022中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&chksm=ea94853cdde30c2a963cfa00a536764ea55cdee7ba6ef4a7716a28f82a97ca630dc271ee5224&scene=21#wechat_redirect)

[在线阅读版：《2021中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505380&idx=1&sn=01d2f5af200abc6bb20411ee8f17b6b5&chksm=ea94e48edde36d98f20b66aecf9f359e49226b411872bcea527fcca0a5de018f407415313800&scene=21#wechat_redirect)

[美国政府发布软件供应链供方实践建议指南](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514400&idx=1&sn=374227cc2e54ab7b644eb2e852a2934f&chksm=ea94884adde3015cc267473775816d120725f906a9c2cc739a7d6c1dceb8cf8d6073d186bf86&scene=21#wechat_redirect)

[NISA和CISA分享软件供应链安全建议](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513770&idx=2&sn=5d9ed5492cd174567b6c98cbcd041969&chksm=ea9487c0dde30ed6aa860e35f8c2515b95979b7ea4c1bc0824977e2d034664500f5b94f71707&scene=21#wechat_redirect)

[美国“加强软件供应链安全实践的指南” (SSDF V1.1草案) 解读来了](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509546&idx=1&sn=a653c828fee1a84f0e19710a32acbdf5&chksm=ea949740dde31e56a33e9a0ba7381819fff434c3c7fa2df37370857dd84cade62378d842fd0b&scene=21#wechat_redirect)

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

[开源软件 LibreOffice 修复多个与宏、密码等相关的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5...