---
title: 滥用Windows原生工具窃密！SideCopy APT投放ReverseRAT，LNK+HTA多阶段鱼叉钓鱼攻击解析
url: https://mp.weixin.qq.com/s/ots0UFxVKP1x4qV5ei0ptw
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:11:11.663633
---

# 滥用Windows原生工具窃密！SideCopy APT投放ReverseRAT，LNK+HTA多阶段鱼叉钓鱼攻击解析

# 滥用Windows原生工具窃密！SideCopy APT投放ReverseRAT，LNK+HTA多阶段鱼叉钓鱼攻击解析

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibnGeyREDnlrsxSdiaPvWckiblciap55TafD29qbZdpW5uyTKPjIbv1x1AF1FaTfPO82LboK5r5ErYScpibWj6xZMKvh5PgxAwdIcKQ/640?wx_fmt=png&from=appmsg)

导语

印度网络安全机构Cyber Swachhta Kendra发布高危APT预警，SideCopy间谍组织正在发动新一轮鱼叉式钓鱼行动，重点瞄准科研院校、政企机构。

整套攻击不用离谱的零日漏洞，大量滥用Windows系统自带合法程序`mshta.exe`，依靠伪装文档的LNK快捷文件、多层HTA脚本，落地专用远控木马ReverseRAT。受害者双击看似普通的文档快捷方式，后台就会完成全套下载、解密、内存加载、持久化驻留，截图、录屏、窃取剪贴板与账号密码，全程利用白名单程序绕过杀毒静态检测，教育、科研单位需要高度警惕。

一、团伙与威胁背景

SideCopy是长期活跃于南亚区域的APT间谍组织，过往主要瞄准政府、国防相关机构，近期攻击范围进一步扩大，把大量高等院校、科研院所纳入狩猎目标，目标以窃取研究资料、内部公文、员工凭证为主。

> 核心武器：ReverseRAT远控木马

特点：多阶段载荷、.NET反序列化+反射内存加载，部分载荷直接内存执行，磁盘不留完整恶意exe；入侵完成后通过注册表Run键实现开机自启，攻击者拿到权限后可以执行命令、截屏、窃取密码、导出剪贴板内容、批量盗取敏感文件。

二、完整多阶段攻击链路

 Step1：鱼叉钓鱼邮件投递ZIP压缩包

攻击者发送伪装公务通知、学术资料、会议材料的钓鱼邮件，附件是ZIP压缩包。

压缩包内包含两样文件：

1. 恶意LNK快捷方式：图标伪装成docx文档，后缀被隐藏，看起来是正常办公文件；

2. 诱饵文档：真实正常的docx，用来迷惑受害者。

 Step2：双击LNK，调用mshta.exe拉取云端HTA恶意脚本

用户双击伪装文档的LNK快捷文件：

- LNK内部隐藏命令，直接调用Windows自带`mshta.exe`；

- 程序访问黑客控制的服务器，远程下载经过混淆加密的HTA（HTML应用程序）脚本，不需要本地提前存放恶意文件；

> 重点：mshta.exe属于微软官方签名系统工具，很多终端安全策略默认放行，很容易绕过防护。

 Step3：HTA释放DLL载荷，展开第二阶段

下载的混淆HTA脚本执行之后：

1. 释放恶意DLL文件；

2. 解压出配套批处理脚本`appT.bat`、二级HTA载荷`startT.hta`、诱饵docx文档；

3. 在屏幕弹出真实的业务诱饵文档，用户阅读文档时，恶意代码已经在后台运行。

 Step4：注册表写入持久化，系统重启依旧存活

修改Windows Run注册表启动项：用户登录系统自动执行`appT.bat`，再次唤起mshta运行二级HTA脚本，保证机器重启后门不会消失。

 Step5：内存加载ReverseRAT远控，建立C2通信

二级HTA利用.NET反序列化、反射加载技术，把ReverseRAT恶意DLL直接载入内存执行，不需要落地完整可执行文件。

- 采集系统硬件信息；

- 屏幕截图、捕获剪贴板、盗取保存的各类账号密码；

- 接收黑客远程命令，上传下载内网文件；

- 向外与攻击者C2服务器建立加密通信通道。

> 提示：不是完全无文件攻击，中间阶段会释放部分脚本，但是核心RAT载荷内存运行，磁盘扫描很难抓到完整样本。

三、中招之后，运维重点排查痕迹

1. 进程异常：`mshta.exe`发起陌生外网HTTPS网络连接，该程序正常业务场景极少访问外网；

2. 注册表痕迹：`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`出现未知bat、hta脚本启动项；

3. 文件路径：系统临时目录出现`appT.bat`、`startT.hta`相关脚本；

4. 网络日志：终端访问恶意域名：`dns.educationportals.biz`、`docsportal.in`相关地址，对外连接IP：`45.61.157.22`；

5. 收到来源不明ZIP压缩包，解压发现后缀为`.lnk`伪装文档的快捷文件。

> ⚠️员工侧关键识别点：Windows务必开启「显示文件扩展名」，看清真实后缀，`.lnk`不是Word文档！

四、个人员工 + 企业运维防御方案

 📌员工个人注意要点

1. 不打开陌生邮件发来的ZIP压缩包，即便邮件主题是会议、学术报告、公务通知；

2. 开启Windows显示文件扩展名，看到docx.lnk、pdf.lnk这类快捷文件一律不要双击；

3. 收到可疑邮件，通过电话、企业IM二次核验发件人身份，不要直接打开附件；

4. 陌生来源文档，优先上传沙箱检测，禁止直接在办公主机运行。

 📌企业安全加固建议

1. 邮件网关防护：拦截ZIP包内部LNK快捷附件，对HTA后缀附件隔离、沙箱检测；

2. 应用程序控制：通过AppLocker / WDAC限制`mshta.exe`无业务场景下执行，阻断HTA脚本滥用；

3. EDR重点监控：

    - `mshta.exe`产生出站网络访问行为；

    - Run注册表键新增bat、hta未知启动项；

    - .NET反序列化、反射内存加载DLL的异常行为；

4. 定期对教育科研、行政、采购岗位开展针对性钓鱼演练；

5. 威胁情报导入IOC，防火墙拦截报告内恶意域名与IP地址；

6. 日常办公禁止使用管理员账号，落实权限最小化。

 📌疑似入侵应急处置流程

1. 第一时间断开受感染主机网络，阻止数据外传；

2. 清理注册表可疑Run启动项，删除系统目录下的bat、hta恶意脚本；

3. 导出进程日志、网络日志做取证分析；

4. 本机、域内全部账号重置密码；

5. 内网横向排查，确认其他终端是否被同样入侵。

文末总结

SideCopy这一轮攻击再次展示APT的经典战术：不依靠高危漏洞，绑架系统自带合法工具完成入侵。

mshta.exe是Windows原生程序，传统杀毒不会直接标记它为恶意，再搭配LNK伪装诱饵、多层HTA脚本、内存加载RAT，对教育科研、政企单位构成实实在在的威胁。

很多安全团队只盯exe病毒，忽略LNK、HTA这类脚本类载体。防御的重心，除了查杀恶意样本，更要监控合法系统进程的异常行为。

转发给运维、行政、科研、人事同事，警惕伪装成公务、学术资料的LNK钓鱼附件！

**加入知识星球，可获取权益**

一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友入圈交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblj6Qa1c5j4iaSxNtaWyMmOrsJ7WJafnTfxff3PA2nhkdQL7AyqtkzhPaoCicbu2FWhIAe1y02o5icTMZiaiaD1T4WXgf5TRsAVyEFU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibm0l6wIBoUfic1Rxr77k9bUlBJeO2gkADWstEJ1u2JGkNGd6Td2RFTWbUh4PWaibl2jEpIAZnNsBUjCX8D6Xrlmuw44kpnsx1H34/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibnOts86xJKqAicF3fEIc4dnBIEm1bCBvX9PhLYRgIIpzQRnfnkanibo4N4ogOicxz4HEc3rFqIBscWYQdYZpL8Ucu7kbX0aRicnZjk/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkJsTBMez9zJVBx2GkJZX37f7O4FrIibRh5t4A452yETKicDN4YVqlC8IFp7j3rb1FtERwaHNkNFWq93j1mMPnGemzXIv4NGaUSU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkfA9XDdSgS2UFvFl6eje0BXEeKlZScMVtCNVBSqD7DzicMw2yPB4iahzUA3H97RvicGicibqricFoEQQey8l2qRVdeUHoYRcRDMbl8Q/640?wx_fmt=png&from=appmsg)

**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**

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