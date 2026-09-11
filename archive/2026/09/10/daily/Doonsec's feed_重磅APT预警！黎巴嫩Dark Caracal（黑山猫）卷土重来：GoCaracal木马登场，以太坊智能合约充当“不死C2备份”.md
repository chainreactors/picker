---
title: 重磅APT预警！黎巴嫩Dark Caracal（黑山猫）卷土重来：GoCaracal木马登场，以太坊智能合约充当“不死C2备份”
url: https://mp.weixin.qq.com/s/VSYBmGkoGsyW_sCU4sMJIA
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:50:35.748646
---

# 重磅APT预警！黎巴嫩Dark Caracal（黑山猫）卷土重来：GoCaracal木马登场，以太坊智能合约充当“不死C2备份”

# 重磅APT预警！黎巴嫩Dark Caracal（黑山猫）卷土重来：GoCaracal木马登场，以太坊智能合约充当“不死C2备份”

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

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibnMNsvZx0lpr3EaYFE1LictL91CuetS9bJnPsBm1RWMz7DJ8qwfeWib3K74qFdLXHvUPJbhB1eAIjJueV8xZOhUUarzTU2sjF80U/640?wx_fmt=png&from=appmsg)

导语

黎巴嫩关联老牌间谍APT组织Dark Caracal（黑山猫）再度更新武器库。Arctic Wolf Labs披露最新攻击活动：该组织推出全新Go语言模块化木马框架GoCaracal，搭配老牌后门Bandook共同作战，最具颠覆性的是，恶意程序利用以太坊智能合约做C2备用通道。就算主服务器被安全机构全部关停，攻击者只需要链上一笔交易，就能下发全新控制地址，极大提升对抗防守方的韧性，拉美多国政企成为重点狩猎目标。

一、APT Dark Caracal：深耕全球的老牌间谍组织

Dark Caracal被研判与黎巴嫩国家安全总局（GDGS）相关，是知名的国家级网络间谍团伙，常年针对政府机构、通信企业、媒体记者、社会活动人士实施情报窃取，攻击足迹遍布全球二十余个国家和地区。

过往该团伙擅长使用钓鱼邮件、恶意SVG附件投递载荷，此前主力工具为Bandook、AsioGate后门。而2026年的新一轮攻击中，该组织没有简单替换旧工具，而是打造全新GoCaracal框架，新旧两套工具混合上阵，同时创新引入区块链技术解决C2被查封的痛点，攻击技术实现重大升级。

二、完整攻击链路：SVG钓鱼为入口，多层载荷接力入侵

本轮攻击瞄准委内瑞拉通信机构，波及智利、巴西、厄瓜多尔、哥伦比亚等整个拉美区域，全套链路层层递进：

1. 诱饵投递：西班牙语税务、财务钓鱼邮件

黑客发送伪装成发票、税务单据的钓鱼邮件，附件是武器化SVG矢量文件。很多人会把SVG当成普通图片，但它本质是可执行XML代码，用浏览器打开就自动执行内嵌逻辑，极易绕过传统邮件过滤设备。

2. 跳转重定向，下载恶意压缩包

SVG文件内置Base64编码短链接，经过多层跳转，导向攻击者控制的`getpdfdigital[.]cloud`等恶意站点，释放受密码保护的7‑ZIP压缩包，内含GoCaracal轻量版植入体`tf‑oficina004a9.exe`。

3. 双工具协同：轻量GoCaracal先站稳脚跟

轻量版GoCaracal执行后完成主机信息采集、建立加密C2通道，作为“入场跳板”，继续向下投递两大载荷：

Delphi加载器，释放老牌后门Bandook（已经做了命令标识符混淆，绕过旧特征库检测）；

完整版Extended GoCaracal，具备全套情报窃取、远控能力。

关键事实：GoCaracal不是直接替换Bandook，而是作为能力补充，两套恶意程序同时在受害主机运行，工具库分层化，就算其中一类工具被查杀，另一套仍可维持入侵链路。

三、GoCaracal：两套配置，模块化设计能力拉满

通过对249份样本溯源，安全研究员还原了GoCaracal从2026年1月到7月完整的迭代进化路线。框架分为轻量版、完整版两套编译配置，同一套代码库按需裁剪功能，适配不同作战场景。

🟢 轻量版（跳板植入体）

定位：快速获取立足点，不做大范围窃密

采集主机基础信息：用户名、操作系统、安全软件列表、活跃窗口；

AES‑GCM加密C2通信；

提供交互式shell、文件下载上传、shellcode注入；

核心使命：下载更多恶意载荷，把控制权交接给后续工具。

🔴 完整版（全功能远控RAT）

完整版从v1.0.1迭代至v1.0.6，拥有34个处理函数，是完整情报收割平台：

1. 系统侦查：遍历进程、磁盘、递归搜索敏感文档；

2. 数据窃取：记录键盘击键记录，窃取Chrome、Brave、Firefox浏览器Cookie与账号密码；

3. 隐秘交互：WebRTC远程桌面，克隆Chrome配置生成隐藏浏览器会话；

4. 网络代理：搭建Socks5代理，把沦陷机器当做内网跳板；

5. 持久驻留：修改注册表，生成特殊NTUSER.MAN配置，实现开机自动复活。

四、最大技术亮点：以太坊智能合约BulletproofC2，做不死的备用指挥通道

这是本次攻击最值得警惕的创新点：攻击者没有把全部C2通信跑在区块链上，而是将以太坊合约当做“配置信息死信箱”。

1. 完整版GoCaracal优先连接预设主C2服务器；

2. 如果主服务器多次连接失败，木马会访问以太坊公共RPC节点，调用`eth\_getStorageAt`读取名为`BulletproofC2`智能合约的存储数据；

3. 合约内部存放备用C2的IP地址，木马读到后写入内存，立刻切换到新服务器继续通信。

攻击者只需要发起一笔链上交易，即可修改合约内存储的IP。不需要更新受害者电脑里的恶意程序二进制文件，成千上万台已中招主机就自动获得新C2地址。就算安全机构查封全部旧的C2基础设施，也无法彻底切断入侵链路。

研究人员观测到，攻击者先在Sepolia测试网调试合约，确认逻辑无误之后再部署到以太坊主网，证明该功能绝非写在样本里的摆设，已经实战落地使用。

五、攻击带来的现实风险

1. 传统IOC查杀部分失效

Bandook做了标识符混淆；GoCaracal模块化编译，不同样本功能差异大，单纯靠旧病毒特征难以拦截。

2. C2基础设施极难彻底根除

借助以太坊合约作为备份通道，防守方很难一次性完全切断通信链路，存在“死灰复燃”风险。

3. SVG附件容易被忽视

SVG常被邮件网关归类为图片，容易绕过邮件安全过滤，成为APT热门入口。

4. 目标以政企通信机构为主

主攻政府、通信、财税相关机构，一旦被入侵，文档、凭证、通信记录全部面临外泄风险。

六、企业安全落地防护建议

1、邮件与网关层防护

严格管控SVG格式附件，不将SVG简单识别为普通图片；对西班牙语的发票、税务主题附件重点告警拦截。

拦截域名列表：`getpdfdigital[.]cloud`、`visualizarpdf[.]online`等相关恶意投递域名。

2、终端EDR重点监控行为（优先行为检测，不单纯依赖哈希）

1. 陌生可执行文件执行后，出现大量主机信息探测、shellcode注入行为；

2. 进程异常访问以太坊公开RPC接口，查询链上合约存储数据；

3. 注册表NTUSER.MAN异常修改、不明来源的Run键持久化；

4. 浏览器凭证数据库被非浏览器进程读取窃取。

3、针对威胁情报处置

导入YARA检测规则，覆盖GoCaracal恶意框架；定期更新Bandook混淆变种的行为告警。

重点排查拉美业务分支机构、涉外财税通信部门历史钓鱼邮件。

4、安全培训要点

提醒业务人员：SVG不是普通图片，不要直接用浏览器打开陌生邮件里的SVG附件，即使文件名写着“发票、收据、报税单”。

写在最后

从AsioGate到全新GoCaracal，Dark Caracal的演变，代表新一代APT的作战思路：不再一味追求复杂零日漏洞，而是模块化恶意代码 + 创新的抗关停基础设施 + SVG钓鱼社会工程学。

区块链技术不止加密货币，也正在被高级威胁组织利用，打造更难根除的指挥控制机制。对有涉外业务，尤其拉美地区业务的国内企业，需要充分重视这类新型间谍活动，不能只依靠静态病毒特征，行为检测、异常通信监控变得愈发关键。

互动：你见过SVG作为钓鱼附件的攻击案例吗？欢迎评论区交流。

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