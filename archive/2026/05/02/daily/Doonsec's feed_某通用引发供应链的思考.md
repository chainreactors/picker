---
title: 某通用引发供应链的思考
url: https://mp.weixin.qq.com/s/sQGkKhJk6cL4fbcUfCZMVA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:25:48.514734
---

# 某通用引发供应链的思考

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51yFSDiaWQLJmhYPdo8ud4k9ia1KvwsGTu04GIKJ2vuhrkiaeX5HF9LuBlQ/0?wx_fmt=jpeg)

# 某通用引发供应链的思考

原创

不知江月待何人
不知江月待何人

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

码领资料

获网安教程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

# 本文由掌控安全学院 - **不知江月待何人** 投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**

## 前言

前段时间看到很多人在打某通用系统，简单记录一下思路。
某通用单位系：xxx奕科技公司
产品如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51uKaOK82syqXNNM5UccMfeetKAOWWB1haycsQ8Hp7icbxOwW7HSDWkJw/640?wx_fmt=png&from=appmsg)
资产还不少，记住这个容器服务平台 等下还要考，以及这个事务中心 可强行接管统一
熟悉的Caas平台，又是熟悉的老朋友 云计算
最近比较流行云上攻防，见的比较多的还是ak、sk泄露接管
Docker逃逸以及K8s，这里先按下不表 Caas平台有大用处。

## 开局

根据上述所列资产，找对应服务资产
第一步：打点
跟到某资产，统一系统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51gNxQKzzCl7Ulb3ibDd559a6w87hHgMFHd68gccJLRibeKYljuqwL98ng/640?wx_fmt=png&from=appmsg)
这里的两种登录方式，账号 && 扫码【统一扫码 心跳连接到智慧校园平台 扫码登录】
熟悉的无账号开局，为了方便这里省去了子域，C段资产翻查，直奔结果

## 统一未授权

【老版本统一存在Shiro反序列化】
新版 —》翻JS 找API接口测逻辑，未授权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51O6vbzFLVqvlcz1H9BjrkmFrs3t0fAEfTib22q21hYyIdvcuAjcFhH9g/640?wx_fmt=png&from=appmsg)
记住这个接口，提示参数未完整，根据提示补全即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51nV3Sb44uuzgNdwV7JCtru0seic9JQa1vtM7iaZ3TyJyjkxWfq1BH1pug/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51rMCnQuu0XY4tvo8H8IdbRlqvGgicOaG2ibdial50BDCtic6ktdtaU3xpDg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51NoAutevTe3Sh88fn4nv8fTdgTpjpToYdW3xINoFq7I0EHgWSLUhk3g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51HwltdwoPNNRESE3iaI9gtLIJvY6YVNUKY3XhLXhX7zsmPEiaxPN1KUcg/640?wx_fmt=png&from=appmsg)
继续补全

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51b2AKJiakibRictdvKzCfnR1m44j5d8k9Wh5QyArnl7fZa9iavGVmQuL28Q/640?wx_fmt=png&from=appmsg)
有戏！这里需要注意几个点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo511EgueHcR3aEoLqPXgViaw7OS9qy1LoibvcPzscXEOa4ngcIxQ2nmvn7A/640?wx_fmt=png&from=appmsg)
bh、fjlj、fjlx：png
bh值：uuid，fjlj值传了一个组什么的，fjlx这个是重点
知道了回显，继续回去看接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51KeEjPr7HmNPj60x4dhxOmsdI898ZZj8RB4CnXQibJOOlYz6mN00wdMQ/640?wx_fmt=png&from=appmsg)
attachmentId=需要传一个参数值，哪个值呢？bh
是一个未授权任意文件下载，当然bh以及fjlj 均是未授权任意文件下载
这里注意，fjlx：png这个参数点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51CJiaibYYALdibKvl8gztiaBYxxo06OLLzLMaZIHvcNUxqc1YshoUnVDPeA/640?wx_fmt=png&from=appmsg)
这里能探到源码文件泄露的话，这里就可以结束了，可惜没有
xlsx文件同样可疑，如果，如果有账号密码泄露？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51O5PuZoA4oYl1YwWVLxoZlVbMqfyloyeUvF5mlOKKticoUMEHiayCTaXg/640?wx_fmt=png&from=appmsg)
有趣了起来，都是web兴趣不大，记得前文提到的Caas平台，具体是哪个不知。根据泄露信息继续找
就是你了！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51PwQhKbEO6wKzAYXz6EZhJPITft0ZltQWTUibib2nhadHUrN4vazgr3Aw/640?wx_fmt=png&from=appmsg)
有趣！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51Ivh0tibpD9gCXX5SerRGIBRaBNo1383wvnAljrzyxlAAPk84U5bJMIA/640?wx_fmt=png&from=appmsg)
Portainer是docker的图形化管理工具，这就和Caas云服务平台有关联了，怎么和官方服务通信进行镜像下发呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51OX9zS2gDSV2nvPFFiaRQyniaXWTag7qhM6Z7EeYJibljdVf5NdMMYHCGA/640?wx_fmt=png&from=appmsg)
这里敏感不方便放细节图
白盒的角度来讲，到Portainer就已经结束了，正式的镜像包是同步下发的，所以

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo5160DVKI1QBAhoRnGKEmqxZjiaAvQ1X3afyVCZZouM5jQ71qnpaA4ias4w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51lckMj1LsczmKdgrOHMBBGhbKy5YD9kyfxSGxd07iankD9iazcpdPiaK9g/640?wx_fmt=png&from=appmsg)
到这里就结束了，剩下的就是枯燥的找资产，核对api 找系统验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqp1c3jjcUj6T0B6Qbxwo51kwQzZfl8YnXphibhGIo1WesHjIcFdHq002oXVdoR5JtIJ10wq4QmTnQ/640?wx_fmt=png&from=appmsg)

## 写在最后

如果，如果把资产测绘各个平台的特性用到极致呢？
未完待续~

```
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

没看够~？欢迎关注！

分享本文到朋友圈，可以凭截图找老师领取

上千教程+工具+靶场账号哦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

 分享后扫码加我！

回顾往期内容

Xray挂机刷漏洞

零基础学黑客，该怎么学？

网络安全人员必考的几本证书！

文库｜内网神器cs4.0使用说明书

代码审计 | 这个CNVD证书拿的有点轻松

【精选】SRC快速入门+上分小秘籍+实战指南

## 代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！

![](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

点赞+在看支持一下吧~感谢看官老爷~

你的点赞是我更新的动力
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BwqHlJ29vcq98SadiaYm6GqwrAZjdeXAuLrl5ATlxIMCiabYgjLJ1M1gcLHicsRuISeqtAuLaSfRtBULuibjDBcLsg/0?wx_fmt=png)

掌控安全EDU

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