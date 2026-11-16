---
title: Check Point Gaia OS 本地提权漏洞，已在野利用，CISA 纳入 KEV 清单
url: https://mp.weixin.qq.com/s/8HombD42eTGhS6LhDghx6w
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:45:07.034695
---

# Check Point Gaia OS 本地提权漏洞，已在野利用，CISA 纳入 KEV 清单

# Check Point Gaia OS 本地提权漏洞，已在野利用，CISA 纳入 KEV 清单

原创

维度攻防
维度攻防

维度攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

CVE-2026-123039，Check Point Gaia OS DynamicCLI 本地权限提升漏洞，该漏洞已经被 CISA 在 11 月 13 日正式加入 KEV 已知被利用漏洞清单，野外攻击事件真实发生，风险等级极高。

---

## 一、漏洞基本信息

✅ CVE 编号：CVE-2026-123039✅ 漏洞名称：Check Point Gaia OS DynamicCLI 本地权限提升漏洞✅ CVSS 3.1：7.8 高分高危✅ 攻击向量：AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H✅ 漏洞类型：CWE-732（关键资源权限分配错误）+ CWE-862（授权缺失）✅ 影响产品：搭载 Gaia OS 的 Check Point 安全网关、安全管理服务器等系列设备✅ 官方公告：Check Point sk1000362✅ 状态：已在野被利用，CISA 要求限期处置

> ⚠️ 重点说明：该漏洞本身是本地提权漏洞，不能直接远程打；但攻击者经常搭配 PHP2Shell 系列漏洞（CVE-2026-109618 / CVE-2026-109619）先拿下 Mobile Access 门户拿到本地账号，再利用本漏洞直接提权到 root，形成完整攻击链。

## 二、漏洞原理

Gaia OS 内部的DynamicCLI守护进程以 root 权限运行，监听本地 socket 文件 /tmp/dynamic\_socket：

1. 这个 socket 文件全局可写；
2. 服务端没有对连接来源做身份校验、鉴权；
3. 任何已经登录到系统的本地低权限用户，都可以向这个 socket 发送指令，让系统以 root 权限执行命令，直接拿到最高权限。

简单一句话：拿到低权限 shell 之后，一键 root 接管防火墙。

防火墙、VPN 网关本身就是网络边界核心设备，一旦被拿下 root 权限，攻击者可以篡改策略、窃取配置、横向渗透内网，甚至部署擦除类恶意程序，破坏力极强。

## 三、真实攻击链复盘（PHP2Shell + CVE-2026-123039）

根据 Check Point 官方研究团队披露的攻击事件：

1. 初始接入：攻击者利用 Mobile Access 门户 PHP 漏洞（PHP2Shell）打入网关，拿到 portal 服务账号的低权限 shell；
2. 权限提升：利用 CVE-2026-123039，通过 DynamicCLI socket 提权至 root；
3. 持久化植入：上传 PHP webshell，部署 TSGA 后门 + TSProxy 代理组件（PhiliKit 变种），实现加密远程控制；
4. 横向移动：在内网扫描资产，通过 SSH 横向到 VMware ESXi 虚拟化主机；
5. 破坏动作：投放 destroy\_v6 擦除器，销毁虚拟机数据，留下标记文件，无勒索，直接破坏。

> 本次攻击分为两波：第一波定向攻击，带有数据销毁行为；第二波大范围全网扫描，属于机会性投毒，不限行业。

## 四、受影响资产自查清单

请运维、安全同学尽快盘点内网资产：

* Check Point Security Gateway
* Check Point Security Management Server
* 多域管理服务器 MDSM
* 所有运行 Gaia OS 的 Check Point 硬件 / 虚拟化网关

👉 核对官方公告 sk1000362，确认版本是否在受影响范围内。

## 五、处置方案（优先级从高到低）

### 🔴 紧急修复（首选）

按照 Check Point 官方 sk1000362 指引，升级固件到已修复版本，打上对应补丁。

### 🟡 临时缓解措施（暂时无法升级时）

1. 收紧 Gaia 系统本地账号权限，清理闲置账号，最小权限原则；
2. 限制 Mobile Access 门户公网暴露，增加 IP 白名单、二次认证；
3. 监控 `/tmp/dynamic_socket` 的访问日志、异常进程、陌生 socket 连接；
4. 审计所有登录日志、命令执行记录，排查异常登录与提权行为。

### 🟢 事后排查（如果设备已经暴露在公网）

重点排查这些痕迹：

* `/opt/CPcvpn-R81.20/tmp/`

  下异常 PHP 会话文件，含`upload_progress_pwn`标记；
* 门户模板目录下 `zz*.tpl`、`challenge_render.tpl` 等异常 webshell；
* `/tmp/CPconfigdaemon`

  、`slot_CPconfigdaemon`、`/lib/libcpfwcommon.so` 恶意文件；
* 存在 `destroy_v6`、`DREAM_ANNEXATION.txt` 擦除标记文件；
* 异常 SSH 连接、内网扫描流量（gogo 扫描器）。

## 六、IOC 指标（可导入 SIEM / 威胁平台）

* 恶意 IP：`130.94.19[.]204`、`130.94.19[.]168`

POC 链接：https://github.com/googlesky/CVE-2026-123039

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/56vojF9ZLWEUrByhdC81sgBwVuGYeBDzVbW08PJxSDcOjcVcl79pVPic05r349tgxyWk0kJY5knOkm3aCpkwxSqBiaUr9t5VzPibybSwUkibAicM/0?wx_fmt=png)

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