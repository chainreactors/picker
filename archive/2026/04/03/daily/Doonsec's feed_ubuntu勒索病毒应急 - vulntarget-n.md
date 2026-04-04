---
title: ubuntu勒索病毒应急 - vulntarget-n
url: https://mp.weixin.qq.com/s/JfvoAd2ToirhrFf1xB7a3A
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:11:24.263953
---

# ubuntu勒索病毒应急 - vulntarget-n

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Wq4VJsQicA18V3ZMPUMOMicVXwibWmmKeeDc7l2HXaIFR5WU3paibbcmERdNfkNd1Qqb6iaze3WrP7Qxm3BWNUIepW4wG30cuqfYRmZPtDwJhKCs/0?wx_fmt=jpeg)

# ubuntu勒索病毒应急 - vulntarget-n

原创

GSDK
GSDK

GSDK安全团队

![]()

在小说阅读器中沉浸阅读

# 一、要求

```
在面对勒索病毒这样的网络威胁时，我们不能被动等待，而要积极应对。我们需要了解攻击的原理和过程，熟练掌握应急响应和取证分析的技术，以便在面对真实的威胁时能够迅速有效地应对。vulntarget-n是一个模拟全球化勒索病毒高发环境下的应急响应和取证分析案例，其模拟了一个正常运行的业务服务被勒索病毒攻击的情景：● 客户在阿里云部署的业务环境● 今天突然发现首页变成了一个勒索的界面，要求用户支付赎金以解密数据。● 客户发现其中部分重要文件被加密为.vulntarget结尾。随即客户要你进行应急响应并取证分析，因为是阿里云的ECS，客户将阿里云ECS实例镜像导出到本地，要求你在明天分析出结果。
具体要求如下：● 分析攻击事件是如何发生的，请给出攻击画像● 恢复原来的index.jsp页面，恢复正常的web服务● 找到隐藏在其中的3个flag
已知服务器账号密码：账号：root 密码：Vulntarget@123
```

二、环境配置

靶场地址：https://github.com/crow821/vulntarget

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA18bRnllxeCIZ899oE61gQduhQzkPhmmumthLsWpLvliaJ3Weqia7Wpo9ibhJxnOOVLwWoVT2HHGiaZOwZZJQE8wgTic7ZCuzuTMXHuQ/640?wx_fmt=png&from=appmsg)

下载完后是一个raw文件，要下载一个qemu转换为".vmdk"格式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1icse6norxDic8rKQaPlY2X4NibagYEVibk6qibK289icN7iccJJ5TlLd5uUM0dicouLunsoL2CDaWSibSkWWrP9vJMDftaJcAwODaLQvPM/640?wx_fmt=png&from=appmsg)

下载好后安装，添加环境变量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA19FQickw4BydzLepoV4aEsx726ubqwefMQu8BNIDaAian753a10I1lFKqWzzx6Pd9N9YqrArXEvXn2QfpzdcU7nIuXzBUIlelVOw/640?wx_fmt=png&from=appmsg)

然后在raw目录下运行命令转换为镜像格式

```
qemu-img convert -f raw raw文件名 -O vmdk 保存的vmdk文件名
qemu-img convert -f raw vulntarget.raw -O vmdk xxx.vmdk
```

转换完后新建虚拟机，然后选择磁盘的时候选择这个磁盘

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA19cut32nAMiaFuyTrnMY2mQuoIcQsl2NIIXK2zciavMDAzOyDumpqHKGqjKHnzwhqZpFcVcVUZmMMz94MbjSNxx1480ialfp2IgjU/640?wx_fmt=png&from=appmsg)

建好后打开虚拟机，输入账户密码即可开始打靶

三、开始应急

打开靶场，发现网页被篡改了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1864TG1xqGJkwEYxyeafW4486moL8eaTjYib1E6kHFtcJrjfloPWORQiaV6ULjicH7UvTxibkwPf7OUIbTatopJ5Mba9NkYGt5VPEI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA19PSXibbnYmXypOGibicxWglIb296BeGVcFVgEUmxpn6lbWI03dI3PafM23wRspFVgL8icqdaxa07EwOhRRzklMFibSD5UbexgiaY920/640?wx_fmt=png&from=appmsg)

查看登录情况

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA18rX1W7FCflzwBQceOiaqJ7dsBTVspNHsvJS3tXjoIeF1FGUgDgibF3wGS2FKzOgoXoRHrqy4X14yKFjWFAEAwmpP7zeA9cePvmQ/640?wx_fmt=png&from=appmsg)

###

### 分析网站日志

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA18ybtsvK7BXibWSAoZmN4ibAcDrNJ9LLl2VMlbzKXc3jibVoR9WG9InhO8DKtmbsTfNNaVibQkQVda6ZttbibfQHiaHcrC5f21dokZ38/640?wx_fmt=png&from=appmsg)

看看access日志

发现大量123.123.123.123的访问记录，而且有在扫描

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA19I26SKQTcLpUrt9NbNGPye91JZ4yuqRO5dWHZ51MFIGpuDOTATIRfw2ZjYXR05jt8o9iaV7DY2DQzDODDzwY2pU40mx1WzXEAo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA1iclMWdb8TDibucRNv5icIPgtcnE5bZrfoibemNjv0L4CNicU6qsZiaMorRZTkKz0SXRyhgXQ61jnUm0vSdEkIZosiaHfHliaIslchlibhQ/640?wx_fmt=png&from=appmsg)

####

#### 发现在命令执行，执行的是vulntarget.jsp

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA19NoHIpuXmHmdqgzM9QbSpxLTp4uM3icRKSdZXBcEC2JFfagDmLoYN5lLoMAwJQ2Ih02TsxdZIAM5ckW7P7DMnOFyib8zrMzg52k/640?wx_fmt=png&from=appmsg)

####

#### 发现在这上传的vulntarget.jsp

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA1ibnc0MI4fv6hdZ9eU6iah2UyibMqBx59IwfwQNCEwO6BW1niab1RfhXny1Oibp6v8pHRp3iacicwqCDH5NucdF9YAvz5xL5dWwE0WzXQ/640?wx_fmt=png&from=appmsg)

应该是利用的是CVE-2017-12615

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1ibOc0icu6AL4AFGWxB538aFwN5gH5M0OR8vz0ibiarBibZRrPcHsCxd7sYQVKDG96jfD5a3bJhicHuZa5AHMECnwDH3O5w2Puac5CdQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA1ibU9W88doia2RfzjCftlBkXAQ6fM6C9LtD0jV6pItlPWdv0ptV8CPYDnM9QZc7r82dFUTRTAn9Ajkjkxmp5CsJWqEybqHJXpWNY/640?wx_fmt=png&from=appmsg)![]()

####

#### 发现flag：flag{Welcome\_t0\_join\_Us}

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA19kIEjPIhzbmoMcMVIJjWdSvJC78fUbT8aeUQ9dzIE8E1Y1oE6ZgpJOVEWkay4IksKKcjxgOKMoyvO4oJVTEFKTkicckXWpoOdk/640?wx_fmt=png&from=appmsg)

这里应该是加密脚本，但是在在后续的日志中显示删掉了，系统中找了一下也没找到

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA18Ir1mrCWOBMu871bKewBg3S3LoPATGXTXwibOWufVqvbj7BUIzabEx1npkSThyibOoDzKWKiaU5aaSSXibCA9YkxfGVLIeu0APb2c/640?wx_fmt=png&from=appmsg)

###

### 加密的网页

#### 这也有一个flag，但是是加密的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA19OI0iarWktEqaNIicKlP6C59XznodDhOZzicaFSAj1AUJ8XZ8BH3tA26Yob2G4Ll8iaJNXqLwJ7KYFmtriaquAicv01uiaOOwbafiaHt8/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA18Glu0npHmy67YtsAia5QAiaXaib5S1NicNibtDKRRHLwTwNsItasjJ0x4ldhDuDJG3OG1PXiagw3T88h0DsJojDt8sHLibNKibF3EIEfM/640?wx_fmt=png&from=appmsg)![]()

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA1icnbaOecsXmMKVYUutOXFEL8Y3kuzvSYn5iccIAlQqHXABcknxrmvSzRicOMATcOdvlwtLdg77NNN1NScgic0yjuZgEXict9tAXHsc/640?wx_fmt=png&from=appmsg)

###

### 分析history

#### 发现flag：flag{vulntarget\_very\_G00d}

疑似在运行加密脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA190RBdgxjC2C4YsiaNibvY43mB5yg56juJqy67Vwt9FicBM0SOnymCGOpmMxv9Es6P9ibDKqdFcgWtZ5lTYWxUSxf4ydcibdbtP8TTQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1ibOPOjsB10m1BRKPoNb51AoQ5WObtt8KQUZx0ia7VFoVnmhteNKhibdMV8ic6Spqu8GkSlMyticGYY9MLwJkgVxe7bPs95icjBpwQ24/640?wx_fmt=png&from=appmsg)![]()

### 发现密钥

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA1icZwBfe0UibE723OllMPCZYXxcYciajEoIzm80IaM3NZvDrcJCvxtbJ0nm29nUzVAnh1cohcicMh4wb9hibH1HSmVxiaOdG8NliboJVw/640?wx_fmt=png&from=appmsg)

###

### 定时任务无发现相关异常

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA19r1YmvictrfUiaF3Wto8icTRicrQwzEv9mZHoicicOOnAUNSlbZGkd1TW4YGqWK1uFMXvgasQa99rlgpQEIqBNLFOiaQVYGb0up9VBnc/640?wx_fmt=png&from=appmsg)

###

### 恢复数据

#### 这个时候就差解密恢复原来的数据了,看看有哪些文件被加密的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA19SI7CVEicVkDjvenFrRZ4OkRC2rJQklswsS4vSaL5Iich6UOKoBu9orbjF1nSWuKtPgA22Ftnv4agxuJvQBCOPtw57HyPYm9nRg/640?wx_fmt=png&from=appmsg)

再看看刚刚的两个密钥，应该是用这个解密的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA185areTBwic1BlaSFJUtIkNdPVQSUseib8MCEC0nDv88EibtLZ7OQaxUKW02hqURY13HbsianOlh7NMflDUM98ahWB2IPuqOkBZV7Y/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA1icyonlYLN2kPUdEgv1nfQOesxmhIib45fXQ2osbdAediaDSd0g1HFLGdaeY8DLibiczAEFMGINsyNgsbz0Oxn4yuyju5LMiaJfUicl6s/640?wx_fmt=png&from=appmsg)![]()

给数据给豆包，要他写一个解密脚本

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA1ibG3uXJ26uvpuibyiaic5n50s8TaYGJia4Boa5fVz1NPcOibea2mxH2jdZRdflwAnfgqHc5egYYsBW46aDoO4kxU79b5lXoy9ptguOg/640?wx_fmt=png&from=appmsg)

####

#### 运行一下，拿到加密的flag：flag{https://github.com/crow821/vulntarget}

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA18PMgGDMUIcaFHAwLGUds8jibDQcv7VWaRibSDxRiaxWjQibjuJzu1O03xXic1picDxO9AvbNJIy9ftYsCvI9MHYCX3ia7YJsd04GEk6E/640?wx_fmt=png&from=appmsg)

改写一下脚本，这个脚本太长了输出不来。成功解密出原来的index.jsp

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA19QcPQoUTepoJP5w74hxG4nhd9O3ZGgAaaFoenbhjcNZoF3giame4hlcaEBoHK7CY76P3CALG1BfdVPPsNZSe11lqm3sHhpZrrQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1icvGsvy7xlhZ5Nz8zY3t8iaCfMulhd7QpNYkVhLXnH6RDMCP3iaox9NcFvkYhpH7Om4QmA4AACW8sic2q2DOj49Uy2SG5bT76h7gY/640?wx_fmt=png&from=appmsg)

再恢复一下404.jsp.vulntarget，确认是webshell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1icpzAwZR8sPfTa8sc2xnHVElGcVvryScqrTLEQ70qRUxqcJQQNMzNeMNdDEfwaJWbibcibOcN0RtmQ4mXaGY4MqH6jVttN32dulw/640?wx_fmt=png&from=appmsg)

###

### 重新上传一下，成功恢复原来页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1ic8Xn6Cp8mPhULepcP5IZz3iagwarQhbcN93xusjv6BoeGEmP6MzMF9DZ58r9sibBcPUzh3PR5AiaWY1VpyfyI44ibL9qSaicCP2tc4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1iccM2ib8pePcCgQwppSyiaibQiaQ8weB1acOpaGqu2pXEg3m2Epn1icNS3JzxE0lAMsxHYglPYh3PKY10YU7YclS5ibwH5ZbYCXfQXUY/640?wx_fmt=png&from=appmsg)

至此打靶结束

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Xu1xJEZRrFjUe1HmsusbqLJiaQvscUlHp1kgYagMRTFy1TyiaryxmOjvkpS6UKic5ricVOjdicibiaLMTibKkUqiafYD8vw/0?wx_fmt=png)

GSDK安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xu1xJEZRrFjUe1HmsusbqLJiaQvscUlHp1kgYagMRTFy1TyiaryxmOjvkpS6U...