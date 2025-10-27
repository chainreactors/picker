---
title: 哪吒监控-多服务器监控与运维工具
url: https://h4ck.org.cn/2024/11/18524
source: obaby@mars
date: 2024-11-15
fetch_date: 2025-10-06T19:17:13.389053
---

# 哪吒监控-多服务器监控与运维工具

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

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# 哪吒监控-多服务器监控与运维工具

2024年11月14日
[86 条评论](https://h4ck.org.cn/2024/11/18524#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG710.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG710.jpg)

前几天在[杜老师](https://chat.dusays.com/dusays/channels/town-square)的聊天室，聊到那些闲着没事到处攻击人的 cc 狗的问题。[杜老师](https://dusays.com)扔出来一个链接，并且说道：可以装个监控玩玩，看实时流量神马的。

于是呢，请杜老师写个教程：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-131902.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-131902.jpg)

杜老师信誓旦旦，表示晚上八点二十发。然后呢，我等了好几个八点二十了也没看到。虽然昨晚杜老师更新了一篇，但是不是教程，哼唧唧。就离谱啊。

终于，实在忍不住了，然后自己照着官网的文档直接安装了一套：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-132148.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-132148.jpg)

**果然男人都靠不整，哼。**

具体教程还是等杜老师更新吧，我就不写了。

不过，在安装过程中发现一个问题，不知道是兼容信问题还是神马问题。在 ubuntu 20.04上，通过独立安装的面板，无法正常启动服务，所以建议还是直接 docker 安装，如果是这个系统的话，安装倒是也简单，一行命令，傻瓜式操作：

```
curl -L https://gitee.com/naibahq/scripts/raw/main/install.sh -o nezha.sh && chmod +x nezha.sh && sudo CN=true ./nezha.sh
```

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-132515.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-132515.jpg)

剩下的各种配置就更傻瓜化了，不过安装之后发现一个问题。就是自己的网站首页没有 favicon 的小图标，但是杜老师的有：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-132620.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-132620.jpg)

要解决这个问题也简单，后台修改前台自定义 css，添加以下代码：

```
<link rel="icon" type="image/x-icon" href="https://s.h4ck.org.cn/static/logo.svg?v20210804">
<link rel="apple-touch-icon" sizes="180x180" href="https://s.h4ck.org.cn/static/logo.svg?v20210804">
```

然后就促来啦：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-132840.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241114-132840.jpg)

完美，嘻嘻。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《哪吒监控-多服务器监控与运维工具》](https://h4ck.org.cn/2024/11/18524)
\* 本文链接：<https://h4ck.org.cn/2024/11/18524>
\* 短链接：<https://oba.by/?p=18524>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[哪吒监控](https://h4ck.org.cn/tags/%E5%93%AA%E5%90%92%E7%9B%91%E6%8E%A7)[服务器监控](https://h4ck.org.cn/tags/%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%9B%91%E6%8E%A7)

[Previous Post](https://h4ck.org.cn/2024/11/18537)
[Next Post](https://h4ck.org.cn/2024/11/18518)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2025年4月2日

#### [南墙 WAF 系列（一）– 管理后台证书自动更新](https://h4ck.org.cn/2025/04/20074)

2024年2月21日

#### [django Celery 的几个异常](https://h4ck.org.cn/2024/02/15510)

2023年9月27日

#### [DAYI.MA（闺蜜圈）– 后台开发进度](https://h4ck.org.cn/2023/09/13453)

### 86 comments

[« 上一页](https://h4ck.org.cn/2024/11/18524/comment-page-1#comments)
[1](https://h4ck.org.cn/2024/11/18524/comment-page-1#comments)
2

1. ![](https://gg.lang.bi/avatar/f708fe332792fb965837fec42b58154ece68b3d2d608dfb006b39535a2a901ba?s=64&d=identicon&r=r) **[段先森](https://www.duanxiansen.com/)**说道：

   [2024年11月16日 13:10](https://h4ck.org.cn/2024/11/18524/comment-page-2#comment-121159)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 119](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 119") Microsoft Edge 119 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这就是自己动手，丰衣足食嘛。哈哈哈

   [回复](#comment-121159)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年11月16日 14:42](https://h4ck.org.cn/2024/11/18524/comment-page-2#comment-121160)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      嗯嗯，是哒

      [回复](#comment-121160)
2. ![](https://gg.lang.bi/avatar/40c46b2a6ef05464946a7e3f5230bdfa16b5d4e861c7b69977ef77efde66638a?s=64&d=identicon&r=r)

   [2024年11月16日 15:13](https://h4ck.org.cn/2024/11/18524/comment-page-2#comment-121161)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Chrome 130") Chrome 130 ![iPhone iOS 18.0](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 18.0") iPhone iOS 18.0 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   滴，已学

   [回复](#comment-121161)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年11月16日 17:18](https://h4ck.org.cn/2024/11/18524/comment-page-2#comment-121164)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      滴，技能+1

      [回复](#comment-121164)
3. ![](https://gg.lang.bi/avatar/2ee7324fec3f0f214b85c596c2affecd8ed9356138e1673c963fe5ce3e284a27?s=64&d=identicon&r=r)

   [2024年11月17日 18:49](https://h4ck.org.cn/2024/11/18524/comment-page-2#comment-121214)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 2](https://badgen.net/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Google Chrome 86](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 86") Google Chrome 86 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   你这是一个站一台机器吗？那不是很麻烦管理起来

   [回复](#comment-121214)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年11月18日 09:06](https://h4ck.org.cn/2024/11/18524/comment-page-2#comment-121220)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https:/...