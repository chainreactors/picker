---
title: 一条命令搞定黑龙虾渗透测试，接入qq和飞书机器人—.—openclaw搭建教程
url: https://mp.weixin.qq.com/s/bLh0NtZkmIyAPpSFXkeDwg
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:30:02.277733
---

# 一条命令搞定黑龙虾渗透测试，接入qq和飞书机器人—.—openclaw搭建教程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfPPXBVdCjbGeBr3ZiaIJbpdibc4kdOjF3Y53goV4w3icFTerIXj2nc0DH3u68LFqvqgL6hdv3b0htRzIbgOibuKHN32HdQGyZMTgAE/0?wx_fmt=jpeg)

# 一条命令搞定黑龙虾渗透测试，接入qq和飞书机器人—.—openclaw搭建教程

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于泷羽Sec
，作者仙草里没有草噜丶

![](http://wx.qlogo.cn/mmhead/Hp9HAaP9GFBKneKn5ryBUs0PRR7YFdhjkVm1EtmTw39DFXQog0cNn1NibPUo2tbPL2mH1HymCVxM/0)

**泷羽Sec**
.

B站：泷羽Sec，团队专注于网络安全领域的内容创作与分享，为网络安全而战。来自一个从零开始学习网安的见习生。很菜，不喜勿喷。

全文仅供安全学习使用，禁止对未授权的目标进行渗透测试，所造成的后果自行承担，与作者以及团队成员无关

历史工具集合：https://pan.quark.cn/s/f113bdb29fd7

## 服务器选购

服务器推荐4h4g，10M即可

选择这款轻量云即可

![image-20260309222714339](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfNGcSVNFoeLbVBEG16OWSichiczOrLIKX21MrBvEurNPMTaWHcXwPJhWW3mLekibqaKGliafH3dJUPgicb4sRf0YyEeW6eA5Mh6rib2U/640?wx_fmt=other&from=appmsg)

image-20260309222714339

实惠服务器链接：https://www.boheidc.cn/aff/QOWYLYCV

手机扫码：

![image-20260309223009879](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfOzTI97aTAicJJu7JL66KQZSpKfDzZb4HfhUZQ0DmS44VwSAtrpyqRZVhiac6zujZZMlhypreA68cBChgkHluZVqH29tonVhvkOg/640?wx_fmt=other&from=appmsg)

## 安装宝塔

一路 选y

```
if [ -f /usr/bin/curl ];then curl -sSO https://download.bt.cn/install/install_panel.sh;else wget -O install_panel.sh https://download.bt.cn/install/install_panel.sh;fi;bash install_panel.sh ed8484bec
```

看到账号密码和访问地址后，访问登录

![image-20260309223153506](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfM0DxqM2ibPlCsYG2984vGjOfy2AMR88Vo5luicoSSRDiaTzQ7vHLIvv5SibQscSzACr1jrTqxyCRxquqFcc5YXKkPDot3cmgVtgAM/640?wx_fmt=other&from=appmsg)

image-20260309223153506

全文仅这一条命令你就说是不是一条命令安装吧

![584_20260225111247707](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfOPVI2Liaic370EyrRkSMYtN5kR4pVoWMjuJicVgN5DSaX7now6ulpBtHWlT5geEt2GRvjfAc3BjkqMr3ickUfHheMIve2hQBHUmSo/640?wx_fmt=other&from=appmsg)

584\_20260225111247707

安装成功后，来到软件商店，搜索openclaw

![image-20260309200406827](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfNiahUS55vfBjJTOWN5d0hdD5HP0yuhZoTpu53RTLIR3EE4MIjkE4QLCMT6q1oKK4mrBSwticu2VWCMr3yjYr21M84kpDKCaiaC4I/640?wx_fmt=other&from=appmsg)

image-20260309200406827

## 安装openclaw

![image-20260309200525082](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPOvZonOwMHczNtGric4iazp4Tus4yk2PA7bZWMPFQA2gLsGq89yPfVAob7ib4uiaFMnkUzQfnSJ9ZiasBJ6gWKEAPicH2ibwTxQZN8j0/640?wx_fmt=other&from=appmsg)

image-20260309200525082

## 配置deepseek api

用一顿饭钱试试，在deepseek开放平台

https://platform.deepseek.com/usage

![image-20260309204056654](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfOIOKeiaMeD0vroajFKuRD3QkY6SYnoibic0OuuzianKcGR3AnsH3QvRJMGTghCXTVaMhWMTHTv84FJcRWzVOGgcPSnbfJ5Gg3ZfnQ/640?wx_fmt=other&from=appmsg)

image-20260309204056654

创建apikey

![image-20260309204129069](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPmn1icfXoQfQFJLtskRwyXSvT3tsSWLOwszG7Df6p0ZYYfkJ3pICt4BjXlNdo08DIsRUgDom0wvObz8zSO9ZZfMqgWF6hMYz68/640?wx_fmt=other&from=appmsg)

image-20260309204129069

按照我的配置来

![image-20260309204338293](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfMC00QNiaSRZjhPNVCRFPicJXDLHfpxJjuJibYejO05iaaEhvwVMbQM8iajVZSiaxEoO2mgv5XUgSGD2Ru58Fv52woOzPVrySWzZOFFQ/640?wx_fmt=other&from=appmsg)

image-20260309204338293

在访问信息中能看到openclaw的访问地址

![image-20260309204528155](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfNKVMZTblFV3O83CyJU4vr52KzO6lB34cujQ9taHvDczQD3ePTkwlXIcWL6S37RnbFroSRBU1mzNdUWwiaGMxMZxTjhgmyQkG4s/640?wx_fmt=other&from=appmsg)

image-20260309204528155

访问之后，在概览中设置中文

![image-20260309205819288](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPqS2qlYjccCcPos2OH4iaAhWDP6XkylAcbhibl7rqhnoq0IzglDFSn1KZcfjMwDB9RZkr5lyhtkAlicxCSSz9h9UMV6lsTrlQTeA/640?wx_fmt=other&from=appmsg)

image-20260309205819288

## vulfocus靶场测试

我们去vulfocus中开启一个实例（vulfocus是一个开源的靶场学习平台，不存在未授权进行渗透测试，所以可以放心使用）

https://vulfocus.cn/

![image-20260309213006218](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfNGCrzXia8xjwKB3a6MtZLd550uheOq8HUD3s37IjNLg7QnN996KCNNzW6v9GXcOjoEY3lU8tMibFQH3Ip30ZCBvPmib3jxlsUvMY/640?wx_fmt=other&from=appmsg)

image-20260309213006218

我们给他一个任务，帮我找到123.58.224.8:53257这个靶场的漏洞信息，帮助我找到flag，增加vulfocus的积分

![image-20260309212817920](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfOzUo0bcjlhj6hNPb9c42IlUIOlo7yE8wicOq8DwkndB8pvC3aCNxibpvIzxmeA1btBeQ5ibicFfrmMThqRicMnUPUu8fBU6PJVDMug/640?wx_fmt=other&from=appmsg)

image-20260309212817920

发现了git泄露

![image-20260309213200912](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfOvWjAVpRBFsI2EmmXgR8BevLiajicaYLn6p1aPusyCoSrPd4Mia95d1LjXicjlgnVN2Nugum30XN5xuCdiaZ7kF9UOQXv9ArS2fF6E/640?wx_fmt=other&from=appmsg)

image-20260309213200912

让我们进一步验证，很明显，是git泄露

![image-20260309213146430](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfP9bQo8rhSicBMRfmIjbRhYZrql1utxDyibIzJnajk47NMibQbsZ4etuImiaKxVHB7ZkK6WacY5QEQ5aFfia2nO9xnxNWAAv7m9EiazI/640?wx_fmt=other&from=appmsg)

image-20260309213146430

然后这是一个未安装的界面

![image-20260309213936634](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfM18BrpYicuXu5xYXjqGVB4T2AhUEbaehtgia4nialaHDjxHCPMWWbic4oMSswH80GmqFZULXjkCicbMI2paKw3qJXtNiakhRBcXOm50/640?wx_fmt=other&from=appmsg)

image-20260309213936634

它会自动开始安装wordpress

![image-20260309214000888](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfMyM30IDXHhnDRZiab9Hn2HKN5PhiaPw9EKJDwSEhF1vmmwOO0xibth9K0lrK6le5791ZaRnUY8IVQiaIvEc4lNWXhTz9p6t8yibcq4/640?wx_fmt=other&from=appmsg)

image-20260309214000888

查看效果，既然安装成功了！

![image-20260309213950274](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfOzIvu6bU3OmRpLkJ775OTdNq8upk28nlasx3pLvoMibKkjfo2N0d9gQpYBqKpCibCtfktf2iab2liciajwiaFGu57rECA5ibeibKPtR6I/640?wx_fmt=other&from=appmsg)

image-20260309213950274

而它又说，成功登录

![image-20260309214130242](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPvib4vfuG0kaIxgyBXGKicbF3IXVyGlPyL0RuFM72zVMDIJWuKG1s4ha733UfjGXaEbJEeqc6v7Sb5S0FTpAyIXicjrdED2f9F1k/640?wx_fmt=other&from=appmsg)

image-20260309214130242

为了验证这一效果我们使用它提供的账号密码admin/admin登录

![image-20260309214112854](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfP967ZWjiaISx79KImoDa9x4ZuVJoTB2CkibzARyHLlq1rJa3E9RQaGv8tApOEca6NPfqgEG4NCEMBzqjibak16ItSBTcWFTHwdPc/640?wx_fmt=other&from=appmsg)

image-20260309214112854

登录成功！

![image-20260309214219335](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfML0U0uU6iaG88bq8gIRbkJoVbmLPD5rW5ua5tVbZVZKO9GkbmIVib2qIQeLmibjkmeYm7qI4bStX8VjTWQmuDBf4ToxmgmiaULzo8/640?wx_fmt=other&from=appmsg)

image-20260309214219335

由于vulfocus靶场时间有限，仅演示到这里，感兴趣的可以自行购买服务器

## QQ机器人接入

打开qq开放平台

QQ开放平台｜机器人列表

![image-20260309192825918](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMFrXvVQq5eJ26HnVh5td3FhwvheR71nbz5OnGssjOrVdNn3vI4rC4ZwrJgq6OV9F3jwaSoic6Xplz6SgoLE7coriciciaCvMLzMNo/640?wx_fmt=other&from=appmsg)

image-20260309192825918

创建机器人

![image-20260309193217761](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPx73zqchhvlIC0wMoattA1uF8EFsWNHJvyapjIByvbTjpfd7BmPuLxiaSgVyoGsBDLnOR6MtMWUcXvOE7LYUGPfnhc0icooOmXM/640?wx_fmt=other&from=appmsg)

image-20260309193217761

这样你登录的qq就会出现一个对话框，但是还不能使用基础的聊天功能，因为还没有配置好API

![image-20260309193246274](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfNAP2m8SNLm9PQ4shLbW5X5VPGnsic5NGKPUeicxxmZc12fRZkRR94ESG6vHDY6UP0CiaYOPp22Zb1obRRbiak38AtLXaU03OvwmHg/640?wx_fmt=other&from=appmsg)

image-20260309193246274

OpenClaw原生接入方法，不过我们不用使用这个方法，我们记住机器人上面的appid以及appsecret

![image-20260309194032113](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMxCcEL5ib1iay3ian3ic7390RvB22BJ3W2yAJ63PTfHPqNrTl10V2DGBewKFicL9r2m1QPhM6FdiaDg6BcGiapjiaGZOZuLqh0o9UBRfo/640?wx_fmt=other&from=appmsg)

image-20260309194032113

我们点击添加机器人

![image-20260309204944500](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfP4tYBpOMP9apSmGlgrZocV4AsTmc2IH2xRgFY6YS4h0k4tVScSKLgtAvAn8Qy3Te7zVImNSe0gKWj1dmic08n8n1Ij6HUuHaO4/640?wx_fmt=other&from=appmsg)

image-20260309204944500

选择QQ机器人

![image-20260309204957792](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfM9HJic5nlyHWPSENQjU8jMOgk5gibuIdbQxhaf4496V8mjuWMT47A6BIsvkiaibIDU3Wnw9yI3vB4MxZ2PKibKobyPrCRTzZ4oRp9s/640?wx_fmt=other&from=appmsg)

image-20260309204957792

配置好之后点击保存配置

![image-20260309215250609](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPtiafyNsqrE7rMvu7W3jM1Tv8xWMtc2gZYzMeDPvs1dic2Il6vUEyQ3QCHD4gZ5HanOvgQbdibPhYxomeoSWwngRDgcZND21IV0w/640?wx_fmt=other&from=appmsg)

image-20260309215250609

这时候就能回复了

![image-20260309215329990](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfNAIMVxLAHReS8tcT2jVvEw7XfWrlM5jkCQ4eMchzkPZH1...