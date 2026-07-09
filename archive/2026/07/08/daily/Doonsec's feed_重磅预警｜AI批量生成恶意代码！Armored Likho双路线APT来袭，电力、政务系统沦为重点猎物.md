---
title: 重磅预警｜AI批量生成恶意代码！Armored Likho双路线APT来袭，电力、政务系统沦为重点猎物
url: https://mp.weixin.qq.com/s/viA04EI6pOSSixSOSGXoDQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:56:50.604500
---

# 重磅预警｜AI批量生成恶意代码！Armored Likho双路线APT来袭，电力、政务系统沦为重点猎物

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/E3ZvvAXyiaibmUQFYvhyWSzDqLunL9PboSWvB6ytpAjleqlzHRCXkWlxMzB0dvBHpiaRUGeLyYuv4QSQjIvmP8f6CvWuz6pQl0PYOO523OtIBY/0?wx_fmt=jpeg)

# 重磅预警｜AI批量生成恶意代码！Armored Likho双路线APT来袭，电力、政务系统沦为重点猎物

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkQByKkBIbw5GgEW0LccyUvs4trIn6ndaibVticlmhjnyCBa3oe4YGria9HFcglHKd8dSbHxKMMoUgBw3jTrsjdicAMNwMy8lvaIrk/640?wx_fmt=png&from=appmsg)

2026年7月，卡巴斯基联合SecurityAffairs披露全新高级威胁组织Armored Likho（代号Eagle Werewolf），该团伙首次大规模使用大模型生成全套攻击载荷，一套工具双线作战：一边针对俄、哈、巴西电力、政府机构长期间谍窃密，一边面向普通用户盗取加密资产。自研BusySnake窃取木马搭配Go2Tunnel反向隧道，利用LNK高危漏洞+Python隐蔽加载，传统杀毒极难拦截，政企基础设施务必紧急自查！

情报来源：SecurityAffairs官方威胁报告，卡巴斯基实验室完整样本溯源分析

一、全新APT团伙：双线攻击，兼顾情报窃取与加密洗钱

团伙两大攻击赛道（罕见双目标模式）

绝大多数黑产/APT只会选择牟利或间谍单一路线，Armored Likho同时布局两条攻击链：

1. 国家级定向间谍线（核心目标）

主攻俄罗斯、哈萨克斯坦、巴西政府机关、电网电力基础设施，长期潜伏窃取政务文件、电力调度数据、基建核心图纸，无加密勒索行为，以情报收集为最终目的。

2. 黑产牟利支线

面向普通个人、中小企业终端，窃取浏览器密码、OTP验证码、加密货币私钥、远程桌面凭证，批量倒卖或盗取数字资产变现。

核心攻击武器库

1. AI自动生成多级加载器（本次最大突破）

2. BusySnake Python多功能窃取木马（主力载荷）

3. Go2Tunnel反向SSH隧道工具（内网远程控制）

4. 混淆模块化RAT远控、NSIS自解压恶意安装包

二、划时代威胁：大模型AI批量生成恶意加载器，溯源难度拉满

AI恶意代码三大标志性特征（一眼识别团伙样本）

安全研究员发现该团伙所有一级加载脚本都带有极强AI生成痕迹，人工编写恶意代码绝不会出现：

1. 代码附带大量冗余图文注释、emoji项目符号、分段标记；

2. 代码结构重复、逻辑分段模板化，每次攻击样本结构完全不同；

3. 无需专业黑客开发，仅通过LLM对话即可快速迭代新载荷。

对防御的致命冲击

1. 快速变种：一次钓鱼活动可生成上千份结构各异的恶意脚本，特征库完全跟不上；

2. 溯源困难：无固定代码指纹，无法通过传统样本关联团伙；

3. 降低门槛：零基础攻击者也能批量产出绕过静态查杀的加载程序。

三、两条入侵链路：LNK漏洞/NSIS安装包，双击即沦陷

团伙设计两套投递载体，全部依托鱼叉钓鱼邮件投放，诱饵贴合政务、民生场景：政府通知、人道救助申请表、线上心理测评问卷。

路径1：恶意LNK快捷方式（高危漏洞ZDI-CAN-25373）

1. 压缩包内伪装文档的lnk快捷，利用漏洞隐藏后台执行命令；

2. 用户仅双击查看文档，后台自动拉起PowerShell；

3. 脚本从官方Python源下载3.12.10嵌入式安装包、pip工具；

4. 静默部署至`%APPDATA%\WindowsHelper`专属工作目录。

路径2：NSIS自解压恶意安装程序

1. 打开弹出虚假心理测评页面迷惑用户；

2. 后台注入加载器至系统可信进程内存；

3. 从GitHub开发仓库拉取全套木马组件落地同一目录。

两条链路最终落地路径完全统一，所有恶意程序集中存放`WindowsHelper`文件夹，便于统一管理。

完整Python部署恶意脚本逻辑（攻击核心步骤）

PowerShell绕过系统限制静默下载官方Python，重命名无窗口`pythonw.exe`运行木马，全程无弹窗、无报错：

1. 下载Python 3.12.10离线安装包，静默自定义安装；

2. 自动拉取get-pip工具，离线安装依赖环境；

3. 释放加密BusySnake窃取器pyc文件；

4. 创建计划任务、VBS启动器实现永久驻留。

四、主力木马BusySnake深度拆解：全能窃密+隐蔽隧道

1. 高强度加密保护，运行全程解密

采用PyArmor Pro 9.2.0加密Python字节码，函数调用时临时解密，执行完毕立刻重新加密；使用`.pyw`无窗口后台运行，任务管理器仅显示无标识Python进程。

2. 全方位数据窃取能力（覆盖几乎所有凭证）

剪贴板无限循环监控，记录所有复制密码、私钥、OTP链接；

全盘扫描64位十六进制字符串（加密钱包私钥、API密钥）自动回传；

浏览器全量窃取：Chrome/Edge DPAPI解密密码、Firefox密钥库直接读取；

Telegram会话打包、RustDesk远程桌面截图盗取登录凭证；

自动上传桌面、下载文件夹5MB以内全部文档；

全局键盘记录，带时间戳留存完整操作记录。

3. 隐蔽持久化，规避常规运维排查

1. 五分钟高频循环计划任务，不使用原生schtasks命令，改用COM组件`Schedule.Service`创建，行为告警极难捕捉；

2. 自定义锁文件防止多开，不使用系统互斥体，进程监控工具无法识别；

3. 伪装系统目录`WindowsHelper`，命名模仿微软官方更新程序。

4. 内置Go2Tunnel反向SSH隧道，实现内网全权接管

1. 连接域名`grked[.]online`获取隧道密钥与连接指令；

2. 建立持久反向SSH通道，黑客远程交互式操作内网终端；

3. 新增沙箱延迟机制，运行前置延时，避开自动化动态分析；

4. 任务分级管理：SCHEDULED/IN\_PROGRESS/SUCCEEDED/FAILED四状态上报C2。

5. C2通信基础设施

指令服务器IP：159.198.41.140

隧道中转IP：159.198.32.222

核心配置域名：grked[.]online

五、高风险单位&高危行为自查清单

重点受害行业

1. 各地政务机关、外事单位；

2. 电网、电力调度、能源基础设施企业；

3. 外贸、跨境机构、个人加密货币投资者；

4. 科研院所、持有大量涉密文档办公终端。

企业高危漏洞行为

1. 未修复ZDI-CAN-25373 LNK高危快捷漏洞；

2. 终端无EDR，仅依靠免费杀毒，无法监控COM创建计划任务；

3. 允许PowerShell无限制外网下载运行Python安装包；

4. 员工随意打开邮件内lnk快捷、不明自解压程序；

5. 内网无分段，办公终端可直连电力、政务核心服务器；

6. 未监控对外SSH反向隧道外联流量。

六、分层落地防御方案（政企运维专用）

一、员工基础防线：切断钓鱼入口

1. 陌生邮件压缩包、带lnk快捷附件一律不打开，政府通知、救助文件线下核验；

2. 系统开启完整文件扩展名显示，区分文档与恶意快捷；

3. 禁止随意运行外部NSIS自解压安装程序；

4. 收到心理测评、线上问卷类邮件提高警惕，全部走沙箱检测。

二、终端安全加固（拦截BusySnake核心手段）

1. 及时更新Windows全量补丁，修复ZDI-CAN-25373 LNK漏洞；

2. EDR添加监控规则：拦截COM组件创建高频五分钟计划任务；

3. 告警监控`%APPDATA%\WindowsHelper`可疑目录，出现立即隔离；

4. 限制PowerShell外联下载Python、pip等开发工具；

5. 监控无窗口`pythonw.exe`后台长期驻留、批量读取浏览器密钥库行为；

6. 屏蔽木马C2、隧道中转IP与域名黑名单。

三、网络边界防护

1. 出口防火墙阻断反向SSH隧道外联行为；

2. 审计终端访问GitHub、境外Python源大量下载流量；

3. 留存全量网络日志，重点排查长期后台加密上传行为；

4. 电力、政务内网与互联网严格物理/逻辑隔离。

四、疑似中毒应急处置步骤

1. 立即断开内外网，禁止重启保留内存取证；

2. 删除`WindowsHelper`完整目录，清理相关Python程序；

3. 检索并清除COM创建的五分钟循环计划任务；

4. 全盘修改浏览器、系统、远程桌面、加密钱包密码，开启二次验证；

5. 全网批量扫描同源Python窃取木马，排查横向扩散；

6. 导出进程、网络日志留存，同步上报安全管理部门。

七、行业安全趋势总结

Armored Likho攻击标志AI生成恶意代码APT正式规模化落地。过去黑客手动编写的木马存在固定特征，如今依靠大模型快速生成海量变种，传统基于样本、代码特征的防护体系全面失效。

电力、政务等关键基础设施作为首要攻击目标，不能仅依靠杀毒软件，必须结合行为监控、漏洞修复、流量审计、员工钓鱼培训构建多层防御。随着LLM普及，后续会出现更多AI赋能APT攻击，政企安全体系需同步升级行为检测能力。

你们单位是否管控PowerShell外网下载权限？遇到过伪装政务通知的钓鱼邮件吗？评论区交流运维防护经验！

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