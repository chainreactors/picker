---
title: 网络钓鱼电子邮件越来越多地使用 SVG 附件来逃避检测
url: https://www.4hou.com/posts/rpXB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-06
fetch_date: 2025-10-06T19:35:31.352834
---

# 网络钓鱼电子邮件越来越多地使用 SVG 附件来逃避检测

网络钓鱼电子邮件越来越多地使用 SVG 附件来逃避检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 网络钓鱼电子邮件越来越多地使用 SVG 附件来逃避检测

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-12-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)70266

收藏

导语：其他活动利用 SVG 附件和嵌入式 JavaScript 在打开图像时，自动将浏览器重定向到托管网络钓鱼表单的网站。

威胁者越来越多地使用可扩展矢量图形 (SVG) 附件来显示网络钓鱼形式或部署恶意软件，同时逃避检测。网络上的大多数图像都是 JPG 或 PNG 文件，它们由称为像素的小方块网格组成。每个像素都有特定的颜色值，这些像素一起形成整个图像。 SVG（即可缩放矢量图形）以不同的方式显示图像，因为图像不是使用像素，而是通过代码中文本数学公式中描述的线条、形状和文本创建。

例如，以下文本将创建一个矩形、一个圆形、一个链接和一些文本：

```

    Hello, SVG!
```

在浏览器中打开时，该文件将生成上述文本描述的图形。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241119/1731998603688767.png "1731997921186248.png")

生成的 SVG 图像

由于这些是矢量图像，它们会自动调整大小，而不会损失图像质量或形状，这使得它们非常适合在可能具有不同分辨率的浏览器应用程序中使用。

**使用 SVG 附件逃避检测**

在网络钓鱼活动中使用 SVG 附件并不是什么新鲜事，然而，根据安全研究人员发现，威胁者正在网络钓鱼活动中越来越多地使用 SVG 文件。

SVG 附件的多功能性，使得它们不仅可以显示图形，还可以使用。这使得威胁者可以创建 SVG 附件，这些附件可以创建网络钓鱼表单来窃取凭据。如下所示，最近的 SVG 附件 [VirusTotal] 显示了一个带有内置登录表单的虚假 Excel 电子表格，提交后会将数据发送给受害者。

![svg-phishing-form.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241119/1731998604189053.png "1731997813179088.png")

显示网络钓鱼表单的 SVG 附件

最近活动 [VirusTotal] 中使用的其他 SVG 附件会伪装成官方文档或要求提供更多信息，提示您单击下载按钮，然后从远程站点下载恶意软件。

![svg-malware.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241119/1731998606904866.png "1731997857155979.png")

用于分发恶意软件的 SVG 附件

其他活动利用 SVG 附件和嵌入式 JavaScript 在打开图像时，自动将浏览器重定向到托管网络钓鱼表单的网站。问题在于，由于这些文件大多只是图像的文本表示，因此安全软件往往不会检测到它们。

从上传到VirusTotal的样本来看，最多只有一两次被安全软件检测到。尽管如此，接收 SVG 附件对于合法电子邮件来说并不常见，人们应保持怀疑态度。

除非您是开发人员并希望收到这些类型的附件，否则安全研究人员会建议删除包含它们的任何电子邮件会更安全。

文章翻译自：https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iQ4m54Op)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)