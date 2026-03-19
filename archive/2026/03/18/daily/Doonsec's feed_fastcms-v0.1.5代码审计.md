---
title: fastcms-v0.1.5代码审计
url: https://mp.weixin.qq.com/s/xmpM_v-Ozvccw2vJyLIyEQ
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:18:50.064444
---

# fastcms-v0.1.5代码审计

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tOrb0WDic7icj6oZF8L6lPJfJiahn2MFIeXTWb3eaMQxq41Cp9fjlB1JhRYibqxOl5KrB9g2j2CXYDamaH8iaIXOcr2gX9DR9laQNxIDawpVrpOE/0?wx_fmt=jpeg)

# fastcms-v0.1.5代码审计

信通云服
信通云服

信通云服

![]()

在小说阅读器中沉浸阅读

Fastcms是一款基于SpringBoot前后端分离架构打造的插件化CMS系统，凭借高度模块化的设计实现了优秀的可扩展性与可维护性，可高效完成网站搭建与微信小程序开发，是构建微信营销类插件的理想底层平台。

# 一、SQL注入

查看项目加载的依赖、项目说明文档、全局搜索可以判断项目使用了MyBatis

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7icjNGxGC0803ynrlDIyNB2v4kOYZqd6UyhGujuORnYF5ibjoZFY7Rr98XhkNBMHOQom3eF4afujfNaYYuLMpmlOTb1sQvgqdu208/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7ichlVNmzloicWSJXL2PmicWht11kU8icckBicbPdwkg0sy3qzK3Lia0V6cZk8gk4u5EyJKAlYTBDGbwmatEkLE9jGrlL3NpriahnwSibbY/640?wx_fmt=png&from=appmsg)

当使用MyBatis框架时，在使用like、in、order by时不能使用预编译，可能就会使用${}直接拼接，全局搜索${定位可能存在漏洞的地方

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7icgxnbb4MjYriaICglQhmp8SfXDWib1fm0WTunPzq9YTS0vk60jTCib2GtHb7z5TXaInY9ucicHvXQuzsJcJHaNu9PUbaAyXn5IrsVg/640?wx_fmt=png&from=appmsg)

分析存在sql直接拼接的情况，${ew.customSqlSegment}直接拼接到sql语句中

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7ichAH5CUcLmJ7zI4R12rYtnBmWFpHXg1FYjic6mSOaNIodZn2qFGbYcs2GpQv4LJFqk6R5ppDv2XosibF5JZXHc5EKAjMTC9BQlicc/640?wx_fmt=png&from=appmsg)

找到应用程序中调用pageArticle的地方，orderBy为可控参数，由于order by语句无法使用参数化查询，直接拼接用户输入会导致SQL注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7icgGJW77sXm3yI8fk8ur8eYlDasw9Mibk7uzKRE40sowdgJ0NX4iboP0AX4VibNjibsnRKDHglMdp8KHEEFibSu3kTgQ0Iht1Rz0xVt4/640?wx_fmt=png&from=appmsg)

然后分析接口路由规则并定位目标路径，完整的路径为/fastcms/api/client/article/list

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7iciaftslyATHvo5U5J48tSW0DaZfdcMKP9EWDc5CQAzZro7pRJ3YuEyRMDib3QdKsjyGichBh8KIomokjaPOW5f80fzv0YzUcTqNUw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7ichp8ZcsGFq1qcBlkibNOIgtghD6UWAect1nNPsibJGetIc8w36ywOv9kxaOkdSqFrAdDk3ibKEP6dMHahJ3mfpicUbWrbb0PKliaVlM/640?wx_fmt=png&from=appmsg)

或者看注释信息，大概是与文章相关的功能点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7iciaAgiaAq7JEkNEMPTFDkPslxp2Eib2zpYr6OjIOo1icySIQHTK0wZApHF0YcOReNSa6Q52E7RNVCtqM6P25ibESMB3LHz9IUHYPe8s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7ichNibfKzboc5SekbYOzsf6ia8eaKCmx96TIiacGKmlb9KNkQb0kSrUG1KryYGDO9oc56eMBM7azV6Dic2ibGaXB0m7aNoWR2QFa3X3Q/640?wx_fmt=png&from=appmsg)

添加orderBy参数，构造POC进行测试

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7icjSibJt8oBZ8r5QDJ5dqX5YeOa7kKIdlRBaPiaZHja0psXqHNYiaW7RNnn9QJMmzLibMicib3n3Lmn9k0wHfWQnlic8ojcD7dyoZwjlgQ/640?wx_fmt=png&from=appmsg)

# 二、文件上传

审计上传模板文件的源码发现，代码只对dirName做了路径校验

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7icgs9oic5MTnBtZXEQndksBmZMYY7HcN9jpfkP0e7BuzYSEfskPpf77B3g5jdXO2AomOh9r23wm4JMLghD5TGHIpKNJSicRjCNBAk/640?wx_fmt=png&from=appmsg)

由于没有用户对上传的文件名进行校验，直接用file.getOriginalFilename()拼接文件保存路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7ichtwnwEjjml1OL1c6ibciblEWUW9KicglGoHpDydByxavYcmH6WYNZk0jkJb3nc4EcCy1OGqQH6y4wUQrfyicAQOhxTDsian2ORCZ7U/640?wx_fmt=png&from=appmsg)

导致可以通过构造包含../的文件名，可以突破目录限制，将文件上传到任意目录

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7icjZvVN0yEEG0cVR0ibHfy00Nw4iaoWyV0Dc3gPXd6TfJsHZRcAT8sF0qNvVn2dSBpiczeCiaeQViaHRkudmCwTErLeCWraQsFFtb2Xg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7ich9q9vK8icbEPETa3rd2eR6ZydQzVDeLnUPBVkMfJ24ZokOu9hY677bxInDFzSYicIsKs4xqTGBF6ePhfWfiaqzuYFb09erM3W0Ig/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LI0hzbSc8PbZj0wlf4RzQLdk7nrUiczuKr7Ev999EricU2FxD6zGW2My69yUaycXdf8wJAaeNoevYB0KBO7rRbqA/0?wx_fmt=png)

信通云服

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LI0hzbSc8PbZj0wlf4RzQLdk7nrUiczuKr7Ev999EricU2FxD6zGW2My69yUaycXdf8wJAaeNoevYB0KBO7rRbqA/0?wx_fmt=png)

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