---
title: 今日（2026年5月17日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/DEp-k51JvZ5EccMCqLSoLw
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:09:23.384368
---

# 今日（2026年5月17日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555vwxx0PWrB1QVyvno4LiaxX25MVk8dtMZbdBHKSEVYHKIOt4dufovJqRGBtMdicYNWDFMFpVDTZLN154JicueKR5yNKgHOBqqsXTc/0?wx_fmt=jpeg)

# 今日（2026年5月17日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026-05-17 | 威胁等级: **High** | 来源: SecurityOnline.info · Qualys · thehackernews

一、Linux Kernel ptrace 退出竞争条件信息泄露漏洞 (CVE-2026-46333)

**本地信息泄露****PoC已公开****Linux Kernel**

**受影响产品：**受影响 Linux 内核版本（主要 2017 年后发行版，包括 CloudLinux、AlmaLinux 等默认配置，使用 OpenSSH ssh-keysign 等 setuid 组件的系统）。上游修复于内核 commit 31e62c2e。

**影响：**本地未授权（unprivileged）用户通过 ptrace 访问检查中的退出窗口竞争条件（race in \_\_ptrace\_may\_access()），可窃取特权进程文件描述符，读取 root-only 文件如 SSH 主机私钥（/etc/ssh/ssh\_host\_\*\_key）和 /etc/shadow。无需直接提权即可获取敏感凭证。PoC 已公开。

**热度原因：**5月14-15日 Qualys 披露并附带公开 PoC，安全社区和 Linux 发行版快速响应；影响广泛服务器/容器环境，易被本地攻击者（含恶意容器逃逸后）利用窃取凭证，CISA/社区高度关注，成为近期 Linux 内核安全焦点。

**修复建议：**立即升级到包含修复的内核版本（7.0.8、6.18.31、6.12.89 等稳定分支）。临时缓解：设置 kernel.yama.ptrace\_scope=2 或更高；限制用户命名空间；监控 ptrace 相关系统调用；避免不必要 setuid 二进制暴露。更新后重启系统。

二、Next.js WebSocket Upgrade SSRF 漏洞 (CVE-2026-44578)

**CVSS 8.6****High****Next.js**

**受影响产品：**Next.js 自托管版本 13.4.13 至 15.5.15 和 16.0.0 至 16.2.4（使用内置 Node.js server）；Vercel 托管版不受影响。

**影响：**未认证攻击者通过精心构造的 WebSocket 升级请求触发 SSRF，可让服务器代理请求到任意内部/外部目标（含云元数据服务、内部 API），导致数据泄露。CVSS 约 8.6（High）。

**热度原因：**5月11-13日前后披露，PoC 快速流传；约 79,000 暴露实例被扫描发现。自托管 Next.js 流行，攻击面广，开发者社区关注度高。

**修复建议：**升级到 15.5.16 或 16.2.5。临时缓解：在反向代理层阻挡 WebSocket 升级请求；避免直接暴露自托管服务器到公网；监控异常内部请求。

三、PraisonAI 认证绕过漏洞 (CVE-2026-44338)

**CVSS 7.3****快速利用****AI Framework**

**受影响产品：**PraisonAI Python 包 2.5.6 至 4.6.33（使用 legacy Flask API server）。

**影响：**默认认证禁用，导致未认证用户可访问 /agents 和 /chat 等受保护端点，触发 AI 工作流执行。CVSS 7.3（High）。

**热度原因：**5月11日前后披露，披露后 4 小时内即被扫描/尝试利用，体现"快速利用"趋势。开源 AI 框架流行，易被攻击者针对。

**修复建议：**立即升级到 4.6.34 或更高。临时缓解：启用认证（设置 AUTH\_ENABLED=True 和 token）；限制 API 服务器网络访问；监控未授权访问日志。

四、总体修复建议

最高优先（立即处理）：

① Linux Kernel ptrace 信息泄露（CVE-2026-46333，PoC 已公开）——立即升级内核；设置 ptrace\_scope 限制；监控异常 ptrace 调用。

② Next.js SSRF（CVE-2026-44578，CVSS 8.6）——升级到 15.5.16/16.2.5；限制 WebSocket 升级请求。

③ PraisonAI 认证绕过（CVE-2026-44338）——立即升级到 4.6.34；启用 API 认证；检查未授权访问日志。

高优先级（48小时内处理）：

① 审计 SSH 主机密钥（/etc/ssh/ssh\_host\_\*\_key）和 /etc/shadow 文件权限，确认内核更新前未被窃取。

② 扫描暴露的自托管 Next.js 实例（约 79,000 个），优先修补面向公网的节点。

优先关注本地/容器环境（Linux 内核）和暴露 Web/AI 服务；启用自动更新、内核补丁与日志监控；使用 EDR/WAF 检测异常；定期扫描暴露面。信息基于最新公开来源，漏洞动态变化，建议查阅 NVD、Qualys、厂商公告或 securityonline.info 获取最新补丁和 IoC。

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