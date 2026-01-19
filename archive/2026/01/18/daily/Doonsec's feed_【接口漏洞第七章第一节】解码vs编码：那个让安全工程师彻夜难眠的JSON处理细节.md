---
title: 【接口漏洞第七章第一节】解码vs编码：那个让安全工程师彻夜难眠的JSON处理细节
url: https://mp.weixin.qq.com/s/dBHILYO09dGFDcJjxnY7bg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:36:11.906582
---

# 【接口漏洞第七章第一节】解码vs编码：那个让安全工程师彻夜难眠的JSON处理细节

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q1FLeSvS8FDDNS83c6G2oe0nZJhb0M6owTGLatjWyjSg1hn93UwEE6ian9mDr3b9Y4Np65SibnkTdXQ/0?wx_fmt=jpeg)

# 【接口漏洞第七章第一节】解码vs编码：那个让安全工程师彻夜难眠的JSON处理细节

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

今天我们来讲讲“结构化数据格式中的服务器端参数污染”如何进行挖掘和测试。

攻击者可通过操纵参数，利用服务器解析JSON、XML等数据时的漏洞进行攻击。

测试方法是：向用户输入中注入异常结构化数据，观察服务器响应。

示例1：普通参数注入

假设用户编辑个人资料时，浏览器发送：

```
POST /myaccountname=peter
```

此时服务器会将其转换为JSON请求：

```
PATCH /users/7312/update{"name":"peter"}
```

综合以上情况，我们进行尝试注入管理员权限参数【注意注入时的符号和格式】，具体如下：

```
POST /myaccountname=peter","access_level":"administrator
```

若输入未经严格过滤，此时服务器可能会进行以下请求：

```
PATCH /users/7312/update{name="peter","access_level":"administrator"}
```

从而导致用户peter获得管理员权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1FLeSvS8FDDNS83c6G2oe0ajNr1C4a2uucibge3rXZEbQ333Rt8903xkg3qIdQZeKAriaDhhG6xtZQ/640?wx_fmt=png&from=appmsg)

示例2：JSON数据直接注入

若前端直接提交JSON数据：

```
POST /myaccount{"name": "peter"}
```

这种情况下，前端和服务器端接收和请求连接是相同的，我们可以直接尝试注入【这种场景与前面章节说到的挖掘隐藏参数有相似之处】，需要注意的是前端提交的注入数据是带 \""编码的，具体如下：

```
POST /myaccount{"name": "peter\",\"access_level\":\"administrator"}
```

此时提交数据到服务器，若服务器对提交的数据解码后未重新编码，服务器接收的数据就会是下面这些：

{"name":"peter","access\_level":"administrator"}

这样就会导致权限提升。

当然，注入也可能发生在响应中

例如，用户输入存入数据库后，若未经编码直接嵌入API的JSON响应，就可能被利用。检测方法与请求注入类似。

需要注意，此类漏洞不仅限于JSON，XML等结构化数据同样存在风险。

总体来说，这类漏洞主要就是利用接口传参中的结构化数据，当服务器对这类数据校验不完善的情况下，就可能引起较多问题。

好了，关于api接口中的结构化数据，我们如何寻找突破点的思路就介绍到这。关于api接口漏洞，这边会持续输出更多内容，感兴趣的话，可以点点关注。

觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正

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