---
title: 是UPS吖（二）–-群晖
url: https://h4ck.org.cn/2023/02/%e6%98%afups%e5%90%96%ef%bc%88%e4%ba%8c%ef%bc%89-%e7%be%a4%e6%99%96/
source: obaby@mars
date: 2023-02-12
fetch_date: 2025-10-04T06:25:35.698010
---

# 是UPS吖（二）–-群晖

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

[Linux『Linux』](https://h4ck.org.cn/cats/xtxg/linux%E3%80%8Elinux%E3%80%8F), [个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 是UPS吖（二）–-群晖

2023年2月11日
[4 条评论](https://h4ck.org.cn/2023/02/11167#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

开篇当然还是最喜欢的小姐姐啊。其实ups的安装还是非常简单的，不过后面的插孔都是3插，机柜上就安装了一排机柜插座，导致出现一个问题就是机柜内很多双口插头没地方插，本来想把边上的插排撤掉的，但是明显不行啊，两个光纤转换器插头+路由器+交换机的插头都没地方插，于是就把插排又给按上了。安装之后的效果就是下面这个样子啦。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-104532.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-104532.jpg)

可以看到nas的风扇上已经好多灰了，但是我真的不想清理啊。好麻烦啊，完全不想动肿么办呢。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-104803.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-104803.jpg)

机柜里的线现换过好多次了，现在基本都换成了六类网线和光纤，除了链接树莓派的网线依旧是5类网线其他的基本全部都换了。现在也不想折腾整理了，等哪天实在忍不了了再说吧。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-104949.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-104949.jpg)

前面看效果还可以叭（我能说机柜其实也是个储物柜吗）

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-105103.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-105103.jpg)

存储加各种网络设备开机负载。

**连接好数据线就可以去群晖的设置页面进行设置了**。我有两台nas，名字分别是venus和mars（我家的设备和网络都是按照太阳系命名的，是不是很有创意啊），ups和venus链接，进入venus的配置页面：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210201539.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210201539.jpg)

选择硬件和电源，切换到不断电系统，勾选启用ups支持，类型选择usb ups应用就可以了。群晖7.0以上系统没有自动关机，只有进入待机模式。我选择的是进入电池模式30秒后待机，这个时间也可以设置的稍微长一些，可以根据ups的续航进行设置。

ups的数据线只能链接一台nas，所以需要启用网络ups服务器。勾选之后点击允许的nas设备，设置ip地址（输入另一台设备的ip地址）：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210201605.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210201605.jpg)

到这里基本venus的配置就算完成了。点击设备信息可以看到当前的ups相关信息：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210201625.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210201625.jpg)

**下面进行第二台设备的配置：**

同样进入设置页面，选择synology不断电服务器，在下面的网络不断电服务器ip地址中填入venus的ip地址，其余的设置可以根据实际情况进行调整：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210201617.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210201617.jpg)

到这里设置基本就算完成啦。

拔掉电源测试一下：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-110210.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230211-110210.jpg)

30秒后就收到了进入电池模式的邮件通知，同事nas可以卸载硬盘，存储变得不可用。到这里基本设置就算完成了，由于关机需要时间，所以测试的时候可能是我刚好重新通电nas刚好关机。个人觉得群晖的设计逻辑问题不大，如果需要进入休眠模式直接关机的话可以修改系统脚本，这个我没试，需要的话可以搜索一下。到这里群晖的设置基本就结束啦。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《是UPS吖（二）–-群晖》](https://h4ck.org.cn/2023/02/11167)
\* 本文链接：<https://h4ck.org.cn/2023/02/11167>
\* 短链接：<https://oba.by/?p=11167>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[UPS](https://h4ck.org.cn/tags/ups)[群晖](https://h4ck.org.cn/tags/%E7%BE%A4%E6%99%96)

[Previous Post](https://h4ck.org.cn/2023/02/11176)
[Next Post](https://h4ck.org.cn/2023/02/11157)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2022年5月4日

#### [群辉 NAS 降级记](https://h4ck.org.cn/2022/05/10114)

2024年2月23日

#### [论持久战](https://h4ck.org.cn/2024/02/15533)

2025年4月10日

#### [虎背熊腰](https://h4ck.org.cn/2025/04/20163)

### 4 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2023年2月12日 00:32](https://h4ck.org.cn/2023/02/11167#comment-92211)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   你这个分享就比杜老师厚道多了

   [回复](#comment-92211)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年2月12日 08:36](https://h4ck.org.cn/2023/02/11167#comment-92223)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 108") Google Chrome 108 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      是吧 ![cool](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/cool.gif)

      [回复](#comment-92223)
2. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

   [2023年2月12日 15:52](https://h4ck.org.cn/2023/02/11167#comment-92230)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 110](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 110") Microsoft Edge 110 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   原来群晖可以作为UPS服务器，一会试试！

   [回复](#comment-92230)
3. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

   [2023年2月13日 14:15](https://h4ck.org.cn/2023/02/11167#comment-92250)

   ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

   ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   <https://v.qq.com/txp/iframe/player.html?vid=b0700dg78dq> ladis官方视频教程地址。

   [回复](#comment-92250)

### 发表回复 [取消回复](/2023/02/11167#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

[ ]  在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。

[x] 如果有人回复我的评论，请通过电子邮件通知我。

[x]

Δ

### 标签云[Tag Cloud]

Your browser ...