---
title: Nexus安卓木马分析报告
url: https://www.4hou.com/posts/m0Zp
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-12
fetch_date: 2025-10-04T11:30:32.416460
---

# Nexus安卓木马分析报告

Nexus安卓木马分析报告 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Nexus安卓木马分析报告

LianSecurity
[技术](https://www.4hou.com/category/technology)
2023-04-11 13:36:19

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)126871

收藏

导语：2023 年 3 月 21 日晚上，链安与中睿天下联合研发的监控系统检测到一种新型安卓木马。在经过睿士沙箱系统捕获样本之后，发现该安卓木马极有可能是原安卓网银盗号木马 SOVA 的变种。

**概述**

2023 年 3 月 21 日晚上，链安与中睿天下联合研发的监控系统检测到一种新型安卓木马。在经过睿士沙箱系统捕获样本之后，发现该安卓木马极有可能是原安卓网银盗号木马 SOVA 的变种。与此同时，意大利安全公司 Cleafy 发布了一篇题为《Nexus：一个新的安卓僵尸网络？》的报告，确认该病毒确实是 SOVA 的变种，并将其重新命名为 Nexus。

**样本分析**

* 样本名称： Chrome.apk
* 样本 SHA256 为:  376d13affcbfc5d5358d39aba16b814f711f2e81632059a4bce5af060e038ea4
* 样本文件大小:  4792032KB

**主要行为列表**

* 删除指定应用以其应用数据
* 安装并启动任意应用
* 隐藏自身应用图标
* 卸载保护
* 上传用户短信数据以及通讯录
* 使用 SmsManager 发送短信、 删除短信、取消短信通知
* 拨打电话
* 获取用户 cookie 信息并上传，注入 cookie 等
* 读取并上传数字钱包信息
* 记录并上传键盘输入记录
* 查询敏感信息手机数据(查询存储邮件、应用账号数据、IMSI 等手机信息)
* 设置静音
* 屏幕解锁
* 访问指定 Url
* 试图禁用管理员用户
* 开启辅助功能
* 监听手机重启事件
* 使用 DownloadManager 下载文件

**安装测试**

当木马安装完成后，手机主界面会出现一个类似 Chrome 浏览器的图标（如图1所示），与真实的 Chrome 图标略有差异。木马使用的图标较小，但在没有相关对比的情况下，基本上很难识别出这种差异。

#

![](https://liansecurity.com/ucenterapi/upload/file/69d9616750171614f126e8e9498235a4)

图 1

当木马启动后，界面会提示用户需要开启“无障碍功能”。在用户点击界面任意位置时，将自动跳转到系统内的“无障碍功能”设置并自动启用该功能（如下图所示）。

![容器 1(1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681120407961250.png "1681119494132864.png")

在启动“无障碍功能”之后，程序会自动弹出并请求获取“设备管理员权限”（如图2所示）。

#

![](https://liansecurity.com/ucenterapi/upload/file/1d918d48ba6f9bf9aa3db5ed431d34f4)

图 2

在恶意应用获得设备管理员权限后，它会在后台不断收集用户信息，用户很难察觉其存在。一旦设备管理员权限被授予，用户在尝试打开设备管理员权限设置界面时会发现界面迅速关闭，无法撤销权限。类似地，通过 adb 执行操作时也会遇到相同问题，界面会立刻关闭。这是因为恶意应用程序已经监控了设备管理员设置界面的开启动作，从而阻止用户撤销其权限。因此，用户需要启用 root 权限才能成功卸载此恶意应用。

#

```
adb shell am start -S "com.android.settings/.Settings\$DeviceAdminSettingsActivity"
```

**样本深度分析**

**基础信息**

![5(1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681120408296133.png "1681119585677937.png")

图 3

![](https://liansecurity.com/ucenterapi/upload/file/9eeec3cfd4ba76d6a0a44345c44b58c3)

图 4

在使用 Incinerator 进行手动分析之前，通过“基础分析”模块，我们发现该样本程序具有加密壳（如图3所示）。这意味着恶意应用程序的开发者使用了一种加密方法来保护其代码，以防止分析和逆向工程。同时，我们注意到签名信息中使用了“CN=Android Debug”（如图4所示），这与正常的 Chrome 证书不一致。这可能意味着此恶意应用程序的开发者试图伪装成正常的 Chrome 应用，以便更容易地欺骗用户并获得其信任。

得益于 incinerator 具备 Apk 权限分析功能，我们可以在 Apk 的详细信息中获取相应的权限列表（如图5，6所示）。

#

![](https://liansecurity.com/ucenterapi/upload/file/8c614ba30c47a1965016569dda4e6884)

图 5

![](https://liansecurity.com/ucenterapi/upload/file/2810336370326fca50ecb1adf6578306)

图 6

在应用权限列表中，样本获取的权限中有 13 项被评定为“危险”的权限。其中有几个权限尤为危险：

* 发送短信（SEND\_SMS）
* 读取短信（READ\_SMS）
* 接收短信（RECEIVE\_SMS）
* 读取联系人（READ\_CONTACTS）
* 写入联系人（WRITE\_CONTACTS）
* 读取电话号码（READ\_PHONE\_NUMBER）

普通应用通常不会申请一些涉及敏感操作的权限，如改写通讯录、读取和发送短信等。这些权限通常仅限于专门的通讯软件。然而，当恶意应用获取辅助功能权限后，它可以利用这一功能来自动开启其他权限，包括一些对用户隐私和安全具有潜在威胁的权限。

辅助功能是 Android 系统中一项强大的功能，旨在帮助有特殊需求的用户更好地使用设备。然而，这一功能也可能被恶意应用滥用，从而执行不受用户控制的操作。一旦恶意应用获得了辅助功能权限，它可以在用户不知情的情况下执行各种操作，如启用其他敏感权限，进而窃取用户数据和破坏其隐私。因此，用户需要谨慎授权辅助功能权限，避免将其授予不可信的应用。

代码中用辅助功能开启的权限列表如下：

#

```
android.permission.READ_SMS：允许应用程序读取短信消息
android.permission.SEND_SMS：允许应用程序发送短信消息
android.permission.RECEIVE_SMS：允许应用程序接收短信消息
android.permission.READ_CONTACTS：允许应用程序读取联系人列表
android.permission.WRITE_CONTACTS：允许应用程序编辑联系人列表
android.permission.READ_PHONE_STATE：允许应用程序读取设备电话状态和身份信息
android.permission.WRITE_EXTERNAL_STORAGE：允许应用程序写入外部存储，例如SD卡
android.permission.MODIFY_AUDIO_SETTINGS：允许应用程序修改声音设置
android.permission.READ_EXTERNAL_STORAGE：允许应用程序读取外部存储，例如SD卡
android.permission.INSTALL_PACKAGES：允许应用程序安装其他应用程序
android.permission.CALL_PHONE：允许应用程序拨打电话
android.permission.GET_ACCOUNTS：允许应用程序访问设备帐户列表
android.permission.READ_PHONE_NUMBERS：允许应用程序读取设备电话号码
android.permission.CLEAR_APP_CACHE：允许应用程序清除所有缓存文件
```

#

![](https://liansecurity.com/ucenterapi/upload/file/ec65723b3273174a343489d3475883f6)

图 7

![](https://liansecurity.com/ucenterapi/upload/file/a4ff37c7b736fe71b508700ba4390c88)

图 8

如上图所示，该应用首先硬编码了需要通过辅助功能开启的权限列表，接着向系统发起对这些权限的申请。在 PermissionsTask 环节中，应用会监听权限申请的动作。一旦监听到权限申请，该应用便利用辅助功能在权限申请界面上自动点击“同意”按钮。

**静态代码分析**

在使用 Incinerator 工具对样本进行自动脱壳并分析恶意行为代码后，我们发现以下主要功能：

**1. 删除指定应用以其应用数据**

恶意应用具有删除其他应用及其数据的能力，可能影响用户正常使用手机及其应用。

#

![](https://liansecurity.com/ucenterapi/upload/file/bac232005174772d5cb898d949dc8617)

图 9

clearApp 方法确实是通过执行 pm clear package 命令（如图9所示）来删除与特定应用程序包相关的缓存数据，包括图片缓存、临时文件、数据库缓存等。这样可以帮助清理设备上的垃圾文件，释放存储空间。

而 deleteThisApp 方法则通过触发 android.intent.action.DELETE intent 来实现应用的卸载（如图9所示）。当系统接收到这个 intent 时，会弹出一个卸载确认界面。通常情况下，用户需要在此界面上手动点击“同意”按钮才能完成卸载。然而，由于这个恶意应用具有辅助功能权限，它可以在卸载确认界面出现时自动点击“同意”按钮，从而在用户不知情的情况下完成卸载操作。这种做法进一步提高了恶意应用的隐蔽性和破坏性。

**2. 安装并启动任意应用**

恶意应用可以安装并启动其他应用，可能进一步传播恶意软件或将用户引导至恶意网站。

#

![](https://liansecurity.com/ucenterapi/upload/file/47e148941a8983668bf233bc1721120a)

图 10

安装和卸载应用确实是通过辅助功能来实现的。这种方式可以方便地为用户自动化应用的安装和卸载过程。唯一的区别在于，为了实现这一功能，恶意应用需要适配不同厂商的安装应用包名和安装 Activity 的名称。

这样一来，恶意应用可以在各种不同的设备上成功执行安装和卸载操作，从而更加隐蔽地实现其恶意行为。这种策略使得恶意应用在各类设备上具有更广泛的攻击能力。

**3. 隐藏自身应用图标**

为了难以被发现和卸载，恶意应用会隐藏自己的应用图标（如图11所示）。

#

![](https://liansecurity.com/ucenterapi/upload/file/2a22503bc8505cabd5cbbc4084d626b7)

图 11

在这个恶意应用中，开发者使用了 setComponentEnabledSetting 方法来禁用 Launcher Activity。这样一来，用户就无法通过设备主屏幕上的应用图标（Launcher Icon）来操作或访问该恶意应用了。

setComponentEnabledSetting 方法可以用来启用或禁用应用程序组件，如 Activity、Service、BroadcastReceiver 等。在这种情况下，恶意应用通过禁用 Launcher Activity，达到了隐藏自身的目的，让用户更难以察觉其存在。这种做法进一步提高了恶意应用的隐蔽性，使其更难以被发现和移除。

**4. 上传手机联系人等敏感信息**

恶意应用可以窃取并上传用户的联系人、短信、Cookie 等信息，可能导致用户隐私泄露和财产损失。

#

![](https://liansecurity.com/ucenterapi/upload/file/fec40b6d80161cd69eedbb748387e9ce)

图 12

![](https://liansecurity.com/ucenterapi/upload/file/0e9d5f601edfe7f0a01b49920a0a22aa)

图 13

如图12、13所示，恶意应用首先通过 content://sms 访问短信内容，然后经过一系列业务逻辑处理，将其整合到网络请求的数据中。除了短信数据，这个请求还包含了如 SIM 卡信息、受害者设备的 IP 地址、国家、城市和设备型号等信息。最后，这些数据会被发送到指定的服务器。

通过这种方式，恶意应用能够窃取用户的短信和设备信息，然后将这些数据发送给攻击者。攻击者可以利用这些信息进行各种违法活动，例如诈骗、窃取用户隐私、甚至是身份盗窃。

**5. 使用 SmsManager 发送短信、 删除短信、取消短信通知、读取短信**

5.1 上传短信

![](https://liansecurity.com/ucenterapi/upload/file/90ce1eff5787453308a3cbef169a556b)

图 14

![](https://liansecurity.com/ucenterapi/upload/file/e2261256839bc65eb625995adddb6d32)

图 15

根据上述描述，该恶意应用通过监听收到短信的系统广播，从广播中提取收到的短信内容，然后将每一条短信发送给远程服务器。在完成这个过程之后，应用还会终止收到短信的广播，以免被用户或其他应用程序发现。如图15所示，super.execute 指的是将收集到的短信数据发送给远程服务器。

这种行为表明，该恶意应用在窃取用户短信方面采取了较为积极的手段。用户需要加强对此类应用的防范意识，以避免对其隐私和安全造成不良影响。

5.2 发送短信

![](https://liansecurity.com/ucenterapi/upload/file/7321db5b9db67fd34ae3b76be3f12587)

图 16

调用系统 SmsManager 发送短信（如图16所示）。

**6. 获取用户 cookie 信息并上传，注入 cookie 等**

![](https://liansecurity.com/ucenterapi/upload/file/9545c3cbd4eb39c1f88d7aeb452a2483)

图 17

如图17所示，读取所有 cookie，上传到远程服务器，并且通过 CookieManager 把本地 cookie 删除。

**7. 读取和上传数字钱包信息**

7.1 读取余额

![](https://liansecurity.com/ucenterapi/upload/file/11fad808556b0d3a373165019b18dbe8)

图 18

通过辅助...