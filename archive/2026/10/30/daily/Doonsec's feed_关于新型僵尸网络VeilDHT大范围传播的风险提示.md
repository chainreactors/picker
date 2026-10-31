---
title: 关于新型僵尸网络VeilDHT大范围传播的风险提示
url: https://mp.weixin.qq.com/s/nYrmahLRnWBgZJdCZ3z8lQ
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:44:07.463049
---

# 关于新型僵尸网络VeilDHT大范围传播的风险提示

# 关于新型僵尸网络VeilDHT大范围传播的风险提示

原创

CNCERT
CNCERT

国家互联网应急中心CNCERT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRgf8gaicNlle1rOEwXqD6WrQDcQk3iaAsucOxYoJmfcQqCg0qrAObheSnStArW0kysg5M0XBicOgJyuIDXuyeKc1Ly2uiaRBkIKrG4/640?wx_fmt=png&from=appmsg)

感谢绿盟科技伏影实验室在本报告的样本分析工作中做出的重要贡献。

一、概述

近期，国家互联网应急中心（CNCERT）监测发现一种隐蔽性极强的全新僵尸网络正在大范围传播，主要感染Linux服务器与IoT设备。其传播以漏洞利用为主，我们将其命名为VeilDHT，其中，DHT取自其藏身公共分布式网络的备用控制信道，其实际控制地址经DNS假IP应答与DHT混流双通道获取。

VeilDHT是一个功能体系完备、以隐蔽性为核心设计理念的全新僵尸网络家族，其开发者具备专业的密码工程素养，已对Linux服务器与IoT设备生态构成现实威胁。与多数将工程投入集中于攻击能力的僵尸网络不同，VeilDHT把主要精力放在隐蔽性上，功能也更为全面：配置以乱序密文存放，通信采用认证加密，心跳完全随机化，发现、阻断、解密和清理的难度都明显提升；功能上具备DDoS攻击、任意命令执行、交互式反向Shell及反向代理能力，一旦感染，受害主机便同时成为攻击源、隐蔽跳板和长期可控的资源。2026年10月16日至10月26日期间，CNCERT监测发现该僵尸网络感染的日上线肉鸡数最高达到15805台，累计已有40467台设备受其感染。现将其主要情况分析披露如下。

二、恶意样本分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRiauo017ZqISOkbfVthsAX8IsdOib2rURyqq36rBgnfqd5I1qFePIY04gNNFYavqLoy67NgwdgQX150f6ic94mb3lRryYrIjGh7RU/640?wx_fmt=png&from=appmsg)

图 1 VeilDHT僵尸网络

1.传播方式

该木马主要通过漏洞利用实现扩散，目标以Linux服务器和各类IoT设备为主，当前观测到攻击者使用的漏洞如下：

CVE-2024-3912：ASUS路由器命令注入漏洞

CVE-2021-35394：Realtek Jungle SDK 命令注入漏洞

2.通信机制

C&C寻址机制是该家族最突出的特点，木马通过两条通道获取真实控制端地址，均以伪装为前提。一是经过加密编码的DNS应答，二是公共P2P网络。两条通道均对真实控制端地址进行了伪装，互为备份，控制面摆脱了对固定域名或IP的依赖，使其控制端得以长期隐藏，检测、封禁与追踪的难度较高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRg3qeEfpz5tmMjIicBLLcsnyeEVbg79icU07qrDiaMOxN1TbffLxKllWCYsiaWtIya0JVgib8ibvcWy3Z2M7iaNAPMcU5ASYJ4PHKqz5k/640?wx_fmt=png&from=appmsg)

图 2 VeilDHT获取控制ip方式示意图

VeilDHT通信保护贯穿握手、认证、指令传输全过程，其中使用了Ed25519、X25519、SHA-512、XChaCha20-Poly1305等加密算法。上线时，木马以内置验证公钥核验控制端签名，确认无误后才建立会话；其后发送的主机信息、心跳与指令全部在加密通道内传输。该体系严格遵循现代密码工程规范，远超僵尸网络常见的轻量混淆。只有在密钥交换阶段就完整掌握流量，事后截获的通信数据才有解密的可能。这套加密逻辑的完整和严谨程度在僵尸网络中并不多见，说明开发者具备专业的密码工程能力。

3.核心功能

VeilDHT僵尸网络具备覆盖UDP、TCP、GRE等协议的20种DDoS攻击、任意命令执行、交互式反向Shell及反向代理能力，控制端还可查询主机信息、控制主机重启并令木马自删除。DDoS攻击、命令执行、代理和管控等能力一应俱全，一旦被感染，受害主机便会同时成为攻击源、隐蔽跳板和长期可控的资源。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRhyNmxDL5WNP4I87vc9ph8AoNFfD0RtXCSl9HqenKQJmYfTQoYhHibFiaWQdUDEhJwaGgfp6qzk7FTlVNBmGpicYpLJk23ordszpQ/640?wx_fmt=png&from=appmsg)

图 3 VeilDHT功能体系示意图

信息收集：VeilDHT会收集并上传受害主机的架构、主机名、内存、进程数等信息，为后续的横向移动或更有针对性的攻击提供信息基础。

命令执行：该家族具备命令执行功能，能够执行任意系统命令，并可重启主机、令木马自删除，威胁性因此显著提升；

反向Shell：能够建立交互式的反向Shell通道，对受害主机形成完全控制，可作为进一步攻击的立足点；

反向代理：能够转发网络流量，将受害主机用作攻击跳板，隐藏攻击者的真实来源；

DDoS攻击：支持20种攻击方式、覆盖多种协议，攻击指令可动态下发，实现对指定目标的精准打击。

4.对抗与规避检测

除上述功能外，木马在通信、心跳、配置存储、进程运行等方面均进行了专门的隐蔽处理，并支持版本的滚动更新，整体上分析、阻断和清理的难度较高。

通信：木马与控制端之间的通信全程加密，攻击指令与回传数据均以密文形式传输，且其加密设计使得其通信流量即使被中途截获也难以还原，通信隐蔽性强。

心跳：木马的心跳采用随机化机制，周期与内容均呈随机特征，规避了基于固定规律的流量检测。

配置存储：木马的配置信息以密文形式存放，并打乱存储顺序，静态分析难以按序还原完整的配置内容。

版本的滚动更新：木马支持版本的滚动更新，可在受害主机上自动完成升级，使控制端能够持续推送新版本、长期掌控受控节点。

三、感染规模

通过监测分析发现，2026年10月16日至26日期间，VeilDHT僵尸网络在我国境内感染“肉鸡”规模约40467台，境内日上线肉鸡数量最高达15805台。其感染量变化趋势如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRhVticV12qKRAvIicYb8crwrVqHzaE1CUQ5F1kkbqeh7ZayicdkFtQOe56803MgNkib0pJpDZsvHUIaGiayiaIZwicgwZ0X3yAxoBtx0c/640?wx_fmt=png&from=appmsg)

图 4 境内感染终端数量

四、总结

VeilDHT具备极强的隐蔽性，其对抗设计贯穿配置、寻址、通信、心跳与节点接管等环节：配置以乱序密文存放，DNS应答返回的皆为伪装IP，通信全程加密，心跳呈随机规律，版本更替采用协商式的滚动接管，层层设防，构成一套完备的对抗体系。

该家族现阶段正处于传播扩张期，其开发者是一个具备专业能力的运营团伙，意在构建一个能够长期在线、隐蔽持久的资源池。受控主机将同时被用作DDoS攻击源和隐蔽攻击跳板，对Linux服务器与IoT设备生态构成现实威胁，需要持续监测和高度警惕。

五、防范建议

请广大网民和网络运营者强化风险意识，加强安全防范，避免不必要的经济损失，主要建议包括：

1.及时梳理资产清单，修复相关系统漏洞，包括历史漏洞和最新曝光漏洞，IoT设备应同步升级固件。

2.加强口令强度，避免使用弱口令，密码设置应包含大小写字母、数字和符号，建议使用16位或更长密码，不同设备使用不同口令并定期更换。

3.尽量不打开来历不明的网页链接，不安装来源不明软件；通过官方网站等可信渠道获取软件，下载后校验文件哈希。

4.安装终端防护软件，定期全盘查杀；重点排查异常进程、异常外连，以及本提示所列特征字符串和异常端口监听。

5.网络运营者应监测本提示所列IOC的域名解析请求与IP连接情况（所列域名的当前解析结果为伪装IP，真实控制端以下列IP为准），发现异常及时阻断并留存证据。

6.发现主机感染后，立即核实受控情况与入侵途径，对受害主机隔离清理，并及时向属地主管部门报告。

六、相关IoC

82de137cfb3d7a6bf38cca60e85b8476c75c646c764071f98b8cb34d9de42e44

http[:]//160.119.66.18:80/n2/

http[:]//160.119.71.134/n2/

t-smc[.]top

wish-list[.]cfd

mgnacrrrta[.]cfd

lostmymind[.]cfd

afterhours[.]click

nightslikethis[.]club

imagiraffe[.]shop

namecheat.niggerservers[.]xyz

boopfactory[.]top

135.136.191[.]231

82.27.2[.]131

144.172.67[.]77

151.243.213[.]187

176.100.39[.]134

178.83.206[.]213

176.100.36[.]169

156.246.90[.]214

23.27.230[.]15

45.146.131[.]109

209.141.61[.]163

160.119.71[.]27

143.246.62[.]76

217.113.235[.]21

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjias1f0ya4xRXa4ksGEFrPEojCsltT0hVibveROdPV42mpAdAJ03ZynIbRRGesKGHW6SVz6yoibOjibVta2vrBeLnOOBSm58vorQ0/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz65uZccENTFwtVytvibEnzNbibwZw0F5MItQaglR2pQNzcw4dYE1FfLGuMhRztcV49nmwkkexPBKZPibQ/0?wx_fmt=png)

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