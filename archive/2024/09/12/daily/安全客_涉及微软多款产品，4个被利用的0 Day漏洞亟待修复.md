---
title: 涉及微软多款产品，4个被利用的0 Day漏洞亟待修复
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649786863&idx=1&sn=830d42f5a9877e0226f0be133543e6a8&chksm=8893b980bfe430960a4d3f99dfd5fefe6d1c298ab14665d4cccab6322be1d5689712b289b465&scene=58&subscene=0#rd
source: 安全客
date: 2024-09-12
fetch_date: 2025-10-06T18:28:36.724600
---

# 涉及微软多款产品，4个被利用的0 Day漏洞亟待修复

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb4Mz500lzfSdDb2GMwEsbXoNdcIMuiaavQLMLfgRrkibfpNmCib4W8bUrX9HcU8q7fhP7QJMq21lcjcw/0?wx_fmt=jpeg)

# 涉及微软多款产品，4个被利用的0 Day漏洞亟待修复

安全客

近日，微软发布了79个修复补丁，其中包括针对几个被攻击者在实际环境中利用的0 Day漏洞（CVE-2024-38217、CVE-2024-38226、CVE-2024-38014、CVE-2024-43461）以及一个导致Windows 10早期CVE修复失效的代码缺陷（CVE-2024-43491）。

**NEWS**

**被积极利用的漏洞**

首先，我们来看一下唯一一个之前已公开的漏洞：CVE-2024-38217，这是一个允许攻击者绕过“网页标记”（Mark of the Web, MotW）的漏洞。

Elastic Security研究员Joe Desimone报告称，这个漏洞已经被攻击者利用多年，他们通过构造具有非标准目标路径或内部结构的Windows快捷方式文件（.LNK）进行攻击。

这些文件会迫使Windows“重写”它们并移除MotW元数据，从而导致安全特性如SmartScreen应用程序声誉检查和旧版Windows附件服务安全提示的完整性和可用性受到影响。

接下来是CVE-2024-38226，这是另一个允许攻击者绕过安全功能的漏洞。该漏洞影响Microsoft Publisher，这是一款独立应用程序，也包含在某些版本的Microsoft Office中。

微软解释道，“攻击本身是由一个对目标系统已认证的用户在本地执行的。经过认证的攻击者可以通过社会工程学说服受害者从网站下载并打开一个特制的文件，从而在受害者的计算机上发起本地攻击。”

显然，有人成功绕过了Office宏策略，在目标计算机上执行了恶意代码。遗憾的是，微软没有透露是谁报告了这个漏洞，因此我们无法推测该漏洞被利用的攻击性质。

另一个被利用的0 Day漏洞是CVE-2024-38014，这个漏洞存在于Windows Installer中，可能允许经过认证的攻击者提升权限至SYSTEM级别。

Trend Micro零日计划负责人Dustin Childs指出：“有趣的是，微软表示这个漏洞不需要用户交互，所以实际的利用机制可能比较特殊。不过，这类权限提升漏洞通常会与代码执行漏洞配合使用，以控制系统。”他建议“快速测试和部署这个修复。”

Tenable高级研究工程师Satnam Narang补充道，由于权限提升漏洞通常与后期入侵活动有关，它们可能不会像远程代码执行漏洞那样受到广泛关注。但这类漏洞对攻击者来说非常有价值，因为它们可以造成更多损害或获取更多数据，因此组织必须确保修复这些漏洞，以切断攻击路径，防止未来的入侵。

CVE-2024-43461是一个Windows MSHTML平台伪装漏洞，目前尚未描述为在实际环境中被利用，但Childs表示它应被视为高风险漏洞。

“这个漏洞类似于我们在7月报告并修复的漏洞。ZDI威胁狩猎团队在6月发现了这个漏洞并报告给微软。看来威胁行为者很快绕过了之前的修复，”他指出。“我们报告这个漏洞时表示它正在被积极利用，但不清楚为何微软没有将其列为活跃攻击。应将其视为高风险漏洞，特别是它影响所有受支持的Windows版本。”

**NEWS**

**其他值得关注的漏洞**

CVE-2024-43491是一个有趣的漏洞，它有效地使得一些影响WindoCVE-2024-43491是一个有趣的漏洞，它使得影响Windows 10版本1507的一些可选组件（如Internet Explorer 11、Windows Media Player、MSMQ服务器核心等）的修复回滚。

Immersive Labs的高级威胁研究总监Kevin Breen指出，“这个漏洞影响了Windows更新系统，使得某些组件的安全补丁被回滚到易受攻击的状态，自2024年3月以来一直处于这种状态。这些组件中有些曾在实际环境中被利用过，这意味着尽管Windows更新显示已完全修补，但攻击者仍可能利用这些组件。”

不过，微软表示尚未检测到对CVE-2024-43491本身的利用。微软的Windows产品团队发现了这个问题，但没有证据表明它在公开场合被知晓。

另一个好消息是，受影响的Windows 10系统仅占少数。用户/管理员应检查公告，确认机器是否受影响，并按照顺序安装“2024年9月的服务堆栈更新（SSU KB5043936）和2024年9月的Windows安全更新（KB5043083）。”

在微软认为更可能被利用的修复漏洞中，有四个Microsoft SharePoint漏洞（CVE-2024-38018、CVE-2024-38227、CVE-2024-38228、CVE-2024-43464），这些漏洞可能被用来在SharePoint服务器上实现远程代码执行。尽管这四个漏洞都要求攻击者首先进行认证，但SharePoint管理员应该及时实施这些修复。

文章来源：

https://www.helpnetsecurity.com/2024/09/10/cve-2024-38217-cve-2024-43491/

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4Mz500lzfSdDb2GMwEsbXokqSWLtI1fdUaJn5JEF24bfgs8bQLpYz6q4Kc8Q2c7WWkO8rDrH5icvg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4Mz500lzfSdDb2GMwEsbXogZtbJBCtkFRz6tTNkaLtsIeXcgtUVQ94rgvaxU6ZXfz6qDDewZu3qw/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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