---
title: AI批量生成钓鱼文档！Kimsuky动用OpenCode工具，LNK快捷文件借GitHub实施间谍入侵
url: https://mp.weixin.qq.com/s/f9R4jDoOLH_yB7V_85wYlA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:59:14.822013
---

# AI批量生成钓鱼文档！Kimsuky动用OpenCode工具，LNK快捷文件借GitHub实施间谍入侵

# AI批量生成钓鱼文档！Kimsuky动用OpenCode工具，LNK快捷文件借GitHub实施间谍入侵

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

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibl8JzZqycsLev3B0kkwPHySWdG7Z0EPJY1bLRpFBicaADcSyI6iaeAq8QXGKicKvMYezv6micf0b8jjqfCZnvu9Mt8nCb1YqPWCkmc/640?wx_fmt=png&from=appmsg)

导语

安全厂商Genians披露GitPower行动最新进展：朝鲜APT组织Kimsuky（金淑姬）已经直接使用OpenCode AI智能代理批量制造财务类钓鱼诱饵文档。

邮件发来一份看起来正规的保费缴纳、政策资金通知压缩包，解压后是伪装成PDF、Excel的LNK快捷方式。双击打开，屏幕显示AI生成的业务文档，后台悄悄运行混淆PowerShell，调用GitHub作为秘密指挥服务器，建立定时任务长期潜伏窃密。

部分样本还自带沙箱检测，碰到安全分析环境直接销毁痕迹。金融、零售、企业行政财务岗位成为重点攻击目标，不能再靠“找错别字”判断钓鱼文件。

一、团伙与新武器：OpenCode AI代理

Kimsuky GitPower系列攻击大家已经不陌生，过去已经证实该团伙部署本地离线大模型做诱饵、解析窃取文档。

而本次拿到实锤证据：诱饵PDF元数据直接留下`opencode`标记，OpenCode是开源AI编码代理，可以批量输出文档、代码草稿。

关键物证：部分生成的PDF里面，AI产出的占位符文本`(temporary value)临时值`没有人工删除就直接对外投放，多份文档创建时间精确到同一秒，证明是脚本一次性批量生成，不是人工逐份编辑。

黑客两套文档流水线并行产出诱饵：

1. OpenCode直出版本：速度最快，但会残留占位符草稿痕迹；

2. HeadlessChrome渲染流水线：先生成HTML，无头浏览器转PDF，格式规整，几乎没有低级残留痕迹。

诱饵主题全面转向企业财务业务：保费缴纳通知、利息结算、政策补贴资金、证书更新、商户台账、Visa付款单据，同时产出PDF、XLSX、PNG多种格式诱饵。

二、整套攻击链路：LNK伪装+GitHub当C2指挥通道

整套攻击沿用GitPower成熟武器链，同时新增反沙箱、备用投递渠道Pastebin。

Step1 鱼叉邮件投递ZIP压缩包

邮件附件是zip，内部存放恶意LNK快捷文件。

伪装技巧拉满：

图标盗用Chrome浏览器图标；

文件属性伪造描述：韩文文档、2.84KB、修改时间2023‑10‑20，和真实文件大小时间完全不符；

命令行前面填充约300个空格，打开快捷方式属性看不到恶意PowerShell指令；

文件尾部填充大量随机字符人为膨胀体积，干扰部分沙箱自动检测。

Step2 用户双击LNK，前台展示诱饵，后台执行解密

1. 用户双击LNK，系统启动被隐藏的超长PowerShell指令；

2. 使用团伙自研自定义算术解码器（不是标准Base64）解密载荷；

3. 脚本从GitHub Raw接口，依靠硬编码的GitHub PAT个人访问令牌，远程下载AI生成的诱饵文档，在屏幕正常打开；

用户眼里只是一份财务通知文档，完全意识后台已经失控。

Step3 建立持久化后门，伪装系统任务

解密后的脚本完成一系列驻留动作：

1. 在`%AppData%`目录释放随机命名ps1脚本；

2. 注册隐藏定时计划任务，名字模仿BitLockor（故意拼错BitLocker）、MATLAB、.NET Framework系统组件，每5‑35分钟自动唤醒；

3. 使用`conhost.exe --headless`无窗口模式执行PowerShell，看不到黑框弹窗；

4. 执行完成之后，脚本自我删除，抹除部分现场痕迹。

Step4 双备份C2通道，GitHub为主，Pastebin做备用

为防止单一平台封禁，攻击者准备两套指令下发渠道：

1. GitHub Raw（主力）：拆分拼接URL字符串规避静态检测，携带PAT令牌拉取后续恶意载荷；

2. Pastebin（备用退路）：一旦GitHub链路失效，部分变种自动切换到Pastebin拉取恶意代码，保证入侵不中断。

Step5 新增反分析机制，对抗安全人员研判

新版本加入完整反沙箱逻辑：

1. 枚举进程列表，如果发现VMware工具、x64dbg、ProcessHacker等调试/虚拟机工具，直接终止执行；

2. 检测到沙箱常用用户名`Bruno`，立刻删除脚本退出；

3. 主动清空PowerShell命令历史记录，销毁取证线索。

哪怕诱饵PDF打开报错乱码，下载、驻留、执行后门的逻辑依旧完整运行，不会因为文档损坏而停止攻击。

三、企业自查：出现这些特征高度怀疑GitPower系列攻击

文件与LNK特征

1. ZIP解压出来LNK快捷文件，图标伪装Chrome，属性描述写着“韩文文档 2.84KB，修改时间2023‑10‑20”；

2. LNK命令行开头存在数百个空格，命令长度数千字符；

终端行为痕迹

1. `conhost.exe --headless`启动无窗口PowerShell；

2. AppData、Temp目录出现随机名称ps1脚本；

3. 计划任务出现拼写错误的BitLockor、MATLAB、.NET相关定时任务，周期5‑35分钟，设置隐藏运行；

4. PowerShell携带GitHub PAT令牌访问raw.githubusercontent.com；

5. 进程枚举虚拟机、调试工具，删除PSReadLine命令历史。

文档侧小线索（仅供辅助，不能作为唯一判断）

PDF元数据出现`opencode`、`HeadlessChrome / Skia/PDF`，文档内残留`(temporary value)`占位标记。

四、个人&企业防御实操建议

📌员工个人注意

1. Windows务必显示文件扩展名，ZIP解压出来`.lnk`不要双击，哪怕图标看着像PDF、Excel；

2. 收到保费、利息、政策资金类邮件附件，不要直接打开，走企业IM二次核验发件人；

3. 记住重点：AI生成诱饵不一定有错别字，不要靠阅读文档内容判断是否安全。

📌运维企业加固要点

1. 邮件网关拦截ZIP包内LNK快捷附件，业务必须接收则强制沙箱解析；

2. EDR重点监控：LNK启动PowerShell、conhost无头执行、大量前置空格的超长命令行；

3. 威胁狩猎：检索计划任务中模仿BitLocker、MATLAB、.NET但是存在拼写错误的任务项；

4. 网络侧告警：业务无关终端携带GitHub PAT令牌访问raw.githubusercontent.com，以及异常访问Pastebin原始文本接口；

5. 针对财务、行政、采购岗位开展专项钓鱼演练，主题围绕保费、补贴、结算单据。

📌疑似中招应急处置

1. 立刻断开受害主机内网，阻断后门继续接收指令、横向扩散；

2. 清理全部随机命名PowerShell脚本，删除恶意隐藏计划任务；

3. 核查是否访问GitHub/Pastebin恶意基础设施，留存完整进程、网络日志；

4. 修改本机账号、域账号、各类业务系统全部密码；

5. 全网告警，筛查其他终端是否收到同款钓鱼ZIP压缩包。

文末总结

GitPower新变种标志Kimsuky的攻击模式已经进化：AI代理OpenCode实现诱饵文档工业化量产，借助GitHub、Pastebin这类大众云平台做C2，搭配LNK伪装、反沙箱、多备份通信通道，整套间谍工具链越来越成熟。

很多传统识别手段失效：没有明显错别字、恶意流量伪装成开发者平台正常访问，诱饵文档损坏也不影响后门运行。防御重心要从“读邮件找破绽”，转向监控终端异常行为、附件格式管控、计划任务审计。

转发给财务、行政、运维同事，警惕伪装成财务单据的AI生成LNK钓鱼攻击！

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