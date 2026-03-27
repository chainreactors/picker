---
title: C23-X05 魅影潜伏与仿冒陷阱：银狐组织借OpenClaw安装包实施攻击活动深度分析
url: https://mp.weixin.qq.com/s/1JQUgrXszTvkfVVdyqxQkw
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:28:29.985592
---

# C23-X05 魅影潜伏与仿冒陷阱：银狐组织借OpenClaw安装包实施攻击活动深度分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/j1hpA7GJeRC8aicAQ6hKGJ3VQgfHO0ibib2YQLrl5HGzpeDvuIn01NsicnlFfOporq8wTgKVHvkFu7PUrflJVb2AjqcwibJicBmk75tvVT5wiaNzpU/0?wx_fmt=jpeg)

# C23-X05 魅影潜伏与仿冒陷阱：银狐组织借OpenClaw安装包实施攻击活动深度分析

启明星辰集团

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j1hpA7GJeRCtVlt2o1C4LaPBu2Qrz18mDKOvWTCGWB2csSZaFaRHPVUd1ia6wycSrEEJu6wPfTTkPxgib8LJuHicj3B0ylKP5jt1nZUvBEnDvs/640?wx_fmt=gif&from=appmsg)

**为智能时代立信，为创新价值护航。**

**—— 启明星辰**

随着开源AI代理框架OpenClaw（“龙虾”）的爆火，黑产团伙“银狐”迅速借势发起钓鱼攻击活动。通过生成高仿钓鱼页面，注册仿冒域名，利用搜索引擎优化（SEO）和付费广告将恶意链接置顶，诱导用户下载伪装成“OpenClaw本地部署工具”的恶意安装包。用户执行恶意安装包后，在释放出合法安装软件的同时，暗中执行恶意程序，最终释放并执行远控木马，对用户计算机进行控制，实现信息窃取、内网渗透、横向移动等恶意操作。攻击者通过针对安装链路的投毒，达成了对目标主机几乎“零门槛”的远程接管。

启明星辰威胁情报中心（VenusEye）近期追踪到银狐组织多个仿冒OpenClaw的站点，这些站点上的恶意安装包采用了相同的攻击手法，根据样本特征和ioc关联，这些攻击活动都归因为银狐组织。下文以一个典型的样本为例进行分析。

用户访问仿冒网站http[:]//ai-openclaw.com.cn/，能看到较为精致的下载页面，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRAWdnxmxphwPQ9Cpoex5dSnUMMGyTZmBcO6FXPYBeetOlkhpKvGiaricdBMg9ncSD3dLXRc9ficTM3WP7A3gC3D6QZPlc0DVTHRpw/640?wx_fmt=png&from=appmsg)

用户点击页面中的「下载OpenClaw」按钮后，下载名为`opealeAi_7beAole-x64.zip`的压缩包。该压缩包内包含可执行程序`opealeAi_7beAole-x64.exe`，其MD5值为ff28115a55b9a11d92bbb458efe0b940。

**样本分析**

用户执行该恶意安装包之后，在释放出合法安装程序的同时，会暗中执行恶意程序。通过侧加载方式执行恶意DLL模块，读取嵌入了恶意数据的png文件，解密出shellcode并执行，经过两层解压执行，最终执行具有远程控制功能的恶意DLL。整体执行流程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRBo6PBibr9jZ5xiaINf7vTeM0drg5QMc3oVEbBw9m4whMg97icVZ1hJEjaTwVL3GRX22qiak16oCmTsYkmZSRBicRibykkl1ibOibuJZk8/640?wx_fmt=png&from=appmsg)

##

**原始恶意安装包**

##

## opealeAi\_7beAole-x64.exe是原始恶意安装包，通过Inno Setup工具打包而成，在安装脚本中指定了文件的安装路径，并指定在安装过程中执行名为“9k9UV.exe”的文件。如下图所示：

##

## ![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRAQeH9Ellpb9zAAUTdIK5Nib2p7qTuaNhXq5gG3gqfzKmAYJib1yMnHyhfCMjt5qfzJYWJs62dskaKDibZVSmDLLPxuRVKssvUssY/640?wx_fmt=png&from=appmsg)

##

## 用户执行opealeAi\_7beAole-x64.exe之后，会将多个文件释放到C:\Program Files (x86)\165jut\yPSTY中。安装程序在桌面创建名为“Claw”的快捷方式，指向文件C:\Program Files (x86)\165jut\yPSTY\BTM1j\OpenClaw\_77b4b0ac.exe，以迷惑受害者。BTM1j文件夹中除了OpenClaw\_77b4b0ac.exe之外，还有一个图标文件。如下图所示：

##

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j1hpA7GJeRCsn8gst6KpsMc311teRkz78lwnw88IuvDYRpzWbsscxa4cARBwpPENrqDWEhxHKJ0t3JEHMN3f3ibiaZjJWviaswiaFZJrqiaqa8AY/640?wx_fmt=jpeg&from=appmsg)

OpenClaw\_77b4b0ac.exe是国内某公司开发的合法的OpenClaw本地部署工具，具有有效的数字签名，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRCEtP3KQBqBavXNicdOkrXvBUM6jFNdXKTDxTeQ8GlvhFicGk5uFl2lj5ULTIhfX9IZvU5I8tx8zIOwiaQuRJvz2MZN81nyFqNtqo/640?wx_fmt=png&from=appmsg)

运行该程序，会进行OpenClaw的本地部署，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRBlXEutEYg1EEGjR4TFzia8KOYs4WtnQ5mxlbJ0uDWeKzCibehOll4ymNw73ibz6FJ5XlqXGJtD7CBF0llIF2CCbW9e8vzZsQeXEk/640?wx_fmt=png&from=appmsg)

原始恶意安装包会将3个文件释放到dhbZ4文件夹中，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRDrBwuQuSyDjwForjsP45Flj4FhB5owDibL6p2a86ibVBCyesGK5mEOuhYp7icKIGnsGRlPM7spv5WibTia8HTGGwEmyiagaaL3OomH4/640?wx_fmt=png&from=appmsg)

其中BxakJ.Mx是png格式文件，可以通过图片查看软件正常打开。如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRCUmIdibdTDnvhnnasYiaR6ngJalkxh56LOibHEC7gxy7h7OBhCaicG9xlibHbibicGGeKMFSUUTcuj11oR3jSzZ9e890diaTcgqvW2QLA/640?wx_fmt=png&from=appmsg)

BxakJ.Mx中，在正常图片数据之后嵌入了多个恶意数据块，每个恶意数据块为0x200C字节，其中数据部分占0x2000字节。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRAmUOJVbCNBYvdgj5iaoZsXJWMnMOGxXGdHSz6IQLHw9p9QISibtN3cJzPXRicVibgTyM0qlQMtQNdJIEyxOZVdUr30LmOy5Ekuhos/640?wx_fmt=png&from=appmsg)

##

**恶意DLL**

9k9UV.exe会被原始恶意安装包启动，该文件是经过篡改的白文件，程序启动后，会自动加载同目录下的恶意DLL模块**vTPr.4DH**。在 vTPr.4DH执行过程中，首先定位当前进程所在目录，读取文件**BxakJ.Mx**中的恶意数据，通过**RC4算法**解密各个恶意数据块并进行拼接，随后创建纤程(Fiber)，在纤程中将解密得到的明文作为**shellcode**执行。整体流程如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRBYhSdibOibeIrv4miccbgIyTZ46w68lAZLks9XpPFFJTT0NXR4Wr702ibG4Mp7RC48yiaxTIIZ77JHicXBjTAkxBmnk8DlfAugDmmV0/640?wx_fmt=png&from=appmsg)

创建纤程执行shellcode如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRAQ6b7jtOmrwGNoYxDmJwhibNxjSwlylmhR7PvoDP6etIhUsJhP3PDGctleGAAmziaS1qWpgVzPgy6CEJf5icB3KA3iaGGfLbbTq28/640?wx_fmt=png&from=appmsg)

##

## 第一层payload

##

## 该shellcode由两部分组成，第一部分是加载器，第二部分是经过压缩的DLL文件数据。加载器的功能是从第二部分数据解压缩出DLL文件，并将其加载执行。如下图所示：

##

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRAFzibAIPib8jF2cuwISN7ic99z6kFAnsEgPWavts1yMp62lVMdpM67EaLClka6y0A9CZcxHgQu3soeW88aM735vxuHHHIYiarpAkk/640?wx_fmt=png&from=appmsg)

第二部分的压缩数据如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRC4J0PmUKZ4Cb63ACZ8YOujky8SLWTEaXvSgSyVqaQWJicCdCOfyF3K9Fic5rI0QtTMyOaX5iarbt631s2s8PL2HYmiao2ZiaLZo4P8/640?wx_fmt=png&from=appmsg)

DLL文件的数据压缩算法为LZNT1，解压缩之后如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRDuGUkIqpVRvcMY7Zr7ULoNR1t91BTaibXObiccYroU4deriaWd9FDjNx7xrXwHKRahbCCmuT3ZyvmfDFTXJZAPGwbMQNATu4qNrA/640?wx_fmt=png&from=appmsg)

解压缩后的DLL文件编译时间为2026-03-11，该文件经过VMP加壳，代码严重混淆。如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRC9ZAr5XpDukLvxkLHbib3rutlpibU3XlVzezuygTKiam9SmCq2CufPwHKTR5k8NlFEbyan5Xm3dX4Z9onfjchJ9DdrmFibqupjmMU/640?wx_fmt=png&from=appmsg)

该DLL主要有以下3个功能：

* 首先将当前文件夹及其中的文件设置为隐藏和系统属性；
* 解密出远程控制程序的配置信息，将配置信息的各字段加密后进行Base64编码；
* 再解密出一段shellcode，根据操作系统版本选择不同的进程进行注入。在Windows7系统中，将shellcode注入当前进程自身；在Windows10及以上版本的操作系统中，选择系统进程（例如sihost.exe）进行注入。

注入到进程中的shellcode与上一阶段的shellcode类似，同样由两部分组成，其功能同样是解压缩出DLL文件并加载执行。

数据压缩算法同样为LZNT1，解压缩前后如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRDsFk2vQfZE1FHeKxksDnia3jlcbLibbZrbANoKdMCVZwEVVCSS2WH7YASBIr2drWEDhhYrcJibZV7Rzuof91ck47vbkYsnyH2AzQ/640?wx_fmt=png&from=appmsg)

加载该DLL并执行其入口函数，将配置信息作为参数传入。

最终payload

解压缩出的DLL文件是最终payload，其功能是远程控制工具。该DLL的编译时间为2026-01-08，也经过vmp加壳处理。如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRDjHflrRmGko5ECmXz9J49tXjTXKLMicIePQDoTHZGqWjuI3ibx3txowfUiaP4NoicYDsTBnia9Tg4cb6oyESsXSiauN9wuBiaY0t2nK8/640?wx_fmt=png&from=appmsg)

配置信息被作为参数传递到DLL的入口函数，其中包含IP、端口、木马版本、时间戳等，这些信息经过异或加密和Base64编码。部分内容如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRDk2UmkFhkw09IhvRcWZxoEiavVib8lKOkgQ44BJ2Mpjic98Z94z0TiaQ9EHFtcNXwfNr485v5qtXzOlW1jV9EyRglxBPr396G8qbQ/640?wx_fmt=png&from=appmsg)

配置信息各字段的内容和含义如下表所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRB1olxquQyq1C869mbrosPyicnibh6SKDN9SWRBYMY0v6ibc3W2Y0EdAxAgGz8o4M7jd18J86CW1pMsVZf0U3hpZNPPVZYvichMgbc/640?wx_fmt=png&from=appmsg)

该DLL启动后，首先在%ALLUSERSPROFILE%下创建名为6C9A2AEAD706160111D90B7F3748D150的文件夹并设置为隐藏和系统属性，在其中创建文件config.ini并写入配置信息。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRBSAbicD2n6F4d1pp5bxmkQUlu4kayHibRVVWshiacKwYbjwYUlNW9lv5Fx3Z8uOozqZSVaiaI1liczZxvXYicic6AJ8wgxpnWgdicpwiaY/640?wx_fmt=png&from=appmsg)

config.ini文件的内容经过异或加密，其中包含ip、port、ip1、port1、ip2、port2、version等字段，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRDbfoNu4kfJZqCMxp42e4h4vY9bibZyYRRXOYWvaHaVzBC7t0oaXtia18kViaMLexBxgjog1zJuVXrOWKyH2u1WTiaJFDcnm8AbtC4/640?wx_fmt=png&from=appmsg)

然后依次连接配置信息中指定的各个C2，如果连接失败，则切换到下一个。网络连接情况如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRA3nxrG1AzbEfYRDkjSQ08ZX8oM8lw0b4PLbib4lib7qXPHqX9kTnRrOiahjVydp1tuETQ98r8rgnCIRSLcs1qoMpaB4M5Kpx20HI/640?wx_fmt=png&from=appmsg)

连接C2成功后，获取本机的计算机名、用户名、操作系统版本、MAC地址、内网IP地址、当前时间、Telegram和微信安装情况等信息，压缩并加密后发送到C2。收集的信息如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRAaMWvvgfF3ianCCYQ2ODT0cnzEXJp1brsGmz6rpI0MpYxn59kaqUUHcicoURbvpSzQhXdsr3VaBjl9MfvvHoTVAAB6OFZ2VANsI/640?wx_fmt=png&from=appmsg)

将加密后的数据进行封装，在头部增加了数据长度和固定值0x11、0x22、0x33、0x44，作为上线包发送到C2。对应的网络流量如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRCc0uXVSibQicYnEhhwDaFzgKlcJkY8a4ykEve6nFmiajh1l2xjGowU5tbGvNU44biaodNicQBCO6WLlxzUngx1Dm3y7JJ2JpcnMN4M/640?wx_fmt=png&from=appmsg)

将上线包的网络流量解密、解压，可以得到原始的明文信息，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRDPKzWr2oxD37Gyiaiat03c7ErSTwfNx2nIhD5LF5TcrDcLweiab0GjiavpricriafEDoWwaXRF1xGkSq8BtfZmgTzScp8N8gxAfpv0k/640?wx_fmt=png&from=appmsg)

然后从C2接收控制指令并执行，实现远程控制功能，包括文件上传、文件下载、文件执行、安装插件、键盘记录、CMD命令、绕过UAC等。解析控制指令并执行，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRCQGNHhRJavuRZKsfga9mRiaehFluv7azmr0dCDYon5F8ibIQ1NiapX6TH5GFoAYXo3lNN1hZPeDgbxsAHkl5urP2wSicPSjuL8nTA/640?wx_fmt=png&from=appmsg)

其中绕过UAC进行提权如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRBxjbISLGKun1N...