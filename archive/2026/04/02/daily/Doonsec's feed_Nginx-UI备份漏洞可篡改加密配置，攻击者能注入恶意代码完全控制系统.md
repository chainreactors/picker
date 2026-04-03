---
title: Nginx-UI备份漏洞可篡改加密配置，攻击者能注入恶意代码完全控制系统
url: https://mp.weixin.qq.com/s/7pfSd1RZkB6ZEpchDnCgPg
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:25:31.223622
---

# Nginx-UI备份漏洞可篡改加密配置，攻击者能注入恶意代码完全控制系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3ZT6MaszxHHg7xKeOMgvnMiayKhyp1iak3KGmtkB2V9S90veKvN2qTF2PJxC69qjYCY9xY59zkDKpj3Kicfzq40kMiaicDvbc8Paj0/0?wx_fmt=jpeg)

# Nginx-UI备份漏洞可篡改加密配置，攻击者能注入恶意代码完全控制系统

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1KBBEEv5jYsgV7lEajTntoiazzP9UiaxF4NvtibGcUictY7aUR3NALaLRU9qs6j3fpnrumsoO1mQiaNBdI7iaPHHqaAtynNliaNRsogo/640?wx_fmt=jpeg&from=appmsg)

##

**Part01**

## ****漏洞概述****

Nginx-UI 备份恢复机制中被披露存在一个高危安全漏洞（CVE-2026-33026）。该漏洞允许威胁攻击者在恢复过程中篡改加密备份文件并注入恶意配置。随着公开的 PoC 利用代码发布，未打补丁的系统面临被完全攻陷的即时风险。

**Part02**

## ****加密缺陷利用原理与PoC****

该漏洞的根本原因在于应用程序备份架构中存在严重缺陷的循环信任模型。当 Nginx-UI 生成备份时，会将文件压缩为 ZIP 归档并使用 AES-256-CBC 加密，但系统未能维护可信根信任。AES 密钥和初始化向量（IV）作为备份安全令牌直接提供给客户端，而非在服务端保护加密参数。

更严重的是，包含加密文件 SHA-256 哈希值的完整性元数据文件也使用相同密钥加密。由于攻击者拥有密钥，可轻松绕过所有加密安全控制。此外，恢复过程未执行严格的完整性验证，即使哈希不匹配触发系统警告，恢复操作仍会继续。

安全研究员 'dapickle' 成功演示了如何利用这一架构弱点。公开的 PoC 包含可自动解密和重建 Nginx-UI 备份文件的 Python 脚本。攻击流程包括：

* 生成标准备份并从 HTTP 头提取安全令牌
* 使用解密脚本解压归档并修改内部配置文件app.ini
* 注入恶意命令（如StartCmd = bash）
* 使用重建脚本压缩修改后的文件，计算新的合法哈希值，更新元数据，并使用原始令牌重新加密整个包
* 上传篡改后的备份至 Nginx-UI 恢复接口，系统将盲目接受并执行注入的负载

**Part03**

## ****影响与归因分析****

该漏洞被评为严重级别，在多个影响指标上获得 CVSS 4.0 最高分。成功利用可使攻击者永久篡改应用配置、在 Nginx 路由中植入后门，并在主机上实现任意命令执行。

值得注意的是，该漏洞是 GitHub 公告 GHSA-fhh2-gg7w-gwpq 中记录的前期漏洞的回归。虽然早期补丁解决了备份文件的未授权访问问题，但完全未能解决底层加密设计缺陷，使系统仍面临归档修改的根本性风险。

![系统接受修改后的备份（来源：Github）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0rZGkVseEfdls505RPWkWWG3VqSqJJNoSzfrHD0TycSH5wF4hmzaMMjiaWxaw1SYxrJGLXTz4QooSNxkw0IIxCgpQyibrarvz1k/640?wx_fmt=jpeg&from=appmsg)

安全社区将该漏洞归类为多种弱点组合，包括完整性检查值验证不当（CWE-354）和加密签名验证失败（CWE-347）。该漏洞影响基于 Go 的 Nginx-UI 软件包，特别是 2.3.3 及更早版本。管理员必须立即升级至 2.3.4 修补版本。

除应用最新补丁外，建议开发者实施服务端可信完整性根，使用私钥而非客户端暴露的令牌对备份元数据进行签名。此外，系统应安全配置以避免循环信任模型，并在任何哈希验证失败时严格中止恢复操作。

**参考来源：**

Public PoC Exploit Released for Nginx-UI Backup Restore Vulnerability

https://cybersecuritynews.com/nginx-ui-backup-restore-vulnerability/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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