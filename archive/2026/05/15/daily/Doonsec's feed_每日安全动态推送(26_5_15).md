---
title: 每日安全动态推送(26/5/15)
url: https://mp.weixin.qq.com/s/MM0jh4O_xJfaZ6FiDoPDCw
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:13:33.583097
---

# 每日安全动态推送(26/5/15)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/5/15)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

•  CVE-2025-68670：xrdp 中通过 UTF-8 缓冲区溢出实现的认证前 RCE 漏洞
<https://securelist.com/cve-2025-68670/119742/>

本文深入剖析了 Kaspersky 在 xrdp 远程桌面服务器中发现的 CVE-2025-68670 远程代码执行漏洞，详细揭示了攻击者如何利用 UTF-16 到 UTF-8 的编码转换差异，通过精心构造的域名名称绕过认证并触发栈缓冲区溢出。文章不仅提供了清晰的漏洞利用原理与概念验证（PoC），还强调了负责任的披露流程与开源社区协作对提升整体网络安全生态的关键作用。

•  逆向工程 Discord Electron：分析 ASAR 提取、沙箱漏洞与 RCE 风险
<https://blog.securelayer7.net/electron-app-security-risks-part-2/>

本文突破了理论框架，直接逆向分析 Discord 和 Element 等亿级用户应用的真实二进制文件，揭示了生产环境中 Electron 应用从 XSS 到 RCE 的具体攻击链。其最大亮点在于通过提取 ASAR 包并逐行审计源码，直观展示了 `sandbox: false` 等关键配置缺失如何导致系统级漏洞，为开发者提供了极具实战价值的防御参考。

•  全面防御：应对 AI 驱动攻击与 Mythos 威胁态势的防御指南
<https://www.cisco.com/c/m/en_us/about/doing_business/trust-center/cisco-defending-against-ai-attacks-guidance.html>

本文独家披露了 Anthropic 尚未公开的 AI 模型 Mythos 所展现出的突破性‘情境感知’与代理式认知能力，揭示了其如何从根本上降低网络攻击的技术门槛。文章基于 Cisco 的内部测试，前瞻性地提出了应对 AI 驱动威胁的新型防御框架与‘安全默认’代码生成策略，是当今网络安全领域必读的里程碑式技术指南。

•  微软 MDASH 多智能体系统发现 16 个关键 Windows 漏洞
<https://sectoday.tencent.com/event/nhZJKp4B5M25NX6PFNYx>

微软推出了名为 MDASH（多模型智能体扫描框架）的新一代自动化安全系统，该系统通过编排超过 100 个专用 AI 智能体，在审计、辩论和概念验证的流水线中协同工作。MDASH 在 CyberGym 基准测试中以 88.45% 的分数超越了 Anthropic 的 Mythos 和 OpenAI 的 GPT-5.5，成功在 Windows 网络栈和认证栈中识别出 16 个新的关键漏洞，其中包括两个远程代码执行（RCE）漏洞。这一成果标志着 AI 漏洞发现技术从研究阶段正式跨越到企业级生产防御，展示了多智能体架构在加速补丁发布和应对自动化攻击方面的战略优势，同时也揭示了 AI 作为进攻性工具的双刃剑风险。

•  YellowKey 与 GreenPlasma：Windows BitLocker 零日漏洞及 PoC 公开
<https://sectoday.tencent.com/event/phbbKZ4B5M25NX6PSIdt>

针对 Windows 11 及 Server 2022/2025 系统，两款名为 YellowKey 与 GreenPlasma 的严重未修复零日漏洞被披露。YellowKey 利用 WinRE 组件及特定 FsTx 目录实现了对 BitLocker 全磁盘加密的完全绕过，而 GreenPlasma 则通过 CTFMON 服务中的任意内存段创建缺陷进行本地权限提升至 SYSTEM 级别。由于一名对微软披露流程不满的研究者出于报复心理，已将这两个漏洞的 PoC 利用代码公开，导致数百万设备面临即时威胁。在官方补丁发布前，安全专家建议立即实施自定义 PIN 码及 BIOS 密码等缓解措施以防御潜在攻击。

•  Kukurigu：利用 xfrm-ESP 与 RxRPC 漏洞链实现稳定的 Linux Kernel 页面缓存投毒提权
<https://cxsecurity.com/issue/WLB-2026050007>

本文揭示了代号为'Kukurigu'的严重漏洞链，通过巧妙组合xfrm-ESP与RxRPC协议缺陷，实现了无竞态条件且成功率接近100%的Linux内核本地提权。该漏洞影响跨度长达9年且覆盖主流发行版，其稳定的内存驻留页缓存污染技术为内核安全研究树立了新的警示标杆。

•  NGINX 重写模块 18 年历史堆溢出漏洞 (NGINX Rift)
<https://sectoday.tencent.com/event/lRYSKp4B5M25NX6PHa_4>

安全研究人员披露了名为 NGINX Rift (CVE-2026-42945) 的严重漏洞，该漏洞存在于 NGINX 的 ngx\_http\_rewrite\_module 中，其根源可追溯至 2008 年，影响长达 18 年。该漏洞源于脚本引擎双遍处理机制中的状态不一致，当特定条件下组合使用 'rewrite' 和 'set' 指令并包含问号时，URI 转义扩展会导致堆缓冲区溢出。未认证的远程攻击者可通过发送构造的 HTTP 请求触发此漏洞，导致 Worker 进程崩溃（拒绝服务）或在禁用 ASLR 的环境下实现远程代码执行 (RCE)。该漏洞影响 NGINX 0.6.27 至 1.30.0 版本以及多款 F5 产品，厂商已紧急发布补丁修复此问题及相关的三个内存破坏漏洞。

•  InstallFix 行动：利用 Claude AI 信任通过虚假安装程序与多阶段恶意软件攻击
<https://cybersecuritynews.com/hackers-using-fake-claude-ai-installer-pages/>

本文揭示了攻击者如何利用付费搜索广告和伪造的 Claude AI 安装指南，通过社会工程学诱骗用户执行恶意命令，其多阶段攻击链巧妙利用合法系统工具（如 mshta.exe）和动态 C2 域名规避检测。这一针对 AI 工具信任机制的新型威胁，为防御者提供了关键的 IoC 和针对开发者及普通用户的即时防护策略。

•  Android adbd 零点击 RCE 漏洞 (CVE-2026-0073)
<https://sectoday.tencent.com/event/zPq6AZ4B5M25NX6P0C4Y>

Google 在 2026 年 5 月安全公告中披露了 Android Debug Bridge (adbd) 守护进程中的严重零点击远程代码执行漏洞 (CVE-2026-0073)。该漏洞源于 adbd\_tls\_verify\_cert 函数中的逻辑缺陷，导致无线 ADB 的相互 TLS 认证被绕过。攻击者无需用户交互，仅需通过同一局域网或近场连接即可在 Android 14 至 16 设备上获取远程 Shell 访问权限并绕过沙箱限制。该漏洞影响广泛，Google 已发布安全补丁，但部分设备厂商的更新延迟仍使大量用户面临风险。

•  ScarCruft 供应链攻击：Windows 与 Android 后门瞄准游戏平台
<https://cybersecuritynews.com/new-scarcruft-supply-chain-attack-hits-gaming-platform/>

本文首次深度剖析了朝鲜国家支持黑客组织ScarCruft利用游戏供应链漏洞，针对中国延边地区朝鲜族群体实施的精准间谍活动。文章独家披露了新型Android版BirdCall后门的技术细节，揭示了攻击者如何通过伪装成合法游戏更新来窃取难民及脱北者的敏感数据，为当前地缘政治背景下的供应链安全研究提供了关键情报。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/mmbiz_jpg/HhcytTU2b7ch9C2daHZK4EAbBIMSVrNcficbCgHGkDicq3qkaAPXBkuVY3IuIku5PiabwZGTJEq5CUDWyicIRXPttE6m5a3Zd5pHZzmRm3BrcV4/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

腾讯玄武实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

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