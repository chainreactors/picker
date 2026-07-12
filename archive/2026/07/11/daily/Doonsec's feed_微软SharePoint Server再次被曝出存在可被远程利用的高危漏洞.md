---
title: 微软SharePoint Server再次被曝出存在可被远程利用的高危漏洞
url: https://mp.weixin.qq.com/s/cmNeAPe6Bt7i2-nySnkZSw
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:10:30.023995
---

# 微软SharePoint Server再次被曝出存在可被远程利用的高危漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hfjKPyxBDjrWxEVau4JrQnxic8PVkXcKBvzttZto3KcKk5m9MAYAdibgDRE4zicI7jf3kAx6vXRBQUBLPczAq1PddVhuXUiciakBOHJydqIDGibDQ/0?wx_fmt=jpeg)

# 微软SharePoint Server再次被曝出存在可被远程利用的高危漏洞

原创

何威风
何威风

河南等级保护测评

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近期，微软SharePoint Server再次被曝出存在可被远程利用的高危漏洞，并已在实际攻击中被利用。美国网络安全与基础设施安全局（CISA）随后将相关漏洞纳入其已知被利用漏洞（KEV）清单，并发出紧急修复提醒，强调该漏洞已具备现实攻击风险，影响范围主要集中在本地部署的SharePoint服务器环境。

根据安全通报，该漏洞属于远程代码执行（RCE）类型，攻击者在未授权的情况下即可通过网络请求触发漏洞，从而在目标服务器上执行任意代码，进而获得系统级控制权限。微软已在此前的安全更新中对该漏洞进行了修复，但CISA指出，现实中仍存在大量未及时更新的系统，正在被攻击者扫描与利用。

与此同时，另一份安全分析指出，该漏洞已经被多个攻击活动纳入武器化利用链，攻击者往往通过组合多个SharePoint相关缺陷，实现从初始访问到权限提升再到持久化控制的完整攻击路径。在部分案例中，攻击者甚至可在补丁发布后仍通过残留访问或配置缺陷维持系统控制能力。

此类SharePoint漏洞的风险不仅局限于单一应用系统，而是可能进一步扩展至企业内部协作体系，例如文档管理系统、邮件服务以及与其集成的业务平台。一旦攻击成功，可能导致敏感数据泄露、内部横向移动以及关键业务中断等严重后果。

安全机构建议，相关组织应立即开展以下防护工作：一是核查 SharePoint Server 版本并确保更新至最新补丁；二是对公网暴露的 SharePoint 实例进行隔离或限制访问；三是启用日志审计与异常行为检测，重点关注可疑的远程执行行为；四是对已疑似受影响系统开展取证排查，以确认是否存在潜在入侵痕迹。

总体来看，本次事件再次表明，企业级协作平台已成为攻击者重点关注目标之一，而“已修复但未部署”的安全补丁窗口，正是当前最常见也最危险的攻击切入点之一。

---

[等保、关保、数保、个保，网络安全与数据治理“四位一体”的体系化制度框架](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505812&idx=1&sn=018455069df3d9894104953c6e14a91f&scene=21#wechat_redirect)

**[网络安全等级保护制度统一框架辨析](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505812&idx=1&sn=018455069df3d9894104953c6e14a91f&scene=21#wechat_redirect)**

---

**>>>等级保护<<<**

**[从资质驱动到能力驱动——新标准下测评机构的生与死](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[测评机构迎大考，安全厂商的机会来了！](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[测评机构的回旋镖来了！测评机构不仅要会“测别人”，更要先“管好自己”](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[新标准背景下等级测评机构应培养什么样的人才](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[供应链企业应该如何适应等级保护发展](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[网络安全等级保护制度演进，安全治理思维的演变](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

[网络安全等级保护之安全物理环境](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全区域边界](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全通信网络](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全计算环境](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全管理中心](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全管理制度](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全管理机构](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全管理人员](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全建设管理](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全运维管理](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

**[网络安全等级保护制度演进，回看2003年27号文](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[网络安全等级保护制度演进，回看2004年66号文](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505809&idx=1&sn=2403c84d9c92c697d9083bc79e7469a0&scene=21#wechat_redirect)**

**[网络安全等级保护制度演进，回看2006年7号文（过渡性文件）](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505809&idx=1&sn=2403c84d9c92c697d9083bc79e7469a0&scene=21#wechat_redirect)**

[《等级保护条例》迎来最新进展](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505649&idx=1&sn=342bf65417e243d0771ca56d852e76a4&scene=21#wechat_redirect)

[网络安全等级保护制度统一框架辨析](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505789&idx=1&sn=239bac6ed28aa1bbf7c7d36cbf0b7f57&scene=21#wechat_redirect)

[网络安全等级保护安全物理环境之防盗窃和防破坏实现](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121519&idx=1&sn=631a7fe01f6172254409e26272c68ffe&scene=21#wechat_redirect)

[网络安全等级保护物理访问控制实现](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121492&idx=2&sn=2dc3e4c889b8b33464176a871dd2fac5&scene=21#wechat_redirect)

[信息安全技术 网络安全等级保护测评过程指南](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121469&idx=1&sn=745b1a5bbb2c0bac74d0cbcdf03bf2e0&scene=21#wechat_redirect)

[夜读：GB 17859-1999安全保护等级划分准则](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121433&idx=1&sn=0074031432dd648b7d41627c11b520d2&scene=21#wechat_redirect)

[等级保护基本要求标准系列](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121261&idx=1&sn=83eaa31a45d33b441a84a1ffafac583d&scene=21#wechat_redirect)

[等级保护的数据摸底调查](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652120232&idx=1&sn=4e95783ee5fd62e9e9cc8b74103fc310&scene=21#wechat_redirect)

[网络安全等级保护自查清单（对照法条）](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121146&idx=1&sn=07cef95c28356b7f740a00f94ab7f170&scene=21#wechat_redirect)

[由新《网安法》罚则看等级保护、应急安全责任](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652120509&idx=1&sn=db3380982915487b4689a312349f984f&scene=21#wechat_redirect)

[等级保护的数据摸底调查](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652120232&idx=1&sn=4e95783ee5fd62e9e9cc8b74103fc310&scene=21#wechat_redirect)

[以等级保护为中轴线/基础的网络安全监管体系发展](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505443&idx=1&sn=b55926a407e187fd62563c8cae51199a&scene=21#wechat_redirect)

[网络运营者等级保护合规自查表](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505260&idx=1&sn=ed42da685a9950029b024dd9bbc89247&scene=21#wechat_redirect)

[信息安全技术 网络安全等级保护测评过程指南](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121469&idx=1&sn=745b1a5bbb2c0bac74d0cbcdf03bf2e0&scene=21#wechat_redirect)

[网络安全等级保护全生命周期一览图](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121384&idx=1&sn=6fb506fc4365c1ddb1e2578cd0f606aa&scene=21#wechat_redirect)

**[开启等级保护之路：GB 17859网络安全等级保护上位标准](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652096276&idx=2&sn=7a7c95d4d000ad3c89ef393c7ff78416&chksm=8bbced2dbccb643b90402b84e1f730afd8cbf25d169066778a66fa04b1482bb486f20bcc5166&scene=21#wechat_redirect)**

**[网络安全等级保护：什么是等级保护？](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652095939&idx=1&sn=5b143b489cb4716976cf52094f0113fd&chksm=8bbceffabccb66ec7ee7d740bd96d630063d6efce16affdcf62e0f9dfcacf4024572dcf8de89&scene=21#wechat_redirect)**

**[网络安全等级保护：等级保护工作从定级到备案](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652100027&idx=1&sn=4bac7d37ed73cc1b3d8d6b852f17ac61&chksm=8bbcff82bccb76947a835e8274a7613146a93ef7329599be8ba74927e48c5765279b4d1f7a2c&scene=21#wechat_redirect)**

**[网络安全等级保护：等级测评中的渗透测试应该如何做](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652097967&idx=1&sn=cf7c423071fbf448b5e57163f0f5882a&chksm=8bbce796bccb6e80a9852d6f4bd1a405aae2143610b5f06f221070210b54b6554462d7ee5a6b&scene=21#wechat_redirect)**

**[网络安全等级保护：等级保护测评过程及各方责任](http://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652096257&idx=1&sn=c17dbdfac67c78e16a3c00b9266f4cc4&chksm=8bbced38bccb642e6691ca3287b4db7abd2053b5ac805896d14ba89113985f9dfb19c4a96a6b&scene=21#wechat_redirect)**

**[网络安全等级保护：政务计算机终端核心配置规范思维导图](http://m...