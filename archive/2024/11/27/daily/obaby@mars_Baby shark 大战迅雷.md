---
title: Baby shark 大战迅雷
url: https://h4ck.org.cn/2024/11/18666
source: obaby@mars
date: 2024-11-27
fetch_date: 2025-10-06T19:14:35.088089
---

# Baby shark 大战迅雷

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

[微软『Windows』](https://h4ck.org.cn/cats/xtxg/wrxt)

# Baby shark 大战迅雷

2024年11月26日
[101 条评论](https://h4ck.org.cn/2024/11/18666#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG762.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG762.jpg)

晚上在电影站闲逛，想下载点新的小片片，结果，迅雷死活不给下载。

下载的时候提示：“疑似包含违规内容，无法下载”。这就 tm 离谱了，你作为一个下载工具，你 tm 关我下载什么东西呢，还疑似，疑似你妹啊。

重试几次就变成了：任务包含违规内容，无法继续下载。

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-25-212351.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-25-212351.png)

这 tm 就离谱，在我的电脑上还能让你这么猖狂？

猜测是换了路由器之后，之前有些域名屏蔽可能失效了，但是之前的规则现在也不记得了，网上随便搜一下，很多改 hosts 的方法，但是内容都是吵来吵去的，屁用没有。这就是中文互联网的处境，垃圾内容复制粘贴，连标点符号都不带改的，fuck！

既然别人的不靠谱，那就只能靠自己了，请出 baby shark ，额， 不，错了，是 wireshark。选择网卡进行抓包。

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-25-213012.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-25-213012.png)

开始有数据之后，重试几次下载，此时依然会提示无法下载。在wireshark 上面的筛选框输入 http 协议进行过滤，当然直接筛选 dns 查询也可，这里还是 http 直观。直接找 post 请求，看发送数据，左侧展开超文本传输协议内容，查看请求 host，这个就是要屏蔽的域名了。至于右侧发送的数据是啥，十六进制的，管他呢。问为什么是这个请求，问就是经验，其他的 get 都能看懂，就找不是明文的屏蔽就完了，顺便可以找下广告的域名一块给 k 了。

就是下面两行了：

```
127.0.0.1 hub5btmain.v6.shub.sandai.net
127.0.0.1 api-web-game-ssl.xunlei.com
```

再加上网上流传的那个文件内容（虽然没有屁用），拼成下面的样子，全部写入 hosts 文件，重启迅雷。

```
127.0.0.1 hub5btmain.sandai.net
127.0.0.1 hub5emu.sandai.net
127.0.0.1 upgrade.xl9.xunlei.com
127.0.0.1 hub5btmain.v6.shub.sandai.net
127.0.0.1 api-web-game-ssl.xunlei.com
```

再次开始任务就可以愉快的下载了：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-25-213237.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/Screenshot-2024-11-25-213237.png)

那个没有速度的真的是因为没有资源，😂~~，另外别好奇问这是个什么东西，问就是不知道。谁懂男人的那些恶趣味呢！~~

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Baby shark 大战迅雷》](https://h4ck.org.cn/2024/11/18666)
\* 本文链接：<https://h4ck.org.cn/2024/11/18666>
\* 短链接：<https://oba.by/?p=18666>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Wireshark](https://h4ck.org.cn/tags/wireshark)[迅雷](https://h4ck.org.cn/tags/thunder)

[Previous Post](https://h4ck.org.cn/2024/12/18679)
[Next Post](https://h4ck.org.cn/2024/11/18629)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年5月23日

#### [Glass CMD 6.1.7601.17514 fow Windows 7 SP1(64bit)](https://h4ck.org.cn/2013/05/5201)

2010年4月9日

#### [Windows 7 Bing官方主题](https://h4ck.org.cn/2010/04/1467)

2023年6月3日

#### [Delphi记事本源代码–考古向](https://h4ck.org.cn/2023/06/12251)

### 101 comments

[« 上一页](https://h4ck.org.cn/2024/11/18666/comment-page-1#comments)
[1](https://h4ck.org.cn/2024/11/18666/comment-page-1#comments)
2

1. ![](https://gg.lang.bi/avatar/266ac351c5db82a6eb4d1df913bf9da58351a5ee21f06f52ffd0d77f4ff9ce08?s=64&d=identicon&r=r) **[游钓四方](https://lhasa.icu)**说道：

   [2024年11月29日 11:01](https://h4ck.org.cn/2024/11/18666/comment-page-2#comment-121637)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Google Chrome 129](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 129") Google Chrome 129 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   牛

   [回复](#comment-121637)

   1. ![](https://gg.lang.bi/avatar/c44d885e47f3366e1926898246ecc70fc950b80314f34861521a7bad7b7af49c?s=64&d=identicon&r=r)

      [2024年12月4日 16:18](https://h4ck.org.cn/2024/11/18666/comment-page-2#comment-121779)

      ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

      ![Microsoft Edge 131](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 131") Microsoft Edge 131 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      卧槽，我在办公室要点开你的博客都是换手机打开的，一打开就学到新知识了！
      老司机就是厉害。

      [回复](#comment-121779)

      1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

         [2024年12月4日 16:21](https://h4ck.org.cn/2024/11/18666/comment-page-2#comment-121782)

         ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

         ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         老司机，带带我，哈哈哈

         [回复](#comment-121782)
2. ![](https://gg.lang.bi/avatar/950deeb4218c9ed0022292e431abf0c097f984521c4dadd7d6316402f2b273fc?s=64&d=identicon&r=r)

   [2024年11月30日 03:18](https://h4ck.org.cn/2024/11/18666/comment-page-2#comment-121641)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Microsoft Edge 131](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 131") Microsoft Edge 131 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   还能这样

   [回复](#comment-121641)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年11月30日 08:48](https://h4ck.org.cn/2024/11/18666/comment-page-2#comment-121642)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 130") Google Chrome 130 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      嗯嗯 是哒

      [回复](#comment-121642)
3. ![](https://gg.lang.bi/avatar/ec9d03ebdd1aa9658a99cca05cf659934cb824f7cc28dc290b5d344b644bcc88?s=64&d=identicon&r=r)

   [2024年11月30日 21:35](https://h4ck.org.cn/2024/11/18666/comment-page-2#comment-121644)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 129](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 129") Google Chrome 129 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这是 资源违规，若是 提示版权啥的，也能这样操作吧~

   我回头试试。先收藏了~~

   或说你这评论框的小表情整挺好，抄了抄了 ![drinks]...