---
title: 【鲲鹏杯】OSINT 方向 Writeup：从线索到答案
url: https://mp.weixin.qq.com/s/5ymzJwisECuJ42LzcnbgjQ
source: Doonsec's feed
date: 2026-11-09
fetch_date: 2026-11-10T09:01:30.302792
---

# 【鲲鹏杯】OSINT 方向 Writeup：从线索到答案

# 【鲲鹏杯】OSINT 方向 Writeup：从线索到答案

原创

鲲鹏杯组委会
鲲鹏杯组委会

云晞科技Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 纪念日

题目

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkNrMMtx8icicJwmRV1V5ibR7u0iaWrClVEKwS4ChJ4tjnYIUEoRwlmMw9633UjuK2zuicKPNUVDEqN9T8AOnxwuRFfDl1eC6XqF5oE/640?wx_fmt=webp&from=appmsg)

来到YunSee官网（搜索引擎搜得到，微信公众号也有），在团队开源项目这里能访问到YunSee官方Github仓库

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVldbE4U8aMfWCfxbuvLopwyribicHKHiahAia0zCRKmx7M4UExBuEzK9gUsclzyzyesNW2Qg2icCLHHwva1gSTImvWMFxdpJX1QqsyQ/640?wx_fmt=webp&from=appmsg)

通过Google 搜索 `Github 注册时间在线查询` 会有相关教程让你访问相关接口或是在线查询网站

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkOdPpQumwZeIRbtY5Mic0e38gicWDnYgibvwaDLUVNr69tsIM1nsyaEWjvibFO0icb4F4022KdnvRSoarH0Mq1lsibz7m16EcBERl7s/640?wx_fmt=webp&from=appmsg)

https://xyl1null.github.io/GittyAge/

查到创建日期 与 时间：2026727135813 （GMT+8）

题目给到的描述是（GMT-4）

也就是202672715813

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVljs4UwJR67P3Zc38PMIHIggAfuVLEhd59W6Q9x4Cv3U46uC5Sg0LRHkpdiasfgK9MHuKzicCDjyHFbpuiaQgnAJSxdBq07UKwvIo/640?wx_fmt=webp&from=appmsg)

多次尝试搜索 去除年份 72715813 搜到奶娃头像账号

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmYn28SoicKYKnZ6njqqlO1ZtvgnClTXTiaEQrIibEd1Lic73D6u7y573OvWrp1bslTpyocGrZfDceWR5Fq8sO45cCjrab7LcUEvRA/640?wx_fmt=webp&from=appmsg)

主页有科普视频

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVnvHTTqR6Lic7xibSl6Q2tIERVraqJYiavbFPXQyWJsfDJY3FvBSq7z5warJCmURJavxFwAcl3jmeQNYKflibutvqp7yTibI4YmCHZM/640?wx_fmt=png&from=appmsg)

在视频中有部分帧会出现一部分flag，需要手动拼接

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkBQFPFJ6Fe5hibDsdeBOttbG5oiaaanLWCDNicqGCkcfCIJnvwblzqdXhib3Kib5TnBfROOaueRtqCdnJ4cghwuzQFhticcKSUJK8J8/640?wx_fmt=webp&from=appmsg)

## 《春》

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVn5avVmFW3GShgiaOTSibb4zmys8JtQicrrmT4lXQraCfPoT39zcHKgQgtv0aCCUH2r0fhibp2mKSodVLibK76OKcfztKoG5ibgE0sCI/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVk7cRGPPMydxFmbVBqcI7Mxujjx0WBaCd9zribBBiceibib9toaoYqkgLyf9NYHunkAUqlop1vibESrb4N0j9PWnay4hjcMFd9nYK40/640?wx_fmt=webp&from=appmsg)

解题思路: 这道题目主要考的是对于 OSINT 开源情报信息的 搜集能力 以及对其的利用，这个诗句是个兔子洞，当时我设计题目的时候会想到 有会去直接搜诗句的；本题目的核心在于**苏轼**走过的路，**我**也走过一遭。然后需要提交 附近一个带桥字的路牌名字的md5值;

首先我们能确认的信息有 `苏轼` 我(Dark\_River) 还有上面的这张图片, 可以在QQ群找到我，利用QQ 的公开空间去确认我走过一遭到底的哪个地方这题我在群中也有过提示 他并不是简单的图寻，是一道OSINT 题目，其实打开我的QQ空间就能看到我最近游山玩水的地方就是**西湖** ，我还用了苏轼的诗句:**“欲把西湖比西子，淡妆浓抹总相宜”**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmg8yQlsVJ5e8z1PluWDsD9P8n2nQr0hbiaR1QAXFYWeHPw0J9ZGRjQOqbehWEVkiceSPJ01uUdIK2Wwmmw0eJicSzustBlTDxPns/640?wx_fmt=webp&from=appmsg)

知道大概位置后可以通过 百度地图进行搜寻，因为考虑到时间问题我还加了句提示 在苏轼建造的水利工程附近，那么现在得到的信息就有 ①地点:西湖+苏堤附近 ②图片中应该是水杉树林 ③名字中带一个桥,那就对于百度地图进行3D 浏览查看

1. 首先找到西湖的苏堤:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkqlezkhIaqDGnVyBHw41Nken6OWbU7P1o4ydvZe6C65Gf7USKL6fc9G8dVicTViaf2zz5N1GgDFKZh8XRUqf0rTXLD2TYNAUaiaU/640?wx_fmt=webp&from=appmsg)

2. 开启全景地图 对附近进行查看  可以对附近的全景划分未4个区

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVm06ERbAJfMcxM6FeaUGib44aAbhqQRrkFa3nf6TMWEtTF3Zo4tvP9ywHaicllp1oKtoszKtSjBhUKewaM1ibL8TRcklH84JEzV34/640?wx_fmt=webp&from=appmsg)

3. 接着又是一个坑点 大部分到这都会去搜寻各种各样的桥，什么饮马桥什么的.接下来应该对于这4个区进行大概的 信息考察 看看其植被的品种 环境等.

**A 区有点像图片中拍摄的地方 先标注**

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVliapicUmo4aqYo1vlu36GxI0Zic6v02JVoUhGnMGmibEfrNJWbJy1XNaUIBFvicaCeM49Et786lV8ceAIbabZItvCIfXxQh0JZhIG0/640?wx_fmt=webp&from=appmsg)

**B区 明显不是**

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkVZ7JMv2GBNJCVoxc4mB6NOCy1E4ErVF2h8MmlHrXPwLsicSMicB38wj3kVEArzAXR4DlRcdVnuzjx22q0icHV6hGLu3BLytvUZU/640?wx_fmt=webp&from=appmsg)

**C区 有点异常 里面有个延伸到 景区内的路段，一看名字 清波桥河下**

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkV929Ftk8TO8fE28ZO4M7ZAicsKg0e8dwsdy5ZdutjhhzXTHDpDoYjvCTLYvygoGtFtLYuB04lG69icTHnEWD20Tbpsa4oj00Vc/640?wx_fmt=webp&from=appmsg)

**用全景进行探索**

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlibljMrs3icqJopYIoZiajtvEia75Dm11xVtibF9NI6fYy9PV6gWPapGicuBTQbWG8e0tlBNf6uVUJp4X9MicDHQQNjaqvZnqJvpmicLE/640?wx_fmt=webp&from=appmsg)

发现了题目中给到的位置 答案就是**清波桥河下**，名字带桥不是桥.当然要提交其md5值(小写)

## 收手吧阿祖!!!

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkcARtm0gftwGgmAia5rFGBWibeFMicO01TdEmQ2VLCxic8yvfIbVrCxZHyx6O3b6auzDq30I2naUSG4sK3niaXRc2VdVAPHticXy5SA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnln3YXq8L4icXPHaVLdFmaLaJjv5sHle1cCwuhU9NfwDpUaSlCk0a23QgAZ9LDHml8L2wl4uM9O47Lhk3jH7GIO9SwAicQJPyYk/640?wx_fmt=png&from=appmsg)

这道题难度较高,是我在练习国外的 OSINT题目后自己琢磨制作的(题目全程可以直接访问没有特殊动作 特殊地区请谅解) 这道题目准确的来说是OSINT + 一些MISC ;

先从文件层面来分析 有2 我累铜泥完压缩包中存在2个 文件 一个的flag.7z 一个是 wyz.png ,MISC做的多的都知道 flag.7z 大概率就是flag了。

首先本题目给的信息几乎没有，只是个梗，那么只能对图片和7z 文件动手了,7z 文件对其进行简单的文件检查和exif信息等，然后重点是png 文件 用010 打开 开局看扁所有人的 各位彦祖，可以看到 文件头是完整的 在注释出现了很多 yunsee.team 的网址

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVn0MyibFoy43NE3ZrNCKCnc9UAmnEzCCG2CUVbZmxzoUZp0QFsC40uvtMSNiaEdR5ObIIXHGRIFPppUbNxU2Q5aMc5hgpYhe6Qok/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVn27mdRibDU2CFDiczJFRgssBzOnjrAQQdxTYjyW2oIPiayyxDiaI7zvXP5bLiaGNEEByXUwdBcrZhR4KjUIqKQOhq4Ky2icf9tQ3Xn8/640?wx_fmt=webp&from=appmsg)

访问后可以看到是我们团队的 简介/介绍页面 这里先埋下一个伏笔，我们接着区审阅png 文件 当然如果你对网页感兴趣的也可以看看源码什么的，可能有些会藏下一步的指引之类的。

为了防止有些小帅哥和小美女不动脑筋，直接用某位随波逐流去梭哈，我特意测试过了 需要手动去提取才好搞到 下一步的关键道具: （古法） 在这里我们需要知道 在计算机系统中各种文件 是有他们各自的文件头和文件尾巴，文件头是用于计算机去分辨他是什么类型的文件 而不仅限于所谓的后缀，文件尾是用于结束一个文件的标识，PNG 的文件尾常常可以看到是一个可见字符串 IEND......进行封闭的，那么我们就能通过文件尾巴来判断 有没有藏匿文件

先记住”本文件”正常的文件尾

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVlXJ1NISDX6KjWYw2w2D6nZkvf2pEWkmibc827wcicZvGHibbejP5iayqdmH7HwyLUMP8okG8w8Rrvfu8yzy57GdbIRB0XIxfriaDSA/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkdxxbCGvDhppvv8jFpWXWnddPJAqXfPKzIVw5AwzOng5IIGZOvUaOuguibicZN7M6fw70R3SvsJwMlS7zqqnuHumicHAzfqNqF2U/640?wx_fmt=webp&from=appmsg)

接着我们简单搜寻 IEND可以看到出现了2个IEND ，还需要进行跟踪以防有概率是文件他的16进制可能翻译为ASCII 的时候正好是IEND 因为我们是通过 明文来的 准确的来讲应该通过完整的 文件尾16进制来进行跟踪

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlD05EGM4RvJXXWAtTriaYbNuu687xVdblxITzOa51PqQjgicvgmPrnCLN5YdXM6aYsQWWUWuSh6bZyQhGeoLpKNiceia6pPQiahicQ0/640?wx_fmt=png&from=appmsg)

能看到 第一个文件尾是正确的，这就说明该png文件中可能还藏匿了其他文件 ，我们可以直接将 逗号后的全部内容都剪切到另一个文件中，然后先看看 刚才的文件有没有出现异常,然后通过对剪切部分的 文件头修补来得到 一张图片

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmgrd2dQTUxvydK3WiaRaSbT2jEPLYnv93ibZXWGL4ngU9PYpQIR2Mia9XVfPnfBwUmxKjpUt2fmssz1WiaUbCxSTnficbyzsQLhxoQ/640?wx_fmt=png&from=appmsg)

有些没了解过 CTF 历史的可能不知道这个标识，他是 国外DEFCON黑客大会 CTF的标志 ,我国蓝莲花战队曾经在2013年成为首支成功闯入DEFCON黑客大会 CTF全球总决赛的华人队伍。 然后提示中说过要结合 yunsee.team 官网来进行搜寻，官网中最突出的是名字 通过名字 + defcon 的形式来搜索 , 这里其实可以直接用作者也就是我的名字来进行尝试 (这和前文的yunsee.team 有关)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkwMHEA7znZN9jtNDgfWtz7SGIicwDPNkGyzQxu0xy4QxyhfmyvNF5MWtWP9YWVZTtr5K8E0yuP4QFwOfZgLEiaib17Bo0pQfYic2U/640?wx_fmt=png&from=appmsg)

能搜到 defcon 的user Profile 网页

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkXUQ62Jsnpibicn79aZH0bicmIXfLYHvyPHUgyQsicMypZwcLGGI1pdhB7kvqGQEjicZf6XdlicK5EIFiahDWubdw52g2kugCKYiawuX8/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVmYv5jCzK2RiazBUvMsGHicAIjnWBkvo1uhHCZdtGjib6konrMlb3vribV6HCH8ib0Jysr00vXK3nq6hCv9uAMKyicvSJkic1hiaS7lYaY/640?wx_fmt=webp&from=appmsg)

然后能在 About 中看到 16进制信息

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlsAV7Ko6mWkkmlkQ9qELYsDcY8HjJKcEYjrQw2ZrHMicHHV9y1vGO6fW7RTXib7pfA2hTVbhOcHTIVic07kFSw5joNWD3TSus5u0/640?wx_fmt=webp&from=appmsg)

这里用 chef 解密后是一个网址

`https://cn.anotepad.com/notes/am4hp97p`

一个在线的网页记事本里面

复制出来对其进行检测 可以看到一个 ASCII 艺术 其实他是个彦祖的ASCII 图，但是 网页的问题会变形 ，然后最上方为英文版三国演义，最下文有个提示: 有些事情在不同的角度看，会得到不同的结果，一千个人心中有着一千本哈姆雷特，找到那些相同的东西

通过查看 我们发现了一个**base64**

解码后是一个兔子洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVnGibMiczXlnW6XxurlJSILEb6VoniafCmaVia1xE1T9IwT3JibUs5pOb9bPJ59iaBOMefwS55m6ibtKzib9nWt0cXTjcXiaeibHbuuGZ4oc/640?wx_fmt=webp&from=appmsg)

提示中说不同角度 去看相同的东西 这里面相同的东西 有看起来很奇怪的字符串

`/KXXt@Vuay\d9Nwv>EC<U*,f%tXc/N^vG-\![Bk8K/YcEk?2:>`

从不同角度也就是说将其反转试试

`>:2?kEcY/K8kB[!\-Gv^N/cXt%f,*U<CE>vwN9d\yauV@tXXK/`

然后去尝试解他可以在base92 中得到密码

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVmquCkUN4qxrJCkysWS2Blwz3cFcvAviaYolmuI77CHPw2ory926BVsHD3CB9uNRz2z3EoQHhH35nPArrP...