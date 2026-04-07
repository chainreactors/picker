---
title: OpenSSH 10.3 发布，修复 Shell 注入及其他安全漏洞
url: https://mp.weixin.qq.com/s/hhvbv9yEs72Xk6ZgZojkHw
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:02.857149
---

# OpenSSH 10.3 发布，修复 Shell 注入及其他安全漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnuKzfU4icSKvsC1HR8nxU2w4qUcoJfe4N2IECUAfrrqYulMIUJm0Fc2EFDk94t1zJ5SUwxwKN75FrBkPXv29oNfYTUibsRZ98l30/0?wx_fmt=jpeg)

# OpenSSH 10.3 发布，修复 Shell 注入及其他安全漏洞

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnsl9u6WLdJs0icBImFc3TLWjCWb0VLnlVMic4l8iaLiaQ8fFFia7xibTNXhXZK6zJU3fleadMqouA99YXTo7IBtdTlyKfqL1PORkwpM8/640?wx_fmt=png&from=appmsg)

OpenSSH 项目发布了 10.3 版本及其可移植版本 10.3p1。在三月下旬短暂的测试阶段后，这一重大更新解决了多个重要的安全漏洞。

最重要的修复措施防止了一个危险的 shell 注入漏洞，这使得本次更新成为全球系统管理员必不可少的升级。

OpenSSH 仍然是 SSH 协议 2.0 的领先实现，提供安全的加密通信。

本次发布的首要重点是修复 SSH 客户端中发现的一个 shell 注入漏洞。

此前，通过命令行传递的恶意用户名在配置文件中使用特定令牌（如"%u"）时，可能执行任意 shell 命令。

OpenSSH 10.3 通过为 shell 字符添加更严格的验证规则来修复此问题。然而，开发人员仍然强烈建议不要将 SSH 命令行直接暴露给不可信的输入。

其他值得注意的安全修复包括：

**证书认证漏洞**：修复了服务器(sshd)中的一个缺陷，该缺陷允许包含逗号分隔名称的证书绕过 authorized\_keys 文件中的某些限制。

**传统 SCP 权限问题**：解决了传统 scp 中的一个长期存在的漏洞，即以 root 身份下载文件时未能清除危险的 setuid/setgid 权限位。

**ECDSA 密钥强制执行**：解决了一个问题，即限制 ECDSA 密钥使用特定算法时，意外地允许接受任何其他 ECDSA 算法。

**主要功能和改进**

除了安全补丁外，OpenSSH 10.3 还引入了多项有助于管理员管理连接和防止滥用的实用功能：

**连接洞察**：新增命令（如 ~I 和 ssh -O conninfo）允许用户快速查看其活跃 SSH 连接和打开通道的详细信息。

**更强的反垃圾邮件惩罚机制**：服务器现在包含"invaluser"惩罚机制，可自动减缓尝试使用虚假用户名登录的自动化机器人和攻击者。

**多重吊销文件**：管理员现在可以在 RevokedHostKeys 和 RevokedKeys 配置中列出多个文件，以更好地管理被泄露的密钥。

**标准化代理转发**：增加了对 SSH 代理转发官方 IANA 分配名称的支持，提高了整体兼容性。

**亚秒级惩罚**：PerSourcePenalties 功能现在支持小数时间，允许防御性阻断持续时间少于一秒。

OpenSSH 10.3 正式放弃了对不支持加密重新密钥的旧版不安全软件实现的兼容性。

ProxyJump 命令行选项现在严格验证主机名和用户名，以阻止进一步的 shell 注入风险。

证书中为空的"principals"部分不再充当通配符；它现在严格匹配任何内容。

建议各组织尽快将其服务器和客户端升级到 OpenSSH 10.3，以保护其基础设施免受这些新披露漏洞的威胁。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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