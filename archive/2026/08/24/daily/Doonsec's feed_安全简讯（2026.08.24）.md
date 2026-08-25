---
title: 安全简讯（2026.08.24）
url: https://mp.weixin.qq.com/s/R0Jp1LVcpv4kUQP8Wwuk3w
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:56:32.182584
---

# 安全简讯（2026.08.24）

# 安全简讯（2026.08.24）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. Zimbra邮件系统严重漏洞正被攻击者利用**

8月20日，波兰计算机应急响应小组（CERT Polska）近日发出警告，攻击者已开始利用Zimbra Collaboration Suite（ZCS）中的一个严重命令注入漏洞（CVE-2026-73570）。ZCS是一款广泛使用的电子邮件与协作软件，全球数亿用户及数千家企业、数百家政府机构均依赖其服务。该漏洞源于SNMP监控组件在处理通知时对用户输入过滤不当，导致未经身份验证的攻击者可通过发送特制SMTP请求，以Zimbra用户身份远程执行任意操作系统命令。Zimbra安全团队已于7月20日发布10.1.20版本完成修复。据Shadowserver监测，目前网络上暴露有超过12,100台Zimbra服务器，主要分布于欧洲和亚洲，但其中未打补丁及蜜罐的具体数量尚不明确。CERT Polska于本周一确认该漏洞已被积极利用，并紧急建议管理员检查系统日志中是否存在异常，如Zimbra服务非正常重启，以及排查用户“zimbra”在过去30天内是否在敏感目录下创建过可疑文件。

https://www.bleepingcomputer.com/news/security/critical-zimbra-rce-flaw-now-actively-exploited-in-attacks/

**2. Streamlabs遭ShinyHunters勒索，数据恐被公开**

8月19日，流媒体软件公司Streamlabs据称遭到知名黑客组织ShinyHunters入侵，后者已在暗网发布最后通牒，要求该公司在8月21日前主动联系，否则将公布被盗数据。该组织在其泄露网站上用惯用语“做出正确的决定，不要成为下一个头条新闻”发出警告，但未说明具体被访问的系统、入侵手法，也未提供数据样本，因此目前无法独立核实攻击的真实性及泄露信息的具体内容。Streamlabs为罗技旗下子公司，为超1500万活跃创作者提供直播工具，覆盖约70%的Twitch主播，若攻击属实，影响范围将极为广泛。ShinyHunters以高频高调攻击闻名，近年曾袭击Sysco、Ralph Lauren、Oracle PeopleSoft、EY、思科、Rockstar Games等多家巨头，还参与去年Salesforce数据盗窃案，波及Cloudflare、Google等700余家公司。目前Streamlabs及罗技尚未公开回应。

https://cybernews.com/security/logitech-streamlabs-data-breach-shinyhunters/

**3. ToxicPanda 2.0攻击目标扩至349款应用**

8月23日，ToxicPanda安卓恶意软件已演进至2.0版本，攻击目标扩至349款应用，支持167个远程命令，破坏力显著增强。新版本核心升级是新增VPN服务权限利用，借此阻断设备与Google Play通信，绕过安全检查后静默安装恶意载荷，并进一步获取辅助功能权限。同时，恶意软件集成了无线ADB调试功能，可获取shell级访问权限，静默授权、消除后台限制并实现持久化驻留。在攻击手法上，ToxicPanda 2.0利用不可见的钓鱼覆盖层窃取金融应用登录信息，伪造锁屏界面获取设备PIN码，部分样本还以虚假系统更新画面掩盖后台活动。为保持持久性，它能识别小米、OPPO、vivo、三星和华为等设备，绕过厂商电池优化机制防止进程被终止。该恶意软件通过亚马逊AWS托管存储桶分发，已影响全球16个国家。安全厂商Zimperium已发布检测指标，建议用户谨慎授予VPN及辅助功能等敏感权限。

https://www.bleepingcomputer.com/news/security/toxicpanda-android-malware-uses-vpn-permissions-to-block-google-play/

**4. Quest酒店数据泄露，客户信息遭窃**

8月22日，澳大利亚知名连锁公寓酒店Quest近期向客户通报了一起数据安全事件。根据一位读者分享的邮件，Quest于2026年8月17日发现其数据库系统遭到未经授权的访问，并立即采取控制措施。事件根源在于其第三方服务提供商的漏洞。泄露的数据与2025年6月之前的客户记录有关，涉及客人的全名、电子邮件及其他联系方式。Quest向《注册报》确认，少量数据条目还包含出生日期，这使得受影响客户面临身份盗窃的潜在风险。然而，Quest在信息披露方面显得相当保留。公司不仅未透露涉事第三方的具体身份、泄露的具体方式，也拒绝说明受影响客户的总数。由于其运营超过30年，数据泄露实际追溯的时间跨度也引发外界疑问。Quest表示已联系所有受影响的客人，完成系统修复和补救工作，并已启动取证调查，同时聘请了外部网络安全和隐私顾问。

https://www.theregister.com/cyber-crime/2026/08/19/australian-hotel-chain-leaks-guests-pii-after-breach-at-third-party-database-operator/5289341

**5. 合众银行否认被入侵，LockBit指控系第三方泄露**

8月22日，美国合众银行（US Bancorp）近期回应了勒索软件团伙LockBit的指控，称其自身系统并未遭到入侵，相关数据泄露事件源自第三方服务提供商，并进一步追溯至第四方环境。发言人向Recorded Future News表示，已展开调查并确认这是一起与银行外部环境相关的潜在网络事件，目前没有任何证据表明银行自身系统、网络或数据存储库受到损害。银行已向执法部门提供信息，并将继续配合调查。这一声明是在LockBit于某周四早上将该银行列入受害者名单并威胁在两周内泄露数据后作出的。美国合众银行最初已告知媒体，无迹象显示其网络遭未授权访问。但银行拒绝透露涉事第三方及第四方的具体名称，仅表示将持续关注指控并保持高度警惕。

https://therecord.media/us-bank-says-breach-claims-related-to-fourth-party-incident

**6. TrueConf漏洞遭利用，CISA敦促紧急修复**

8月21日，美国网络安全机构CISA于本周四向联邦机构发出紧急警告，指出威胁行为者正在积极利用TrueConf视频会议平台中的两个严重漏洞。TrueConf是一款依赖可扩展视频编码（SVC）的安全本地视频会议系统，用于将客户端连接至企业专用服务器。受影响的是自2022年以来发布的所有TrueConf Server版本，两个漏洞编号分别为CVE-2026-72529和CVE-2026-72530，均允许远程攻击者通过4307/TCP端口访问服务器。其中，CVE-2026-72529可让攻击者调用未公开函数并执行任意脚本，而CVE-2026-72530则允许攻击者逃逸隔离环境并在宿主系统上执行代码。这两个漏洞已于2026年6月在TrueConf Server 5.3.9、5.4.9和5.5.5版本中得到修复。CISA已将这两项漏洞纳入其已知利用漏洞（KEV）目录，并要求联邦机构在三天内修复CVE-2026-72529，两周内修复CVE-2026-72530。虽然CISA未透露漏洞利用的具体细节，但卡巴斯基此前已发出警告，称黑客组织Head Mare正利用这些漏洞部署PhantomCore恶意软件。

https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-trueconf-vulnerabilities/

预览时标签不可点

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