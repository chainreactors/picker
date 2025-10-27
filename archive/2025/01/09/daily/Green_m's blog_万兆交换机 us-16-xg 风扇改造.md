---
title: 万兆交换机 us-16-xg 风扇改造
url: https://green-m.github.io//2025/01/08/us-16-xg-upgrade/
source: Green_m's blog
date: 2025-01-09
fetch_date: 2025-10-06T20:10:08.598847
---

# 万兆交换机 us-16-xg 风扇改造

* [Home](/)
* [Categories](/categories/)
* [Essays](/essays)

* [**Declare**](/declare/)
* About me
  + [About me](/aboutme)
  + [My reading lists](/books)
  + [Friends](/reference)
  + [RSS](/feed.xml)
  + [About this theme](https://github.com/luoyan35714/LessOrMore.git)

# The more know the more need to learn.

[Misc](/categories/#Misc-ref) /

# 目录

# 万兆交换机 us-16-xg 风扇改造

Posted on Jan 08, 2025 By [Green\_m](https://green-m.github.io/)

* [0x00 前言](#0x00-前言)
* [0x01 获取适合 us-16-xg 的 3D 打印件](#0x01-获取适合-us-16-xg-的-3d-打印件)
* [0x02 购买合适的猫头鹰风扇](#0x02-购买合适的猫头鹰风扇)
* [0x03 拆机](#0x03-拆机)
* [0x04 减速线](#0x04-减速线)
* [0x05 安装风扇](#0x05-安装风扇)
* [0xff 参考](#0xff-参考)

## 0x00 前言

最近在考虑升级家庭内网，最开始买了个小型万兆交换机，Switch Flex XG (usw-flex-xg)，这个小设备挺精美的，当然 UBNT 家的东西都挺精美的，虽然它只有4个 10G 电口。

到后面发现有的设备只有 SFP+ 光口，有的又只有电口，考虑到有很多这种复杂混合的场景，我的 Switch Flex XG 就不能满足这种万兆需求了，如果使用光转电模块，模块本身贵不说（便宜的出现兼容问题比较麻烦）， 发热量还非常高。

思前想后，还是考虑修改架构，从以前的纯电口切换到以光口为主，电口为辅的混合内网万兆架构，光口的优势很多，如模块便宜，发热量低，性能要求也低等优点，唯一缺点就是和电口的兼容性不好。 挑了很久的交换机，最后还是选中了 us-16-xg，这个产品在闲鱼上2000不到就能拿下，但有12个光口和4个电口，共16个万兆口，作为通常溢价较高的 UBNT 产品性价比太高了。

但这个产品的最大缺点就是噪音较大，两个小风扇吹起来有点吵，比氦气盘的炒豆子还稍大一点，要是放卧室肯定是睡不着的。

搜了一下是可以对它进行改造的，使用出名的猫扇，但不能直接改，原装的是 3CM 的风扇，猫扇最小的是 4CM，中间需要加一个 3D 打印件，下文详细介绍完整的改造流程。

## 0x01 获取适合 us-16-xg 的 3D 打印件

reddit 的[帖子](https://www.reddit.com/r/Ubiquiti/comments/idshm5/how_can_i_make_the_ubiquiti_unifi_switch_16_xg/)里，讨论了如何让 us-16-xg 更加静音，提到可以通过 3D 打印，打印一个转接头，把 3CM 风扇转接到 4CM 风扇使用，具体打印件的[蓝图地址](https://www.thingiverse.com/thing%3A4143421)。

对于我来说没有3D打印机，自己是没法打印的，还好闲鱼上有该打印件成品卖的，可以直接下单。 到手如图所示：

![/styles/images/us16xg/3dadapter_1.jpg](/styles/images/us16xg/3dadapter_1.jpg)

看起来比较简陋，但用起来效果挺不错的。

## 0x02 购买合适的猫头鹰风扇

猫头鹰风扇，简称猫扇，在风扇领域可以说是大名鼎鼎，说到静音风扇优先想到猫扇。适合该交换机的猫扇是最小规格的 40MM 直径的风扇，型号为 Noctua NF-A4x20 FLX，对应的适配器接口是 3 pin 的。

花费 125/个，两个共250人民币，在淘宝上买了两个新的风扇。

![/styles/images/us16xg/noctuafan_2.jpg](/styles/images/us16xg/noctuafan_2.jpg)

猫扇确实做得很好，看包装就知道，整体包装比较精美，内部风扇和配件一应俱全，配备了两根降速线（Low Noise Adaptor 和 Ultra Low Noise Adaptor ），扩展线，螺丝，减震胶钉等内容。

## 0x03 拆机

话不多说直接开拆。

先看下拆开前的样子，我这个虽然是二手的，但是成色挺新，划痕灰尘都比较少，各种配件也都在。

![/styles/images/us16xg/us16xg_3.jpg](/styles/images/us16xg/us16xg_3.jpg)

揭开头盖骨之后的样子：

![/styles/images/us16xg/us16xg_4.jpg](/styles/images/us16xg/us16xg_4.jpg)

拆的过程中发现螺丝刀质量不行，差点给我拧滑丝，我的刀头直接给我弯了，还好有个备用的螺丝刀临时顶了上去。

先把两个风扇卸了：

![/styles/images/us16xg/us16xg_fan_5.jpg](/styles/images/us16xg/us16xg_fan_5.jpg)

叫什么 sunon 的牌子的，也是 made in china 的风扇，这两个风扇看着小，噪音可实在是不小。

没搜到同款的风扇，搜到了一个近似款的，型号为 MC30151V2-000U-A99 Sunon ，感觉数据可能差不多。

![/styles/images/us16xg/sunon_fan_6.png](/styles/images/us16xg/sunon_fan_6.png)

可以看到这个小风扇最大转速能达到 7000 RPM，噪音可以达到 20 dB(A)，当然这个值噪音值也不是很高，但实验室数据和实际数据存在较大偏差也是正常的。 :)

虽然猫扇的转速不如原装风扇，但猫扇的直径更大，最终满速散热效果应该和原装的风扇效果差不多。

## 0x04 减速线

猫扇是有减速线的，但这里我没有用，因为减速线主要是以减少最大转速为代价，比较生硬，虽然确实静音效果非常好，但也对散热有一定影响。

官方对于减速线的效果是有统计图的：

![/styles/images/us16xg/noc_fan_9.png](/styles/images/us16xg/noc_fan_9.png)

使用 ULNA 跟不用的效果确实非常明显，但我家里因为其他设备也挺吵的，根本没有那么安静，所以我就没有接任何的减速线。

如果读者有这样环境的需求，那么减速线也是可以考虑使用的。

## 0x05 安装风扇

接下来把 3D 打印件和猫扇组合在一起，这一步需要考虑几个问题：

* 猫扇的正反，背面出风，正面进风
* 打印件的角度
* 减震胶钉需要修剪，不然不能完美塞进去。

安装第一个风扇：

![/styles/images/us16xg/us16xg_fan_7.jpg](/styles/images/us16xg/us16xg_fan_7.jpg)

两个都装好：

![/styles/images/us16xg/us16xg_fan_8.jpg](/styles/images/us16xg/us16xg_fan_8.jpg)

由于3D打印件没有考虑减震胶钉，所以不修剪的话会稍微翘起来，特别是放在板子上的部分。

然后把盖子盖回去，测试一把直接点亮，运行完美。

最后对比一下换猫扇前和猫扇后的温度和风扇状态：

换之前：

![/styles/images/us16xg/before_10.png](/styles/images/us16xg/before_10.png)

换之后：

![/styles/images/us16xg/after_11.png](/styles/images/us16xg/after_11.png)

可以看到温度和风扇和原来是差不多的，但噪音却已经小了非常多。

## 0xff 参考

[3D 打印件图纸](https://www.thingiverse.com/thing%3A4143421)

[How can I make the Ubiquiti UniFi Switch 16 XG quieter](https://www.reddit.com/r/Ubiquiti/comments/idshm5/how_can_i_make_the_ubiquiti_unifi_switch_16_xg/)

[[网络] 究极进化？不讲武德的万兆光结构全案例实场景组网分享！](https://www.chiphell.com/thread-2278906-1-1.html)

[Silencing the Ubiquiti US-16XG 10G switch](https://vcojot.blogspot.com/2020/09/silencing-ubiquiti-us-16xg-10g-switch.html)

[MC30151V2-000U-A99 Sunon 风扇手册](https://www.mouser.sg/datasheet/2/659/Sunon_08142017_MC30151V2-000U-A99%29%290%28D03022490G-00-1216833.pdf)

[UniFi\_Switch\_US-16-XG\_DS](https://dl.ui.com.cn/datasheets/unifi/UniFi_Switch_US-16-XG_DS.pdf)

Copyright © 2014-2025 [`Green_m`](http://weibo.com/u/2585957090).

Powered by [Jekyll](http://jekyllrb.com), theme from [Less](http://lesscss.cn/)