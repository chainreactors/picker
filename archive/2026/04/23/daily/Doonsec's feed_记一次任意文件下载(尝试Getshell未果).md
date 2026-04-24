---
title: 记一次任意文件下载(尝试Getshell未果)
url: https://mp.weixin.qq.com/s/qc-zG6ls_I7uxcU4G_63RQ
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:55:23.340481
---

# 记一次任意文件下载(尝试Getshell未果)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbB8G4uAa8lcp562VNj7ltk9uO7y33zVtZXK4ibwzBmbMl1uEp8zFOvukag5xBOK53E6y77NEzT4bll9ucmoxkHgHpgUvrfObBL4/0?wx_fmt=jpeg)

# 记一次任意文件下载(尝试Getshell未果)

略懂安全的三秋
略懂安全的三秋

略懂安全的三秋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原文链接：https://forum.butian.net/share/2130

有请今天的主角登场，不难看出这是一个招聘系统 1.先尝试注册

## ***有请今天的主角登场，不难看出这是一个招聘系统***

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbCAys8mzlzdgtKdtpUYPxlnweCI2icpF8nUgFWSzEdUqrxJruT3hTJ5eedkI07SexguB9SkOtslD32jGXHicNx7epd9WMdTcnAxE/640?wx_fmt=png&from=appmsg)

# **1.先尝试注册**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbBHypWSZRRafRib9g83ITWXUBqribnAUVE0tREUtK5PicaBiadicPiab5a6FibtlT4TjO9eOooAeOv2OibjW8YicvP7OWYuazdDK1bJibfWs/640?wx_fmt=png&from=appmsg)

## **2.但是！！我这种懒狗是懒得去注册的**!

**由注册的提示我们可知，密码最少为六位，那我们就直接上爆破吧**

**再想想，这里我们是选择爆破密码还是选择爆破用户名呢？**

**根据这个站的功能可知，这是个招聘网站，招聘网站那肯定以人名为用户名的多吧？**

**是吧是吧应该是吧**

**所以我们这里选择爆破用户名，密码设置为123456**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCEFxYBGVPua1zhvia7Oz8tbsveMRZ4Fy3z1aqUbicBlgHibOeRMlaoCoX76y0eDgnFjabalykfv2GCZz2bLhPtudgdcHNlqvtic3E/640?wx_fmt=png&from=appmsg)

、

**果然印证了我的猜想，还没有跑完整个字典我就暂停了**

**上图200返回的是登录错误，302是登录成功后跳转至/Manager页面**

## **3.我们这里选择xxxxxx来继续进行测试**

**啊，点击修改简历，一眼我就看到了附件上传四个大字**

**以往的经验告诉我，这里挺有可能Getshell**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbAhHDBbUOSUDz3Ods3E9lIn1vCzct9wwV0dsPfREanCm7q7aIWiaZu9V127MCBibrVxibA7Pgvh0NbOdicQv3BdI7icgVqLT6na5l3Q/640?wx_fmt=png&from=appmsg)

# 4.尝试上传

**这里先上传一张正常的图片试试水**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbDftduOlp4pcmMTpOb8x4l7H1phcBnuichB9JznDmUR4xKCygwUDxp5zuArhlRSPlIficjficcbxbzJwLMy37WHQad2hNkB98wGfw/640?wx_fmt=png&from=appmsg)

## 5.开启抓包，点击保存

**正常发送，发现跳转了**

**那我们就把抓的包放掉**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbA6yl8AdqibCPOLAns8fFFCJufoWib4duN5tJkBUAzuVRVbRaR3ia8CDRgbGG1TgibibEW12qBo7YdnQn145rCaMIM5CvLKPBmndg54/640?wx_fmt=png&from=appmsg)

**发现保存成功，还重命名了，测试了这三个上传点发现都是会重命名文件，只是上传的目录不同而已**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbCLJj63PmSOx9vUQgWicJPq0jdGCAF41EbyCiaVWgRgl29otAGsW0C6XbQoUkVnba2cYaVhIw4FvGjEHNuNIKJTwU6nPGworycF8/640?wx_fmt=png&from=appmsg)

## 6.这里我思路有点断了。。。

**乱点乱点回到主页看了一下**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbCfJgiaIAriclib4HyTjUFFqcBJ5fSHQn1La051LnicXOKem9Ndc538MAUzn6GpaNWGXdVc17Sx73IC2GlRqrXkBb89Af7JD032Qb0/640?wx_fmt=png&from=appmsg)

**看到附件处有一张证书，再看左下角有个敏感词** ***filename***

# 7.任意文件下载

**右键复制链接地址，粘贴到 HackBar 把 *filename*** **参数后面的值删掉**，**访问**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbDuODx6IVfoolxlCvjcnoicHIrN429zgyoz1TBvZ3jg44icIp71Libr5vcfsWBTjKVEptVXNycgo7fStnsMibJM7PBGJ0E6YhNKsyA/640?wx_fmt=png&from=appmsg)

**用../测试看看有没有 Web.config**

## **8.经过一番测试，使用三个../可成功下载Web.config**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCuZ0Zjxiay4icGJt9MUe2KDy7YiauxNgdfMskDQe10kLJVUwtLsRuJ5U45m1BBIK56ENU7hicfUPhXhVWKs3fibZmmBZCzOvpyaWIM/640?wx_fmt=png&from=appmsg)

**其实经过图7可也发现 cet 对应的为 upload 后面的目录**

**(反正就是猜吗，猜一下又不要?，?)**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbCc3o7cOCWGjxdP7OodZjNqZkzpkkev3ZQP9jXSEIjKsjUmJBkGAZcJttYTJWQzKUCibcdeg8FnmKaeslr8xbiccNIeOM3KibnBZA/640?wx_fmt=png&from=appmsg)

**经过测试呢，确实是，也可以更方便下载文件**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbATia6xpXv5Gve1ROwcgZnobRypZRmHGycuU5kGPMudgFIXkOLQe1YWOLUgEWs38iaKYQOJuKleCic46hzsUy5czUyQCib3RNiawu4g/640?wx_fmt=png&from=appmsg)

**一个中危到手，嘿嘿**

**查看 Web.config 发现有数据库ip账号密码，尝试连接，连不上，这里就不放图了**

# 9.尝试Getshell

**没头绪了乱点乱点**

**望着这个四六级证书的链接发了呆，想着，四六级四六级我TMD又考不过**

![](https://mmbiz.qpic.cn/mmbiz_gif/Qzel5kQIPbAURaibqibJLuY4DagXicAY7T4NLEdNcicO27ta2GVpR9L535gyzyMM5hFcpyN31Uh36ALpBaleeHpBClBgzBjuCa0wyfTxdDY6Ybo/640?wx_fmt=gif&from=appmsg)

。。。。。。

**咦！猛地一看，嘶~这个不是把大学名称拼接到文件名里面了嘛**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbDmDd7mh18aWmv7bA7vY4XUW9gwfGsO2Fpic2Ru9Ta7EAa3JpOyo7ibsvHTTxibnDLbEYcF4fLEKTVkvgX5DxkukqCT7pVeMA9elQ/640?wx_fmt=png&from=appmsg)

**那我不是可以构造文件名来截断后缀！！！？？？**

**说干就干，先在本地测试一下先**

## **10.上传测试**

**在本地测试可以发现%00截断是可以成功上传的**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbBHJ0BkiaK2vyJhQtfsOfkIaxIcjd2YKadJ9lxcZU2ulWoR3K6fmUszN4YdTEZTiaWibdQmnsFG9I25vsDW3JAflb4iaagbxlVars0/640?wx_fmt=png&from=appmsg)

**先不截断，上传文件看看文件名是否为我所猜想的那样**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbDhRCplicnmCYia8ETF1BibAC3OYNia32Tz4bXFicDLRb82FmvPr52E5NsdJ6utPQ52MP0ocKwACaIaibh8tCQE5gMYiaXukEDzaqQTmY/640?wx_fmt=png&from=appmsg)

**芜湖！猜想正确，把大学名直接拼接到文件名里**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbAmfUKMaAKYu09d4dBqblGibnq32RvrodSiamLhSkAEHSTKw4x0iarDAQJb3kaenoKEEHbxErAS0JfSJVCSPrXibsVxQxracScy5hs/640?wx_fmt=png&from=appmsg)

## 11.想法很美好现实很骨感

**使用%00截断**，**就快要成功啦，好激动**！！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbCfvFma18wxuiciaicDos3MgKsH3k9xvg6IhPJicn4eZJXWnKpjZ2cqsDBjNPGxJRZyEV9gDN5rdRFwbKaoHsTRZuxXc9SqwAt2QSs/640?wx_fmt=png&from=appmsg)

**小手一点，上传！**

。。。。。。。。

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbDH8cXadKUIyfgsGXKic8IskbKAHRcvpgzqrHyXxtFUPuxUWVezgmMXTyE2zTiagXJUyS2AaiavxCRbZB4TLqPxu856bcj5da0AFc/640?wx_fmt=png&from=appmsg)

**没事，那就换种截断**

**使用 *::*$*DATA*截断**

**em。。。提示保存成功，但是文件呢？？？**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbDhKqU9UDNcKU4nbvzCO5mDTIDFrMPcAMXBwictqp0H9HeucT7AIdBuVu5oAyspz5FwXLmeNxwJfAniaaC9ZfgyMP1mvQ2YxW734/640?wx_fmt=png&from=appmsg)

**算了，那我自己找吧**

**通过上面任意文件下载爆出来的路径可知该文件在X:\XXX\Content\upload\cet\目录下**

**文件名规则为：年-月-日\_姓名\_学校\_四六级证书.jpg**

**但是我们截断了后缀所以尝试访问：年-月-日\_姓名\_qwe.aspx**

**访问得：**。。。。。。。。。。。。**不可能吧**？

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCm6SPu7Jn3HYSYF8GfWoICruFaMiaadqo84BRFy2FONBf6VB63gUGaZI8omhe86IEcHfgcvPmfIQ1iceGYuCMufxryyBPwiaUQZY/640?wx_fmt=png&from=appmsg)

**那我访问正常上传的四六级png呢？**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbDATjyue1Ia9UH0nRicapDhHCYE4XdDgOztFUcaDyONiaJ7dISUYXHOliaebRg5iaGD19bssULC67Y12IbuskUGfOSaUHdKcibNibP54/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Qzel5kQIPbAXYTZAnSRTQjeBF0LNmSDibfNwXC5btiaG5YBktBT9Uu43eicsMGPKrMnlQXksUibl4Fr4MU5m0f14Zia4z0Sz3iaYRd3Gy1EgQYiaes/640?wx_fmt=gif&from=appmsg)

## **12.寄！**

**这特码下载得到，访问不到**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCECVrRGCEtVL10UlwuFehrjzgTc4V6bDB6cXNIc1C5teX5pQPBdrXRGoQKzuLicm68Y3ooRHyWU3kia2bicic3bhAmMD9eibCvZwCk/640?wx_fmt=png&from=appmsg)

**太狠了，期间我还在想是不是以 \_ 替换了 / 来当作目录，最后测试无果**

**应该是做了目录限制，不允许直接访问这个cet目录**

。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

划水划水划水划水划水划水划水

划水了好几天后

# **13.尝试下载源码**

**（可是。。没有玩过aspx啊，而且这还是个MVC框架的，我一无所知呀）**

**尝试使用任意文件下载 index.aspx(无果)**

**尝试使用任意文件下载 Default.aspx(无果)**

**尝试使用任意文件下载 Global.asax(成功！)**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbBNvXrzfw2RyzgmnvWyAz1P658CibIGsQMcfL19vjYTUG5bye97o6NjIl5jZdyyXuibxsfIhBSSLHS3jhRKbU69icwtuTjF046km8/640?wx_fmt=png&from=appmsg)

**这。。我也看不懂啥意思啊**

**这目录结构是啥样我也不知道呀**

## **14**.**于是，我决定去网上下个MVC源码下来看看目录结构**

**下载的这份源码叫Leavescn-v2.5**

**大概看了一下，好像还真像那么回事**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbB5trLYke05ibkaWoib9sgWH8NC35lO9SZXlprdDa94aicKonDkStIW2DG6LF3KkrQaAwDRknoYicoqqnt64hiczzFy0c5LJWcxzLQE/640?wx_fmt=png&from=appmsg)

**进到bin目录发现一个System.Web.Mvc.dll**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbC419TxR6SarUlbRJ3ajiaq2nMXtkkhRNBbmcibVoc5ZX8ib3RS2gnRkUfw55pfPmUsPLWXFziaqjqGhpWOJmamcY7tMYNuwnicK2Qg/640?wx_fmt=png&from=appmsg)

## 15.尝试下载**System.Web.Mvc.dll**

**嘿嘿，还真有**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbChRCXRYrZJWaPNHNibyKqmc1XN2Y5fQVcicAziak2mlnAib60hJes6EOanico93V8qNZ9WYlJguJCplbNYcvWuMHEqjUYgXce4YkTY/640?wx_fmt=png&from=appmsg)

**下载dnSpy来反编译看了看**

**发现。。。看不懂，最后问了一下大哥，大哥说我下错文件了**

**。。。那我怎么知道代码在哪个文件呢(来自小白的疑问)**

**尝试下载其他文件无果**

。。。。。**继续日**

## **16.对比目录**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbA2iaUoQjGrCjmqwumMwDBIOBLbW6EzHVVTPluVyYWpraibmpX8fa1LSmdRvvrYZicKMsHhiay3KQ7GtgNbnw8BTObrkYT1vu2YYSY/640?wx_fmt=png&from=appmsg)

**在该bin目录下有一个MyWeb.dll文件**

**那我这边也尝试下载**

## **17.找到真正业务代码**

**成功下载该文件**

![](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbDlb3u4jkDc2J4UXOW4XTTicZicEtyywbR3c72n4EhO4AZr6pyq0yHVjXL5NcN3vvUibD2tIG3ZFc0zqFrzXluGIIY9bqwUiaf7EcQ/640?wx_fmt=png&from=appmsg)

**丢进dnSpy找到下载功能的源代码**

**Download传了两个string参数**

![](https://mmbiz.qpi...