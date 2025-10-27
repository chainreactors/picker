---
title: Python 开发人员提醒：PyPI 木马包假冒流行库发动攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515700&idx=2&sn=28c134528939223ed316b6f5b450dcd6&chksm=ea948f5edde306489a6bb564bbb5995de242208d44ab2dde95fce873e09f15d1fc295584cb61&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-02-25
fetch_date: 2025-10-04T08:04:43.328640
---

# Python 开发人员提醒：PyPI 木马包假冒流行库发动攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQZeSribxs2yU1w56EMvgX9cibEWoDwFM4f7lBL8cfQtIcQm2ctmIasLDXSFOzy1VxdcW7Ln07LWicAw/0?wx_fmt=jpeg)

# Python 开发人员提醒：PyPI 木马包假冒流行库发动攻击

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

**网络安全研究员提醒称，“假冒的程序包”正在模仿PyPI 仓库上可用的流行库。**

研究人员提到，42款恶意PyPI 包伪装成合法模块如HTTP、AIOHTTP、请求、urllib和urllib3的typosquatted 变体，它们的名称是：aio5、aio6、htps1、httiop、httops、httplat、httpscolor、httpsing、httpslib、httpsos、httpsp、httpssp、httpssus、httpsus、httpxgetter、httpxmodifier、httpxrequester、httpxrequesterv2、httpxv2、httpxv3、libhttps、piphttps、pohttp、requestsd、requestse、requestst、ulrlib3、urelib3、urklib3、urlkib3、urllb、urllib33、urolib3和xhttpsp。

ReversingLabs 的研究员Lucija Valentić指出，“这些包的描述大多不会提到恶意意图。某些包伪装成真实库并对比它们和已知、合法HTTP库之间的对比。”但实际上它们利用下载器作为管道，向受感染主机或信息窃取工具传播第二阶段的恶意软件，窃取敏感数据如密码和令牌。

Fortinet 公司也在本周早些时候披露了PyPI 上的恶意HTTP包，提到这些恶意包推出木马下载器，其中包括打包了多种函数的DLL 文件 (Rdudkye.dll)。

这41个恶意PyPI 包是恶意人员投毒开源库如GitHub、npm、PyPI 和Rubygems，将恶意软件传播到开发者系统并发动供应链攻击的最新例证。

一天前，[Checkmarx 公司提到开源npm 注册表中的垃圾包激增，它们的目的就是将受害者重定向到钓鱼链接](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515685&idx=3&sn=585c317461d2d139b03552687e9f8520&chksm=ea948f4fdde306597b21a8fcf3bfd316531608c05576ecdc861a765a86575def468ff9fe5eb1&scene=21#wechat_redirect)。

Valentić 指出，“和其它供应链攻击一样，恶意人员正在利用 typosquatting 制造混淆，并利用不谨慎的开发人员不慎使用名称类似的恶意包。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSZu3o6N7v8IvXlaSpv9pqrC38BdYic1GvE8xzpEraJy9nHYRGk5rCC0dHKEfBr2rC1nJ8gMCDIvIw/640?wx_fmt=jpeg)

**推荐阅读**

[在线阅读版：《2022中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&chksm=ea94853cdde30c2a963cfa00a536764ea55cdee7ba6ef4a7716a28f82a97ca630dc271ee5224&scene=21#wechat_redirect)

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[在线阅读版：《2021中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505380&idx=1&sn=01d2f5af200abc6bb20411ee8f17b6b5&chksm=ea94e48edde36d98f20b66aecf9f359e49226b411872bcea527fcca0a5de018f407415313800&scene=21#wechat_redirect)

[NPM仓库遭逾1.5万个垃圾邮件包的钓鱼攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515685&idx=3&sn=585c317461d2d139b03552687e9f8520&chksm=ea948f4fdde306597b21a8fcf3bfd316531608c05576ecdc861a765a86575def468ff9fe5eb1&scene=21#wechat_redirect)

[SolarWinds 称将在2月底修复多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515647&idx=3&sn=e5d9ae1f0396aaa5c5eb758484fb760b&chksm=ea948c95dde3058339a2b4d43a851fdc2441afec55b15919595ce8d9f6b98ea46b38a0e06ae3&scene=21#wechat_redirect)

[第三方app受陷，Atlassian 数据被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515624&idx=3&sn=67fc0501190042defabcc173a6eb618f&chksm=ea948c82dde30594c6d827c3f9a2ec0f74bc3ac9f01de20c08188c4f469b2a74cbf9381d0a01&scene=21#wechat_redirect)

[奇安信总裁吴云坤：构建四大关键能力 体系化治理软件供应链安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515606&idx=1&sn=be020e0c8715a3f3b2c31a379ca01e0d&chksm=ea948cbcdde305aab8950259a837c775cd6fb12d0db8801e92776fcae41529ce655f3a18ff6c&scene=21#wechat_redirect)

[几乎所有企业都与受陷第三方之间存在关联](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515478&idx=1&sn=759fe4b09a25bbfa2b215044d8c0ebbc&chksm=ea948c3cdde3052aabad27c5aebc6c4f97bc84d8ab2bb490162e86c1848b9c8ac80b8dd56327&scene=21#wechat_redirect)

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

[Apache开源项目 Xalan-J 整数截断可导致任意代码执行](http://mp.weixin.qq.com/s?__biz=MzI2NTg4...