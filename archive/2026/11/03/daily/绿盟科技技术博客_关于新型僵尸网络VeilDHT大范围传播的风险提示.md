---
title: 关于新型僵尸网络VeilDHT大范围传播的风险提示
url: https://blog.nsfocus.net/%e5%85%b3%e4%ba%8e%e6%96%b0%e5%9e%8b%e5%83%b5%e5%b0%b8%e7%bd%91%e7%bb%9cveildht%e5%a4%a7%e8%8c%83%e5%9b%b4%e4%bc%a0%e6%92%ad%e7%9a%84%e9%a3%8e%e9%99%a9%e6%8f%90%e7%a4%ba/
source: 绿盟科技技术博客
date: 2026-11-03
fetch_date: 2026-11-04T08:17:44.631627
---

# 关于新型僵尸网络VeilDHT大范围传播的风险提示

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* 关于新型僵尸网络VeilDHT大范围传播的风险提示

# 关于新型僵尸网络VeilDHT大范围传播的风险提示

[0](https://blog.nsfocus.net/%E5%85%B3%E4%BA%8E%E6%96%B0%E5%9E%8B%E5%83%B5%E5%B0%B8%E7%BD%91%E7%BB%9Cveildht%E5%A4%A7%E8%8C%83%E5%9B%B4%E4%BC%A0%E6%92%AD%E7%9A%84%E9%A3%8E%E9%99%A9%E6%8F%90%E7%A4%BA/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-11-0318:55") 发布于 21 小时前

![](https://blog.nsfocus.net/wp-content/uploads/2026/11/CNCERT网络安全信息动态.jpg)

阅读： 52

**感谢绿盟科技伏影实验室在本报告的样本分析工作中做出的重要贡献。**

### 一、概述

近期，国家互联网应急中心（CNCERT）监测发现一种隐蔽性极强的全新僵尸网络正在大范围传播，主要感染Linux服务器与IoT设备。其传播以漏洞利用为主，我们将其命名为VeilDHT，其中，DHT取自其藏身公共分布式网络的备用控制信道，其实际控制地址经DNS假IP应答与DHT混流双通道获取。

VeilDHT是一个功能体系完备、以隐蔽性为核心设计理念的全新僵尸网络家族，其开发者具备专业的密码工程素养，已对Linux服务器与IoT设备生态构成现实威胁。与多数将工程投入集中于攻击能力的僵尸网络不同，VeilDHT把主要精力放在隐蔽性上，功能也更为全面：配置以乱序密文存放，通信采用认证加密，心跳完全随机化，发现、阻断、解密和清理的难度都明显提升；功能上具备DDoS攻击、任意命令执行、交互式反向Shell及反向代理能力，一旦感染，受害主机便同时成为攻击源、隐蔽跳板和长期可控的资源。2026年10月16日至10月26日期间，CNCERT监测发现该僵尸网络感染的日上线肉鸡数最高达到15805台，累计已有40467台设备受其感染。现将其主要情况分析披露如下。

### 二、恶意样本分析

![](https://p3-sign.toutiaoimg.com/tos-cn-i-axegupay5k/a0951983fd594129a0e864bf701189d2~tplv-tt-origin-web:gif.jpeg?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1794307969&x-signature=wxOZuum4WuUhE8iXK9vQojrFUm4%3D)

图 1 VeilDHT僵尸网络

**1.传播方式**

该木马主要通过漏洞利用实现扩散，目标以Linux服务器和各类IoT设备为主，当前观测到攻击者使用的漏洞如下：

CVE-2024-3912：ASUS路由器命令注入漏洞

CVE-2021-35394：Realtek Jungle SDK 命令注入漏洞

**2.通信机制**

C&C寻址机制是该家族最突出的特点，木马通过两条通道获取真实控制端地址，均以伪装为前提。一是经过加密编码的DNS应答，二是公共P2P网络。两条通道均对真实控制端地址进行了伪装，互为备份，控制面摆脱了对固定域名或IP的依赖，使其控制端得以长期隐藏，检测、封禁与追踪的难度较高。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/463de95c7b304da0bf00106c5ef75e49~tplv-tt-origin-web:gif.jpeg?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1794307969&x-signature=3WxcU9TaPUUV2KjSCA%2B7yd%2Bo%2FLs%3D)

图 2 VeilDHT获取控制ip方式示意图

VeilDHT通信保护贯穿握手、认证、指令传输全过程，其中使用了Ed25519、X25519、SHA-512、XChaCha20-Poly1305等加密算法。上线时，木马以内置验证公钥核验控制端签名，确认无误后才建立会话；其后发送的主机信息、心跳与指令全部在加密通道内传输。该体系严格遵循现代密码工程规范，远超僵尸网络常见的轻量混淆。只有在密钥交换阶段就完整掌握流量，事后截获的通信数据才有解密的可能。这套加密逻辑的完整和严谨程度在僵尸网络中并不多见，说明开发者具备专业的密码工程能力。

**3.核心功能**

VeilDHT僵尸网络具备覆盖UDP、TCP、GRE等协议的20种DDoS攻击、任意命令执行、交互式反向Shell及反向代理能力，控制端还可查询主机信息、控制主机重启并令木马自删除。DDoS攻击、命令执行、代理和管控等能力一应俱全，一旦被感染，受害主机便会同时成为攻击源、隐蔽跳板和长期可控的资源。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/b413ca0c45f842a99b6d63bd177475d9~tplv-tt-origin-web:gif.jpeg?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1794307969&x-signature=CLNNLeZlR5EiGV84qq4%2FY3LIW%2B0%3D)

图 3 VeilDHT功能体系示意图

**信息收集：**VeilDHT会收集并上传受害主机的架构、主机名、内存、进程数等信息，为后续的横向移动或更有针对性的攻击提供信息基础。

**命令执行：**该家族具备命令执行功能，能够执行任意系统命令，并可重启主机、令木马自删除，威胁性因此显著提升；

**反向Shell：**能够建立交互式的反向Shell通道，对受害主机形成完全控制，可作为进一步攻击的立足点；

**反向代理：**能够转发网络流量，将受害主机用作攻击跳板，隐藏攻击者的真实来源；

**DDoS攻击：**支持20种攻击方式、覆盖多种协议，攻击指令可动态下发，实现对指定目标的精准打击。

**4.对抗与规避检测**

除上述功能外，木马在通信、心跳、配置存储、进程运行等方面均进行了专门的隐蔽处理，并支持版本的滚动更新，整体上分析、阻断和清理的难度较高。

**通信：**木马与控制端之间的通信全程加密，攻击指令与回传数据均以密文形式传输，且其加密设计使得其通信流量即使被中途截获也难以还原，通信隐蔽性强。

**心跳：**木马的心跳采用随机化机制，周期与内容均呈随机特征，规避了基于固定规律的流量检测。

**配置存储：**木马的配置信息以密文形式存放，并打乱存储顺序，静态分析难以按序还原完整的配置内容。

**版本的滚动更新：**木马支持版本的滚动更新，可在受害主机上自动完成升级，使控制端能够持续推送新版本、长期掌控受控节点。

### 三、感染规模

通过监测分析发现，2026年10月16日至26日期间，VeilDHT僵尸网络在我国境内感染“肉鸡”规模约40467台，境内日上线肉鸡数量最高达15805台。其感染量变化趋势如下：

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/1c65171aefbb407e8d621084c791810c~tplv-tt-origin-web:gif.jpeg?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1794307969&x-signature=%2Bl3rXjlWa%2F8CjbTuIcjlMbbSFcY%3D)

图 4 境内感染终端数量

###

### 四、总结

VeilDHT具备极强的隐蔽性，其对抗设计贯穿配置、寻址、通信、心跳与节点接管等环节：配置以乱序密文存放，DNS应答返回的皆为伪装IP，通信全程加密，心跳呈随机规律，版本更替采用协商式的滚动接管，层层设防，构成一套完备的对抗体系。

该家族现阶段正处于传播扩张期，其开发者是一个具备专业能力的运营团伙，意在构建一个能够长期在线、隐蔽持久的资源池。受控主机将同时被用作DDoS攻击源和隐蔽攻击跳板，对Linux服务器与IoT设备生态构成现实威胁，需要持续监测和高度警惕。

### 五、防范建议

请广大网民和网络运营者强化风险意识，加强安全防范，避免不必要的经济损失，主要建议包括：

1.及时梳理资产清单，修复相关系统漏洞，包括历史漏洞和最新曝光漏洞，IoT设备应同步升级固件。

2.加强口令强度，避免使用弱口令，密码设置应包含大小写字母、数字和符号，建议使用16位或更长密码，不同设备使用不同口令并定期更换。

3.尽量不打开来历不明的网页链接，不安装来源不明软件；通过官方网站等可信渠道获取软件，下载后校验文件哈希。

4.安装终端防护软件，定期全盘查杀；重点排查异常进程、异常外连，以及本提示所列特征字符串和异常端口监听。

5.网络运营者应监测本提示所列IOC的域名解析请求与IP连接情况（所列域名的当前解析结果为伪装IP，真实控制端以下列IP为准），发现异常及时阻断并留存证据。

6.发现主机感染后，立即核实受控情况与入侵途径，对受害主机隔离清理，并及时向属地主管部门报告。

### 六、相关IoC

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

最后修改日期: 2026-11-03

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [绿盟科技登榜AI赋能安全技术路线图，入围数量居安全厂商首位](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E7%99%BB%E6%A6%9Cai%E8%B5%8B%E8%83%BD%E5%AE%89%E5%85%A8%E6%8A%80%E6%9C%AF%E8%B7%AF%E7%BA%BF%E5%9B%BE%EF%BC%8C%E5%85%A5%E5%9B%B4%E6%95%B0%E9%87%8F%E5%B1%85%E5%AE%89/)
* [Linux内核IPv4 TCP释放后重用漏洞（CVE-2026-98432）通告](https://blog.nsfocus.net/linux%E5%86%85%E6%A0%B8ipv4-tcp%E9%87%8A%E6%94%BE%E5%90%8E%E9%87%8D%E7%94%A8%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-98432%EF%BC%89%E9%80%9A%E5%91%8A/)
* [关于新型僵尸网络VeilDHT大范围传播的风险提示](https://blog.nsfocus.net/%E5%85%B3%E4%BA%8E%E6%96%B0%E5%9E%8B%E5%83%B5%E5%B0%B8%E7%BD%91%E7%BB%9Cveildht%E5%A4%A7%E8%8C%83%E5%9B%B4%E4%BC%A0%E6%92%AD%E7%9A%84%E9%A3%8E%E9%99%A9%E6%8F%90%E7%A4%BA/)
* [绿盟科技联合电科金仓发布一体化信创方案，打造自主可控、智能高效的安全防护体系](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E8%81%94%E5%90%88%E7%94%B5%E7%A7%91%E9%87%91%E4%BB%93%E5%8F%91%E5%B8%83%E4%B8%80%E4%BD%93%E5%8C%96%E4%BF%A1%E5%88%9B%E6%96%B9%E6%A1%88%EF%BC%8C%E6%89%93%E9%80%A0/)
* [2026 TechWorld·上海站成功举办，绿盟科技上海研究院正式落地](https://blog.nsfocus.net/2026-techworld%C2%B7%E4%B8%8A%E6%B5%B7%E7%AB%99%E6%88%90%E5%8A%9F%E4%B8%BE%E5%8A%9E%EF%BC%8C%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E4%B8%8A%E6%B5%B7%E7%A0%94%E7%A9%B6%E9%99%A2%E6%AD%A3%E5%BC%8F%E8%90%BD/)

## 文章导航

[上一篇文章 绿盟科技联合电科金仓发布一体化信创方案，打造自主可控、智能高效的安全防护体系](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E8%81%94%E5%90%88%E7%94%B5%E7%A7%91%E9%87%91%E4%BB%93%E5%8F%91%E5%B8%83%E4%B8%80%E4%BD%93%E5%8C%96%E4%BF%A1%E5%88%9B%E6%96%B9%E6%A1%88%EF%BC%8C%E6%89%93%E9%80%A0/)

[下一篇文章 Linux内核IPv4 TCP释放后重用漏洞（CVE-2026-98432）通告](https://blog.nsfocus.net/linux%E5%86%85%E6%A0%B8ipv4-tcp%E9%87%8A%E6%94%BE%E5%90%8E%E9%87%8D%E7%94%A8%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-98432%EF%BC%89%E9%80%9A%E5%91%8A/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).