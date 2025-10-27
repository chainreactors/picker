---
title: 多个BMC供应链漏洞现身，数十家厂商生产的服务器受影响
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514911&idx=2&sn=a07e3f6f6557db4b5408f3f337728a4c&chksm=ea948a75dde3036344fe266d8db84bdd445070bc070dfd60d49eaeb5317d40dc0f3cb80d4e0a&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-12-07
fetch_date: 2025-10-04T00:42:51.922391
---

# 多个BMC供应链漏洞现身，数十家厂商生产的服务器受影响

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTuVPuqrDOhQATDPibArtr44vbDYtz1MnM0ObQBhPoI528ceboN00V5hSKBsQdtdMHic0G73GyhPtgg/0?wx_fmt=jpeg)

# 多个BMC供应链漏洞现身，数十家厂商生产的服务器受影响

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

**AMI MegaRAC 基板管理控制器 (BMC) 软件中存在三个漏洞，可导致攻击者在易受攻击的服务器上执行远程代码。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44iaRva35OibIvs1roVLvrW4lAHWqFFib0icaa4iaNacVLLlsoIqI2RhB9XPg/640?wx_fmt=gif)

固件和硬件安全公司 Eclypsium 发布报告指出，“利用这些漏洞可导致远程控制受陷服务器、远程部署恶意软件、植入勒索软件和固件以及造成服务器物理损坏。”

BMC是服务器中的权限独立系统，用于控制低层硬件设置并管理主机操作系统，甚至适用于机器关机的场景。这些能力使BMC成为有意在设备上植入持久性恶意软件的威胁行动者的香饽饽，这些恶意软件在系统重装和硬件驱动替换的情况下仍然可保持持久性。

这些漏洞被称为 “BMC&C”，可被能够访问远程管理接口如 Redfish 的攻击者利用，从而可能控制系统并威胁云基础设施。

在这三个漏洞中，最严重的是CVE-2022-40259（CVSS 评分9.9），它是一个任意代码执行漏洞，攻击者拥有最低访问权限即可实施攻击。CVE-2022-40242（CVSS评分8.3）和可被破解与滥用从而获得shell 访问权限的一个系统用户哈希有关。CVE-2022-2827（CVSS评分7.5）是位于密码重置特性中的一个漏洞，可用于判断具有特定用户名称的账户是否存在。

研究人员解释称，“CVE-2022-2827可用于精准定位预存在的用户，不会导致获得shell但会为攻击者提供可执行暴力破解或凭据填充攻击的目标清单。”

这些研究结果再次强调了保护固件供应链安全且确保BMC系统未直接暴露到互联网中的重要性。该公司指出，“随着数据中心倾向于在特定硬件平台上进行标准化，任何BMC级别的漏洞将很可能适用于大量设备且可能影响整个数据中心或所交付的服务。”

前不久，Binarly 公司披露了位于基于AMI设备中的多个高危漏洞，它们可导致在早期启动阶段的内存损坏和任意代码执行后果。今年5月初，Eclypsium 公司还披露了名为“Pantsdown”的BMC漏洞，它影响 Quanta Cloud Technology (QCT) 服务器，如遭成功利用可导致攻击者完全控制设备。

---

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSZu3o6N7v8IvXlaSpv9pqrC38BdYic1GvE8xzpEraJy9nHYRGk5rCC0dHKEfBr2rC1nJ8gMCDIvIw/640?wx_fmt=jpeg)

**推荐阅读**

[在线阅读版：《2022中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&chksm=ea94853cdde30c2a963cfa00a536764ea55cdee7ba6ef4a7716a28f82a97ca630dc271ee5224&scene=21#wechat_redirect)

[在线阅读版：《2021中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505380&idx=1&sn=01d2f5af200abc6bb20411ee8f17b6b5&chksm=ea94e48edde36d98f20b66aecf9f359e49226b411872bcea527fcca0a5de018f407415313800&scene=21#wechat_redirect)

[IBM Cloud 漏洞可用于发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514887&idx=2&sn=fc8fe04678c1bb7757a64344a8fc5b41&chksm=ea948a6ddde3037b34cd376b259012b87fa9489ccb342643bf2a24ce8e6af5c5d86a3fe761d6&scene=21#wechat_redirect)

[GitHub Actions 漏洞可导致攻击者投毒开发管道](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514872&idx=2&sn=99f948eba89e5ef6fd054c745dfde955&chksm=ea948b92dde30284a5e685e93453fec9d40647f629a76e60c63121549900e3970308a1fce8b7&scene=21#wechat_redirect)

[美国开源软件安全评价方法体系分析](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514771&idx=1&sn=e77f88ada5f793bcb5eced9745ddc38a&chksm=ea948bf9dde302efe8a6a97ffa33c09123350b4ceecd9625e100c19714e9be9b3fff525d46b2&scene=21#wechat_redirect)

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

[开源web应用中存在三个XSS漏洞，可导致系统遭攻陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513307&idx=2&sn=4a99112b...