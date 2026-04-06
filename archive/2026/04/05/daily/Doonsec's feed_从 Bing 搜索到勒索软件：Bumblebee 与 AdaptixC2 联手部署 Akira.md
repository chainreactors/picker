---
title: 从 Bing 搜索到勒索软件：Bumblebee 与 AdaptixC2 联手部署 Akira
url: https://mp.weixin.qq.com/s/EEF1t1I2do6JqGo7jDglgw
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:40:32.514115
---

# 从 Bing 搜索到勒索软件：Bumblebee 与 AdaptixC2 联手部署 Akira

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/PO9bjOzlHYCg7YocQPWm6I7giakV0WV2l2QxNV9PSLZSLJJKn37LuCdfRp2Dn8vKTjquc5KK3RT67HibqzV9OIoJx8EUKicNCyvDJwOnAq2ibbE/0?wx_fmt=jpeg)

# 从 Bing 搜索到勒索软件：Bumblebee 与 AdaptixC2 联手部署 Akira

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器中沉浸阅读

一次看似普通的 Bing 搜索，如何在 44 小时内演变为全面的勒索软件攻击？The DFIR Report 最新披露了一起真实入侵案例：攻击者通过 Bing SEO 投毒手段，将用户引导至伪造的 ManageEngine 下载站，植入 Bumblebee 恶意软件，最终部署 Akira 勒索软件，导致整个企业网络瘫痪。

────────────────

一、攻击概述：从搜索引擎到勒索软件

2025 年 7 月，威胁行为者发起了一场针对 IT 管理工具的 **Bing SEO 投毒攻击**。当受害者在 Bing 中搜索"ManageEngine OpManager"时，搜索引擎将恶意网站 **opmanager[.]pro** 推荐至前列。

用户下载并执行了伪装的 MSI 安装包 **ManageEngine-OpManager.msi**。该安装包在安装正版软件的同时，通过 **consent.exe** 加载了 Bumblebee 恶意软件 **msimg32.dll**——这是一个典型的 DLL 侧加载攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYBHvbs9kIhfmKkLJHkg8ZCFQX75dq4hzXgDUEvFibN4FialLfOJ7kLkFUaJXADxhHliaqIp5AvBEokwj6y0D7IykqibsOksDJxUaG8/640?wx_fmt=png)

▲ Bing 搜索结果中被投毒的恶意网站

由于目标是 IT 管理工具，执行安装的用户往往是 **Active Directory 中拥有高权限的 IT 管理员账户**，这为攻击者后续的横向移动提供了天然便利。

────────────────

二、攻击链深度分析

阶段 1：初始访问 — Bumblebee 恶意软件

Bumblebee 是自 2021 年底以来活跃的初始访问工具，2023 年首次被发现利用 SEO 投毒进行传播。本次攻击中，Bumblebee 通过 DGA（域名生成算法）域名与以下 C2 服务器建立通信：

109.205.195[.]211:443
188.40.187[.]145:443

阶段 2：持久化 — AdaptixC2 信标

初始执行约 **5 小时后**，Bumblebee 部署了 **AdaptixC2** 信标（AdgNsy.exe），建立了新的 C2 通道至 **172.96.137[.]160:443**。AdaptixC2 是一个开源 C2 框架，攻击者利用其进行后续指令控制。

攻击者随后使用 Windows 内置工具进行了内部侦察：

systeminfo
nltest /dclist:
whoami /groups
net group domain admins /dom

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYBwibRD3he1ulRlzGkpRFdskvUgEfLicoHwXprlwujKOMLPQJ6BpVMJSpficA5Urgf3RERXdicsFdzcQTmQvuKhAJk2XZaMuibiaf6nA/640?wx_fmt=png)

▲ 攻击流程示意图

阶段 3：权限提升 — 域控接管

攻击者创建了两个新域账户：

net user backup\_DA P@ssw0rd1234 /add /dom
net user backup\_EA P@ssw0rd1234 /add /dom
net group "enterprise admins" backup\_EA /add /dom

随后使用高权限账户 **backup\_EA** 通过 RDP 连接域控，使用 **wbadmin.exe** 转储 NTDS.dit 文件——这是 Active Directory 的核心凭据存储：

wbadmin.exe start backup -backuptarget:\\127.0.0.1\C$\ProgramData\ -include":C:\windows\NTDS\ntds.dit,C:\windows\system32\config\SYSTEM,C:\windows\system32\config\SECURITY" -quiet

⚠ 这种利用 wbadmin 进行 NTDS.dit 转储的技巧相对罕见，能绕过传统的 LSASS 监控检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PO9bjOzlHYCwqf0zCk6qTvQwEQKw9d76oLnA5TDg5KDpiaaxohvGVJe9HnzY9ZiaGx4gIerVe2vdeHpz2T0uLSfsamEh0p140pwzB84zJCoYY/640?wx_fmt=png)

▲ 恶意 MSI 安装包执行流程

阶段 4：数据窃取

攻击者在文件服务器上安装 **FileZilla**，通过 SFTP 将数据外传至 **185.174.100[.]203**。同时，攻击者还尝试从 **Veeam 备份服务器**的 PostgreSQL 数据库中提取凭据：

psql.exe -U postgres --csv -d VeeamBackup -w -c "SELECT user\_name,password,description,change\_time\_utc FROM credentials"

阶段 5：勒索软件部署 — Akira

攻击者使用 **rundll32.exe + comsvcs.dll** 对多个工作站进行 LSASS 内存转储，随后部署 **Akira 勒索软件**（locker.exe），加密本地驱动器和远程网络共享。

⚠ 攻击者在首次勒索部署两天后，通过 RustDesk 返回，对子域控制器发起第二轮攻击并再次部署 Akira。从初始访问到首次勒索软件部署仅 44 小时，瑞士电信 CSIRT 观察到的案例甚至仅 9 小时。

────────────────

三、检测规则与威胁猎杀建议

以下检测要点来自 The DFIR Report 的 DEATH（Detection Engineering And Threat Hunting）框架：

**初始访问检测：**

监控来自用户目录的 MSI 安装及其异常子进程（consent.exe、msimg32.dll 加载）。关注名称可疑的 MSI 包如 ManageEngine-OpManager.msi。

**凭据访问检测：**

监控 LSASS 内存转储（rundll32.exe comsvcs.dll）、PostgreSQL 凭据查询、wbadmin 用于 NTDS.dit 转储的异常使用。

**C2 通信检测：**

监控 Bumblebee DGA 域名模式（8-14 位随机字符 .org），以及 SSH 反向隧道到外部 IP 的行为。

**横向移动检测：**

监控新创建账户的 RDP 登录（Type 10），以及初始主机到域控之间的异常认证模式。

────────────────

四、IoC 情报

|  |  |
| --- | --- |
| 类型 | 值 |
| 恶意域名 | opmanager[.]pro |
| 恶意域名 | angryipscanner.org |
| 恶意域名 | axiscamerastation.org |
| DGA 域名 | ev2sirbd269o5j.org |
| DGA 域名 | 2rxyt9urhq0bgj.org |
| Bumblebee C2 | 109.205.195[.]211 |
| Bumblebee C2 | 188.40.187[.]145 |
| AdaptixC2 C2 | 172.96.137[.]160 |
| SSH 隧道 | 193.242.184[.]150 |
| SFTP 外传 | 185.174.100[.]203 |

文件哈希

|  |  |
| --- | --- |
| 文件 | SHA256 |
| ManageEngine-OpManager.msi | 186b26df63df3b7334043b47659cba4185c948629d857d47452cc1936f0aa5da |
| msimg32.dll (Bumblebee) | a6df0b49a5ef9ffd6513bfe061fb60f6d2941a440038e2de8a7aeb1914945331 |
| locker.exe (Akira) | de730d969854c3697fd0e0803826b4222f3a14efe47e4c60ed749fff6edce19d |

────────────────

五、防御建议

1. **限制高权限账户日常操作** — IT 管理员不应使用域管账户进行日常网页浏览和软件下载

2. **监控异常域账户创建** — 特别关注 backup\_\* 命名模式的账户及后续的特权组添加

3. **加强 CI/CD 和备份系统安全** — Veeam 备份数据库应使用独立凭据，定期轮换

4. **部署 DNS 安全监控** — 阻断 DGA 域名解析请求

5. **远程访问工具白名单** — RustDesk 等远程工具应纳入监控范围

────────────────

**来源：**The DFIR Report
**原文链接：**From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira
**发布日期：**2025-11-04

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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