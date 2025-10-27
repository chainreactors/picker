---
title: 群晖无公网IP免费隧道穿透
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247490426&idx=1&sn=514c6bc07c0be1c0aab2092eeb996b48&chksm=fad4c66dcda34f7be94529067929bfc941a14643df955dba79eb6c99576d0d0fba9f2bfcf6ed&scene=58&subscene=0#rd
source: NOVASEC
date: 2025-02-26
fetch_date: 2025-10-06T20:37:49.684960
---

# 群晖无公网IP免费隧道穿透

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FG6IOBLtYHUMYA351icliaqOhW1FaGRlSBicKr2blYJSrstX9JVpx7Dmbxg/0?wx_fmt=jpeg)

# 群晖无公网IP免费隧道穿透

NOVASEC

以下文章来源于科技早知道Know
，作者科技早知道Know

![](http://wx.qlogo.cn/mmhead/naPHoFY2n5RiaX3070UwlZHdAaAIeYWoYic3Oicj7ffgvR2jVR1XEJiaDT21ZzYkVyduIG2bpIYnDUU/0)

**科技早知道Know**
.

✨「AI未来派」硬核科普站🚀🔥为您分享：✅拆解AI神操作✅狂薅AI生产力工具✅AI爆款玩法 ✅元宇宙新动态📩 评论区提问秒回

# 群晖无公网IP免费隧道穿透

## 域名注册

首先我们先注册一个域名，Freenom可以注册免费域名，但是好像最近不太稳定，官网点这里：A Name for Everyone

而且国内出了新政，2022年3月起所有域名都要实名认证，不然有可能会频繁掉线，所以这里我推荐大家上阿里云实名注册一个域名：https://www.aliyun.com/

---

## cloudflare托管域名

点击这里添加域名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGibAovmDIRbfl0YoCxhQ14XTKReCktibDGVqeNSwUxhqUv1VmHNQvpJFA/640?wx_fmt=png&from=appmsg)

然后选择这个免费的，点击继续

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGCvulbicwYJiclsD8QJZpFXYSic0esSbwaflUTb1hX7INQfLtcDRjZZ8kA/640?wx_fmt=png&from=appmsg)

然后复制这里的 dns，按要求修改就行啦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGmusnzFetScFpum88btjJLS6YTRxOn2uBiaVR1JAjyjCniaSehQZUkFew/640?wx_fmt=png&from=appmsg)

---

## 配置Zero Trust

登录到cloudflare，找到Zero Trust

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGGiaCyA6lMxUPrVs8m8icmbEdCtvdGsMa3jyicKQGy4bHaeN6Xud9piasCQ/640?wx_fmt=png&from=appmsg)

这里写个项目名字

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGO5oA68h1r7H8rOhNibXL8nLpxJOLgQXrWsvwB8QvIySnp2rDvibI5q4w/640?wx_fmt=png&from=appmsg)

选择免费的项目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGHzibg7ekYddST1H4g75QeQGlYia3VVriaey99sh99OIZ6AQLs6bVedaEg/640?wx_fmt=png&from=appmsg)

这里需要绑定银行卡，绑定完之后进行解绑就行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGiaibWUiaVJJLYVEVPyAZmd7YPNg7qS6l4diausURONVdUaBFStf23riap9A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGpj2J8PsMRDxWazFiae8GHcvymiblLk37gwdia66ZqTS4w1xaG9Zr3yiamw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGdAmvmLOLicF1ic3o5HMNgzpAEE3OvX8MsfCPCX7ulRaKxIticjVzp7BZA/640?wx_fmt=png&from=appmsg)

然后进来点击create a tunnel 创建一个tunnel

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FG7MBfANrj0ib5DFyCtlO6ibvOWSicSTHLuM0wJozhmE9OwDetlHS5ibeQ7A/640?wx_fmt=png&from=appmsg)

这里随便写一个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGOJp2TLr3VZOIu6RzGlCZ9gc1ySCVHUCF3SFQ8KHsbMKHj2mMbviaDEg/640?wx_fmt=png&from=appmsg)

选择docker，然后复制下面的命令

```
docker run cloudflare/cloudflared:latest tunnel --no-autoupdate run --token eyJhIjoixxxxxx
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGwIVFfJp0wZWx4k5VfLt3DmGvu5ERI1ZaoECYicZdmic2kBq11JEGkD3g/640?wx_fmt=png&from=appmsg)

## 配置docker

在群晖docker找到cloudflare后进行下载。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGJ5AACR9HCmu4FMG1Iula4Nc5HBia8QPbCmibgozZ1syYfdImAMiakNuLg/640?wx_fmt=png&from=appmsg)

然后开始配置cloudflare，选择高级设置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGCnxKicsSYd674aZBUOLerFibxGyYJ1OVnoUaBDJkk5eGtE5fhmbkOjTw/640?wx_fmt=png&from=appmsg)

在执行命令的位置贴上复制下来的命令，如下：

```
tunnel --on-autoupdate run --token eyJhIjoixxxxxx
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGFQYQPKqUNkWTUDia6eBmkyp3TnoHKGKNkicWNF41ibEUkLPEUSzw0LicFg/640?wx_fmt=png&from=appmsg)

然后点保存，端口不用配置，配置文件夹。新增加一个cloudflare，装载路径为/etc/cloudflared，然后点下一步完成就好了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FGQ8cicYq6tclwGBrWOZTF3YljiaoriaOTPkmhG7N2DZoOCvfANf3AlWQCg/640?wx_fmt=png&from=appmsg)

然后启动docker，可以看到cloudflare已经是正常使用了，直接访问域名可以访问到内网地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FG9EUfOr7dicA4gG1CyicqrYCUdrkib5QrQFTHAWfhrI5QUjmZzpLiaBsXAg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QUyQl3BlLgBVRXxhAZic01FG5Olo4b3szlaoox3x3XrmtxwUqDActCPOXEdFmcdZRKoiaEZCYPeLvAA/640?wx_fmt=png&from=appmsg)

## 多隧道创建

如果我想穿透不止一个端口那怎么办，其实特别简单，只需要再加一条隧道穿透规则，修改我们已有域名前面的子域名即可，操作如下 打开我们的隧道穿透Cloudflare Zero Trust

选择Access下的Tunnels 点击Configure今日我们已经创建好的穿透隧道，然后点击创建就好了

> 参考链接：
> https://zhuanlan.zhihu.com/p/591320825

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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