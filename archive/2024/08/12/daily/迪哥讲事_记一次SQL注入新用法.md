---
title: 记一次SQL注入新用法
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495497&idx=1&sn=99faeaead656d98179eb1fd5ae21f398&chksm=e8a5e52adfd26c3cd6d71af0ecbc296d27844230af350b29d3fd79ceb9ba1776eb5f69249071&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-12
fetch_date: 2025-10-06T18:01:53.476513
---

# 记一次SQL注入新用法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4GqSVoVnVBMKCnfRx5R1burQ1C0CEgjkkHs7BRk8uES0tf0ooAxFUKyiarSwzuO87IqOvH7ylzIibQ/0?wx_fmt=jpeg)

# 记一次SQL注入新用法

Alivin

迪哥讲事

```
作者：Alivin原文地址：https://forum.butian.net/share/470
```

在参加某市攻防演练的时候，发现目标站，经过一系列尝试，包括弱口令、SQL注入等等尝试后，未获得到有效的入口点。在准备放弃之时，看到页脚的banner：xxxxx信息科技有限公司 [!...

# **0.前言**

在参加某市攻防演练的时候，发现目标站，经过一系列尝试，包括弱口令、SQL注入等等尝试后，未获得到有效的入口点。在准备放弃之时，看到页脚的banner：xxxxx信息科技有限公司

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOAQzyvMV3pRwHMZl6YicgV9l24pf0gHgG9LyLzL6t6T1ia7SWZ6nAoyqOw/640?wx_fmt=png&wxfrom=13&tp=wxpic)

然后有了个想法，到fofa里面搜这个banner，找到一些其他使用该站的，但是没有参与攻防演练的（PS：演练前该单位做过整改弱口令全改了）。

# **1.旁路进站获取未授权接口**

经过尝试，果然皇天不负有心人，进入到了其他厂商的后台，于是开始寻找未授权就能访问的接口或者RCE点，脱代码来审计，从而获取目标权限。

找了一圈，后台没有直接RCE的点，无法脱代码来审计，但是发现了一个有趣的点：

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOAQuqArf7XRVNlZQicGiaH1icatDicx0LULiapkSiaIXtTBCbN74FlotPW2fbg/640?wx_fmt=png&wxfrom=13&tp=wxpic)

此处查找联系人的接口，存在未授权访问，数据包为：

```
POST /HanNeng/SelectHelp HTTP/1.1
Content-Length: 29
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: ASP.NET_SessionId=vd11thy3qnmgz0h4dtyb51ra; rem=1192
Connection: close

Type=User&Field=UserName&Con=
```

经过测试发现该处不仅存在未授权访问，Field参数还存在注入。

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOAXW4G2v1cjPcH7cjjpUTpic0QyJOy4NHHFrlyiaPZibKIDTepBoapu0K8A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

直接给出部分sql语句：

```
select count(*) from tb_User where IsDeleted!=1 and Password'
```

测试过程中发现field是列名，证明如下：

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOATAZn1pRUL6HA3XogrwqEjUBpU3D7TXTQcqNg1k2VujgDx2sibccFKlg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

当我认为可以sqlmap一把梭的时候，却发现了这该死的waf：

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOAQBTa3Sete6AcGGngH6pfIhosuTZ4UwjI61e6L2ReO1XBicbcQQ84ToQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

# **3.与waf生死缠斗到和平相处**

尝试绕过waf：

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOAiaIsvny4tqSesXiamKDGkglViaJ5cicsIrdmqiaHYiaxL1cE2nZux95AoIoA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

发现like附近语法错误,这时候想起来根据其他搜索方式，比如工号搜索的时候，应该是模糊匹配的：

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOAiamz0NBPyf4NdSXxmp65Tic6JDuoLMPHjw8hg7HMKzfr2be2VJe8ViamA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

发现Con参数的内容应该是进行了模糊匹配，也就是说sql语句可能是：

```
select count(*) from tb_User where IsDeleted!=1 and userid like '%可控点2%';
```

可控点2不存在注入，可控点1存在注入但是有waf，这时候就想到一个特别好玩的方法，我把field传入个password是否能获取到password密文呢？

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOA4pibPyoyGblZ7f0icVa2JDR67aPbwKcx6Nibrpf8XV81C7N3Mbv2r5LdQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

然而并没有，所以呢，猜测此处是这样一个逻辑：

先执行sql语句，确定用户数量：

```
select count(*) from tb_User where IsDeleted!=1 and userid like '%可控点2%';
```

然后再执行sql语句筛选用户信息，工号和姓名：

```
select username,userid from tb_User where IsDeleted!=1 and userid like '%可控点2%';
```

所以肯定不可能直接把密码传出的，那么就没得搞了么？要么绕过waf，要么还能。。。

```
select count(*) from tb_User where IsDeleted!=1 and password like '%可控点2%';
```

这样我只需要构造payload：`Type=User&Field=password&Con={遍历}`就可以一位一位注入密码了，比如：

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOANJIOXdQ5XL9AOghficdS4wFZD1b2XKmgmyy8FWahvhKCzJRD1ts7J0w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOA1Av1ULicLLTQ4R8LCTd8DNdHVcvgRs9yBmJGttcCkp5S3iag0uiaf9Bng/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

用户pageCount数量一直在减少，密码相同的用户一直在减少，但是这里要说明一个点，因为是%可控点%，所以123的前后都有可能有数据，当时我犯了这个错误，导致注入出的md5不全。注入出md5证明如下：

![](https://mmbiz.qpic.cn/mmbiz_png/XYnjkohc3g8bTduq4bLCanDq5xN5bQOArUyEuKYuyjqibibZ6qpjAfopoCzstCALCUr4zhH3OicpKd0O9otWS4Wcw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

自此就可以和waf和平共存，你防你的大注入，我搞你的小密码。获取完整md5后解密即可登录后台。

声明：本公众号所分享内容仅用于网安爱好者之间的技术讨论，禁止用于违法途径，**所有渗透都需获取授权**！否则需自行承担，本公众号及原作者不承担相应的后果.

如果你是一个长期主义者，欢迎加入我的知识星球([优先查看这个链接，里面可能还有优惠券](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247489122&idx=1&sn=a022eae85e06e46d769c60b2f608f2b8&chksm=e8a61c01dfd195170a090bce3e27dffdc123af1ca06d196aa1c7fe623a8957755f0cc67fe004&scene=21#wechat_redirect))，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[2022年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

## 福利视频

笔者自己录制的一套php视频教程(适合0基础的),感兴趣的童鞋可以看看,基础视频总共约200多集,目前已经录制完毕,后续还有更多视频出品

https://space.bilibili.com/177546377/channel/seriesdetail?sid=2949374

## 技术交流

技术交流请加笔者微信:richardo1o1 (暗号:growing)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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