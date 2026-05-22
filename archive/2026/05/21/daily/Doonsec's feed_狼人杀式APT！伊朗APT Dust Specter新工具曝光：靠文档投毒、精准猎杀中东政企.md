---
title: 狼人杀式APT！伊朗APT Dust Specter新工具曝光：靠文档投毒、精准猎杀中东政企
url: https://mp.weixin.qq.com/s/C_jKOlRgov66KOx6mHaElw
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:06:10.793156
---

# 狼人杀式APT！伊朗APT Dust Specter新工具曝光：靠文档投毒、精准猎杀中东政企

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/E3ZvvAXyiaiblxmqclc8sNoJEI0FB0icNJeFwMNCkNA3KuicPWBkFLCHwjqwJ4ibXCdJB8Lf7aibemuxjtq69475h9oGU4xkEf1B9FYR5ibouPtRgA/0?wx_fmt=jpeg)

# 狼人杀式APT！伊朗APT Dust Specter新工具曝光：靠文档投毒、精准猎杀中东政企

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblK0ic1ncvY73iax1sIXKicChA1PBHFIqROicS66j93KbvWjiaqibictgXPxwubuVBZYXG4ibjtCNtppfAtN51lXIViaYjaTGUib39DtXia9w/640?wx_fmt=png&from=appmsg)

APT圈子又爆狠料！伊朗关联Dust Specter（尘埃幽灵）组织，近期祭出一套代号“Tinker Tailor Soldier Paper”的全新黑客工具包，主打文档投毒+AI生成恶意软件+社交工程诱杀，专挑伊拉克、中东地区政府官员、能源企业、外交机构下手，玩法堪比线上狼人杀——伪装渗透、暗中窃密、不留痕迹！

一、顶级伪装术！PDF文档变“毒饵”，点开即中招

这套工具包最绝的是极致伪装，完全拿捏职场人“点开陌生文档”的习惯，堪称“钓鱼天花板”：

黑客伪造伊拉克外交部官方PDF，封面印正规公文样式，内页嵌“下载文档”醒目按钮，诱导受害者点击跳转恶意链接。

一旦中招，恶意程序自动执行，释放4款全新定制恶意软件——SPLITDROP、TWINTASK、TWINTALK、GHOSTFORM，全程无弹窗、无异常，后台悄悄接管电脑，普通人根本察觉不到！

二、AI加持！4款恶意软件分工，窃密+潜伏全拿捏

和传统老套恶意软件不同，这套工具AI深度参与开发，代码里藏着表情符号、AI占位符，隐蔽性拉满，4款工具分工明确，环环相扣：

SPLITDROP：“开门钥匙”

伪装成WinRAR，解压后自动释放核心恶意模块，是整个攻击的“第一步跳板”。

TWINTASK：“执行打手”

专门执行黑客远程指令，偷偷下载更多恶意程序、窃取本地机密文件。

TWINTALK：“秘密联络员”

加密通信+随机延迟伪装，连接黑客服务器，实时传输窃取的情报，还能躲避防火墙追踪。

GHOSTFORM：“无痕潜伏者”

最狠的AI定制款！全程内存运行、不留磁盘痕迹，仿谷歌表单诱骗，还能延迟执行，杀毒软件根本查不到！

三、双重套路！不止文档，会议链接也藏毒

除了PDF投毒，黑客还玩双重诱杀，瞄准职场高频场景：

伪装Cisco Webex政府会议页面，谎称“需政府专属模式入会”，诱导用户粘贴恶意PowerShell脚本。看似正常操作，实则一键安装木马，长期控制设备！

这套工具还疯狂滥用Google Sheets、Slack、Discord等常用云服务，把恶意指令藏在表格、聊天记录里，伪装成正常办公流量，堪称“合法外衣下的窃密利器”。

四、猎杀目标明确！中东政企成重灾区

伊朗Dust Specter组织目标精准，重点盯伊拉克政府官员、外交机构、能源企业、军工单位，核心窃取：

外交机密文件

国防军工资料

能源行业核心数据

政府人员信息

攻击不留痕迹，溯源难度极大，堪称中东地区“最危险的网络猎手”。

五、3招筑牢防线，别当“待宰羔羊”

面对这套AI加持的新型攻击，政企、职场人必记3个保命要点：

1. 陌生PDF/会议链接，一律不点开、不粘贴脚本，官方文件走内部系统核实；

2. 禁用PowerShell无授权执行，定期更新系统补丁，堵住漏洞；

3. 部署终端检测工具，警惕异常进程、可疑云连接，早发现早处置。

结语

伊朗Dust Specter的“狼人杀式”攻击，标志着AI+文档投毒+社交工程已成APT新趋势，中东政企成首要目标。网络威胁不分国界，伪装越来越真、手段越来越狠，唯有时刻警惕、筑牢防线，才能守住数据安全底线！

**加入知识星球，可获取权益**

一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友入圈交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblj6Qa1c5j4iaSxNtaWyMmOrsJ7WJafnTfxff3PA2nhkdQL7AyqtkzhPaoCicbu2FWhIAe1y02o5icTMZiaiaD1T4WXgf5TRsAVyEFU/640?wx_fmt=png&from=appmsg)

二、为什么加入？

职场瓶颈期找不到突破方向？安全项目落地缺成熟方案？面对APT攻击、勒索病毒不知如何构建防御体系？

三、在这里，你能获得的不只是资料包，而是直接对接行业专家的「私人顾问服务」

✅ 职业发展「精准导航」

 1v1简历优化：针对安全岗（渗透测试/安全运营/合规等）拆解JD，突出核心竞争力；

 晋升避坑指南：从工程师到安全负责人，分享晋升路径，避开「技术强但管理弱」的晋升陷阱；

 技能栈规划：根据你的基础（应届生/3年经验/资深专家）定制学习路线，比如从0到1学SOC安全建设、APT威胁狩猎。

✅ 安全方案「对症开方」

 实战方案库：含医疗/制造业/等行业的勒索防御、数据安全合规、供应链安全加固方案（附落地工具清单+成本测算）；

 架构设计咨询：小到EDR选型，大到零信任体系搭建，提供「预算效果」平衡的最优解（已帮10+企业节省40%防护成本）。

✅ 圈子资源「直接对接」

 大厂安全负责人拆解真实案例（如某支付公司攻防对抗的实战复盘）；

四、适合谁？

 想突破职业天花板的安全工程师/架构师；

 需快速落地安全项目的企业负责人；

 关注行业动态的安全爱好者或IT从业人员。

**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

AI紫队安全研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

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