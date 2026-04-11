---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（04/06-04/10）
url: https://mp.weixin.qq.com/s/Xtd769w9A4k2smHOiQRmDA
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:18:40.754912
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（04/06-04/10）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mxwq2AF6zpPXNbP2LkLnkcNgFFGpUAbW6lAT3aS32f15DVuU4uuSqJwX1xN6gmjxxpYDMoCgGMsQLRNdeLtaclDybpNUj99T21qFLjftqeo/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（04/06-04/10）

盛邦安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件953起，同比上周增加40.98%。本周内贩卖数据总量共计418418.8万条；累计涉及9个主要地区及8种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpNHVywOGnJUwCPA6ZxS7JxSadngniacsTp3c8RZ8nZDfVYVU2oJhjHKjibYiaIkTDN3VeK1dTiavccECzVBeBFxmQorsVX9zO2RFxg/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及金融、服务、政府等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpOQZtpJ2ChKwzZy99NCiaqRpRmtmlkd3AxBsdE4ib0fzG3F0dWS2jvpoWAL3SJWyrXLicQOH5R2oc0QHbpFD0BD5TL7zmyjDtWs8k/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期主要威胁来自恶意软件、僵尸网络及木马攻击，需加强关注；本周内出现的安全漏洞以ChurchCRM QueryView SQL注入漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP 8881条，主要涉及XPATH注入攻击、组件漏洞攻击等类型。

**01.**

**重点数据泄露事件**

**PowerLab数据库泄露**

泄露时间：2026-04-06

泄露内容：攻击者在暗网论坛上声称，已上传一个与法国定制PC及游戏硬件零售商Powerlab.fr相关的数据库。该数据集包含1.5万个客户账户，涉及用户账户ID、姓名、电子邮件地址、是否订阅简讯、注册日期以及上次访问详情等字段。

泄露数据量：1.5万

关联行业：零售

地区：法国

**美国车主驾驶执照和身份证数据集泄露**

泄露时间：2026-04-06

泄露内容：攻击者在暗网论坛上发布广告，兜售一个据称包含480万条美国车主记录的数据集。该攻击者声称数据库中含有大量个人身份信息（PII），包括姓名、电子邮件地址、电话号码、社会安全号码（SSN）、出生日期、驾照识别码及所在州/省份、完整地址数据，以及IP地址。

泄露数据量：480万

关联行业：汽车

地区：美国

**哥伦比亚两大银行数据泄露**

泄露时间：2026-04-08

泄露内容：黑客近日声称已入侵哥伦比亚两家主要金融机构——Bancolombia集团和波哥大银行，并在暗网论坛上公开了部分客户数据样本。泄露的样本显示，Bancolombia相关数据包含客户及顾问的姓名、地理位置信息、保险计划详情，以及部分登录/登出时间戳等内部业务数据。而波哥大银行的泄露样本则包含约30条更为敏感的个人信息记录，涉及客户的姓名、电话号码和住址。

泄露数据量：未涉及

关联行业：金融

地区：哥伦比亚

**Alinto邮件系统通信记录泄露**

泄露时间：2026-04-08

泄露内容：法国企业邮件服务商Alinto近日被曝因配置失误，导致一个公开可访问的Elasticsearch数据库泄露了超过4000万条SMTP邮件传输记录，暴露了大量企业及政府机构的邮件通信元数据。泄露的信息主要包括发件人邮箱、收件人邮箱、地理位置信息、邮件中继IP地址及通信时间戳等，虽未包含邮件正文，但涉及约450万个唯一邮箱地址。

泄露数据量：4000万

关联行业：通信

地区：法国

**欧盟委员会云平台数据泄露**

泄露时间：2026-04-07

泄露内容：欧盟委员会云环境近日遭受供应链攻击，攻击者共窃取约91.7GB的压缩数据（解压后约350GB），泄露信息包括姓名、邮箱地址、邮件内容及其他云环境配置数据。安全研究人员确认，泄露数据中还包含邮件附件、完整的SSO用户目录、DKIM签名密钥、AWS配置快照以及内部管理URL等敏感内容。

泄露数据量：未涉及

关联行业：政府

地区：欧洲

**02.**

**热点资讯**

**Kubernetes成为云攻击新焦点**

最新研究显示，2025年针对Kubernetes环境的攻击告警同比激增282%，其中IT行业占比超过78%。攻击者主要利用暴露的公网应用、RBAC配置错误、Pod过度授权以及Service Account Token泄露等问题，在获得容器执行权限后，窃取Kubernetes身份凭证，并向云平台核心资产横向移动。典型攻击路径包括：通过钓鱼攻击或漏洞入侵容器，提取挂载的Service Account Token，调用Kubernetes API枚举Secret和工作负载，再利用过度授权的云凭证横向渗透至AWS、GCP、Azure等云资源。该事件表明，Kubernetes的安全风险正从容器逃逸转向“身份滥用+云横向移动”，配置错误与权限过大的身份体系已成为主要薄弱点。

消息来源：

https://unit42.paloaltonetworks.com/modern-kubernetes-threats/

**AI普及推动API安全风险快速上升**

随着企业加速部署生成式AI与AI Agent，API安全风险显著上升。AI应用高度依赖API完成模型调用、数据交互与系统集成，使API成为暴露面扩张最快的攻击入口之一。然而，许多组织在快速上线AI功能时未同步建立完善的API治理机制，导致影子API、认证配置错误、接口过度暴露及权限控制缺陷大量存在，攻击者可借此绕过身份验证、调用敏感模型接口或直接访问后端数据。同时，AI Agent与自动化工作流使API调用链更趋复杂，单点攻破可能引发链式横向访问，扩大数据泄露与业务滥用影响。

消息来源：

https://www.esecurityplanet.com/threats/api-security-risks-rise-as-ai-adoption-accelerates/

**关键基础设施设备因Modbus暴露公网**

研究发现，全球20个国家共179台工业控制系统（ICS）设备通过Modbus协议直接暴露于公网，其中部分设备关联国家电网、铁路等关键基础设施，存在重大的运营与安全风险。由于Modbus协议在设计上缺乏身份认证与加密机制，攻击者在访问开放端口（通常为502端口）后，可直接读取或修改设备寄存器数据，进而干扰控制器、仪表及工业逻辑。即便是技术水平有限的攻击者，也可利用这些接口实施破坏或操控行为。该事件再次凸显传统OT/ICS协议在公网暴露场景下的系统性安全缺陷。关键基础设施若缺乏网络隔离、防火墙与访问控制，将面临极高的攻击风险。

消息来源：

https://cybernews.com/security/critical-infrastructure-devices-exposed-modbus/

**微软暂停安全软件维护者账户引发更新中断**

微软近期暂停或终止了多名关键开源项目维护者的开发者账户，受影响的包括VeraCrypt和WireGuard等安全软件，导致其无法为Windows发布新版本。维护者称微软未提前警告，也未提供明确原因或有效申诉渠道。其中VeraCrypt维护者用于签署Windows驱动和引导程序的账户被直接终止，WireGuard维护者也遭遇类似冻结。安全专家称一旦相关软件出现紧急漏洞，维护者无法及时推送补丁，可能延长数百万用户的风险暴露窗口。

消息来源：

https://cybernews.com/security/microsoft-suspends-veracrypt-wireguard-accounts-maintainers/

**法国网络攻击造成数据泄露已引发现实安全风险**

法国正经历近年来最严重的网络攻击浪潮。2026年初已发生58起勒索软件事件，同比增长29%，使法国成为全球第五大勒索软件攻击目标国。攻击激增的原因包括该国经济体量大、地缘政治敏感、关键行业数字化程度高，以及各类组织普遍存在“修复缺口”。攻击目标覆盖政府、医疗、教育、航空、体育及国防等关键领域，反映出网络暴露面持续扩大。整体而言，法国面临的已不仅是网络安全问题，更是网络攻击向现实社会安全风险外溢所带来的严峻趋势。

消息来源：

https://cybernews.com/security/france-cyberattacks-wave-reasons-cnil/

**03.**

**热点技术**

**AWS Bedrock沙箱隔离被绕过**

最新研究披露，Amazon Bedrock AgentCore的沙箱模式存在网络隔离绕过问题，攻击者可利用DNS隧道技术突破其宣称的“无外部网络访问”限制：通过将敏感信息编码至子域名并发送至受控DNS服务器实现数据外泄，或借助DNS响应建立双向C2通道，实现远程控制。同时，AgentCore微虚拟机元数据服务（MMDS）曾存在未强制会话令牌的问题，可被用于读取IAM凭证，结合DNS隧道后可进一步窃取云身份并横向访问AWS资源。AWS已调整默认安全配置并更新文档，明确沙箱模式并非完全隔离，建议高安全场景使用VPC模式及DNS Firewall等额外防护。该研究揭示，AI代理执行环境的“沙箱”安全边界并非绝对可信。

消息来源：

https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/

**SparkCat伪装成正常应用窃取移动端加密资产**

安全研究人员发现，移动端信息窃取恶意软件SparkCat再次活跃，已伪装成正常应用混入Apple App Store和Google Play，针对Android和iOS用户发起攻击。该恶意软件主要利用OCR技术扫描设备中的截图、照片等图片，从中提取加密货币钱包的密码恢复提示词，进而盗取加密资产。相比早期版本，新版SparkCat加入了代码虚拟化、混淆增强与跨平台隐藏技术，显著提升了检测和分析的难度。研究人员指出，该恶意软件最初主要针对亚洲语言用户，现已扩展支持英语识别，攻击范围进一步扩大。虽然相关恶意应用已部分下架，但此次事件再次表明：即使是官方应用商店，也无法完全杜绝高级恶意软件的渗透。

消息来源：

https://www.cybersecurity-review.com/sparkcat-malware-returns-to-target-android-and-ios-users-hiding-in-innocent-apps-to-try-and-steal-your-details/

**GPUBreach借助GPU Rowhammer实现攻击**

研究人员披露的新型硬件攻击技术GPUBreach，可通过对GPU的GDDR6显存实施Rowhammer位翻转攻击，实现权限提升并最终完全控制系统，标志着GPU内存攻击已从数据篡改升级为系统级提权威胁。攻击原理为：诱导显存位翻转破坏GPU页表（PTE），使无特权的CUDA内核获得任意GPU内存读写能力，进而结合NVIDIA驱动中的内存安全缺陷，将控制范围从GPU侧扩展至CPU侧，获取Root权限。值得注意的是，即使在启用IOMMU保护的情况下，该攻击仍可成功，传统DMA隔离机制无法有效阻断。这对多租户GPU云环境、AI训练平台及高性能计算基础设施构成严重潜在风险。

消息来源：

https://www.bleepingcomputer.com/news/security/new-gpubreach-attack-enables-system-takeover-via-gpu-rowhammer/

**Chaos木马新变种瞄准配置错误的云环境**

安全研究人员发现，Chaos恶意软件的新变种已将攻击目标从传统的路由器和边缘设备，扩展至配置错误的云部署环境，重点攻击暴露于公网且存在配置缺陷的Hadoop、Docker等云服务。该木马具备远程命令执行、载荷下载、加密货币挖矿及DDoS攻击能力，新增的SOCKS代理功能可将被控主机转化为代理节点，为攻击者提供匿名流量转发并隐藏攻击来源。攻击者通过利用配置错误的Hadoop实例远程执行命令，下载并运行Chaos载荷，随后删除痕迹以降低取证难度。相比旧版本，新变种弱化了SSH横向传播和路由器漏洞利用模块，转而强化代理功能与对云主机的滥用能力。

消息来源：

https://thehackernews.com/2026/04/new-chaos-variant-targets-misconfigured.html

**Masjesu僵尸网络提供DDoS攻击租赁服务**

安全研究人员披露，新型僵尸网络Masjesu正以DDoS攻击租赁（DDoS-for-Hire）平台的模式活跃运营，通过Telegram公开招揽客户，提供分布式拒绝服务攻击服务。该僵尸网络自2023年出现以来持续扩张，主要感染路由器、网关等IoT设备，覆盖多种硬件架构及多个厂商产品，并通过新增命令注入与远程执行模块不断扩大规模。在技术层面，Masjesu具备持久化驻留、自传播、远程命令执行及多种DDoS Flood攻击能力；感染后会关闭wget、curl等常见进程以排挤竞争僵尸网络，并监听固定端口供攻击者直接控制。研究人员指出，该僵尸网络采取“低调运营”策略，主动避开部分高敏感目标和受关注IP段，以降低执法风险、延长生命周期。整体来看，Masjesu的出现表明，IoT僵尸网络正持续向“商业化攻击服务”模式演进。

消息来源：

https://thehackernews.com/2026/04/masjesu-botnet-emerges-as-ddos-for-hire.html

**04.**

**热点漏洞**

**Botan TLS 1.3客户端认证绕过漏洞（CVE-2026-34582）**

Botan是一款C++密码学库，提供TLS 1.3协议和客户端证书认证功能。Botan存在TLS 1.3客户端认证绕过漏洞。该漏洞产生的原因是TLS 1.3实现允许在收到Finished消息之前处理ApplicationData记录。攻击者可利用该漏洞通过完全省略Certificate、CertificateVerify和Finished消息而直接发送应用数据记录，绕过服务端强制执行的客户端证书认证。

影响版本：

Botan<3.11.1

**OpenAM反序列化远程代码执行漏洞（CVE-2026-33439）**

OpenAM是一款访问管理解决方案，提供JATO视图和表单处理功能。OpenAM存在反序列化远程代码执行漏洞。该漏洞产生的原因是jato.clientSession HTTP参数存在不安全的Java反序列化，绕过了之前对jato.pageSession参数的白名单ObjectInputStream缓解措施。攻击者可利用该漏洞在未授权状态下向任何包含<jato:form>标签的JATO ViewBean端点发送精心构造的序列化Java对象，在服务器上执行任意命令，对系统造成破坏。

影响版本：

OpenAM<16.0.6

**Plane认证流程敏感信息泄露漏洞（CVE-2026-27949）**

Plane是一款开源项目管理工具，提供认证流程和错误处理功能。Plane存在认证流程敏感信息泄露漏洞。该漏洞产生的原因是当提交无效代码等错误处理时，用户电子邮件地址作为查询参数包含在URL中传输。攻击者可利用该漏洞通过高权限用户身份诱导用户操作获取PII信息。

影响版本：

Plane<1.3.0

**WWBN AVideo SSRF响应泄露漏洞（CVE-2026-39370）**

WWBN AVideo 是一个开源的视频分享平台，支持视频上传、转码和在线播放。其 `objects/aVideoEncoder.json.php` 接口在处理 `downloadURL` 参数时存在 SSRF 校验绕过漏洞。该功能仅通过检查 URL 后缀（如 .mp4, .zip, .png 等）来验证合法性，导致校验逻辑不完整。具有视频上传权限的攻击者可以构造指向内网服务的恶意 URL，利用合法的媒体后缀绕过检查，从而读取内网服务的响应内容，实现 SSRF响应外泄。

影响版本：

WWBN AVideo<=26.0

**ChurchCRM QueryView SQL注入漏洞（CVE-2026-39342）**

ChurchCRM是一款开源的教会管理系统，提供查询视图和高级搜索功能。ChurchCRM存在QueryView SQL注入漏洞。该漏洞产生的原因是QueryView.php中的searchwhat参数在使用QueryID=15时未进行有效过滤。攻击者可利用该漏洞通过已认证用户身份执行任意SQL命令，从而对数据库进行完全控制。

影响版本：

ChurchCRM<7.1.0

**05.**

**攻击情报**

本周部分重点攻击来源及攻击参数如下表所示，建议将以下IP加入安全设备进行持续跟踪监控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpMVn4hHjPEtfBBkoYmibt3oykQLP9TB8jFpPeib6NtFUyHAdblyrqa23zB2H7FUEQ3W7lk0Qib6icm3GZ9KC1oTjBGQHmZmSIicdCdo/640?wx_fmt=png&from=appmsg)

*请注意：以上均为监测到的情报数据，盛邦安全不做真实性判断与检测*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6oQwlp95XBm9ia9yroBLJd83wAseiabOAQoLDBAJrxjfU1KmTexS35sibxXQvt4ots9DicJoxXNiabToHw1T09Myv7Q/0?wx_fmt=png)

盛邦安全应急响应中心

向上滑动看下一个

知道了

![]()
微...