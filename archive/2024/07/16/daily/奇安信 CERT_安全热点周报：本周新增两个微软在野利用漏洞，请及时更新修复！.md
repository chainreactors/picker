---
title: 安全热点周报：本周新增两个微软在野利用漏洞，请及时更新修复！
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501684&idx=2&sn=c2f25c8f5524b2bc8d881d1c7d54b6e7&chksm=fe79e3ecc90e6afae418944501c2fc4b3ac7f7fbab4966185c2a7e805ef1041635cd508b3bae&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-07-16
fetch_date: 2025-10-06T17:44:17.265886
---

# 安全热点周报：本周新增两个微软在野利用漏洞，请及时更新修复！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibk4pC7wiaphWwfxZm5f4qGefVkBVyjFpMicP3vsBrAco815SeFkrtwGsXkOgyRkB7MOjjb5Txuxuibw/0?wx_fmt=jpeg)

# 安全热点周报：本周新增两个微软在野利用漏洞，请及时更新修复！

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 两部门印发《关于开展“网络去NAT”专项工作 进一步深化IPv6部署应用的通知》 |
| • 国家标准《数据安全技术 个人信息保护合规审计要求》公开征求意见 |
| • 菲律宾国家医保系统泄露超4200万用户数据，负责国企高管遭议会公开质询 |

**PART****0****1**

**漏洞情报**

**1.ServiceNow多个高危漏洞安全风险通告**

7月11日，奇安信CERT监测到官方修复ServiceNow UI Jelly模板注入漏洞(CVE-2024-4879)和ServiceNow Glide表达式注入漏洞(CVE-2024-5217)。ServiceNow的Jelly模板和Glide表达式由于输入验证不严格，存在注入漏洞。这些漏洞可以被未经身份验证的攻击者通过构造恶意请求利用，在ServiceNow中远程执行代码。目前该漏洞技术细节与PoC已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**2.GitLab身份认证绕过漏洞安全风险通告**

7月11日，奇安信CERT监测到官方修复GitLab身份认证绕过漏洞(CVE-2024-6385)，攻击者可以在某些情况下以其他用户的身份触发pipeline，从而造成身份验证绕过。奇安信鹰图资产测绘平台数据显示，该漏洞关联的国内风险资产总数为486206个，关联IP总数为24776个。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**3.Splunk Enterprise任意文件读取漏洞安全风险通告**

7月8日，奇安信CERT监测到Splunk Enterprise任意文件读取漏洞(CVE-2024-36991)在互联网上公开，在特定版本的Windows版Splunk Enterprise中，未经身份认证的攻击者可以在/modules/messaging/接口通过目录穿越的方式读取任意文件，造成用户信息的泄露。奇安信鹰图资产测绘平台数据显示，该漏洞关联的国内风险资产总数为2374个，关联IP总数为501个。目前该漏洞技术细节与EXP已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**4.Rejetto HTTP File Server模板注入漏洞安全风险通告**

7月8日，奇安信CERT监测到Rejetto HTTP File Server 模板注入漏洞(CVE-2024-23692)，由于该系统存在模板注入漏洞，未经身份验证的攻击者通过发送特制的 HTTP 请求在受影响的系统上执行任意命令。奇安信鹰图资产测绘平台数据显示，该漏洞关联的国内风险资产总数为84919个，关联IP总数为13059个。目前该漏洞已发现在野利用，鉴于该漏洞EXP已广泛传播，利用成本极低，请您立即着手修复，以避免潜在风险。

**PART****0****2**

**新增在野利用**

**1.****Windows MSHTML 平台欺骗漏洞(CVE-2024-38112)**

7月 9 日，微软共发布了139个漏洞的补丁程序，修复了Microsoft Office、Windows Hyper-V、Windows Imaging Component 和 Windows Win32K等产品中的漏洞。据微软称，Windows MSHTML 平台欺骗漏洞(CVE-2024-38112)已被作为零日漏洞在野外利用。Check Point Research 的 Haifei Li 向微软披露了该漏洞。

CVE-2024-38112 是 Windows MSHTML 中的一个欺骗漏洞。它的 CVSSv3 评分为 7.5，被评为重要。未经身份验证的远程攻击者可以通过诱使潜在目标打开恶意文件来利用此漏洞。微软指出，为了成功利用此漏洞，攻击者还需要采取“额外行动”来“准备目标环境”。

Check Point Research 最近发现，威胁行为者一直在使用新颖的（或以前未知的）技巧来引诱 Windows 用户进行远程代码执行。具体来说，攻击者使用特殊的 Windows Internet 快捷方式文件（.url 扩展名），单击该文件时会调用已退役的 Internet Explorer (IE) 来访问攻击者控制的 URL。在 IE 上还使用了另一种技巧来隐藏恶意的 .hta 扩展名。通过使用 IE 而不是 Windows 上更安全的现代 Chrome/Edge 浏览器打开 URL，攻击者在利用受害者的计算机方面获得了显著优势，尽管该计算机运行的是现代的 Windows 10/11 操作系统。

从技术背景来看，威胁行为者使用 .url 文件作为初始攻击媒介的情况并不少见。甚至以前也发生过使用新型或零日 url 文件相关漏洞的情况——去年 11 月刚刚修补的CVE-2023-36025就是一个很好的例子。恶意 .url 样本最早可以追溯到 2023 年 1 月，最晚可以追溯到 2024 年 5 月 13 日。这表明威胁行为者已经使用这些攻击技术一段时间了。

建议管理员和家庭用户尽快测试和部署微软官方发布的补丁，以避免已知漏洞的攻击。

参考链接：

https://research.checkpoint.com/2024/resurrecting-internet-explorer-threat-actors-using-zero-day-tricks-in-internet-shortcut-file-to-lure-victims-cve-2024-38112/

**2.Windows Hyper-V 权限提升漏洞(CVE-2024-38080)**

7月 9 日，微软共发布了139个漏洞的补丁程序，修复了Microsoft Office、Windows Hyper-V、Windows Imaging Component 和 Windows Win32K等产品中的漏洞。其中包括五个严重漏洞和三个零日漏洞，Windows Hyper-V 权限提升漏洞(CVE-2024-38080)作为其中一个零日漏洞已被在野利用。

CVE-2024-38080 是 Microsoft Windows Hyper-V虚拟化产品中的一个权限提升漏洞。该漏洞的 CVSSv3 评分为 7.8，级别为重要。本地经过身份验证的攻击者可以利用此漏洞提升至 SYSTEM 权限。

据微软称，该漏洞已被作为零日漏洞在野利用。一位不愿透露姓名的研究人员报告了这一情况。目前尚未披露有关该漏洞在野外利用的更多细节。趋势科技零日计划的达斯汀·查尔德 (Dustin Child)解释说：“虽然微软没有明确说明，但让我们假设最坏的情况，并假设授权用户可能在客户操作系统上。”

自 2022 年以来，Windows Hyper-V 中已有 44 个漏洞得到修补。这是第一个在野以零日漏洞形式被利用的 Hyper-V 漏洞。

研究人员解释说：“作为临时的解决方法，您可以禁用许可服务，但如果您正在运行它，则可能需要它。”同时确保这些服务器无法通过互联网寻址。如果这些服务器中有一大堆都与互联网相连，预计很快就会被利用。

建议管理员和家庭用户尽快测试和部署微软官方发布的补丁，以避免已知漏洞的攻击。

参考链接：

https://www.tenable.com/blog/microsofts-july-2024-patch-tuesday-addresses-138-cves-cve-2024-38080-cve-2024-38112

**PART****0****3**

**安全事件**

**1.南非矿业巨头遭网络攻击：被迫隔离IT系统 企业运营受干扰**

7月11日MyBroadband消息，全球最大的铂金和黄金生产商之一、南非矿业巨头Sibanye-Stillwater透露，其全球IT系统遭受了网络攻击。该公司向利益相关者发出通知称：“公司发现事件后，便立即根据事件响应计划实施了主动隔离IT系统、保护数据的应急措施…虽然对事件的调查仍在进行中，但可以肯定事件对集团全球运营的干扰较有限。”该公司进一步表示：“我们自愿向相关监管机构报告此事件，并将在必要时提供进一步更新。”

原文链接：

https://mybroadband.co.za/news/security/544063-south-african-mining-giant-hacked.html

**2.菲律宾国家医保系统泄露超4200万用户数据，负责国企高管遭议会公开质询**

7月9日The Record消息，菲律宾健康保险公司（PhilHealth）执行副总裁Eli Dino Santos日前在菲律宾众议院拨款委员会听证会上作证称，该公司发生违规事件后尚未按照法律要求，向每位受害者发送有关数据泄露的通知，此举遭到议员们的猛烈抨击。菲律宾健康保险公司是由该国卫生部长担任董事长的国企，负责管理国家医保系统，该系统在2023年9月遭遇勒索软件攻击，导致服务中断数周，且超4200万用户数据泄露。按照法律要求，菲律宾健康保险公司需要在事件发生后72小时内通知受害者，但其未能执行。

原文链接：

https://therecord.media/philippine-lawmakers-want-answers-data-breach

**PART****0****4**

**政策法规**

**1.国家标准《数据安全技术 个人信息保护合规审计要求》公开征求意见**

7月12日，全国网络安全标准化技术委员会归口的国家标准《数据安全技术 个人信息保护合规审计要求》已形成标准征求意见稿，现公开征求意见。该文件提出了个人信息保护合规审计原则，规定了个人信息保护合规审计的实施要求，适用于个人信息处理者开展个人信息保护合规审计工作，也可为相关机构对个人信息处理活动进行个人信息保护合规审计提供参考。

原文链接：

https://www.tc260.org.cn/file/2024-07-12/938c7131-4560-46cb-83a8-5f9bcc4e88a0.docx

**2.两部门印发《关于开展“网络去NAT”专项工作 进一步深化IPv6部署应用的通知》**

7月10日，工业和信息化部、中央网信办联合印发《关于开展“网络去NAT”专项工作 进一步深化IPv6部署应用的通知》。该文件包括有序实现网络升级、持续拓宽IPv6通路、确保网络安全稳定等五方面工作任务。在网络安全方面，该文件要求基础电信企业、互联网企业针对开展IPv6升级改造的网络系统，要持续强化网络安全防护管理，定期开展风险评估，做好重要系统网络安全风险监测预警和应急处置；对于影响范围较大的设备升级、配置变更、服务变动，要制定预案，加强关键节点性能监测，保障网络安全稳定运行。

原文链接：

https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2024/art\_2ac6ac3bd9b34197b1ba7fbe50f00076.html

**3.美议员提出《联邦网络安全法规简化法案》，以改进监管碎片化问题**

7月8日，美国参议员Gary Peters和James Lankford共同提出《联邦网络安全法规简化法案》，要求白宫国家网络总监成立一个跨机构委员会，负责协调联邦监管机构对企业提出的各种网络安全要求。该法案提出一个月前，参议院举行了一场听证会。听证会期间，国家网络总监办公室负责网络政策和项目的助理Nicholas Leiserson警告议员，网络安全法规的“碎片化”问题日益严重。他说：“为了解决这个问题，需要国家网络总监办公室和国会牵头，由私营部门提供信息。”该法案解决了这次听证会上提出的许多问题。跨机构委员会将负责识别“过于繁冗、不一致或相互矛盾”的网络安全要求，并提出更新建议，同时在各机构之间建立最低标准和互惠机制。

原文链接：

https://www.congress.gov/bill/118th-congress/senate-bill/4630/cosponsors?s=1&r=28

**往期精彩推荐**

[万字长文！AI技术在威胁情报运营的应用实践](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501667&idx=1&sn=a95e9d571cbbc4b25870f331003a65dc&chksm=fe79e3fbc90e6aed5863fab472bb385cdd3217abdf213df55415e2a2693d91fd6b2e988121ce&token=157314108&lang=zh_CN&scene=21#wechat_redirect)
[【已复现】ServiceNow 多个高危漏洞安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501658&idx=1&sn=b834ae63de9a82f42af98aa628b8bbf7&chksm=fe79e3c2c90e6ad4ba7ea97ab57d68c81713306dc1fb2df37f73a98063ee38c7ef5ad7d6ad32&token=157314108&lang=zh_CN&scene=21#wechat_redirect)

[GitLab身份认证绕过漏洞(CVE-2024-6385)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501645&idx=1&sn=033df8702e13f8707d03274b085c7391&chksm=fe79e3d5c90e6ac3126b23338bc75eb076c1c17b83c0a2e96c117458a4af4d98444ce7343ee7&token=157314108&lang=zh_CN&scene=21#wechat_redirect)

本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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