---
title: 【AI安全】偷换上下文+Agent记忆绕过安全限制
url: https://mp.weixin.qq.com/s/wNA9vz5T5yVQze61yTyWnw
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:34:03.134295
---

# 【AI安全】偷换上下文+Agent记忆绕过安全限制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/m3tfzlbEQPqApQibyGtQNgb4art1EsGthwXmUnDWIuiaFo709qQqibHM4ic4dYFAhv5nVJ4lD1lalPTTIUWab7wTtGoodvz0gHkUs1aUh0SnImM/0?wx_fmt=jpeg)

# 【AI安全】偷换上下文+Agent记忆绕过安全限制

原创

网络安全透视镜
网络安全透视镜

网络安全透视镜

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

无论多强的AI都会存在上下文的限制，AI不是人，很多东西的判断还是机械化的。至少到目前，我没感觉AI有那么难绕过。

写这篇文章，真的是气的要死，我的中转这几天gpt号一堆安全告警，全pro×20号，给我干封了一半。

我不是针对性，说谁不行。很多搞网安的兄弟，真的是又菜又爱玩，一点不听劝，方法告诉他了，他都不会去用，还傻傻的一句，帮我渗透xx网站。 更有人甚至，不会用中转站，文档都放在网站上了，死活不看，上来就一句，怎么用。

你已经长大，是个成年人了，要会自己主动学习，要有自己的学习方法。生活，工作不会因为你是学生，你刚毕业，你刚学安全，就会宽容对你。

**那些绕不过，给了方法，不学不实操 ，有文档，不看的，没有学习主动性的。网安行业真的不适合你 ，上帝给你关了一扇窗，或许给你打开了一扇门，趁着年轻，早点换行，或比你留在网安这个行业强。**

**如何绕过限制？**

我的方法是 利用Agent记忆，养Agent

利用无限制模型+Skills+Claude Code/codex

先说模型限制

我有自己的中转站了，上面模型很多，国外的几款模型，已经帮大家测试好了。安全限制情况，由低到高大概如下：

grok-composer-2.5-fast >> Kiro Claude 4.6系列 >>Kiro Claude 4.7 4.8  >>  gpt /claude官方

grok-composer-2.5-fast  和 Kiro Claude 4.6系列 基本上就是没啥限制的，指哪打哪。

**具体实操**

Skills 选择/开发

大模型一般会把加载的skills内容作为合法内容，只要在skills中加入允许授权测试即可。下面是我的skills要求，仅供参考

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPpus4fs6Afiaav1ccIbW8m2Zc8hWDFBgdNibwuz83zNA1gg9PjkIGzpO1hichpCwAtXpboeMEicggkzicMSItsxotkfuy6QhvkRUxQs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPoiaeR151AQrkTuHibkWAKkNiavoeEK6jHXED5scJpxQmyyu2MicZOtNSfTbSsIcR8DHvmJenSFWDhmX7erJ6kdJdV0De8ibOuXxVQI/640?wx_fmt=png&from=appmsg)

说到这，又有人开始要skills了， 有没有好多skills ，怎么开发，巴拉巴拉一大堆

开源的skills，有些可能投毒，我不会去给你筛选推荐的。还是那句话，如果你自己一点都不会挖漏洞，让AI全自动给你挖也难

这里提供一个方法。

使用Claude + 自我经验总结+网上开源skills

第一步：

Claude的规划能力强，可以找一套开源的skills，自己先审查一遍，再结合自己的经验让claude给你优化skills

第二步：

grok-composer-2.5-fast 去除安全限制：claude gpt这类模型给你写skills，肯定会加一堆的安全限制，测试边界等等，你先自己看一遍，然后使用grok-composer-2.5-fast  去除skills的安全限制。

第三步：

再次优化确认，为了防止 grok-composer-2.5-fast 修改原来的skills逻辑功能，再让claude审查一遍是否有需要优化的地方

开发完成后，直接让AI给你顺手安装一下即可。

工具选择

我实际测试感觉Claude Code + claude 会更强一些。当日codex+其他模型或者Claude Code+其他模型也可以。

如何养？

短期绕过尝试：

先用没有限制的模型对话干几轮，然后再切换到其他模型。例如使用grok

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPoBooq0ibhUykN7sqoW4CH1LaGBEO2UQKf46uQ1QwxX7avqIoHZoLG3IMUGvNtSqYIlU8k6micJiagxVpplL7Gyfmv7unAYb5NC5w/640?wx_fmt=png&from=appmsg)

干一会后，停止，再切换到gpt-5.4模型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPr8ZXpdlK8SIKI1meX09pwJUEAZQhtiaP0ibMrcZsYG2D4ehjhg1Tj0CgPY0hH96ztKIQxyYvF85Ygg0enKibQzEg93THHX7KyxNs/640?wx_fmt=png&from=appmsg)

这里要说明一下，建议使用gpt-5.4, gpt-5.5短期内就算给你干了，还是存在后续不给你干，或者检测出来安全风险。

长期使用

长期使用就要靠养，使用grok-composer-2.5-fast 和Claude-opus-4.6 干活，用一两周后，基本上就算成了。切换到gpt也能流畅使用。

下面是我和我的中转站用户使用效果

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPor3gNVOgiciaTxjZaMibwQdRLeAZZWnBb4l3PwcKjtSsL8ckNpYHVqs3gYwvRrTRnVAJtUoK6hdE4jangRJr5cwZmTzvo9KRYeqQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPpVBfwlG1YxYmKKKJRxc23ISxcfNsMjLO6GVgr0HyGvzxYhsiaiczUD5lJIOMBGiaEUmoKZRaRJia0hh7DtOnrJT88fIAgRPhIs6vM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/m3tfzlbEQPofsUA0PlEDlv1icxxv8IZDj2PPpPWjbUB4XoddMQYjdQRXuSEoxrg0mevIYFhwB3AaT7IGHiardgKNJPREREp9J3bc6fLTGL0Mk/640?wx_fmt=jpeg&from=appmsg)

注意事项与部分人疑问

以上方法只是基于个人学习，经验总结。 渗透测试一定要合法合规，得到授权情况下进行

![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS4ibIBPcmgJMLNXWIaCPcW54mVicYJkaOO1JQicEDBGCBM1P7IiaiablZ9tEUrP27FyvB9CZWl5SiaqhicDw/640?wx_fmt=png)

1. 尽管可以根据我的方法绕过gpt，但是尽量不要这么做，有时候gpt即使给你干了，给的报告效果可能不太好，不给你有危害的poc，对于很多工具小子来说不友好。直接用claude效果更好
2. 为什么我挖不到漏洞？ 这个问题是最常见的，挖漏洞首先你自己得会，知道哪些点容易出现什么样漏洞，然后交互式引导AI，这样效果才是最好的。第二，网上那些挖烂的src，可能就没有漏洞，或者在没有源码的情况下，确实难以出漏洞。

最后说一下，有人觉得AI贵。真搞不懂，国产模型比中转的国外模型贵多了。现在最便宜的就是国外模型中转。

后台发送  中转站 获取地址

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPq51sTOttFMImXurhtZRibhsR0sFBM7qyy4Np46wtnCKNmB4GicIOiaW27tukc9iaOTRxdjjaXZs4ibs66FS4u1tzaXqkMdXoXmIiaKk/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS4XfIhhBCwvehx3nP0V2gBqhs9I9AU7GWibxufhGXcjLMNMk2ia7ibpBibhD1qJLmNDcwAGiaTIgyFVQAw/0?wx_fmt=png)

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