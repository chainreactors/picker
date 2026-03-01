---
title: 安全简讯（2026.02.28）
url: https://mp.weixin.qq.com/s/7VZBPuGXPatfewIA3abczg
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:20:54.790697
---

# 安全简讯（2026.02.28）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309ZrzfpgOelA4rSu0voEHopWgktWkREPj8iarlUMbPcDRuDrZHYLLECUu8dbWTJGzJlt14htU911icpnQpibsusvULAWr7UViczyEc8kI/0?wx_fmt=jpeg)

# 安全简讯（2026.02.28）

启明星辰安全简讯

![]()

在小说阅读器中沉浸阅读

**1. Gemini AI助手引发Google API密钥暴露风险**

2月26日，近期，TruffleSecurity研究人员在扫描全球网站时发现，近3000个嵌入在公共JavaScript代码中的Google API密钥存在严重安全风险。这些密钥原本用于地图、YouTube嵌入、Firebase等服务，在Google推出Gemini AI助手后，其权限被意外扩展至Gemini身份验证，导致攻击者可复制密钥访问私有数据并滥用API调用获利。研究显示，这些暴露密钥多部署于金融机构、安保公司、招聘企业等组织的网站源代码中，部分密钥自2023年2月起便持续暴露。TruffleSecurity通过测试Gemini API的/models端点验证了密钥的有效性，发现单日最高可产生数千美元费用。问题根源在于，开发者此前将Google云API密钥视为非敏感数据公开，而Gemini推出后，这些密钥突然获得更高权限却未被及时察觉。研究人员于2025年11月21日向谷歌报告漏洞，谷歌历时数月于2026年1月13日将其归类为“单服务权限提升”。谷歌已采取积极措施。

https://www.bleepingcomputer.com/news/security/previously-harmless-google-api-keys-now-expose-gemini-ai-data/

**2. ManoMano遭第三方服务商黑客入侵致数据泄露**

2月26日，法国DIY电商巨头ManoMano近日披露，其一家第三方客户服务提供商于2026年1月遭遇黑客攻击，导致约3800万用户数据泄露。该公司证实，黑客通过未经授权访问该突尼斯分包商系统，窃取了与用户账户及客服互动相关的个人信息，包括姓名、电子邮件、电话号码及客户服务沟通记录，但未涉及账户密码或公司系统数据修改。作为欧洲领先的家居装修、园艺产品在线市场，ManoMano在法、比、西、意、德、英六国运营，月均独立访客达5000万。此次事件源于黑客论坛上化名“Indra”的攻击者宣称对入侵负责，并声称获取了3780万用户账户及数千份支持工单与附件。网络安全公司Hackmanac指出，泄露根源或与Zendesk数据泄露相关，但ManoMano未直接确认技术细节。事件曝光后，ManoMano立即采取应急措施：禁用相关访问权限、撤销分包商数据访问权、强化访问控制与监控，并同步通报法国国家信息与自由委员会（CNIL）及国家科学与工业管理局（ANSSI）。

https://www.bleepingcomputer.com/news/security/european-dyi-chain-manomano-data-breach-impacts-38-million-customers/

**3. 马赛足球俱乐部遭网络攻击，40万用户信息面临风险**

2月26日，法国马赛奥林匹克足球俱乐部（OM）近日证实遭遇网络攻击，成为近期针对大型体育组织网络安全事件的最新案例。该俱乐部成立于1899年，是法甲联赛创始成员之一，并于1993年成为首支夺得欧洲冠军联赛冠军的法国球队。据威胁行为者在黑客论坛披露，其于本月初入侵俱乐部部分服务器，窃取了包含40万名员工、球迷及支持者信息的数据库，具体数据涉及姓名、地址、订单记录、电子邮件及手机号码。攻击者还声称获取了2050个Drupal CMS账户信息，其中包括34名俱乐部员工和1770名贡献者、版主的账户凭证。为证明攻击真实性，攻击者公开了部分数据样本，并试图在论坛出售所谓“2026年2月比赛数据”。俱乐部在周二发布的声明中确认了攻击事件，但强调“得益于技术团队与专业服务商的快速响应，事态已得到控制”。目前俱乐部所有业务均在安全环境下正常运行，且无银行信息或密码泄露。然而，俱乐部表示仍在调查事件具体范围，并已向法国数据保护机构（CNIL）正式报告，同时呼吁球迷警惕钓鱼攻击及可疑活动。

https://www.bleepingcomputer.com/news/security/olympique-marseille-football-club-confirms-cyberattack-after-data-leak/

**4. UAT-10027利用Dohdoor后门攻击美国教育和医疗保健系统**

2月26日，Cisco Talos近日披露编号为UAT-10027的威胁集群，该集群自2025年12月起以美国教育及医疗保健机构为目标，部署了新型后门程序Dohdoor。攻击初始阶段通过钓鱼邮件触发PowerShell脚本，下载恶意.bat文件并利用DLL侧载技术加载Dohdoor恶意DLL。该后门通过DNS over HTTPS（DoH）与Cloudflare基础设施隐藏C2通信，将流量伪装成合法HTTPS连接，实现绕过传统安全检测的持续访问。Dohdoor为2025年11月编译的64位DLL加载器，采用双重解密机制：批量数据使用SIMD指令的XOR-SUB算法处理，剩余数据通过位置相关公式解密。其C2通信通过解析Cloudflare的JSON响应获取服务器IP，并模拟curl流量发送HTTPS GET请求下载加密载荷。为规避EDR检测，Dohdoor会动态定位ntdll.dll中的NtProtectVirtualMemory函数，通过修补系统调用存根创建直接系统调用跳转，绕过用户模式钩子。Talos评估认为，尽管UAT-10027与Lazarus存在技术关联，但其目标领域特殊性仍需引起相关行业高度警惕。

https://securityaffairs.com/188558/apt/uat-10027-campaign-hits-u-s-education-and-healthcare-with-stealthy-dohdoor-backdoor.html

**5. 朝鲜APT37组织发起Ruby Jumper恶意活动**

2月27日，云安全公司Zscaler近日披露，由朝鲜国家支持的黑客组织APT37发起的"Ruby Jumper"恶意活动，正通过可移动存储驱动器在物理隔离系统与联网系统间建立隐蔽数据传输通道。攻击链始于受害者打开伪装成朝鲜媒体关于巴以冲突阿拉伯语译本的恶意LNK文件，该文件会部署PowerShell脚本提取有效载荷并启动诱饵文档。脚本首先加载RESTLEAF植入程序，通过Zoho WorkDrive与C2服务器通信，获取加密shellcode后下载基于Ruby的SNAKEDROPPER加载器。该加载器会安装伪装成usbspeed.exe的Ruby 3.3.0运行时环境，并通过每五分钟执行的计划任务替换RubyGems默认文件，实现自动加载。THUMBSBD后门以ascii.rb文件形式下载，负责收集系统信息、暂存命令文件，并在USB驱动器创建隐藏目录进行数据双向传输，将可移动介质转化为"隐蔽C2中继"。VIRUSTASK则通过替换合法文件为恶意快捷方式，在驱动器有2GB以上空间时触发感染，向新物理隔离设备传播。FOOTWINE间谍软件伪装成APK文件，支持键盘记录、屏幕截图、音视频录制等远程操作。

https://www.bleepingcomputer.com/news/security/apt37-hackers-use-new-malware-to-breach-air-gapped-networks/

**6. RESURGE恶意软件实现Ivanti设备隐蔽持久入侵**

2月27日，美国网络安全和基础设施安全局（CISA）近日公布了关于RESURGE恶意植入程序的最新技术细节。该程序被用于利用CVE-2025-0282零日漏洞入侵Ivanti Connect Secure设备，具有延迟启动、复杂网络级规避和认证技术等特性，可实现隐蔽通信与持久性驻留。据CISA分析，RESURGE是一个名为libdsupgrade.so的32位Linux共享对象文件，具备rootkit、bootkit、后门、投放器、代理和隧道等多重功能。其独特之处在于不主动向C2服务器发送信标，而是无限期等待特定入站TLS连接，通过CRC32 TLS指纹哈希方案识别攻击者的连接尝试。当在"web"进程下加载时，它会挂钩"accept()"函数，在流量到达服务器前检查TLS数据包，若指纹匹配则建立双向TLS会话，否则将流量导向合法Ivanti服务器。攻击者还使用伪造的Ivanti证书进行身份验证，该证书仅用于认证而非加密，且通过互联网明文传输，防御者可将其作为网络签名检测入侵。

https://www.bleepingcomputer.com/news/security/cisa-warns-that-resurge-malware-can-be-dormant-on-ivanti-devices/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

启明星辰安全简讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

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