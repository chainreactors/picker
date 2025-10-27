---
title: 德企Festo 和 CODESYS 的OT产品受3个漏洞影响，可导致供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514853&idx=4&sn=f887c2246bde0615a6afcc197112e9a8&chksm=ea948b8fdde30299897ba08d1d9780bac245ae05c8b213f63334fa58fc54924eb5c5e95c5bac&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-12-02
fetch_date: 2025-10-04T00:18:08.175443
---

# 德企Festo 和 CODESYS 的OT产品受3个漏洞影响，可导致供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSXU3yX3JfkwE20YdSXMFEIZH1RFnJkBcHEGyPCyPyxlicMIRxYGlDEJeoFp2DMz6SBBrL3hM4ZS9A/0?wx_fmt=jpeg)

# 德企Festo 和 CODESYS 的OT产品受3个漏洞影响，可导致供应链攻击

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

![](https://mmbiz.qpic.cn/mmbiz_png/FIBZec7ucCiaWtRttKahE4rd7icPBW6mLiaWubZBfibktxAlCMH6dwLG1225lH4Xo8nmA5ENG7I4o905Qq23icpkHwg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSXU3yX3JfkwE20YdSXMFEIrIkntER4Tr90Zhj3SLRHO8EwI0rmzhQiavicAGEMsVwk4Jy5d3nPiaf9g/640?wx_fmt=gif)

**研究人员披露了影响德国公司 CODESYS 和 Festo运营技术 (OT) 产品中的三个新漏洞，它们可导致源代码篡改和拒绝服务后果。**

这些漏洞是由 Forescout Vedere Labs 报告的，是OT:ICEFALL系列漏洞中的最新成员。研究人员指出，“这些问题说明，要么是在设计不安全的方式（产品发布之时起非常普遍的情况）中，制造商将很多危险函数囊括其中，无需认证即可访问；要么是安全控制的实现低于一般标准。”

在这些漏洞中，最严重的是CVE-2022-3270（CVSS评分9.8），影响 Festo 自动化控制器。无需任何认证即可使用 FGMC 协议重启设备并引发拒绝服务条件。

Festo 控制器中的另外一个DoS 漏洞（CVE-2022-3079，CVSS 7.5）和对未记录网页 (“cec-reboot.php”) 的未认证远程访问权限有关，对Festo CPX-CEC-C1 和 CPX-CMXX PLCs具有网络访问权限的攻击者可利用该漏洞。

第三个漏洞和CODESYS V3运行时环境中使用弱加密来保护下载代码和引导应用过有关（CVE-2022-4048，CVSS 7.7）。恶意人员可利用该漏洞部署并操纵源代码，从而损坏机密性和完整性防护措施。

研究人员还发现了影响 Festo CPX-CEC-C1 控制器的两个已知 CODESYS 漏洞（CVE-2022-31806和CVE-2022-22515），它们源自Control 运行时环境中的不安全配置，可导致拒绝服务扫描认证情况。

研究人员指出，“这个案例再次说明了漏洞未在所有受影响产品中得到披露的供应链问题。”

建议组织机构发现并清点易受攻击设备，执行适当的网络分段控制，并监控网络流量中的异常活动。

---

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSZu3o6N7v8IvXlaSpv9pqrC38BdYic1GvE8xzpEraJy9nHYRGk5rCC0dHKEfBr2rC1nJ8gMCDIvIw/640?wx_fmt=jpeg)

**推荐阅读**

[在线阅读版：《2022中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&chksm=ea94853cdde30c2a963cfa00a536764ea55cdee7ba6ef4a7716a28f82a97ca630dc271ee5224&scene=21#wechat_redirect)

[在线阅读版：《2021中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505380&idx=1&sn=01d2f5af200abc6bb20411ee8f17b6b5&chksm=ea94e48edde36d98f20b66aecf9f359e49226b411872bcea527fcca0a5de018f407415313800&scene=21#wechat_redirect)

[微软GitHub Copilot 被诉违反开源许可条款和侵犯开发人员权益](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514414&idx=1&sn=a937561278e4afeadc5816a57d8be22c&chksm=ea948844dde301521c4b577e4e0e5e3292436a79499f9b3e00726bd0f3a03f3400c521010ded&scene=21#wechat_redirect)

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

[开源软件 LibreOffice 修复多个与宏、密码等相关的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513283&idx=1&sn=5fbd02e0f95926cab449829326e0a8a1&chksm=ea9485a9dde30cbf0fb5e64dcbabdcbc1486306bbf9305df01d0f12022f30b84421fe09b167c&scene=21#wechat_redirect)

[Juniper Networks修复200多个第三方组件漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512960&idx=1&sn=0df41cf06e3efd8089ec6d6d6b03fc20&chksm=ea9482eadde30bfc407cd490459c7c947bbf2496475946f0379...