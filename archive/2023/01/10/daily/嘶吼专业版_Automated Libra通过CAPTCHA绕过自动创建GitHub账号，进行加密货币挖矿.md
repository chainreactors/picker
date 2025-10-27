---
title: Automated Libra通过CAPTCHA绕过自动创建GitHub账号，进行加密货币挖矿
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247556226&idx=2&sn=6f190cb64d81eba51f261f30017ad738&chksm=e915ccb8de6245aea309264ea8b6b36dfa1e22506a15114596ab3d94df6119208c6c8e0f7bea&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-01-10
fetch_date: 2025-10-04T03:26:27.863355
---

# Automated Libra通过CAPTCHA绕过自动创建GitHub账号，进行加密货币挖矿

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYz28AY197YrdPKRXz9lmrrBvJb6UfcVe3vAjcQw2ib0K1X1fLw2o7gpA/0?wx_fmt=jpeg)

# Automated Libra通过CAPTCHA绕过自动创建GitHub账号，进行加密货币挖矿

ang010ela

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Automated Libra黑客组织通过CAPTCHA绕过技术自动账号创建，进行加密货币挖矿。

近期，南非黑客组织'Automated Libra'通过CAPTCHA绕过技术实现自动账号创建，在云平台创建账户，利用免费的资源进行加密货币挖矿来获利。

Automated Libra是位于南非的黑客组织，也是freejacking攻击活动PurpleUrchin背后的黑客组织。Freejacking 是使用免费云资源来执行加密货币挖矿活动的过程。Unit 42 研究人员分析了Automated Libra的250GB数据，发现了黑客的基础设施、历史和使用的技术。黑客使用简单的图像分析技术绕过CAPTCHA图像，实现云平台自动化账号创建，每分钟可以成功创建3-5个GitHub账户。Unit 42研究人员成功发现了黑客在PurpleUrchin攻击活动中使用的40个加密货币钱包和7种不同的加密货币。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)利用GitHub工作流进行加密货币挖矿

Automated Libra在针对GitHub的攻击活动中融合了Play and Run以及freejacking技术。此外，攻击者还利用了GitHub CAPTCHA检查的弱点。

攻击者以平均每分钟3-5个的速度自动创建GitHub账号。创建GitHub账号后，就开始了freejacking攻击活动。

攻击者在不同的VPS（virtual private server）提供商和云服务提供商平台上创建了超过13万个账户，但是并没有付费。这些创建的账户使用的都是虚假的个人信息以及信用卡信息。这使得攻击者可以在完成加密货币挖矿活动后并未完成付费。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)自动化账号创建

创建GitHub账户的第一步是输入邮件地址、密码和用户名，如图1所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYMFOtibIjoSNgEz6EAQfibHrVh0OeYyR19n5Rdw8nup9icr6XIp5BbYq4Q/640?wx_fmt=png)

容器运行虚拟网络计算（VNC）服务器：使用如下命令启动Iron浏览器：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYIWLGuicMEVGjqCaeOu7ExUPTpLdxHFeUPJrMibChAibsCEpicKEib3y3rDw/640?wx_fmt=png)

图 2. VNC服务器展示Iron浏览器

然后使用xdotool工具，该工具是完成GitHub表单的主要脚本。表单完成后，GitHub会提示CAPTCHA：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYLyfaowrgwYpgRfCcOJ0OC8c2kK6DZtBw0hO29viady24yDLa2ZYso6Q/640?wx_fmt=png)

图 3. GitHub CAPTCHA

攻击者使用了一个非常简单的机制来解决CAPTCHA问题。从攻击者创建的GitHub账户统计数据来看，攻击者实现CAPTCHA绕过的方法非常有效。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)利用CAPTCHA的弱点

为绕过CAPTCHA需要识别图片背景中的星系，攻击者使用了ImageMagick工具套件中的2个工具：convert 和 identify。

首先，使用convert工具将图像转化为RGB格式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYGibM9KhTRgZibBGzYpDsxY4PmRpQQe5zTcjSGzib14vZ9qbOXBCeb759g/640?wx_fmt=png)

图 4将图像转化为RBG

转化完成后，使用identify命令来提取red 通道的skewness 特征：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYq2T3ia4j4WxCIp6CAGp8RzKcJuPCDibehGBTVmJ3iatZIjl1stw72fh0Q/640?wx_fmt=png)

图 5. 提取red 通道的skewness 特征的命令

最终的结果如图6所示，以从大到小的顺序排序。值最小的图像就是背景图片，比如：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYXibcu7x2jiaJAdjGVRCHmZ5Z87BjAXwslp4MAc0LorHpibcDL9PWTCTYg/640?wx_fmt=png)

图 6. 每个图片的red通道输出

图4中的image 2就是识别出的星系背景图片。CAPTCHA解决后，GitHub需要一个启动码，如图7所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY1osFErCEHLyCggQIZyosPZ2Zg3JeeNMYWmYmee5mgyIIOFm6BGllLQ/640?wx_fmt=png)

图 7. GitHub 请求启动码

攻击者使用Gmail账号来自动获取启动码。这一过程使用了IMAP协议和PHP脚本来读取收到的IMAP消息。

启动码输入后，自动化过程就可以生成个人访问token。GitHub注册过程的最终结果是一个用户名和GitHub部署的个人访问token。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY6ic8WWE4In5BzHstVO4nCwHwvGLaiaiawh7qCficXylhUcfU5LtIniaQdDw/640?wx_fmt=png)

图 8. 调用运行的容器

随后，容器执行以下操作：

设置SSH 密钥；

使用GitHub API创建GitHub库；

配置创建的库的权限。

此外，攻击者还使用基于MD5哈希值的随机名来对库进行命名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYrSZljPMJRtDN7Ocns7lcRRZBOyOXAnhbPW8qSRIDdwz98yCAYeGSfA/640?wx_fmt=png)

图 9. 对库进行随机命名的命令

GitHub库创建完成后，攻击者调用一个bash脚本来用目标工作流来更新库。工作流是用PHP脚本生成的， PHP模板编码的工作流示例如图10所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYSnZSjmRSkarkia2NdVzGCxWo8hDicGjBZROic3yx5wjgfCFO1vSIbk90g/640?wx_fmt=png)

图 10. PHP模板

研究人员发现其中的一个工作流中有64个任务。生成的工作流配置为github.event.client\_payload.app事件下的repository\_dispatch运行。工作流机制允许攻击者执行外部应用。在本例，攻击者运行外部bash脚本和容器，如图11所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYFD9FqHaMkqVpRCG1Ju54d8uSduyGBe58dfXQAzEy2j7XMYc6pmf5wA/640?wx_fmt=png)

图 11. 执行外部应用的工作流机制

工作流运行的bash脚本是从外部域名访问的。攻击者运行的容器是用来安装和初始化加密货币挖矿功能的，如图12所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYJ94LFCDfyZVI5YYg93CCictpaGWse6FumFXyglZu9ibjhTxuvgoPOgEQ/640?wx_fmt=png)

图 12. 加密货币挖矿容器

生成的工作流运行64个任务，每个任务都从5个可用的唯一配置中随机选择一个。

经过确认的攻击者创建的GitHub账户数如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYQMSWZv7qPsiabsyAibgLVMU0jFQgLx57shDjrMKwZ1NoXcf7HDGWPQHw/640?wx_fmt=png)

图 13. PurpleUrchin攻击者创建的GitHub账户数

此外，攻击者还在Heroku、Togglebox、GitHub等不同云平台服务商创建了超过13万用户账户。

参考及来源：https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY8ibUfL0VE1I201h1RRVZobiaLSUzGMPqtSuhCASCo6U7iavsibpcVNtYIw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYiccVtVfamoV5CmOLoWymczo2ftpBxbPPwiaMATs9mjGUAr0UiaPM2K2Jg/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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