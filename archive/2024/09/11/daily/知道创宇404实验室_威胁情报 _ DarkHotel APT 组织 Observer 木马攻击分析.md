---
title: 威胁情报 | DarkHotel APT 组织 Observer 木马攻击分析
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650988197&idx=1&sn=467dc6837730e5dc30d6bd47a2fa2b15&chksm=80799c97b70e1581800d35234141ee640f517dfddd310f8b6049eaa003255408db11eed32264&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-09-11
fetch_date: 2025-10-06T18:28:57.166143
---

# 威胁情报 | DarkHotel APT 组织 Observer 木马攻击分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT065fC1wanlWMcrJfxYMke7CMLL3KkwUez4GpxYMA5xOVlicUORTicGKFeW20Ec2HLLVeJ88dhprOdw/0?wx_fmt=jpeg)

# 威胁情报 | DarkHotel APT 组织 Observer 木马攻击分析

原创

404高级威胁情报

知道创宇404实验室

**作****者：**K&XWS@知道创宇404高级威胁情报团队****

**时间：2024年9月10日**

**1. 情况概述**

参考资料

今年6月，知道创宇404高级威胁情报团队在分析过程中发现了几个APT组织的攻击样本，通过同源关联到其他的攻击木马，并对此展开了分析。根据近期国内外安全厂商发布的“伪猎者APT”组织的文章，对比确认为同一批通过WPS漏洞进行网络攻击的最终载荷木马[1][2]。

2023年8月至2024年7月，我们观察到Darkhotel的持续攻击活动，并使用了两套不同的攻击武器及技战术。攻击行业也早已脱离了Darkhotel名字代表的酒店行业。Darkhotel是有着东亚背景，针对企业高管、政府机构、国防工业、电子工业等重要机构实施网络间谍攻击活动的APT组织，其足迹遍布中国、朝鲜、日本、缅甸、俄罗斯等国家。2019年之后有关 Darkhotel 组织的行动在开源情报中的占比连年降低，同时国内厂商曝光了数个具有东北亚背景且技战术不同的攻击集合，我们认同这些攻击集合都是 Darkhotel 的子集，Darkhotel只是一个代表了该背景的攻击集合名字。

**2. 木马分析**

参考资料

**2.1**

### **样本攻击/释放链**

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7BCaPjXfFq0opPK8FPVEn1uiccMWMzaD4iaibQL43DZnAo927iagzyXZF8g/640?wx_fmt=png&from=appmsg)

**2.2**

### **样本功能综述**

###

本次捕获的类型1向服务端请求下载一个文件，该文件解密后释放的载荷与类型2几乎一致。与类型2不同的是，类型1在下载阶段还额外下载了一个lnk文件，该lnk文件的主要功能是通过COM劫持以运行释放的载荷（实际类型1下载的文件是将类型2中的文件进行了合并）。相较于类型2，类型3样本在文件解密后释放了两个载荷。根据**类型3**中**PDB**路径信息，将其记为`Observer`，接下来将就各类型样本进行描述。

#### **2.2.1 类型1分析描述**

类型1样本为dll文件，该dll存在一个名为`mydllmain`的导出函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7pWxHjj3IQ4CuqlvK4ewAkHykR1xibvogicsOf9VbHMJaMyPiczIxHyVHQ/640?wx_fmt=png&from=appmsg)

该DLL文件中的大部分字符使用了攻击者自定义的加密算法处理，该算法自2023年起一直被使用至今，解密算法逻辑为异或3再解base64：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7quU33Yutx3FfJ1YylFibLDauflaaQHEyqDgJliaBgyfDJCLqzNNb9zAQ/640?wx_fmt=png&from=appmsg)

滥用合法的windows的照片库查看器组件shimgvw.dll，通过其中的函数`ImageView_Fullscreen`，从远程服务器上下载文件zetaq.txt：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7OLxGRfdGMTyohnsTWGWw1Nv1gn9Mlyu72ibgcia6OC10fTY85AFqTxLw/640?wx_fmt=png&from=appmsg)

从`%userprofile%\AppData\Local\Microsoft\Windows\INetCache\IE`中遍历查找文件名为zetaq的文件，并从其中解密出后续文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke75Nt8bRJkH4ic1kHuh0T67pbINuP4JBXjwKdHsibDMticyfMrrWtehggNg/640?wx_fmt=png&from=appmsg)文件的解密及释放流程如下：

1. 从偏移2开始读取24个字节数据并解密，该数据表示包含的文件数。
2. 继续读取24个字节数据并解密，该数据表示文件总大小。
3. 继续读取24个字节数据并解密，该数据表示文件加密后大小。
4. 继续读取24个字节数据并解密，该数据表示文件解密后大小。
5. 如果包含的文件数大于1时，则循环解密并释放对应文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7b7fiaY2DIb68zQkJsCI7eYlBn8TyVW4LYMLDQIjC4cibUMsvtVH1JXVQ/640?wx_fmt=png&from=appmsg)

最终zetaq解密出2个文件，分别为`SecureBootUEFI.da`和`regit.lnk`，将`regit.lnk`设置名为`PCATaskServices`的计划任务，滥用合法系统程序pcalua.exe执行该文件。

LNK参数解析后如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7fHenfcQYrOyKzf3UtGBicBJX1DNyEwER1CibN2GJ4GzSxWic5Cz0TMamQ/640?wx_fmt=png&from=appmsg)regit.lnk的主要功能是将之前释放的文件SecureBootUEFI.da重命名为SecureBootUEFI.dat，并劫持系统COM组件`F82B4EF1-93A9-4DDE-8015-F7950A1A6E31`，利用该COM组件执行SecureBootUEFI.dat。

2.2.1.1 SecureBootUEFI.dat分析描述

SecureBootUEFI.dat的主要功能有两个：

1. 文件夹遍历：从服务端获取需要需要检索的文件夹路径，并将获取的文件信息拼接后作为UA回传到服务端。
2. 组件下载并加载执行：从服务端下载后续载荷并加载运行。

在SecureBootUEFI.dat中字符串的加解密算法变为异或3。

获取主机名和用户名，后续将获取的数据拼接后异或加密作为首次通信url的一部分：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7N7dia7LDc6CXRNsO5KbwAic4ohCsnAHWG6LestVpxy51HhyfrqibLU8Dg/640?wx_fmt=png&from=appmsg)

解密出两个通信C2，其中一个C2用于从服务端获取数据并执行，一个用于数据的上传（用户信息及文件夹遍历结果），为方便后续描述，分别命名为server1和server2：

1. **server1：hxxps://bitbucket.org/whekacjj/whekacjj/downloads/**
2. **server2：hxxps://c.statcounter.com/12959673/0/7901c79c/1/**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7ohJhg5Ao4ZNCrLtfDpUW6mGgkb7LPkZf1eV3micF3hktfBvbickpr3Sw/640?wx_fmt=png&from=appmsg)

文件夹遍历时通信的url格式如下：Server1 + xor3([pc\_name][username])\_[finddir\_count].A

向服务端1发送请求后，服务端1返回的数据为需要遍历的文件夹，获取到的文件夹信息使用`[ ]`进行包裹后用`,`进行拼接，最终所有的数据拼接搭配到`Referer:`后，并上传到服务端。

无论是否获取到服务端下发的文件夹数据，每通信一次则全局变量finddir\_count加1：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke76yNJupicb0c9QGQq1wfcsCdz50BvcbrQbdC1aK1Wf4ztVzuZKJ2XxDw/640?wx_fmt=png&from=appmsg)

组件下载功能的通信url格式如下：server1 + xor3([pc\_name][username])\_[download\_count].B

文件下载后被存储到`%Userprofile%\AppData\Local\Microsoft\Windows\Shell\Sample.tmp`，将Sample.tmp复制到`%Userprofile%\AppData\Local\Microsoft\Windows\Shell\Service.dat`并加载运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7Ghjr1XZAdBXMGbQpootz1uCxFuTLsp52Zbt1cUb6ate4rQicCMn4Q1g/640?wx_fmt=png&from=appmsg)

服务端返回的数据使用`g73qrc4dwx8jt9qmhi4s`作为key进行异或解密，而非样本中的异或3算法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7uCUVdfgDu23Ma8DQjGf3DaLYPiagSklulJ36AFwV3uO7fzrRp4VV9mQ/640?wx_fmt=png&from=appmsg)

当上述两个功能相关的通信完成后，样本还会向服务端发送当前受控主机的状态，包含当前文件夹遍历count、组件下载count、主机名、%userprofile%和加密后的主机名和用户名。

当上述流程完成后进入1小时的sleep，攻击者利用这种长休眠机制不仅能够在一定程度上躲避流量设备的检测，而且可以让攻击者有足够的时间针对指定用户下发组件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7hb6K6TcqaaA3CtwicZCB1uhNoPIJjSoB5rBvIDP8iaSA9Rp90TdsVicZQ/640?wx_fmt=png&from=appmsg)

后续则循环上述通信步骤。

#### **2.2.2 类型2 分析描述**

类型2与类型1在功能上几乎是一致的，以下仅有区别的部分进行描述：

* 区别1：lnk文件通过下载而非文件解密后释放。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7QPpJnY79andY1qXqjQib6CuXjiaDDjO3daZT9gr8tX2uyUibLxVEOAE0Q/640?wx_fmt=png&from=appmsg)

* 区别2：计划任务名为`GoogleRegisterTask`和`CLSUpdateService`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT065fC1wanlWMcrJfxYMke7SBA6EPhraerAia9UpLBCNpJdkfR2ZlHb1eazKI4mSbrE0nXYKRnB4kg/640?wx_fmt=png&from=appmsg)

**3. IOC**

参考资料

## Hash：

* 8620a8a3f75b8b63766bd0f489f33d6a
* dd2f326bac70baca94eb655bdfae175d
* 445a84e3216da14b73dbe52aeb63e710
* 030a68e321dec0e77b4698fccc5d54db
* dd2f326bac70baca94eb655bdfae175d
* 18fdde4bf8d3a369514b0bc8ddcf35dc
* ccf49ea51585ae38fb510b0fa52aec08
* 7e20f52d4e7074663d9f9a252b59a2d6

**4. 参考链接**

参考资

[1] [Operation DevilTiger：APT-Q-12 使用 0day 漏洞技战术披露](https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247511799&idx=1&sn=dbee6e45aaba5f7c6308a2858553cf8a&scene=21#wechat_redirect)

[2] https://www.welivesecurity.com/en/eset-research/analysis-of-two-arbitrary-code-execution-vulnerabilities-affecting-wps-office/

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT0Z79Hq9GCticVica4ufkjk5xiarRicG97E3oEcibNSrgdGSsdicWibkc8ycazhQiaA81j3o0cvzR5x4kRIcQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**往 期 热 门**

(点击图片跳转）

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT2OVmxDyJicjufFMKd825S8D4EIWeBMuAAjJOibiahygyOfMhdQoK8SzCZ5WCyWzvm3gM66QyUGUr5cw/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650985033&idx=1&sn=eb8264e9eb4f3dec90c22ecb464e5e9e&chksm=8079907bb70e196d58b310e5733e4c9cb0f7a6d4c4d51c3afeca35f73b14cbfc828e2d2afb95&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxltIJSd9MIY6u8ORKtZZNG0oxfmTK2Iuo7rgYc7ujXmqVWYbygYAYkcg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650984694&idx=1&sn=7ba5d62b933542ac64cecc692e8fc282&chksm=807992c4b70e1bd2f0588c7c9f865cc4200bce4a37f718e61a4d8c85eaaf9bd84e6498ad191a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GZ2mYNZYnqOD2pAicQctCmNHw5fre6QTGr4XJ0CJGqmEncGw9z0z7BYA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650986722&idx=1&sn=683cdf211094018be422a0e4ef628522&chksm=80799ad0b70e13c6ae3b436f74551c84a1d3d93e1653e6610787182e935d2238b33c9c8ab14c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT3XlD8Odz1EaR5icjZWy3jb8ZZPdfjQiakDHOiclbpjhvaR2icn265LYMpu3CmR1GoX707tWhAVsMJrrQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

戳“阅读原文”更多精彩内容!

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

知道创宇404实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
...