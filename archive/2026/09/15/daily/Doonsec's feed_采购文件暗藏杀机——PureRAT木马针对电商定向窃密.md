---
title: 采购文件暗藏杀机——PureRAT木马针对电商定向窃密
url: https://mp.weixin.qq.com/s/tseg9C7Sx4QVZceCl8RXlA
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T06:59:44.755579
---

# 采购文件暗藏杀机——PureRAT木马针对电商定向窃密

# 采购文件暗藏杀机——PureRAT木马针对电商定向窃密

原创

火绒安全
火绒安全

火绒安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SqeITVe7cPHYPzldRcYFWP8mamxDxDtt3dNkPcxwuJRvYPLOAOOvuLfu1MXGAQYhVycw1G3WmryJiadrbbKEss267g9A3Mg8MJ8/640?wx_fmt=gif&from=appmsg)

近日，火绒安全实验室收到用户反馈，称其在日常网络交易中经常有人发送“采购文件、下载打开”的信息，经溯源与技术分析，火绒安全工程师发现这是一起针对性瞄准电商行业商家的恶意网络攻击活动，该攻击主要通过站外社交、私聊、邮件、陌生对接渠道传播，攻击者伪装成合作客户、采购方，将恶意hta脚本文件伪装成正规的采购资料文档，以发送采购清单、报价单据、样品核对资料等商务名义投递恶意压缩包文件，精准诱导电商运营商家、店铺工作人员解压打开文件，触发恶意程序运行。用户误打开该伪装文件后，程序会在后台静默运行，隐蔽释放并启动多层恶意加载器，全程无明显弹窗提示、无运行痕迹，最终在系统内存中落地运行PureRAT远程控制木马，实现对受害终端的长期控制、数据窃取等恶意操作。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpKuMCSiaaEbvAOHOtznSAaFcfe0SiaFLj7hEGtUlnyDOY3ByALP3BLjEzGa1sibL679ibYsoMAib2fLwvXRAcvueqlTicUORXxcZ1Zo/640?wx_fmt=png&from=appmsg)

用户反馈

在样本传播的第一阶段，hta负责隐藏窗口、释放文件并启动加载器；第二阶段加载器将自身复制到加密硬编码的指定目录，通过随机数据膨胀文件，并借助rasphone.exe及Connection Manager配置文件间接启动转移后的副本；进入目标路径后，程序初始化clr、修改当前进程内的AmsiScanBuffer，再以内存方式加载托管Loader。Loader随后解密名为PayloadSource.zip的资源，恢复并运行最终PureRAT。

PureRAT与控制端建立TLS通道，并使用protobuf交换结构化消息。其功能包括主机信息收集、安全软件探测、浏览器及加密货币钱包数据窃取、屏幕截图、摄像头探测、计划任务持久化，以及在内存中加载控制端下发的.NET工具模块。

目前，火绒安全产品已实现对该行为的拦截与查杀。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sqm7aI4RVvBJ9ksU3jXI9vhPtQ7Gkicib09OgqAvtAibPElhTibBQ16NoQY9A6k70Eo9sC3J4yEPc01qeG391zevRP4mjQDx58xXTQ/640?wx_fmt=png&from=appmsg)

查杀图

**0****1**

**流程图**

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sp7icDzCNvKltxv0TUpR1nawYIJ6u0lZXCJ7cdfIjeX0XmShWP7EoSRFMSMuY1WUvx7tCH91ic27Vt8g106wvYqOEABQQfeNUWFw/640?wx_fmt=png&from=appmsg)

查杀图

**0****2**

**样本分析**

攻击者向电商商家投递包含“9月份采购样品清单.hta”的压缩包，诱导收件人打开附件。用户双击该文件后，Windows系统调用mshta.exe执行其中的HTML与脚本代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqutuPNHdF0HKY4zQd2qZdRXLBmw0U0ibzm1dck3T5LqibAWJR7kcwGvuzibNER7mtk1U47ibwGTuLOP8jXgZYqibsSp5b1eLvjLRp8/640?wx_fmt=png&from=appmsg)

攻击者投递的恶意压缩包

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoggyONWMGQblHQecVS6icajkBeGVCR3zIhhuIIgDJwyRmtGqagAApicvchVFbK6a6QiaWloVTOkgPNloKBOCzsyFrJIpzjKj1XaU/640?wx_fmt=png&from=appmsg)

.hta文件运行命令行

hta文件启动后先隐藏自身窗口，避免持续显示脚本界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sot9vsxrrj3T0zpW6H2Z1Tyzdqu4QYcfmnRLq6ibGTod3LNjLiaVYJ48KgLVHgia7uBgq1Dtv2PYvuIFPpUqwV9KhXDFq4GM2wTMQ/640?wx_fmt=png&from=appmsg)

hta隐藏窗口

hta文件会释放.zip扩展名伪装的加密数据文件，随后解密恢复PE内容，并在自定义文件名表中随机选取一项作为解密后PE文件的文件名，本次分析时生成文件为supplier.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqKJu3dbRfXAIZ4FQeHJw9xxSy3OFv3hOVHG3pHEOFeiaClmDDYx7cNrKaarYduTD8NLqFCxqmjonRn1iccP61YP5icnlyUJ1lJ4A/640?wx_fmt=png&from=appmsg)

生成解密恢复PE后的随机名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqIoPksEUseOQqJxJ9d7Hy1v6YEZv0UV4VPYPevKKvLiazSp8TnroLX8oj3roPQCIiaKicTnroxFceVQyynqlIEAKB34ntAOmIGLw/640?wx_fmt=png&from=appmsg)

.hta释放的文件

hta会释放bat文件，通过bat文件，运行supplier.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SraxqTkHJ4jMtV9KS7wprqtPlzugGnI0uQWYiaVhtm5PibsjEuUogdmxnReWYvibER8AwxYJu3xskthCBVELmvLdDCpprM63OunicE/640?wx_fmt=png&from=appmsg)

启动程序的bat文件

supplier.exe运行后会创建类似Windows Search组件的目录，并将自身复制到以下位置：

C:\ProgramData\Search\34f3ee81e944bc6b\avq.exe

复制过程中，supplier.exe生成随机数据并追加到avq.exe尾部，使不同副本的体积和散列发生变化。膨胀操作主要用于增加样本的hash随机性，对抗杀毒软件上传云端检测。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SqTGMMdwjVYpz5UDErBBfxhMlwM6Oiav1y1huaibVhl5M1UuBTrnfg6vtvEic8iaYISklXNicSGVoqLGmt4OmEE4ibLlynf8Xt7iaCC9c/640?wx_fmt=png&from=appmsg)

supplier.exe生成随机数据

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SqnMBhI5QWnBf36iaicWTXD0HJTLNg0onbQXBaBPb4ZuJDftIfN7VCluUoV1xEicnO1ibXq6XCHqDDIiaRxgLSic1RskqibSSkNmV9ycI/640?wx_fmt=png&from=appmsg)

supplier.exe填充数据到文件中

supplier.exe还会释放.pbk、.cmp和.cms配置文件到公共用户目录。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoP6yiaCNM5PxYFte0F2RamiaicjaQu6OnZMib8t3OgFqqOD0jwUVULrx4D72orqEOSqIPLT8muHXxicbWs66Mican4o26BdOf0oREZo/640?wx_fmt=png&from=appmsg)

释放的Connection Manager配置文件

其中，pbk配置将cmdial32.dll指定为自定义拨号组件；配套cms文件的Pre-Init Actions，文件功能是通过cmd.exe启动转移后的avq.exe。

```
[Pre-Init Actions]
0=C:\Windows\System32\cmd.exe, /c start "" "C:\ProgramData\Search\34f3ee81e944bc6b\avq.exe"
```

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SrJ0Vicb9ziaBWgQ9rDibdiaP2ibZPhzmXiaAs43a5scXWJf8ypA7RKl1hYXGX0JF06In5Py1lzz5Q0ggCLMcVzPTSP2mu1Ohr8tETIg/640?wx_fmt=png&from=appmsg)

Connection Manager配置及间接启动命令

supplier.exe使用WPTaskScheduler RPC创建临时计划任务通过以下命令启动系统自带的rasphone.exe：

```
rasphone.exe -f C:\Users\Public\DDC87699A36825C5.pbk -d "PoCEntry"
```

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SrMzJOMmibOGZB6kawI7MwIY09TDrn4Nr1beJmZxJicgQ9FDyWGZqnPdkYZzVASAWFVpR6DEDvicAwCnMaiaZD47iajVk39YqfES9x0/640?wx_fmt=png&from=appmsg)

创建临时计划任务

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SrXB7NumicHUsTXickuKf0fJoQmpGibpAwzAwFhhrf73KGSicr8q6ribRYhxThKpEqEkImibwvBlO2AGS4WQKkoqCd83dIDrTMKuPIWM/640?wx_fmt=png&from=appmsg)

supplier.exe的调用链

上述行为完成后，用户进程列表中会出现avq.exe进程。

avq.exe没有在导入表中直接暴露全部关键API，而是通过PEB遍历、名称解密和动态解析方式获取CreateMutexA等函数地址。avq.exe创建以下全局互斥体，避免相同路径对应的实例重复运行：

Global\M\_dd14849afcab7b94

avq.exe修改当前进程中amsi.dll!AmsiScanBuffer的函数开头，阻止amsi扫描，随后avq.exe会初始化clr，取得默认AppDomain，并把内嵌的Loader放入SAFEARRAY中，通过\_AppDomain.Load从内存加载。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpVib544x1vkiclWTyPibYqa5p1rEUAia3C3vmMdg9aog7cCaqDbqZHibEIez9yT5xovdNhUDkvx94iblcUY1TgXYbEUnERdwsRggbgE/640?wx_fmt=png&from=appmsg)

加载器修改AmsiScanBuffer返回结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sr0NTYic77Qo3Mib0tZicuRXzpsI9zUvgCicBNeDe7R461mADFarW6GZuFMPhVc16Jck4XiclkM6uc6QbJ6wicnumUdnepwicgEFr10OU/640?wx_fmt=png&from=appmsg)

avq.exe在内存中加载托管Loader

avq内嵌的Loader被加载运行后，Loader会在内存中读取内嵌资源PayloadSource.zip。其内容不是可直接打开的ZIP压缩包，PayloadSource.zip是经过TripleDES-CBC加密并由GZip压缩的载荷数据。

Loader会读取PayloadSource.zip、Base64解码TripleDES密钥和IV、TripleDES-CBC 解密并去除PKCS#7填充、跳过四字节长度字段GZip解压、Assembly.Load(byte[])、反射调用解密后程序的GClass0.smethod\_0函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SrbRGE9qru1Xzz7egj8E82LwQGk2QdHqxiauujF7gwY1ybicCibibxYicuHGPy22xzO2umSwHXOicEGnxmaSBEAPp3IMxzhyUMvWsmUc/640?wx_fmt=png&from=appmsg)

Loader解密并加载PureRAT

解密后的程序是76,800字节的.NET程序集，SHA-256为：

d882627c3a9ceb934a45f969c9416996337e36cbf7a07831f5e82d5c3ae4f855

程序集代码包含版本字符串4.4.1，其内嵌PKCS#12证书的主题和颁发者均为CN=PureRAT Agent。结合网络客户端结构、证书身份和功能实现，可以推断最终载荷为PureRAT 4.4.1。

PureRAT启动后创建Socket、NetworkStream和SslStream，使用内嵌证书建立TLS通信。本次运行中，传入Winsock的sockaddr\_in的远程地址为：

> 172.98.22.177:56002

PureRAT并借助protobuf-net库进行序列化和反序列化业务数据。连接建立后，PureRAT先收集主机及受害者信息并向控制端登记，随后接收protobuf消息，由命令分发函数调用对应功能模块。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoHudMW9yTqwL3B9mMBBSKLkf0Jb8T1K07ApbLh6SKEy7ibyuvlg8a0BWiaNkj23x4cc1XEF9qAtXicGg56GiambvFtzvhQNCAPkibA/640?wx_fmt=png&from=appmsg)

PureRAT控制端解密前配置

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SraNcpQuDuHIbAkANREww8A2VjcLSyBIz4AF6unsN8VH1kqwRUeHBkzibzZZCyhWhV6hBqLpN5TtypiakTbzrqJM6lqAEd0uvg3g/640?wx_fmt=png&from=appmsg)

PureRAT控制端解密后配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqQudicloER4pFpSbotPW30vZtsuGLP1ibeMdCLlrnAfOnRouWrnaRxs0PjsRXyibOX9zPWruBe99mmkvesWcQBQGDOicO39kK7hicc/640?wx_fmt=png&from=appmsg)

PureRAT控制端内嵌TLS证书

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Spoiaa2JssmhpLNSI3ic9fES3fMR7dWavv2Mr3PFXCOibGepmA5W5XzKu4ecUDrow4O4L56wnN3qYKQf4KulWOLo4JzqKY7pZZheQ/640?wx_fmt=png&from=appmsg)

PureRAT初始化TLS通信函数

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Srhr3z4Wmeqibdvn7yibmpLiakKNGY8j2hkaoEk08o1Q8XHbLqyrOocwruVicicPVpTWDgfRpz9Rbh9MMiauc8JvictibRqKcPvNGepuQE/640?wx_fmt=png&from=appmsg)

PureRAT交换数据函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SroPicSpOgLErZOTkiaB2VCHeqBicjpiaEH59iaynyNicdvXIk3bj1meHxLLd6oUe1NnWmT2zLFBiaoDXHVRE3TzPhiaPCjRkBSNAc22xo/640?wx_fmt=png&from=appmsg)

PureRAT命令分发函数

PureRAT中包含窃取Chromium系浏览器数据，并定位窃取加密货币钱包扩展及本地客户端数据的功能。其目标包括Chrome、Edge、Brave、QQBrowser、Vivaldi，以及MetaMask、TronLink、Coinbase Wallet、Trust Wallet、Phantom、Ronin 等扩展；同时还会寻找Atomic Wallet、Electrum、Exodus、Ledger Live、Telegram Desktop和Foxmail等应用数据。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SryARX682azYkb0JHrb2bzNPPoZy5lUQ7U2dqvsQoGUjNvswJToXpXzI6eC654dYdvIesibJ65XFrP64nzOgu0YrjiaxuKScJFGg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SpQRK5Hn8wxk0qibOfhL3khib0nei...