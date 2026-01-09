---
title: 众测环境下被忽视的“水洞”攻击面
url: https://mp.weixin.qq.com/s/0qNQRE3Z9ohWvTajDDYhNg
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:27:31.920695
---

# 众测环境下被忽视的“水洞”攻击面

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw1aj5jf5NMtk3FRXeZgbf7usfjULNQwxmibuycN7c6eTnywoAdSYdYF0jbnMyicorYR6gJmsEvF4VVQ/0?wx_fmt=jpeg)

# 众测环境下被忽视的“水洞”攻击面

泷羽Sec-track

![]()

在小说阅读器中沉浸阅读

以下文章来源于月的造梦星球
，作者一天要喝9杯水

![](http://wx.qlogo.cn/mmhead/ibkKkoaQFco5pQeXibaCYf7M9wfmBa82WiaGBGtUbYqyWNIX7E2fPhbjCYr9qlfUV2UHWZElnmEdpI/0)

**月的造梦星球**
.

临渊羡鱼 不如退而结网

> 分享几个在众测中遇到过的"水洞"案例,赏,本身众测开放时间就短并且要和大量师傅一同开始竞争,所以摸索出了一些简单的漏洞案例，忽略的功能点，隐藏的资产面，但是具体通过标准也是由厂商定夺,"水洞"危害字如其名,赏金也是符合"水"的标准50-300区间

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsV1iaCKxKKHQAnVxiaDtHDx8FyxaQowAuZhibciboaFdsqNiagO4G6CuIdTMw/640?wx_fmt=png&from=appmsg "null")

#### 转载

欢迎转载文章提供给安全圈其他师傅学习,但请标明社区原文地址，尊重社区内原创作者劳动成果,个人公众号：月的造梦星球, 欢迎讨论学习,共同进步。

#### CSV注入

此漏洞大多数`SRC`不会收取,因为危害大小完全是人为控制的,导出的`xlsx`没有被触发那么就一定没有效果,只能做到钓鱼的效果,但学习一下不是坏事,在不限制漏洞类型的众测中还是可以捡到钱的大部分人忽略了这个问题,相关原理可以看以下师傅的文章。这里说案例过程，如本地复现需要在`office`设置

https://xz.aliyun.com/news/11718

CSV注入漏洞原理及利用教程

```
文件->选项->信任中心->信任中心设置->外部内容
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVCBMyJP3Faz5PeibYibOP9BSUxz3mvfEbhjiccAyic5CdkpsbPFpCcOlb2g/640?wx_fmt=png&from=appmsg "null")

漏洞完成需要必备两个条件,1是支持输入文本信息，2是支持将输入的文本信息以表格的形式导出,一般存在于信息统计，或者日志导出等地方,在文本信息处输入`payload`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVzQgOLHD45GHZV4LVKKoNwNeTpJOlygfvQXNz7kfiaZolfrPMzBct4nQ/640?wx_fmt=png&from=appmsg "null")

```
=1+cmd|'/C calc'!A0
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVNNWvPy8ldudSveloaV7FnsnCEHpgibMsEtWtGZh31dLHlnyxA8BDRPg/640?wx_fmt=png&from=appmsg "null")

`payload`无过滤直接插入表格,如果存在过滤可以利用运算符`+-` 或者分号等进行绕过,具体可以看看其他师傅总结的绕过技巧文章,此处是无任何过滤的,那么直接进行**导出报表**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsV4GusvDY86aBJHSqib77J4gZLgHKZl0h6vKmfG7N7tg2d84c5SiayibmFQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVJvFFEJeiafVBc5VMicamOk6UQnCk7OE8RBZsTzkZJspMTWc1wicicq2Zrg/640?wx_fmt=png&from=appmsg "null")

导出后打开方式选择微软的`excel`打开，当在excel中打开`csv`文件时，文件会转换为`excel`格式并提供`excel`公式的执行功能，会造成命令执行问题。攻防钓鱼中也是一个不错的选择,因为在较老的版本如o`ffice 2016 MSO（16.0.4266.1001）`无该开关选项，那么默认就是开启; 因此无法禁止执行外部程序,只要恶意文件打开就会调用,执行反弹`shell`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVJdYG5Edc14ibzlaZHNiadicrEiacGklSGC9iaGJNbic8TUHMVEZUhibicc9R5A/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVtwabKS5W5BicCeGOBWT9OxVxFB0WNVBcWXia6Yc75jqyUjiawpfdMlepw/640?wx_fmt=png&from=appmsg "null")

#### 意见反馈越权

挖掘业务只要可以突破常规均是有效的,小程序我也是比较喜欢看反馈这种地方,大概率不起眼的功能点更容易出现越权,并且反馈常常会和文件上传挂钩,捡一波越权+文件上传`XSS`亦或者存储桶相关漏洞,也是美滋滋

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVtWnyBUSlI7rAibnFtDKfVjjAaa3ynbDJxgByTBQ9JcUo27oYbaSYjnw/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVzz1umBsxMibYCS3pTDYPprKYhvoDmgCJ4LYaOdgicXdJ0Q1DX9hFXYpw/640?wx_fmt=png&from=appmsg "null")

下面功能点就是最好的情况,并且可以发现手机号是固定的无法修改其他号码;那么在业务逻辑的角度讲,反馈要实名到个人,不能是恶意反馈,假如说我们可以在`BP`替换信息为他人的电话号码,就可以以他人身份进行反馈了,但是这种方法只限于功能点原本是固定的情况,如果功能点本身就可以替换姓名号码,那么我们再改也没有意义; 报告未留存完整漏洞也已修复,这里就不贴数据包效果了,各位师傅明白意思就行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsV6RaAuiaWiaXEticF5QradUnOTbQzRvOmbYwgo7V7BjxkhYk6TbG6BahnQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVicvicelz844ibWVcU7bdeghia0gYQtWjk0VEG5GPWTmEtDR9eEdnvHazFA/640?wx_fmt=png&from=appmsg "null")

#### 递归Fuzz未授权

开局登录框,虽然不是`Vue`框架但仍会看看插件有无泄露接口,只出现了一个接口

```
/sap/bc/ui2/flp
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVLS70IGkqxzAut88lHEotrYPukiaCFxMbjs4f9OWYesM30uBLF8LMOgQ/640?wx_fmt=png&from=appmsg "null")

测试完整访问会重定向会首页,`BP`也没有发多余的数据包,逐层删除也均是`404` ,进而去挖掘前台功能点也是一无所获,随机又回到这个接口开始进行递归`Fuzz`目录看是否可以探测到隐藏服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVLIduPt0EOibkLEe0lPcUrvSwG5I7bUQNq540UwVDAfR4CVVXpGe3ZqA/640?wx_fmt=png&from=appmsg "null")

```
/sap/bc/ui2/flp
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVWXWkzL40lKXpFCtAuxWuOzS3SRicffNVZD06CzGbYMyCoZlOt4Vb7BQ/640?wx_fmt=png&from=appmsg "null")

因为前台已经拿到了第一层接口`sap` 通常我会先在有效基础上进行爆破,在拼接上`admin` 后也是`302`来到了新的完整接口`default.html` 默认,并且需要登录

```
/sap/admin/public/default.html
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVETjWfchJYtq0cwTkOVOkjotJzbTibM5UDuK8SKRjoW58VtrehX96IMQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsV47Po7qsIImeNtS1I64LF4GNoWolMgsfbXJwIKNdyiblFJv9V1JjM2oQ/640?wx_fmt=png&from=appmsg "null")

后续我继续尝试在二层目录`admin`基础上继续爆破`Fuzz`并无有效反馈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVhHsdAh0E39mmLo8A2X76vaI8Klhgiaib43kmfk6qICBND3aXEJdua7VA/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVsBCRzxZaC7WDR3ZMOnAj67FBLicweOQA5EP2INSaArM54xFYdib6BWiaQ/640?wx_fmt=png&from=appmsg "null")

三层目录是`public`但感觉不太可能会有东西了,把目标转向`default.html`页面去进攻,在BP固定`default`值为`payload`点,这种地方还上目录字典没啥意义,因为四层目录很明显就是通过`html`渲染显示,只能`Fuzz`出更多的 `*.html`文件,随即掏出参数字典

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVncFM55QtPIRDbpsbv8jJxOZqMmMXYqoFXf5BVYEozKx5tTUyfAOKEA/640?wx_fmt=png&from=appmsg "null")

长达二分半下爆破结束,排序一下数据包,一一访问最终也是在根目录下发现`index.html`可以被未授权访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVEF8YGWYMuNORNVFLWaB8vxOC8lVFRwm5QjS6kvmwEWeV3UHuicGFreg/640?wx_fmt=png&from=appmsg "null")

```
https://xxxxx/sap/admin/public/header.html -----> 鉴权登录

https://xxxxx/sap/admin/public/index.html  -------> 未授权访问
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVHJdw9JwOAxsr0xbwIVEZ1NPfflXictPBU09dwJLT5E3fDOIPqicVvmXg/640?wx_fmt=png&from=appmsg "null")

对比可以看到`inde.html`无需认证即可访问操作,此漏洞引出了字典的重要性以及`Fuzz`这一操作,哪怕我从根目录开始`Fuzz`只要字典内有`SAP`目录那么我也可以顺利挖掘到这个漏洞,实战中可以多多收集形成自己的实战字典。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVibl1Ep0cf5C2wjwTaXkJwnEHbvpbwSKFfCVefb2d2VphjnxlibWy2o2g/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVVZxLcQNwXreF4bG11kl8iaw0lFAEHmicojicsrgeCcGbfpjGMhib9HKyfQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVT1oiafKdb3omEcvkJd1r2LwxwFia5BX7oFQLsCSGw6mcOjictzDFv7EKg/640?wx_fmt=png&from=appmsg "null")

#### 并发业务量

点赞、分享、转发等业务如果存在具体的数值,那么可以尝试多次点赞、分享、转发,影响对应帖子文章等舆论导向,这类业务在`APP`,`Web`、小程序屡见不鲜毕竟大家都更认可点赞转发量更高的文章；从众心理会觉得越多人追捧的文章越权威。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVCjfhBMbhMfbuNZpD1elPPZvXxKnvXPf6aIoGd35Hu3iawXpBMhoPLjw/640?wx_fmt=png&from=appmsg "null")

资产收集到一处`APP`分享贴吧也因为,点赞不存在并发,但是分享数量存在,可以多次进行分享数量增加并不是每一个用户只能分享一次的逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVicckIqhRjic4RjNP912NV6PnJaFQic0OYXjLgXErcH2ZTuMhST3IfuoMA/640?wx_fmt=png&from=appmsg "null")

手动分享或者BP多次重发,并发时间均可造成分享数量激增

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVQLOakbq5Tw1bO8r7vEdicd1qMjqQdy5YjGEibnCItfcfPXymibZSKkgFg/640?wx_fmt=png&from=appmsg "null")

同样功能点,分享、点赞、收藏存在固定的数量，`yakit`抓取数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVReOwHpB5pfCaY4kPoicbDiclvz2jNUFOEYEHmRWtyjfokQ0YEfNkNkwg/640?wx_fmt=png&from=appmsg "null")

设置发包值,等同于`BP`并发插件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVlXvSyyVq75xqKLqDRFicJpkJv6hRAElVoFYHTrw7oicpSQtzdhyCn7gg/640?wx_fmt=png&from=appmsg "null")

发送后刷新页面成功并发,毫无难度

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVPRW1bJE30VSOKquOFKjWna935ApLYGVp3Nyq6QtDxMtnicT5gEFjY9Q/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibjuibbR3icQCX26KVdjA9hCA9y3Q2iahbsVRnSMdloL5FYQvdTKbxYbY3QV7TXakahoPnVuWb1Hb4SC2...