---
title: Mac 微信最新版多开脚本
url: https://h4ck.org.cn/2025/08/21289
source: obaby@mars
date: 2025-08-15
fetch_date: 2025-10-07T00:17:33.953172
---

# Mac 微信最新版多开脚本

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

[Mac OSX『Mac OS』](https://h4ck.org.cn/cats/xtxg/mac-osx%E3%80%8Emac-os%E3%80%8F)

# Mac 微信最新版多开脚本

2025年8月14日
[53 条评论](https://h4ck.org.cn/2025/08/21289#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250814092706_43.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250814092706_43.jpg)

这次微信更新，我也不记得是什么时候了，可能是上周，或者是更早一些？之所以忘了是因为最近电脑上就登录了一个微信，另外一个微信已经好久没登录了。

今天早上习惯性的运行了一下以前写的那个脚本，结果执行完了之后，没有打开另外一个微信窗口而是直接切换到了已经开启的微信窗口：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/UserszhongmingPicturespersonalJietu20250814-093159.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/UserszhongmingPicturespersonalJietu20250814-093159.jpg)

额，这尼玛就有意思了。

以前也试过所谓的插件 hook 的形式，但是一直效果不怎么样，所以就采用了最简单粗暴的办法，那个 启动微信呢脚本也很简单，就一行代码：

```
nohup /Applications/WeChat.app/Contents/MacOS/WeChat > /dev/null 2>&1
```

现在看来，这行代码不行了。这就尴尬啦，该怎么搞呢，其实最简单的方法就是直接复制个微信出来，改下 bundleid，对文件重新签名，这样就有两个不同的 app 了。

但是，一想到这么多步骤，还要执行命令一条条的就觉得蛋疼，还是直接上 cursor 写个脚本，哈哈哈。执行下试试效果：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-093806.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-093806.jpg)

支持的参数：

```
 sudo sh baby_wechat.sh
-e 微信双开脚本使用说明:

-e 用法:
  baby_wechat.sh [选项]

-e 选项:
  setup         设置微信双开环境（创建WeChat2.app）
  start         启动微信双开
  auto          自动设置并启动微信双开
  -s            显示当前运行的微信进程
  -k            关闭所有微信进程
  -h            显示此帮助信息

-e 示例:
  baby_wechat.sh setup       # 设置微信双开环境
  baby_wechat.sh start       # 启动微信双开
  baby_wechat.sh auto        # 自动设置并启动微信双开
  baby_wechat.sh -s          # 显示运行中的微信进程
  baby_wechat.sh -k          # 关闭所有微信进程

-e 注意:
  首次使用建议运行 'baby_wechat.sh auto' 来自动完成所有设置
  需要管理员权限来创建和修改应用
  需要安装 Xcode 命令行工具
```

执行完之后就看到效果啦：

luancher 有两个微信：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-093957.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-093957.jpg)

两个微信可以单独启动，进行登录：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-091435.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-091435.jpg)

版本信息：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-091738.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-091738.jpg)

问题是为什么不能学 qq 呢，天然支持多账号登录，哼！

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-093659-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250814-093659.jpg)

相关脚本已经开源了，访问 github 查看，下载使用：

<https://github.com/obaby/baby-wechat>

无法访问的使用下面的地址：

<https://gitee.com/obaby/baby-wechat>

**免责声明: 本脚本仅供学习和研究使用。使用本脚本产生的任何后果由用户自行承担。**

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Mac 微信最新版多开脚本》](https://h4ck.org.cn/2025/08/21289)
\* 本文链接：<https://h4ck.org.cn/2025/08/21289>
\* 短链接：<https://oba.by/?p=21289>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[macos](https://h4ck.org.cn/tags/macos)[多开](https://h4ck.org.cn/tags/%E5%A4%9A%E5%BC%80)[微信](https://h4ck.org.cn/tags/%E5%BE%AE%E4%BF%A1)

[Previous Post](https://h4ck.org.cn/2025/08/21321)
[Next Post](https://h4ck.org.cn/2025/08/21261)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2018年7月26日

#### [mac pip权限问题 mac OSX pip OSError: [Errno 1] Operation not permitted](https://h4ck.org.cn/2018/07/6223)

2018年1月3日

#### [也谈微信 跳一跳 外挂](https://h4ck.org.cn/2018/01/6061)

2020年6月4日

#### [iOS 签名杂谈（一）](https://h4ck.org.cn/2020/06/7112)

### 53 comments

1. ![](https://gg.lang.bi/avatar/19a53855a6616e2ead18670b736d1917a8b5dbe3f22d629e637d9e3f384e451f?s=64&d=identicon&r=r) **[小彦](https://note-star.cn/)**说道：

   [2025年8月14日 10:50](https://h4ck.org.cn/2025/08/21289#comment-127886)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![WebView 4](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/android-webkit.png "WebView 4") WebView 4 ![Android 15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 15") Android 15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   不错，电脑微信要切换账号好麻烦，而且聊天记录不是连续的

   [回复](#comment-127886)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年8月14日 11:25](https://h4ck.org.cn/2025/08/21289#comment-127889)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      是的，这点就很垃圾，记录不连续。

      [回复](#comment-127889)
   2. ![](https://gg.lang.bi/avatar/b8988a975c704d67b3fe29316a8314fd33d3581287414b9c43e56c34f9d79d1e?s=64&d=identicon&r=r)

      [2025年8月14日 15:32](https://h4ck.org.cn/2025/08/21289#comment-127903)

      ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

      ![Microsoft Edge 139](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 139") Microsoft Edge 139 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      windows的可以写一个.bat脚本
      @echo off

      start “” “D:\APP\WeiXin\Weixin\Weixin.exe”

      start “” “D:\APP\WeiXin\Weixin\Weixin.exe”

      exit
      里面改成自己微信的路径，想要多开几个就复制几行就ok了

      [回复](#comment-127903)

      1. ![](https://gg.lang.bi/avatar/19a53855a6616e2ead18670b736d1917a8b5dbe3f22d629e637d9e3f384e451f?s=64&d=identicon&r=r)

         [2025年8月14日 15:47](https://h4ck.org.cn/2025/08/21289#comment-127904)

         ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

         ![WebView 4](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/android-webkit.png "WebView 4") WebView 4 ![Android 15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 15") Android 15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         这样，我试试~

         [回复](#comment-127904)
2. ![](https://gg.lang.bi/avatar/5d3b04c9c4a8b58d5049988184be392b3ce6141900a0f9295c2e4fbee234c9cd?s=64&d=identicon&r=r)

   [2025年8月14日 11:10](https://h4ck.org.cn/2025/08/21289#comment-127887)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Safari 18](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 18") Safari 18 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X ...