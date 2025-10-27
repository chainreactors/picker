---
title: 451个PyPI包被指安装Chrome扩展窃取密币
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515546&idx=2&sn=dff1912bb356843ce867ca344a5f21c1&chksm=ea948cf0dde305e685ca1501ecbff82caea554592b685d602b01eab7e8f49635838103871733&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-02-15
fetch_date: 2025-10-04T06:38:02.502794
---

# 451个PyPI包被指安装Chrome扩展窃取密币

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS2eLJXXAakjqDbHJykRr3qOicLCTPniaWhA29wAKYgd7ictPqsAXItoh0giaeLZNhBodLNPLImPNqfuw/0?wx_fmt=jpeg)

# 451个PyPI包被指安装Chrome扩展窃取密币

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

**Phylum公司表示，超过450个恶意PyPI python 程序包安装恶意浏览器扩展，劫持通过基于浏览器的密币钱包和网站进行的密币交易。**

该攻击活动始于2022年11月，最初仅有27个恶意PyPI包参与，而现在恶意包数量已达到450个。这些恶意包通过细微改动假冒热门包即typosquatting方式，欺骗软件开发人员下载。Phylum 公司发布报告解释称，除了扩大攻击活动规模外，攻击者现在还利用一种新型的混淆方式实施攻击。

**0****1**

**新一轮的typoquatting攻击潮**

其中一些遭假冒的流行包包括bitcoinlib、ccxt、cryptocompare、cryptofeed、freqtrade、selenium、solana、vyper、websockets、yfinance、pandas、matplotlib、aiohttp、beautifulsoup、tensorflow、selenium、scrapy、 colorama、scikit-learn、pytorch、pygame和 pyinstaller。

攻击者为如上热门包使用13到38种typosquatting版本，试图覆盖将导致下载恶意包的一系列潜在输入错误。为躲避检测，攻击者利用未出现在2022年11月攻击潮的一种新型混淆方式，即在函数和变量标志符中使用随机的16位汉字标志组合。

分析人员发现，代码使用内置的Python函数和一系列算数运算生成字符串。因此，虽然混淆创建了看上去很强大的结果但不是太难以攻破。报告提到，“虽然这种混淆构建了及其复杂和高度混淆的代码，但从动态角度看并不高明。Python是解释型语言，代码必须运行。我们只要评估这些实例，就会获悉代码到底在做什么。”

**0****2**

**恶意浏览器扩展**

为了劫持密币交易，恶意PyPI包将在文件夹 '%AppData%\Extension' 中创建恶意Chromuim浏览器扩展，这种手法类似于2022年11月的攻击手法。之后，它们会搜索和谷歌Chrome、微软 Edge、Brave和Opera相关的Windows快捷键并劫持，通过命令行参数 “—load-extension”来加载恶意浏览器扩展。例如，Chrome 快捷键会被劫持到  "C:\Program Files\Google\Chrome\Application\chrome.exe --load-extension=%AppData%\\Extension"。当web 浏览器启动时，该扩展将加载，而恶意JavaScript将监控复制到Windows剪贴板上的密币地址。当检测到密币地址时，该浏览器扩展将通过受控的硬编码地址取而代之。攻击者通过这种方式将密币交易额发送到攻击者的钱包而非本来的收件人。

在这一新型攻击活动中，攻击者扩大了受支持钱包的数量，当前增加了Bitcoinm Ethereum、TRON、Binance Chain、Litecoin、Ripple、Dash、Bitcoin Cash 和 Cosmos 的密币地址。

这些恶意包名称如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS2eLJXXAakjqDbHJykRr3qdEQdFNQ6iczzDH5L08ibxNl1J5RX5gWKahiaYERKaM7NribNWt12sgAbkA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS2eLJXXAakjqDbHJykRr3qx1BCuSCy2aBmFwbBxu6Tmm5jN2jQaeUxcQ7TwOntHkod5iasicmXGcbA/640?wx_fmt=jpeg)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSZu3o6N7v8IvXlaSpv9pqrC38BdYic1GvE8xzpEraJy9nHYRGk5rCC0dHKEfBr2rC1nJ8gMCDIvIw/640?wx_fmt=jpeg)

**推荐阅读**

[在线阅读版：《2022中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&chksm=ea94853cdde30c2a963cfa00a536764ea55cdee7ba6ef4a7716a28f82a97ca630dc271ee5224&scene=21#wechat_redirect)

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[深度分析：美国多角色参与的软件供应链安全保护措施](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515534&idx=1&sn=32d0d289fcc99c859325f35101773d65&chksm=ea948ce4dde305f2309ea1b9ca9e601ef74b05fdc0b35935a43334c65bb8bc47ca179b818fa9&scene=21#wechat_redirect)

[在线阅读版：《2021中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505380&idx=1&sn=01d2f5af200abc6bb20411ee8f17b6b5&chksm=ea94e48edde36d98f20b66aecf9f359e49226b411872bcea527fcca0a5de018f407415313800&scene=21#wechat_redirect)

[热门开源Dompdf PHP 库中存在严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=2&sn=6ff90ed5a1a5cfe857a4aa75a16def08&chksm=ea948c2edde305386563b822262353daa67aecbbe719fdcbf7b97f402220ee247091ea7aeac0&scene=21#wechat_redirect)

[命令注入漏洞可导致思科设备遭接管，引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515439&idx=1&sn=bb8d8abcbaaf7e2be431ab9cd0712617&chksm=ea948c45dde30553179da977f93800b8c57d85c6185257361358931ab913191be82c3079d54c&scene=21#wechat_redirect)

[命令注入漏洞可导致思科设备遭接管，引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515439&idx=1&sn=bb8d8abcbaaf7e2be431ab9cd0712617&chksm=ea948c45dde30553179da977f93800b8c57d85c6185257361358931ab913191be82c3079d54c&scene=21#wechat_redirect)

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

[黑客攻陷Okta发动供应链攻击，影响130多家组织机构](http://m...