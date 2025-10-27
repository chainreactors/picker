---
title: .NET基础安全视频 | 生成强名称程序集规避防护规则
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247496071&idx=1&sn=671bdd31cea9a8acd3761aefbb0434c4&chksm=fa595f6acd2ed67c33b35dbdf7600148869ffd025087abaf839d70e2c16c4ce39eea3f03f445&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-10-19
fetch_date: 2025-10-06T18:53:12.536994
---

# .NET基础安全视频 | 生成强名称程序集规避防护规则

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9hLVQib6uyt20YqibJgA887CMLiaY5SD5yyPU0dMuicx7445NHQ3d1nzNSZ3fkLFS6GHnaUUSCqJPHmw/0?wx_fmt=jpeg)

# .NET基础安全视频 | 生成强名称程序集规避防护规则

原创

专攻.NET安全的

dotNet安全矩阵

01

.NET强名称程序集

.NET强名称签名在渗透测试和持久化驻留中为恶意代码提供了一定的可信度、稳定性和隐蔽性，有助于绕过基于强名称的安全策略限制，实现更隐蔽的持久化和跨应用程序的载入。

02

基本介绍

在 Visual Studio 中为程序集生成强名称签名的步骤相对简单。强名称签名是通过密钥文件（.snk 文件）给程序集赋予唯一标识的方式，帮助保证程序集的完整性，避免与其他具有相同名称的程序集发生冲突。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9hLVQib6uyt20YqibJgA887CmLnPia3e8LgXZBW2Tczia24RxFjRgcV61KibumMPichEbjAiclzxSSEoiaqw/640?wx_fmt=jpeg&from=appmsg)

03

原理分析

## 1.1 打开项目选中签名

首先，在 **解决方案资源管理器** 中找到并打开项目，右键单击项目并选择 **属性**。进入属性页面后，切换到 **签名** 选项卡，然后勾选 **对程序集签名** 复选框。这将启用签名选项

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9hLVQib6uyt20YqibJgA887C7AsX4Hiaw2cFzQdtbuL9ZMvX4R6ia2vgNcibbNhJK7CVBciateSmhKvamw/640?wx_fmt=png&from=appmsg)

## 1.2 生成密钥文件

在 **选择强名称密钥文件** 下拉菜单中，可以选择现有的密钥文件，或单击 **<新建...>** 创建一个新的密钥文件。若选择新建密钥文件，系统会提示为密钥文件命名（例如 MyKey.snk），并可以选择设置密码以保护密钥文件

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9hLVQib6uyt20YqibJgA887C07MQcbJTiaCfH6o9QW6yqvb7bMGyYZjXEBKaicEsMQBcJicRjctlNCfkA/640?wx_fmt=png&from=appmsg)

综上，通过这些步骤，即可在 Visual Studio 中为程序集生成强名称签名。强名称签名并不会加密程序集，但能保证其唯一性和安全性，再注册到全局缓存里可以绕过一些安全防护规则。视频内容已经打包在星球，感兴趣的朋友可以加入观看学习。

04

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=4&sn=db68011fb075c1d02268811163646b53&chksm=fa5947adcd2ecebbb1ca6659f289a5e344e37d1136fe0bd9272b5578e4c71bb19bb250e934d3&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOE2ogFoYIdqnYynqF6XyicI7XfRsWsn36wsCpKpAJcIQOicZUhbDJOe0w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488762&idx=1&sn=a5710927a6ba09b5c83adf616e2b12ae&chksm=fa5aba17cd2d330119d1ab2ce4b3a434274f0adf96729dbf8f04bef16c389565fc144f84d341&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

05

加入.NET安全基础入门

在这里，不是孤军奋战。我们特别设立了多个会员专属的内部星球陪伴群，加入的成员可以自由地提出疑问、分享见解、相互启发。我们相信，通过思想的碰撞与经验的交流，您将收获远超预期的宝贵财富。目前已有80+位朋友抢先预定，对.NET安全基础入门知识感兴趣的朋友们请尽快加入星球！

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8iciasX3mOSk23icIyjXqibhQE8nibEBxSljtLrQMlf3kHrLPa0Y1icR5ibodAFbTEkdLia2tSib4W6VNdEsQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

为了回馈广大朋友们的热情与支持，****特别给朋友们准备早鸟价129元，**后期价格随着内容和质量的不断沉淀会适当提高******。这不仅是对您前瞻眼光的认可，更是为了让您以更优惠的价格，拥抱日益增长的知识价值。越早行动，优惠越多，福利满满！

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9hLVQib6uyt20YqibJgA887CI3ibHBz2nBDJI2ib15JmImYaoghGe6G7hPX5V1RtrykoqeCshNZabzkg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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