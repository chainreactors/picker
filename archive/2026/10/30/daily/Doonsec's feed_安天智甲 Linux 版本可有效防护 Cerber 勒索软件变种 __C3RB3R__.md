---
title: 安天智甲 Linux 版本可有效防护 Cerber 勒索软件变种 \"C3RB3R\"
url: https://mp.weixin.qq.com/s/oMsbZ5FGqIaxXsumbtYmAg
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:43:14.426846
---

# 安天智甲 Linux 版本可有效防护 Cerber 勒索软件变种 \"C3RB3R\"

# 安天智甲 Linux 版本可有效防护 Cerber 勒索软件变种 "C3RB3R"

安天CERT
安天CERT

安天垂直响应平台

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方"蓝字"

关注我们吧！

本报告由[安天CERT](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650208789&idx=2&sn=00b7643e03b81ed7c151388153fce778&scene=21#wechat_redirect)工程师结合安天（Antiy）[AVL Code](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215515&idx=1&sn=1dea52c669e041d35f049f0fdce5bb1e&scene=21#wechat_redirect)与[澜砥N2.6威胁检测分析大模型](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215429&idx=1&sn=90a38343331dcf53aace361ea618edfb&scene=21#wechat_redirect)辅助生成。

#

# 1. **概述**

#

# **近日，安天CERT 监测发现，自2026年10月28日起，互联网上出现针对群晖（Synology）NAS 设备的集中勒索攻击活动。本次攻击载荷为 Cerber 勒索软件的 Linux 平台变种，安全社区依据勒索信标识、暗网联络信息，将该变种暂命名为“C3RB3R”。 该勒索软件加密文件后原文件名保留，文件后缀追加`.L0CK3D`，各目录下生成勒索说明文件`read-me3.txt`。**载荷具备对群晖DSM 特有目录进行遍历排查的能力**，受害设备覆盖场景较广。 该勒索软件为Cerber 勒索软件家族 Linux 分支变种。原始 Cerber 家族最早于 2016 年被安全业界公开监测；该分支（社区代称 C3RB3R）最早在 2023 年捕获到相关样本。安天 CERT 依托安天 AVL Code 智能体，基于澜砥垂直模型开展样本分析，已完成恶意代码解析并形成专项分析报告。**同时建议相关用户及时更新群晖DSM 系统补丁，修复高危漏洞，并避免将管理端口直接暴露在公网。** **经验证，安天智甲终端防御系统**Linux 版本（简称 IEP）可实现对该勒索软件的有效查杀，为用户终端提供防护能力。 2. 攻击分析 C3RB3R 勒索软件最初以 Windows 平台传播而知名，本样本为其 Linux 变体，主要针对公网暴露的存储类设备。攻击者主要利用设备公网暴露、未严格管控的访问入口，尝试通过授权绕过或远程代码执行类漏洞获取管理员权限，进而实施入侵。样本的攻击链完整覆盖"初始访问→持久化→密钥生成→文件加密→勒索信投放"等多个阶段： **表****2****-****1****攻击者实施攻击的步骤** | | | | --- | --- | | **阶段** | **行为描述** | | **初始访问** | 主要利用公网暴露存储设备上的授权绕过、远程代码执行类漏洞获取权限。 | | **持久化** | 从 /proc/self/exe 读取自身，复制到 /var/lock、/dev/shm、/var/tmp、/tmp 等目录并伪装为系统组件（init-rsysd 等） | | **密钥生成** | 从 /dev/urandom（回退 /dev/random）读取随机字节，生成 AES 对称加密密钥与初始向量 | | **文件加密** | 递归遍历（跳过系统目录与已加密文件），用ChaCha20算法对目标文件加密 | | **勒索信** | 在目录中写入动态构造的 read-me3.txt 勒索信，并生成 C3RB3R\_LOG.txt 日志 | | **防御规避** | 字符串混淆（仿射变换）、单实例互斥锁机制、规避系统目录 | 2.1**样本分析** C3RB3R 勒索家族该 Linux 变体为 C++ 编写的 ELF 可执行程序，具备完整的勒索攻击链：单实例互斥→命令解析→字符串解密→自复制持久化→ChaCha20加密文件→追加扩展名→写入勒索信。 **表****2****-****2****样本标签** | | | | --- | --- | | **病毒名称** | Trojan/Linux.Cerber[Ransom] | | **MD5** | A1375E0F82AE86DF528876C049B5A23C | | **文件****大小** | 451.48 KB (462,312字节) | | **文件****格式** | ELF | | **目标平台** | Linux | | **编译****语言** | C++ | | **VT首****次上传时间** | 2026-10-28 04:02:19 | | **加密扩展名** | .L0CK3D | | **勒索信** | read-me3.txt | | **联系方式** | Tor | 加密后勒索信内容如下，勒索信起始标识为 “C3RB3R INSTRUCTIONS”。 ![](https://mmecoa.qpic.cn/mmecoa_png/frAs2k03YpnQ4doHPSNSaQeO5vnZ6nLq8Amrr6OKibOcEovrUnGgFpEcyaGOWbeick8TfIGROc6OSrdtJdLKHppK6jXz9wZQAlnia3CjzcuZlg/640?wx_fmt=png&from=appmsg)  图**2****-****1****勒索信** **安天 CERT 提示：不要支付赎金，付费无法确保完成解密，还会助长勒索犯罪。** 该样本经检测为UPX加壳，AVL Code自动化脱壳。  ![](https://mmecoa.qpic.cn/sz_mmecoa_png/frAs2k03YplWgEN2L0E33hGZ5XPTZiaGaT3FibhXEHic6poHlXbqgmXoBtGCIIpvaVBaIdIzg7dQicYmIIej3djlLbsNia5PXOCBITbRCSH5ZIQ8/640?wx_fmt=png&from=appmsg) **图****2****-****2****自动化脱壳** **（****安天AVL Code智能体基于澜砥垂直模型分析生成****）** 分析确认该勒索软件加密文件方式具体为文件内容用 ChaCha20加密形成移动密文A，ChaCha20密钥使用AES密钥（勒索软件启动时随机生成）加密形成一段密文B，将密文B与AES密钥用RSA加密形成一段密文C，最后拼接文件内容：密文A+密文C+原始文件大小。 ![](https://mmecoa.qpic.cn/sz_mmecoa_png/frAs2k03YpnymViaPwvukgGlNiaupSy6o1GEwoQSl7DTYK9Z02hm2bo949faj8RHJp60Kr8Jz5Vlic6Ys7sOweMvia8C43oXH63RQ5NgbmltWIU/640?wx_fmt=png&from=appmsg) **图****2****-****3****加密方式分析** **（****安天AVL Code智能体基于澜砥垂直模型分析生成****）** 加密阶段，样本从根目录递归遍历文件系统，跳过 /boot、/proc、/sys、/dev、/etc、/bin、/lib 等系统目录，并重点跳过群晖专属目录 /usr/syno、/var/packages，避免破坏系统与套件。待加密目标按扩展名筛选，覆盖大量数据库（.db、.sqlite、.mdb、.pdb、.ibd、.mdf 等）与虚拟机镜像（.vmdk、.qcow2、.vhdx、.iso、.vdi 等）以及各类文档；同时跳过 .exe、.dll、.sys、.msi 等系统/可执行文件。  ![](https://mmecoa.qpic.cn/sz_mmecoa_png/frAs2k03Ypn9qnWsnggC5eOTv9FDBN9XHpLzrhxGxf0B3gLicL17Y6xD8YEqCAZnWQNWUxlhnniaomOup3ibAlsLZm4m2qwCflZiaM1fGzcuPb4/640?wx_fmt=png&from=appmsg) **图****2****-****4****目标加密扩展名列表** **（****安天AVL Code智能体基于澜砥垂直模型分析生成****）** 对每个目标文件，样本加密文件后，在文件名后追加".L0CK3D"扩展名，并将加密结果写回（实现 文件 → 文件.L0CK3D 的重命名），同时跳过已带该扩展名的文件，避免二次加密。 ![](https://mmecoa.qpic.cn/mmecoa_png/frAs2k03YpkdvJMzD2pJOpIticqMicSEkuPVcLgqpxhNfnicialvLq3F944DwMte9a15TMxeW7Wr2lFWCUgds1NAWN7a7T5pd1MpnibgXBLu4tZ4/640?wx_fmt=png&from=appmsg) **图****2****-****5****文件加密与扩展名追加（****.L0CK3D）** 样本还具备持久化机制：从 /proc/self/exe 读取自身二进制，复制到 /var/lock/init-rsysd.lo、/dev/shm/init-rsysd.lo、/var/tmp/init-rsysd、/tmp/init-rsysd 等路径，意图在设备重启后自启动。 ![](https://mmecoa.qpic.cn/mmecoa_png/frAs2k03Ypmqv0h0wx14IiaO2gO5wibxM0yMGbdibUUHTgSicibVVDWhJuClaoRibXRAdFBO81ibS8rb3eTwAvvMypsByOicGnIuUgVLGoe9ETzickl4/640?wx_fmt=png&from=appmsg)  图**2****-****6****持久化自复****制（****/proc/self/exe → 各 init-rsysd 路径）** **（****安天AVL Code智能体基于澜砥垂直模型分析生成****）** 勒索软件执行时期的整体流程如下所示。 ![](https://mmecoa.qpic.cn/sz_mmecoa_png/frAs2k03YpnyQv2QR0LBbIicibAsY7Hib0MXptdg79XwfM45yqEfvicyDnZrpMsrsbAq1t8ku7HYpIoyMalDlLW1ZFprWqAw7UfDRtOs8icszhGQ/640?wx_fmt=png&from=appmsg)  图**2****-****7****整体执行****流程** **（****安天AVL Code智能体基于澜砥垂直模型分析生成****）** 3. 防护建议 针对该勒索软件，安天建议个人及企业采取如下防护措施： 3.1**个人防护** 1.**强化终端防护**：Linux 主机部署对应杀毒防护软件；安天智甲 Linux 版用户保持勒索软件防御模块开启（默认开启）；群晖 DSM 开启内置安全审计、入侵告警； 2.**及时更新系统与套件**：及时更新 Linux 系统内核、软件包；群晖 DSM 及第三方套件尽快升级官方最新版本，修复漏洞；禁止无防护直接将管理端口暴露公网，远程访问优先使用 VPN； 3.**加强口令强度**：禁用默认账号，杜绝弱口令；密码建议 16 位及以上，大小写字母、数字、特殊符号组合；多台 Linux 主机、NAS 不要复用同一密码；启用 SSH 密钥登录，同时开启两步验证（2FA）； 4.**补丁常态化更新：**开启系统自动安全更新，定期执行包管理安全升级，重要服务器做好更新前测试，及时修复高危漏洞； 5.**关闭高危端口**：通过防火墙（iptables/nftables）严格管控，非必要关闭 / 限制22 、3306等端口；SSH、管理端口禁止全网放开，配置 IP 白名单访问； 6.**管控脚本与命令权限：**Linux 主机最小化权限管控，限制 bash、python 等脚本执行权限；关闭无用的 SSH、TTY、远程执行服务，禁用不需要的用户 shell； 7.**定期隔离数据备份**：重要文件遵循 3-2-1 备份策略；备份存储与 Linux 主机、NAS 网络隔离，不要同网长期挂载，避免备份一并被勒索加密。 3.2**企业防护** 1.**开启日志：**开启关键日志收集功能（安全日志、系统日志、SSH 登录日志、Web 访问日志、服务错误日志、传输日志），开启 DSM 审计日志，为安全事件的追踪溯源提供基础； 2.**设置****IP****白名单规则**：通过 iptables/nftables、主机防火墙或 NAS 防火墙配置访问控制策略，对 SSH、DSM 管理后台等远程服务配置 IP 白名单，阻止规则外 IP 进行暴力破解； 3.**主机加固**：对 Linux 系统、群晖 NAS 进行基线核查、安全加固； 4.**部署入侵检测系统（****IDS****）**：部署流量监控类软件或设备，便于对勒索软件及时发现与追踪溯源。建议部署**安天探海威胁检测系统（PTD）**，该系统以网络流量为检测分析对象，能精准检测出已知海量恶意代码和网络攻击活动，有效发现网络可疑行为、资产和各类未知威胁； 5.**灾备预案**：建立安全灾备预案，确保备份业务系统可以快速启用； 6.**安天服务**：若遭受勒索软件攻击，建议及时断网，并保护现场等待安全工程师对计算机进行排查。安天7\*24小时服务热线：400-840-9234。 **安天智甲终端防御系统（简称“智甲EDR”）是面向办公机、服务器、虚拟化主机等设备的终端安全防护产品，智甲EDR依托安天自主研发的AVL SDK威胁检测引擎和海量威胁情报，通过资产管理、威胁检测与分析、勒索专项防护、主机管控、软件管理、分布式防火墙等多种能力，打造“可管理”、“可感知”、“可防护”、“可响应”的全场景、一体化的终端安全纵深防护体系。** **目前，安天智甲Linux版本可实现对该勒索软件的有效查杀。** ![](https://mmecoa.qpic.cn/sz_mmecoa_png/frAs2k03YpmbVyrKCs5SAAnhibib9PqgicGJOQ2ck2XR5l1KCe4b534uNuwhxyA1cUTSnessgoGHZQ87CicQJddibFURedjnebx1ps2ZexA7nXaQ/640?wx_fmt=png&from=appmsg) **图****3****-****1****安天智甲阻止加密行为** 参考链接 [1] 群晖疑似出现0day导致用户遭受勒索软件攻击 https://mp.weixin.qq.com/s/lmlWfRxM0bTHaiItAfIXrw [2]补丁已发，为何仍有NAS被锁？360 AI专家还原Cerber攻击链 https://bbs.360.cn/thread-16187993-1-1.html [3]【勒索预警】群晖NAS最新版遭勒索病毒攻击，疑似涉及0day漏洞 https://bbs.kanxue.com/thread-293361.htm [4]群晖DSM+Gitlab CE 遭 C3RB3R 勒索软件攻击！救灾直播贴（v2ex） https://www.v2ex.com/t/1252851 [5]【勒索病毒-C3RB3R .L0CK3D】群晖被入侵（Linux.do） <https://linux.do/t/topic/3089422>**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yicx1jVK2eOnMpQiaccCDTrrxNFUNEkjj9HOFJY9d1a1PkIWPTeH4uXSslP7nKTo0qUORjCREJq8BISLcgCepGgw/0?wx_fmt=png)

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