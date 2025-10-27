---
title: 新版Windows unity扫雷游戏去广告
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458573935&idx=1&sn=39fef18d2337580aead23c2ffe1f8e0c&chksm=b18dece586fa65f3c016ac6f4e2bfd578c7acf325a1f0e545c6b8c940673220405226917e363&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-09-16
fetch_date: 2025-10-06T18:22:40.985866
---

# 新版Windows unity扫雷游戏去广告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFrpoiatkeiaTGgSCGuLKF5evwrnDf2zv72libh5yELvu5MEznhA6sS9VRg/0?wx_fmt=jpeg)

# 新版Windows unity扫雷游戏去广告

orw

看雪学苑

1

**起因**

怀旧一下Windows 扫雷，结果发现界面大变样，变了好看了许多，但是广告也特别扎眼睛，所以就想干掉广告还世界一个清静。

目的：微软商店扫雷去广告

2

**经过**

首先是想通过子窗口，字符串找到业务代码，但是均失败了，不得已要对程序深入分析，先通过导入表下断点找到业务代码的范围，最终发现业务代码是使用il2cpp 进行解释执行，接下来就需要研究il2cpp,之后得知unity 把c# 代码使用il2cpp继续二次编译，通过对GameAssembly.dll和global-metadata.data的反编译可以得到c#的类，方法和字符串信息，然后对应的代码地址，根据类名函数名找到相关业务代码进行patch，最终成功去掉广告。

源程序：微软商店下载第一个

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFvHR0ibSpTdEy5miciaDcBCX43MasTJbAMKpKMATOEWfNHEMABFPRwLkHQ/640?wx_fmt=jpeg&from=appmsg)

进入游戏选择任意模式可以发先下方有一个很大的广告窗口。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFC0icvX2l8L5eT3W2lz01YMQoIoYicq9PZpURicmScBDFy4jM0NZuZic5cg/640?wx_fmt=jpeg&from=appmsg)

程序目录：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFZ8Hbtyq1cgxAw7NKSS1mzSPJ4T9gqMoloibLkzIb8WWdIwYv343ucXg/640?wx_fmt=jpeg&from=appmsg)

传统思路：
（1）先用spy++ 找到子窗口，处理 creatwindows。

spy++ 查看一下窗口，没有子窗口，此路不通。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFYoNXFicbPcAKM6MSYibB1rbU607VHMqbiaSUZyNIcRoqAEpg8pW8GbcTw/640?wx_fmt=jpeg&from=appmsg)

（2）查找字符串，看看那里使用了相关字符串，patch 相关代码。

x64dbg 附加也找不到字符串。此路不通。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFAKhD3XMXvF3Jjw2HIqBn9iaywhP7iapf5D6X2XlH15GHsrib9NoZFkdzA/640?wx_fmt=jpeg&from=appmsg)

（3）上调试器对导入表下断点分析，根据导入表提示寻找业务逻辑在那里。

dll模块的导入表就是该模快用到的其他模块的功能，所以对导入表下断点可以帮我们尽快找到业务逻辑代码，减少额外信息的干扰。

接下来就是导入表下断点，从而进一步找到功能逻辑代码在哪，首先把系统dll 排除掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFjyuLqvqunVdeLicecLRD4fkrgfTchjejbvs0AYPP3l95nCR3iaz4MicAA/640?wx_fmt=jpeg&from=appmsg)

经过调试发现程序的逻辑在GameAssembly.dll 中，观察右边的符号名称，il2cpp看起来像个解释器，对高级代码进行解释执行，比如获取类，获取方法等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFHbchoBt1NvoZnibzrmicoANvxtCEyGJHwrIlqKvy26hoYiaZicCUssDpvA/640?wx_fmt=png&from=appmsg)

继续调试发现，程序逻辑确实是不断的获取类的信息然后在执行更加验证了我的想法。以下跳转的地址就是获取类的信息然后去执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFSK42WRibvqIczzEtDOvtBorNeICZS19Ey53gYtTvia6iazgAqZhtFlg2w/640?wx_fmt=png&from=appmsg)

所以接下来就需要研究一下il2cpp的原理，有没有办法反编译为高级代码。毕竟直接分析工作量太大了。

深入分析：
（1）分析il2cpp 作用，并找到global-metadata.data。

通过一些特征字符串并查阅资料该游戏是unity开发，使用il2cpp 打包
il2cpp是一种将其他的高级语言转化为标准c++ 代码的技术。

参考https://docs.unity.cn/cn/2019.4/Manual/IL2CPP-HowItWorks.html

IL2CPP 的工作原理：

使用 IL2CPP 开始构建时，Unity 会自动执行以下步骤：
将 Unity Scripting API 代码编译为常规 .NET DLL（托管程序集）。
应用托管字节码剥离。此步骤可显著减小构建的游戏大小。
将所有托管程序集转换为标准 C++ 代码。
使用本机平台编译器编译生成的 C++ 代码和 IL2CPP 的运行时部分。
将代码链接到可执行文件或 DLL，具体取决于目标平台。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxF9vBCaQZz49EWZXjoRnrF4dZ26NlruwxwpqBKzyibhmorSqTJfF97KQw/640?wx_fmt=jpeg&from=appmsg)

接下来就是需要找到 被打包的c#代码的信息在哪，c# java 这种解释执行的语言执行时需要类的信息， 不管用什么样技术手段这里东西一定存在某个地方。

从unity 官网可以看到 存储文件是global-metadata.data。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxF48mrMYl4XoTteXGP3fkJORJ0Nr2NZgw8HGVw6daZ1GwKnepF7NPy3w/640?wx_fmt=jpeg&from=appmsg)

其中global-metadata.data 中有C#中的方法名、属性名、类名，字符串等。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFe2mbqTt12po63FLBzxHC9bHX4EWEwIxueXldGHKS1IKzB0nzkMicMkA/640?wx_fmt=jpeg&from=appmsg)

（2）反编译GameAssembly.dll和global-metadata.data

接下来看看有没办法反编译一下，找到工具，可以通过Il2CppDumper dump 。https://github.com/Perfare/Il2CppDumper

使用Il2CppDumper 弹出两个文件选择框 先选择GameAssembly.dll 在选择global-metadata.data

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFic8tqoShctC80bIicVn0mW4pZQAdJRNcEDwk0aicnmQbFNUdmLkUnxIPg/640?wx_fmt=jpeg&from=appmsg)

然后当前文件夹出现DummyDll目录

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFiaFsJCB5bAw5ZdevwabuAWiaExN4mGmHsmRLqc83lnaDPqxaYRkcGLdg/640?wx_fmt=jpeg&from=appmsg)

其中Assemble-CSharp.dll 就是c#写的业务逻辑。

（3）使用反编译工具查看Assembly-CSharp.dll，这里用dnspy，下面看c#的业务逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFjzNBv2zTZfDLRpKjk3zn4icupgiaeicuo7WybKuP7IFxpwAZeASsWASzg/640?wx_fmt=jpeg&from=appmsg)

发现这里没有代码，观察右边有RVA 和VA 这里其实对应的函数在GameAssembly.dll

Ida 打开GameAssembly.dll ，0x1807C1FD0对应的汇编代码

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFP5nONt8ia2qrX0UWa6WVwuxdn3ptTicniakp7Vsa9flxw9ibVFibK0f5umA/640?wx_fmt=jpeg&from=appmsg)

（4）接下来根据这些类和函数名大推测业务逻辑最终找到广告的类：

这里看到程序右下有个红色的按钮，猜测名字包含 buttonclose 然后在dnspy里搜索。

找到这个可疑的类：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFSH3QTvVEzo8nrjujyHQLVPodVX0Yg9apDsstlLUvjrYQ0tureO9zTA/640?wx_fmt=jpeg&from=appmsg)

X64dbg中先对onCloseAdButtonClick下断点，然后点击 那个红× 关闭按钮，发现断点来了说明找对地方了， 接下来就是对把初始化函数干掉，这样这个button 就不能正常创建了。

最后做验证使用x64dbg patch 0x1808FDC50 ,广告消失了，干净的窗口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFMe5LvArlqZ7eE4lmYzs1gmYhibB3PsJuI6WG8YEcH0JXou8VpxEoE3w/640?wx_fmt=png&from=appmsg)

3

**总结**

对于使用il2cpp 打包的程序，先找到对应的类的信息字符串等数据，使用Il2CppDumper 弹出两个文件选择框 先选择GameAssembly.dll 在选择global-metadata.data，得到Assembly-CSharp.dll c#相关类和函数等信息。根据反编译分析业务逻辑，根据函数的rva 算出实际代码地址去下断点调试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFOy7NaBZR5eicC31uLD1XN9icXGr0wKPm2lrybPoaoKxz9JconxToTOQg/640?wx_fmt=png&from=appmsg)

看雪ID：orw

*https://bbs.kanxue.com/homepage-960204.htm*

\*本文为看雪论坛优秀文章，由 orw 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HiaPMdDo2UWw2QkoicbgP3sHMTQKZdohMejPPs45YLJ5ib6s7ibqtoRic2RM0RBNeLrOsKJibTAwmibCDkw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572548&idx=4&sn=b5fb10e6d4d18358d2b29359c3e59f49&chksm=b18de78e86fa6e98915c04728a77f15dc4521ce2f96d456af072481df554f61253c93499d74b&scene=21#wechat_redirect)

# 往期推荐

1、[CVE-2023-0461复现笔记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572548&idx=2&sn=728093f73ed936ec6d031493a4f61eeb&chksm=b18de78e86fa6e987d9afde055f469e2db67a3fd5e56fdbd83c41c5758bdf2516297c6283b2c&scene=21#wechat_redirect)

2、[混淆 Pass 分析 - Flattening](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572456&idx=3&sn=bb7abeeccca94754648d7f73d201d482&chksm=b18de62286fa6f34d96056166bdec3ff52be2c90928fb7582a6dbcb56a2e60c90794b946bfbf&scene=21#wechat_redirect)

3、[URLDNS反序列化利用链](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572382&idx=3&sn=358d10426f05a9dfc5e1f4b8cfb68ff8&chksm=b18de6d486fa6fc22c9e0a7deeefa7fcac0129a7d51b6f69d8cd9aef692c12e0360243e700a7&scene=21#wechat_redirect)

4、[CVE-2023-2008复现笔记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572285&idx=2&sn=0222e2ed9589877a875eb5cb86056ac2&chksm=b18de57786fa6c61103d2f5c157fbdb516461dcba4b82b88daea0ed03e0c2bfbfefa1fb7d8ad&scene=21#wechat_redirect)

5、[逆向进入内核时代之APatch源码学习](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572214&idx=1&sn=8d99655757749015c672e096913c55bf&chksm=b18de53c86fa6c2a7dfbaec22faa9e4a62eb4734fd00d307ff133b0ebfd20fe6007f45128905&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFbXGJjuJGtG6jAn2kRA69YSMLLR2AEzN3nsYd0TDxmZNLVSmHHj1Gkg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFJYHrpNzheTEXib85SebcaahXuSd27XuOSapQbZ2TAxMnFbicZnGYQwsQ/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFJYHrpNzheTEXib85SebcaahXuSd27XuOSapQbZ2TAxMnFbicZnGYQwsQ/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxFJYHrpNzheTEXib85SebcaahXuSd27XuOSapQbZ2TAxMnFbicZnGYQwsQ/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EBEutOkrA9Lfl3YbUbWFxF3lcMaBr5Y5NLInxxBgibVfNh2esL1cfWmia5eA6pZXxI0BK33YyvibibyA/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt...