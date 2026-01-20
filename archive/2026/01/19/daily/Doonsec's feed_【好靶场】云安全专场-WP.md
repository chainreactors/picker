---
title: 【好靶场】云安全专场-WP
url: https://mp.weixin.qq.com/s/HiGlt_27wdKU8GZoSS8sSA
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:35.888579
---

# 【好靶场】云安全专场-WP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw24I1gcybTavbWKyCA3b30jkBGLwmic8XuB6N6TxcKGk5Q3j0Sud1o3MIibUjVlib6PbuwjA5wEkTKAw/0?wx_fmt=jpeg)

# 【好靶场】云安全专场-WP

原创

track
track

泷羽Sec-track

![]()

在小说阅读器中沉浸阅读

> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！

**往期推荐：**

**[【工具】Shiro反序列化利用工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489273&idx=1&sn=89c2855997f7c0317211bb21b7c3bdb5&scene=21#wechat_redirect)**

**[【工具】Sqlmap中文汉化版](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489242&idx=1&sn=67c1cac7a017a4f1c57e97fc415ef6fd&scene=21#wechat_redirect)**

**[若依(RuoYi)框架漏洞战争手册](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489224&idx=1&sn=a59ca4e14728e9a03b38223b57f39447&scene=21#wechat_redirect)**

**[【工具】多平台GUI图形化资产测绘工具，支持一键导出](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489051&idx=1&sn=c1dcbe17078b6ed0bd16e7d061bae691&scene=21#wechat_redirect)**

**[【SRC】记某次未授权导致的20多w敏感信息泄露](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489015&idx=1&sn=175618374766f6a199b21baa981bca8e&scene=21#wechat_redirect)**

**公众号：**

靶场url：http://www.loveli.com.cn/findbug?keyword=oss

```
注册邀请码：5a00c6cb8645461c
```

## 前置介绍

响应类型

* **未授权访问，包含路径**
* **AccessDenied：访问禁止，做了权限**
* **NoSuchKey：访问对象不存在**
* **NoSuchBucket：访问存储桶不存在--》可尝试接管**

## OSS出了什么问题

打开靶场，存在如下内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jyiaQFdqTSxvIg5uRaibiar89dk6kicaDKSlsxQViaTV2nUf4nJY0e3eN6qQ/640?wx_fmt=png&from=appmsg)

提示flag不在这里，注意文件名的后缀

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30j2oOOdCFvbMVR9jKACQXEibgghAwYsib0sT1nzPvNW6V5icxPSLpG72EZg/640?wx_fmt=png&from=appmsg)

不存在列桶

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jjlXHpjORl7lBXfZQzaRMwRdHqRqYe8zYvY31sQJb5CaOPobpzTIEeQ/640?wx_fmt=png&from=appmsg)

注意后缀，存在一定规律，三位数字，burp设置爆破，成功获得flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jhLajibtyQo3AWyNhToUrZ8JvEQT39QmA9jjnGqZW4zQgSA9yAibc7DOg/640?wx_fmt=png&from=appmsg)

## OSS出了什么问题2

环境--》文件覆盖

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jfT21rF0L52bo0xzO9uBP8JVicFKyl0ldAgXM4RuQIcFLfibZPPgWoibPw/640?wx_fmt=png&from=appmsg)

访问flag.txt并下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jicgdEnljib3iaDtJ1BGEdMVkfZvXibia39OOad7thKQVZ8dAdoicG86a9wmA/640?wx_fmt=png&from=appmsg)

打开burp，随便上传一个文件，得到提示，这里应该就很清楚了，为了让大家练习一下文件覆盖，日常渗透中，有了明确的文件路径，如果存在未授权上传，比如PUT方法，就可以尝试覆盖其他用户已经上传的文件，比如头像点，进行覆盖

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jvMRkxwYhKPpeAETiblpBozFhziaphnLEvlYSznlD5iaUY5Lb2qJ1SpfWA/640?wx_fmt=png&from=appmsg)

新建一个flag.txt，然后上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jicPmw0pibM1cZ0TTE9CebQYmibK238EZqfuAZrlvjewuCmBQn65wKtrlA/640?wx_fmt=png&from=appmsg)

然后再次访问初始url，下载flag.txt文件即可得到flag

```
http://haobachang520.oss-cn-chengdu.aliyuncs.com/xxx/flag.txt
```

## OSS出了什么问题3

根据提示结合之前的域名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jcdpk6SGH08LL6BZgZakXohOOy9CMBzrbHrYOPm5oYX83HIR86hp2Cg/640?wx_fmt=png&from=appmsg)

访问url

```
https://haobachang522.oss-cn-chengdu.aliyuncs.com/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jDaZLgXWmq7nRD0eNMS6OyhR59yB3IDM0yh58jx7Dficz5QQQUIC8Lnw/640?wx_fmt=png&from=appmsg)

备份文件扫描无果，JS文件存在AKSK泄露，LTA开头，是阿里云的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jNveFEdgGYd1j8S6ibqZ0j1PFfzibJdtr1qDW0yaSV9ySblQOo6XVQLeQ/640?wx_fmt=png&from=appmsg)

使用GUI云管理工具无法连接，不能列桶

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30je2BGiaXflt3fnSDJxIicoGQ7v9LQMCJvNFO3Rk9Z8HEBEyI5ulLrBwow/640?wx_fmt=png&from=appmsg)

换一个工具，命令如下

```
wget https://gosspublic.alicdn.com/ossutil/1.7.14/ossutil64
chmod +x ossutil64
./ossutil64 config
./ossutil64 ls oss://haobachang522/
./ossutil64 cat oss://haobachang522/flag.txt
```

配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jdaA8URVadYVgZEpX5e9aQES4r3Antux2YaG24pHhK9BptbZ0y3alfA/640?wx_fmt=png&from=appmsg)

读取flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jQW4xsEYCicAHliaQKLPYKApze1tKcDCibV5VvmnaFQibf4PHpBqeLiaYFpQ/640?wx_fmt=png&from=appmsg)

## OSS存储桶接管

> 通当管理员在云存储服务中创建一个 bucket 时，该桶的名称是唯一的。然而，一旦管理员将 bucket 与自定义域名关联，通过DNS解析将 CNAME 指向 bucket 的域名，就存在一种潜在的劫持风险。 管理员将 bucket 删除后，没有将域名解析的**CNAME**删除。这种情况下，因为 bucket 的唯一性是在存储服务层面而不是在域名解析层面，攻击者通过**注册相同名称的 bucket**，上传任意文件到新注册的 bucket，攻击者就能够控制原本与域名相关联的内容

打开环境，请求flag.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jDVemadhCXYw0aKIyPus7Uanxm0drD58WGCTSNuxUgCyiamdoBbOpIcg/640?wx_fmt=png&from=appmsg)

访问域名，提示存储桶不存在，但是我们可以正常访问到，存在接管的可能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jIgsURcKzcxFrst2qdGHJzsv8TkMg11FItGicHB7f0hKqlXs4ic85hHQA/640?wx_fmt=png&from=appmsg)

打开阿里云OSS控制台，注意url名称

```
https://hbc917867.oss-cn-chengdu.aliyuncs.com/
hbc917867：bucket名称
chendu：地区
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jW1y2p4ebT1R3ic2hJvuH17nnQoibDzX1tVuGk25LwhJ7YiaThc5ssDaQg/640?wx_fmt=png&from=appmsg)

再次访问，可以发现已经接管了，默认OSS存储桶设置的时候是**公共不可读**的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30j972OBA6BDp9Qwo7cZMeNAsTZrzc9qmhyVViaWrdEeZ1h1DP2An7u5pQ/640?wx_fmt=png&from=appmsg)

由于一开始的域名，flag.txt是直接在域名后的，所以直接上传同名文件到根目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jbefEItAicyo4IUWJN3Oxicf9MLPJCEv9FARwnhHEHJ5aB5tiajtMdwibOA/640?wx_fmt=png&from=appmsg)

上传文件flag.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jbln9xqKGF5Cf9LykNFB0MiaiasSCF1h6jTul1Bn5V7d1qFciaIBIYuJAQ/640?wx_fmt=png&from=appmsg)

此时依然没有权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30j3QRU6YibYjaDc102ELO1qDLRsqxDFx2WmDtOwbSwwf8wz1oJrZ9ia2Nw/640?wx_fmt=png&from=appmsg)

关闭**阻止公共访问**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jmXAUrTSD6SWrsibjRWIVLVvsC6cypfsKtDNLH6tJIb4GWFsz0xtwwvQ/640?wx_fmt=png&from=appmsg)

设置为公共可读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jSKbfnI59TNEpmvrH4K5jkPSjcWjAkSpbfBbtzmGOibCadgyTvYJt4eA/640?wx_fmt=png&from=appmsg)

此时就成功接管了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jgfXZgvwNCH2ypxgMmcDiaSSiayceefEVvoFpyawwmAendYicD1ORPgxyA/640?wx_fmt=png&from=appmsg)

## OSS存储桶爆破

靶场信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jrxzOcsm2Du9jmh0zM8KrDfcY2qpvPOWibsXhsbtrKrQwab8kiboWKUGQ/640?wx_fmt=png&from=appmsg)

需要爆破桶名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jROYYicuTw4WdykZ1d4ia8hwc22icaDa9MYx0HzZHtxuTnAERTawMTg2gw/640?wx_fmt=png&from=appmsg)

打开burp，如下配置，两个payload均使用数字，组合枚举

> 日常渗透可枚举桶名/地区

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30jTC9cvKQxDLq4G8bwicL6glEhUhO607bWtkTGpInBRgzcgKbWlMIwTfg/640?wx_fmt=png&from=appmsg)

403访问禁止，说明存在该域名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30j3ae5nK3KweetTkO3h8ycv5QjwAm1yRtnLdia4gVlrUPqGzPicjmicSXQw/640?wx_fmt=png&from=appmsg)

之后去获取flag即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw24I1gcybTavbWKyCA3b30j4KOysyqUyxQDnRwjmUkcteDLKuQcAYbwcUZAKQAEpVuFb9lGCRMHQw/640?wx_fmt=png&from=appmsg)

## 知识星球

**可以加入我们的知识星球，包含cs二开，甲壳虫，渗透工具，SRC案例分享，POC工具等，还有很多src挖掘资料包**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2ob06EicM7DDKBlMjOVw0mmNOVKLafx8sRvQbcCQ91ACGG0DWnFb85TOIUSQBgWWmibMSa9KiaEfQXA/0?wx_fmt=png)

泷羽Sec-track

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2ob06EicM7DDKBlMjOVw0mmNOVKLafx8sRvQbcCQ91ACGG0DWnFb85TOIUSQBgWWmibMSa9KiaEfQXA/0?wx_fmt=png)

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