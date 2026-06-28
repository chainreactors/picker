---
title: 消息模板注入漏洞
url: https://mp.weixin.qq.com/s/3IxDbhDRWVzFC-kE4ogi5Q
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:12:27.738966
---

# 消息模板注入漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8tDOXFoCoQicWs7srh8Ad3SpJBLbcictzlydMuPhdRXCxvPhISicq5PCYQIaRc3ukggMm3zFJD5dd8oicIh97bnjlwW7xpk2ZsWmkjBiczVyn5x4/0?wx_fmt=jpeg)

# 消息模板注入漏洞

原创

游山玩水
游山玩水

山水SRC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 免责声明

**本公众号分享的所有渗透测试技术文章仅面向合法授权的安全测试、学习交流与研究用途。读者必须确保自身行为符合《网络安全法》等相关法律法规，严禁将其用于任何未授权攻击等非法活动。因不当使用或传播相关内容所引发的任何法律责任与风险，由行为人自行承担，本公众号（或本人）概不负责**

## 测试流程

#### 测试前提

1. **功能入口**：存在一个可以向用户绑定邮箱或手机发送通知的功能点（常见于“找回密码”、“安全提醒”、“订单确认”、“邀请好友”等）。
2. **可控参数**：发送请求包中存在可控参数（如 `url`、`callback`、`return_url`或特定的追踪参数如 `cid`），且该参数的值会被后端直接拼接到发送给用户的 URL 链接中。
3. **无过滤/编码**：服务端未对该参数进行合法性校验（如域名白名单），也未对特殊字符（如 `?`、`&`、`#`）进行 URL 编码处理。

#### 测试流程

**步骤一：抓取正常请求**

1. 触发一个会发送邮件或短信的操作（例如：点击“找回密码”）。
2. 使用 Burp Suite 拦截该请求。
3. 观察请求包（Request）结构。假设正常的请求包如下：

   ```
   ```
   ```
   POST /api/send_notice HTTP/1.1
   Host: www.xxx.com
   Content-Type: application/json

   {
   "user_id": "12345",
   "type": "reset_pwd",
   "url": "https://www.xxx.com/reset",
   "cid": "ABC123XYZ"
   }
   ```
   ```
   ```

**步骤二：分析接收内容**

1. 查看收到的邮件或短信。
2. 内容通常包含一个链接，格式为：

* `https://www.xxx.com/reset?cid=ABC123XYZ`
* 或者：`https://www.xxx.com?redirect=...&cid=ABC123XYZ`

**步骤三：构造恶意 Payload（修改参数）**

回到 Burp Suite 的拦截请求，修改 `cid`参数的值，插入特殊字符以截断原逻辑或添加新的参数。

* **Payload 1：添加恶意跳转参数（Open Redirect）**

+ **原始值**：`"cid": "ABC123XYZ"`
+ **修改后**：`"cid": "ABC123XYZ&redirect=https://evil.com"`
+ **结果链接**：`https://www.xxx.com/reset?cid=ABC123XYZ&redirect=https://evil.com`
+ *解析*：如果用户点击，虽然看起来前缀是官方域名，但实际上参数 `redirect`会指引用户跳转到攻击者网站。

* **Payload 2：修改为钓鱼内容**

**步骤四：验证结果**

1. 放行修改后的请求。
2. 检查邮箱或手机短信。
3. 确认收到的链接中，`cid`参数已经被成功修改，且包含了攻击者注入的内容。
4. 点击链接，确认是否能跳转到恶意站点（如 `evil.com`）。

危害

钓鱼攻击（主要危害）

**攻击者可以利用此漏洞发送看似完全合法的官方邮件/短信。用户看到的是**`www.xxx.com`域名下的链接，极易信任并点击，从而被诱导至伪造的登录页，导致账号密码泄露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8tDOXFoCoQicdeGgeXTTZHEdPWoVpQfOfpy8YbibUY3QTPVXiabHr3ROS4mgz52KXtZourMcVTFmIM8UZIe1lbfLCyVV9xFOFmePySIq4lqpU8/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BXWf54pHyFmsnAoomcxMvpxr0NRiaiaibRWIjfusaRLibIUMSwsQUNy2k2rtjeky3xPBmDLia6x4hktJdhNhUic8aFpQ/0?wx_fmt=png)

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