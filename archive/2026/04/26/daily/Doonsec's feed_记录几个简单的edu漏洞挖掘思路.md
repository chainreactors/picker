---
title: 记录几个简单的edu漏洞挖掘思路
url: https://mp.weixin.qq.com/s/5H6akWNhxIVosCiXm_Gw9A
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:02:10.727590
---

# 记录几个简单的edu漏洞挖掘思路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R9d0DzJpTeLbOW4ib2JmSRYa0LVJsNcic4kaatvePEzbHOJ8gbCFzrlRibLo9BooCibMrF5E5jCD8DRzDnnXwibN222pVaYic5DObkibAKibKOmUUYE/0?wx_fmt=jpeg)

# 记录几个简单的edu漏洞挖掘思路

小轩
小轩

响应云Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 响应云Sec

#### 免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者
间接的后果及损失，均由使用者本人负责，公众号响应云Sec
及作者不为此承担任何责任，一旦造成后果请自行承担！
```

#### 0x01前言

各位师傅晚上好，由于最近没有什么空就没有发布文章在这里和师傅们说一声抱歉，今天分享的是edu漏洞挖掘思路。

#### 信息收集

很多师傅都抱着一颗出漏洞决心，但是发现一圈下来没有毛都没有发现，这个时候自己就开始怀疑自己。师傅们有没有想过不是自己没有能力或许是没有找对应脆弱资产？？？

```
比如你想搜索充值入口 你可以在微信搜索 职业学院充值/缴费 （微信小程序的最多了）
或者 xxx技术学院
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeJbGZ1A71gJcpvVNA4wiaOgeB89mFaMx0JiaJCvM5ibUwQbHlm9g4hcT1SF54ibwoicnQ2ALwTSga4QPVFpJhEBQC5LZBP2KMSRZ7j4/640?wx_fmt=png&from=appmsg)

### 文件上传

发现该证书站点小程序存在文件上传接口，我就测试了一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeLWaBJ0tTUa6E1ALrAeOMOMp6gs5fmc6h1vDJibwRDnD4RwJ6LYeqeoGUmr2jdfZTu9khNTXqVZhoKPw1fpwxBUadMDqaXjRRbA/640?wx_fmt=png&from=appmsg)

文件上传入口

![](https://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeKicPMJMzy914dd6ZbFhcNPDJeDw7JLH7UQUeKQOpONApWIvwI9J7ReBtbHYeRuicgCOBngvib5mqfZGiaV8LdfPoyOWS49I6y06MM/640?wx_fmt=png&from=appmsg)

构造上传文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeJgATX8iaOBfX6HaSytN3cEpK4Zziba58AnaAEFgib26IIKiaMU6GmHmLOSSk5jySGnR6xVvx76ja0Kqy0qacE3qpj4NmHCmbYoCLU/640?wx_fmt=png&from=appmsg)

回显上传绝对路径 拼接路径访问

![](https://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeLqN2ND1tQw3FqqwgHWs8zRTj3BJwC2jeG0D4KrQXA6ulEpNQiaXrabk5c6znxGFOib7DicKxAxX2qceDso47U6mUSp45hw1KRMib4/640?wx_fmt=png&from=appmsg)

发现任意上传文件，可惜的是网站不是php，jsp，aspx的都可以上传但不执行，后来就上传了存储型的xss，没有拿下GETshell还是挺可惜的。

### 未授权访问

话说回来这种漏洞就有点意思了哈，可以不需要管理员权限就可以 增 改 查,但是需要构造数据包。关于这个漏洞是怎么来的呢（通过反编译小程序提取敏感信息路径出来的）

工具推荐:https://github.com/Mstce/Onyx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeLMBtojPxbPR8SvmYqfziaa6JoH9OIvpzopBpwbNibtiaP5xZW2s0ibnCy9O7JLNIiakqmNaLmF9kvGoxjxjrgyKVQ3BHcugYZupMY4/640?wx_fmt=png&from=appmsg)

增加用户的数据需要自己构造（后面我会说这个构造是泄露出来）

![](https://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeJI9V3M2vrDDSS9Hj6icE4Llurnxkogk7heCjvia7r8JUnTSpCH2IKsef2vWuic1kfDfLpMY6y95WIk8U0WchuHsiaUJndf74dYROk/640?wx_fmt=png&from=appmsg)

这个呢是修改用户信息的，但是不能把用户改为管理员权限。 主要是可以修改用户的基本信息（名字 学校 手机号 性别 专业等） 这里我就用 谢志强的信息修改学校 改为91xueyuan，提交数据包，发现也是返回修改成功

![](https://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeI1zM7LyEhSzpeaIVXf646sqicP219xia9o2Zh4w6xT3sl9micVmwJ0nQVSpZDrsahlWqfEQZiajpL5aXs7eT4nxbhyGUqibu7vKwaY/640?wx_fmt=png&from=appmsg)

这个是查询接口可以通过（手机号 id  state:"5"）来查询。师傅们还记得前面我说的那个构造标准参数怎么来的吗就是提交了 'state' 这个返回 志强的信息去构造的 也是水洞一个，其他的接口也没有什么好玩的了

### 支付逻辑漏洞

某大学财务系统的费用缴纳网站，老演员了开局一个登陆框（首先测试了sql注入无果后还是老实的注册完测试里面的功能吧） 注册成功后 发现功能点还是比较少的

《功能点》 在测试过程中就去点击了，小额缴费发现有一个叫 汽车检测与维修技术服务师（高级）的缴费项目（要100蚊），用burp记录了相关的流量包，果然发现了东西

![](https://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeLDicP0icgzOeb0Q1gJMVxQ2ejFpghJl1umvuQqmtf7TsdVcB96W4m0NgY66icTvHGZg6VbNHbAtdB0JIaicD3oHl4gkQKcx6Xaic4Q/640?wx_fmt=png&from=appmsg)

```
usercode=61032419xxxxxxxxxx&zje=0.01&banktype=abc&clientType=wx&businessId=1493990161191665664
//usercode=用户账户也是身份证
//zje=0.01 //这个是需要缴纳的金额 我修改成了0.01

返回结果
{"errorMessage":"操作成功","traceId":"1497959654137921536","success":true,"showType":0,"data":{"data":"https://xxxx.xxxx.com/mpay/mobileBank/zh_CN/EBusinessModule/BarcodeH5Act.aspx?token=17772118150139582323","orderid":"ahzypt2026042600074","rtnMsg":"操作成功","rtnCode":0,"status":0},"errorCode":"0","host":"172.17.255.133"}

返回成功了，发现有一个url心想这个肯定是支付接口把他复制到了浏览器（他说需要到微信），打开了微信点了进去需要支付0.01（果然和我前面修改的一样，但是系统会不会有订单还要支付后回去看看）
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/R9d0DzJpTeL5Yjm3XT4JUFZCYibVRJbf8ArCGk2Do6cwibz4rROwbKHepK4J1pdFeUMibMiaJGSlM7O0J0HsMuyKialWnDgCxDrpy7RfQCNtfQHU/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeLIaPmclDsUSaPTUprawRqbYUN49Od8F5uHK0xgPhZ8jfRKqGk9f92RDFM6YgbRNq9M4DonVVCAljD7cfbdaT14PzqAFCLia948/640?wx_fmt=png&from=appmsg)

很给力，系统返回了支付成功的订单！！！

- END -

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeKDOjDBsWa5gSQdQh7QjycaRPIEPDV62WoMOibfcKYic3PZVZcFjZL0ZaW3XTfGNtJGyRSTAm7GeGBQjgibhVtdsck12nhbcHumg4/0?wx_fmt=png)

响应云Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeKDOjDBsWa5gSQdQh7QjycaRPIEPDV62WoMOibfcKYic3PZVZcFjZL0ZaW3XTfGNtJGyRSTAm7GeGBQjgibhVtdsck12nhbcHumg4/0?wx_fmt=png)

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