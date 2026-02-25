---
title: stored RCE？：AI代码审计到底怎样？
url: https://mp.weixin.qq.com/s/ffLjxji5yklNntEBFeku6w
source: Doonsec's feed
date: 2026-02-24
fetch_date: 2026-02-25T04:12:43.001283
---

# stored RCE？：AI代码审计到底怎样？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xILtmngVKHZkhWAUMHpGzYVGm9WRO9bKIcsv7ia1U8efJO4iasBibmJj82bdVsHM8Ku5Kcr1fdibV6xkRzGf7QL6o3icYTSXfuqQhsZY0vYYsXgM/0?wx_fmt=jpeg)

# stored RCE？：AI代码审计到底怎样？

原创

AdminTony
AdminTony

川云安全团队

![]()

在小说阅读器中沉浸阅读

1、背景

最近Claude Security Code做代码审计很火， 而且看完官方提供的zero-days文章以后， 还是挺惊讶的AI的想象力，如下：。

https://red.anthropic.com/2026/zero-days/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHaJ83o2c6d7YMwuwtfMgO5syCZ7BicgptOFP3EoLG4I2oIuKFsiaW8PQj6RGXL1hib8ciaP4u0DM9CzHvRqmsiaQAFJynwWuqZhZ3jM/640?wx_fmt=png&from=appmsg)

虽然Claude Security Code试用不了，都是依赖背后的LLM模型的话，直接用cursor替代会怎么样呢？

2、测试

用之前审计过的一个项目来测试，这里模型使用的Claude Opus 4.6，先直接对项目跑一遍看看：

首先，任务拆分的挺好的，把关键的一些漏洞都做了checklist，单独进行检查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHYQxnzAXt7OHpW0Ssw0706yltuLGcSx1V7l9fTbbwycrtPZL1XnWibG8oib422I342gzq0bkoevs9fMeUpTVbAWxHv3s91mSNWh4/640?wx_fmt=png&from=appmsg)

然后，在过程中，发现如果只用cursor的话，其逻辑还是静态特征查询，然后定位到代码片段进行分析，这点上和静态扫描器区别不大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHYgEpeE3UmWSjpK9icXC7qDHXrgVwBP1d3UTqZNpnHB9mZiaibQ0wW047ps2zkzWZECXugboekibBzDH0NKlfAmQBYT7vq4TFic4DRk/640?wx_fmt=png&from=appmsg)

静态扫描器最大的问题就是污点追踪做的不太好（ps：个人感觉），痛点是扫出来一堆漏洞，但是人工分析成本大，那么大模型会解决这个问题么？ 我们看下报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHaAjKpVZibialASqV0TAKp3DFypReJx3F0iaiaeVMAI45KbGQoflTYwJw9sI5T1bxjcj5ZFBhoQXc57unU9paUEfGbgMZ5F9qpF6cE/640?wx_fmt=png&from=appmsg)

其中SQL注入那几个问题，是之前人工审计发现过，且提交过的，没有新增内容，主要目光放在RCE。

![](https://mmbiz.qpic.cn/mmbiz_png/xILtmngVKHZ8OrrLichXu45McKg7JZGH26HhxdMicCh4erpcqhuMBsuYLUNxibTCO0FI2yu9NbuApR226jRW0qLXksnkgWXelUgWKH8Cv1ALwI/640?wx_fmt=png&from=appmsg)

看到还是静态扫描器类似的问题，会把一些非controller里面的问题报出来（在controller调用到model的时候，可能做了检查，或者参数已经变的不可控了）。

到这里是比较失望的，感觉和静态扫描没啥太大的区别。

3、真RCE？还是假RCE？

接着，让大模型分析一下其调用链，是真的RCE？还是假的RCE？

![](https://mmbiz.qpic.cn/mmbiz_png/xILtmngVKHZ34T0UerOLtqictrOyTO3Ul1MKkQE619KWjMvMb3pmcMcbCc4JZZ1DvD4U33JmvZlTqLMWhKBNE7ibQMH86NTIDrgpXIqEQMVSY/640?wx_fmt=png&from=appmsg)

然后它进行了一系列的查询，最终确定调用链。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHamUW5KpKia5pugUkOVOoicrdk4MGYG7fToicBjtJHmxFXvRjkBM4jQ0ibruOsiaGzziaWVDWuf54W93knSBEuHlk8ibTwCNatibW9bibSc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHacKeSxqX8qxPn6PibLavXDwKW9bGHjyhicyuWC3d5WO9KkiatY7g3jh4Zew5Wg3YJ7wf4wbUSycYWluQfPQRMqnjUFkcH8rtc9N0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHYdCcNJZf1l1KQxCxGIia1abKYkd0SI0h5QibjLn8yhypevibOutI9nIJ58YCJq5vYLSxgdFgD0IEqGpboYKKNvuz6UY65Shv8ibTE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xILtmngVKHaelHaL2n0JALOJdrSX2wPYIVLmAkZ8Aq0xRTGTpgfCKF3SbiaQYQibje1034jMHxBhI5GY4har5ibpFF3Vmh2PwgggSzJ82TVHOs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xILtmngVKHYt3kXJKZmsE7cA0GDVOSMicR1TqTaCudRaV301enFII94GWCkO9tXTOvicwtiaUz3XSuz7AmhppyerGpb57OatRqbiazYFlywLQrw/640?wx_fmt=png&from=appmsg)

完整调用链示意图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHYyejXbgnW0CSRSKsYuP0XDOnF2EiaV4tDGeG85F2LHfnLwaVdFRojxsr0oOMb0iaaDicc2cV3klb6axfvFkVib6Lk7AMVhLN2FrE0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHY2GEdk29aXhTibhmNbHZQWGGM0yrTKdiaQWGUKibgqMiaaibyWSdqAYyT5M4yffTHqAUbdGDuHl2D5pIIOKVldAD0fPTQKMDRH6FS0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xILtmngVKHZfceB78B5Adv5W9Vhk2WLcR2D1P07YRuhicUV2zduxmcy4SY9iaFFG98kFyNrKO9agV6Mpq5fw6dE3ps77W4tWFVJY7cXekWicx4/640?wx_fmt=png&from=appmsg)

调用路径和触发条件，写的清清楚楚的，后来人工分析了一下这个攻击链，确实可以执行。确实牛逼！

漏洞本身也挺有意思的， RCE的输入点和触发点是分开的，有点存储XSS的感觉，AI描述Stored RCE 很形象。

这里大模型简化了很多的人工分析工作，评估了一下，如果人工审计这个漏洞，找输入点 和 触发点的话，估计得2小时时间，甚至更高，但是大模型几分钟就完成了。非常节省效率，而且还把payload准确的给出来了。

4、Stored RCE！干！

输入点：

![](https://mmbiz.qpic.cn/mmbiz_png/xILtmngVKHZzahJDSH8Tq3e8dbrOPiaicAHmCW7fu2WTfRGfcqpSpGAKAfsT206GpuF55OSxLa0NKD9Q7l2owqAsVHcw2nj9ZiaT5zf7w5jutg/640?wx_fmt=png&from=appmsg)

触发点：点开购物车到下单页面，计算器触发！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xILtmngVKHbrDQI6M4iaMnAhiab23CFd8TNiaWBzPNnYaRCxt7d8Eb9VdwibOxrAFCnxn7PoadTibBfr4g5kwicsv9AyZUr5YaxH45Nk7cWIH7eWs/640?wx_fmt=png&from=appmsg)

5、总结

AI在代码审计领域表现出了非常强大的能力，可能Claude Security Code还有更高端的玩法：语义理解、git历史提交记录的对比分析，如果不付费使用Claude Security Code的话，手搓一个MCP、skills或者工作流大概也能实现相应的效果。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BibfH6dHpibZIHYnYEmlhHKFOVIaY7lCfpLAavvIcz1E8nmlia4giccyNJBWJykuKly1DYGJGKwX7gSZACX9xl7ZhQ/0?wx_fmt=png)

川云安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BibfH6dHpibZIHYnYEmlhHKFOVIaY7lCfpLAavvIcz1E8nmlia4giccyNJBWJykuKly1DYGJGKwX7gSZACX9xl7ZhQ/0?wx_fmt=png)

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