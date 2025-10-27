---
title: G.O.S.S.I.P 阅读推荐 2024-09-05 用PDF做点坏事
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498814&idx=1&sn=bd3fba594bf73147a5f0b8daf2a7d39b&chksm=c063d2e7f7145bf112104b874c2369d0d4baf15cd7346d6957a4a80d9854ff2e452d748550fb&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-09-06
fetch_date: 2025-10-06T18:27:28.806787
---

# G.O.S.S.I.P 阅读推荐 2024-09-05 用PDF做点坏事

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HafBhQ9jDic14ZRrTHqjm2tOXT3Vs7pfKnlXXaOsfc1JKRQrknhqa56dxbB8eIESibsPzEtcqQlsZg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-09-05 用PDF做点坏事

原创

G.O.S.S.I.P

安全研究GoSSIP

海内存知己，天涯七比零。听说CCTV拒绝直播国足，做了件好事。我们还是多读点书少给自己添堵吧，今天就来介绍一篇教你做坏事的文章。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HafBhQ9jDic14ZRrTHqjm2tgoO9JJ8NLoM8xh8ibO87OaxWhnkeia3icE0q84iacNeho5zODAeTuQpmJw/640?wx_fmt=png&from=appmsg)

还记得我们在今年春节期间的那篇文章【[G.O.S.S.I.P 春节总动员之制作二向箔](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247497277&idx=1&sn=28aa44f01ce7f048a7c2a9ddb3cd9f06&chksm=c063d8e4f71451f262b34c0b3816511903448e9c46ff1005411faeea030c9f9f938b849ae3d3&scene=21#wechat_redirect)】吗？PDF文件格式里面可是藏了很多玄机的，今天我们介绍的这篇*Hacking With PDF*传授了一些入门级的破坏技术，比如在PDF里面进行XSS攻击。说到这个，不禁想起了很久之前在Adobe Acrobat Reader里面的那个问题：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HafBhQ9jDic14ZRrTHqjm2tp2ZcdmrxJtJNBseQnD6C33M28BdndV4XHvicWiaUCNA44sRlwl2G68aQ/640?wx_fmt=png&from=appmsg)

所以这篇文章里面的弹框警告只是小菜一碟啦~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HafBhQ9jDic14ZRrTHqjm2tQpWZcPNxH11eWd89HHlgkKE0E8dIDk93dRF81ah1XfOulnsz60PJUA/640?wx_fmt=png&from=appmsg)

当然你也可以利用一些第三方PDF viewer的漏洞，比如利用Foxit Reader相关的CVE-2018-9958，来在你的Windows系统上启动一个shell~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HafBhQ9jDic14ZRrTHqjm2tV61ibY3y6C3CEnm9LyiamkgnULOszp7Jf4sTHs7SHohCq3qVByANyP6g/640?wx_fmt=png&from=appmsg)

现在都要讲道德，文章最后也介绍了一些PDF的解析工具，能帮你在打开之前进行一些安全检查：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HafBhQ9jDic14ZRrTHqjm2t2SMYCaibVFylxhUGeB5mNknml5GDblUyITNiaPzcN1MM2a4yibaJ9UM9A/640?wx_fmt=png&from=appmsg)

当然，最后作者还把所有文章里面介绍的（恶意）PDF都放在GitHub上供大家下载了：

> https://github.com/0xCyberY/CVE-T4PDF

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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