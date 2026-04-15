---
title: 最大程度获取网站JS的工具
url: https://mp.weixin.qq.com/s/86L-SsuqO-0uatIGoQbrxg
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:40:36.422018
---

# 最大程度获取网站JS的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVl5xmEyCnNFfZOic7dsKSj45rpKO5vSTvoia6vrIhdcojrlZpR8ytib2K2H0cGOfR04kf1RONYWsZpAjzZKRAbwBxIPaeqPnodOmQ/0?wx_fmt=jpeg)

# 最大程度获取网站JS的工具

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 185，阅读大约需 1 分钟

## Webpack\_extract

chrome 插件
https://github.com/xz-zone/Webpack\_extract

![d82d153c90d5bfbaaf0120b44eeae5bb.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkhdBq9J2kTtW6aqyVteibw8cHNnLJnibvSUQmAssicubU1XZ086qaZkrlpx0QNt3uK4Ney1v4ZG7pPoLNwYTTBic4ydMdbyWxyfMg/640?from=appmsg "null")

d82d153c90d5bfbaaf0120b44eeae5bb.png

自动化收集js，自动化加载js，自动化分析js

提取映射
![0f39f04e38a53b381f0d522a51b054c4.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkNI9qM72ibl0XBIXWfUIvEmpAJoibPWI44pnSPkjibh6uexxnicVIYgRYNk6HyMYKZmBqQ4mJQjDF2V8ywpmmgMUkKWjOJYl64Uh8/640?from=appmsg "null")

0f39f04e38a53b381f0d522a51b054c4.png

当前Source当中的JS数量
![babb2846f9e4eda7ad73b6af254b5fc9.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnyiaBzF6ydZvWouz7ph74icibEaxTNPSPxj6WytJDcdJ8dWMgun5Nh2YxUpqfFC6uIvtPu7D0H6svKwfdg5QHbcpbXebhaXqMbpM/640?from=appmsg "null")

babb2846f9e4eda7ad73b6af254b5fc9.png

可以看到，动态加载JS也成功提取

![7caa3860f172de69a18b02754a4dff90.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnPOZ4dRLodDGKfRwRmrnaCkicP2w8jtrI038YUtuMSsVPUUW8mQyShQFcFQq2PpvPH7mUVvw2SkcCKWQUAheFncdbUoGe3dTxU/640?from=appmsg "null")

7caa3860f172de69a18b02754a4dff90.png

## Packer-InfoFinder

项目地址：https://github.com/TFour123/Packer-InfoFinder

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkemjoCDh6ibzeTe0Qc4BeMpoJxcrKv4On494Ap6cEtzxos7mQg21GVXblwYNFoAKMFTaiaF4TLpAhLpmxfw6hMbHSkbZGQEoVcU/640?wx_fmt=png&from=appmsg)

Packer-InfoFinder 是一款专为现代Web应用设计的自动化安全扫描工具。它能深度抓取目标网站的JavaScript文件，智能还原由Webpack等打包器进行代码拆分（Code Splitting）的异步模块，并利用强大的正则引擎扫描所有JS代码，发现其中可能存在的敏感信息，如API密钥、内部路径、凭证、个人身份信息（PII）等。

```
python Packer-InfoFinder.py -u "https://target.com" --finder
```

也能提取
![e0fba090d4340498fd090f9389ed5a70.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVk5KtJ7vuODzUaE3pb9KRR34ZlN5ibMyrllicpYP2GOHXhIFHJmyXH9tfK55tRQicic1Nd9ToPwX66W8qbibeekqeASGbIN49ZPricXw/640?from=appmsg "null")

e0fba090d4340498fd090f9389ed5a70.png

结果：
![0c8ee89de14b5df021011b961930448d.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmEazLmyGAjwnU1SdNibxurvZul1pR97kcXrqLZhciapaO8eDLLSapBP7dpWvVRlNAYeiafEG8fIQegpUxeDKBRaCPxZDcbXEZrXs/640?from=appmsg "null")

0c8ee89de14b5df021011b961930448d.png

![8ab21d1618c37ee94aea7939cb152013.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVk4IbOK7Ng1MibYkqYc44iaBEwHxTtlAmNrVdERznSmquSMn0B2uJWCyaFRWKDTTwicuVZpN8BdvCV8CPlXqpqO9giafqkV32pN7ic8/640?from=appmsg "null")

8ab21d1618c37ee94aea7939cb152013.png

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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