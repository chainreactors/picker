---
title: 移动应用测试之APP日志的抓取
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247506090&idx=1&sn=5863007a4eb9c59b7b532757a305a2f0&chksm=ce5dfacbf92a73dd4b91f7e3d801ab5a9c4b1aeceedf7c4abc2ca5e6439f94e2c773886fe659&scene=58&subscene=0#rd
source: Tide安全团队
date: 2023-01-06
fetch_date: 2025-10-04T03:10:30.046680
---

# 移动应用测试之APP日志的抓取

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOfneqyuFojN3BNXaNiaenFMgWVl3VgCHO9DewoM4a0sXOZuFrkDqRsRw/0?wx_fmt=jpeg)

# 移动应用测试之APP日志的抓取

原创

molengsu

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVhN8RQR8c6zEaACxatlch2rgdzYzYAiahr1GUq1cLMMGVnvKpF8biaWA/640?wx_fmt=png)

# 1.为什么要抓取app日志

在移动应用渗透测试中敏感信息安全风险检测需要对应用日志进行分析，日志内容如果包含敏感信息，可能会造成数据泄漏的风险。

在app应用程序发生异常出现Crash崩溃、ANR阻塞时通常说明应用程序存在一定的问题，这时候需要收集应用日志定位错误位置帮助开发调试修复程序。

# 2.Logcat收集app日志相关工具配置

Android日志系统提供了记录和查看系统调试信息的功能。日志都是从各种软件和一些系统的缓冲区中记录下来的，缓冲区可以通过logcat命令来查看和使用。logcat本身是android的shell的一个命令，可以通过adb shell进入shell后执行logcat命令,也可以通过adb logcat直接运行。

## 2.1 ADB的安装与基础使用

adb全称是Android Debug Bridge，它是一个命令行工具，通过它可以与Android设备进行交互，可以进行常见的安装/卸载app、打开app、查看app的日志等操作。

这里简单列出几条ADB常用命令为下文中我们测试使用：

```
# 1.查看
adb --help #查看帮助手册
adb devices #检查连接到电脑的安卓设备，常用的检查命令
adb shell dumpsys activity | find "mFocusedActivity" #Android 7.0及以下查看前台应用包名
adb shell dumpsys activity | find "mResumedActivity" #Android 8.0及以上用此命令查看包名
adb logcat #打印log信息
adb logcat -v time #log信息显示时间戳
adb logcat -v time > d:\logcat.txt #把日志信息重定向至d:/logcat.txt

# 2.连接与交互
adb connect ip:port #通过WiFi进行远程连接手机进行调试，手机和电脑需在同一个局域网上，计算机内部通信地址127.0.0.1，夜神模拟器默认的端口号是62001
adb disconnect ip:port #断开一个（ip:port）连接
adb shell #登录设备shell（安卓的底层是Linux）

# 3.文件传输
adb pull <手机文件路径> <本机路径> #从手机拉取文件到本地电脑
adb push <本地电脑路径> <手机路径> #从本地推送文件到手机

# 4.安装与卸载
adb install *.apk #为了快速获取apk的安装包路径，可以直接把apk直接拖到cmd的窗口，安装成功会返回success
adb uninstall <appPackage name> #卸载需要输入应用包名
```

ADB的安装：

实际上adb是一个免安装工具，使用adb时只需要adb工具被命令行调用到就可以了。

1.首先根据系统的版本下载adb，获取连接https://www.androiddevtools.cn/

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOFfycibQISic5l0qdaDW1mAFicibl28oib3ibYvpvcYicyE2vmiasOagYvejXRw/640?wx_fmt=png "null")

2.解压下载的Platform-tools zip包，将Platform-tools路径添加到系统环境变量中。随后在命令行执行`adb version`查看adb版本，未出现报错安装配置成功。

3.mac os中可直接使用brew进行安装

```
brew install android-platform-tools
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfO8Vic2FVI8QTfap0GVibOyF689jmSQvPZ9HiaNibYg7tSMmEfQXqD8bibEdA/640?wx_fmt=png "null")

安装完成后在根目录`.bash_profile`添加环境变量，使用`open .bash_profile`打开编辑，在下方插入如下代码

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOcKdrTKHTT4EopoLc9zNSjGJLiaL2oKmo2mtlu93XKj0rwI4tpq1f3LQ/640?wx_fmt=png "null")

```
export ANDROID_HOME=/Users/用户名/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

保存后`source .bash_profile`更新变量，查看adb

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOga97Nic4sMq005hk3gw3hR4gErxBXVSYY25w0kedc4nBvbFIJ0Ziaj9A/640?wx_fmt=png "null")

## 2.2Logcat语法命令

```
语法格式：

[adb] logcat [<option>] … [<filter – spec>] …
选项：
-b：加载可供查看的备用日志缓冲区，例如event或radio。默认使用 main和system缓冲区集。请参阅查看备用日志缓冲区

-c, –clear：清除所选的缓冲区并退出，默认缓冲区集为main和system。要清除所有缓冲区，请使用-b all -c。

-e, –regex=：只输出日志消息与匹配的行，其中是一个正则表达式

-m, –max-count=：输出行后退出。这样是为了与–regex配对，但可以独立运行

-print：与–regex和–max-count配对，使内容绕过正则表达式过滤器，但仍能够在获得适当数量的匹配时停止

-d：将日志转储到屏幕并退出

-f：将日志消息输出写入

-g, –buffer-size：输出指定日志缓冲区的大小并退出

-n：设置轮替日志的数量上限，默认值为4，需要使用 -r 选项

-r：每输出时轮替日志文件，默认值为16。需要使用-f选项

-s：相当于过滤器表达式‘*:S’；它将所有标记的优先级设为“静默”，并用于放在可添加内容的过滤器表达式列表之前

-v：设置日志消息的输出格式。默认格式为threadtime。

-D, –dividers：输出各个日志缓冲区之间的分隔线

-c：清空（清除）整个日志并退出

-t：仅输出最新的行数。此选项包括-d功能
```

## 2.3Logcat缓冲区

android log输出量巨大，特别是通信系统的log，因此，android把log输出到不同的缓冲区中，目前定义了四个log缓冲区：

1）Radio：输出通信系统的log

2）System：输出系统组件的log

3）Event：输出event模块的log

4）Main：所有java层的log，遗迹不属于上面3层的log

缓冲区主要给系统组件使用，一般的应用不需要关心，应用的log都输出到main缓冲区中。默认log输出（不指定缓冲区的情况下）是输出System和Main缓冲区的log。

实例：

```
adb logcat –b radio

adb logcat –b system

adb logcat –b events

adb logcat –b main

//将缓冲区的log打印到屏幕并退出
adb logcat -d
//清除缓冲区log（testCase运行前可以先清除一下）
adb logcat -c
//打印缓冲区大小并退出
adb logcat -g
//输出log
adb logcat -f /data/local/tmp/log.txt -n 10 -r 1
```

# 3.日志收集过程

### 连接设备

先将设备通过usb数据线连接到电脑，设备开启USB调试。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOhZVEH3SYJu2fw544icS6G3vgOwZKlAb650IAyia3OJAnkoZsUAMHTS9A/640?wx_fmt=png "null")

通过`adb devices`命令查看是否连接成功：

```
molengsu@mlsdeMacBook-Pro / % adb devices
List of devices attached
FJH5T19114009780 device
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOIHwg5pq5v6fP0WcT9JjGvggSWBk1CDEXqcwZKRz0qxt4Hh5rvhJXOQ/640?wx_fmt=png "null")

### 查看设备log输出

我们直接通过adb logcat查看的输出是所有应用的

```
adb logcat -d  ##所有应用logcat输出
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfORB2Vkr4wypX4gHmPRibqAe6FNlsqXQiarjuSOqzmwSemdou0eqNqHT8g/640?wx_fmt=png "null")

为了精准分析我们可以通过应用pid来查看我们想要分析的应用日志。首先列出设备已安装的应用查看应用包名

```
adb shell pm list package
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOkicGpqbAfxLicRbXX06uh7aLu1XIhRx2icr6BFaiaCecOgI8hFZPia38bnQ/640?wx_fmt=png "null")

然后获取应用的pid，在获取时现在手机上打开要获取的应用，因为pid是分给进程的，应用运行起来才会分配pid。需要注意的是，pid是分配给进程的，如果app关闭了再重新打开，就会分配一个新的进程，同一个包名对应的pid就会变。

```
adb shell dumpsys meminfo com.xxxx.xxxx  ##com.xxxx.xxxx是包名
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOoD49kCP9noTx0YyZ3WKDyPI4nvUT3a7gic1p7omWnLbOTCKcXiaa2glg/640?wx_fmt=png "null")

拿到pid后就接着可以输出应用日志了

```
adb logcat -d --pid=30923
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOpbfSaZpREqHsMibJyFLjfjrftyOo4hvDtgZ76dyKqHXibdoE2yMeiamcg/640?wx_fmt=png "null")

为了方便查找也可以将日志导出到文件中，导出时要注意新建一个文本向里写入文本设置好可写的权限。

```
adb logcat -d --pid=30923 > logcat_test.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfOVLRHgwvllaGPRpe2HbmdQExicEWh9iaNbHMHyzKrvQ93JwnDldxDKBIw/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVRkIZicnNe7lTWSdRO3hkfODQUjLAeVfUDH9L58Kt1FrapvfbTsUhYdVtjoTuDBJVdKxcyubiar1cg/640?wx_fmt=png "null")

往期推荐

[敏感信息泄露](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247500219&idx=1&sn=8da48a9a049bab2f9215ad373868a1a5&chksm=ce5de3daf92a6acc7c2a58329c913062e9c34a9615ce742b761b2775916781abb50159a7d2d7&scene=21#wechat_redirect)

[潮影在线免杀平台上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499902&idx=1&sn=59cba8d980b4ecb0deefff99edaabd4d&chksm=ce5de21ff92a6b09a8972a0144557b0099e443aa8e018b17151c816fc7f08f3615ecb22617fc&scene=21#wechat_redirect)

[自动化渗透测试工具开发实践](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498466&idx=1&sn=085c15679436dedb06a179ca8d47951a&chksm=ce5dd883f92a5195ef74ac517741f6d3da0da40b5501d72016e52cb70344904bb85b8aef65ba&scene=21#wechat_redirect)

[【红蓝对抗】利用CS进行内网横向](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247492640&idx=1&sn=43b1991dc5628eab322923083fde8d70&chksm=ce5dc641f92a4f57ffb18e2977644b1f977fcc5e0eccdf10956d3ae4ce70dc95024500631e89&scene=21#wechat_redirect)

[一个Go版(更强大)的TideFinger](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498344&idx=1&sn=3679330363ff6890166b09f6a502f769&chksm=ce5dd809f92a511f6066fcbb12fb5c1dc8c2642e4e2690dad64d76cc6f9247eae356d16f5810&scene=21#wechat_redirect)

[SRC资产导航监测平台Tsrc上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499823&idx=1&sn=065ffeae6bd02fff922cfb12c5a0f4df&chksm=ce5de24ef92a6b58f709260b691e6b36e4a53aac00d3022946302b8e638696ed55c70e13e16f&scene=21#wechat_redirect)

[记一次实战攻防(打点-Edr-内网-横向-Vcenter)](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498965&idx=1&sn=655548831da6808a020ad07294a92e60&chksm=ce5ddeb4f92a57a283d5692c246e54655319ab0d09f6403e354300a2777cda6ae4c787631ab3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/rTicZ9Hibb6RWbGNtVfIZbm2rmGO4hQDzQUrLN62vEGlA4fPmib5utUAp9gbQicb6FC82RjsVI5vx7wEc9yAAiaFEoQ/640?wx_fmt=gif)

E

N

D

**知识星球产品及服务**

**团队内部平台**：潮汐在线指纹识别平台 | 潮听漏洞情报平台 | 潮巡资产管理与威胁监测平台 | 潮汐网络空间资产测绘 | 潮声漏洞检测平台 | 在线免杀平台 | CTF练习平台 | 物联网固件检测平台 | SRC资产监控平台  | ......

**星球分享方向**:Web安全 | 红蓝对抗 | 移动安全 | 应急响应 | 工控安全 | 物联网安全 | 密码学 | 人工智能 | ctf 等方面的沟通及分享

**星球知识wiki**：红蓝对抗 | 漏洞武器库 | 远控免杀 | 移动安全 | 物联网安全 | 代码审计 | CTF | 工控安全 | 应急响应 | 人工智能 | 密码学 | CobaltStrike | 安全测试用例 | ......

**星球网盘资料**：安全法律法规 | 安全认证资料 | 代码审计 | 渗透安全工具 | 工控安全工具 | 移动安全工具 | 物联网安全 | 其它安全文库合辑  ...