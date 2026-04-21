---
title: 某次测试从前台登录页到渲染后台功能
url: https://mp.weixin.qq.com/s/u9UN2cBc3jZwbyxhPgOPmQ
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:46:25.941316
---

# 某次测试从前台登录页到渲染后台功能

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQ7L1XIWLeicmKWGicddXz2zg9k0xZrWwjJdbticLdGOUicF1CVVMxhGVibaP7M375IIZUBcOt0iaicgzzcmzib6YVzcicaQGhPYWCfrFzk/0?wx_fmt=jpeg)

# 某次测试从前台登录页到渲染后台功能

中铁13层打工人
中铁13层打工人

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:中铁13层打工人原文链接:https://forum.butian.net/share/2492
```

前言

某次测试目标给了一个后台系统

# 1.后台权限获取

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRx9cfh9OVWc7LO5w4yicyN8sgusCpOKgOy5NNPUqJjKjeEJArOE4SwS4JmEQibnnxPRH9JykpbqN1CudiaEbDMLfL9XcJu8KQOZw/640?wx_fmt=png&from=appmsg)

打开一看，平平无奇的后台系统，也没有提供测试账号，爆破了一番弱口令未果，尬住。

也遇到过很多这种只有一个登录页面且没有账号的情况下，想了想为了以后测试起来效率高一点，总结了下经验大概有这么几种思路去获取后台权限。

1.爆破常见弱口令

2.寻找是否有硬编码的账密

3.分析js中登录逻辑的判断，是否为前端认证（例如依赖返回包中的某个字段值）或者是否有认证缺陷（例如只要有某某header就行）

4.获取其他登录角色/登录体系的认证字段，看认证是否共用能否越权（例如同系统下的普通用户角色和机构用户角色/前台可注册的用户和后台用户等）

5.寻找是否有隐藏的注册点，直接注册

6.js寻找敏感接口，对接口尝试访问利用

7.登录口尝试注入，注出账号密码或者使用万能密码登录

8.中间件/组件漏洞

最终收集到一个与web系统同名的微信小程序，发现域名和认证的字段用的都是同一个，直接尝试微信小程序手机号快捷登录接口获取的返回包替换web后台登录接口的请求返回包，成功登录。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSkNJOZ7ZboI1icK8ZjXRtL4BMSUb5SJeiaibw2a4D4tQsKYphTNcXibRX5EbbuQqBy1RibNwk7BZia5SHSYcFmfeHAfIWI6S4oS8W2E/640?wx_fmt=png&from=appmsg)

成功触发了后台请求

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRezRsfzu5NuGjOxibvXCJ6TqNicntMoccrVm0yUpQDUumqFXNSbgUFQU2HOviaAhuUo9wus8xhXHszejPynCblwda6zp42TFnvibo/640?wx_fmt=png&from=appmsg)

但是浏览器页面上是空的，啥也没有。

# 2.获取后台接口

这种登录后空页面的情况，一般都是账号权限不够导致后端没有返回高权限接口的数据导致前端无法正常渲染页面导致的。

## 2.1 js翻找接口

最常规的测试思路当然就是去翻js里面的接口了，虽然账号权限不足没有功能页面，但是很多情况下js里面是含有后台高权限的接口的，可以直接尝试构造参数访问利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQy00mibAdfvKSkz4LZFgzBjLqRAGxHpJxDI5iboib2iasxAhvwlP8w7In6xYPg8ribbZftBfVmDLp6wjLTSfbloibPvpbS3RYd49Sf8/640?wx_fmt=png&from=appmsg)

翻js也是有讲究的，js里找接口大家都知道，但是有一点要注意的是翻的js全不全。

例如下面这个例子，默认的页面只加载了部分js

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRlucRUibsWTcIicD3cicezHuOVPTTb5RcNoSAianPFhBLzUwO5eCWagoO2OxLxUXrP5NIbyED49oLz2vwX7Hk5ysruXlJ8AJNNPb4/640?wx_fmt=png&from=appmsg)

对已加载的接口名进行搜索，发现其实还是有很多js没有加载出来的，收集一下，写个脚本批量请求把js全部加载出来，便能测试到更多的接口。

这种方式简单无脑，但弊端是如果部分接口的传参没有直接写在js里，导致就算拿到了接口构造参数也比较麻烦。

## 2.2寻找接口文档

接口文档往往包含全部的接口以及参数信息，拿到后测试起来比较方便。

除了fuzz类似swagger这种组件的接口文档以外，还可以观察下登录的数据包，看加载菜单的接口的名称，寻找名称与其类似的。

例如登录后获取菜单的请求url为loadlist,则可以搜索js中有没有adminlist,getlist等相关接口，也可以拿到接口信息。这样替换其返回包就可以在页面上渲染出功能点来测试了。

回到我们遇到的情况，分析得出是该接口返回为空导致页面没有东西的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQtOWpFYuyhLaVUGP0a3fYJiakdfcanptbUBfZGSrsSoR4xy08Slvbr8HoUBIbOFYLIftmeewJdK1cZNfyjNnjlnZIhZ5KwDibE0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTDvXEk2oocloesgK1ic3ykBcvgY9H4qSM7dUWbbO5DqQ20LAyD1cEKgJnUZUNaWg93842icHCNicuTPr3sUaqgRiay7jtDXFXHdls/640?wx_fmt=png&from=appmsg)

从接口名称“initMenu”也可以知道这是一个获取功能菜单的接口，返回为空，所以导致页面上没有任何功能点。

先看看这个接口的传值是啥

浏览器寻找并打上断点获取明文（断点调试网上文章很多了不再赘述）

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboStHA5s7YzKlO1xJPlH8PcXvzicAjgjTFfpquRe7xwhuicyA8ictIydo5W5GibE21U0Q8EM48DUnLlLO9TV1RUiaBicA4ZXIOUK1D6iaI/640?wx_fmt=png&from=appmsg)

可以看到传的值也是空的，那么改请求参数获取更多返回基本是行不通了。

尝试全局搜Menu的菜单的关键字寻找是否有其他菜单有关的接口，发现了一处Menutree接口，应该是有全部功能页面数据的！

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR7tfiac7ViaxKO1SoEZSzwCicv0iaDcR78lToFic1IZQqAumZZKLKNRMyg6rB0755lEuU5dmSbcNTpiahe0VKiav7OBIaWrCaHgCzB60/640?wx_fmt=png&from=appmsg)

直接访问返回400，没关系，模仿initMenu接口的请求包和传值post访问下（数据包有签名断点调试生成即可，测试时一开始忘了加密body了，没想到后端也可以正常处理==）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTcsDxqoicKawSK8vLjIo4BCkgqyATk1ZfDHgABsCpHqHPTUE3xMCFiaK3ibBaJ3Yuh8wr6GibV8Q4rXSJT6HjoEArHjibgZGQ1EQKc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSibq86WhDE7ic6MaCUdLqmVquibZrq2jCwfsic9wynEmeurhJjM4JsYBTvQhzWkb4NYY6LpAI0jZGibPxp8Mk0UiaKhV8eJGndy2dpQ/640?wx_fmt=png&from=appmsg)

成功得到了菜单页面的数据，复制该返回包，登录我们的账号，替换到initMenu这个请求的返回包中应该就可以出现功能页面了。

但是失败总是贯穿人生始终，返回的页面还是空的。

# 3.生成功能页面

继续分析js对initMenu接口的返回的处理

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS3zueybT5p2wd73PNiafAkBcvIaw7ULLf8FXyzbnnl5otVhscrEnP5BMrYod21ibn7AHUosyKicHPAyqtIbyQZ2ibKpAy093SpaLg/640?wx_fmt=png&from=appmsg)

原来页面生成时，取的是res.data.data

而initMenutree接口返回的我们需要的值在res.data.data.tree中，所以前端渲染不了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQXiaicNDVr8DcFtJHBVGFE9dMh0aBYvzO3e8aKyDoS2icVfrHYureE6yQP6W0X4CCwKYNNlSDDNNl2RPHdfN7wxEBTKzvmcy6MHU/640?wx_fmt=png&from=appmsg)

如下修改一下字段就好

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGwXzo5rWeWbL6d0nN7TFibvskqwMJMzELicRQJOpl0I7yejKdsDbR3vkY88R4gy49cbgJoyct0iaOmfUFmQFXtDgeeWbPgeFPibY/640?wx_fmt=png&from=appmsg)

替换后成功生成功能页面

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRP7BezXt6sicViaEo02gIkTgutqTVrLD5fBnicHibKnmoQRGuhb6CsibByQ3lH2qADaJiaEU1GI4Pic2uGu3ucic5CWbkMqQicFvkLib0KE/640?wx_fmt=png&from=appmsg)

后续抓包测试，发现多处垂直越权及其他漏洞，较为常规不再赘述。

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中）**

```
信息收集(会永久提供fofa-key助力)弱口令漏洞任意文件读取&删除&下载漏洞sql注入漏洞url重定向漏洞未授权访问漏洞挖掘XSS漏洞挖掘等等常见漏洞EDUSRC证书站挖掘案例分享SRC挖掘实战针对各种常见功能总结的常见测试思路等经典常见Nday漏洞复现等各模块不在一一介绍
```

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSWarKnFiaUicnq701hWQaiaA94FmgLNE8SVmrJiaJwluiavCE2VRvDV3ZYnwhib2pSNEpPp3Qp3beicPIAsVs3dS4A2MoYQXcsticwlqQ/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRD8gJdgFicMTaYcSMHydxPNJvagOaOrNbrM6S2tDPEcmjyECKacjmNJBCtwGAKMNdMes7tztJfWZGqjKxC7tkg99v4uDXDTpSE/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRPAemLYYSWRsc2cHYkwwxQicDQNf46MY8wUetFibPmetZdkicr4BNvPF0cBibqyS9emwayFf6njw9kjvBvWLoFDQJY5JQDMSUqh4E/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

```
渗透测试基本问题一汇总渗透测试基本问题二汇总渗透测试基本问题三汇总微步护网面试题目长亭科技面试深信服护网面试启明星辰渗透测试面试题目安恒面试题目360面试奇安信护网面试运维面试题目运维面试题库网安面试相关文档大全相关面试文章推荐等等
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSoLqEzH0a3A4LQrvTIkGx81Sh5pf6fCoEQJhYg715vrJicSkfBuCoAmV2Kp4uOMe5jcUZutPwicibFibtJ1ZmyiaAibCg0XicWnsNcicE/640?wx_fmt=png&from=appmsg)

**陌笙****纷传****圈子介****绍**

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&视频5、不定期分享通杀、0day6、有圈子群可以技术交流以及不定期抽取证书&免费rank7.分享各种护网资料各家安全厂商讲解视频&精选实战面试题目8、各种框架漏洞技巧分享9、各种源码分享（泛微、正方系统、用友等）10、漏洞挖掘工具&信息收集工具&内网渗透免杀等网安工具分享11、各种ctf资料以及题目分享12、cnvd挖掘技巧&CNVD资产&src资产分享&补天1权重资产分享&fofakey共用13、免杀、逆向、红队攻内网防渗透等课程分享14、漏洞库&字典以各种内容不在一一说明15、cisp-pte/pts&nisp一级&nisp二级&edusrc证书内部价格15、如果有漏洞挖掘问题或者工具资料需求可以找群主(尽量满足)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSY2pbvbP3qGAlW8O43bRvAISCxZm4UDTRsaMVbJKTsjfTMTDlq6qNBcVs4tkl4UzgqGz5ag81baU1rusKE09J9T6cMVliaibibwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTrLRQpTicOR7bzyNiajiapVJgyMiaYlEDBVU87YXMnanOFWsCYN3cCVGsKkibzV9dMryvbFXBb4Z3472ib27RJ1Xq1HnKJIp5u49GYQ/640?wx_fmt=jpeg&from=appmsg)

**目前650多条内容，扫码查看详情，持续更新中。。**

**如果觉得合适可以加入，价格不定期会根据圈子内容和圈子人数进行上调。。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTf4cCVdicO19OlMKjUqicUpTREyLiawUiaVBe7TXVa9fLcvT0mqkAEfcGwAcfNWxnUlaFBYLEvdU2wVjToBO4X0TfexQ2gecibiastw/640?wx_fmt=png&fro...