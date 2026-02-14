---
title: 基于DeepSeek的提示词注入与变体管理工具
url: https://mp.weixin.qq.com/s/Qm9QTnJo4Trux7Dl7sikdg
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:04:47.149130
---

# 基于DeepSeek的提示词注入与变体管理工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODxicT9kW8mb3orOicINM22Fl9dQFwRrD89icr6uUdl6qNzPUVKQBT7CTBahwec6upOibhUgsdR2iamu6wyeYpQgOn7NqFS3tM6Fs56A/0?wx_fmt=jpeg)

# 基于DeepSeek的提示词注入与变体管理工具

原创

0xSecDebug
0xSecDebug

0xSecDebug

![]()

在小说阅读器中沉浸阅读

# GMF(GiMeFive)

>     请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**。
>
> ***项目地址在文章底部哦***

> 学习AI安全也有一段时间了，经常可以看到各位大佬以及师傅们各种骚套路的提示词，但苦于没有一款趁手的管理工具用于整理。在各种搜集工具无果、又有粉丝咨询是否有相关工具的情况下，心想：**等待不如行动，开搞！**
>
> 本人小白开发，大佬勿喷，欢迎提Issue一起完善～

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODylEZlSjpQ8ZlaClWqRB6qIHia0fPEUnptHDpdq4GfmZTsrYR0TeaRm8Dn4FNgvzApPvO1ibV80VTuRMmoFiaeJ1hy832OvlibUdsg/640?wx_fmt=png&from=appmsg)

专业的提示词注入（Prompt Injection）安全与管理工具，帮助安全研究人员和AI开发者识别和防御针对大型语言模型的各种攻击向量。

## 🚀 项目概述

GMF（提示词注入管理器）是一个功能强大的跨平台桌面应用程序，专门设计用于测试、管理和防御提示词注入攻击。它提供了一个综合平台来创建、组织、测试和分析各种提示词注入技术，帮助用户理解和防御AI系统中的安全漏洞。

### 主要功能

* **智能变体生成**：基于规则和AI的提示词变体生成引擎
* **提示词管理**：支持提示词创建和管理

## 🏗️ 系统架构

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyvnm7BHJ8D4B5PgUI9Th9Ap4Yd5z253Sph0XHN9zKcSUF48vfF1Ogw3ux4Jp9CpiaL9G6Z0IU8vHbZZeAzAR4XET8KH8RyqsGQ/640?wx_fmt=png&from=appmsg)

## 🧰工具使用

### 主界面

1. 应用菜单栏
2. 分类栏
3. 提示词列表
4. 设置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwzSnib1tABHWTRCQG28ZjnNiaDUIHGibicbVpS5tUqsOPmDvXFIuBAKSiasibsgYdMufU4qgaRse1lWoKog4cTcbtXRsQgT6EYygo8Q/640?wx_fmt=png&from=appmsg)

### 新建提示词

点击新建按钮，可以新建提示词，新建完成后记得点击保存

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzuib6GoTMIbZKmhvY3d7gZ7jG5sopEt8Fzh82hgz4ogn68B7hicNsHVicHbDndo9Uic2U41aovysSytx8VaSib5ZicEIzu9UXuSCDZk/640?wx_fmt=png&from=appmsg)

## 分类

点击左侧的分类会在右侧分类栏显示此分类下的所有提示词

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyuveMlfpibHPt4bbpjK2751x3u1H2CicNicUR7eibDFQ1gmuUcvpvEHuo1lP84Wd9K1aTx5VB8bwKhtFhenNMpH3tmHFEiaYXqrqHk/640?wx_fmt=png&from=appmsg)

左侧区域右键即可新增分类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODy6Ly4lN1oxZrq1ibVWbMKaRkpTTDrSYOtqf4grjIY9m7icP1AwpLeWvUeCEaJEmpmBZrBnxZtJ7Ij36xy2S2hmW1zoXjuEoOdPY/640?wx_fmt=png&from=appmsg)

已创建的分类，右键可以重命名或者删除分类，删除后分类栏后，选择此分类的提示词不会删除，分类会变为未知。

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyA5LmhMZJohsSicVmrEWPAcL4XaMA5K9ib7Mm1K4CNibeVxiaT60xiasYsrNxiaPBNXTUCoO1bvCAkCXyoNof49TaDNBdOprb7s4AIA/640?wx_fmt=png&from=appmsg)

## 生成变体

其实就是通过内置规则/AI对系统的提示词进行优化

选择一个提示词-->生成变体-->选择不同的生成方式

生成的提示词点击复制即可复制提示词，点击保存就会把提示词进行保存，保存后，下次选择此提示词时保存的提示词内容还是会存在。

### 1.AI优化(推荐)

下面两种变体方式是基于规则库，但目前规则库内容不够完善和全面，很多提示词生成变体后，没有任何变化，建议还是使用AI。

在设置中配置好API和Key值后即可使用

一次性会生成5条，下面是目前所支持的变体

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODx2ib5vbTgrPh4Mx8UU7EwRgYN14somwjVj1pItUDVTKMdxdicBmZ5icNBUqiaOFCZN83Pqz3Agic92YgN6vRuODz2HuAOo8FbvEoQo/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyTVPv2RqmmHhOACa6Vggib8tqFU6fQib5mK7iaiczlCcKezTlVAnLOKjk36P9jfDGyzeyEjc7UYXMBn1iact8bSC4JIj1qcAC6sq80/640?wx_fmt=png&from=appmsg)

### 2.编码变体

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzF8GfDZNVZCZumwtkUgYSbmaN9tLJ3RO6uOwew6aCoQrDAUp4b7gMFgaK4yjX13Jk3a6R0ibThX2xujAgfsgcxUYfqhjuattgM/640?wx_fmt=png&from=appmsg)

### 3.规则变体

目前就这些变体，基于内置的规则库，暂时还不够完善，有较多提示无法使用。

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwlicV0HHrHxvrvGvt771Y2GMYia5DWzbEyNSrzWTIra7COtxV98n0EV4WxnlnRVvYn61CiaLicBeKltSbBqiaMeoBxgibG4iaAB2ehZY/640?wx_fmt=png&from=appmsg)

## 主题

右上角或者设置都可以，点击即可切换不同主题

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzxWbcIx0CmkWr1B0zH4siclanyOQWWEo93WibuTcqlQg4rN8DRFeq7vweSQ9vI4LwBoiciceNwognk17WoJCjkoO0bGrweALNxUDU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwNXIia8WtyakVrAyWbzASBbseD8t4K9ImpcFGGnV4eOmeTj7OMUjm1HkmzIlaGCAUUyibuBtsicqv9eCM59DMXMiblMgoOGAcaJtA/640?wx_fmt=png&from=appmsg)

## 设置

主要就是主题的切换以及DeepSeek的API的使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyI1Plld6yYMia6XvxUX0Jl5KmQgW7Id6FKoCxfPhVbub6ujpjoxalv1nRkngDLtpN3gP4N5PbicoiaaG0gcxNjdR2pJPGhn9iaRk8/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxhGF41DUgXe9jeexibXbQYYIEufibxT0IFH7gaYZkkwgyzuLOOEbU3D3lW3otqRvrbGOmsw8B8B3o24CzUYMmVaSjtMLfka153A/640?wx_fmt=png&from=appmsg)

## 用户Bug改进和优化

这个在工具的应用菜单的帮助里面，点击后会直接进入问卷，由于工具当前是第一版，可能会出现bug或者需要改进的地方，希望各位师傅多多提出意见和建议，或者加入工具的交流群或者我的微信，直接提出也可以。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxDcYhvpAzLK0GeibZ6eibX878zAY51koYsWYa73rssuYVvrfoLzN1xlLdOWRbnMKuZcEWwG3QbZx9T3Hia74ccsKkNfTcIVyu9ds/640?wx_fmt=png&from=appmsg)

## 📞 支持与联系

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyQRvXQxIj5evEdasMSVUVhiaQQNfh2K4hmeVGcZos0kcIpoVTlqsicFWWFLASwtRELI5Y9dDSwuKR0Y0xv71jfmZ8maftuHBg0Y/640?wx_fmt=png&from=appmsg)

## 📖 项目地址

```
https://github.com/EdinLyle/GMF
```

## 💻 威胁情报推送群

>   如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。
>
>  如果师傅们想要获取**网络安全相关知识内容**，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
>
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg)![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

0xSecDebug

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

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