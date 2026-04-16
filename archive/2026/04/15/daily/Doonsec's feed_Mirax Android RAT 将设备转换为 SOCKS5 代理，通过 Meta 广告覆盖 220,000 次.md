---
title: Mirax Android RAT 将设备转换为 SOCKS5 代理，通过 Meta 广告覆盖 220,000 次
url: https://mp.weixin.qq.com/s/ii_hcqutNFAyDd0Qhiotsg
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:49:56.315816
---

# Mirax Android RAT 将设备转换为 SOCKS5 代理，通过 Meta 广告覆盖 220,000 次

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADsicAIrh5jx57y7CtP03K6UI276tzCXndibj8FogicySu0ibrLn3aVMLU6ksibxOewhtXiajDhY5EPDfCz68xjtDUbNk159f0YM21XMhg/0?wx_fmt=jpeg)

# Mirax Android RAT 将设备转换为 SOCKS5 代理，通过 Meta 广告覆盖 220,000 次

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs9I2vicgrOCUUmkd158INgvA4ibJUadMKKapd6glgSUtwM5ib49xsUJt8Kzad2UC3DLiaibehHdjt8mQcIu25QAK943Idvep4ibB4vls/640?wx_fmt=jpeg&from=appmsg)

一种名为Mirax的新兴安卓远程访问木马被观察到积极针对西班牙语国家，活动通过Meta上的广告覆盖了Facebook、Instagram、Messenger和Threads上的超过22万个账号。

意大利网络欺诈防范公司Cleafy表示：“Mirax集成了先进的远程访问木马（RAT）功能，使威胁行为者能够实时与受攻击设备全面交互。”

“除了传统的RAT行为外，Mirax还通过将感染设备转变为住宅代理节点，提升了其运营价值。它利用SOCKS5协议支持和Yamux复用技术，建立了持久代理通道，使攻击者能够通过受害者的真实IP地址路由流量。”

Mirax的细节首次曝光于上个月，当时Outpost24的KrakenLabs透露，一名名为“Mirax Bot”的威胁行为者在地下论坛上以2500美元的价格宣传一项私人恶意软件即服务（MaaS）服务，订阅期为三个月。还有一款月价1750美元的轻量版，去除了代理和通过加密器绕过Google Play Protect等功能。

和其他Android恶意软件一样，Mirax支持捕捉击键、窃取照片、收集锁屏细节、执行命令、浏览用户界面以及监控受损设备上的用户活动。它还能动态从命令与控制（C2）服务器获取HTML覆盖层页面，用于合法应用程序进行凭证盗取。

另一方面，SOCKS代理的引入是一个相对较少为人知的特性，使其区别于传统RAT的行为。代理僵尸网络有多重优势，使威胁行为者能够绕过基于地理位置的限制，规避欺诈检测系统，并在匿名性和合法性提升的幌子下进行账户接管或交易欺诈。

研究员Alberto Giust、Alessandro Strino和Federico Valentini表示：“与典型的MaaS产品不同，Mirax通过高度受控且排他性的模式分销，仅限于少数加盟机构。”“访问似乎优先针对在地下社区中享有声誉的俄语参与者，显示出有意维护行动安全和行动效能的努力。”

传播恶意软件的攻击链利用Meta广告推广dropper应用网页，诱骗毫无防备的用户下载。多达六则广告被观察到积极宣传一个免费观看体育和电影直播的流媒体服务。其中五则广告针对西班牙用户。其中一则广告于2026年4月6日开始播出，覆盖了190,987个账户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oPZcPicUADsicyWK32eoB5icLEBbB1VA5spJUIORGBwLanUlOSyVpicibbLAFm8prnYFrQcB8MspUQDWws6GvHGxmPAchUDStcXNzAaPfTCzPUG8/640?wx_fmt=png&from=appmsg)

Dropper应用的网址会进行多项检查，确保它们能被移动设备访问，并防止自动扫描暴露真实颜色。恶意应用的名称如下——

* StreamTV （org.lgvvfj.pluscqpuj 或 org.dawme.secure5ny） - Dropper app

* Reproductor de video （org.yjeiwd.plusdc71 or org.azgaw.managergst1d） - Mirax

该活动的一个显著特点是利用GitHub托管恶意投放APK文件。此外，构建面板还提供在两个加密器——Virbox和Golden Crypt（又称Golden Encryption）之间选择，以增强APK保护。

安装后，投放器会指示用户允许从未知来源安装恶意软件。提取最终有效载荷的过程是一个“复杂的多阶段操作”，旨在规避安全分析和自动化沙箱工具。

恶意软件安装后伪装成视频播放工具，提示受害者启用无障碍服务，从而使其在后台运行，显示假装安装失败的错误信息，并提供虚假覆盖层以掩盖恶意活动。

它还建立了多个双向C2通道用于任务执行和数据外泄——

WebSocket 位于 8443 端口，用于管理远程访问和执行远程命令。

8444端口的WebSocket用于管理远程流媒体和数据外泄。

在8445端口（或自定义端口）上设置WebSocket，用SOCKS5设置住宅代理。

“RAT与代理能力的融合反映了威胁格局的更广泛转变，”Cleafy说。“虽然住宅代理滥用历来与被攻破的物联网设备和智能电视等低价安卓硬件相关，但Mirax通过将此功能嵌入功能齐全的银行木马，标志着新阶段。”

“这种方法不仅提升了每次感染的变现潜力，也扩大了攻击者的作战范围，他们现在可以利用被攻破的设备进行直接的金融欺诈，并作为更广泛网络犯罪活动的基础设施。”

此时，Breakglass Intelligence详细介绍了一款名为ASO RAT的阿拉伯语安卓RAT，该系统通过伪装成PDF阅读器的应用程序和叙利亚政府应用程序分发。

公司表示：“该平台提供完整的设备攻破能力——短信拦截、摄像头访问、GPS追踪、通话记录、文件泄露以及从受害者设备发起DDoS攻击。”“带有基于角色的多用户面板表明它作为RAT即服务或支持多运营商团队。”

目前尚不清楚该行动的具体最终目标，但以叙利亚为主题的应用诱饵（如SyriaDefenseMap和GovLens）表明，该应用可能针对对叙利亚军事或治理事务感兴趣的个人，作为疑似监控行动的一部分。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

HackSee安全生活

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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