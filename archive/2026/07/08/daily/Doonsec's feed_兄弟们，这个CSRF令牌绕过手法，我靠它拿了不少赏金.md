---
title: 兄弟们，这个CSRF令牌绕过手法，我靠它拿了不少赏金
url: https://mp.weixin.qq.com/s/d3BshNOv91ti17G80jWb2g
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:01:06.509783
---

# 兄弟们，这个CSRF令牌绕过手法，我靠它拿了不少赏金

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qg1MKHx3jGGiavCUjCSJTz9gCu3O9fuH8mYQ17qMyOG33iaUkX3fNzAdqyZOZs2u1Zm0S5xQhSkHQhwnDvhFBibICQfKTWicpOkNPk2F8QD7kn8/0?wx_fmt=jpeg)

# 兄弟们，这个CSRF令牌绕过手法，我靠它拿了不少赏金

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

做赏金猎人这些年，我总结出一个规律：很多时候不是防御太强，而是校验逻辑自己给自己挖了坑。今天聊一个最常见的CSRF令牌绕过姿势，简单到你可能会怀疑自己之前为什么没发现。

令牌校验，居然还挑请求方法

有些应用只对POST请求认真检查令牌，一换成GET就完全放行。就像门卫只看正门，侧门随意进出。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGE1bD6xhicG6UWJyd1K9BM6b9z5cbhJ4gO7d09kbB8jCfOP4D71eTt4lfJeGW3OHXlFyib9v6fFLjOGwg038B1t4xBJ6T8EBvInQ/640?wx_fmt=png&from=appmsg)

攻破它有多简单？咱们过一遍流程。

用Burp打开内置浏览器，登录后正常提交一个“更新邮箱”的请求。在代理历史里找到它，丢进Repeater。你随便改一下csrf参数，后端立马拒绝，看起来防护很到位。

然后右键选择“Change request method”，把它转成GET请求。你会发现，刚才还严防死守的令牌校验突然消失了，数据照样生效。

到了生成PoC这一步，专业版Burp直接右键选“Engagement tools”里的“Generate CSRF PoC”，勾上自动提交，一键搞定。社区版手动写几行也不麻烦：

```
<form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">    <input type="hidden" name="email" value="anything@web-security-academy.net"></form><script>    document.forms[0].submit();</script>
```

把这段贴到漏洞利用服务器的Body里保存，自己先验证一下效果。确认能触发后，换上目标邮箱，重新保存，发送给受害者，收工。

整个过程可能五分钟都用不到，一条CSRF漏洞就到手了。

真实场景里，这类校验疏忽远比靶场更隐蔽，但思路通用。这就是为什么我一直说，挖洞拼的不是工具多贵，而是你对逻辑漏洞的嗅觉。

觉得这招实用，麻烦点赞、在看支持一下，转发给你一起挖洞的兄弟，还没关注的点个关注，后面还有更多实战技巧慢慢聊。

【往期推荐】

[单看都是中低危，组合起来却拿下严重漏洞？赏金猎人都在练的CORS+反射XSS组合拳](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447798699&idx=1&sn=60912627eb65639cbb0c6e6e3a2a3d3d&scene=21#wechat_redirect)

[免费打造你的渗透测试 AI助手：Burpsuite+Ollama+本地大模型 → AI辅助分析，赏金猎人高效挖洞（脚本已打包）](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447798575&idx=1&sn=0636ff98027e96c2dbbec867b59ba8ff&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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