---
title: 【408考研-操作系统篇】无需列表快速解决xa0CLOCK 置换题
url: https://mp.weixin.qq.com/s/Pfi1Zzfhf75H-6MPt_omXA
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:53:30.522715
---

# 【408考研-操作系统篇】无需列表快速解决xa0CLOCK 置换题

# 【408考研-操作系统篇】无需列表快速解决 CLOCK 置换题

原创

crackme.net
crackme.net

crackme安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这篇文章是上一篇文章的变体，考研主要考 LRU 置换题，从来没考过 CLOCK 置换题（应该是，我还没复习到真题阶段，不太了解历史考情），但就怕哪年考到这种题，有备无患

FIFO 算法就不写了，和上一篇文章的解法形式一样，仅仅更换一下“缓存命中时的替换逻辑”（缓存命中时不需要划掉前面的）

[【408考研-操作系统篇】无需列表快速解决 LRU 置换题](https://mp.weixin.qq.com/s?__biz=Mzk3NTM5MDA5MA==&mid=2247484144&idx=1&sn=a83a2b4bbe6539644e8ef085a95e32f9&scene=21#wechat_redirect)

本来就是高度内化的方法，让我解释出来就相当于“用意识解释神经线路”。然而可悲的是，我的元认知充分强大到能让我意识到这件事非常复杂，但却没有足够强大到让我能如鱼得水做到，导致耗能效果还不好（比如这篇文章，我猜你一定看不懂哈哈哈），所以还是要自己悟（）

# 例题

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kGhLgo0BUA7aKwHILTsnUguAyJjtJU9kicMIb6AGUCiadCdWBZYdMqXvZNDfB7baTE8GnpYa4vndEIzqy7cwwXNbIiatN8eLUZynEoq8aYy5s8/640?wx_fmt=jpeg&from=appmsg)

> 页框 4，访问顺序 7 0 1 2 0 3 0 4 2 3 0 3 2 1 3 2，页置换算法是 CLOCK，求缺页次数

快速解法：

注意：这种方法是“错误容忍”式的，所以可以写错部分草稿，依然能得出正确的结果（我会标注哪里允许出错）。所以，不需要再消耗大量大脑带宽拿来检错，节约点带宽专注于题目

1. 1. 访问 7 0 1 2，缺页，下划线标注

![](https://mmbiz.qpic.cn/mmbiz_jpg/kGhLgo0BUA7cgYhWJbNfVcCx8qMzUw4iaibtlAxYp1Xxvqz9iaJWAiaJEBEOoaHDg7eekfE4Sy8RwZcbE6JLaH5NAa8nnYheT6YpEoZzib2z59N4/640?wx_fmt=jpeg&from=appmsg)

2. 2. 访问 0，不缺页，跳过
3. 3. 访问 3，缺页。以最后一个写下划线的页框为起始，向右循环移动，经过访问位为 1 的页框就划并标记访问位为 0（还记得刚才说过“错误容忍”吗，这里我就没划，而是直接标注了访问位为 0），直到遇到第一个访问位为 0 的页框并替换

最后一个写下划线的页框是第四页框，所以循环到第一页框开始移动，循环一圈，替换第一页框的页面

**“错误容忍”其实指的就是：只要能正确区分访问位，划不划、写到哪里，都无所谓的**

![](https://mmbiz.qpic.cn/mmbiz_jpg/kGhLgo0BUA7FVFpAibuxcYRkicwmhC8fs9DibZom5DmyhQcTiasU6oRRsibw1cSqvSKZUicn2zJlJoNrXbKGupiang7WKfjMxVx8BKonmG1MqEe1QI/640?wx_fmt=jpeg&from=appmsg)

2. 4. 访问 0，由于 0 的访问位是 0，所以划掉第二行的 0，使其回到第一行

或者充分发挥“错误容忍”的特性：第一行第二行的 0 全部划掉，在第三行写 0，因为第三行访问位是 1，怎么样都无所谓的，因为能正确区分访问位

![](https://mmbiz.qpic.cn/mmbiz_jpg/kGhLgo0BUA5ITlLiarDic3BTICzsUq0BwNt0jVVDKf7Fz5dpQ70Nd52yHm3ia0THB0IvOHelvI4rbwG5rmT2J8cxzk3ibpticRb9rq4PfQqJkbV4/640?wx_fmt=jpeg&from=appmsg)

2. 5. 访问 4，缺页， 最后一个写下划线的页框是第一页框，替换第三页框，中间的第二页框访问位标记为 0

![](https://mmbiz.qpic.cn/mmbiz_jpg/kGhLgo0BUA6v5TTKdA0Imibqp0lEH7bkWheblIYIRK0miaucvV8Qg8o8DC2WbmaDpqEfzZaU81gwor1Ml0lW4bUx59pQL8ISgUPvkyYuzwtR8/640?wx_fmt=jpeg&from=appmsg)

2. 6. 继续遍历，直到缺页，也就是访问 1 时。同理，最后一个写下划线的页框是第三页框，转一圈替换第四页框
3. 7. 直到遍历完全

**草稿有误**，最后一步的 2 缺页，应该写的比 1 更低，不然就区分不出来最后一个写下划线的页框到底是哪一个了。**但是我懒得改了，当成“错误容忍”的错误使用例吧（）**

也就是说，如果将要写下划线的页框，比现有的最后一个写下划线的页框更小，在纵轴上就应该写的更低

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kGhLgo0BUA7VGg6uc5TJiccCQfTIJSsUmmmOoeWEBdCuggRO0LrhDviahYPW8fKsaHsS7gdyuEFaGATprqMPIo7qeUanatgfgCdiag1Wv9DeiaI/640?wx_fmt=jpeg&from=appmsg)

最终，缺页 8 次，四个页框的页面分别是 (3, 0) (2, 1) (4, 0) (1, 1)，如果此时再次发生缺页，应该替换第三页框

还能回溯，比如题目问“页面 7 没有在第几页框出现过”，那很明显 7 只在第一页框出现过，没有出现的页框就是二三四。或者，页框一只存储过页面 7 和 3

由于“错误容忍”机制的存在，这份草稿仅供参考，你让我再解一次都不一定能写出同样的一份草稿

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f2j8DeXVicRQ9KGpr3vDNkdIwyasHFEWCmJibCSicITuAqbVgkygYicev0lUCVEj7B2XfSpnEhs6o7mVylZW5gzorA/0?wx_fmt=png)

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