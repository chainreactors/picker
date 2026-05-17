---
title: 今日（2026年5月16日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/Oifip77LM0bJP4nINQKhZA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:45:25.128183
---

# 今日（2026年5月16日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555uSYR4LkicGDoSInTvP4rlFnLMnltR0vh77gHGRhTzRbdoxNPhEkK0XLQjicTEgMvcfmMEtia0y4ibmYcvgpScN60C2quZ4tjksYRc/0?wx_fmt=jpeg)

# 今日（2026年5月16日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026-05-16 | 威胁等级: **High** | 来源: SecurityOnline.info · NVD · thehackernews

一、NGINX ngx\_http\_rewrite\_module 堆缓冲区溢出漏洞 (CVE-2026-42945)

**CVSS 9.2****Critical****NGINX Rift**

**受影响产品：**NGINX Open Source 0.6.27 至 1.30.0、NGINX Plus R32 至 R36 及相关产品（Ingress Controller、App Protect）。几乎所有使用 rewrite/if/set 指令结合未命名 PCRE 捕获（如 $1、$2）和含"?"替换字符串的配置。

**影响：**未授权远程攻击者通过精心构造的 HTTP 请求触发堆缓冲区溢出，可导致 worker 进程崩溃（DoS）或在 ASLR 禁用时实现远程代码执行（RCE）。存在公开 PoC，影响全球约 1/3 网站基础设施。

**热度原因：**NGINX 是最广泛部署的 Web 服务器之一，此漏洞潜伏近 18 年（自 2008 年起），AI 辅助发现 + 公开 PoC 迅速推高关注度。Patch Tuesday 期间相关讨论叠加，互联网暴露实例多，易被大规模利用。

**修复建议：**立即升级到 NGINX 1.30.1（稳定版）或 1.31.0（主线版）。临时缓解：修改配置使用命名捕获（如 named 替代 $1/$2）或移除易触发 rewrite 组合；监控日志中的异常请求；启用 ASLR 并限制暴露。

二、VMware Fusion TOCTOU 本地权限提升漏洞 (CVE-2026-41702)

**本地LPE****高可靠****VMware Fusion**

**受影响产品：**VMware Fusion 25H2 及之前版本（运行于 macOS）。

**影响：**本地非管理员用户通过 SETUID 二进制中的时间-of-check to time-of-use（TOCTOU）竞争条件，可提升权限至 root。无需额外交互，高可靠。

**热度原因：**VMware 虚拟化产品广泛用于开发/测试环境，root 权限提升风险高；近期 Linux/虚拟化权限提升漏洞链讨论多，此漏洞在 5 月中旬披露，安全站点重点推送，吸引 Mac 管理员关注。

**修复建议：**升级到 VMware Fusion 26H1（或最新版本）。Broadcom 推荐立即应用 VMSA-2026-0003 补丁。临时措施：限制本地用户访问 Fusion 主机，监控 SETUID 二进制活动。

三、Microsoft Windows Netlogon 栈缓冲区溢出漏洞 (CVE-2026-41089)

**CVSS 9.8****Critical****Windows Server**

**受影响产品：**Windows Server 2012 及更高版本（域控制器相关组件）。

**影响：**未授权远程攻击者通过低复杂度攻击实现域控制器 SYSTEM 权限（Critical RCE/EoP）。无需凭证或用户交互。

**热度原因：**Patch Tuesday（5月12/13日）披露的 30+ Critical 漏洞之一，Netlogon 是高价值目标（类似历史 ZeroLogon），企业域环境广泛，安全社区和 Patch 分析广泛讨论，热度持续至本周。

**修复建议：**立即应用 Microsoft May 2026 安全更新（KB 等）。优先修补域控制器；监控 Netlogon 流量异常；启用相关缓解措施直至全覆盖。

四、Microsoft Exchange Server OWA Spoofing 漏洞 (CVE-2026-42897)

**已在野利用****CVSS 高****Exchange Server**

**受影响产品：**Exchange Server 2016、2019、Subscription Edition（On-Premises）；Exchange Online 不受影响。

**影响：**攻击者通过恶意邮件诱导用户浏览器交互，可在 OWA 中执行 JavaScript（spoofing/潜在 RCE 链）。已野外利用。

**热度原因：**已确认野外利用 + CISA/Exchange Team 警报，5月15日前后安全站点重点报道，企业邮件系统高危，易被钓鱼结合。

**修复建议：**启用 Exchange Emergency Mitigation Service (EEMS) 或运行 On-Premises Mitigation Tool（注意可能影响部分功能如日历打印）。等待完整补丁并检查日志异常；用户端警惕可疑邮件。

五、其他值得关注的漏洞

**Linux Kernel ptrace 相关本地权限提升**（近期 PoC 发布）：允许非特权用户 root 文件访问，Linux 服务器广泛影响。

**Cisco SD-WAN 认证绕过**（CVE-2026-20182，CVSS 10，已利用）：网络设备管理员接管风险高，建议立即修补。

六、总体修复建议

最高优先（立即处理）：

① NGINX rewrite module RCE（CVE-2026-42945，CVSS 9.2）——立即升级到 NGINX 1.30.1/1.31.0+。

② Exchange OWA Spoofing（CVE-2026-42897，已野外利用）——立即启用 EEMS 或运行缓解工具。

③ Cisco SD-WAN 认证绕过（CVE-2026-20182，CVSS 10）——立即应用厂商补丁；限制网络设备管理接口暴露。

高优先级（48小时内处理）：

① VMware Fusion TOCTOU LPE（CVE-2026-41702）——升级到 Fusion 26H1；监控 SETUID 二进制。

② Windows Netlogon 栈溢出（CVE-2026-41089，CVSS 9.8）——立即应用 MS May 更新；优先修补域控制器。

③ Linux Kernel ptrace LPE——更新内核；限制非特权用户访问。

优先处理互联网暴露的 Web/边缘服务（NGINX）和关键基础设施（Windows/Exchange/VMware）。使用漏洞扫描工具验证，关注 CISA KEV 和厂商公告。信息实时变化，建议查阅官方 MSRC、NGINX/F5、Broadcom 公告获取最新补丁。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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