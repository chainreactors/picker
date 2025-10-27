---
title: 记一次Android 恶意软件逆向及Frida动态分析
url: https://forum.butian.net/share/4563
source: 奇安信攻防社区
date: 2025-09-25
fetch_date: 2025-10-02T20:37:47.105199
---

# 记一次Android 恶意软件逆向及Frida动态分析

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

### 记一次Android 恶意软件逆向及Frida动态分析

* [移动安全](https://forum.butian.net/topic/50)

本文记录了一次Android 恶意软件逆向及Frida动态分析的实战过程，包括脱壳、恶意软件代码逆向分析、frida破解加密、绕过frida检测等技术细节，详细分析了Android 恶意软件的攻击链路。

一个在国外的同学说工作邮箱收到了一封钓鱼邮件，扫描钓鱼邮件的二维码会下载一个Android APP，想让我帮忙分析下这个恶意APP究竟会执行什么操作。Android 恶意软件平时遇到的不多，便想着研究研究。
逆向分析
====
脱壳-解除DPT-Shell的保护
-----------------
先在Android模拟器上运行该应用程序，查看进程：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-7d05cc04b56b27e368e55240035df9e8c6518ed7.png)
使用JADX反编译代码，反编译后查看包名，竟然与进程中的包名不一样。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-0e4d662b2845cba375ab8f28790a615fd18289d9.png)
我们简单查看一下代码，从这里可以看到APP受到名为 [\*\*DPT-Shell\*\*](https://github.com/luoyesiqiu/dpt-shell) 的工具的保护。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-5bb2f7f5e2f63171bbdc22b96b892c146535979c.png)
由于这是一个开源应用程序保护工具，因此去github上分析一下源码看看它是如何工作的。在 APK 加壳过程中，将事先准备好的壳 dex 与原始应用的 dex/资源压缩包拼接生成新的 `classes.dex`，其中壳 dex 负责解密与加载逻辑，原始数据以 zip 形式附加在壳 dex 之后，并在文件末尾额外写入 4 个字节记录原始数据长度，最后修正 dex 的文件大小、SHA1 和校验和头部，使其成为合法的 dex 文件，从而实现安装时先运行壳逻辑、再在运行时释放和加载真实的应用代码，达到保护与防逆向的目的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-0bcea9e92c18a0a98770efbbb40b6c29575308c1.png)
注意到代码中有这样一段`ZipUtils.compress(getDexFiles(apkDir), getOutAssetsDir(apkDir).getAbsolutePath() + File.separator + "i111111.zip"); `,`getDexFiles(apkDir)` 会收集 \*\*APK 里真正的 dex 文件\*\*,然后用 `ZipUtils` 压缩，打包成一个压缩包,输出路径就是`assets/i111111.zip`,因此，下一步是寻找保存在 assets 文件夹中的实际 dex 文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-9775584c835f6d02025a2c524d985ed448f8335a.png)
最终在应用程序android目录的code\\_cache文件夹中找到了i111111.zip，解压后就得到了真正的dex文件：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-8ae67cc38da19712f53eec45defd4b5d0e7f8268.png)
恶意软件功能分析
--------
BroadcastReceiver 暴露了大量自定义广播指令，涵盖应用管理（安装、卸载、获取应用列表）、界面控制（弹窗、日志窗口、权限界面）、敏感操作（相机、人脸识别、短信收发、身份证上传、支付页面）以及系统控制（后台运行、音量、外部存储读写）等功能，加上其中出现的 \*\*ShowBankDF\*\*（银行对话框）模块，可以判断该 App 具备远程控制和窃取敏感信息的能力，整体行为特征非常接近 \*\*恶意金融木马/远控木马\*\*。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-dd21228e78750e3bd5299ef92acd6c791fcb0c17.png)
接下来我们具体分析：
### 短信追踪
`SmsServiceRoom` 是一个封装短信内容的服务类，采用单例模式保存 `SmsContent`，对外提供存取接口。它在整个 App 中可能承担 \*\*短信拦截、存储与转发的核心功能\*\*，和前面 BroadcastReceiver 中的短信相关广播（读取、通知、发送）形成呼应，进一步印证该 App 具备 \*\*监控和操纵用户短信\*\* 的恶意特征。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b86ccd533cb2a645068ddeb904b2905df98a1252.png)
### 屏幕录制
`ScreenRecordService` 是一个后台录屏服务类，支持持续录制屏幕。它与前面提到的短信拦截、摄像头、银行对话框等模块一起，构成一个功能完整的远控木马框架：既能获取短信、相机、身份证件，又能录屏监控用户在应用中的操作，尤其可能用于 \*\*窃取网银/支付类操作的敏感信息\*\*。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-c4c1ce4d6334d92f3c00262e48354050c9bf81ca.png)
该应用程序在后台运行多个服务，其中突出显示的是 ScreenRecord 服务。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-d64d4ed55fcb5e3dda6ef0c74391dc4957821dcd.png)
### 数据泄露
媒体窃取服务，属于恶意Android应用的服务模块，用于统计用户的音频、视频、图片、下载文件和联系人等信息，窃取到敏感信息用于进一步勒索和诈骗。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-2144a456efa72e238065de4255b039c9861c0eac.png)
联系信息窃取服务，属于恶意 Android 应用的联系人收集模块，用于序列化并上传用户的姓名、电话、邮箱及联系历史等隐私信息。攻击者窃取然后使用这些信息对其他潜在受害者进行横向移动，并采取与当前受害者相同的步骤。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-67e5962660b6955eac8294d09333dc6064b92651.png)
### 浮窗密码窃取
`BcaInputPwdWindow` 是恶意 Android 应用中的浮窗密码窃取模块，它继承自 `FloatWindow`，在用户界面上悬浮显示虚假输入框，通过 `LiveString pwd` 实时捕获用户输入的密码，并利用 `commitData()` 方法可能将密码上传到远程服务器，结合 `show(int i)` 方法实现对系统界面覆盖和展示，整个模块经过混淆和加固，属于典型的 Android 欺骗输入、窃取敏感信息的技术实现。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-a481557a7bac8dd58a6c3cb7b405313db53765d5.png)
借助此功能，恶意软件可以自动执行点击并假装这是来自用户的合法点击事件。为了了解该模块如何在诈骗活动中利用，我们进一步跟进Strategy类，如下图所示：
`PhoneStrategy` 是恶意 Android 应用中管理手机 PIN 或解锁策略的模块，封装单个和多组策略对象，可能用于记录或匹配用户密码模式，以配合浮窗窃取和其他隐私收集功能。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-8f240099b2f3624d99cb6d1e45a3f6028221ce57.png)
`ListenMethod` 是恶意 Android 应用中定义的枚举监听模块，提供多种用户操作和输入事件捕获方式，其中包含密码输入监听，可能与浮窗和策略模块结合，用于全面监控和窃取用户敏感行为。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-ddc01609c5f1cd62a5c1b8b9063bd883292c1bc8.png)
\*\*`PhoneStrategy`\*\* 中封装了单个和多组策略 (`StrategyData`)，但是在反编译的源码中没有找到策略的内容，由此可以想到此恶意软件应用程序会动态加载来自JNI Functions 的数据，也就是so文件，我们需要用Ghidra逆向so文件进行进一步分析：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-645a46fec90bc24e81a89491757019c52be76ecf.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-bd0de10057efb797e7dc4b0811938ee096eb12a7.png)
获取到保存在Native Lib中的策略数据后，可以在看到这条策略定义了一个针对 \*\*BBL 手机银行 App 的 PIN/数字输入监听规则\*\*，通过监听点击事件获取用户输入的数字键（0~9）和删除操作，并将文本内容返回给应用逻辑（可能进一步上传），实现精准收集用户 PIN 或交易密码。该策略结合前面分析的 `BcaInputPwdWindow` 和 `ListenMethod`，形成完整的 \*\*输入监听 → 数据收集 → 远程上传\*\*链路。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-0731768274d3d255d33a72ca952a54b89fd315f8.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-4e9d79748b58729a18da043f455c9e3074162a35.png)
### 人脸识别视频录制
FaceRecognition服务，人脸服务通过前置/后置摄像头在前台或策略触发条件下隐蔽采集用户面部图像或视频，可能结合本地处理与加密上传，实现身份验证欺诈或账户接管。当攻击者有足够的信息来访问手机银行账户时，将会使用记录的人脸识别视频绕过手机银行的登录验证。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b1b654dd44fedaee9a345747e780e91a39060f25.png)
### 恶意软件利用链路总结
当受害者下载安装恶意应用后，应用会在受害者使用目标应用（如银行或支付 App）时触发各模块协同工作：`BcaInputPwdWindow` 在前台显示浮窗覆盖真实界面，诱导受害者输入密码或 PIN；`ListenMethod` 枚举监听用户的点击、输入和回车行为，配合 `PhoneStrategy` 和 `StrategyData` 策略决定何时收集敏感信息；同时，`MediaFilesData` 和 `ContactData` 被动收集受害者的多媒体文件和联系人信息，人脸服务模块`FaceRecognition`在策略触发或用户操作过程中隐蔽采集面部图像或视频，所有数据经序列化或加密上传至远程服务器，实现从用户安装、正常操作到多类型隐私数据收集和远程窃取的完整互动攻击链路。
动态分析
====
使用BurpSuite来拦截恶意软件应用程序流量，但是可以看到报文是加密的，在代码中查找密钥，但是都无法解开加密，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-ab23e582ab6b1a74d7619c5c280fe117d89c2e94.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-5366065b1b08ee1254ba234876aebc4853c90e96.png)
尝试用frida来破解加密，在加密前发起请求，解密后发起响应。在第一次尝试中，发生了与 \*\*Null 指针异常\*\*相关的错误。程序尝试返回\*\*0x0\*\*，由于这不是一个有效的地址，会触发 \*\*Null 指针异常\*\*。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-960af59f35d409290de1ceb9de4a5a31bdfe7a9b.png)
考虑到APP试用了DPt-shell保护程序，分析DPT-Shell源码看看是不是对frida也有检测：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-003c96d84ee0b9d30a06760ed837d461a3a1cf38.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-a8c2eacc76df46e99a7437c27801835fea25fea6.png)
如果代码检测到 \*\*Frida-server\*\*，将运行汇编指令，这意味着 lr（链路寄存器）设置为 0，因此当程序尝试使用此寄存器返回时，它最终会到达程序最终崩溃的地址。`mov lr,#0 0x0`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-415678c5cba344515cc8f991bcba435829878103.png)
通过分析，我们可以得知\*\*frida 检测\*\*使用 \*\*pthread\*\* 创建一个新线程来运行 \*\*Frida Detection\*\*，因此我们可以用以下脚本来bypass，通过 hook `pthread\_create` 并在特定条件下返回错误，Frida 检测线程根本无法启动，程序就不会触发 `dpt\_crash()`。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-43068d1424fd348f8f27cc4398750325aabd2076.png)
最终绕过成功，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-8c7a2d9fed8bbd83e50c01b27c38ea39faa0fd08.png)
成功看到登录的明文数据，包含了用户名、密码、银行...