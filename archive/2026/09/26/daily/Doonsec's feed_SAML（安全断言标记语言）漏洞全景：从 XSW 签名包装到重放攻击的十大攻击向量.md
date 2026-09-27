---
title: SAML（安全断言标记语言）漏洞全景：从 XSW 签名包装到重放攻击的十大攻击向量
url: https://mp.weixin.qq.com/s/p-ZEyHytwLdorbZGYCxrOg
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:23:06.165392
---

# SAML（安全断言标记语言）漏洞全景：从 XSW 签名包装到重放攻击的十大攻击向量

# SAML（安全断言标记语言）漏洞全景：从 XSW 签名包装到重放攻击的十大攻击向量

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MiaJADeuhdJVWOjT3LSqll9NibrIo72EsG0taepQFc25M0EqKPFpwc0gbesEDQicSCicMNHjojRKXl6w1Lr5uy3EgeSzYw2kvIIHc/640?from=appmsg)
> **导语**：SAML（安全断言标记语言）是企业 SSO（单点登录）的事实标准，但它基于 XML 的复杂协议结构天然藏着攻击面。攻击者只要抓住签名校验、XML 解析、受众绑定这三处松懈，就能从认证旁路一路打到权限提升——本文带你摸清十大 SAML 漏洞的攻击面。

---

## 一、协议背景：为什么 SAML 这么脆

一次完整的 SAML SSO 流程可以压缩成三步：用户在浏览器里访问 SP（Service Provider，服务提供方）→ SP 重定向到 IDP（Identity Provider，身份提供方）登录 → IDP 把签好名的 SAML Response（包含用户身份与权限断言）POST 回 SP。信任的根基是 IDP 用 XML DSig（XML 数字签名）对整个 Response 或其中 Assertion（断言）做的签名。

问题在于 XML 是结构化、可扩展、可嵌套的载体，攻击者可以在不破坏外层签名的情况下，塞入第二份未签名的 Assertion、改 Subject（主体）、换 Recipient（收件人）、丢注释、嵌 XSLT（可扩展样式表转换语言）。任何一个解析环节疏忽，就是一道敞开的后门。

![SAML XSW 攻击示意](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PWE3r3bvTibDxn53JsgLycicz4ylEYu1ic4ZFovk29clVldiatV3KyE5aiahbcs0fheRKUzIeT8eH42mCvTr9WyoWWGZ0f2nptQXf8/640?from=appmsg "SAML XSW 攻击示意")

---

## 二、十大攻击向量详解

### 2.1 签名包装攻击（XSW，Signature Wrapping）

SAML 漏洞里的"头号明星"。攻击者保留 IDP 签名的原始 Assertion（断言）原封不动，但在同一份 Response 里塞入第二份伪造的 Assertion。SP 的解析逻辑校验的是第一份签名的合法性，读取的却是第二份的用户身份。XSW1 到 XSW8 一共八种变种，差别在于克隆签名的位置（顶层 Response 内 / 外层 Object 内 / Extensions 节点里等）。Bypass SAML 2.0 SSO 的经典文章里有完整利用链，配合 Burp 的 SAML Raider 插件可以直接在 Repeater 里改包。

### 2.2 XML 攻击：XXE 与 Billion Laughs

SAML Response 本质就是一段 XML。如果解析器没禁用 DTD（文档类型定义）处理，就会被 XXE（XML 外部实体）打：注入 `<!ENTITY xxe SYSTEM "file:///etc/passwd">`，读取服务器本地文件、甚至触发 SSRF（服务端请求伪造）。换 Billion Laughs 实体递归展开的写法（十层嵌套 ×10 倍展开），几百字节就能耗尽服务器内存完成 DoS（拒绝服务）。

### 2.3 SAML 消息完整性滥用

签名只验证来源合法，不等于内容没被改。攻击者拿到一份合法 Response 后，可以修改其中的属性字段：把 `Role=User` 改成 `Role=Admin`、把 `Group=Staff` 改成 `Group=Domain Admins`，如果服务端只校验签名但不做属性白名单对照，权限提升就完成了。

### 2.4 缺失或无效签名校验

最离谱但真实存在的漏洞：服务端根本没调用 XML DSig 校验函数，只检查了"是不是从 IDP 域名来的"。这种实现等于把门锁换成摆设，攻击者完全可以自建工具伪造一份带任意身份的 Response。HackerOne 报告 #888930 就是这类案例。

### 2.5 重放攻击

SAML Assertion 必须满足两个不变量：Assertion ID 全局唯一，且只能被消费一次。如果 SP 不维护 ID 黑名单或有效期过宽，攻击者用中间人位置或浏览器历史记录里捕获一份 Response，可以反复提交登录任意次，绕过多因素认证。这正是去年某大型身份厂商 CVE 的根因。

### 2.6 CSRF（跨站请求伪造）

SAML 流程中的 SAMLRequest 是 GET 参数明文传递，攻击者构造一个隐藏 form 自动 POST 给目标 SP 的 ACS（断言消费服务）端点，强制受害者的浏览器完成登录流程，最终会话 Cookie 落到攻击者手里。RelayState 参数尤其危险，必须校验来源与不可预测性。

### 2.7 XML 注释处理

部分 XML 库在序列化时会丢弃注释，但签名是基于规范化后的字节计算的。攻击者在已签名内容里塞入带恶意结构的 XML 注释（`<!-- -->`），签名验证通过后，解析器把注释移除、剩余节点重新拼接，结构就跟签名时对不上了。已通过 SSO 认证的攻击者可以用这一招把自己"切换"成另一个用户。

### 2.8 XSLT 注入

SP 如果用 XSLT 把 SAML Response 转换成内部数据格式，又没禁用 `document()` 函数与外部实体，就可以读取任意文件甚至执行系统命令。这是 SAML 漏洞里 RCE（远程代码执行）风险最高的一条。

### 2.9 受众/收件人混淆（Token Recipient Confusion）

`<Recipient>`、`<Audience>`、`<Destination>` 三个字段决定 Response 应该被哪个 SP 消费、给哪个用户用。如果 SP 没校验 `AudienceRestriction`，攻击者可以用 A 服务的合法 Assertion 去登录 B 服务（两个 SP 共用同一个 IDP 时尤其高发）。这种漏洞有时也叫"跨服务令牌复用"。

---

## 三、防御方案

防御 SAML 漏洞要从协议库、签名校验、字段白名单三个层面同时加固：升级到支持 SAML 2.0 严格解析的库（如 OpenSAML 3.x），调用 `verify()` 接口对 Assertion 整体校验；禁用 XML 解析器的 DTD 与外部实体；维护 Assertion ID 一次性消费表；严格校验 `<Audience>` 必须等于本服务实体 ID；对属性字段做白名单与值域检查；RelayState 加不可预测的 CSRF Token。OWASP 的 SAML 安全速查表把这套打法写得很细，建议直接照搬。

---

## 四、总结

SAML 攻击面看似集中在签名，但真正能打到权限提升的，往往是 XML 解析细节、受众绑定、属性校验这些"不起眼"的环节。Red Team（红队）做评估时，先用 SAML Raider 跑一遍 XSW 八种变种，再用 XXE/重放/CSRF 补刀，基本能覆盖 80% 的高危场景；Blue Team（蓝队）则要把签名校验、字段白名单、一次性消费这三件事做扎实，少一个就漏一条。

**原文出处**：https://github.com/harsh-bothra/learn365/blob/master/days/day3.md

**实战参考**：

* Bypass SAML 2.0 SSO（Aura）：https://research.aurainfosec.io/bypassing-saml20-SSO/
* SAML Raider：https://github.com/CompassSecurity/SAML Raider
* OWASP SAML CheatSheet：https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/SAML\_Security\_Cheat\_Sheet.md
* 漏洞案例：https://hackerone.com/reports/888930

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OWwskuGTMborGnTk7aD4e0T8iaNYtibt8iazoacocQOicNLrzic8kcZKxYaMIvWT27hnWneupJslQjoNYz2x8N4k6be1rKZoQvtr98/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N9p4dMXWJvzXQmmiaSiaFdcRuUibTBSzxgCCfzD1OxeOcoQUibMkymaBKp8wqyLk7waicy2sC6DiaBIS0OO1cZWCl6icCYibEOAkjWVt4/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NsmBwrboHujSpzrUZayaV5YlveOmhmgAARiaZs4cJ2N67UiaCWx4V9qFj3puPG09YQ3ZwLBXH1SrYWXc3fGDy5UrnJ1IILHRYTc/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6O2odkYic22NJnjr6sLakp1qvRn5LrgBYHuKibyAOVSBoqO1icBsBqx22wq5ax40uTWyQqCFAaECsiccPd6Uy2ydkDcyQZTP2wlOlE/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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