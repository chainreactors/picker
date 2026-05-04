---
title: Linux用户等这一天，太久了--AMD + Valve 终于搞定开源 HDMI 2.1
url: https://mp.weixin.qq.com/s/HMtnLvDqiwXSbfQB8am-ig
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:31:54.728473
---

# Linux用户等这一天，太久了--AMD + Valve 终于搞定开源 HDMI 2.1

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icvDMZl2IHQwMuib6oNbeMib53QGuVV20CdocOJNvW3j6hMCaicOhvHNCYmvRaibUyqLCEMC1OJXYyfNzBjS66gIOBafmMCVOQkDMlWkTkIxFtS4/0?wx_fmt=jpeg)

# Linux用户等这一天，太久了--AMD + Valve 终于搞定开源 HDMI 2.1

梓陌说科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**如果你是 Linux 用户，或者你曾经因为 HDMI 高刷问题折腾过，欢迎在评论区说说你的故事**

我最近刷到一条消息，看完还挺感慨的——AMD 终于要把完整的 HDMI 2.1 支持带到 Linux 上了，而且是开源的那种。你可能不知道，这事儿在 Linux 圈子里已经拖了太久了，好多人早就等得不耐烦了。

![](https://mmbiz.qpic.cn/mmbiz_png/icvDMZl2IHQxjDa1oKos5CnNLLEz7c4ARTiaibHGIoEDibHLhYcrx8zTJd9mFMwNgTLzVCFnlKo2XB6ELNibpSHtZFXyP8lp7ibH1b36CgEIMBVicc/640?wx_fmt=png&from=appmsg)

先说说背景吧。以前 Linux 系统对 HDMI 2.1 的支持一直很尴尬。虽然显卡硬件本身是支持的，但就是没法在软件层面上完全跑起来，尤其是那些高分高刷的特性，比如 4K 120Hz 或者 5K 240Hz，在 Linux 下基本就是摆设。你要是用 Windows，插上就能用；但到了 Linux，有时候连个 4K 144Hz 都认不全，不是黑屏就是卡在低刷新率上。原因其实挺扯的——HDMI 2.1 的很多功能，比如我后面会提到的 FRL，是需要授权和闭源驱动才能实现的，而 Linux 社区一直坚持开源路线，两边就拧巴住了。

AMD 其实之前一直想跟 HDMI Forum（就是那个管理 HDMI 标准的组织）好好聊聊，看能不能给 Linux 开个口子，支持开源驱动用上 HDMI 2.1。结果呢？一开始对方的反应特别冷淡，甚至可以说直接拒绝。你能想象那个画面吗？AMD 的工程师拿着方案去沟通，结果碰了一鼻子灰。搞得 Linux 用户只能憋屈地用 DisplayPort，虽然 DP 也很好用，但很多电视和显示器接游戏主机、播放器的时候还是以 HDMI 为主啊，总不能让我为了用 Linux 再把家里设备全换一遍吧？

好在这段时间情况终于有了转机。最近有个 AMD 的开发者出来透露，说公司正在给 AMD GPU 驱动写一套完整的、开源的 HDMI 2.1 支持方案。最让人高兴的是，这套方案不是糊弄事的那种——它真的会包括 HDMI 2.1 独有的那些高级功能，其中最重要的一个叫“固定速率链路”，英文缩写 FRL。别被名字吓到，说白了它就是让 HDMI 接口在传输数据的时候更稳定、带宽更高。以往 HDMI 2.0 的带宽大概也就 18Gbps 左右，撑死了跑个 4K 60Hz；而 FRL 可以让带宽一下子冲到 48Gbps，这样 4K 120Hz 甚至 5K 240Hz 才能跑得起来。对喜欢玩游戏或者搞影音编辑的人来说，这差别简直天壤之别。

说到这里，就不得不提 Valve 在这件事里扮演的角色了。你可能会问，一个做游戏平台的公司，怎么跑来掺和 HDMI 的事了？其实是这样的，Valve 一直在推他们的 Steam Machine 游戏主机，这台主机跑的是基于 Linux 的 SteamOS 系统。如果连个完整的 HDMI 2.1 都搞不定，那玩家把机器接上客厅里的大电视，结果只能跑个 4K 60Hz，谁还愿意买啊？所以 Valve 自己也急，去年年底的时候，他们专门跑去跟 HDMI Forum 谈判了好一阵子，给 Linux 争取开源的 HDMI 2.1 支持。说真的，要不是 Valve 后面推了一把，这事可能还得拖个好几年。

现在的结果是，AMD 已经提交了第一批 Linux 内核补丁。内核开发者们现在正在审核和测试，如果没有大问题，应该很快就会合并进去。也就是说，用不了多久，你只要装上一个比较新的 Linux 内核，再加上对应的 AMD 显卡驱动，就能跟 Windows 一样，舒舒服服地用上 HDMI 2.1 的全部功能了。想想看，接上电视或者高刷显示器，游戏画面丝滑跟手，看电影也不再有任何卡顿或撕裂，那种体验多舒服。

作为一个偶尔折腾 Linux 的用户，我自己心里还是挺期待的。虽然大部分人平时用 Windows 或者 macOS，但如果你喜欢玩点开源的东西，或者本来就是 Linux 主力用户，那你一定懂这种等了很久终于盼到头的感觉。以前每次遇到显示输出方面的问题，就得去翻论坛、改配置，运气好能凑合着用，运气不好就只能换个接口将就。现在 AMD 和 Valve 一起把这条路铺好了，以后应该能省下不少折腾的功夫。

当然，目前补丁还只是第一步，完整的支持可能还要等几个内核版本迭代。但方向已经定了，补丁也在路上，剩下的无非是时间问题。我觉得这件事最大的意义其实不光是技术上的——它还说明，只要大家真的想解决问题，就算之前被拒绝、被拖延，最后也总能找到办法。AMD 没放弃，Valve 愿意出钱出力，开源社区也从没停止过抱怨和尝试。现在终于要落地了，挺好的。

等哪天我自己的 Linux 机器更新完内核，接上 HDMI 2.1 的电视试试效果，再回来跟你们说感受。希望到时候一切顺利，别再出什么幺蛾子了。

本文基于IT之家、TechPower Up等公开资讯整理改写，结合一些个人理解重新组织表达。

PS：内核补丁这事是AMD工程师自己透露的，信息来源可靠。文中的个人感受和观点纯属主观，不构成任何投资或购买建议。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icvDMZl2IHQydTQRDGPtExIGRaPlrW4XkXyN548qiaIQcJO28nIMaxeIodr4ykgsF6QiaoUT0L2wicMkibfJ0JYeOl24jyaAFibyPTvpcsElTREGc/0?wx_fmt=png)

梓陌说科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icvDMZl2IHQydTQRDGPtExIGRaPlrW4XkXyN548qiaIQcJO28nIMaxeIodr4ykgsF6QiaoUT0L2wicMkibfJ0JYeOl24jyaAFibyPTvpcsElTREGc/0?wx_fmt=png)

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