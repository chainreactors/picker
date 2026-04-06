---
title: TRAE+x64dbg+MCP辅助逆向环境配置
url: https://mp.weixin.qq.com/s/bxCriG6jTIVT2fajQ83IvQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:38:30.837961
---

# TRAE+x64dbg+MCP辅助逆向环境配置

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6nhGiavBDP4bT0aiaFQ9U2f9zMw55bj2yeqBJ9GwpPjpnMyDmWK85J09RVdazKogvZWEibdH5lvBEpMqeRwraGPoIuXIkUMZc4zRKMiapZcfsYQ/0?wx_fmt=jpeg)

# TRAE+x64dbg+MCP辅助逆向环境配置

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器中沉浸阅读

一、简介

TRAE：字节跳动推出的AI辅助工具，目前包括chat模式、builder模式、mcp模式、solo模式。

```
链接：https://www.trae.com.cn
```

x64dbg：一款开源的针对Windows32位或64位可执行程序的动态调试工具。

```
链接：https://x64dbg.com/
```

x64dbg-mcp：我使用的是一个GitHub上的开源MCP项目。

链接：https://github.com/SetsunaYukiOvO/x64dbg-mcp

二、环境搭建

1.TRAE安装

TRAE的安装不再过多叙述，直接搜索官网进行下载安装即可。

2.x64dbg安装

接下来开始安装x64dbg，打开官网如图，点击Download跳转到sourceforge网站，然后点击下载latest即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4b4sCM6jFm1P7AutBW8Cc2CvhmYEk8sY64c3icGoWibYOnEFiahIGTpbdOX4vfRXngO24Tia9eUL8HnAuliciaCOc0RBgd4gTB1aPZJI/640?wx_fmt=png&from=appmsg)

下载下来后是一个压缩包，在合适位置解压，即可获得x64dbg和x32dbg。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Yux89IdLlrY1U9s7iazHLBujej3LHk7Uu0icc1YclhLU4k2rHJyeV7DYeZ2j2qttbZZQsOBvLSmiaUQHfVqB7iaoGNurAQiakju0k0/640?wx_fmt=png&from=appmsg)

3.x64dbg-mcp的配置

首先点击以上GitHub的链接，下载最新的release版本，包含一个后缀dp32的文件和一个dp64的文件，这两个文件是编译好的mcp服务端插件，分别拖入到x64dbg文件夹下的plugins文件夹和x32dbg文件夹下的plugins文件夹。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aib1O39IaVf5YQoG59Vp87zjOlL8UO5EoNa1blHBOesoJdKYJN0qu37myUghRvw1eTCHzyKn2sibAM4wmXIkMnVPVlcB1RLYMtM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4bXYKq5qZnS5NiaWzs0RGmzoNCCDM2aKjTW0m8TAk8iaicaGnx4kBGEDWebZzDy2QLwp51lYeRdm4XI8oAWgoPsak24WEYpJJkN2Y/640?wx_fmt=png&from=appmsg)

然后打开x64dbg.exe进行测试，打开后点击日志页面查看，发现mcp server成功载入。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Y5u5siceiaBeZibYibI43qcUE8NSNEWflacXOTQ93fNAXkzNqaE6AQnc8iclo3LmHxVmp51lCMopapHJ7vZ83ic5BGaIef2ZtKJSbWY/640?wx_fmt=png&from=appmsg)

在菜单栏里面找到插件，点击后发现多出了x64dbg mcp server选项，点击后可以配置该mcp server自动加载启动以及决定开启或者停止。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Y25TcqvFic7h4h8B3XiaqUYqcKMHC7Mrkx9gQ4RlyAzsjJTOKbcwn8aMZiaxohgEmVswVS19YyrqoS26gsbCDmvrWdzM0En5kuGQ/640?wx_fmt=png&from=appmsg)

再查看日志，发现已经开启x64dbg mcp server成功，开放端口3000。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4btpZMJldrYgkdZYSOsfBzPmHYiaCQpQPKL1LJKw3icBAhSoNlEKb1GnXNVPIO6ZowSAacZtibJ73icxVx2h7kRbwLmLFOyyFhliaAc/640?wx_fmt=png&from=appmsg)

4.TRAE配置MCP客户端

打开TRAE，选择MCP->手动添加，输入配置json如下，即可配置成功。

```
{  "mcpServers": {    "x64dbg": {      "url": "http://127.0.0.1:3000"    }  }}
```

三、简单UPX加壳的程序结合AI实战分析

该程序下载于bugkuCTF练习网站，题目链接如下：

```
https://ctf.bugku.com/challenges/detail/id/280.html
```

    下载后发现该程序是upx加壳，于是需要xdbg动态调试脱壳处理（当然使用upx -d肯定是首选，但是为了深入学习练习，我们还是采取手动脱壳并dump内存的方式）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aH2z4ELFSiaqjiaggkf9DgtwQvicxSYdnq96Wg6FePS77q8j7jI59UDhSjz1DRbPiaP18vxjNqoNjfsW4DAp54D8ItO6TaBxOEvGU/640?wx_fmt=png&from=appmsg)

    使用开启了mcp服务的x64dbg运行该程序，并停在PE文件的entry point处，接下来我们使用trae来对话分析该程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aNP9KNRMt3vLZzQo7x8MerFrRunuYrFapQ3t2iao3dbRBfoia9VPqQxibbxKjLMBGcrKXyQdPhoVNbPRweYvRhl6lN5PaiayY8Esc/640?wx_fmt=png&from=appmsg)

    可以看到我直接让AI去帮我找这个加壳程序的OEP，AI结合我的语义决定使用ESP定律找OEP，然后他接下来开始读取我所停位置接下来的汇编代码，以及SP的值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Z4jCjyQbmLneofLAldqD2BIYOtYibkVV1gHKcmTopfIMK2zZxMVLibONbyPibD2q2squJYVunrlWaSJxU5ibZ4lBfjMfmnYHnbcXs/640?wx_fmt=png&from=appmsg)

    然后AI设置好了硬件断点在当前RSP地址，开始进行调试知道有指令访问触发该硬件断点，它尝试了几次发现一直没有停止，然后开始了它的偷懒操作，首先查看内存映射，然后决定直接使用x64dbg自带的dump\_detect\_oep工具运行，直接找到oep位置位0x00401500。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZmmAbW01Lwib1FqobXFiaZoicDJWMgFHdx9s9IGibFPDYIJs4MyEcBQfvRm95RwMmlCB5ltJkf4RicuQVgChIiaM56icf9y9icky61XJo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4b9bjDQNhg5SMuwXNJX71sSZcN41RUyNzWOicQWziaVUYdAxriaJ8iacvAcqWanBRdkS5rUMXVK6UEsdLqYnFLrUbribQ9uFXeJwjHs/640?wx_fmt=png&from=appmsg)

    以上步骤成功找到了该upx壳程序的oep位置，然后接下来给它指定的函数地址，让他进行功能性分析以及制作获取flag的脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YzJrKJ8RkujPyFtekEaeLQtYfibK9VuQKzUNdNUWNgjUD7SBax5W6XyDmmYdELibDbOBypC1g02f05FTE1FQuiaE0nOVOjibBVqes/640?wx_fmt=png&from=appmsg)

    这是AI分析的该函数总体流程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aRhFyfKJQSqwn9Cm8gdtP9CiaHSfvAkDZOKtIn4gKFv3FgjvazHy7iaricrKCb5ZolEfH0JSAZvicficXnNw72Ktf1qTyU2OzI31CY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Z6GH25DIxC8gibDx078ovAQYW9CFTvNjiaG8Jh9rcWndAr9hYqT9o8mK6ANskbA4WeOQ9ibGhaphUnGqELbyGZRltwxrFiavkMCaI/640?wx_fmt=png&from=appmsg)

    然后AI给生成了一个解题脚本，复制到py文件中运行，明显不对，只能是大体过程正确。

四、总结

    以上是使用trae+x64dbg+mcp的AI动态调试逆向辅助的搭建流程和实战演示，可以看到效果还是不错的，不过在使用过程中需要结合AI分析，多次给AI反馈结果，这样可以得到一个不错的效果。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ubxw8wJEYdluKbaN4LDwroa6C5W8flqTtNkiaZBpt9ibcVXJTlDmAHJHcR5TBR7AREPYETB3XUJF6v692P7GaD5A/0?wx_fmt=png)

SPEEDCoding

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ubxw8wJEYdluKbaN4LDwroa6C5W8flqTtNkiaZBpt9ibcVXJTlDmAHJHcR5TBR7AREPYETB3XUJF6v692P7GaD5A/0?wx_fmt=png)

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