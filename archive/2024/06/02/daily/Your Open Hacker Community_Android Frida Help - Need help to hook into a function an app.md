---
title: Android Frida Help - Need help to hook into a function an app
url: https://www.reddit.com/r/HowToHack/comments/1d5h1fq/android_frida_help_need_help_to_hook_into_a/
source: Your Open Hacker Community
date: 2024-06-02
fetch_date: 2025-10-06T16:56:04.535798
---

# Android Frida Help - Need help to hook into a function an app

[跳到主要内容](#main-content)

打开菜单
打开导航

前往 Reddit 主页

r/HowToHack
A chip

A close button

[登录](https://www.reddit.com/login/)登录 Reddit

展开用户菜单
打开设置菜单

[![r/HowToHack 图标](https://styles.redditmedia.com/t5_2uxyh/styles/communityIcon_sjak3ovn3qtc1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=60deb89b51148be32456b72f023ef962333cb264)

转到“HowToHack”](/r/HowToHack/)

[r/HowToHack](/r/HowToHack/)

![subreddit 的横幅](https://styles.redditmedia.com/t5_2uxyh/styles/bannerBackgroundImage_u92cjw2h2qtc1.png)

![r/HowToHack 图标](https://styles.redditmedia.com/t5_2uxyh/styles/communityIcon_sjak3ovn3qtc1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=60deb89b51148be32456b72f023ef962333cb264)

[r/HowToHack](/r/HowToHack/)

Welcome! This is your open hacker community designed to help you on the journey from neophyte to veteran in the world of underground skillsets. Ask, Answer, Learn.
Visit us on discord
https://discord.gg/ep2uKUG

---

成员数

在线人数

•

[sky\_high993](/user/sky_high993/)

# Android Frida Help - Need help to hook into a function an app

[hacking](/r/HowToHack/?f=flair_name%3A%22hacking%22)

Hello , I am a beginner and would like your help -
I am having trouble hooking to a function in an android app. it is running, but the hook is not triggered.

```
package defpackage;

public final class cpq implements n6n, w2j.a, tlh {

...

public static final boolean W() {

        return du9.b().b("reply_voting_android_enabled", false);

    }
...
}
```

With frida I used the script : **run\_frida\_script.py**

```
import frida

package_name = "com.twitter.android"

device = frida.get_usb_device()
pid = device.spawn([package_name])
session = device.attach(pid)
script = session.create_script(open("hook_to_function.js").read())
script.load()
device.resume(pid)

# Prevent the script from terminating
input()
```

With the javascript : **hook\_to\_function.js**

```
Java.perform(function() {

    var cpqClass = Java.use("defpackage.cpq");

    cpqClass.W.implementation = function() {
        console.log('defpackage.cpq.W was called');
        send('defpackage.cpq.W was called');
        var result = this.W();
        console.log('Result: ' + result);
        return result;
    };

});
```

In the terminal I ran:

```
python run_frida_script.py com.twitter.android hook_to_function.js
```

* I have tested Frida the hooking to the process of the app, and it was successful.

Thank you for reading and for your help .

阅读更多内容

 共享

是 Reddit 新用户？

创建账户，畅游精彩的社区世界。

通过电子邮件地址继续

通过手机号继续

继续操作即表示您同意我们的
[用户协议](https://www.redditinc.com/policies/user-agreement)
并确认您已了解
[隐私政策](https://www.redditinc.com/policies/privacy-policy).

公共

任何人均可在此社区中浏览内容、发帖和评论

0
0

## 热门帖子

---

* [Reddit

  reReddit：2024年6月1日的热门帖子

  ---](https://www.reddit.com/posts/2024/june-1-1/global/)
* [Reddit

  reReddit：2024年6月的热门帖子

  ---](https://www.reddit.com/posts/2024/june/global/)
* [Reddit

  reReddit：2024年的热门帖子

  ---](https://www.reddit.com/posts/2024/global/)

[Reddit 规则](https://www.redditinc.com/policies/content-policy)

[隐私政策](https://www.reddit.com/policies/privacy-policy)

[用户协议](https://www.redditinc.com/policies/user-agreement)

[辅助功能](https://support.reddithelp.com/hc/sections/38303584022676-Accessibility)
[Reddit, Inc. © 2025。保留所有权利。](https://redditinc.com)

展开“导航”

折叠“导航”

![](https://id.rlcdn.com/472486.gif)