---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（05/18-05/22）
url: https://mp.weixin.qq.com/s/HSu8_Xm_JcbLWf55qwyVEg
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:35:29.066309
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（05/18-05/22）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mxwq2AF6zpNRcm97Jpr7B307njhIqBr9sHRfQ8TO8Auq2hO0ib0z7lD24AnVDgyw5rhvBPeibYJX3IS5uKpfMIp2blM6ibW6UfVJAXtF2KjPPU/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（05/18-05/22）

盛邦安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件701起，同比上周增加16.7%。本周内贩卖数据总量共计4247.6万条；累计涉及7个主要地区及7种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpOm9RjwzNx4XnOPFz3bkMMCWoqqNKsdPAWpHiaSXsHe2jFSNBECxuibGTvQHlHgr59FUtEXibIet6aCD7BNUKrialKibtOFQVTG1WMs/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及博彩、金融、政府等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpNRFfWesLAWmWia6ZQjaJoQY8IGkxAtHywVRibjKTVSsArUn4ItOtIKjwX8R6yX5oGbmTvM4qOQ4Zia0DFJdaX5hW10dv8Rh5zsVk/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期安全威胁以数据泄露与漏洞攻击为主，多起政府、教育及企业相关服务商数据库疑似泄露，本周内出现的安全漏洞中以python-jsonpickle远程代码执行漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP8213条，主要涉及扫描探测、组件漏洞利用及Webshell攻击等类型。

**01.**

**重点数据泄露事件**

**科威特公民数据库疑似被泄露**

泄露时间：2026-05-21

泄露内容：科威特中央统计局的公民数据库疑似被泄露，包含100万名18岁及以上科威特公民的记录，包括户主信息、国家身份证字段及家庭信息。据称数据来源于政府统计服务器。

泄露数据量：100万

关联行业：政府

地区：科威特

**GitHub 数据泄露**

泄露时间：2026-05-20

泄露内容：全球最大的代码托管平台GitHub确认发生数据泄露，攻击者通过被污染的Visual Studio Code扩展入侵员工设备，获得内部仓库的未经授权访问。被盗数据包括约3,800个内部仓库的源代码及内部组织数据，攻击者在暗网出售数据。GitHub 表示，目前没有证据显示客户仓库受到影响，但内部仓库暴露可能泄露操作工具、内部 API、认证流程及基础设施配置。

泄露数据量：未涉及

关联行业：代码托管

地区：美国

**Jimmy Fairly客户数据库疑似泄露**

泄露时间：2026-05-21

泄露内容：法国眼镜和验光品牌Jimmy Fairly的客户数据库疑似被出售，数据包含客户 ID、姓名、称谓、邮箱、邮寄地址、城市及邮政编码、出生日期、电话号码，以及国家和通信数据。

泄露数据量：35万

关联行业：零售

地区：法国

Move Up Formation数据库疑似泄露

泄露时间：2026-05-21

泄露内容：法国培训、教育和职业发展公司Move Up Formation的数据库及源代码疑似被泄露，包含客户端CSV文件、完整SQL数据库，以及2,940个源代码文件和管理员登录引用。

泄露数据量：未涉及

关联行业：教育

地区：法国

**Happipad客户数据库疑似泄露**

泄露时间：2026-05-20

泄露内容：加拿大社会企业Happipad的客户数据库疑似被泄露，包含12,178条CSV记录。数据涉及姓名、邮箱、电话号码、个人资料状态、注册与核查状态、省市国家及邮政编码、性别及访问频率等信息。

泄露数据量：1.2万

关联行业：住房

地区：加拿大

**02.**

**热点资讯**

**Linux 内核本地提权漏洞曝光**

近日，Linux内核中存在九年的漏洞CVE-2026-46333（代号ssh-keysign-pwn）被披露。漏洞源自\_\_ptrace\_may\_access()函数权限管理不当，允许本地非特权用户在Debian、Fedora、Ubuntu等系统泄露敏感文件（如/etc/shadow、SSH主机密钥）并执行任意命令。PoC利用工具已发布，建议尽快更新内核或临时提高kernel.yama.ptrace\_scope参数。对可能受影响的主机，应轮换SSH密钥并检查set-uid进程中存储的凭证。此外，文章还提及Linux本地提权漏洞PinTheft，可利用RDS模块零副本双重释放在ArchLinux系统获取root权限，显示本地提权风险仍存在。

消息来源：

https://thehackernews.com/2026/05/9-year-old-linux-kernel-flaw-enables.html

**Microsoft破获恶意软件签名服务**

Microsoft破获了一项恶意软件签名服务行动，代号OpFauxSign，该行动利用Artifact Signing系统生成短期欺诈代码签名证书，将恶意软件伪装成合法软件如AnyDesk、Microsoft Teams、PuTTY和Cisco Webex进行传播。该行动由威胁组织FoxTempest自2025年5月起实施，涉及全球数千台机器和网络，支持Rhysida勒索软件及Oyster、Lumma Stealer、Vidar等恶意软件。FoxTempest通过提供预配置虚拟机，使客户可直接上传恶意工件获取签名二进制文件，服务费用5000至9000美元。该组织还与多个勒索软件分支相关，攻击目标包括医疗、教育、政府和金融机构。Microsoft已采取封禁网站、下线虚拟机和撤销证书等措施，并提醒受影响机构更换密钥及审查凭证。

消息来源：

https://thehackernews.com/2026/05/microsoft-takes-down-malware-signing.html

**Discord默认启用端到端加密保护通话**

Discord宣布，其平台上的所有语音和视频通话现已默认启用端到端加密（E2EE），覆盖私信、群组私信、语音频道和Go Live直播，Stage频道除外。该功能基于开源协议DAVE实现，并已支持桌面端、移动端、网页、PlayStation、Xbox等平台。Discord表示，大规模测试已完成，并开始移除支持未加密回退的代码。DAVE结合WebRTC、MLS组密钥交换及临时身份密钥技术，在提升隐私保护的同时尽量降低通话延迟和中断。Discord称，目前暂无将端到端加密扩展至文本聊天的计划，因为其文本系统最初并非基于加密架构设计。

消息来源：

https://www.bleepingcomputer.com/news/security/discord-rolls-out-end-to-end-encryption-on-voice-video-calls/

**身份凭证暴露已成为关键攻击路径**

在企业混合环境中，缓存的访问密钥或长期保留的角色权限，一旦被攻击者获取，就可能贯通跨系统和云环境，直达关键资产。Active Directory、云身份提供商、服务账户、机器身份及AI代理等都携带跨系统的权限，单一凭证泄露即可授予攻击者完整身份及所有附带权限。未审查的组成员、遗留的开发者权限、非人类身份的高权限继承，都可能形成可被利用的攻击链条。传统身份管理工具（如 IGA、PAM）独立运作，无法映射这些身份链条的连通性，导致攻击者轻易沿身份链推进。有效防御需要统一可视化身份、权限和访问策略，将潜在攻击路径提前切断，从低权限立足点阻断到关键资产的纵深渗透。

消息来源：

https://thehackernews.com/2026/05/when-identity-is-attack-path.html

**Chromium 漏洞可让浏览器在后台执行恶意 JavaScript**

Chromium 内核浏览器存在一个自 2022 年起未彻底修复的漏洞，即使关闭浏览器，JavaScript 仍可在后台运行。攻击者可通过恶意网页利用服务工作者执行代码，将浏览器变为隐形“僵尸网络”成员，可用于 DDoS、流量代理和重定向。该漏洞影响 Chrome、Edge、Brave、Opera、Vivaldi 和 Arc，不会绕过系统安全边界，也不会访问用户文件或邮件，但信息泄露增加大规模攻击风险。

消息来源：

https://www.bleepingcomputer.com/news/security/google-accidentally-exposed-details-of-unfixed-chromium-flaw/

**03.**

**热点技术**

**Shai-Hulud恶意npm包扩大攻击**

研究人员发现，攻击者在npm平台发布了600多个恶意软件包，涉及@antv生态及多个热门JavaScript库，形成新一轮Shai-Hulud供应链攻击。恶意代码主要针对开发者工作站和CI/CD环境，窃取GitHub、npm、云平台、Docker、Kubernetes及SSH等敏感凭证，并通过SessionP2P网络和GitHub仓库加密外传数据。攻击者还利用被盗OIDC令牌生成合法Sigstore签名，使恶意包能够通过标准来源验证。此次攻击具备自传播能力，可自动感染受害者拥有的软件包，并通过VSCode和ClaudeCode配置植入后门实现持久化。研究人员建议开发者立即移除受感染版本，回滚至5月18日前的安全版本，并轮换所有暴露凭证。

消息来源：

https://www.bleepingcomputer.com/news/security/new-shai-hulud-malware-wave-compromises-600-npm-packages/

**Trapdoor针对安卓用户进行恶意广告欺诈**

网络安全研究人员披露了一项名为Trapdoor的新广告欺诈和恶意广告行动，针对安卓设备用户。该行动涉及455个恶意应用和183个C2域，通过伪装成PDF查看器或设备清理工具的应用诱导用户下载第二阶段应用，触发隐藏WebView并加载攻击者控制的HTML5域名以请求广告。Trapdoor自我维持，通过多阶段应用安装形成非法收入循环，用于资助后续恶意广告活动。在高峰期，每天处理6.59亿投标请求，相关应用下载超过2400万次，流量主要来自美国。行动还滥用归因工具，仅对通过恶意广告获取的用户激活恶意行为，同时采用多种反分析和混淆技术规避检测，谷歌现已移除所有识别出的恶意应用。

消息来源：

https://thehackernews.com/2026/05/trapdoor-android-ad-fraud-scheme-hit.html

**第三方脚本和供应链攻击新风险**

研究显示，现代恶意攻击不再依赖用户操作，而是通过合法第三方脚本和供应链继承信任链实现数据窃取。案例包括Shai-Hulud木马化Trust Wallet Chrome扩展窃取助记词850万美元，以及chalk/debug和Solana Web3.js库注入恶意代码截获密钥和流量。攻击者利用AI生成域名变体、选择性激活、HTML5现金站和混淆技术，绕过静态分析、CSP、防火墙和EDR。核心问题在于企业安全堆栈缺乏浏览器运行时行为监控。防御策略包括支付和认证页面部署运行时监控、建立脚本行为基线、实施SRI检查，并结合严格CSP和域名治理策略。

消息来源：

https://thehackernews.com/2026/05/typosquatting-is-no-longer-user-problem.html

**SonicWall漏洞可绕过MFA实施勒索攻击**

研究人员披露，攻击者正在利用SonicWallGen6SSL-VPN设备漏洞CVE-2024-12802，通过暴力破解VPN凭证并绕过多因素认证（MFA）获取网络访问权限。攻击过程中，黑客通常在30至60分钟内完成登录、网络侦察、凭证复用测试及远程连接，并尝试部署CobaltStrike和BYOVD工具以实施后续勒索软件攻击。研究显示，部分设备虽然已更新固件，但因未完成LDAP重新配置等修复步骤，仍可被绕过MFA。攻击日志中会显示正常MFA流程，增加检测难度。研究人员认为攻击者可能是向勒索软件团伙出售初始访问权限的中间人。由于Gen6设备已停止安全支持，建议尽快升级至新版本，并重点监控sess="CLI"、异常VPN登录及相关事件ID。

消息来源：

https://www.bleepingcomputer.com/news/security/hackers-bypass-sonicwall-vpn-mfa-due-to-incomplete-patching/

**SHub新型macOS木马窃取钱包和浏览器数据**

研究人员发现，SHub信息窃取木马推出名为Reaper的新版本，针对macOS用户发起攻击。该木马通过伪造WeChat和Miro安装页面传播，并利用applescript://方案启动恶意AppleScript，绕过Apple此前针对终端命令执行的安全限制。恶意脚本会伪装成Apple安全更新，静默下载并执行后门程序。Reaper可窃取Chrome、Firefox、Edge等浏览器数据，以及MetaMask、Phantom等加密钱包和密码管理器信息，还会收集Telegram会话、iCloud数据和开发者配置文件。木马还具备文件窃取、钱包应用劫持和持久化能力，可通过LaunchAgent定时与C2服务器通信，实现远程控制。研究人员建议重点监控异常ScriptEditor执行、可疑网络连接及新增LaunchAgent行为。

消息来源：

https://www.bleepingcomputer.com/news/security/shub-macos-infostealer-variant-spoofs-apple-security-updates/

**04.**

**热点漏洞**

**Das U-Boot FIT签名验证绕过漏洞（CVE-2026-46728）**

Das U-Boot是一款广泛应用于嵌入式设备的开源引导加载程序，支持多种处理器架构和启动管理功能。Das U-Boot存在签名验证绕过漏洞。该漏洞产生的原因是FIT（Flat Image Tree）签名验证过程中未将hashed-nodes节点包含在哈希计算范围内，攻击者可利用该漏洞构造恶意FIT镜像绕过签名校验，从而加载并执行未授权代码，影响设备安全启动机制。

影响版本：

U-Boot <2026.04

**Quick.CMS跨站脚本漏洞（CVE-2021-47981）**

Quick.CMS是一款轻量级内容管理系统，可用于快速构建和管理网站内容。Quick.CMS存在跨站脚本漏洞。该漏洞产生的原因是系统admin.php?p=sliders-form端点未对sDescription参数输入内容进行充分过滤和转义，攻击者可利用该漏洞通过构造包含恶意脚本的请求或CSRF表单，在已认证用户提交表单时执行任意JavaScript代码，从而窃取用户会话信息或实施其他恶意操作。

影响版本：

Quick.CMS == 6.7

**Fuel CMS SQL盲注漏洞（CVE-2021-47980）**

Fuel CMS是一款基于CodeIgniter框架构建的内容管理系统，可用于网站内容管理和后台维护。Fuel CMS存在SQL盲注漏洞。该漏洞产生的原因是系统Activity Log接口未对col参数输入内容进行充分过滤，攻击者可利用该漏洞通过向logs端点提交恶意SQL语句，基于响应时间延迟执行盲注攻击，从而获取数据库敏感信息或执行未授权数据库操作。

影响版本：

Fuel CMS == 1.4.13

**EgavilanMedia PHPCRUD SQL注入漏洞（CVE-2021-47956）**

EgavilanMedia PHPCRUD是一款基于PHP的简易数据库管理工具，用于执行增删改查操作。EgavilanMedia PHPCRUD存在SQL注入漏洞。该漏洞产生的原因是系统insert.php接口未对firstname参数输入内容进行充分过滤，攻击者可利用该漏洞向接口提交恶意SQL语句，从而获取敏感数据库信息或执行未授权数据库操作。

影响版本：

PHPCRUD == 1

**python-jsonpickle远程代码执行漏洞（CVE-2021-47952）**

python-jsonpickle是Python语言的一个库，用于将Python对象序列化为JSON格式并支持反序列化回对象。python-jsonpickle存在远程代码执行漏洞。该漏洞产生的原因是在反序列化过程中未对py/repr对象进行安全检查，攻击者可利用该漏洞通过构造包含py/repr指令的恶意JSON载荷，在反序列化时触发eval函数执行，从而执行任意系统命令和Python代码，导致服务器被完全控制或执行未授权操作。

影响版本：

jsonpickle == 2.0.0

**05.**

**攻击情报**

本周部分重点攻击来源及攻击参数如下表所示，建议将以下IP加入安全设备进行持续跟踪监控。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpPPyCuHAj53x770JEe7eWyLubXX3QyMBtlGZSq4pO3O0zl322icyyyOAebAaabicXRDOoqyJpBgiaM93ScnicL0CRiaENEBoBvNC6GE/640?wx_fmt=png&from=appmsg)

*请注意：以上均为监测到的情报数据，盛邦安全不做真实性判断与检测*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6oQwlp95XBm9ia9yroBLJd83wAseiabOAQoLDBAJrxjfU1KmTexS35sibxXQvt4ots9DicJoxXNia...