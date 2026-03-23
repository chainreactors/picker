---
title: 记edusrc社工配合默认密码身份证后六位简单突破统一认证登录
url: https://mp.weixin.qq.com/s/7ymKdj84PvGyBPqWNFQ8Mg
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:22:32.674695
---

# 记edusrc社工配合默认密码身份证后六位简单突破统一认证登录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboT9RgIgDc3EgyhVHoXEU7NBibunibvBpFkcJXCDSILaiabHTjlVM6716GUwEHLbRq8pcZlZ7h9BhqD5icFMD4Sx6VrTibYZtrQC8vdo/0?wx_fmt=jpeg)

# 记edusrc社工配合默认密码身份证后六位简单突破统一认证登录

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

前言

巧妙利用信息收集快速突破统一身份认证登录（得有狗运）

信息收集

```
body="身份证后六位" && org="China Education and Research Network Center"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSgr1OGaJ1uhNKtDqkqlpKuY354qnCQuvutkGlKjcRc85ebkAWGJBYRrMickuNNjiaSey8eibnjgZMFGWtvhRXrGcaK6VficoW7KCY/640?wx_fmt=png&from=appmsg)

会发现一些这样的站点，都是身份证后六位作为默认密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQMkib1WruZVsrHLiacpZsX7ayIZ8AeVIko7vZNhtK4DYgzfvDcOLynBAcqkccRPZVZnyrGHFtrK9ibfhwGsBFbiadj5JqN9Cib4qDU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRBOohia6ibQe0oEQ8FjHvTflc4ZqfJdtoicwUKkh3FkFGibkFMga02fdSKbh9PLW4AXQ58icXTgEmpQGI0LgD0szzhicicy7yZaXySbM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR65LmibBqptIyJHaBHib6DPDUtQCR21SDMfHV88WYQQuySWTsU7ibLbyHIIHw6xedn9nkbFpX3CCA4HOHc2Eu5uiaMqcica1ibibdqUI/640?wx_fmt=png&from=appmsg)

然后就可以去收集对应学校的身份证学号信息等

我这里以某个学校的统一身份认证为例子

信息收集到这个页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSyJc1fgSibGsUicBYKDvSno2X9dQ1vV5N6BBpH8wQblNibCzT2Qbxia2dKhqLiaC9gx5QnwoONLQyYkQgCbzhJA3NlG22mPs1O3Oko/640?wx_fmt=png&from=appmsg)

点击登录说明

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRT62SJEmzF49r3LwAWtskhW9kooicDKRrbTn4BKmynw5sicSO0KovPSouE4BV5hcsv09dv5qL9YOowYzuNwxmByaUdSwJd4XYSo/640?wx_fmt=png&from=appmsg)

可以看到这里默认密码是身份证后六位

我们直接去抖音，快手，小红书，贴吧，google语法等

你各种能收集到身份证地方去尝试

我这里直接构造

xxxx学校录取通知书，去各种平台搜索

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSUcYT8mmHM9lXVZDSMfW6oXzYW1kE6Pd08wzFicicajUPoCSAxXKxicfsW9yFP0HBZdmUo1yz8LvibBLDf2CWW5BurTLNRuzAZS7Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQbnU6t6OdEwrHeUXEpTZvrSJJ6RUicsbI53Qib0u6LchWCmgnnFPRfeL64A2fTR6Gjw6vCSMMrlia02uOG8JGBh7zTShicrsC7qHE/640?wx_fmt=png&from=appmsg)

发现很多截图证明一下

接下来就是找学号

直接使用姓名

site:edu.cn 姓名

site:edu.cn 考生号

发现学号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTS8kxL2kvYQbcXbRBoiarFYezZ4ID8qCV48nX9nibRibOyQjhibMojpcfibaKGUdKFBjcoKOUYxka0FXITgozx8UnqmNNDejnLiajGg/640?wx_fmt=png&from=appmsg)

使用学号配合身份证后六位简单进入统一

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRCoVq2NUdG2AribrnmEsb4IMapaVtstU5yqnsw8xt4IaMVBJbKTsPFyiaV1LNb9jYiaPV2Yibp9RvMFkKcg0a0hsWdiblDtbF6SFmA/640?wx_fmt=png&from=appmsg)

然后这么多功能，漏洞不是随便挖

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTA4YC0Lg1Q0akrMcetuw3MRer9CIyGqpk5XlibKZ2SHWRh6RJPXqoKqZ6orV3ex9Pz0kPHxGhia1h1hNWmTWsGprGfvVrQenUGQ/640?wx_fmt=png&from=appmsg)

配合功能以及数据包结合思维导图的提示，这不狠狠水rank

如果真一个都找不到，直接找后台有sfz信息泄露的点

配合弱口令可以水个低危

案例2

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT5GtX7p4l51LWpVcOSC82L7ctoMrd2NonCGTw4FKicPQupYBcY0krWl3GeicmrTEMcLDbRhs6mQicINSiahWm25fkYv3YJPzTY7Bc/640?wx_fmt=png&from=appmsg)

这个更简单

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQKPIZVrbj517Ra3NmfCC3fpaffvsAiah9zLFeazia5brePBVRTVEZBFvVvGu5WbGVq4grAOoLqQ9mbxRy6NIM6z2cPdAOvE1fp4/640?wx_fmt=png&from=appmsg)

录取通知书直接有学号和身份证号，一键登录即可

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT8uv7b0MQKsfAqoDmB2KujWtxjdnqDMRk5eTcWZV1kXnetu7iblRrl5cCfZf6ia8XlWJOncXgK7QQgICmnRjzhVibC6K9P5STCAI/640?wx_fmt=png&from=appmsg)

思路也可以扩展比如默认密码是学号工号的站点

后台回复加群加入交流群

广告：  cisp pte/pts &nisp1级2级低价报考，货比三家不吃亏。

陌笙安全交流圈子+陌笙渗透测试知识库+陌笙安全漏洞库介绍 （加入圈子送知识库+漏洞库）

如果觉得合适可以加入，人数满300人，就没有5元的优惠券了，目前价格只需35元，圈子的价格只会根据圈子内容和圈子人数进行上调，不会下跌![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_64@2x.png)

圈子福利

**漏洞挖掘1v1指导,我给指定站,你测试之后出报告,我根据报告总结你不出洞的问题,以及看漏洞点和总结，当然你可以自己找站，我来帮你完善总结思路。（不包过，思路为主，主要针对小白，大师傅就没必要了，主打性价比，帮师傅们快速提升，挖到第一个edu洞。）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRy4XkqZv1icZQh41ZFvHgGCNHYWpn9kL6ScT1QR9S70kDzbh2NWK2RU8GeHMrwiaibWGYtbH7UXPFVy5GVq6ia9v27EMRic08FnJMs/640?wx_fmt=png&from=appmsg)

陌笙安全知识库介绍（内容在更新中）

```
SRC挖掘基础CNVD挖掘EDUSRC挖掘公益漏洞挖掘常见工具推荐&用法内网渗透红蓝攻防代码基础学习代码审计0day&1day&经典Nday复现内网渗透AI&&云渗透APP&&小程序渗透免杀&&WAF绕过hw&&渗透安服面试优秀文章推荐某鱼网安资源分享等模块
```

总览

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRQicyhMcmxjnjsLK9IpBRq6lCKmJhkZfTjKO7B22rrCgLffSKDh5iasN6uA1NUTIzu0rJS7libnyJE66dc6FUDDjKlVj1GN4ps9Y/640?wx_fmt=png&from=appmsg)

src挖掘模块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTNqXjA6Yt2BSOjW0NK8ciak8PCqXwpNzygBjUIWSzibHLeXmSQZNZUSp2BHcZIdI38vW6pOzZgDCNhxRiafZsWyPkxyWAg4OUVjg/640?wx_fmt=png&from=appmsg)

陌笙安全漏洞库介绍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSuHeiarsjWEoNZ7AnCAURuZnhmen71rf13j2W9phYKQP3Xbv07sia3SRAL7TH0kOsdQsCUTxZWHIesyiavpkhiaibgOq1ficrGG5Y3w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTmVRgFTibOSyBlpcJuEm7XibolB08wRclibvzDfqqETat3tccCSgC1lPHcEziav3EN8rfh6yvAeCe0acEeHZ5WsUN7LpwIfNodmf0/640?wx_fmt=png&from=appmsg)

圈子介绍

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&视频5、不定期分享通杀、0day6、有圈子群可以技术交流以及不定期抽取证书&免费rank7.分享各种护网资料各家安全厂商讲解视频&精选实战面试题目8、各种框架漏洞技巧分享9、各种源码分享（泛微、正方系统、用友等）10、漏洞挖掘工具&信息收集工具&内网渗透免杀等网安工具分享11、各种ctf资料以及题目分享12、cnvd挖掘技巧&CNVD资产&src资产分享&补天1权重资产分享&fofakey共用13、免杀、逆向、红队攻内网防渗透等课程分享14、漏洞库&字典以各种内容不在一一说明15、cisp-pte/pts&nisp一级&nisp二级&edusrc证书内部价格15、如果有漏洞挖掘问题或者工具资料需求可以找群主(尽量满足)
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQLW5X2q5ibOoTBfZeBTd8b8fCht2b9CSdmibG305NblA0TPI3kg3D8K02iaPBSEU3zpicppUFr1KrMuCWtpRIOiapFrl5J0HLV1vY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQHxT1ELI2BOHibhTiaXjMQNWGyZKaCrnXpIicOllIFicx5cbdBVia0egwycXMMAkhSmwVUbJm3XpAfF411XPg8WsH4yB96BM78DMdM/640?wx_fmt=jpeg&from=appmsg)

目前530多条内容，扫码查看详情，持续更新中。。

如果觉得合适可以加入，价格不定期会根据圈子内容和圈子人数进行上调

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSYymsw5ibS2Ha9KN0q9z2paTZ3L9H75lJxg8yNLrB3uHX5qOa0Q6DGeOCFY6W55kibLKQP6sic0vGJIh56UvQPZzvR0HKWCFjC4I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQWWsprmriaicIkJiar69Sicf7ngjqfEQhfib3AOHWzVFajbZTOy9mheiawFEic5pXHAU9EI25HQ0SUvDI2RFplW9fbXhSibDtwxKJcSus/640?wx_fmt=jpeg&from=appmsg)

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