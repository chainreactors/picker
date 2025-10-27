---
title: Cdp协议深度应用Web渗透加解密
url: https://forum.butian.net/share/4315
source: 奇安信攻防社区
date: 2025-05-20
fetch_date: 2025-10-06T22:23:43.819038
---

# Cdp协议深度应用Web渗透加解密

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Cdp协议深度应用Web渗透加解密

* [渗透测试](https://forum.butian.net/topic/47)

Cdp协议深度应用与探索

渗透测试与加解密
========
作为一个苦逼的安服仔，在不断接收全国各地的奇奇怪怪的安服项目的洗礼后，这些奇奇怪怪项目一开始只是简单的web加解密签名，再到小程序加解密，最后是APP的加解密。有些时候会真的很疑问，这些技术，真的和渗透相关吗？再到后来我了解到，有一类工作叫反爬，也就是说那些客户的项目，其实并非是防止我们测试，而且将我们的源头，请求(爬虫)给防御住了，而网络安全测试的基本就是请求，而加解密就是端防类的一种。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-0953e4b873eb18562cd56fa335ba9048296221a1.png)
某厂反爬工程师要求
成长历程
====
刚开始接触是web，也仅会处理web。而web的核心是html+js。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e7adb1c6de9d4e359d6ecbaa0f8b2dcee24ccb36.png)
刚开始学习的时候就只会进行搜索。什么encrypt什么包特殊头，json.stringify等等。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-78dd85b84d6a331a0bf13598d01ed2e16cc778f1.png)
打上断点一顿分析，结合mitmproxy以及burp的替换功能，也勉强能够解决大部分加密站点。
后来自己还对自己一次对抗分析过混淆的不知道哪个厂商的产品而高兴。因此还写过文章<https://www.moonsec.com/8899.html>。
感兴趣的师傅可以看看。在做了特别特别多的类似加解密的项目，发现每一次都要去分析，也需要花大量的时间去编写逆向脚本，大大小小项目有几十了吧。总结来说：有好有坏，有些项目也因此挖到一些漏洞，但有些项目时间花了更多的时间，也无产出。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-0c873f2e4ceadce9ab951846e3392b7bc5305d67.png)
后来逐渐发现部分难以测试的也逐一解决，接下来我将经验分享。
首先是2023年10.23的这篇文章，是第一次将小程序的js调试带入我的渗透日常。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-4d1d44f33f0eb74e92434b532933aae02fd39561.png)
这个项目是基于Wechat-open-devtools来分析的，也是我第一次感受到devtools的强大。目前测试小程序时基本上都能用得到这个项目。
<https://github.com/JaveleyQAQ/WeChatOpenDevTools-Python>
使用前先下载对应的微信版本，然后每次启动微信要提前退出将WeChatAppEx.exe的RadiumWMPF目录给删除。然后使用python main.py -all即可。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d4b39a47db14ac067317c3761d470190d22c6a3b.png)
于是我们就得到了一个devtools。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-fde2e808840c439f988c1f185d79ebaaee730bb8.png)
但是这个devtools和谷歌的devtools并不完全相同。首先就是源js文件，特别难分析，甚至于找不到加密的点。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-90a0657ba470e007e5463e7dce173380021bafdd.png)
在这种情况下，学会了从堆栈分析，从请求出发，去溯源到对应js文件点。这种方式不仅对一些混淆的js，甚至于一些高端产品如瑞数等分析找到入手点都非常不错，是最佳的分析点入手点，唯一快速定位加解密的方式。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-bcdfa373a1673b2a52839a9c25925185f96be1e7.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e2ff17f7962be60eb3bcd8c9b77ceb4451fc467c.png)
当然仅分析当然不够，针对web的html+js大家会使用到burp的替换，将关键的前端加密点替换成明文点然后再自行进行加密等。当然小程序我也想这样去应用，可是小程序的js运行在微信的内部的。我们无法进行修改那要如何做呢？
因为无法修改，我们就只能做做简单的对称加密的破解，并不能做到非对称加密的全自动测试。这个问题确实困惑了我很久。当然有几种思路，第一我们找到微信加载JS的入口去改掉微信加载JS流程。第二就是本次会分享给大家的条件断点。我们右键对断点进行编辑时，是可以通过断点进行编辑js调试的。也就是对运行时的js进行注入脚本。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-a79265963a8288a4482d3fb4e319ee2f2596f058.png)
什么是条件断点呢？
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c6420fef657ccdb11ad391d4d216b83602ad7a07.png)
条件断点并非只是单纯的进行了false与true的判断。而是对执行一个表达式，就比如可以执行js代码，那我们就可以对一些关键数据点进行替换进行传输，比如替换明文数据，当然除此之外还远不止这点功能，比如调试瑞数时的nerver debugger就是使用的条件断点，表达式为false。那到这儿就不得不感叹CDP协议对于JS调试的强大。
后续安服仔又涉及到APP的测试，抛开root，脱dex，过厂商来讲。核心本质对抗加解密技术会用到一个叫做rpc的技术。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e4fbf67e65a8057879a8924ea49e8fc868c07c29.png)
介绍一个经典注入脚本案列，APP支付宝框架mPaas，就是通过rpc交换的数据。
<https://github.com/F6JO/mPaas-frida-hook/blob/main/frida.js>
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-eae05aa4f2d4191b7f2bc81c552da93f3f0af0b9.png)
简单来说，就是将加密前的数据转发至中转服务器，修改后返回源程序。颇有点中间人代理的那个意思。这个技术非常常用，优点就是非常便捷，几乎通用，任意js的程序也可以复用类似的技术当然包括小程序。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d0e1d92d89eb8dc98f4e8914575e41006b38bf94.png)
就比如我们注册一个请求函数，然后在任意断点使用这个函数，即可将数据进行外带转发进行修改测试。当然为了应用这个技术，学习到了js发送请求的常用框架，以及很重要的同步以及异步的用法。但是最终这个技术却遭到了放弃，实用性较差，无法重放，仅可简单调试一些简单的web。
再后续由于Wechat-open-devtools的不断迭代，微信官方终于在新版本修复了那个打开devtools的bug。Wechat-open-devtools终于停止在了某一个版本。秉着为了搞定小程序的想法，避免以后无法进行小程序的端防对抗，我开始了对微信逆向分析，其中包含几个版本。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-5e436e942edbba60ca6cc04b0c6a85d208416f0f.png)
发现所有的小程序都是基于V8进行操作的，什么是V8呢?大概可以理解为运行js的容器，谷歌浏览器就是基于V8进行做的，前几年很火的浏览器漏洞，底层就是v8存在部分问题。而微信的的v8运行小程序的容器是将v8-inspector给阉割了的，也就是说除非你是开发者去使用微信开发者工具去调微信小程序（我初步猜测有很多认证机制），才能使用devtools。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-152e421a1fe6296c439fca02ca61c12676da9976.png)
于是我的目光转向v8的hook。基于这个项目
<https://github.com/haseeburrehmanfaheem/Frida-Scripts-Android/>
我确实也完成了在微信的v8环境下进行常见的命令注入，以及Cpuprofile模块，但这些并不能满足我的需要。于是后续我将目光放在了，自行注入V8-inspector。也就是这篇文章的构造，<https://ivanfan.site/2022/07/16/v8/v8-inspector%20%E8%B0%83%E8%AF%95/>
在自己的小程序注入一个完整devtools，最后失败了，太复杂了。虽然失败，但了解到了真正的devtools的使用方式。devtools都是通过cdp协议去调的。关键的消息发送函数是dispatchProtocolMessage。那发送的数据是什么呢？就是以这种格式的数据传输的操作。比如图中的evaluateOnCallFrame，就是完成加解密关键函数，所实现就是在某个断点帧执行表达式。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-3a17226f543aae0b75fb93c6265aaa573a346b62.png)
那么了解到这个，我这里遂想到是否可以应用于web的加解密呢？web浏览器--remote-debugging-port=9222可以直接调试CDP协议。web老式加解密方法，分析包括别人分享的RPC我都觉得不太好用，没有做到一个真正的便捷。需要分析理解成本都太高。于是对CDP协议进行分析。最终完成高效脚本如下：
1.首先启用cdp.js对cdp监听。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-37b4e21ec49f5d2310d5e934b8b2571b0ae113b3.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b4b5e96b6ad6691466d37b569abd8dd505bae80c.png)
2.然后使用python去启动调试的web进行连接cdp。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-488c800ad57ed7534bc143af70b74846eed50ef2.png)
3.由于我提前找好了加密位置，打开f12,定好断点运行到断点。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ce1171fa3c74ebc1be1d7603b32771f7df2a5e08.png)
4.调用cdp注册的接口。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b0339acb5223bbf787939b50c68b551b19a7e87f.png)
5.调用加密接口。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-cd9266bf3465372f883c6d217453c2636f7c16f5.png)
6.调用解密接口。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-f74c5ea008f392c88480de9bf22ce04040b34e2d.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-16c3e5e2765a2a356de4d692ccb145594d86cf5d.png)
7.成功注册完加解密接口，剩下的只需要将数据填充至中间代理即可。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-71a3351644b4413a1a482c632246bd89dbc90a9e.png)
8.整体流程非常干净清爽，如果你的断点位置找的非常快，那意味着完成这个加解密将会10分钟不到即可完成，如果配合上成熟的AI去结合编写中间代理脚本，将会实现5分钟不到实现加解密。不需要关注加密方式，不需要关注编码，原汁原味的JS调用，仅填充数据即可实现加解密。
我将以上demo代码放置我的github了，大家可以自行下载获取使用，以及根据个人习惯进行优化使用。
[https://github.com/Nstkm001/CDP\\_test](https://github.com/Nstkm001/CDP\_test)
关于cdp的应用，由于之前碰见过有瑞数的项目，此前一直想要获取一套完美的通用的方案。在过去大家很多人都是死磕补环境，参考如下文。
[https://blog.csdn.net/qq\\_40759445/article/details/136503498](https://blog.csdn.net/qq\_40759445/article/details/136503498)
简单来说，就是利用后端语言来处理瑞数本身的js，将加载过程模拟成浏览器一致，俗称补环境。然后对瑞数本身的js进行调试获取cookie。那么我们是否可以通过cdp直接使用浏览器环境来获取到相关cookie呢，答案当然也是可以的，方案也非常简单。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-41e0e485afc3f7753bfbb4ae5e7ae8c6e638db47.png)
这次分享就不包含瑞数处理了，再到后续关于安卓微信的js修改也相继完成，以此筹备小程序无法测试等问题。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1f0f9e6a7fd3c280a8dad5dd9c3c8cd422e63b63.png)

* 发表于 2025-05-19 09:15:58
* 阅读 ( 2806 )
* 分类：[WEB安全](https://forum.butian.net/community/...