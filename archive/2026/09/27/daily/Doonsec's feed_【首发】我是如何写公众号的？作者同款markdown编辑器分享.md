---
title: 【首发】我是如何写公众号的？作者同款markdown编辑器分享
url: https://mp.weixin.qq.com/s/cKJKuw2cCdo2uEZPUZlY8w
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:52:39.371290
---

# 【首发】我是如何写公众号的？作者同款markdown编辑器分享

# 【首发】我是如何写公众号的？作者同款markdown编辑器分享

原创

仙草里没有草噜丶
仙草里没有草噜丶

泷羽Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

分享一下我平时是怎么写公众号文章的，以及我的背景，排版是怎么排的

在两年前我就分享过一次，效果还可以，后来就多了很多博主都用上了我的方案，文章链接如下：

[我是如何利用Typora写网络安全技术文章的，公众号格子背景又是如何做到的？](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247492406&idx=1&sn=b28a85786af68d5b3d67612b0594d7b8&scene=21#wechat_redirect)

以及视频教程

但如今还是还是有不少师傅在后台私信，公众号排版是怎么排的，在这个信息差的时代，今天就再来分享一下，编辑器这次我换了，换成了自己写的一款markdown编辑器，可以直接用我的同款主题，我主要使用的是

https://longyusec.com/tools/md/

![image-20260927120510379](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfNiba50XaJNxunzhCoaZNibq5tY99oxYMa4JXrRquLjbyUKztpbkbwspC1tMyalRNE5QqoHNzVA52LnUyr3icTvTSH7NgclfcvV9E/640?wx_fmt=other&from=appmsg)

记不住？在longyusec.com中找到在线工具，并选着公众号编辑工具即可

![image-20260927135201130](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfPAETdSgZXae9dmiaqTO4n8k3QhflgNwKIpalVqkFzmx8ld5TvVFKj95QtxZ9DRUkkhxrUZr99WEDnMoo91hUcZXkYajbLsrIKY/640?wx_fmt=other&from=appmsg)

里面内置了很多种常用的主题，古风、论文风、公众号绿、极简等等，可以自行选择，这个编辑器可永久免费供师傅们使用

我使用的是论文风\*白

## 使用方法：

1、写好一篇标准的markdown文章，可飞书、语雀等等粘贴上传

2、复制这篇标准的markdown文章

3、粘贴到编辑器中

4、选择合适的主题

5、点击**复制到公众号**按钮

6、打开公众号文章编辑器

7、粘贴到公众号文章编辑器中即可

以下是对没上过云的师傅们写的，**若知道怎么解决图片问题，本篇文章就可以跳过了。**

## 使用建议：

想要灵活的使用这个编辑器，你需要了解两个东西。

第一，markdown标准语法（支持原生html标签）

```
python# 这是一级标题（我通常作为文章主题）
## 这是二级标题
### 这是三级标题，以此类推

*这是斜字*
**这是加粗**
[这是链接](https://curl.qcloud.com/wOsuCOF7)

等等，可以自行bing搜索markdown标准语法，或者AI学一学
```

![image-20260927121215012](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfOCyRARLpwiaCNO4g7K1qlvA0dSxDDxlh72KGInE2f6HJGiaufsAkWPEQmvjsdXfUefWE02piamSQGKNXlwVpHibVFM5XS42K36pK0/640?wx_fmt=other&from=appmsg)

第二解决图片问题，图片是媒体文件，和文字不同，媒体文件需要上传到云端才能被云端的编辑器访问

接下来看一个案例

聪明的你将一个图片放在了本地的markdown预览中这种格式的链接，是放在本地E盘的特定地址

![image-20260927133018362](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOvSCNLGdR97mJAFhE3TvTqACgSsD2gNhY8fr1btkemVcFpsqVYvhG6WmcPsfdNrl9Q4eNibiavt1ial7L2GqqgBDKV7qLlVt9ibibA/640?wx_fmt=other&from=appmsg)

而此时你复制到编辑器之后是这样子的

![image-20260927133113924](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfNXmteKWIhZnEvn5m2Qe405eT3zG1MKsc7BhDvxdibLiblJ8SYtt5gH2hmFeFskQS7FtKRIANR3Z3quR83mdc5ia9ZaRCrib6BWiatM/640?wx_fmt=other&from=appmsg)

自然复制到**公众号编辑器中的时候，就是这样子加载不出图片的样子**。图略

而这个编辑器没有上传云端的功能，所以可以采用对象存储功能

这里我推荐的方案就是用**对象存储**，你可以选择**腾讯云或者阿里云的对象存储**，大厂有保障。我主要用的是腾讯云，因为可以白嫖半年

可以通过下面的链接免费领取半年的**免费50G**，续费也就几十块一年几倍奶茶钱，够用几年了，可以用来存一些备份文件，我主要用来存图片和做计划任务数据库备份，非常方便我们这些站长，当然也有其他的解决方案，比如语雀、飞书、自建存储桶等等这些文本直接复制到编辑器即可

https://curl.qcloud.com/wOsuCOF7

![image-20260927120251064](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfP2EjA3Nj3LpBzwokqS2HqhsKSNnj5IuokGOF0OX5OUWOfgo8y1eel0jMZgiabgulvpJZ8VezsnAHtMNrQuBMFXsfz12VswBRNI/640?wx_fmt=other&from=appmsg)

领取之后来到控制台

![image-20260927120405575](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOZ0LNZRptZwz0QTelR54hmBnR93S6MMvs4JMm1BiaZribWUSLIaRHnq0Etxf02p4238ITa5UP7WUFCpDXuJlDWibTyVsLXNWx1mw/640?wx_fmt=other&from=appmsg)

找到存储桶列表，点击创建存储桶，可以看到我的所有存储桶用了两年才用了22G

![image-20260927122022903](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfMczt6oXiam0TmqGibIdyyDXFbNZBGJibTgbYwOrIapyVkBPZ4UbiaVZoLq8ibBQkiboT9fIA9RbXBQUNG1eBjXIMCGMAjZATj5pUoJ8/640?wx_fmt=other&from=appmsg)

区域建议选择上海的，上海节点对国内用户友好。创建好之后选择权限管理，这里选择公有读写

![image-20260927123800059](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfP5Ky2nAVHDsHrvkQNRqVHBBGDkFic35ULvURnPhIwoiazX88lltd8k9CoH8ajwykQTO2VYZolQnnIVZo6zqWqBedSrgibG7W0rlU/640?wx_fmt=other&from=appmsg)

获取**SecretId**和SecretKey

![image-20260927124135785](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOdAmfjKG13tF2c1vp3fVxibhORA4TiallvgO8PCjX65Ra2TCN0Ticic4ONCgIYaRDgkxoy0ZqUia1icznMCHq4uwJ8SiaE2pMPulLFfo/640?wx_fmt=other&from=appmsg)

Appid一般是你存储桶名称后面的一串数字

![image-20260927124438425](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfMxD1oKH6h9YESWFG15NAnOiaHuwNI88A8tbn3dg8hTsGxnF7MJB6sGaIN4gMrzgzicuZDpibd0Ds06iaEVrc0238oFmePIdomTpG4/640?wx_fmt=other&from=appmsg)

随后在picgo中下载，新建存储桶

![image-20260927124527553](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfPFoMDoxMet4NNdlZMH4nJbcm3XPgHXG2vtwEmySKXVPKhOoOd3MS9TmC9LwaUGuehdS3icFAkLBRka5ibj68GPxEGvAWk7cXzV8/640?wx_fmt=other&from=appmsg)

配置好后需要在这启用，点击选中，并设置为默认图床

![image-20260927125338654](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfM1WgRBPUnGCPRAhEEqDW5mxZBFeJvDKXicfMM1Qb8W4jrpAw52GBPTSoG3o2kNRjrEyISMJNmuq6ybR6pMBsoDTJM5Ulg4IZss/640?wx_fmt=other&from=appmsg)

此时我们需要在typora中设置好picgo的位置

![image-20260927125656992](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfNsrph5kyBKicIH81wjGCbrTH04xq8qNAib31tXjEvmvXrm94UuJHEHU433caDTBjjuH9icrECmIxr6XWVXttQdNJkz7HX5Y9wfYE/640?wx_fmt=other&from=appmsg)

点击上传图片

![image-20260927125640202](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOWHYPl7NHesxgwM6y6Gv27dUuPhn6WMXeqtre84rVItL5nIlAHZNIy6iczLJrljtgv4PwDJdmB7hLVE3Y42jkjlonnAmZhLEEI/640?wx_fmt=other&from=appmsg)

上传成功后是这样子的

```
python![image-20260927122753146](https://longyu-1312988675.cos.ap-shanghai.myqcloud.com/myImg/20260927125710119.webp)
```

![image-20260927125726302](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfO72chgsGvO39jjqa8bRD1ibfFpUF5YmUYmiaXibvBhlPA0GK2kUicAIemf8BLXLt7zUZwE4SHL7cDXW5WmrvX7q3WB6VYWmuBQMb4/640?wx_fmt=other&from=appmsg)

这个时候我们复制标准的markdown文章，带图片地址的文章，就能正常显示图片了

![image-20260927125811860](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOJQlpsG3DwOKFuia2qlS6ickweb0DRA7HLtH1BmNeicsFMq6sZaQTPiaKWxSHm4Bb6OSGIPvick18h0LqRGFgicTYp4RYnwdoTJUYuQ/640?wx_fmt=other&from=appmsg)

## 为什么要选择对象存储？

我觉得最大的优点就是 CDN，腾讯云对象存储自带 CDN，节省服务器带宽，当用户访问你对象存储的图片的时候，流量是直接经过腾讯云对象存储的，而不是你的站点服务器，这样会以更快的速度加载图片，解决了大部分站点图片IO访问慢的情况，你不需要手动配置CDN，而服务器只需要处理文本加载即可

![image-20260927122753146](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfNl4pYeZYFeaw7WXQ4fTee51OffbOW6k3MvA88V9elhxFBTEowiawibLdiafWPscDeIJLCYGDywR0wHPeA9Q4hj7Pdh3AP2q8MPick/640?wx_fmt=other&from=appmsg)

## 如何节省存储桶内存？

首先是压缩文件，上云最麻烦的就是压缩图片文件，使用腾讯云的数据万象，对图片自行压缩的话，那么你每次访问存储桶的图片的时候都要消耗一次图片压缩次数，若站点流量月IP超过1000，平均uv和pv超过5000以上，每人访问一次你的文章，你的文章中有很多图片，若想要快速加载，每次都会消耗腾讯云数据万象的压缩次数，一个月又是一笔不小的开销，我推荐使用picgo的一个插件

![image-20260927123223991](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfNmLboe2iawnibh0O6IkY32mkrqgcZW3ms9eyjvsxfic5cwx80y5C5ytkwoQ1Lib9RE98BQib7RibhT5HiaDV5giaAv3YStReicaYQZ4EyM/640?wx_fmt=other&from=appmsg)

在上传到云端的时候，压缩成webp文件，这款插件是我魔改过的，默认是不能批量上传的，可以让AI魔改一下

## 如何节省上云的流量成本？

同上，压缩图片，另外做好站内防护，比如收到多次用户请求的时候，要对IP进行限制，防止刷存储桶流量

## 一张图一张图的上传很麻烦？

找到格式 》图像 》上传所有本地图片 即可。

![image-20260927140028709](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfPPxnX752Wqjr79LxCIbxXKpPcQJ3tP38hjeXeXxpxwEJicNou75F7H0Ie4TY9TiaXBEhN37icCMB3uPAv1L7gWuyfytOrOd69oX4/640?wx_fmt=other&from=appmsg)

## typora如何快捷上传到自己博客中？

这里我会写一个脚本，服务器端需要写一个php（因为我的博客是typecho，是php写的）或者你博客使用的后端语言，用来接收文章，可以让AI写

![image-20260927141013374](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfPUiaFGo6DtxJTIy4MLWBVuD79WG2JOgXUibMiaPwF5nrtIgaSCqrKNr77O9Wh58SpMm1SZKtyiacSQsVFeDOJbwoo1jl0yKrSROkM/640?wx_fmt=other&from=appmsg)

![image-20260927140908884](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfP2FJFeh2oicSdZ3J047cy2Cx8jbr0PE9rTQFWS743hYHcIcamHZxl7tjXS7ZFFcG1BH3porj7aYe05jnu9I6hLqJAR6icWn0w2o/640?wx_fmt=other&from=appmsg)

![image-20260927141211980](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOpmR22Zy9bJH56rpGQ1E2gpq3A6ic72GFXXJgTx3PItSoLlxjLfhOzrCoF9kxiaZZ4FWT7hPpWuia2ZqpLdibnuCo7mrmIAciaLKgs/640?wx_fmt=other&from=appmsg)

最后应用即可

## 资源推荐

https://longyusec.com/links

这是一个资源导航站，包含了很多的社区，比如src靶场，安全社区，当下热点，以及

![image-20260927133528704](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfPruQL98icR5CJx8d0PxegIo9f6HVjaZLBstUeHoNZn65jpeHdJzhPgsBSiaNyYLpSbB3bKPJYqUia99sB8A6xywztibwPlG0n1ebs/640?wx_fmt=other&from=appmsg)

![image-20260927133555719](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfPZZynEIcCmwcyRzYgFL1hGtbktICKZYU1WjdbK1qnGQ37SLmuTqd7eQM9PTzoLkRU3PGTSd3Pu8aufdNGzE658icvt4nV6OtO0/640?wx_fmt=other&from=appmsg)

快捷访问 **longyusec.com**

![image-20260927135333964](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfPibehvLNSIHtI4kjibOd99icMyhJeckYnPt008bWYMyY0fngVk2DnG2MVQice46j3X1LLfqp3GGlkTM00ibicjxJqdUIllibPl9lCiaic8/640?wx_fmt=other&from=appmsg)

## 服务器推荐

阿里云全场九折优惠：

```
https://link.aitq.net/RcgjvF
```

![image-20260721194150454](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfMc9o0at10wDoE...