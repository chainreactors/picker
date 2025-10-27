---
title: AI 换脸项目 Deep-Live-Cam 一夜爆火：只需一张照片，变身马斯克直播
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653051261&idx=1&sn=0cd9d4012bc29990f62ba52292cb5d01&chksm=7e5724cb4920adddabd309d03ff54d9365712a4787113b4309011fde56866426d1b7e82cc557&scene=58&subscene=0#rd
source: 极客公园
date: 2024-08-11
fetch_date: 2025-10-06T18:03:16.734437
---

# AI 换脸项目 Deep-Live-Cam 一夜爆火：只需一张照片，变身马斯克直播

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5bd6Os2F8PoTX5BLcAFxEhyz1FFTMMiaoDr0J8hbjeaa002Hv4kn4oU7icBQZJ34DqTyEafuYvKhxfw/0?wx_fmt=jpeg)

# AI 换脸项目 Deep-Live-Cam 一夜爆火：只需一张照片，变身马斯克直播

原创

Li Yuan

极客公园

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bd6Os2F8PoTX5BLcAFxEhyXddspZORqhgar57ebfLuwHj0W5KibbEFfld8Q4sghl1PRVDCPlzmricA/640?wx_fmt=png&from=appmsg)

你面对主播可能不是真的小姐姐。

**作者 | Li Yuan****编辑**| 郑玄****

AI 换脸已经不是什么大新闻，视频不再可以完全被信任已经是科技常识。

不过，人类的最后堡垒，直播，最近也崩塌了。

8 月 9 日晚到 8 月 10 日早晨，一个项目突然在 GitHub 上火起来：Deep-Live-Cam，使用一张他人的照片，就能实现在直播流中的实时换脸，而且效果优秀。

直接看外网测试视频：

博主 MatthewBerman 使用了一张伊隆·马斯克的图片生成了直播流，测试了暗光条件和点光源的条件——常规情况下较难处理的场景，但是 Deep-Live-Cam 的表现都非常丝滑，暗光条件下的甚至更像马斯克了。甚至博主戴着眼镜这一点，也几乎没有影响生成的效果。

在测试下的留言中，大家的反应最多的是：「知道这一天早晚会来，但没想到来的这么快！」

**01**

**Deep-Live-Cam**

Deep-Live-Cam 现在在 GitHub 上完全开源，在 CPU 上运行，可以使用 NVIDIA CUDA、Apple Silicon（CoreML）、DirectML（Windows）、OpenVINO（Intel）进行 GPU 加速。

发布者 hacksider 提供了详尽的安装方法，目前 GitHub 上已经有接近 6 千标星。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bd6Os2F8PoTX5BLcAFxEhyWfSichibKU7qjlfURuzibtjc1pqaKPptnHIqwdycRp0x9oJsQhMPMA4qw/640?wx_fmt=png&from=appmsg)

在外网上已经有了不少测试视频。YouTube 博主 Fahd Mirza 直接发布了按步安装的视频教程。

安装完成之后，只需要选择一张图片，一个视频，就能输出一个 DeepFake 的视频——视频中博主录制了一段说话的视频，AI 换脸成爱因斯坦。

而最下方选中 Live 的按钮，就能输出一个直播数据流。

博主还进行了两个极限测试，一个是老虎照片的换脸，软件提示没有找到老虎照片上的脸。另一个是玛丽莲梦露的换脸。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bd6Os2F8PoTX5BLcAFxEhypZxwRds2hwFYrqFOn4njBfsGZJHgyPAkpPwJPpah8MXEQfzVmZIzEQ/640?wx_fmt=png&from=appmsg)

视频效果不错，不过因为博主脸周有一圈白胡子，AI 保留了这一特征，让人脸意外地稍稍有点不自然。

在另一个白人男性的测试视频中，白人男性换脸白人男性，结果则要好很多。

可以看到，视频中测试者手放在脸上，做出夸张表情，都没有影响到太多呈现效果。

Deep-Live-Cam 并不是第一个能够做到实时 AI 换脸的工具。今年年初，Deep Face Live，也已经做到了 AI 实时换脸输出直播流。

不过 Deep Face Live 效果更好的模式，仍然主打用更多的数据对想要换的人脸进行建模后生成实时换脸，单张图片生成的效果不如建模生成的效果。

而 Deep-Live-Cam 中，可以看到单张照片生成的 AI 换脸，在皮肤质感、嘴巴牙齿的动作，这些难点的生成上，都已经相当自然。在操作上，Deep-Live-Cam 的界面也十分简洁，对比 Deep Face Live，看起来普通人上手更容易。因此，此次也受到了更多的关注。

**02**

****换脸直播？电信诈骗？****

AI 实时换脸会带来什么？

一部分人欢欣雀跃。不想用自己的脸直播的人，终于找到了一条出路！

更多的人想到了灰产的可能性：

结合 AI 语音技术——在过去一年内已经发展地相当不错，再配合一个和脸差不多的身体，实时模拟他人进行诈骗操作的成本前所未有地低。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bd6Os2F8PoTX5BLcAFxEhyOINic8DsPlHyaY44twyglgpLyIcGIhoj8ow9eAoANWWD25SRt6ByFrw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bd6Os2F8PoTX5BLcAFxEhyb9sma9AI2XfA8rYUa2wFHn1VkJ0vibODiaDL0ZyTiaCJzFZzoozRaJibicA/640?wx_fmt=png&from=appmsg)

AI 换脸有没有可能会被用来生成犯罪证据？

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bd6Os2F8PoTX5BLcAFxEhyia5ia1h2JqPjiauIOVnm9Qf5nHvCoVRM97ghlBic6QQVVD5QdsynZvAohw/640?wx_fmt=png&from=appmsg)图片文字：我在法庭上观看一个时长 4 分 23 秒的超逼真 AI 犯罪录像，但我并没有犯罪。

而人类最后的堡垒，或者不是人类，而是 AI。

当人类对于 AI 换脸的水平真假难辨之后，人类最终可能要依靠 AI 来分辨视频/直播到底是人类出镜还是 AI 出镜。

Intel 公司，之前曾经推出过 DeepFake 检测器 FakeCatcher，通过检测血流来判断虚假的人脸视频。当血液流经我们的身体时，血管会以非常微妙的方式改变颜色，人眼很难察觉这些变化，但使用光密度测量法（PPG）可以进行检测。

AI 视频本身也有一些只有机器能识别出的水印。荣耀 CEO 赵明就曾经表示，「其实大部分 AI 换脸诈骗是可以被识别的。我们可以通过使用端侧算力来对于视频、图片来判断它是否经过 AI 处理。」

英剧真相捕捉里，曾有这样的情节。AI 换脸技术已经成熟了，但只掌握在少数人手中，全世界都并不了解这件事，以至于法庭仍然继续采纳被篡改的摄像头数据，将无辜的人投入监狱。

令人幸运的是，我们实际所在的现实世界仍然好于虚拟世界，最先进的 AI 实时换脸技术仍然是开源的。作为普通人，起码也能迅速提醒身边的不关注科技的人，AI 换脸技术的最新进展。

\*头图来源：博主 MatthewBerman

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**你如何看待 AI 换脸直播****？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Z5rEl2poJuZqVBGZteWibbvpuA2OibrtXHS6bAJibcYSkxdsV1VicAF088bxt3yluWTQeMyL38W8bfrw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

马斯克：永远不要信愤世嫉俗的人，他们看谁都是坏人。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bY6t6vlgEXpv7hZMzGbcgTJxJfCTUDNbrU6icnQMl1OIiaRCQ5s0AAabox5YhdWPRTMyBatQJPB3zQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653051196&idx=2&sn=30d1b59f47a2e0060268a81fd4e8cee9&chksm=7e57248a4920ad9cad2047bd8c07f22a076ce037baa0ce91299f26be5103003a35ffc00dd1cd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b6znTMB9hEUUe8qh1e2bLtS6ENHialILzjZGgxib6NHKEfL7vKO6vCBtg2TTUTG8ZNTNo4yOK4ffkw/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653051119&idx=1&sn=7985d94af7c26bc79e738a0be058187b&chksm=7e5725594920ac4ff0d1098a0162a1a2b634be03962542ec1105837918d3e097d139ad20a247&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)

‍

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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