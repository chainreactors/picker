---
title: Android应用程序渗透测试
url: https://mp.weixin.qq.com/s/GXxmnQrrVAyNFXaQRe09zg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:27:26.176237
---

# Android应用程序渗透测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kJjVGsbcK2BT6QicDGBZsmyS97ZxZ1LSxZnPQcAQDNiaYZOTVIfGiaf9TI9K85ynhbPd86zAYzc6yicGVJoogr1AbQ/0?wx_fmt=jpeg)

# Android应用程序渗透测试

原创

Gal0nYu

OneTS安全团队

![]()

在小说阅读器中沉浸阅读

点此即可关注公众号

声明

本文属于OneTS安全团队成员**Gal0nYu的原创文章，转载请声明出处！本文章仅用于学习交流使用，因利用此文信息而造成的任何直接或间接的后果及损失，均由使用者本人负责，OneTS安全团队及文章作者不为此承担任何责任。**

温馨提示：本篇文章全是干货，包含了安卓APP靶场测试、补充测试项、隐私合规检测及工具推荐，内容较多请耐心看，实在看不完先收藏码住多看几次!!

**一、靶场下载安装**

https://github.com/t0thkr1s/allsafe

Allsafe 是一个包含各种漏洞的应用程序。与其他的 Android 应用程序靶场不同，这个应用程序不太像 CTF，更加贴合真实应用程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsibZ2ETyiaboulVScO8CTZbUplLlNmxiaYHpBYTcrZMlX3s4M3tRYvbtjQ/640?wx_fmt=png&from=appmsg)![]()

1、下载apk

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsjwVZZTbB1Cg8XQ7alrbETNOc44Rxg4iaoH6A5XJ9NZVCxReMV9QS68w/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

用以下命令即可安装apk到测试机上

adb install allsafe.apk

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOspBUgsJBlDD61qmWBzXI5ELreria2BAZ2olWmx6p9em77cJHjxdHSx3w/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

2、成功安装

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsNMwqrcZU45FDNTJLXAGXBj1ofoNLuHj72TfDpTyPEnDm8icEIA3rrMQ/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

**二、****靶场测试项**

1、不安全日志记录（Insecure Logging）

简单的信息泄露漏洞。使用 logcat 命令行工具发现敏感信息。

adb shell 'pidof infosecadventures.allsafe'

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsSwlh8zIUaunVEZlC9oIun7xBUJtjfBbf6PNucvLljNaVjdRmp4hdog/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

adb shell 'logcat --pid pid | grep secret'

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsnQ53iajlcqomkVwmMuDk4kfSRuoEczqKXVzwZPubibkl5WRjrkbUDXUQ/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

2、硬编码凭证（Hardcoded Credentials）

代码中保留了一些凭据。对应用程序进行逆向工程并查找敏感信息。

用jadx来反编译allsafe.apk，可以在HardcodedCredentials里找到硬编码账号密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOs8FIG6OF6yagt2IJy4JWnw6JicQU82RakVaDdZicy8HgfLWhQD55BLrrA/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

3、Root检测（Root Detection）

通过Frida来绕过Root检测

用jadx反编译，查看Root检测的位置

发现通过RootBeer(RootDetection.this.getContext()).isRooted()来查看是否Root

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsQXDO0Q9VzS4ssNEneE6yY3p6xYoFs7Ay5pXL2E9XIs6s51bPZh001A/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

用Frida来hook返回值

启动frida服务端

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOswiaWgu3V6UauAtXg3Ve32ZxYVowOD8bEZdVlbH2hgaTJItJLG4f5tuQ/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

先查看靶场现在显示的是设备是被Root

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsn0nBARgBImXsztjCaGBjjuxnTHALI85w2DwqXzFEdqXsvuicZnOVw2g/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

编写hook脚本

```
Java.perform(function () {     var RootBeer = Java.use("com.scottyab.rootbeer.RootBeer");     RootBeer.isRooted.implementation = function () {         console.log("Bypassed RootBeer.isRooted()");         return false;     };});
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsnmHaYDPoiaFdLaQibfGO0bYRsnj9loofsiaxbYxibLRHScScOZDCibhvHdA/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

执行以下命令来hook

frida -U -f infosecadventures.allsafe -l hook.js

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsM0VeibficUWEam7icicA7us8jkhO3qUBQKls6WQaDmZ8OKBrI7yJzj9BWg/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

再来查看靶场显示，成功绕过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsvCdBRSVJ4dorpIINB0efdoGsJroKEQsVmsuiaXIz2HyjkN5ialMWyElQ/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

4、安全标志绕过（Secure Flag Bypass）

通过Frida来绕过不允许截屏

尝试截屏发现提示该应用不允许屏幕截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CGzR6MESK5Kk1vl8oG6hOsFupNuK1qyQI655eQbNWKQF2bHeQ0L1I59zj1kqXfwAZkNcAmm1mYQg/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

用jadx反编译apk，发现getWindow().setFlags(8192, 8192)，通过设置flag来禁用截屏

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CTafP8DjN15lWQzuMfC2uicT7rsY2kpe7tiacgSXf8Q0HiaHpfHGwcXUWrZz0zicsx8Ja0MywKNBQT6Q/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

编写脚本来hook，脚本代码如下

```
Java.perform(function () {var Window = Java.use("android.view.Window");Window.setFlags.implementation = function (flags, mask) {console.log("Original flags: " + flags + ", mask: " + mask);var newFlags = flags&(~8192);var newMask = mask&(~8192);console.log("Modified flags: " + newFlags + ", mask: " + newMask);return this.setFlags(newFlags, newMask);};});
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CTafP8DjN15lWQzuMfC2uicppuHmFiaI4yJdibdLoN6M7ezH9c6rB1qjag7g2DuIxGM4WY6wvhoXqUg/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

启动frida服务端

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CTafP8DjN15lWQzuMfC2uiciblWicnuUkY1NS3UibPGDzBNib2v8WQfJwqWB8B3nChDJOm3Fca5Iia9cMA/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

用以下命令来hook

frida -U -f infosecadventures.allsafe -l hook.js

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CTafP8DjN15lWQzuMfC2uicjHk0Hh0ZlibPmiaic6HDQ8hX3ywlHbwzs3Me7bR86e7zxyzAiafrd0JGdg/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

成功截屏

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CTafP8DjN15lWQzuMfC2uic4EESwkIXLCvdzz7zIyHpEbs7iaMWYrtlaj5vIibvt2y5aRQYc1Onv3CA/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

5、Pin绕过（PIN Bypass）

有一个简单的PIN 码验证。在代码中找到该方法，并使用 Frida 覆盖返回值。

用jadx反编译可以找到byte[] decode = Base64.decode("NDg2Mw==", 0)

Base64解码为4863

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2CTafP8DjN15lWQzuMfC2uicuc8DEnr27yp2h8V0J6cXiaC1nAY7EdByXRB6Mpe8jmat3QJHEic4cKJw/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()

但是题目需要我们用Frida来hook函数checkPin的返回值来绕过验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2DWkkeWbia6ic7Oqot6dgWDZKKVcPtibS1S42nibsIwpxIuxqxw0S5lCZ7yhjKruvhbcoAfcS9HMSkw9w/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()

编写脚本

```
Java.perform(function() {    // Get the PinBypass class    var PinBypass = Java.use("infosecadventures.allsafe.challenges.PinBypass");    // Hook the checkPin method    PinBypass.checkPin.implementation = function(pin) {        console.log("[*] Original checkPin called with PIN: " + pin);        // Force the method to always return true        var result = true;        console.log("[+] Overriding return value to: " + result);        return result;    };    console.log("[+] PinBypass.checkPin() hooked successfully!");});
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2DWkkeWbia6ic7Oqot6dgWDZKV2NhQIlrj44HyajbGJqecQj54A5FiaKS7zpYGZuctDGQGdklF60qk0A/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()

启动frida服务端

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2DWkkeWbia6ic7Oqot6dgWDZKqMLEtsT5SAY6XlYJ3BDMXFVUKiaGPWibk2icRUaBfso4GWA0MRDRXuWWQ/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()

用以下命令来hook

frida -U -f infosecadventures.allsafe -l hook.js

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2DWkkeWbia6ic7Oqot6dgWDZKj3VLKNnaciahrOhmGVa59JJmp3EUaAkpMUQpneScJRCGrxawq8x1L2Q/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()

成功hook

 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2DWkkeWbia6ic7Oqot6dgWDZKSwAmibMBY3sCVicVuLf7BdZteLcZJE4D80Qox3JNBWXQTy4zf0g5Js8g/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()

6、Deep Link 漏洞利用（Deep Link Exploitation）

与不安全的广播接收器类似，需要提供正确的查询参数才能通过靶场

用jadx来反编译，获取了启动deeplink的intent的url中的key参数，key需要等于ebfb7ff0-b2f6-41c8-bef3-4fba17be410c

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kJjVGsbcK2DWkkeWbia6ic7Oqot6dgWDZKZfXsfoxCia11QkAZhEY5I8wbVouY9eVmpCbGNpiaiaVP4R6cbPgYUSlnQ/640?wx_fmt=png&from=appmsg)![]()![]()![...