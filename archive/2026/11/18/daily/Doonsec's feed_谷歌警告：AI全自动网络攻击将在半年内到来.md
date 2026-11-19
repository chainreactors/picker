---
title: 谷歌警告：AI全自动网络攻击将在半年内到来
url: https://mp.weixin.qq.com/s/UV65s__SUfgxBmJ5RUYYVw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:39:47.009322
---

# 谷歌警告：AI全自动网络攻击将在半年内到来

# 谷歌警告：AI全自动网络攻击将在半年内到来

e安在线
e安在线

e安在线

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hxdb7gjfn9l5u0V88wJrxfYnum7HVRFbON58cZIOAVuqfEad28Ws4bKBLfpIAbfULIKVTLfQicOOghic93Xiaq8gDL9oz9Z9QUSGQjJibPpr0TY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9n11X5zP9AGgJf90o4zicm6n4FYv1m5O1Dwnqp7ELzHGGbAsfEv42jzCjuicuTzCM4mST66uL88IO9HicibrVqj4pLp9SuWWvp7Vos/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kMibdW2I4S0vic7G0A0ia7nkmwwS1Tu7Pqb0pQPoW3JGQsy5PicMrepWsticb1siaHIaN7WiaCe6bDUx89ZBX4zEBeSy2U4ye582rocs/640?wx_fmt=png&from=appmsg)

**谷歌威胁情报部门发布最新报告称，AI智能体攻击活动已经突破重大门槛，已有威胁组织在攻击法国系列目标时，攻击智能体实现了漏洞发现到利用全程自动化；**

**近期全球也出现了大量基于AI智能体的网络攻击，大量组织中招导致数据泄露乃至更严重影响，甚至FBI也点名警告ARTEX等渗透测试智能体；**

**据谷歌预测，预计半年内，将会出现技术复杂、完全自主的智能体攻击，这将对全球的关键基础设施网络防护造成巨大压力。**

攻击者正开始借助AI驱动的攻击框架构建智能体工作流，自动发现并利用软件漏洞，让攻击速度快得像机器自动运行一样。

谷歌威胁情报小组（GTIG）发现，AI最初只是在攻击流程中用作一些试验性应用，如今已被大规模用于网络攻击。使用者既包括以经济利益为目的的黑客组织，也包括国家支持的黑客组织。

其中一个典型案例是，攻击者使用开源多智能体渗透测试框架CAIRN，对美国航空航天领域发动攻击。另一起案例中，疑似朝鲜黑客利用Claude Code投放恶意软件。

研究人员预计，未来三个月内，攻击者将能够发动一些技术门槛较低的攻击。这类攻击几乎不需要人工参与，主要依靠多个AI智能体协同完成。

他们还预测，未来六个月内，很可能会出现技术复杂、完全自主的智能体攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9mfmgSW9LMMOgU89txGuLzUZoxicoxJX1Ng975buzVZTj3KEofsSUROYBMaq6jL1WE92nzj3rHEKgystgAa03cg9Y1jez5hAZIs/640?wx_fmt=png&from=appmsg)

图：AI在网络攻击中的应用演变

上周，美国联邦调查局（FBI）发布警告称，自8月以来，多个攻击者已开始将ARTEX AI渗透测试框架武器化，并以金融、政府、科技、国防、医疗卫生等领域的机构为目标发动攻击。

**利用AI发现并利用漏洞**

谷歌表示，攻击者正有意滥用开源渗透测试工具套件，实施全自动化攻击。相关工具包括ARTEX、CAIRN、CyberStrikeAI和HexStrike AI。

攻击者利用这些框架，针对暴露在互联网上、漏洞相对简单的系统发动自适应攻击。大模型（LLM）能够轻易针对这类漏洞生成攻击代码。

谷歌威胁情报小组在其《AI威胁追踪报告》中披露了一起案例：黑客利用名为“exploit\_agent”的多智能体系统，对法国媒体、娱乐和教育类网站发动攻击，从漏洞发现到漏洞利用全程自动化。

谷歌表示：“在过去一个季度中，GTIG首次发现攻击者利用大模型框架，在没有人工介入的情况下，完全自动化地完成漏洞发现和利用。”

“具体而言，GTIG发现了一台对外暴露的测试服务器。该服务器托管着一个用于漏洞研究和攻击武器化的多智能体框架，名为exploit\_agent。该框架能够接入多个前沿大模型和本地部署的大模型。”

谷歌通过攻击者对外暴露的测试服务器发现了这一框架。服务器中还存有被盗取的受害者数据、侦察信息、WebShell以及暴力破解脚本。

该系统能够分析热门Web应用的软件更新，寻找可能存在的安全漏洞，并自动尝试利用这些漏洞发动攻击。

谷歌警告称，此类框架投入攻击后，大幅压缩了防御方修补系统漏洞的时间，同时也会产生大量误导性信息，加重安全防护工作的负担。

研究人员以近期的PHP2Shell事件为例指出，PHP官方公布两个漏洞后不久，网上便出现了数百个所谓的概念验证（PoC）漏洞利用代码，其中大部分由AI生成。这给防御人员带来了额外压力，他们不得不逐一验证代码，并制定相应的防护措施。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9nmPfdLIQ3NrZ65I3rpMfvHicXRRUoXib6rjClzYmve4ml7w7wZBOQfYU3XuOibsMXOAeIuPoHdyq7hToZiae3b1MyQX2TDToHR8ps/640?wx_fmt=png&from=appmsg)

图：每月遭利用的漏洞数量

**AI在网络攻击中的其他利用趋势**

除自动化攻击外，谷歌还发现，一个代号为UNC6836的攻击集群近期利用经过修改的Claude Code，针对北美和欧洲的加密货币企业发动了多起攻击。该集群疑似与“Midnight Neptune”有关联。

攻击者初步入侵目标系统后，修改了Claude Code应用的设置，使其在启动时自动下载名为SOMBERMEME的后门程序。

谷歌报告还指出，国家支持的组织、商业供应商和政治网络已开始常态化利用AI开展舆论影响活动。

此外，大模型劫持（LLMjacking）已成为普遍问题。攻击者正越来越多地把它当作新的牟利渠道，受害机构则因此承担高昂成本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9nQgIgiaZiahXLk6W4R355jG2k48ufOG4jialgFYkD7mnRI41WrfRHNhcicXBaXjbMGtHYfPA7IZCtwSe9oxhA7ObgmEPMNTvayUicE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kEYS4iajycgtuzx0qicd8K4eqQnYDw3nXTBbYhubeEKvxNjvnr51FHxdBEzDHTL3sMKhL8HmibzxnpPuLdJ9C0r3icKS4QdzE0WWc/640?wx_fmt=png&from=appmsg)

声明：除发布的文章无法追溯到作者并获得授权外，我们均会注明作者和文章来源。如涉及版权问题请及时联系我们，我们会在第一时间删改，谢谢！文章来源：安全内参

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9n8waloBV8EL8CU1PGU1A8HThFiciaMuibY4pvrMqL49OEAALZj8JxCKNW6USyIkZaKHCqAAz2jLUPic7hZjvNnZQqdJET17BehP1g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9kKZrbCUMZWXxj2Zib35OuHZicqnBvNOIfN7p0ycuDhY4HElGljfWoy84daGXbLEdmszBnG4Ul39iblicbxAzS6YVgMrQ8QIldiaUAM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kNRaZfN2WejnPxrMy9FiclcPEsnhXiaiba3VwlR35qic7BjJ9ZrEcZK4eiajorpyiaZvOnicQGQ9bias3ha2icxAibDg2sLXicURNibr1OVxc/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1Y08O57sHWiaro9eC87veL2BfoUwAjnOfbTbGQwSaaunoz9m7KFdFkib1pMyMoNY4tVtskNSHickKmn7Nza8WGTeA/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过