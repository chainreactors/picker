---
title: 定制博客开发者工具控制台个性化输出
url: https://h4ck.org.cn/2025/02/19219
source: obaby@mars
date: 2025-02-13
fetch_date: 2025-10-06T20:34:01.892871
---

# 定制博客开发者工具控制台个性化输出

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

[前端开发『FrontEnd』](https://h4ck.org.cn/cats/cxsj/%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%E3%80%8Efrontend%E3%80%8F)

# 定制博客开发者工具控制台个性化输出

2025年2月12日
[56 条评论](https://h4ck.org.cn/2025/02/19219#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/WechatIMG1044.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/WechatIMG1044.jpg)

首先祝大家元宵节快乐啊，其实这个东西也不是什么新奇玩意儿了。

很多网站都有这个东西，例如百度：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250212-131456-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250212-131456.jpg)

但是就输出这么个东西明显不够高级的样子，上午访问![小小](https://g.h4ck.org.cn/avatar/7f037a4674a363c65e07b1f2853091a9?s=64&d=mm&r=g)[**小小的小**](https://www.one21.cn/)的博客，发现他的主题自带的输出还是蛮有意思的：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250212-093125-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250212-093125.jpg)

既然如此，俺就不如直接抄过来了：

```
            <script>
                // 消除控制台打印
                var HoldLog = console.log;
                console.log = function() {}
                ;
                let now1 = new Date();
                queueMicrotask( () => {
                    const Log = function() {
                        HoldLog.apply(console, arguments);
                    };
                    //在恢复前输出日志
                    const grt = new Date("08/10/2009 00:00:00");
                    //此处修改你的建站时间或者网站上线时间
                    now1.setTime(now1.getTime() + 250);
                    const days = (now1 - grt) / 1000 / 60 / 60 / 24;
                    const dnum = Math.floor(days);
                    const ascll = [`欢迎访问obaby@mars!`, `爱自己，每天都要开开心心的哦`, `
 ██████  ██████   █████  ██████  ██    ██  ██████  ███    ███  █████  ██████  ███████
██    ██ ██   ██ ██   ██ ██   ██  ██  ██  ██    ██ ████  ████ ██   ██ ██   ██ ██
██    ██ ██████  ███████ ██████    ████   ██ ██ ██ ██ ████ ██ ███████ ██████  ███████
██    ██ ██   ██ ██   ██ ██   ██    ██    ██ ██ ██ ██  ██  ██ ██   ██ ██   ██      ██
 ██████  ██████  ██   ██ ██████     ██     █ ████  ██      ██ ██   ██ ██   ██ ███████
        `, "已上线", dnum, "天", "©2025 By obaby@mars V1.8.16", ];
                    const ascll2 = [`NCC2-036`, `调用前置摄像头拍照成功，识别为【小笨蛋】.`, `Photo captured: `, `🤪`];

                    setTimeout(Log.bind(console, `\n%c${ascll[0]} %c ${ascll[1]} %c ${ascll[2]} %c${ascll[3]}%c ${ascll[4]}%c ${ascll[5]}\n\n%c ${ascll[6]}\n`, "color:#425AEF", "", "color:#ff4f87", "color:#425AEF", "", "color:#425AEF", ""));
                    setTimeout(Log.bind(console, `%c ${ascll2[0]} %c ${ascll2[1]} %c \n${ascll2[2]} %c\n${ascll2[3]}\n`, "color:white; background-color:#4fd953", "", "", 'background:url("https://npm.elemecdn.com/anzhiyu-blog@1.1.6/img/post/common/tinggge.gif") no-repeat;font-size:450%'));

                    setTimeout(Log.bind(console, "%c WELCOME %c 你好，小笨蛋.", "color:white; background-color:#4f90d9", ""));

                    setTimeout(console.warn.bind(console, "%c ⚡ Powered by obaby@mars %c 你正在访问 小妖精 的博客.", "color:white; background-color:#f0ad4e", ""));
                    setTimeout(console.warn.bind(console, "%c ❶ Blog: %c https://oba.by", "color:white; background-color:#ff7aa4", ""));
                    setTimeout(console.warn.bind(console, "%c ❷ Blog: %c https://nai.dog", "color:white; background-color:#ff7aa4", ""));
                    setTimeout(console.warn.bind(console, "%c ❸ Blog: %c https://zhongxiaojie.com", "color:white; background-color:#ff7aa4", ""));
                    setTimeout(console.warn.bind(console, "%c ❹ Blog: %c https://h4ck.org.cn", "color:white; background-color:#ff7aa4", ""));
                    setTimeout(Log.bind(console, "%c W23-12 %c 你已打开控制台.", "color:white; background-color:#4f90d9", ""));

                    setTimeout(console.warn.bind(console, "%c S013-782 %c 你现在正处于监控中，不要干坏事哦.", "color:white; background-color:#d9534f", ""));
                }
                );
            </script>
```

至于怎么生成上面的 ascii 字符串，可以使用下面的两个链接：

[https://patorjk.com/software/taag/](https://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=obaby%40mars)

<http://www.network-science.de/ascii/>

把上面的代码找个 js 文件写进而去，在页面 header 里面引用即可（我直接将代码添加到了 wp 的页面小工具内）。实际效果：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/image-3.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/image-3.png)

当然也可以直接 F12 打开开发者工具查看具体效果。嘎嘎。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《定制博客开发者工具控制台个性化输出》](https://h4ck.org.cn/2025/02/19219)
\* 本文链接：<https://h4ck.org.cn/2025/02/19219>
\* 短链接：<https://oba.by/?p=19219>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[博客](https://h4ck.org.cn/tags/%E5%8D%9A%E5%AE%A2)[开发者工具](https://h4ck.org.cn/tags/%E5%BC%80%E5%8F%91%E8%80%85%E5%B7%A5%E5%85%B7)

[Previous Post](https://h4ck.org.cn/2025/02/19232)
[Next Post](https://h4ck.org.cn/2025/02/19188)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年5月22日

#### [AI，还是AI？](https://h4ck.org.cn/2024/05/17138)

2024年6月22日

#### [黔驴技穷 — 山穷水复疑无路 柳暗花明又一村](https://h4ck.org.cn/2024/06/17385)

2022年9月8日

#### [中文域名体验记](https://h4ck.org.cn/2022/09/10450)

### 56 comments

1. ![](https://gg.lang.bi/avatar/7ca2eb6a07de78fd08989205bc741ef66a4746b1f518fa164f8e71b016366c75?s=64&d=identicon&r=r) **[网友小宋](https://xyzbz.cn)**说道：

   [2025年2月12日 13:41](https://h4ck.org.cn/2025/02/19219#comment-123593)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 132](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 132") Microsoft Edge 132 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   哈哈 挺有意思的。

   [回复](#comment-123593)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年2月12日 14:10](https://h4ck.org.cn/2025/02/19219#comment-123594)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 130") Google Chrome 130 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      嗯嗯 这个纯粹就一个作用 好玩 哈哈哈😉

      [回复](#comment-123594)
2. ![](https://gg.lang.bi/avatar/d23fcc881cf4225d42965fd5f44cfc87de900fc7693b01921f0f4636199eb998?s=64&d=identicon&r=r)

   [2025年2月12日 14:43](https://h4ck.org.cn/2025/02/19219#comment-123598)

   ![Level 2](https://badgen.net/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Firefox 135](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 135") Firefox 135 ![Mac OS X 10.15](https://h4ck.org.cn/wp-...