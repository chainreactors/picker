---
title: 打开海鲜采购单就中招！Kimsuky新型LNK钓鱼，看文档的瞬间电脑已被窃密
url: https://mp.weixin.qq.com/s/qe-Oou9mQkw3NpDkflez7A
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:44:05.994324
---

# 打开海鲜采购单就中招！Kimsuky新型LNK钓鱼，看文档的瞬间电脑已被窃密

# 打开海鲜采购单就中招！Kimsuky新型LNK钓鱼，看文档的瞬间电脑已被窃密

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibn0tMrzGtZZbVW5bibQqib9RdGvp0XBZYFbGZ9ztLCockgjHlbKt67OvDApdOwEygAGaFEqYrT2rrml3dE0aVm14zuxZibhQtLs2o/640?wx_fmt=png&from=appmsg)

导语

 AhnLab最新曝光Kimsuky（金淑姬/APT‑43）最新鱼叉钓鱼活动。

攻击者伪装成酒店海鲜食材采购审批单，制作恶意LNK快捷文件。当你双击打开，屏幕正常弹出业务HWP文档，你专心审阅采购清单时，后台已经悄悄释放恶意脚本、注册定时任务，偷偷收集本机全部系统信息，还利用公有云充当指挥服务器下发远控指令，攻击结束还会自动抹除大量入侵痕迹。

酒店餐饮、贸易采购、政企采购部门是重点狩猎对象，看上去正常的业务文档，背后暗藏全套窃密后门。

一、团伙背景：擅长业务场景伪装的Kimsuky

Kimsuky是朝鲜国家级APT，长期主打鱼叉式钓鱼，擅长贴合目标行业业务场景制作诱饵：招聘简历、行业报告、商务函件、采购申请都是它常用外壳。

本次使用经典LNK快捷文件投毒战术，利用Windows默认隐藏后缀名的特性，把快捷方式伪装成文档。肉眼看上去是“HWP采购文档”，实际后缀是`.lnk`，双击不是打开文档，而是执行内置恶意脚本。

本次诱饵样本

文件名：`[首尔皇家酒店]海鲜食材采购审批请求.LNK`

仿真内容：完整海鲜品类、采购数量、报价明细，和真实酒店采购审批文档几乎一模一样。

二、完整攻击链路：一边看文档，一边被入侵

Step1 用户双击恶意LNK文件

用户收到邮件附件，误以为是普通采购HWP文档，直接双击打开。

Step2 双重欺骗：前台展示真文档，后台释放载荷

1. 脚本会在本地生成一份完全真实的HWP采购文档并弹出显示，用户注意力全部放在业务内容上，不会察觉到异常；

2. 同时后台执行PowerShell，释放经过XOR加密的ZIP包，落地路径：`C:\ProgramData\systmp\sunshine`；

3. 解压释放两个核心恶意脚本：

   `termsvc.ps1`：PowerShell信息采集、回传脚本

   `poc.js`：JavaScript持久化调度脚本

4. 脚本分别复制到`C:\ProgramData\video`以及带UUID随机命名的js文件存入`systmp\ping`目录。

Step3 注册定时任务，每14分钟唤醒后门维持驻留

创建伪装成Office更新的计划任务，命名格式：`MicrosoftOffice2016\_<UUID前4位>`，配置每14分钟自动执行一次恶意JS脚本。

就算用户重启电脑，后门依旧会定时运行，绕过很多一次性查杀手段。

攻击者巧妙使用wscript.exe执行脚本，调用系统自带组件，很多杀毒会判定为正常系统行为。

Step4 滥用公有云Backblaze B2作为C2指挥通道

这是本次攻击一大亮点，不搭建自己的恶意服务器，直接使用正规对象存储服务作为窃密和指令中转：

1. 脚本调用`api.ipify.org`获取受害者公网IP；

2. 采集本机操作系统版本、时区、用户名、域名、计算机名、全部进程列表；

3. 根据设备BIOS序列号创建独立云存储目录，把窃取数据加密上传至Backblaze B2云桶；

4. 从同一个云空间下载名为`aaa`的远程指令，保存到系统临时目录，用cmd后台静默执行；

5. 执行完毕自动删除下载的cmd文件，同时删除最初的LNK诱饵、sunshine中间包，保留驻留脚本，抹除大部分入侵证据。

简单讲：全部窃密、下达指令都走正规云服务流量，防火墙很难识别为恶意攻击。

三、中招自查清单，出现这些痕迹务必紧急处置

运维人员重点检查下面路径与行为，即便原始LNK文件已被删除，残留文件依然存在：

1. 检查计划任务：名称以`MicrosoftOffice2016\_`开头，每14分钟调用wscript.exe运行JS脚本；

2. 高危文件路径核查

   `C:\ProgramData\systmp\sunshine`

   `C:\ProgramData\systmp\ping\.js`

   `C:\ProgramData\video\termsvc.ps1`、`poc.js`

3. 系统临时目录`%TEMP%`是否出现随机命名的cmd文件，并且执行后被删除；

4. 网络日志：访问`api.ipify.org`查询公网IP、大量和Backblaze B2存储服务的认证、上传下载通信；

5. 系统日志发现大量`tasklist`进程采集行为。

四、个人员工+企业运维防御方案

📌员工个人注意要点

1. 一定要打开Windows显示文件扩展名，看清真实后缀，`.lnk`不是文档，不要双击；

2. 收到采购、报价、商务审批类附件，哪怕内容再贴合业务，来源不明不要直接打开；

3. 打开HWP文档之前，确认文件真实后缀，不要被图标迷惑；

4. 陌生附件优先上传沙箱检测，不要直接在办公主机运行。

📌企业运维加固建议

1. 终端EDR监控：重点告警LNK文件执行、PowerShell绕过执行策略、wscript异常定时任务；

2. 监控`C:\ProgramData`下面新建的`systmp`、`video`可疑目录；

3. 邮件网关拦截高风险LNK快捷附件，业务场景确需接收，做沙箱预处理；

4. 审计计划任务，拦截伪装成Office更新的陌生定时任务；

5. 网络侧监控终端异常访问Backblaze B2对象存储的上传行为；

6. 针对采购、行政、酒店贸易等岗位做专项钓鱼培训，APT会高度定制行业诱饵。

📌疑似中招应急处置

1. 立刻断开受害主机网络，防止继续向云端外传内部资料；

2. 删除全部可疑JS、PS1脚本，清理恶意计划任务；

3. 全盘排查是否有后续下载的其他远控木马；

4. 修改本机、域账号、业务系统全部密码；

5. 留存系统日志、网络日志，用于后续溯源。

文末总结

Kimsuky这套攻击再次展示APT的经典套路：用最真实的业务诱饵做伪装，利用系统合法程序、正规公有云做攻击载体，攻击结束主动清理痕迹。

很多人的错觉：“我打开的是正常采购文档，应该没有危险”，而LNK投毒恰恰利用这个心理。

不管是酒店、贸易公司，还是政企采购岗位，千万不要仅凭文档内容是否真实来判断文件安全。

转发给采购、行政、运维同事，警惕伪装成采购审批单的LNK钓鱼陷阱！

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