---
title: 乱下载软件致MBR锁机，逆向分析自救
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458490554&idx=1&sn=df61e994359baaf1a4dd12465b30da43&chksm=b18ea63086f92f26f49e11c240832273c62616f0b236e4557e5ebd7653b257b80c0fb1e09d50&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-04
fetch_date: 2025-10-04T03:00:01.512177
---

# 乱下载软件致MBR锁机，逆向分析自救

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuA8uianK0vTX0guNJmvGhkib7MH1WNNoUzmWlicLAicV4VoRmviciciab2ORDQ/0?wx_fmt=jpeg)

# 乱下载软件致MBR锁机，逆向分析自救

Axinger

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDu6Pe4Td9cKibiab8xHgqTSACWiascOQOIzFGe7mbzT2WlBrRO20QLq389A/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：Axinger

###

### 在某企鹅群里发现了这个东西：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDunicmwLbkxicxLGJsLXGX1DJOdUqO67ZV9sLIHOQDXyOTgPDac5Xt1K3Q/640?wx_fmt=png)

### 我一看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuTH9LgaLwIwh7HUFTldtQI2wQAia6wWfbtmCvg5rtxhcRkicljPsOWzDQ/640?wx_fmt=png)

### 你这辅助打激素了？长得那么肥？

###

### 于是我直接给他打开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuAibnWD0mq4twHYEaqdDoLj6FDmXs5EwNY6Kv9siaIko7QJibuBlic5UWfg/640?wx_fmt=png)

### 不讲武德！偷袭！

###

### 这不得让你进1W3好好玩玩？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuACbmLxKIIKZ90iaicfDsgCp1eiaiaokOl5mFlnroYOULwoSHMTX7rHiafpg/640?wx_fmt=png)

#

# **脱壳**

###

### 不查壳了，直接扔进来。

### 通过观察我们基本可以断定是upx。

## 那就用我们最爱的ESP定律吧！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuO7oMtrKc4icsodgqibYOgfXVrB2X269JW4sXjetf8lUXhlKicWOvYUI2w/640?wx_fmt=png)

###

### 单击F8向下走一步。

### 然后右键ESP，点击一键断点。

### 如果你的OD没有这个功能的话,那就点击跟随到数据窗口，在数据窗口第一行右键，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuyb2oRv9QvsEGjvbsnTNL3wzce3MHy8cbZWrHkAgwLwgWDrmsSPXW4w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDudsCnPdNibY22BR1vpib5e78NoGaZMwx7BApLmHRZLjaAnU2RJl1WtuRg/640?wx_fmt=png)

###

### 之后我们F9直接运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDujKfD9h4RbXibvtL0UklYN9QXmIicnHxHZQjEJRPe3xT4p2vtxl1bbv9w/640?wx_fmt=png)

###

### 断点下来之后在jmp命令上按F4(可能要按两次)。

## 之后单击F8即可跳转到OEP。

#

# **分析**

###

### 但我发现即使跳转到OEP字符串也不是熟悉的易语言。

### 于是我下了一个CreateFileA的断点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuUaePK8gCkKE0IABDS2xM15AEuS2fWkoMCkyGhgYIZibib8jNRNHTjRibg/640?wx_fmt=png)

### 他释放了一个dll，暂时不清楚是干嘛用的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDunzrqnYC9b5icXcwhtdTeialRseHkhY4lDXiaOfYDvTeHlVo1pHIysbNlQ/640?wx_fmt=png)

### 反正不是好东西。

##

## 现在转到00401000搜索字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuTZm6P6bxVdAG0qNoJGTTq6qJaicIZAvrK91kWsxPz9YZaNDlZ6SbPQg/640?wx_fmt=png)

###

### 真行啊字符串都不加密，这不就和裸奔一样了吗？

###

### 然后我在这两个可疑字符串段头下了断点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDulnickcjdxqdJ2o3KDrGWQNk8hL8yERC2uDciaNLzD3nrtaNul5PvhqPg/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuBhSDfYuF0ulJYDn9gxTibpBRSDXM5PIEibuEbSUBem5bibLSShzmYh4Jw/640?wx_fmt=png)

### 之后F9直接运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuAibnWD0mq4twHYEaqdDoLj6FDmXs5EwNY6Kv9siaIko7QJibuBlic5UWfg/640?wx_fmt=png)

### 熟悉的警告。

###

### 我直接给他允许了 (因为我从来不用win自带的任务管理器)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuEPeGOHE3ibCbbroIreAqNibJdHS2yibd8z0x9DicL5PdEQa48ZA4lZLazQ/640?wx_fmt=png)

### 还挺唬人的。

###

### 我这可不叫破解昂，我可没修改过你的任何一个字节。

## 之后他断下了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuLgIPOotJEQsuH1DmDwTqazU7Y9kTI4hrKcmxZS0za7yOTEx1QULfbg/640?wx_fmt=png)

### 这个函数有很多病毒界面的字符串，基本可以确定密码是在这里生成的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuIZSvsWnxhibFOX0PUB4qsuctUAJkGOXNajI3lqpm0NxxNn0InicxAejw/640?wx_fmt=png)

### 上图这个跳转我不太理解，好像正常都是跳过去，我直接修改标志位让他运行下去了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuuaeJnZVzCAQ1Afg3bZQibpibplyCAQ2uTDqONib51Bm55eWS7SiacNpE2g/640?wx_fmt=png)

###

### 我们一步一步跟到这个位置，这时候EAX上已经有了ID号。

### 接着单步跟下去。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDudjiaMseZxyaVctudDZdMZRzFyFma4cRPAtUaicx7c0gobVxyHDCtU4TQ/640?wx_fmt=png)

###

### 经过上面的call之后密码赫然出现在EAX上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuyg613BPIKMr7fLUytQRtWvmSdFB02vCNianficYjeW1BabibPhh2qgHibw/640?wx_fmt=png)

### 那么我们就可以断定00401810这个call就是生成密码的函数。

### 现在我们下上断点重启程序。

## 重启之后我的ID号是94(忘了截图了)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDueOb8PUmDYTicS3hDOeMgDJxWSSxwgsqSoIOdUFQK6APNvNjlWiapoTkQ/640?wx_fmt=png)

### 我们直接来到密码生成的call。

### 我们发现经过这个函数之后EAX中出现了"29"字样。

### 暂时不知道他是什么，先接着走。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDup2IK7YtLlRLvMyg1DNNia4AWZIm0MLullqBbDGUonTFLqWOTvQnvj2Q/640?wx_fmt=png)

### 又在一个同一个call出现了"24"字样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDunNNHCRcZ0iasibZ2MHqwu6eVKs4K14masZ6U4IOYicYdl0rib1ccic184Eg/640?wx_fmt=png)

### 接着一个call把这两个字符串拼在了一起。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuMybsNrc5UgRphdyAva4QiceswHh2spED16mAKkLvicrbueojQcYG0Ivw/640?wx_fmt=png)

### 出现了“23123”字样，暂时不知道是干嘛的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuJ1fWmCtnKL7pXWgLuRY8YeyNsEl50icyoy5RPEiaKLzK7DZRlnYUBNqA/640?wx_fmt=png)

### 经过这个call的时候程序线程卡死，恢复之后出现了一串不明字符。

### 通过观察我们可以猜想：他是一个MD5值。

### 于是我打开了MD5加密网站。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuxjdwQ6W0j8LNvO1kfsSzFGFeKVfib5UNkm5aT09eAMlYBfg9ictaib2ag/640?wx_fmt=png)

### 23123 : 860b432652504fa60f8da945398e20de

## 和EAX的值完全吻合。

### 那么这个call执行的就是MD5加密操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuLdoe1Tc9DzeYNj7BtQEEoBA94fYHaicC7CazmgYzDe5EKEeoTGjyznw/640?wx_fmt=png)

### 这个call 将MD5截下来了一部分(3-11位)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDucWPeLwPRaEeGbyNuhgmqJ2xvtfoC1CuQXypJibfMyNZbIv68xb1qI2Q/640?wx_fmt=png)

### 之后转化为大写。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDukVVicnacS6oUiaTBnxtLPBns8KMRbBPVzXsqIkxn3lflEgv8FbVLUXvQ/640?wx_fmt=png)

### 把之前的"2924"合并。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuicMFrKaXAObSichCeNMEJibhFd1uRCUxBOjZfSIexJmLXB0T8ZRwnYY0Q/640?wx_fmt=png)

### 最后的栈

#### 密码

#### 23123

#### ID

#### 显示信息

#

# **现在通过你聪明的大脑来分析吧~**

###

### ID:94

### PassWord:2924 0B4326525

### 后面没什么好说的，看看"2924"和"94"的关系。

### 很明显，在"9"和"4"的前面加了一个"2"。

##

## 由此可得: 密码 = 2 + ID第一位 + 2 + ID第二位 + 0B4326525

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuTwEHxo4BnTOuuyNU9FeIO09gvsF7hwdiaFgyzKGanfr55pe1TdzK1Mw/640?wx_fmt=png)

###

### 改MBR了，咱就得对自己有自信，我直接允许(大家别这么浪)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuZbLIKRQdEs3XicicdTYQiaLUlIThD6cT8AdXULIE3qPydfVMWpoUPIjIg/640?wx_fmt=png)

### 很快啊！就像是过了一秒，机子就关了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuy52fRy6HRXQiaSic4hXd1wI4PeCtmwnyOadRSsbs3Wwa8qmedf0qyglQ/640?wx_fmt=jpeg)

### 启动之后就这样了(不要在意那个黑洞)。

### 感觉挺标准的MBR锁机。

## 现在我们输入密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDug4sjwvwmiaY94iagse2VnZuRjG0WcC0zzBEqeiaL08UILQib3FwgmcR5ug/640?wx_fmt=jpeg)

## 回车。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuf9bR3Lee91byRMYUGTGeVp3iaR8FfLjrwibRJ3QGOAXVNNeJuRmZrOUw/640?wx_fmt=png)

##

## 正常进入系统。

#

# **总结**

##

## 1.千万不要随便开软件，尤其是名字有[辅助][免费]这种诱惑性字样的，认准正版辅助。

##

## 2.电脑尽量装一个杀毒软件，至少可以抵御MBR锁，用户锁这种脑子有包都能写的锁机。

##

## 3.如果你被锁了就使用PEU盘重建MBR(没有？没有就去做或者买一个)，尽量不要付款(你永远不知道打了钱之后对方给不给你密码)。

##

## 4.就算你知道锁机密码也不能在实体机打开锁机，部分锁机不光是锁机器，而且有可能在内置一个远控或者感染病毒之类的东西(非常麻烦)。

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDu0oeNmIjJnm8jBNA4OZxiaey7vqB6daYp2nllgZFlgWictrn6zxpGpvZQ/640?wx_fmt=png)

**看雪ID：Axinger**

https://bbs.pediy.com/user-home-930820.htm

\*本文由看雪论坛 Axinger 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FJVH3PGSiaY563SLhIPrI0tKsReH9ARfAoZb9ibj7MGPKOXiceialNsOGKPTYRKxcFMlibNjcdZml6dmw/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458487503&idx=3&sn=2961e0a289c1e755b2fc5b0403f73f8d&chksm=...