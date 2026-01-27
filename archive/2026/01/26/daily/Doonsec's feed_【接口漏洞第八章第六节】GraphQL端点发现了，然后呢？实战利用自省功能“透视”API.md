---
title: 【接口漏洞第八章第六节】GraphQL端点发现了，然后呢？实战利用自省功能“透视”API
url: https://mp.weixin.qq.com/s/NZbfQNFcp8tQKJHBidP-Ng
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:36:37.625629
---

# 【接口漏洞第八章第六节】GraphQL端点发现了，然后呢？实战利用自省功能“透视”API

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q0adkO8PP0kkA4jjVukw2za3UibtFVmWZxqmv6ibibicicN1ngFpnhBXLIG8c9oQgDwUibPhGjOTmbdicpQA/0?wx_fmt=jpeg)

# 【接口漏洞第八章第六节】GraphQL端点发现了，然后呢？实战利用自省功能“透视”API

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

我们在前面章节中，有大量介绍到GraphQL API的自省功能理论原理，但在实际运用中，要如何使用，可能大家会有些疑惑，今天我们就结合实际的例子来演示一波，帮助大家加深理解。

在开始之前，还是进行系统的全面访问，并获取到可疑的 GraphQL API 端点，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0adkO8PP0kkA4jjVukw2za78Y4FMAw5t3iaFcDXvN69RcXgqWdqOCHQJ6PPxxN0uwa0kISRRUktyA/640?wx_fmt=png&from=appmsg)

发现端点后，将该接口发送至burpsuite的repeater插件中，并做进一步挖掘。

在repeater中，burpsuite工具中会自动识别 GraphQL API 接口是否开启了自省功能的，被测系统如果开启了该功能，我们就可以直接进入repeater菜单中的 GraphQL 功能，并选择 Set introspection query 功能项，就可以自动拆解接口内部文档内容，并能正常响应接口请求参数内容。

如下图，通过工具调用该 graphQL 接口的自省功能后，得到系统的所有请求字段信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0adkO8PP0kkA4jjVukw2zaqno3NbNtcNdOTNY6Blluk1ufQYsOicxXMLsZR2Ks6mOrWu3dicXbPqHQ/640?wx_fmt=png&from=appmsg)

在获取到系统响应的内部字段后，我们就要阅读理解响应字段内容，以上响应字段内容中，有一个比较特殊的参数字段，是"postPassword"，我们暂时留言一下这个字段。并复制留用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0adkO8PP0kkA4jjVukw2zaFfyDsEQ6IzTan2zjymnVdj9K55XIYKsTf98nGLl51xseIfqX0qv8Ng/640?wx_fmt=png&from=appmsg)

在通过接口的自省功能，获取到隐藏的敏感字段后，我们就要做最后一步的验证及利用步骤了。我们先来看该接口的原始请求格式及数据响应内容，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0adkO8PP0kkA4jjVukw2zauEQiclxibm94tDYDQAxf8C7ExLictGw83Db31xLfzSdpfZQqT7MnlKekA/640?wx_fmt=png&from=appmsg)

知道 graphQL api 的请求参数格式后，我们就可以将之前通过自省功能获取到的可疑参数字段 “postPassword”放入并进行验证。最终可以发现，该系统确实存在自省功能泄露敏感信息的情况，通过添加自省功能响应的字段名称，就能直接请求响应到对应操作人的系统密码信息。【不仅限于密码，还有其他的一些数据，都可以通过添加正确的参数名进行获取】具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0adkO8PP0kkA4jjVukw2zatN52ueibINa2N7pCpr3y6AYvojRWb7ibOPRoXics4pTicj0XlVYptGj6YA/640?wx_fmt=png&from=appmsg)

好了，今天的实际操作就分享到这，希望这种实际场景的操作，对你理解graphQL api 的自省功能有些帮助，关于API接口漏洞的相关内容，这边会持续分享，感兴趣的话，可以点点关注。

觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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