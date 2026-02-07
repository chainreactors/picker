---
title: jsPDF库两大漏洞可致代码注入与系统崩溃，千万开发者需立即升级
url: https://mp.weixin.qq.com/s/ezmGOPRRBDLljggC3V8xiQ
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:06:14.992427
---

# jsPDF库两大漏洞可致代码注入与系统崩溃，千万开发者需立即升级

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1j4glQg8FXeYIUvNhm7UvWZQBcRic707Q9kiaDFstlILhorXQmE2QiceWw5wVdzNxkhCbAdiaWmFqxKd99cDxrLvxrODO90Bc2p5A/0?wx_fmt=jpeg)

# jsPDF库两大漏洞可致代码注入与系统崩溃，千万开发者需立即升级

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

近日，备受开发者欢迎的前端PDF生成库jsPDF被曝出两个高危安全漏洞。利用这些漏洞，攻击者可向PDF文档中注入恶意代码，或通过一张特殊图片导致应用程序或浏览器标签页崩溃。安全专家强烈建议所有使用该库的开发者立即采取行动。

这两个漏洞编号分别为CVE-2026-24737（CVSS评分8.1）和CVE-2026-24133（CVSS评分8.7），均存在于旧版本中。

**漏洞一：通过PDF表单工具实现代码注入**

第一个漏洞（CVE-2026-24737）出现在库的AcroForm模块中，该模块用于为PDF添加复选框、单选按钮等交互式表单字段。问题的核心在于，如果应用程序未对用户输入进行严格过滤，攻击者便能够操控相关API属性，向PDF文档中注入任意PDF对象（包括恶意JavaScript代码）。

这意味着，一旦用户打开由攻击者恶意构造的PDF文档，其中隐藏的脚本便可能自动执行，窃取用户数据或进行未授权操作，风险极高。

**漏洞二：一张“图片炸弹”即可引发程序崩溃**

第二个漏洞（CVE-2026-24133）是一个典型的拒绝服务（DoS）漏洞，位于BMP图片解码器中。攻击者只需构造一张“特殊”的BMP格式图片，在其文件头中嵌入异常巨大的宽度或高度值。

当jsPDF的`addImage`方法尝试处理这张“图片炸弹”时，会触发过度的内存分配，最终导致应用程序或浏览器标签因内存不足而崩溃。这为攻击者提供了一种通过上传图片或特定链接就能瘫痪服务的简易途径。

**解决方案：立即升级至安全版本**

jsPDF维护团队已在新版本中修复了上述漏洞。官方强烈建议所有开发者立即将项目中的jsPDF升级至4.1.0或更高版本。

对于无法立即升级的用户，唯一可行的缓解措施是实施极其严格的输入验证。务必在将用户提供的数据（尤其是表单字段内容和图片文件）传递给jsPDF相关API前，进行充分的清理和校验，切勿直接信任未经处理的用户输入。

参考来源：

本文安全通告内容基于jsPDF官方发布的安全更新及漏洞披露信息。建议开发者参考官方Git仓库的发布页面与安全公告，以获取最准确的技术细节和修复指导。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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