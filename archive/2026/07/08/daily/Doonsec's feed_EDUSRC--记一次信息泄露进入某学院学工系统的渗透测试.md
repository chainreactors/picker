---
title: EDUSRC--记一次信息泄露进入某学院学工系统的渗透测试
url: https://mp.weixin.qq.com/s/hRXsVJyIsjIlFL902kyJ2w
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:56:36.411175
---

# EDUSRC--记一次信息泄露进入某学院学工系统的渗透测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ianpxKPnLHoJLymyDhib1wBR3bLKo7WYcBtxScRiaP9tTM8wZZfYOtiatwDbTO0tv1fz6tqasiaLexnaVClCVYtYBXGyNK2cxzQNCxoA71mYqz7M/0?wx_fmt=jpeg)

# EDUSRC--记一次信息泄露进入某学院学工系统的渗透测试

zkaq - kpc
zkaq - kpc

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - kpc 投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**

#### 文章中敏感信息均已做打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！

## 一、前言

现在的web站点挖掘难度越来越大，有时候能进入一些学校的内部系统也是非常重要的，虽然该系统并没有提示密码的规则，但也可以依靠信息搜集来尝试一些简单的密码规则，比如初始密码就是学号或者身份证后6位，依靠这个思路，有时候会有非常大的收获。

## 二、通过信息搜集获得敏感信息

搜集学号等信息我常用的有以下几种方法：
1、浏览器直接搜，如XXX大学学号
2、fofa 这里的思路是搜集某大学的公示、成绩、名单、奖学金、转专业……这些关键字眼会让我们更快的找到学生的个人信息
3、直接去学校官网去搜，进入学校官网，我们可以从学院分布下手，比如很多学校官网都会有学院设置，包含了XXX学院，我们可以进入某学院，之后再在该学院的通告、公式中找寻名单等关键字。
4、某音、某书等社交平台去搜
按照这个思路，成功在某学院的公示文件中找到了敏感信息，本来只是想要学号，没想到sfz也给了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLBRze4TQiaSX5cfkwojBHUUnps1pONEO0u4rOYDS048tpu2zibNgNyf7NHYplTumLfloh3PcDcKRpmkXiaqT22B0TibwTciaOzjRe0/640?wx_fmt=png&from=appmsg)
既然获得了这些敏感信息，那么肯定要去试一试该校的内部系统是否能进去扩大攻击面。直接用鹰图搜集资产：
(domain=”XX.edu.cn” || web.body=”XX大学” || web.title=”XXX大学”)&&(web.title=”系统” or web.title=”平台” or web.title=”管理” or web.title=”后台”)&&ip.country==”CN”
这样搜集出来的资产既包括学校资产也包括存疑资产，攻击面更广，而且搜集出来的全是系统、平台这样容易出洞、好测试的资产。
经过不断测试，发现该校的学工系统存在默认密码，即身份证后六位：

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKmcYokM8uLGlnicPLfNxRic9lcpyrTduDZ3tpROhjpKgKDFVlBrcevj5G73PVeDnc5ickld1koIpInuQbTgwfLRE15Yicjbic1duXw/640?wx_fmt=png&from=appmsg)
于是通过上面信息搜集获取到的sfz一个个试，运气不错，成功捡到一个使用默认密码的：

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoI8pyXicx4zJ2bORQMR6ib3HlKfyibVd7ibWJWvIpo3WSd1KMfboUjQefzDrNpAfqyDhn4zFI8OxEVQB5ia6SkFMeeZqQtmickjQQ7Nc/640?wx_fmt=png&from=appmsg)
没办法，为了之后的测试，只能修改这位同学的密码了，渗透测试结束再改回原弱口令密码即可。

## 三、多个漏洞打包

成功进入该校学工系统后，我们首先要判断这是什么框架、语言，然后根据这些语言的特性去针对性的测试，如果是java就重点测越权，如果是php，net就多关注SQL注入等。
通过插件，也可以看出该系统是net：

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLY2IwVqMLluG53F6INV0bcIULAt9fHzgTF9rINtPJmE3G7IOIyNmjeK4mR40SaJm6Feng37UOTL018QtoNxxcCuNpebKxLibHs/640?wx_fmt=png&from=appmsg)
那数据库大概率是mssql了，mssql常用的注入方式：
1、有回显：直接用报错注入
2、无回显：用正常的盲注即可，时间或者布尔

## a.SQL报错注入

进入系统后，注意到公告处有某条目，而且是通过id传参的:

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoK00nwd10JplnExOXEtHLx2I06VrKWrO0dfSBl2oic04PwljeDjogoch87KmKbFwP0RrPePEWuDu0M53Sw3xtxxxULCbOUY49A0/640?wx_fmt=png&from=appmsg)
通过burp插件xiasql确认后是数字型的，所以直接把id换成数据库名称函数db\_name()即可报错注入：

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL77c1UbfSMnc2qqJ41OnibGrtnMrQ6cqw1K0sRWqT8z75EVxXtQFgvGJY9s566IfTrsPfv18onvyxu8MGAUXtml2gqXPAgPsIc/640?wx_fmt=png&from=appmsg)
原理：将不同数据类型的数据进行转换或对比时，如果转换的是有关查询语句或函数等，那么就会触发报错。本来id是数字型的，直接换成输出数据库函数，这个函数像整数转换时就会报错，直接获得数据库名。
如果id是字符型的，就用这个payload：id=1’and+1=db\_name()—
原理和上面相同，只是要闭合单引号。

## b.SQL布尔盲注

在邮箱中，发现每条邮件也是通过id传参的，属于是不同接口了，但是这里并没有显示报错信息，只能用盲注了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLXe9ggIZeRLp0MvKx3PKnpfiawDsm3lNYTPF403wGG17x3JLbzDm5yFcIbh74wjCVbcEYJbLy1ibF0nZuqUC1GGuiaNtrUIOat4U/640?wx_fmt=png&from=appmsg)
构造的布尔语句为真则正常返回200，否则直接302：
1=1:
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJEH9vF9wZILeyLLqm5hZmBdV7fjGNoVz9NiaX1A8R3BicVOUUYeC5XOlia3lcrbggIKQbgVJ55gicTrF0ucUqxldqhCuaICThx1co/640?wx_fmt=png&from=appmsg)
1=2:

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJ5qFf502wuNyaW2bpLs7o8kKmibz5GyVcpD4l9YBxbX92R8vX74XCSz5w3IC81zmibiab6PY9UabbZjV12J2Js7CGVn3tibsRYfaY/640?wx_fmt=png&from=appmsg)
接下来开始进一步获取数据，先获取数据库长度：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJKC1QCduXwWicqppl48yibR7sljeMeKiasjHdKWzfBzazUWFias37QpwZdZZLcXZwgs8I2uyeTfavxnYbibvqhqlhbTkkNhCVzkPics/640?wx_fmt=png&from=appmsg)
发现到7时，正常返回200，说明语句为真，数据库长度为7，其实到这里已经可以提交了，不过这个没有什么waf，我直接把库名也跑出来了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI1Ejn3WNt68HNLMRMib6ibwmZCQ5VzZITficnFjic22VbGKfmdoLQOtcYLeAcia1Xbd2RJZlWEvQqdX2UuDtI6FFyeDyl6d1Goxd6g/640?wx_fmt=png&from=appmsg)
直接设置爆破点，截取数据库的第一位，第二位…即可判断出库名，最后得到的和报错注入的也一致，证明布尔盲注没问题。

## c.XSS+逻辑越权组合拳

我们遇到id是一个简单的可遍历的数字时除了注入要测，当然也要测越权，修改id值看是否能越权到其他用户的信息，按照这个思路也是成功在修改家庭信息的模块找到了越权，遗憾的是这里没有注入，过滤的非常严格。（这里讲一句局外话，大家测试时一定要每个功能都测一遍，因为可能一个系统是由多个开发完成的，每个开发的习惯、水平都不一样，千万不能测一两个功能发现没有出洞就直接放弃，说不定其他功能就有洞。如果测试到了某个漏洞也是一样，说不定其他功能点也有类似的漏洞，这样才能增加出洞的概率。）：

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoK8UJvNBLIhYq7wz6vib7gPkDHhTOADTAQqIfK8gXtcIoXMgyQrWWjbIhSpXblXw80tARq0SJI4DmWydqOU8GD0N62IjU7nkcIw/640?wx_fmt=png&from=appmsg)
修改rid即可跳到其他用户的家庭信息界面，而且可以任意修改，既然可以修改，那自然要试试XSS可不可以触发了，如果可以直接扩大危害，测试一番后成功触发：

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIllbquVFKwMBIwY6jDG0JJYicvasWtVULaBS6bribsC2W5ab9KWR39cXHELn3LUpS85fjnOybID2Dj4sicYogPq6SK6HEQ61Mq08/640?wx_fmt=png&from=appmsg)

## 四、总结

正如上面所说的，通过信息搜集才能获取更多的资产，进入更多的系统，进入系统后要根据语言、框架有重点的测试，测试时要各个功能都要测试一遍，不能想当然的认为每个接口都一样校验的非常严格，挖到一个漏洞时也要把其他类似的功能测试一遍。希望这篇文章可以帮助各位大佬，天天上大分。

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

**分享后扫码加我！**

**回顾往期内容**

[零基础学黑客，该怎么学？](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247487576&idx=1&sn=3852f2221f6d1a492b94939f5f398034&chksm=fa686929cd1fe03fcb6d14a5a9d86c2ed750b3617bd55ad73134bd6d1397cc3ccf4a1b822bd4&scene=21#wechat_redirect)

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[记某地级市护网的攻防演练行动](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247543747&idx=1&sn=c7745ecb8b33401ae317c295bed41cc8&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

点赞+在看支持一下吧~感谢看官老爷~

你的点赞是我更新的动力

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BwqHlJ29vcq98SadiaYm6GqwrAZjdeXAuLrl5ATlxIMCiabYgjLJ1M1gcLHicsRuISeqtAuLaSfRtBULuibjDBcLsg/0?wx_fmt=png)

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