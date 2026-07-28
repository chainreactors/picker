---
title: 弹窗不是打扰，是终端安全防线的“特洛伊入口”
url: https://mp.weixin.qq.com/s/u8UiSSRLfBW6U983HScy0A
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:58:22.743163
---

# 弹窗不是打扰，是终端安全防线的“特洛伊入口”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mOJLHzw95XLlBoVxsq1xwUJC0d6BwoYkygFtpLicO8XILriaOxfJ8tuibE4RqQWGDcZNZ61ghibCBnBt1enSNn4pAkeSpbD4T37AukbnS4d4Z2Q/0?wx_fmt=jpeg)

# 弹窗不是打扰，是终端安全防线的“特洛伊入口”

何威风
何威风

祺印说信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近期，微软针对Windows 11中第三方软件推广、广告弹窗以及“臃肿软件（Bloatware）”问题采取了限制措施，并表示Windows生态不应成为未经用户明确授权的软件推广渠道。该事件起因于部分用户反馈，在连接某些硬件设备（如特定型号显示器）后，Windows 11环境中出现了由厂商软件触发的第三方安全软件推广弹窗，引发了用户对“未经充分授权即安装软件”的担忧。微软随后介入，要求相关厂商停止此类推广行为。表面上看，这是一次关于“广告是否影响用户体验”的商业争议，但从网络安全角度深入剖析，其本质涉及操作系统信任边界、软件供应链安全、用户授权控制以及终端安全治理等一系列深层次问题。

所谓Bloatware（臃肿软件），一般指随设备、操作系统或驱动程序预装，但用户并非主动选择安装的软件，典型形式包括试用版安全软件、游戏客户端、厂商管理工具、推广应用、云服务客户端以及浏览器推广组件等。许多用户在购买电脑并首次启动Windows后，往往会发现系统中已存在大量并非自己需要的第三方软件，进而产生“我购买的是设备和操作系统，而不是一个广告平台”的认知落差。本次Windows 11事件正是这种矛盾的集中体现，争议核心包括两个层面：一是软件是否经过明确授权——正常情况下，用户点击安装、明确授权后才应安装软件，但如果连接硬件后系统自动安装组件并弹窗推广第三方软件，用户便会认为系统替自己做了安全决策；二是谁应该承担信任责任——现代Windows生态由微软Windows Update、硬件厂商驱动、第三方软件和Microsoft Store共同构成复杂的供应链，用户通常认为来自Windows更新渠道的软件应该可信，因此一旦该渠道被用于推广软件，便容易导致信任下降。

很多人认为广告只是体验问题，但在安全治理中，推广软件和恶意软件之间存在着一个灰色区域。推广软件往往未经用户主动安装即可长期驻留系统，并获得运行权限，进而扩大系统的攻击面，安全行业通常将这类软件归类为PUA（潜在不受欢迎应用）或PUP（潜在不受欢迎程序）。它们不一定是恶意软件，但可能消耗系统资源、收集用户行为数据、修改系统设置或增加漏洞暴露面，从而在终端上埋下安全隐患。从供应链安全的角度审视，Windows 11事件反映的是现代软件供应链的复杂性——传统模型中“微软提供操作系统、用户直接使用”的线性关系早已不复存在，取而代之的是操作系统、驱动程序、硬件厂商软件、第三方服务、云平台等多个环节层层嵌套的立体结构，任何一个环节都可能影响终端安全。硬件厂商软件若获得系统安装权限，便可部署第三方组件，扩大攻击面，这与近年来软件供应链攻击的趋势高度一致，攻击者越来越关注软件更新机制、驱动程序、第三方插件和管理工具，因为用户信任供应链，所以攻击供应链。

从安全架构的视角来看，广告问题与身份攻击实际上具有相似的逻辑。在CertiGhost这类身份攻击中，攻击者冒用可信身份获得系统信任继而获取权限；而在软件推广问题中，厂商软件利用可信更新渠道进入系统，用户基于对微软的信任而接受了未经主动选择的软件。二者的本质都是利用了“信任链”，区别仅在于一个用于攻击、一个用于商业推广，但安全治理的原则是一致的——谁获得信任，谁就必须承担更高的责任。在企业环境中，这一风险更加明显。对于个人用户可能只是弹窗或资源占用，但企业终端一旦自动安装第三方软件并获得终端权限，连接企业网络后便可能成为攻击入口，造成软件资产失控、未授权软件进入生产环境、违反安全基线、增加漏洞数量等一系列严重后果。

结合我国等级保护体系的要求，这类问题实际上对应着多个安全控制点。在安全管理中心方面，企业应掌握终端设备的软件安装清单、版本信息、授权情况及安全状态，杜绝“企业不知道员工电脑安装了什么”的盲区。在安全计算环境方面，应重点加强软件安装控制、应用白名单、终端安全管理和权限控制，例如禁止普通用户安装未知软件或修改安全配置。在供应链安全管理方面，企业在采购PC设备、操作系统、驱动和管理软件时，应关注供应商的软件组成、第三方组件、更新机制和安全责任，确保全链条可控。针对上述风险，企业应建立软件准入制度，明确允许办公软件、安全软件和业务软件，禁止未知插件、推广软件和未经审批软件进入终端；同时建立软件资产管理（SAM）体系，记录软件名称、版本、来源、安装时间、责任部门和授权状态等关键信息；并通过EDR、MDM或软件分发平台等终端管理工具，实现从发现、审批、安装到审计的闭环管理。

本次Windows 11事件虽然不是传统意义上的网络攻击事件，但它给企业安全治理带来了深刻的启示：过去企业重点关注漏洞、病毒和木马，而如今必须同样关注软件来源、安装路径、权限申请、更新机制和供应链责任。安全不仅是阻止黑客进入系统，也包括防止未经控制的软件进入系统。真正成熟的安全治理，不应只问“有没有安装杀毒软件”，还应追问“这个软件为什么存在？谁批准的？谁信任它？它获得了什么权限？”这正是现代网络安全从技术防护时代进入可信治理时代的重要标志。

****>>>**网络安全等级保护**<<<****

***[网络安全等级保护：等级保护工作、分级保护工作、密码管理工作三者之间的关系](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652098579&idx=1&sn=56da5aedb263c64196a74c5f148af682&chksm=8bbcfa2abccb733ca8dd898d7c0b06d98244ca76bd7be343482369fa80546554cced706fa74c&scene=21#wechat_redirect)***

***[网络安全等级保护：政策与技术“七一”大合集100+篇](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652108174&idx=1&sn=455ba77fd3a186100820b8d180fcd742&chksm=8bbcdfb7bccb56a17cc1d42b93895ecfb0b51a9417a5f63fc4482567c73fb46be0418d43b567&scene=21#wechat_redirect)***

***[网络安全等级保护：安全管理机构](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652109115&idx=2&sn=4f1af46e726949f4d038bde63c2362ef&chksm=8bbcd302bccb5a14b71aa1c242c14636fb3f4d37710e18db76bdcb91ab74a3aaa412f1226c7f&scene=21#wechat_redirect)***

*[网络安全等级保护：网络安全事件分类分级思维导图](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652109100&idx=1&sn=b0a47754b6df3f02f38daf7b7e23eb74&chksm=8bbcd315bccb5a032afa3441f65dfc391355834fbdf574ae6bce3caf42fa90766d80de1d6e84&scene=21#wechat_redirect)*

**>>>数据安全系列<<<**

***[数据安全管理从哪里开始](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652103384&idx=1&sn=391073e6109ff105f02be9029e01c697&chksm=8bbcc8e1bccb41f7fe478a3d22757d61f10dcf42548c1c02c0579b8f161277e527ba98ccb542&scene=21#wechat_redirect)***

*****[数据泄露的成本：医疗保健行业](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652109243&idx=2&sn=cd2405090c5d26f97c602946d3f8eea1&chksm=8bbcd382bccb5a94114aa6fda3d3ba0629eb958a6b7a9711889d552a029462d64ac97e3a46da&scene=21#wechat_redirect)*****

***[数据安全知识：数据安全策略规划](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652104021&idx=1&sn=7f80bb27ce6ad7c9debe83c172ff9f73&chksm=8bbccf6cbccb467a0971b9de4a8b14851c2666ad6934a88b8324a1ffc4b5cf5109cbc3976697&scene=21#wechat_redirect)***

***[数据安全知识：组织和人员管理](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652109274&idx=1&sn=7be5a754d4667aa47c46b16f1b4d0579&chksm=8bbcd3e3bccb5af52e3d908edb77e57505315689950e24754a3152a80528ab6745788a318ec3&scene=21#wechat_redirect)***

***[数据安全知识：数据库安全重要性](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652104183&idx=2&sn=f2a98256b0497ce3a99c0ad30223bf40&chksm=8bbccfcebccb46d8aac9f8a5c8d1f46061ca61ad69b3a61d52d3dc614e1e18ae65d982a5574b&scene=21#wechat_redirect)***

***[数据安全知识：数据整理与数据清理](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652105810&idx=2&sn=97ff4a8d1f2c7f3f6a0252f4df58b20b&chksm=8bbcc66bbccb4f7d058c46bc9c67d34c2042993f2ad32c7732d9816f8dfa4abb7e10f0fd307f&scene=21#wechat_redirect)***

***[数据安全知识：什么是数据存储？](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652108099&idx=1&sn=0ccf837988c4dc590d1fd9d634d0c02b&chksm=8bbcdf7abccb566cfa3ab37a304567fbca0833291b7f0cb99d36cdebd9d1f58ae72d03d82cd2&scene=21#wechat_redirect)***

***[数据安全知识：什么是数据风险评估？](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652106123&idx=1&sn=5f1a4c50b11a1155b22e8d5f01f5c6ca&chksm=8bbcc7b2bccb4ea46d1666254d8f027d2e68d4f38a621f4d7cc05d398f342a0eabeecb29be2e&scene=21#wechat_redirect)***

***[数据安全知识：如何逐步执行数据风险评估](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652106385&idx=1&sn=a71f4b9827f82daff6b5ff61d1f66d2d&chksm=8bbcc4a8bccb4dbe639df71411c12a859b26da7b4fd84b544effc20d98426fd628af59a8c868&scene=21#wechat_redirect)***

***[数据安全知识：数据风险管理降低企业风险](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652106372&idx=2&sn=9ad51e532256b7fbe3aefdf7ec804777&chksm=8bbcc4bdbccb4dabb0cd03a18862dd076ebd798a0bd2aae82a5916e8f9a04b53e5fcd344feb6&scene=21#wechat_redirect)***

***[数据安全知识：数据整理与数据清理](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652105810&idx=2&sn=97ff4a8d1f2c7f3f6a0252f4df58b20b&chksm=8bbcc66bbccb4f7d058c46bc9c67d34c2042993f2ad32c7732d9816f8dfa4abb7e10f0fd307f&scene=21#wechat_redirect)***

***[数据安全知识：什么是数据安全态势管理？](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652105525&idx=1&sn=8625752fb73b4da258b7df177ff8709d&chksm=8bbcc10cbccb481a1b0a68f1061dd2fdda08d2e58974c0fb3fd2c90c9fa77e0641ab814399b2&scene=21#wechat_redirect)***

***[数据安全知识：数据库安全重要性](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652104183&idx=2&sn=f2a98256b0497ce3a99c0ad30223bf40&chksm=8bbccfcebccb46d8aac9f8a5c8d1f46061ca61ad69b3a61d52d3dc614e1e18ae65d982a5574b&scene=21#wechat_redirect)***

***[数据安全知识：数据库安全威胁](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652103736&idx=2&sn=6d70e9d5690b4e3748460d641e14fce8&chksm=8bbcce01bccb47177fce9597fb30e8a27e00a9683e6afbcfb2ea7128a424504ff24af8aa54cc&scene=21#wechat_redirect)***

***[数据安全知识：不同类型的数据库](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652103688&idx=1&sn=9377838e11b62f5d73aa1dbda22ec178&chksm=8bbcce31bccb4727c19ada8cdf5d571227e363447987209eb77f4f07e240b1cd263c2de8a547&scene=21#wechat_redirect)***

***[数据安全知识：数据库简史](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652103686&idx=1&sn=abcfc1080a7641d41607cca4dc0fab1d&chksm=8bbcce3fbccb4729926a8249ec3bb0344a59268b7af49a68100c03839ace2c6ea59228e68c75&scene=21#wechat_redirect)***

***[数据安全知识：什么是数据出口？](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652103679&idx=1&sn=f23569ddbc6e5b5b39b307401a53a7f4&chksm=8bbcc9c6bccb40d06ee30f3e73257c08ff61d5aff33040f9a08513473a1f9619f285a531ef42&scene=21#wechat_redirect)***

***[数据安全知识：什么是数据治理模型？](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652103450&idx=1&sn=ce981cd32e6966e5bfd08e0e85ac6528&chksm=8bbcc923bccb4035b5bd145b2941e0f096cb26f0448a3c5f7fd1bf0652507f2470a33ea26fde&scene=21#wechat_redirect)***

**>>>错与罚<<<**

**[276人落网！河南新乡警方摧毁特大“网络水军”犯罪团伙](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652107934&idx=1&sn=3fdd7afb3d6a3f78a89264fee3d0b20f&chksm=8bbcdea7bccb57b19ec50b56f4d52ea88256f018bdaf52e71b0bb69c04b43b657068fc8873d3&scene=21#wechat_redirect)**

**[重拳出击严打涉网...