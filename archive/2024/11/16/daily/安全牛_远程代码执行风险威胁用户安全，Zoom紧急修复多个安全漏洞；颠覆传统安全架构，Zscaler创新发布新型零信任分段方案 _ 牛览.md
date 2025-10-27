---
title: 远程代码执行风险威胁用户安全，Zoom紧急修复多个安全漏洞；颠覆传统安全架构，Zscaler创新发布新型零信任分段方案 | 牛览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651133388&idx=2&sn=8fe7297f29148fa035db128b29e8dc99&chksm=bd15a51f8a622c096ef4441d0b5acb3ee39ef865e5650f4df483a8648b528a3509fe57972cd1&scene=58&subscene=0#rd
source: 安全牛
date: 2024-11-16
fetch_date: 2025-10-06T19:17:32.260921
---

# 远程代码执行风险威胁用户安全，Zoom紧急修复多个安全漏洞；颠覆传统安全架构，Zscaler创新发布新型零信任分段方案 | 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAH11bOhkd9lhb16qOsOqlTfTL9qqciaDOKzfAyRTcHWwDUAaUMRAf7TVq6l4BvzSDjXqEeBZnHQnQ/0?wx_fmt=jpeg)

# 远程代码执行风险威胁用户安全，Zoom紧急修复多个安全漏洞；颠覆传统安全架构，Zscaler创新发布新型零信任分段方案 | 牛览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

•世界互联网大会“互联网之光”博览会“网络安全主题展”11月19日开展

•黑客组织假冒猎头瞄准航空航天人才实施针对性钓鱼攻击

•研究人员成功破解利用BitLocker加密的新型勒索软件

•远程代码执行风险威胁用户安全，Zoom紧急修复多个安全漏洞

•KVM基础架构曝高危漏洞，Apache CloudStack项目发布紧急修复

•Google正式发布Chrome 131稳定版，修复多个关键安全漏洞

•Splunk发布新一代可观测性解决方案，全面提升业务洞察能力

•颠覆传统安全架构，Zscaler创新发布新型零信任分段方案

**特别关注**

**世界互联网大会“互联网之光”博览会“网络安全主题展”11月19日开展**

2024年世界互联网大会“互联网之光”博览会将于11月19日至22日在浙江乌镇举行。本届“网络安全主题展”贯彻落实总体国家安全观和党的二十届三中全会精神，设置了“独立特装展”“国家网络安全教育技术产业融合发展试验区成果展”“网络安全学院成果展”“网络安全综合性成果展”等展区，相比前几届主题更加鲜明，内容更加丰富。

一、时间及地点

11月19日至22日

乌镇互联网国际会展中心展览中心3号展厅（互联网之光博览会B3馆）

二、主办单位

中国网络空间安全协会

三、特别支持单位

国家电网有限公司、中国移动通信集团公司、中国联合网络通信集团有限公司、云网基础设施安全国家工程研究中心、长安通信科技有限责任公司、奇安信科技集团股份有限公司、天融信科技集团股份有限公司

杭州安恒信息技术股份有限公司、网宿科技股份有限公司

原文链接：

https://mp.weixin.qq.com/s/O1fBaJN93WtmmIR8CMrtKA

**网络攻击**

**黑客组织假冒猎头瞄准航空航天人才实施针对性钓鱼攻击**

ClearSky安全研究机构最新披露，黑客组织TA455自2023年9月以来在LinkedIn等社交平台上发起了一轮针对性网络钓鱼攻击，其主要目标为航空航天领域的专业人士。

据ClearSky分析，攻击者通过伪装成航空航天行业的招聘顾问与目标建立联系后，在获得受害者信任后，诱导对方下载一个名为"SIgnedConnection.zip"的压缩包，并提供PDF指南诱导受害者"安全"地下载和打开这些文件。

技术分析显示，该压缩包中包含的可执行文件会通过DLL侧加载技术向受害者设备植入恶意程序。具体而言，攻击者通过加载名为"secure32.dll"的DLL文件，实现在目标系统中运行隐蔽代码。随后，恶意程序会启动感染链，最终部署Snail Resin恶意软件并开启一个名为"SlugResin"的后门。

为规避检测，该组织采用了多种高级对抗技术：一方面在GitHub平台上对命令控制（C2）通信进行编码，使传统检测工具难以识别威胁；另一方面模仿Lazarus Group的攻击特征，造成归因困难。

原文链接：

https://www.darkreading.com/cyberattacks-data-breaches/iranian-cybercriminals-aerospace-workers-linkedin

**研究人员成功破解利用BitLocker加密的新型勒索软件**

Bitdefender安全公司日前发布了针对ShrinkLocker勒索软件的解密工具。这款勒索软件利用Windows内置的BitLocker驱动器加密工具来锁定受害者文件，此次发布的解密工具可以帮助受害者免费恢复被加密的数据。

尽管ShrinkLocker的勒索技术实现相对简单，但其破坏性不容小觑。ShrinkLocker的技术手段并不高明，不同于传统勒索软件使用自定义加密实现，而是利用Windows BitLocker并生成随机密码发送给攻击者。攻击过程首先通过Windows Management Instrumentation（WMI）查询检查目标系统是否安装了BitLocker；随后，攻击者会移除所有默认保护机制，并使用"-UsedSpaceOnly"参数仅加密磁盘已使用空间以提高效率。该勒索软件使用网络流量和内存使用数据生成随机密码，使暴力破解变得困难，同时删除和重新配置所有BitLocker保护器，增加加密密钥恢复的难度。

Bitdefender的解密工具通过识别BitLocker加密磁盘删除保护器后的特定恢复窗口，成功实现了攻击者设置的密码恢复。受害者可以通过USB驱动器使用该工具，在BitLocker恢复界面进入恢复模式，通过高级选项访问命令提示符来启动解密工具。

原文链接：

https://www.bleepingcomputer.com/news/security/new-shrinklocker-ransomware-decryptor-recovers-bitlocker-password/

**漏洞预警**

**远程代码执行风险威胁用户安全，Zoom紧急修复多个安全缺陷**

近日，Zoom官方修复了其应用程序套件中存在多个安全缺陷，其中最严重的缺陷可能允许攻击者执行远程代码。这些漏洞影响范围广泛，涉及Windows、macOS、iOS、Android和Linux等多个平台的Zoom产品。

其中最严重的是一个缓冲区溢出缺陷，CVSS评分高达8.5。该缺陷可能允许已认证用户通过网络访问提升权限，进而执行远程代码。受影响的产品包括Zoom Workplace App、Rooms Client、Video SDK和Meeting SDK等核心应用。还有一个严重缺陷涉及输入验证不当问题。可能使未经身份验证的用户通过网络访问泄露敏感信息。

此外，Zoom还披露了多个中等严重级别的安全缺陷，涉及输入验证不当可能导致拒绝服务攻击、资源消耗控制不当可能引发拒绝服务、macOS安装程序中的符号链接跟随缺陷，以及macOS安装程序中的资源消耗控制不当可能导致信息泄露等问题。

这些漏洞主要影响6.2.0版本之前的大多数产品，部分macOS特定漏洞存在于6.1.5版本之前。Zoom建议用户通过官方网站更新到最新版本以防范潜在的漏洞利用。

原文链接：

https://cybersecuritynews.com/zoom-app-vulnerability/

**KVM基础架构曝高危漏洞，Apache CloudStack项目发布紧急修复**

Apache CloudStack项目日前发布重要安全更新，修复了其KVM基础架构中的严重漏洞（CVE-2024-50386）。此次发布的LTS安全版本4.18.2.5和4.19.1.3修补了一个可能允许攻击者入侵KVM环境的重大缺陷。

该漏洞CVSS v3.1基准评分为8.5（高危），影响Apache CloudStack 4.0.0至4.18.2.4版本以及4.19.0.0至4.19.1.2版本。安全问题源于模板注册过程中缺少对KVM兼容模板的验证检查。攻击者可能通过利用此漏洞部署恶意实例，进而未经授权访问主机文件系统，危及CloudStack管理的KVM基础架构的完整性、机密性和可用性。

为降低风险，CloudStack强烈建议管理员立即升级至修补版本4.18.2.5、4.19.1.3或更高版本。运行4.19.1.0之前版本的用户应跳过中间更新，直接升级至4.19.1.3。同时，CloudStack还为管理员提供了扫描和验证现有KVM兼容模板的指导，包括在基于文件的主存储上运行特定命令以识别潜在受损磁盘。

原文链接：

https://cybersecuritynews.com/critical-kvm-infrastructure-vulnerabilities/

**Google正式发布Chrome 131稳定版，修复多个关键安全漏洞**

Google公司日前发布了Chrome 131稳定版，针对Windows、Mac和Linux平台修复了12个安全漏洞，其中包括多个高危和中危漏洞。该更新将在未来数周内陆续推送。

在此次修复的漏洞中，最严重的是由Solidlab公司的Vsevolod Kokorin发现的一个高危漏洞（CVE-2024-11110）。该漏洞与Chrome浏览器渲染引擎Blink中的不当实现有关。

其他重要修复还包括：自动填充实现缺陷（CVE-2024-11111）、媒体组件中的释放后使用漏洞（CVE-2024-11112）、无障碍功能中的释放后使用问题（CVE-2024-11113）、Views组件中的不当实现（CVE-2024-11114）以及导航功能中的策略执行不足（CVE-2024-11115）。此外，Chrome安全团队还解决了一个长期存在的绘制实现问题（CVE-2024-11116）和一个低危的文件系统实现漏洞（CVE-2024-11117）。

为确保大多数用户能在潜在漏洞利用代码公开前完成更新，Google限制了部分漏洞细节的访问权限。Google建议用户尽快更新浏览器以防范安全风险。用户可以通过Chrome设置中的"关于Chrome"选项手动检查并安装最新版本。

原文链接：

https://cybersecuritynews.com/chrome-131-released/

**行业动态**

**Splunk发布新一代可观测性解决方案，全面提升业务洞察能力**

Splunk公司日前宣布全面升级其可观测性产品组合，通过Splunk AppDynamics的技术支持，帮助IT运维和工程团队更快速地发现和解决性能问题，为组织提供更强大的业务运营性能可视化能力。

在当今混合和现代化环境下，许多组织面临技术基础设施可视性分散的挑战，这严重影响了其理解性能对运营影响的能力。Splunk可观测性产品负责人Patrick Lin表示，注入更完整的业务上下文信息是克服当今混合现代环境中分散可视性和安全盲点的关键。Splunk的可观测性产品组合在AppDynamics的加持下，能够为客户提供必要的业务上下文，帮助其了解问题的根源及其影响范围。

此次升级的核心点包括：

* 将Cisco AppDynamics整合入Splunk可观测性产品组合，实现跨环境的统一体验；
* 引入单点登录、增强用户界面，并推出Log Observer Connect功能，将Splunk AppDynamics的可视化与Splunk平台上的详细日志关联起来；
* 通过AI增强和基础设施监控来减少故障排查工作量，为ITOps团队提供更有效的工具，简化环境导航和深入分析流程。

原文链接：

https://www.sdxcentral.com/articles/stringerai-announcements/splunk-enhances-observability-portfolio-for-better-business-insights/2024/11/

**颠覆传统安全架构，Zscaler创新发布新型零信任分段方案**

Zscaler公司宣布，正式推出行业创新的零信任分段解决方案，通过创新技术打造更安全、高效的连接方案，以应对分布式环境下日益复杂的网络安全挑战。

在数字化转型浪潮中，企业业务遍布各地分支机构、数据中心和云平台，传统的防火墙、VPN和SD-WAN等安全方案不仅成本高昂且复杂，还可能无意中扩大了攻击面，特别是在应对勒索软件时。

Zscaler的零信任分段方案将零信任原则扩展到分支机构、工厂和公有云等多样化环境。该解决方案将每个位置转变为安全隔离的"孤岛"，通过云实现无缝通信，无需复杂的基于硬件的防护。系统通过Zero Trust Exchange云平台，在设备和工作负载层面实施基于云的分段，每个分支或位置作为独立的网络实体，仅通过执行特定业务策略的受控安全通道进行通信。

IIFL首席信息安全官Shanker Ramrakhiani对此表示，Zscaler的零信任云使他们能够在数据中心和多个云环境中执行一致的安全策略，简化运营并显著降低横向威胁移动的风险。

原文链接：

https://cybermagazine.com/articles/zscaler-powering-a-new-era-of-zero-trust-with-segmentation

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMnicXSRCtG4URyLibbqPegjnnibfRB0z4zIzwghbLOkV5fqGYM8vhuQdqw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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