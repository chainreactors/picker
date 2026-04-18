---
title: 安全简讯（2026.04.17）
url: https://mp.weixin.qq.com/s/57_632c39dxJ2ert4ZCXLg
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:29:13.032916
---

# 安全简讯（2026.04.17）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4S21m309ZrxP9pEwdwd0ZxNbrlCXr4se2vs0kS1jObhVAKv0d93qnMaElsSVHzfFficTOBtyd7g0ibo0RrM7oXbwN268icgYjRFk4gKGIKUlyY/0?wx_fmt=jpeg)

# 安全简讯（2026.04.17）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. 国际“断电行动”重挫DDoS攻击，超七万用户遭警告**

4月16日，在国际执法行动“断电行动”的最新阶段中，全球21个国家协同发力，对分布式拒绝服务（DDoS）攻击产业链进行了深度打击。此次行动由欧洲刑警组织支持，已向超过75,000名使用相关平台发起非法攻击的个人发送了警告邮件或信件。行动期间，执法部门逮捕了四名嫌疑人，查封了53个涉事域名，并执行了25份搜查令。参与国家涵盖多个欧盟成员国，以及澳大利亚、泰国、美国、英国、日本和巴西，展现了全球联合打击网络犯罪的决心。“断电行动”此前已拆除了大量关键基础设施，并查获了包含逾300万个犯罪账户的数据库。在最新阶段，行动重点转向预防与震慑。各国专家在“行动周”前开展了系列冲刺行动，聚焦于DDoS攻击平台的高价值目标用户，同时提升公众对这类活动非法性的认知。执法机构不仅捣毁了非法攻击服务的技术设施，还对“Booter服务”进行了系统性清理。尽管部分运营者以“合法压力测试”为幌子掩饰其真实目的，但由于平台缺乏对攻击目标所有权的验证，这些服务实际上长期被用于非法攻击。

https://www.bleepingcomputer.com/news/security/operation-poweroff-identifies-75k-ddos-users-takes-down-53-domains/

**2. 新型恶意软件ZionSiphon瞄准以色列水设施**

4月16日，一款名为ZionSiphon的新型恶意软件专门针对运营技术领域，尤其以水处理和海水淡化环境为攻击目标，试图通过调节液压和将氯含量提升至危险水平来破坏关键基础设施。该软件由人工智能网络安全公司Darktrace发现，其IP定位及嵌入字符串中的政治信息显示，它似乎专注于攻击位于以色列的目标。部署后，ZionSiphon会检查主机IP是否在以色列范围内，并确认系统是否包含与水或运营技术相关的软件及文件，以确保其运行于水处理或海水淡化系统中。若条件满足，它会通过名为“IncreaseChlorineLevel()”的函数，在现有配置文件中添加文本块，在工厂机械系统物理支持范围内最大限度提高氯的剂量和流量，同时开启氯泵、阀门并将反渗透压力调至80。此外，该恶意软件还会扫描本地子网中的Modbus、DNP3和S7comm等工业控制通信协议，意图与工业控制系统直接交互。ZionSiphon还具备USB传播机制，可将自身复制到可移动驱动器并以隐藏的“svchost.exe”进程运行，同时创建恶意快捷方式文件。由于管理关键功能的计算机通常处于物理隔离状态，不直接连接互联网，USB成为此类攻击的重要传播途径。

https://www.bleepingcomputer.com/news/security/zionsiphon-malware-designed-to-sabotage-water-treatment-systems/

**3. 新僵尸网络PowMix以捷克劳动力为目标**

4月16日，网络安全研究人员发现，一场针对捷克共和国劳动力的恶意攻击活动正在持续进行，其使用一个名为PowMix的此前未被记录的僵尸网络，至少从2025年12月开始活跃。据Cisco Talos研究员Chetan Raghuprasad报告，PowMix采用随机的命令与控制（C2）信标间隔，而非与C2服务器保持持续连接，以此规避网络签名检测。该恶意软件将加密的心跳数据及受害者机器的唯一标识符嵌入C2 URL路径中，模拟合法的REST API URL，并能够远程动态地将新的C2域名更新到僵尸网络配置文件中。攻击链始于一个恶意ZIP文件，该文件激活多阶段感染链，最终释放PowMix。感染链涉及一个Windows快捷方式（LNK），用于启动PowerShell加载器，后者提取嵌入在压缩包中的恶意软件，解密后在内存中运行。这种新型僵尸网络旨在实现远程访问、侦察和远程代码执行，通过定时任务建立持久性，并验证进程树以防止同一主机上运行多个恶意软件实例。与此同时，攻击者还会打开以合规为主题的诱饵文件，提及Edeka等合法品牌并包含薪酬数据及法律法规参考，以分散注意力并增强欺骗性。

https://thehackernews.com/2026/04/newly-discovered-powmix-botnet-hits.html

**4. Rhysida攻击致美医疗中心33.7万人数据泄露**

4月16日，田纳西州库克维尔地区医疗中心（CRMC）于2025年7月遭受Rhysida勒索软件组织攻击，导致约33.7万人的个人及医疗信息泄露。该中心于7月14日检测到可疑活动后，迅速联合执法部门及法证公司展开调查，确认在7月11日至14日期间，有未经授权的第三方访问了医院网络，可能查看或窃取了大量敏感文件。经全面审查受影响文件后，CRMC确认泄露信息因个人情况而异，可能包括姓名、地址、出生日期、社会安全号码、驾驶执照号码、银行账号、医疗信息、病历号及健康保险单信息。医院正在通过邮件向拥有有效地址的受影响个人寄送通知信，建议收信人遵循信中指引保护自身权益。尽管目前尚未证实已发生数据滥用，CRMC仍为受影响者提供免费的身份盗窃保护服务，并敦促公众密切关注账户和信用报告，及时举报可疑活动，必要时联系有关部门。医院还引用了联邦贸易委员会的资源，为公众提供欺诈警报及信用保护的相关提示。2025年8月，Rhysida勒索软件组织将该医疗中心添加至其Tor数据泄露站点，声称窃取了538GB数据。由于无人购买这些被盗数据，该组织最终将其免费公开泄露。

https://securityaffairs.com/190898/cyber-crime/cookeville-regional-medical-center-hospital-data-breach-impacts-337917-people.html

**5. ATHR平台4000美元出售，全自动语音钓鱼窃取凭证**

4月16日，一种名为ATHR的新型网络犯罪平台正以4000美元的价格在地下论坛出售，并收取10%的利润佣金。该平台能够通过全自动语音网络钓鱼攻击窃取包括Google、Microsoft、Coinbase在内的多项服务登录凭证，其社会工程阶段同时使用人类操作员和人工智能代理。据云电子邮件安全公司Abnormal的研究人员分析，ATHR是一个完整的网络钓鱼与语音钓鱼攻击生成器，提供品牌特定的电子邮件模板、针对每个目标的定制功能以及欺骗机制，使邮件看似来自可信发件人。目前该平台支持八项在线服务：Google、Microsoft、Coinbase、Binance、Gemini、Crypto.com、Yahoo和AOL。攻击链始于受害者收到一封精心设计的电子邮件，内容通常为虚假的安全警报或帐户通知，紧急程度足以促使用户拨打电话，但又足够笼统以避开基于内容的过滤器。拨打邮件中的电话号码后，受害者会通过Asterisk和WebRTC连接到AI语音代理，这些代理按照多步骤脚本模拟安全事件。平台仪表盘使操作员能够控制整个流程，包括电子邮件分发、电话管理和实时监控，并接收包含被盗数据的日志。

https://www.bleepingcomputer.com/news/security/new-athr-vishing-platform-uses-ai-voice-agents-for-automated-attacks/

**6. 黑客利用Marimo漏洞部署NKAbuse新变种**

4月16日，黑客正在利用Marimo响应式Python notebook中的一个严重远程代码执行漏洞（CVE-2026-39987），部署托管在Hugging Face Spaces平台上的NKAbuse恶意软件新变种。据云安全公司Sysdig数据，相关攻击在上周开始，目的是窃取凭证，而此时距离技术细节公开披露尚不到10小时。Sysdig研究人员还发现了其他攻击活动，包括4月12日开始的一项行动，该行动滥用Hugging Face Spaces平台，该平台允许用户从Git仓库部署和共享交互式Web应用程序，通常用于AI相关的演示与实验。在Sysdig观察到的攻击中，攻击者创建了一个名为“vsccode-modetx”的空间，其中托管了一个投放脚本和一个名为“kagent”的恶意软件二进制文件，试图模仿合法的Kubernetes AI代理工具。利用Marimo漏洞后，攻击者运行curl命令从Hugging Face下载并执行脚本。该投放脚本下载kagent二进制文件，将其安装到本地，并通过systemd、cron或macOS LaunchAgent设置持久性。该有效载荷是此前未被记录的DDoS攻击恶意软件NKAbuse的变种。

https://www.bleepingcomputer.com/news/security/hackers-exploit-marimo-flaw-to-deploy-nkabuse-malware-from-hugging-face/

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