---
title: cPanel 0Day认证绕过漏洞遭野外利用，PoC已公开
url: https://mp.weixin.qq.com/s/r8ebtL86TC9uQG7ltZRDhA
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:55:58.436495
---

# cPanel 0Day认证绕过漏洞遭野外利用，PoC已公开

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0kufRY7KRjkAk7iaKARToRlJLY5Iiavs5T8BcyUicZgiciaiay4DqxJ0iahQs3u85CFvd1VMr7a73N2HSB1icnQNO2nfOZ8vEUndPQsSE/0?wx_fmt=jpeg)

# cPanel 0Day认证绕过漏洞遭野外利用，PoC已公开

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3TwdcbF6gVLxmWZKfRKaraapHHHwa44qmYcwOcJD1lWwrpbIKgMRkLLHfI6b5b9YV9fUzrUsa1RmsI9cAEAOH8uBlZezK64sA/640?wx_fmt=png&from=appmsg)

##

全球网络托管行业正经历一场地震：cPanel & WHM 中被证实存在一个关键认证绕过漏洞（CVE-2026-41940），且已遭野外利用。该漏洞允许未认证攻击者完全绕过登录机制，可能获取托管控制面板的 root 权限。

安全团队 watchTowr 的研究人员已公开概念验证（PoC）利用代码，使得紧急修补的紧迫性急剧上升。

##

**Part01**

## ****漏洞技术分析****

该漏洞存在于 cPanel & WHM（含 DNSOnly 部署）的认证层。根据官方公告，它影响 11.40 之后的所有版本。考虑到 cPanel 在全球共享主机市场的主导地位，攻击面极其庞大。

漏洞本质上是 CRLF 注入与会话令牌泄漏的组合利用链，使攻击者无需有效凭证即可完成以下操作：

1. 获取基础会话标识符
2. 通过 HTTP 307 重定向泄漏有效的会话令牌
3. 将原始令牌注入服务端缓存
4. 最终获得 WHM root 权限

研究人员 Sina Kheirkhah 发布的检测工具展示了四步攻击链：

* 生成预认证会话，获取基础标识符
* 发送 CRLF 注入载荷（Basic 认证 + 无操作 cookie），通过 HTTP 307 泄漏有效令牌
* 触发 do\_token\_denied 请求，将原始令牌注入服务端缓存
* 访问 /json-api/version，确认获得 WHM root 权限

PoC 工具 authbypass-RCE.py 针对 2087 端口（WHM），可成功攻击 11.110.0.89 及更早版本。

**Part02**

## ****紧急修补与缓解措施****

cPanel 在观测到野外攻击后加速了补丁发布。最新修补版本包括：

* 11.86.0.41 / 11.110.0.97 / 11.118.0.63 / 11.126.0.54
* 11.130.0.19 / 11.132.0.29 / 11.134.0.20 / 11.136.0.5
* WP Squared 部署需升级至 136.1.7

管理员必须立即执行以下操作：

* **强制更新**：`/scripts/upcp --force`
* **验证版本并重启服务**：使用 `/usr/local/cpanel/cpanel -V` 查看版本，执行 `/scripts/restartsrv_cpsrvd` 重启服务
* **手动更新**：对于禁用自动升级的服务器（风险最高），需手动处理

若无法立即修补，建议采取以下临时措施：

* 通过防火墙封锁 2083、2087、2095、2096 端口
* 通过 WHM API 停止 cpsrvd 和 cpdavd 服务

目前，全球多家托管商已预防性下线 cPanel 控制面板。由于该漏洞可能暴露整个服务器生态系统（包括所有托管域名、邮件账户、数据库和文件系统），且 PoC 公开大幅降低了利用门槛，预计短期内会出现大规模扫描攻击。

**参考来源：**

cPanel 0-Day Authentication Bypass Vulnerability Actively Exploited in the Wild — PoC Released

https://cybersecuritynews.com/cpanel-0-day-authentication-bypass-vulnerability/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

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