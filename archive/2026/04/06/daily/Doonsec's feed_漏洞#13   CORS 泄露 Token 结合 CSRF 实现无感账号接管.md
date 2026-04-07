---
title: 漏洞#13   CORS 泄露 Token 结合 CSRF 实现无感账号接管
url: https://mp.weixin.qq.com/s/VPTSmhTbEABYInFZ89HCVg
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:28:22.049998
---

# 漏洞#13   CORS 泄露 Token 结合 CSRF 实现无感账号接管

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jow1el0IZibzKTyuON7uePiaq0JaSqDe2GEZAGuBvWPAwmUXEtleu5KwKica2FxmXZl1riaTb3EuTPeT1ewgpJ2PgXyicQOpXAVGf2MU35d6FaLU/0?wx_fmt=jpeg)

# 漏洞#13 CORS 泄露 Token 结合 CSRF 实现无感账号接管

原创

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

在测试一个私有漏洞赏金计划时，我遇到了一个

### 漏洞场景

这个漏洞发生在两个本该互相隔离的业务场景的交叉地带：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibxjVuSObgwGGvhibX2srHdicKP3LHwWz545eXqje5oFCxxwPibNnzHnuE3vxA4tNpOMyICIG3x8cyIqbX16sRc2CQ5DBD8AvlTLN8/640?wx_fmt=png&from=appmsg)

一个是相对边缘的**密码重置页面**（`http://www.target.com/auth/forgotpassword`）。

另一个则是极其核心的**个人资料修改页面**（`https://www.target.com/site/profile`），在这里可以直接修改用户的姓名、联系方式以及最关键的绑定邮箱。

### 漏洞点功能流程

在正常的业务逻辑里，这两个接口是各司其职的：

1. **修改个人资料**：用户登录后，进入 `https://www.target.com/site/profile`。系统会渲染出一个表单，表单里藏着一个由后端生成的、当前页面专属的防伪造 CSRF Token。用户填好新邮箱点提交，浏览器带上这个 Token 发起 POST 请求，后端校验 Token 没错，再把邮箱改掉。
2. **密码重置**：用户访问 `http://www.target.com/auth/forgotpassword`，页面同样会生成一个 CSRF Token 用于防止恶意请求。

在没有恶意攻击时，每次提交操作都会严格校验对应页面生成的 Token，防止跨站请求伪造。

### 发现过程

起初，常规的子域名枚举和 CORS 自动化扫描探测到，目标站点的密码重置接口 `http://www.target.com/auth/forgotpassword` 存在严重的 CORS 配置错误。抓包一看，响应头里赫然写着：

```
access-control-allow-credentials: true
Access-Control-Allow-Origin: https://evil.com
```

这意味着任何第三方网站都可以带上受害者的凭证（比如 Cookie）去读取这个页面的内容。写个简单的 XHR 脚本去拉取这个页面，发现响应内容里直接把这个页面的 CSRF Token 给暴露出来了。

但在实战中，拿着这种毫无破坏力的 Token 直接去提个 CORS 泄露的漏洞，大概率会被官方以“无实际安全影响”为由直接关掉。毕竟，光拿到一个密码重置页面的 Token 能干嘛呢？

遇到这种情况，思路必须转换：**既然拿到了合法的令牌，那这个令牌能不能在别的地方用？**

目光转向了核心的更新个人信息端点 `https://www.target.com/site/profile`。这个端点本身没有 CORS 漏洞，防守严密，想要修改里面的 `email` 等敏感字段，必须得有合法的 CSRF Token。

这时候，一个假设出现了：**系统的 CSRF Token 校验机制是不是全局通用的？**

测试随即展开：

1. 准备好受害者的邮箱 `victim00@gmail.com` 和准备替换的攻击者邮箱 `attacker00@gmail.com`。
2. 构造一个恶意的 HTML 页面，利用第一步发现的 CORS 漏洞，偷偷拉取受害者在密码重置页面的 CSRF Token。
3. 利用 Burp Suite 拦截正常修改个人信息的请求，右键利用 Engagement tools 直接生成一个 CSRF PoC 表单。
4. 核心操作来了：把表单里的 `email` 字段换成攻击者的邮箱 `attacker00@gmail.com`，并且把表单里用于防御的隐藏字段 `_csrf-backend` 的值，直接替换成刚才通过跨域偷来的、属于密码重置页面的 Token。
5. 当受害者在登录状态下触发这个 CSRF 请求后，奇迹发生了——后端没有拦截。受害者的个人资料被瞬间覆盖，绑定邮箱变成了攻击者的邮箱。到这里，账号已经被彻底接管。

### 漏洞原理

第一，**CORS 策略配置极其拉胯**。密码重置接口允许任意源（`Access-Control-Allow-Origin: https://evil.com`）且允许携带凭证（`access-control-allow-credentials: true`）进行跨域资源共享，导致防御 CSRF 的底层令牌直接裸奔，被攻击者的脚本轻松窃取。

第二，**最致命的 Token 作用域校验缺失**。后端在校验 CSRF Token 时，仅仅验证了“这个 Token 是否有效且属于当前用户”，却没有验证“这个 Token 是不是为当前业务接口生成的”。这就导致了令牌的越权使用——哪怕是从密码重置页面生成的局部 Token，也能畅通无阻地通过修改个人资料接口的校验。这种全局通用的 Token 机制，让原本无害的局部泄露，变成了可以直接打穿整个账户体系的通用钥匙。

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[一种利用 HTTP 重定向循环的新型 SSRF 技术](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484872&idx=1&sn=085b9ed569eefc9a96122fd164da9707&scene=21#wechat_redirect)

[【译】入侵谷歌支持系统：泄露数百万条客户记录（赏金 1.4 万美元）](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485083&idx=1&sn=adec99a8e6b0bfee5ab45ba8cb854805&scene=21#wechat_redirect)

[预接管账号：结合 OTP 校验分离与空格绕过注册内部管理员邮箱](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485067&idx=1&sn=766b936ad8c4d5913df74761d4f9e791&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

漏洞集萃

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

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