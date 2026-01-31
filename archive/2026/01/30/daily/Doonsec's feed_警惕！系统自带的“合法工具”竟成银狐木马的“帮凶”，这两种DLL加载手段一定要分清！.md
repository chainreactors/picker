---
title: 警惕！系统自带的“合法工具”竟成银狐木马的“帮凶”，这两种DLL加载手段一定要分清！
url: https://mp.weixin.qq.com/s/aTJfmmoWbdvFhOKdFOZdTg
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:01:43.510809
---

# 警惕！系统自带的“合法工具”竟成银狐木马的“帮凶”，这两种DLL加载手段一定要分清！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rSuZI9Hg5lfRZmS4Ql2dQAkDHQvfWQEfUu5AGYBnb0kJ7O1AEATKD1yMkOibl5xh59J6gnWJasVibZtIv5gXHFaQ/0?wx_fmt=jpeg)

# 警惕！系统自带的“合法工具”竟成银狐木马的“帮凶”，这两种DLL加载手段一定要分清！

埃里克之旅
埃里克之旅

SOC安全分析之旅

![]()

在小说阅读器中沉浸阅读

最近不少企业和个人用户反馈遭遇了“银狐木马”（SwimSnake）的攻击，中招的用户里，有人是下载了伪装的百度网盘安装包，有人是点了搜索引擎里排名靠前的“假软件站”链接——而这背后，银狐木马之所以能躲过不少安全软件的检测，靠的正是对Windows系统两个“老熟人”的恶意滥用：RunDll32.exe和Regsvr32.exe。

今天咱们就掰开揉碎了说，这两个本该帮系统干活的“合法进程”，到底是怎么被黑客改成加载恶意DLL的“凶器”，再结合银狐木马的真实攻击案例，教大家怎么识别这类隐蔽威胁。

先搞懂：RunDll32和Regsvr32，本来是干啥的？

可能不少朋友在任务管理器里见过这两个进程，但很少深究它们的用途——其实它们都是Windows自带的“系统工具”，设计初衷完全是为了方便用户和程序调用功能，本身半点恶意没有。

先说说RunDll32.exe：它的核心作用是“调用DLL里的具体功能”。你可以把DLL理解成一个“功能插件包”，里面装着各种现成的代码模块，而RunDll32就是“启动器”，能指定调用这个插件包里的某一个功能。比如系统里有些配置工具，就是通过RunDll32调用相关DLL来实现设置的，正常用法得带明明白白的参数，像这样：rundll32.exe shell32.dll,Control\_RunDLL——意思就是“用RunDll32调用shell32.dll里的Control\_RunDLL函数，打开控制面板”，每一步都清晰可见。

再看Regsvr32.exe：它的定位是“给系统注册/注销COM组件”。简单说，有些DLL需要让系统“认识”并记录在注册表后，其他程序才能正常调用它（比如一些办公软件的插件），Regsvr32就是干这个“登记”活儿的。正常用的时候，要么是regsvr32.exe xxx.dll（注册），要么是regsvr32.exe /u xxx.dll（注销），而且它会自动调用DLL里的两个特定函数：DllRegisterServer（注册用）和DllUnregisterServer（注销用），相当于按固定流程跟系统“报备”。

这俩工具本来是系统的“得力助手”，但架不住黑客会“钻空子”——既然它们是系统自带、有“合法身份”的进程，用它们来加载恶意DLL，就像“披着警服的坏人”，很容易骗过基础的安全检测。

重点来了：银狐木马是怎么滥用这两个工具的？

先看银狐木马对RunDll32的滥用：

银狐木马最常见的攻击入口，是伪装成“百度网盘安装包”（比如之前检测到的Baidu-2025102902.exe）。当用户双击这个假安装包时，它会先释放一个合法的百度网盘安装程序（迷惑用户，让你以为真的在装软件），同时悄悄把一个恶意DLL（比如AutoRecoverDat.dll）放到系统的隐藏路径里（比如%APPDATA%\Embarcadero）。

接着，木马就会调用RunDll32.exe，执行这样一条命令：rundll32.exe %APPDATA%\Embarcadero\AutoRecoverDat.dll,xxx（这里的“xxx”是恶意DLL里的导出函数名）。此时任务管理器里显示的是“RunDll32.exe正在运行”——一个系统自带进程，又没有明显的恶意文件名，很多基础安全软件可能会默认它是“正常操作”。

但实际上，这个恶意DLL被调用后，会偷偷解密同目录下的其他恶意文件（比如GPUCache2.xml），生成一个能连接黑客服务器的“后门模块”，还会扫描你的电脑里有没有微信、钉钉、Telegram这些IM进程——一旦检测到，就会释放WinOS远控木马，把你的聊天记录、文件操作甚至键盘输入都传给黑客。

再看银狐木马对Regsvr32的滥用：

Regsvr32的滥用更隐蔽，因为它的“注册组件”行为本身就需要修改注册表，黑客正好借这个“合理操作”隐藏恶意行为。比如在银狐的攻击链里，当木马检测到你的电脑里有微信进程后，会生成一个叫“Code\_Shellcode backdoor.dll”的恶意组件，然后用Regsvr32的“静默模式”加载它——命令是regsvr32.exe /s %LOCALAPPDATA%\Temp\malicious.dll（/s参数表示“静默执行”，不会弹出任何提示框）。

这一步的猫腻在哪？首先，/s模式让用户完全看不到任何操作，你根本不知道有个DLL正在被“注册”；其次，Regsvr32调用时必须触发DllRegisterServer函数，黑客就在这个函数里藏了恶意代码——表面上是“给系统注册组件”，实际上是在内存里加载远控模块，连接黑客的C2服务器（比如27.124.45.x这个地址），还会偷偷禁用你的安全软件（比如切断Windows Defender和服务器的连接）。

更狠的是，银狐木马还会用Regsvr32创建“定时任务”：比如在系统里加一个每天自动执行的任务，命令就是regsvr32.exe /s 恶意DLL路径，这样就算你重启电脑，木马也能通过这个“合法定时任务”重新加载，防不胜防。

怎么区分“正常调用”和“恶意滥用”？

教你3个实用判断方法

可能有人会问：既然这两个进程本身是合法的，我怎么知道它们是不是在加载恶意DLL呢？其实不用太复杂，记住三个关键点就行：

1. 看“调用路径”和“参数”

正常的RunDll32/Regsvr32调用，要么是系统路径下的文件（比如C:\Windows\System32\rundll32.exe），要么参数里的DLL路径很明确（比如C:\Program Files\某正规软件\xxx.dll）。

而恶意调用往往会藏路径：比如DLL放在%APPDATA%、%LOCALAPPDATA%\Temp这些隐藏目录里，或者参数里的DLL文件名很奇怪（比如a1b2c3.dll，没有任何正规软件标识）。

像银狐木马的恶意调用，DLL路径经常是C:\Users\你的用户名\AppData\Roaming\Embarcadero\AutoRecoverDat.dll——这种“用户目录下的陌生路径+不常见的DLL名”，十有八九有问题。

2. 看“是否静默执行+有无正常用途”

Regsvr32如果带/s参数（静默模式），一定要多留个心眼——正规软件注册组件时，要么会弹出提示框（告诉你“注册成功”），要么会在安装过程中明确执行，很少会偷偷用静默模式。而RunDll32如果调用的DLL没有明确的“功能关联”（比如调用一个陌生DLL，却看不到任何对应的系统功能或软件操作），也可能是恶意的。

比如你没装任何新软件，却发现任务管理器里有regsvr32.exe /s C:\Temp\xxx.dll在运行，这时候一定要立刻终止进程，查一下这个DLL的来源。

3. 结合“攻击入口”回溯

银狐木马的攻击几乎都有明确的“入口”：要么是下载了非官方的软件安装包（比如百度网盘、WPS的“破解版”“高速版”），要么是点了搜索引擎里的“非官方下载站”

最后提醒：

别让“系统信任”变成“安全漏洞”

银狐木马这类威胁的可怕之处，就在于它不跟你“硬刚”，而是利用系统自带工具的“合法身份”搞隐蔽攻击——你以为在跟“好人”打交道，其实背后藏着“坏人”。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rSuZI9Hg5leysNlQzCqwjzznXDSNxEicPLlSj1GsPIm9D7wSysDvtcHqEia3eJbAXZBkORTf2YOqo6GQJXJZibIkQ/0?wx_fmt=png)

SOC安全分析之旅

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rSuZI9Hg5leysNlQzCqwjzznXDSNxEicPLlSj1GsPIm9D7wSysDvtcHqEia3eJbAXZBkORTf2YOqo6GQJXJZibIkQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过