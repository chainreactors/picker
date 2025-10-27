---
title: 微软WHQL签名申请完整流程
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458568532&idx=2&sn=e6a287a0fe9aff2df01c76f6df7ec382&chksm=b18df7de86fa7ec8d2fd21d98904bf22ac76eae5d6e2145700917af4d70b453f7b93eaab0968&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-17
fetch_date: 2025-10-06T18:05:58.744303
---

# 微软WHQL签名申请完整流程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZBeLdLXyWB5Bo3gia7icolZTyTwfF575tyiagavkAUGPX8WWNvWibLttLCw/0?wx_fmt=jpeg)

# 微软WHQL签名申请完整流程

yirucandy

看雪学苑

```
一

whql认证是什么
```

whql(Windows Hardware Quality Labs)认证是微软针对第三方的驱动程序进行的一系列测试，旨在确保驱动程序的兼容性。windows 10 1607以后版本的操作系统版本安装的驱动程序都需要先通过whql认证。否则会弹出红色警告框。

```
二

注册公司开发者账号
```

1.以下操作最好使用代理软件进行操作，否则打开网页会很慢。笔者这里已经提供注册好的账号，直接登录，无需再注册，可以跳过步骤二。

访问:
https://developer.microsoft.com/zh-cn/dashboard/Registration/Hardware?step=GetStarted

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZ8dRLjI6MGb2JzDBZlialvWiaib7zib9qCzkbaBg6gINhkibCbLQ8TWIa08w/640?wx_fmt=other&from=appmsg)

提示首先确保先拥有一个EV代码签名的证书。这个证书需要向微软授信的机构购买。

下一步，来到下面的页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZ2VdZcnvF4LAl0ByTEtibiaib7kjxVQwR0nweCMXZxs5zKDxyrO73KSUTQ/640?wx_fmt=other&from=appmsg)

点击”免费新建目录”:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZ5hSjsgWEVYbnEKIAFzhgaiaL8Deia8fvoBowNT9yYbdIuvzuy5S0jw9g/640?wx_fmt=other&from=appmsg)

注意这里的用户名、密码，是你后面将要登录用到的。

点击“”创建“”：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZLGtHuUdK874xG06AfSXgzeaRsz52CaWWZxbR1HT9nrBdz9RkOTyYibA/640?wx_fmt=other&from=appmsg)

创建成功了。点击“下一页”：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZeZhrVGeTxCWMM5C9uUibkyTWXsnj8YImzhKOvUmU1SkClWqMkfOcplw/640?wx_fmt=other&from=appmsg)

输入刚才注册的用户名，点击“下一步”:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZnRtp6w1xNTdMP3Zriajiaga3zT9MEnd5ef7WRIXqHToQfgmqIX4n8sibQ/640?wx_fmt=other&from=appmsg)

输入密码，点击“登录”：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZoibP3Y2R6b86SConl8NKsk0B6WQDibIRDBZtC1c9XfichLCFr3tQQkuJA/640?wx_fmt=other&from=appmsg)

填写好账户详细信息，“下一页”：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZHIYEexp6KrKLCNP22JHZgnMsRjdSwMibJJ87Vo4WnSgcibcOVuCaU8eQ/640?wx_fmt=other&from=appmsg)

若已经有EV签名证书，点击“下一页”：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZUvniaIz50CEFavKNLM1yvPBzhphz9D4Ghtz3iapicktorqMzt5Kgk4Ceg/640?wx_fmt=other&from=appmsg)

点击“立即下载可签名文件”，下载到![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZ94FvvsXu4UlPuicszKWjNJ2AzOJj4cP6iaoevMckibt2c0mhK8aJmwOYg/640?wx_fmt=other&from=appmsg)文件，使用EV证书对其进行签名：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZMWbDUhCUAYF23awANxKEyKQibmYnyqTx2VWHvweB9nHIbPkq26LWgNw/640?wx_fmt=other&from=appmsg)

笔者包中会提供EV签名所需的文件和说明，按照说明进行签名。签好后，上传签名后的文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZ33TwBCw25aibmHgK3QDRbfkIGo1icQicj5MChV8hhibZpqPsE1cm9ibMia2Q/640?wx_fmt=other&from=appmsg)

由于笔者之前已经使用这个相同的EV签名工具签名了SignableFile.bin文件并上传了，所以提示“此证书已用于注册”。后面的注册过程就不在截图了。

```
三

登录公司开发者账号
```

1. 访问：
https://developer.microsoft.com/en-us/dashboard/hardware

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZygweAxUibDFwvqVdrBbweUuw20tmQdkJQPa5ROnbyKzjDv0GZ0xwEOA/640?wx_fmt=other&from=appmsg)

使用刚才申请的账号登录，我这里使用之前申请的账号登录：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZcqJSRMOuXp5gLoiclYlhtKdFAxDuBLjj8Bm4GcV1BYuVo7yjoeN0ibFg/640?wx_fmt=other&from=appmsg)

首次在电脑上登录，手机的Authenticator会收到请求登录信息。这个是注册的时候会提示下载的，用于登录验证的。批准后，会跳到下面的页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZ8oyzgyEBG1oazGc8jCEMhPib3ia5xyErSF4N7AMCibAh0cY44a5ZrcDMA/640?wx_fmt=other&from=appmsg)

到此，注册、登录微软开发者账号完成。后面就需要使用WLK测试，并提交测试报告给微软了。

```
四

准备测试设备
```

至少需要两个系统（必须为英文操作系统），不能是任何的虚拟机，必须是物理机。

测试服务器 一个windows server版本的系统，推荐使用windows server 2012。

测试系统 需要windows 10 版本的操作系统，并且安装好要测试的驱动程序（1607以后的windows 10 可以打开测试模式安装驱动）。

若测试系统只有一台，可以安装windows10最新版的操作系统(笔者用的windows10 20H2)。笔者经验证只测试一个最高版本的windows系统，也能获得WHQL签名。

另外这两个系统需要加入在一个内网并且加入同一个工作组。如果不在同一网段的话，可能安装完HLK client后连接不上HLk server。加入了同一网段后，如果未把测试服务器和测试系统加入同一工作组，则会导致HLK测试的时候找不到测试的项。

```
五

安装测试服务器
```

Windows Hardware Lab Kit (Windows HLK) 是一套进行whql认证的测试框架。HLK套件仅用于windows 10，如果要测试windows 10 之前的操作系统，需要使用HCK套件(Hardware Certification Kit)。

HLK的下载地址为:

https://docs.microsoft.com/en-us/windows-hardware/test/hlk/

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZ1Qr8LHdVxM4LFic4NRLY2JMc2HicwiaoficPqEt7mzKPIj64BcE8hYZf5Q/640?wx_fmt=other&from=appmsg)

选择对应测试系统对应版本的HLK下载
安装完选择Controller + Studio 一路点击Next即可完成测试服务器的安装：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZxuGHpLuxVWqvIgyZxPH216Eic8JwNKfvkuo4BOBIpVMuqibaice73yqGw/640?wx_fmt=other&from=appmsg)

```
六

安装测试系统
```

测试系统的安装不需要额外的去下载安装包了，应该从安装完成的服务端获取。地址为：
\\HLKInstall\Client\Setup.cmd

例如我们的服务器地址是192.168.2.239：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZmcia2nbvbSPl9sfXXFh6NTSibGoQ1cqyL9upLNOWdfwuqyyG8QAFgRDg/640?wx_fmt=other&from=appmsg)

双击setup.cmd，即可出现安装界面：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZP1ZJiaHFtQaCOI7kjCSBHCLV8tHz2cYHicYiaEiaVf2mG8KUjCA25FHsIw/640?wx_fmt=other&from=appmsg)

也是一路点击next即可完成安装。

安装完HLK client之后，去服务端打开HLK studio，便可以在默认连接池中找到我们刚刚成功安装的HLK client。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZbmIxYAgupLK7UiblfEI3ILjOP2k1DrUV4ibuVo7lVftODgwETQr4K2lA/640?wx_fmt=other&from=appmsg)

HLK的测试环境到此搭建完成。

```
七

开始测试
```

首先点击Configuration菜单栏，新建一个计算机池（HLK控制器会把测试的任务，分配到你选择的计算机池里边），然后将默认的计算机池中的计算机拖动至我们新建的计算机池中，然后右键计算机池中的计算机，可以改变其状态，当计算机的状态为Ready状态的时候，即表示当前的计算机可以开始测试任务了。有时候想重新测试时，状态改变不了Ready，需要卸载测试机的HLK client，重新安装。

配置好计算机池后，我们就可以新建测试项目了：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZGRBSibAB7ibw3gE7ciaLGWEY9IteAic41YeLjerdnIGmv1qGAibRYM9Vu0g/640?wx_fmt=other&from=appmsg)

新建完成后选择项目，然后点击Selection，到这里可以选择测项，由于我们的驱动程序是一个WFP网络驱动，选择下图红圈中的Software device，选到对应的驱动程序，打上勾即可：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZQxu73GqutyxWMBqANxHmhiayJgadVyPTAjae1sADHAcsFEWRLA1tRAw/640?wx_fmt=other&from=appmsg)

注意这里需要使用工具加载驱动，并把驱动对应的注册表键值的Start改为1，因为要随着系统启动自动加载驱动。有时HLK Studio的Selection的Software device的列表中没有要测试的驱动，这时候删除Configuration中的Ready状态的计算器，重启HLK Studio或测试机，就能找到驱动了。

下面切换到Tests选项，到
https://docs.microsoft.com/en-us/windows-hardware/test/hlk/
下载playlist。点击Load Playlist，加载对应测试机对应windows操作系统版本的xml文件。

笔者测试机操作系统是windows10 20H2，所以选择下面这个文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZPQdVtDic6vufRaicI3XiaboYiaF4TjXfd2EIAud3cbq9ICB8QoiaRUsXlGQ/640?wx_fmt=other&from=appmsg)

这个功能可以省去很多测试项目，比如下面没有应用Playlist时需要测试很多项目：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZYebrhy8yTkBIzpoA60miawBUZguTfm41wLUH1XfvhCX1u0aSnBXA8Sg/640?wx_fmt=other&from=appmsg)

有些项目是无法测试通过的。

应用后，只需测试下面的项目：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZiaKce7yOyEESGRLuPfIuud6nUpJxJkYL4CXXFhoaI1HZjeIYwIsEricQ/640?wx_fmt=other&from=appmsg)

需要注意的是，笔者在测试有些驱动的时候，先应用了Playlist，只剩下上面这个测试项目。测试开始跑后，EnableDriverVerifier、SetDriverVerifierOptions、QueryDriverVerifierSettings无法通过。解决办法是先不应用Playlist，待上图中的测试通过后再应用Playlist。

下图是测项旁边可能会出现的几种标志的意思，比如有个人形的logo代表测试的时候需要交互：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZic7qBKxB2QDlqHbVqw4XdVeU6xR6C6npPv1Za2QxBlxXrq7eIjtN5IQ/640?wx_fmt=other&from=appmsg)

给全部的测项打上勾，点击Run Selected，此时测试就开始了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZmAZxicz6VVFezytn5P6xibGCXrypUCGOeCrnk5LOB1TicnGIibGsT44L5g/640?wx_fmt=other&from=appmsg)

测试的过程中测试系统会重启，等重启完成后，如果驱动程序需要手动启动的话，就先启动我们的驱动程序，驱动程序启动后就不需要再操作测试系统了，等待测试完成即可。

测试完成后去https://docs.microsoft.com/en-us/windows-hardware/test/hlk/

下载Windows HLK filters：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZpRWyhE57RwxdkC3brcxTvy7eXKq6zMIicB7F8T5PRoQ9IBy8b7V9RyA/640?wx_fmt=other&from=appmsg)

按照里面的步骤去做。

注意：在HLK测试时，报错，错误日志如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HXbURdTdBDW34TsIEGmsPZYaY6OmEMs6kzwjyXzUecqAWvF9H22nicicSh3QR2zqicUW59eANhcrWSg/640?wx_fmt=other&from=appmsg)

解决办法参考：
https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/single-binary-opt-in-pool-nx-optin

在
![](https://m...