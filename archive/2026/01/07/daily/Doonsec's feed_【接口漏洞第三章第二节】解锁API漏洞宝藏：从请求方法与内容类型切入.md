---
title: 【接口漏洞第三章第二节】解锁API漏洞宝藏：从请求方法与内容类型切入
url: https://mp.weixin.qq.com/s/06uaTTcW9QZaNjQqbXA6Xw
source: Doonsec's feed
date: 2026-01-07
fetch_date: 2026-01-08T03:27:30.025856
---

# 【接口漏洞第三章第二节】解锁API漏洞宝藏：从请求方法与内容类型切入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q1giaUw4gWOvrsoqLSPbaoGia8ZDWiaTpGJuj7hGgzepuquaFscXxlvevvnmzXLoHZrE1f8vvl9o0pdQ/0?wx_fmt=jpeg)

# 【接口漏洞第三章第二节】解锁API漏洞宝藏：从请求方法与内容类型切入

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于升斗安全
，作者升斗安全XiuXiu

![](http://wx.qlogo.cn/mmhead/2kpMNDYsSfCCBCENh6LOmFVgC9ciaIhQ4RHwsulEqe0kfcia0rFxsfQH0PLichNS01WIvWvHRpfPM4/0)

**升斗安全**
.

升斗安全：聚焦网安技术、漏洞挖掘与职业成长。 不止于漏洞原理，更专注实战利用。这里是关于白帽技术、赏金猎人与职业破局的硬核分享地。想提升你的“挖洞”功力？关注我们就对了。

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

我们在上一节中大概知道了关于api的漏洞挖掘中，需要关注HTTP请求方法（method）和内容类型（content-type）。今天我们就进一步给大家说下如何针对这两块内容进行验证挖掘。

一、识别支持的HTTP方法（method）

HTTP方法指定了对资源执行的操作。例如：

* GET - 从资源获取数据。
* PATCH - 对资源应用部分更改。
* OPTIONS - 获取可用于资源的请求方法类型信息。

一个API端点可能支持不同的HTTP方法（不仅仅只有以上这三个）。因此，在测试API端点时，检查所有可能的方法非常重要。这有助于发现端点的额外功能，从而扩大攻击面。

例如，端点 /api/tasks 可能支持以下方法（同样请求路径，使用的请求方法不同，作用也会不同）：

* GET /api/tasks - 获取任务列表。
* POST /api/tasks - 创建新任务。
* DELETE /api/tasks/1 - 删除任务。

您可以使用 Burp Intruder 内置的HTTP动词列表，自动遍历一系列方法进行测试。具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1giaUw4gWOvrsoqLSPbaoGiaxKXla4z5D2sz2GM6ph8pqTMUmvKjo12ACOMvCq9AmlUgDtZdiayzq3Q/640?wx_fmt=png&from=appmsg)

注意：

在测试不同的HTTP方法时，请以低优先级的对象为目标。这有助于确保避免意外后果，例如更改关键数据或创建过多记录（如update或是delete方法，一定要用自己的数据进行测试，避免真实存在漏洞的情况下，直接就将系统数据给更改了）。

二、识别支持的内容类型（content-type）

API端点通常要求数据以特定格式提交。因此，根据请求中提供的数据内容类型，API的行为可能有所不同。修改内容类型可能帮助您：

* 触发能够泄露有用信息的错误
* 绕过存在缺陷的防御机制

利用处理逻辑的差异。例如，某个API在处理JSON数据时可能是安全的，但在处理XML时却容易受到注入攻击。

要修改内容类型，我们只需要调整Content-Type请求头即可，并相应地重新格式化请求体。我们可以使用Content type converter扩展插件自动转换请求中提交的数据，实现XML与JSON格式之间的互相转换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1giaUw4gWOvrsoqLSPbaoGiaobHCzzJ4xwU8ricO8bfypt6bFZVcIiaaZMPORVCAnlbUpicbaCSSXFuBw/640?wx_fmt=png&from=appmsg)

直接在repeater中即可修改内容类型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1giaUw4gWOvrsoqLSPbaoGiaO32xeQOnicleFKYnM0PZFFsaycUhfCMKMQ0ib358wfa65QGicrwYmvXEg/640?wx_fmt=png&from=appmsg)

通过以上两种方式，我们就可以对找到的api接口进行请求方法和请求内容类型的测试。修改后重放请求，可能就会看到一些意想不到的情况，而这些，往往就是我们要挖掘的漏洞宝藏之地。

在下一节中，我们将结合实际的场景，来对以上内容进行实际的演示，让我们有更直观的理解。感兴趣的小伙伴们，欢迎关注、分享，这边会持续输出系列内容。

另外，别吝啬你的赞，你的肯定，对我很重要哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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