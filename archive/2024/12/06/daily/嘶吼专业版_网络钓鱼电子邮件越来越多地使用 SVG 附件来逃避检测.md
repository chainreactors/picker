---
title: 网络钓鱼电子邮件越来越多地使用 SVG 附件来逃避检测
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580078&idx=1&sn=9a9522c0b349583b66c4c0d1f21b1978&chksm=e9146994de63e08286e381939950fafa998df8f9871abb353cf2eaee2bd0ec399ebbd0cd49cc&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-06
fetch_date: 2025-10-06T19:39:32.651712
---

# 网络钓鱼电子邮件越来越多地使用 SVG 附件来逃避检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28llckKmFc5bNfoue5bTkHkOe7mnxbllCK8DHP5vkXHHnW3QibB3pPpZ05HECdrW6XPz5t4CjB9LhQ/0?wx_fmt=jpeg)

# 网络钓鱼电子邮件越来越多地使用 SVG 附件来逃避检测

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

威胁者越来越多地使用可扩展矢量图形 (SVG) 附件来显示网络钓鱼形式或部署恶意软件，同时逃避检测。网络上的大多数图像都是 JPG 或 PNG 文件，它们由称为像素的小方块网格组成。每个像素都有特定的颜色值，这些像素一起形成整个图像。SVG（即可缩放矢量图形）以不同的方式显示图像，因为图像不是使用像素，而是通过代码中文本数学公式中描述的线条、形状和文本创建。

例如，以下文本将创建一个矩形、一个圆形、一个链接和一些文本：

Hello, SVG!

在浏览器中打开时，该文件将生成上述文本描述的图形。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28llckKmFc5bNfoue5bTkHkhxPTn2fwzVzUiayEkWLZib15knjbDTeibN4qJG9gkBlIplhDcNoibA0h5w/640?wx_fmt=png&from=appmsg)

生成的 SVG 图像

由于这些是矢量图像，它们会自动调整大小，而不会损失图像质量或形状，这使得它们非常适合在可能具有不同分辨率的浏览器应用程序中使用。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28llckKmFc5bNfoue5bTkHkia6AK9ibOBnDTyHpaxVNkbGd14ery53UOB3eicGnhSoZp0Mxsvq1TjibfQ/640?wx_fmt=png&from=appmsg)使用 SVG 附件逃避检测

在网络钓鱼活动中使用 SVG 附件并不是什么新鲜事，然而，根据安全研究人员发现，威胁者正在网络钓鱼活动中越来越多地使用 SVG 文件。

SVG 附件的多功能性，使得它们不仅可以显示图形，还可以使用。这使得威胁者可以创建 SVG 附件，这些附件可以创建网络钓鱼表单来窃取凭据。如下所示，最近的 SVG 附件 [VirusTotal] 显示了一个带有内置登录表单的虚假 Excel 电子表格，提交后会将数据发送给受害者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28llckKmFc5bNfoue5bTkHkuULc8lJndyAy2FviaxADM6UNZEMH2QFRS2iaaeOMNvYNz2OZ4vzNcphg/640?wx_fmt=png&from=appmsg)

显示网络钓鱼表单的 SVG 附件

最近活动 [VirusTotal] 中使用的其他 SVG 附件会伪装成官方文档或要求提供更多信息，提示您单击下载按钮，然后从远程站点下载恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28llckKmFc5bNfoue5bTkHkQliaGibs7UG4Tn0AYaVX7Hm9DCVe7n64Rb6cehPA2XqZ3Us11icbGRK4w/640?wx_fmt=png&from=appmsg)

用于分发恶意软件的 SVG 附件

其他活动利用 SVG 附件和嵌入式 JavaScript 在打开图像时，自动将浏览器重定向到托管网络钓鱼表单的网站。问题在于，由于这些文件大多只是图像的文本表示，因此安全软件往往不会检测到它们。

从上传到VirusTotal的样本来看，最多只有一两次被安全软件检测到。尽管如此，接收 SVG 附件对于合法电子邮件来说并不常见，人们应保持怀疑态度。

除非您是开发人员并希望收到这些类型的附件，否则安全研究人员会建议删除包含它们的任何电子邮件会更安全。

参考及来源：https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28llckKmFc5bNfoue5bTkHkLuWZMhURt3Mu7AgzgdP1yzcibpqYdM1v6FZI9BAtuDrhcyJU4oYAX1Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28llckKmFc5bNfoue5bTkHkIe9I4Xia1tic15e2Zhibickk1xM0emTnLj5k1jUHkMnpOKMhzOkia3E2U6Q/640?wx_fmt=png&from=appmsg)

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