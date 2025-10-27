---
title: [2024]用EDR剖析流行黑产组织对抗安全软件的多重手段
url: https://key08.com/index.php/2024/05/02/1888.html
source: 白帽Wiki - 一个简单的wiki
date: 2024-05-03
fetch_date: 2025-10-06T17:15:22.091553
---

# [2024]用EDR剖析流行黑产组织对抗安全软件的多重手段

[![](https://key08.com/avatar_pack.gif)](https://key08.com/)

# 白帽Wiki

从2012年开始专注高级网络安全技术研究

查你所想

![](https://key08.com/avatar_pack.gif)

### 一只鸭子

* [首页](https://key08.com/)
* [板块活动记录](https://key08.com/index.php/1596.html "板块活动记录")
* [IDA Internal](https://key08.com/index.php/2365.html "IDA Internal")
* [EDR开发相关](https://key08.com/index.php/project_ayy_waf.html "EDR开发相关")
* [威胁追踪](https://key08.com/index.php/cve_detect.html "威胁追踪")
* [Hypervisor](https://key08.com/index.php/hypervisor_code.html "Hypervisor")
* [机器学习&神经网络](https://key08.com/index.php/keras.html "机器学习&神经网络")
* [EFI驱动编写](https://key08.com/index.php/EFI_Driver_Code.html "EFI驱动编写")
* [关于&联系方式](https://key08.com/index.php/215273185.html "关于&联系方式")

×

# [白帽Wiki - 一个简单的wiki](https://key08.com/)

## [[2024]用EDR剖析流行黑产组织对抗安全软件的多重手段](https://key08.com/index.php/2024/05/02/1888.html)

[huoji](https://key08.com/index.php/author/1/)
 [EDR](https://key08.com/index.php/tag/EDR/),[银狐](https://key08.com/index.php/tag/%E9%93%B6%E7%8B%90/)
 2024-05-02
 2922 次浏览
 0 次点赞

### 文章总结
本文介绍了在日常巡查中发现的一个虚假WPS官网，该网站被用来投放含有gh0st远控功能的恶意软件。这一行为被认定为“银狐”黑产组织所为。与以往不同的是，这个样本采用了多种安全软件对抗技术，成功绕过了大多数基于HIPS的安全软件的防御机制。
技术分析部分指出，样本对杀毒软件进行了免杀处理，目前只有三个杀毒软件能够检测到其为恶意软件。样本使用了一种更高级的虚假数字签名技术，这种签名对文件本身是可信的，但对签名链不可信，因此能够规避一些基于文件签名信任的杀毒引擎。
在持久化方面，样本会在启动后立即通过白加黑的方法加载恶意DLL，并创建服务等待下次重启。防御规避方面，样本会在用户重启电脑时以服务方式启动，并使用DLL侧加载方式劫持白名单文件，最终通过镜像篡改的方式启动注入器，给系统进程注入恶意代码，并连接C2服务器进行远控操作。
文章还提到了使用EDR进行分析的便利性，EDR能够标注恶意行为，从而无需对代码进行分析，只需观察行为即可。
最后，文章提供了相关的IOC列表，以及原文章的链接，供进一步的研究和分析。
### 简介
在日常巡查中发现了一个虚假的wps官网在投放gh0st远控,经过行为判定,是”银狐” 类黑产组织所为.但不一样的是,样本运用了多种安全软件对抗技术,从而绕过大部分国内外的基于HIPS的安全软件的防御机制.
![](https://key08.com/usr/uploads/2024/05/742723484.png)
\*\*要对他进行分析,静态各种混淆壳十分的麻烦,所以使用EDR,不需要对代码分析,只需要看行为,EDR还把行为标注好了,非常的舒服\*\*
整体攻击流程如下:
![](https://key08.com/usr/uploads/2024/05/1177939857.png)
### 技术分析
样本静态对杀毒软件做了免杀处理,截至发文前在VT上只有三个杀毒软件报毒:
![](https://key08.com/usr/uploads/2024/05/3590642447.png)
样本使用了”更高级”一点的虚假数字签名,传统的数字签名伪造技术是复制其他程序的数字签名到本程序,这种类型的签名对”文件本身”来说是不可信的,即出现”数字签名校验错误”.
但此样本是伪造了一个对文件可信但是对签名链不可信的签名,因此能规避一些基于文件签名信任的杀毒引擎:
![](https://key08.com/usr/uploads/2024/05/3591441133.png)
### 持久化
样本在启动后,会第一时间通过白加黑的方法,加载黑DLL:
```cpp
C:\Users\%username%\Desktop\Kveed9b1eUQf\yybob\HipsdiaMain.dll
C:\Users\%username%\Desktop\Kveed9b1eUQf\yybob\TDPINFO.dll
```
![](https://key08.com/usr/uploads/2024/05/3142201771.png)
这两个DLL被加载后会第一时间创建服务ZBJCOptimization:
![](https://key08.com/usr/uploads/2024/05/4058019230.png)
但并不会直接启动服务,而是等待下次重启.
### 防御规避
在用户下次重启电脑启动时,样本以服务方式跟随开机启动,并且使用DLL侧加载的方式劫持多个国内流行的文件的白文件实现链路全白的防御规避行为:
![](https://key08.com/usr/uploads/2024/05/1432685890.png)
最终使用镜像篡改的方式启动注入器并且给svchost.exe与SecurityHealthHostn.exe注入恶意代码执行:
![](https://key08.com/usr/uploads/2024/05/606541326.png)
最终由被注入了恶意代码的svchost.exe与SecurityHealthHostn.exe连接C2,进行后续远控操作:
![](https://key08.com/usr/uploads/2024/05/621745454.png)
### 用EDR分析
![](https://key08.com/usr/uploads/2024/05/4059419782.png)
![](https://key08.com/usr/uploads/2024/05/562705877.png)
### 原文章
https://mp.weixin.qq.com/s/zcr5B\_LLXp5c5D9GhTefdg
### ioc列表
```cpp
E60D144B090D4D0E504DF4B11939EC7FDBDADB58
143.92.34.213
```

![](https://key08.com/usr/themes/GreenGrapes/img/creativecommons-cc.png)

本文由 [huoji](https://key08.com/index.php/author/1/) 创作，采用 [知识共享署名 3.0](http://creativecommons.org/licenses/by/3.0/cn)，可自由转载、引用，但需署名作者且注明文章出处。

 点赞 0

* 上一篇: [[2024]复现Storm-0978的"EDR的梦魇"踩的坑](https://key08.com/index.php/2024/04/28/1874.html "[2024]复现Storm-0978的\"EDR的梦魇\"踩的坑")
* 下一篇: [[2024]制作任意签名者的数字签名证书](https://key08.com/index.php/2024/05/08/1897.html "[2024]制作任意签名者的数字签名证书")

2 条评论

1. ![nullptr](https://dn-qiniu-avatar.qbox.me/avatar/c4acb2997893a14fbb0a8722dde73da7?s=32&r=G&d=)

   nullptr

   这个签名伪造是什么做的呢

   May 6th, 2024 at 11:36 am
   [回复](https://key08.com/index.php/2024/05/02/1888.html/comment-page-1?replyTo=119#respond-post-1888)

   1. ![huoji](https://dn-qiniu-avatar.qbox.me/avatar/f862b8ed035d5544a04ca39e7c8bc412?s=32&r=G&d=)

      [huoji](https://www.wghostk.com)

      自己创建的证书

      May 6th, 2024 at 07:32 pm
      [回复](https://key08.com/index.php/2024/05/02/1888.html/comment-page-1?replyTo=120#respond-post-1888)

[取消回复](https://key08.com/index.php/2024/05/02/1888.html#respond-post-1888)

添加新评论

提交评论

![icon_mrgreen.png](https://key08.com/usr/plugins/Smilies/tieba/icon_mrgreen.png)![icon_neutral.png](https://key08.com/usr/plugins/Smilies/tieba/icon_neutral.png)![icon_twisted.png](https://key08.com/usr/plugins/Smilies/tieba/icon_twisted.png)![icon_arrow.png](https://key08.com/usr/plugins/Smilies/tieba/icon_arrow.png)![icon_eek.png](https://key08.com/usr/plugins/Smilies/tieba/icon_eek.png)![icon_smile.png](https://key08.com/usr/plugins/Smilies/tieba/icon_smile.png)![icon_confused.png](https://key08.com/usr/plugins/Smilies/tieba/icon_confused.png)![icon_cool.png](https://key08.com/usr/plugins/Smilies/tieba/icon_cool.png)![icon_evil.png](https://key08.com/usr/plugins/Smilies/tieba/icon_evil.png)![icon_biggrin.png](https://key08.com/usr/plugins/Smilies/tieba/icon_biggrin.png)![icon_idea.png](https://key08.com/usr/plugins/Smilies/tieba/icon_idea.png)![icon_redface.png](https://key08.com/usr/plugins/Smilies/tieba/icon_redface.png)![icon_razz.png](https://key08.com/usr/plugins/Smilies/tieba/icon_razz.png)![icon_rolleyes.png](https://key08.com/usr/plugins/Smilies/tieba/icon_rolleyes.png)![icon_wink.png](https://key08.com/usr/plugins/Smilies/tieba/icon_wink.png)![icon_cry.png](https://key08.com/usr/plugins/Smilies/tieba/icon_cry.png)![icon_surprised.png](https://key08.com/usr/plugins/Smilies/tieba/icon_surprised.png)![icon_lol.png](https://key08.com/usr/plugins/Smilies/tieba/icon_lol.png)![icon_mad.png](https://key08.com/usr/plugins/Smilies/tieba/icon_mad.png)![icon_sad.png](https://key08.com/usr/plugins/Smilies/tieba/icon_sad.png)![icon_exclaim.png](https://key08.com/usr/plugins/Smilies/tieba/icon_exclaim.png)![icon_question.png](https://key08.com/usr/plugins/Smilies/tieba/icon_question.png)

![选择表情](https://key08.com/usr/plugins/Smilies/tieba/icon_smile.png)

[![](https://img.buymeacoffee.com/button-api/?text=Trust Feature For Human Duck&emoji=&slug=huoji&button_colour=16a085&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00)](https://www.buymeacoffee.com/huoji)

* [最新Wiki](#sidebar-new)
* [最新评论](#sidebar-comment)
* [随机Wiki](#sidebar-rand)

* [[2025]中外AI大战!让AI们通过MCP玩帝国时代2](https://key08.com/index.php/2025/10/04/2816.html)
* [[2025]"ucpd.sys后门事件"详细分析技术报告-他是后门.....吗?](https://key08.com/index.php/2025/09/18/2815.html)
* [[2025]阻止漏洞驱动利用(byovd)技术致盲安全软件](https://key08.com/index.php/2025/09/15/2785.html)
* [[2025]深入研究R3通过网络(WFP架构)致盲EDR的技术原理与解决方案](https://key08.com/index.php/2025/08/31/2761.html)
* [[2025]从0制作IDA的F5代码还原功能(hex-rays插件) 上](https://key08.com/index.php/2025/08/12/2731.html)
* [[2025]VMP源码学习——变异分析](https://key08.com/index.php/2025/07/31/2729.html)
* [[2025]SleepDuck-通用堆栈欺骗检测POC,检测SleepMask](https://key08.com/index.php/2025/07/13/2716.html)
* [[2025]聊一下企业内网中办公网终端的EDR安全运营](https://key08.com/index.php/2025/07/06/2697.html)
* [[2025]Windows的内存防护机制](https://key08.com/index.php/2025/06/23/2688.html)
* [[2025]windbg ttd restore dotnet jit protection exploration](https://key08.com/index.php/2025/06/18/2683.html)
* [[2025]PE代码执行虚拟机详解&原理&源码](https://key08.com/index.php/2025/06/16/2663.html)
* [[2025] Introduction to IDA's Internal Principles (Part 4): function parameter number calc](https://key08.com/index.php/2025/05/18/2560.html)
* [此内容被密码保护](https://key08.com/index.php/2025/05/14/2549.html)
* [此内容被密码保护](https://key08.com/index.php/2025/05/13/2545.html)
* [此内容被密码保护](https://key08.com/index.php/2025/05/09/2541.html)

* 安全小白：[”标准的导出表hook:“打错字了师傅](https://key08.com/index.php/2025/09/15/2785.html/comment-page-1#comment-213)
* 电脑维修：[学到了](https://key08.com/index.php/2021/11/15/1394.html/comment-page-1#comment-212)
* 1：[内容被隐藏](https://key08.com/index.php/2025/05/06/2507.html/comment-page-1#comment-211)
* anon：[鸭总操我](https://key08.com/index.php/2025/04/15/2424.html/comment-page-1#comment-210)
* huojifans：[从加载hid.dll开始后面就是St...