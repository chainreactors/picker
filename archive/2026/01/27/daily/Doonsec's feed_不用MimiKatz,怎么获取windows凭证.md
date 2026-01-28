---
title: 不用MimiKatz,怎么获取windows凭证
url: https://mp.weixin.qq.com/s/eUm61ITAYpsOIlyO5_cXuQ
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:33:19.656206
---

# 不用MimiKatz,怎么获取windows凭证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/biachO2ia6rWDhOL1x4n2PAxyx9wTo3zicHR1dtbRqe2Uc9XdacRfDibqT3esEHca8pHzlqIt7LWFb587NE06icN6XA/0?wx_fmt=jpeg)

# 不用MimiKatz,怎么获取windows凭证

原创

CyberSecGuy
CyberSecGuy

像梦又似花

![]()

在小说阅读器中沉浸阅读

### 不做脚本小子,怎么获取windows凭证

很多时候在实战中,使用像猕猴桃(MimiKatz)的工具进行凭证获取,安全软件很快就会进行警告提示,绕过方法有很多,例如像在源码编译前的做编码处理,编译加壳等,但核心对一些敏感进程进行操作时也同样容易引起安全软件的警告.

那么如果是不用这些工具,我们可以怎么做呢?

下面我们就用Windows系统举例分享,只要有访问权限,我们就一样可以不借助工具来进行获取凭证.

### 直接入主题

# 凭据转储

`凭据转储是攻击者在 Windows 环境中快速提升权限和横向移动的手段之一。一旦他们获得对计算机的访问权限，尤其是在以 SYSTEM 身份或通过令牌模拟获得访问权限的情况下，他们的第一反应就是提取本地用户或域用户的密码哈希值，有时甚至无需使用像 Mimikatz 这样的工具，以免触发杀毒软件的检测。相反，他们会使用 Windows 原生二进制文件来转储敏感的注册表项和内存快照。`

`这种方法的强大之处在于它的隐蔽性。拥有管理员权限的攻击者可以使用 reg save 命令导出 HKLM\SAM、HKLM\SYSTEM 和 HKLM\SECURITY 注册表项。然后，他们可以使用 rundll32 命令触发 LSASS 进程的完整内存转储，该进程存储着明文凭据、Kerberos 票据和缓存的登录信息。这些文件可以在离线状态下被提取和破解，而无需再次访问任何活动内存。`

# 实战示例

`在下面的终端中，红方首先保存了三个敏感的注册表单元：SAM、SYSTEM 和 SECURITY。这些单元包含密码哈希值和密钥，可供后续解析。`

```
Shell: reg save HKLM\SAM sam.savereg save HKLM\SYSTEM system.savereg save HKLM\SECURITY security.save
```

`接下来，找到 lsass.exe 进程 ID，并运行 rundll32 来触发内存转储，静默生成 lsass.dmp 文件。`

`最后，使用 secretsdump(.)py 处理提取的注册表单元文件，从而获取所有本地用户的 NTLM 哈希值。这就是离线凭据提取的原理。`

![](https://mmbiz.qpic.cn/mmbiz_png/biachO2ia6rWDhOL1x4n2PAxyx9wTo3zicHjsj0E8GtOL0TaY0U3e5UopatZu9B3lccZ3GfUGic2NULxnL6PyzRncQ/640?wx_fmt=png&from=appmsg)

如果感兴趣,后续还可以继续写关于这篇文章的后续内容,留言告诉我,你们想学习什么

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/biachO2ia6rWDwdCSxVdTQ1dAqoicGYf8ricD6BuiaEU64urHUGmkzsUDfD8rqWibx2KXE40wesg6s5AInjvy5FjqCWQ/0?wx_fmt=png)

像梦又似花

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/biachO2ia6rWDwdCSxVdTQ1dAqoicGYf8ricD6BuiaEU64urHUGmkzsUDfD8rqWibx2KXE40wesg6s5AInjvy5FjqCWQ/0?wx_fmt=png)

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