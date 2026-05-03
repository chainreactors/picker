---
title: [更新]单文件LNK绕过，但有限制
url: https://mp.weixin.qq.com/s/XD23hhJPxWnGariQfXiafQ
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:25:14.380224
---

# [更新]单文件LNK绕过，但有限制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibXL9MCj2GqMddVWQXRKt2RiblYEQaKjy0Vqo3HzlVh8nzFeicUETPR42J52yqkYqaYJ4CPas21SyRuVZZYkwbLzF78L4Bxdg6nMkmiapLkw0Cc/0?wx_fmt=jpeg)

# [更新]单文件LNK绕过，但有限制

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# [更新]单文件LNK绕过，但有限制

4个月前，我无意发现了[[0day]新挖掘到一套高级LNK快捷方式](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484553&idx=1&sn=1e2519baefe6c1cafad43d50e21a44f6&scene=21#wechat_redirect)，现在它可以支持单文件， 但有条件限制，文末我录了个视频展示这一研究成果。

### 一、背景

上次发出之后，许多朋友问能否支持单文件，说多文件没有实战价值，我尝试**将2文件进一步缩减为单文件**，也尝试过[LNK Icon Smuggling](https://mp.weixin.qq.com/s?__biz=Mzg4NzkwMDA5NQ==&mid=2247484328&idx=1&sn=35adb8db20fd519886909b62c3ddfdb4&scene=21#wechat_redirect)的建议，但该程序不支持。

> 在`360`下挖掘LNK漏洞非常困难，因为绝大部分进程被禁止。但万事不是绝对，上次将system32下的程序扒了个底朝天，同时参考了大量的APT资料，经过999次的失败，有一个新发现。

### 二、技术细节

我无法透露这一实现细节，毕竟公开进程等于双手奉上漏洞或被滥用。

在原有基础上新增`单文件`模式，勾选此选项代表只需单文件即可，因为另一个文件会放在`远程`服务器以供读取。

![新版本](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqOfk7hSRKzticf2YwhJcNuto6I8ias7Q7ZnShPMd8icBAh7R7IsdHMnfDeT7NcQKJcglibJMNMbA50tk9MdJ8EQ6noiaOXlXAiaykvkg/640?wx_fmt=png&from=appmsg "null")

新版本

**限制条件：**

不支持Win11

> 由于NTML漏洞的影响，较新的Windows11-24H2会默认阻止不安全的SMB共享。这意味着，在Win11中如需使用远程UNC路径，必须开启带身份验证的SMB：

![开启带身份验证的SMB共享](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqNfj779rcOVkkn2cZWicnurWpeCvhzYXiaHQdnxETH2QDqnLIAsSQtpmxq0HH5aUDlUaEcKic28Z51Ic57lTwREcjhp38KPgeTkQg/640?wx_fmt=png&from=appmsg "null")

开启带身份验证的SMB共享

而开启身份验证后，需多一步认证的步骤：

![在目标终端中连接共享](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqMtLmiaMJJAqwNrURk1ll8wMImGBibIdiaN4BWF0bic64yUDTGqTVsIllUvk0TjXYPWEsIdW4RU7x8dGEKu50nW17bc6zRicmnWPTks/640?wx_fmt=png&from=appmsg "null")

在目标终端中连接共享

接下来可以运行lnk文件，:

![](https://mmbiz.qpic.cn/mmbiz_gif/ibXL9MCj2GqNZru1taMMPg4aowgicpicQ9226AsDBaZBvNAaRFKA9WribsYOwBthrPxCU2CgticRYBiaA06Rw90CNrFo5NjrVSJPWkh4b8Lyq48YA/640?wx_fmt=gif&from=appmsg "null")

而在Win10系统中，无需认证即可连接，这意味着Win10不受此限制。

![未经身份验证的SMB共享](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqMQZtBRvvjXU0LBISW8ibUX6V59uDiciaWPOBlpuZ7P2qib9lXVxkv6RrRFSAmqI9dKFAuKUib7j3ShC7g3vAdNRNy33xrBmdVqPNK4/640?wx_fmt=png&from=appmsg "null")

未经身份验证的SMB共享

最后，我录了个视频展示这一研究成果：
[视频]

### 三、检测情况

2种不同的模式检测情况(2026年5月1)如下：

| AV | 2文件 | 单文件 |
| --- | --- | --- |
| Defender | 绕过 | 绕过 |
| 火绒 | 绕过 | **被检测** |
| 360卫士 | 绕过 | 绕过 |

如果你对这些红队项目感兴趣或想了解更多信息，可查阅我的产品清单《2026年度红队战术攻防武器库产品手册》[1]及协议《合规协议》[2]。

#网络安全 #红队训练

---

### 四、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

* • 仅可用于已获得书面授权的目标系统测试；
* • 遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

#### 推荐阅读

* • [[视频]4月-红队攻防-完全无法检测的Cobalt Strike](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485322&idx=1&sn=42ad6bb62c4ed023c5d6fc845e692c00&scene=21#wechat_redirect)
* • [[更新]红队加载器LoaderV6.2](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485312&idx=1&sn=1dfa1d392634946dd40994d4f31e32f5&scene=21#wechat_redirect)
* • [高级LNK中的反沙箱技术](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485293&idx=1&sn=3ff02916e7a6b13d280fa145a281e42e&scene=21#wechat_redirect)
* • [[重要更新]高级lnk快捷方式](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485269&idx=1&sn=8897a078d020aa9ff1a1f36c253dedd0&scene=21#wechat_redirect)
* • [红队基础设施指南与高级匿名技术](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485253&idx=1&sn=c55c3849c88bd3b039427b66dd7802fb&scene=21#wechat_redirect)

#### 引用链接

`[1]` 《2026年度红队战术攻防武器库产品手册》: *https://www.kdocs.cn/l/coR1BuQkseWz*
`[2]` 《合规协议》: *https://www.kdocs.cn/l/cqPic7iLh0hn*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

白帽子安全笔记2.0

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

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