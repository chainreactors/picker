---
title: Windows服务器如何免费防篡改
url: https://mp.weixin.qq.com/s/lAB-llMo7k8MKrKh3RrYbw
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:00:30.529111
---

# Windows服务器如何免费防篡改

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jkQ8np17VibhyqHYHmFk8DtutSNZRt2KrNJiaS3O9ktqvEtEmHTpDoNvQJia6zJQx589Ueia3e5Xskxovu580zucmeXa9rviaaicsPv4eqsAttS7s/0?wx_fmt=jpeg)

# Windows服务器如何免费防篡改

原创

护卫神
护卫神

网站安全说

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

防篡改是安全防护中至关重要的一环。尽管我们可以通过修复网站程序漏洞来减少入侵风险，但黑客仍可能利用操作系统或应用软件的漏洞实施非法篡改行为——毕竟入侵途径实在太多了。

说到网页防篡改，大多数人首先想到的是使用专门的防篡改软件。这确实是最直接的方式。不过，如果不借助第三方软件，通过ACL权限策略也能免费实现防篡改的效果，只是配置过程相对复杂，对操作者的专业技术水平和安全经验要求较高。

这个方法只对IIS有效。在IIS框架下，访问网站的用户权限默认称之为IIS匿名账户，我们设置网站目录，对这个匿名账户只给读取权限，就实现了防篡改功能，操作一共分三步。

**第一步：添加匿名账户**

在“**计算机管理-本地用户和组-用户**”，点击鼠标右键，选择“**新用户**”，填写用户名和密码（例如：Web\_Hws），注意勾选“用户不能更改密码”和“密码永不过期”。

 ![1.png](https://mmbiz.qpic.cn/mmbiz_png/jkQ8np17VibhLMsO5NOF1bQzHCJgsaZI2ebCvVpGwBDN0hG4ukW8x12KsREvrkyrc6lyZOv7icGIzsaIjnzzOVPPftPNcC9LsdPZ8D8jw3b9I/640?wx_fmt=png&from=appmsg "1.png")

添加好以后，找到新添加的用户，在名称上点击右键，选择“**属性**”，进入“**隶属于**”选项卡，删除“Users”组，添加“Guests”组，点击“确定”保存。

 ![2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jkQ8np17VibjF7oiaMtqQvEjicP2GgXI183oTs8hU3IK4PiahNqKE9T5tYRVQoiarDTxz0DNfbD3ia4mhX4cyK4assWmvE83YCnx2bNt43JtoAvlE/640?wx_fmt=png&from=appmsg "2.png")

**第二步：设置网站目录权限**

在网站根目录上点击鼠标右键，点击“**属性**”，选择“**安全**”选项卡。

点击右下角的“**高级**”，在弹出的窗体中点击“**禁用继承**”，再选择“**将已继承的权限转换为此对象的显式权限**” ，点击“**确定**”按钮，保存的同时会关闭此窗体。

 ![3.png](https://mmbiz.qpic.cn/mmbiz_png/jkQ8np17VibgQB0agCibl0G7v0nS47Bp06qSWEDGY7bv9AX7QerpsFbadSGca0ia9oI1ozLIQvxTmd9KwPicOuY994hu9pjduH7uGFMsf35jc2I/640?wx_fmt=png&from=appmsg "3.png")

回到“**安全**”选项卡窗体，点击“**编辑**”，删除冗余权限，只保留Administrators和System。然后添加IIS\_IUSRS和Web\_Hws的权限，只给予“读取”。

 ![4.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jkQ8np17Vibia4pbzNkBp8enwnL5HJVWIREVn8Vj14Wk5N6vAzwFPhAo1icDpmwNTBRTiaTEzeRG8AtXJQ7Pm7PFW5yusKSszcIo44xUH1QL5c0/640?wx_fmt=png&from=appmsg "4.png")

**第三步：配置网站启用匿名账户**

进入IIS，找到对应的网站，进入“**身份验证**”页面，在“**匿名身份验证**”上点击鼠标右键，选择“**编辑**”，在弹窗中点击“**设置**”按钮，然后输入刚才创建的匿名账户和密码。

 ![5.png](https://mmbiz.qpic.cn/mmbiz_png/jkQ8np17VibgR0wia5AJTvEbkQBR6oT3fwxuEjicDSg54SvUA5ovUFqiasr4n5OLA0jjJdu6roibpFjuDnahcYaeOKfmCGfSvRh2PbnIR0cDfuw8/640?wx_fmt=png&from=appmsg "5.png")

至此操作完成，只需简单三步，不花费一分钱就能实现防篡改功能。如果有多个网站，每个网站重复上述的操作，注意用户名不能相同。

不过在实际应用时，会有一些副作用，例如缓存目录、图片目录，也没法写入文件，导致网站不能正常运行。解决办法也不难：给这些目录单独加匿名账户的写权限，但务必在IIS禁用这些目录的脚本权限。

总体而言，对于不是专业搞运维的人，操作起来有些困难。如果经济允许，使用轻量级的防篡改系统会更合适。推荐使用【护卫神.防入侵系统】，内置几乎所有CMS的防篡改规则，只需选择网站根目录和防篡改模板，就能配置强大的防篡改功能，而且没有副作用。对缓存目录、图片目录开放写权限的同时，还能阻止黑客上传网页木马到这些目录进行访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jkQ8np17VibjjnXeqxI8delQfwib43VQqmm9rjVN8Et7T5tPQ5fdgubn7zgeLQ3RpBAVubm2pqX50qflchbjESse6NxwWxOVNBNNB4hyRLZ8I/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NV9GjS35LEh5QDfFonaZkRr55IgslibHfSR3vic4EUUyhRVqr2ic5cJx2IPtZm1T4icK3e2Qz8crIibdQAN3535f6kg/0?wx_fmt=png)

网站安全说

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NV9GjS35LEh5QDfFonaZkRr55IgslibHfSR3vic4EUUyhRVqr2ic5cJx2IPtZm1T4icK3e2Qz8crIibdQAN3535f6kg/0?wx_fmt=png)

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