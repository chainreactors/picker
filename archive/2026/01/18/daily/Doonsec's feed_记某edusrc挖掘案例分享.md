---
title: 记某edusrc挖掘案例分享
url: https://mp.weixin.qq.com/s/_CbIWcnrEE9VQEump0ctnQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:34:48.625085
---

# 记某edusrc挖掘案例分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlk3P6orF1cF4PCpKPYibpaKRqbJnKkRibNUnlXMeN2ehfwaickSYY2KKrg/0?wx_fmt=jpeg)

# 记某edusrc挖掘案例分享

原创

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

某站点组合拳挖掘

```
信息收集之后，发现登录框
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtl6aD8xnO4YUXicbPcp9E8QRdIWYrSN06qMW9esa3QP26PALKMz3MRbEw/640?wx_fmt=png&from=appmsg)

常见登录框测试思路

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtllRBQMydURibZ8jzfWT2O7TfZaFqITPoLIALRHMm54snnqjGHQVgGkhA/640?wx_fmt=png&from=appmsg)

我们直接弱口令admin/123456成功进入后台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlCxKIPNFagialGsopypU6Iibp9jIX30qSblqJZ3rfy0blzaic33xS3DUHw/640?wx_fmt=png&from=appmsg)

进入后台先找找看有没有敏感信息啥的

在个人报告这里泄露了4w+

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlVSXNXXEZ30Jc9amh5uxECwBsvpCJapka7Y327A4pE4vYIhC96T3pRA/640?wx_fmt=png&from=appmsg)

然后其他接口接口也泄露了很多

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlS37mUd84xsm5WtAEwu037yNtuVI4VEVgvGjdchRbVicbvBY62vyCv1Q/640?wx_fmt=png&from=appmsg)

可以看到有id抓包进行遍历，我从1-9999都遍历了一下，最多的有6000条，少的也有1两条

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlQHLyoTvIjF1kYoVKKia0b3Fk2mkHZaSzQBgNaGvtMOS2sH4jat79Kag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtl0VSt3PjibLIhNCwiaSiaMRvXAGQjlCgrjyukKGcD6RROibRSVgmFmlZxIw/640?wx_fmt=png&from=appmsg)

累计泄露了至少十万+

之后挂上xiasql插件，进行点击功能，看有没有注入，这里注意，挂上插件之后，不要点击，增加删除，之类的操作，不然会出问题

尽量多点功能，让流量都过插件，几分钟之后，整理发现结果，一共有7个不同接口的报错注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlGGicqJhQxFQ0HIvBjsmvIruOIT1so8pIJbvSqXCSIM1LKQuvD9dNmjg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlHSMBI6WPNJVpZxibbErgrHIfBLSdZbeq6ndkncNvQAFAkRicvzbXicflw/640?wx_fmt=png&from=appmsg)

sqlmap效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlOqxdx0mSNjbV8qogenAHc3lyqKcoqQGPXeAhuTtaW9Z7Jsribvwwruw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlDUQiakqIHvg5u8NVxNibOYLG0kuBiciaYXPBOT67GOBLKVZ5iarzvgiaF3nw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtld3Ch4sZvWiboTBBHovenD3cfY8DY4A2FGH7DPmZSckD7C0ib1UYRCLUw/640?wx_fmt=png&from=appmsg)

其他也是同理不在一一展示

后面针对功能继续进行挖掘，后台来到测评任务这里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlm1R2c33IcWBDqibRfl1EhJcYhWqpB4c0hXNS0mNF2ndnZMibyV9Y1xkg/640?wx_fmt=png&from=appmsg)

点击更多然后导出人员名单这里会直接导出用户敏感信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlYVNJykeOKMyyY7mrpYKaoJ7tpXcsfyibtpjh8dUa0w0ILwuKxVANwEA/640?wx_fmt=png&from=appmsg)

导出之后进行查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtleC9gyhX4r5ibmKzVlkA4HnWwEEQgHvzSLuOyJdA98gQtrY8CbMgDlFw/640?wx_fmt=png&from=appmsg)

针对导出功能，越权和未授权问题居多，我们是管理员重点测试未授权

测试方法

直接复制下载链接到没有登录过的浏览器进行访问发现可以直接下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlf5lHwPSicHoeHSRRM5QJciapwWZ5APT0YWsSQbgXKpBykMHz7xzt7Snw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlxTjnSmbxzrSyBeImMuEhlFwsMbwpLia4egfunQGtDTfwTqFWuibRvrNA/640?wx_fmt=png&from=appmsg)

看大小依旧数据满满

后续通过浏览器插件，发现是tp,直接使用工具进行梭哈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlErqNjaP97ejvbt8wibLY0icaKHoBXvvuul0VjBaYHibJNcKdIt8MBrQ1Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlltRGeS4BJtwxAaibnmBpHxxmUvzt2kmYvY2JE6x3icrDaGx77vksdglA/640?wx_fmt=png&from=appmsg)

发现存在信息泄露

直接访问可以看到网站根路径，如果是没有注入的话，可能是个水洞，但是如果有注入且之前我的用户权限是root可以尝试使用mysql写木马，但是危害等级达到了，不在进行尝试，点到为止。

后台回复加群加入交流群

有实战需要可以加入小圈子

主要内容是（2025-2026/edusrc实战报告）其他内容无需多言

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO5YDCWWqcKCRI4sweub6vtlYqJyN5SEwk5foMym6qzstLasBJO2d4Hxckicd7Wnibkss74YG142VzkA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

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