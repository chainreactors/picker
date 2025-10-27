---
title: 超级自恋狂 — 定制终端 ssh 欢迎语
url: https://h4ck.org.cn/2025/02/19232
source: obaby@mars
date: 2025-02-14
fetch_date: 2025-10-06T20:33:34.690155
---

# 超级自恋狂 — 定制终端 ssh 欢迎语

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

[系统相关『OS』](https://h4ck.org.cn/cats/xtxg)

# 超级自恋狂 — 定制终端 ssh 欢迎语

2025年2月13日
[50 条评论](https://h4ck.org.cn/2025/02/19232#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/10581739427072_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/10581739427072_.pic_.jpg)

今天宝子开学了，其实这个假期她在家也没待几天。昨天折腾完浏览器控制台自定义输出之后，目光又转向了很久之前就想做，但是一直没做的终端以及 ssh 的定制输出。

这个东西简单做法非常简单，不外乎是配置 sshd 的banner 或者/etc/update-motd.d/下的相关文件，然而，我想要的不仅仅是输出几个文字那么简单，最起码要能达到类似于昨天做的控制台输出 ascii 字符画的效果。

然而，这个实现起来的确比上文提到的控制台输出要复杂的多。毕竟作为纯文本的终端系统要输出复杂字符或者直接输出图片难度还是挺大的。

最开始是想基于 neofetch 来做：

> Neofetch is a command-line system information tool written in `bash 3.2+`. Neofetch displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.
>
> The overall purpose of Neofetch is to be used in screen-shots of your system. Neofetch shows the information other people want to see. There are other tools available for proper system statistic/diagnostics.
>
> The information by default is displayed alongside your operating system’s logo. You can further configure Neofetch to instead use an image, a custom ASCII file, your wallpaper or nothing at all.
>
> You can further configure Neofetch to display exactly what you want it to. Through the use of command-line flags and the configuration file you can change existing information outputs or add your own custom ones.
>
> Neofetch supports almost 150 different operating systems. From Linux to Windows, all the way to more obscure operating systems like Minix, AIX and Haiku. If your favourite operating system is unsupported: Open up an issue and support will be added.
>
> 地址：https://github.com/dylanaraps/neofetch/

效果：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/68747470733a2f2f692e696d6775722e636f6d2f47466d433541642e706e67-600x384.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/68747470733a2f2f692e696d6775722e636f6d2f47466d433541642e706e67.png)

在实际测试的时候发现左侧的图片要想实现项目首页的这个效果，竟然无法做到，按照 wiki 的指导，支持下面的 backend：

Neofetch 3.0 included a rewrite of how we handle different modes (`image`, `ascii` and etc) which allowed us to add additional image backends to Neofetch. Neofetch now supports displaying images using [`catimg`](https://github.com/posva/catimg), [`libcaca`](http://caca.zoy.org/wiki/libcaca), [`chafa`](https://github.com/hpjansson/chafa), [`iterm2`](https://github.com/gnachman/iTerm2), [`jp2a`](https://csl.name/jp2a/), [`kitty`](https://github.com/kovidgoyal/kitty), [`pixterm`](https://github.com/eliukblau/pixterm), [`pot`](https://github.com/SeungheonOh/pot), [`libsixel`](https://github.com/saitoha/libsixel), [`termpix`](https://github.com/hopey-dishwasher/termpix), [`tycat`](https://www.enlightenment.org/about-terminology), and [`w3m`](https://github.com/tats/w3m).

然而，不管是 iterm2 还是w3m，实际实现效果都非常差。无法正常显示要加载的图片。后来发现 viu 可以在终端显示图片，然而效果嘛，看下来还是不行，不过放到终端里面，也算是能看出人形来了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250213-142342.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250213-142342.jpg)

然而，困难之处在于 neofetch 无法使用 viu 作为 backend 显示图片。

并且这个项目已经停止更新了，按照作者的说法是回家种地了。就在这个结束不久之后又出现了一堆新的 fetch。

按照评价最高的就是 fastfetch，这个东西同样支持定制化的图片输出。

> Fastfetch is a [neofetch](https://github.com/dylanaraps/neofetch)-like tool for fetching system information and displaying it prettily. It is written mainly in C, with performance and customizability in mind. Currently, Linux, Android, FreeBSD, macOS, SunOS and Windows 7+ are supported.
>
> 地址：https://github.com/fastfetch-cli/fastfetch?tab=readme-ov-file

这个东西是用 c 语言开发的，不再跟 neofetch 一样是纯 bash 脚本。至于运行效率提升，应该是有一些。

同样，看项目首页的效果还是不错的：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250213-142642.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250213-142642.jpg)

既然选定了目标，那就继续开始折腾吧。由于家里的电脑是 windows，所以选择了远程 ssh 到 ubuntu 服务器上进行配置的方式。在测试的过程中发现基于 w3m 无法在 ssh 终端中显示图像。一番搜索之后，发现了这么一个项目：

```
https://github.com/sqlsec/fastfetch/tree/main?tab=readme-ov-file
Fastfetch 是一个类似 neofetch 的工具，用于获取系统信息并漂亮地显示它。它主要用 C 语言编写，并考虑了性能和可定制性。本项目是一个 Fastfetch 轮子，主要是集成了宝可梦显示和其他系列的恶搞图片，目前只在 Linux 和 macOS 平台下测试过。
```

里面继承了一个宝可梦的字符图片生成。那么基于这个东西既然能在 ssh 中显示，那么也就是说如果能生成宝可梦类似的文本就可以正常显示所谓的图片了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/config-linux-pokemon.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/config-linux-pokemon.jpg)

上面的图片虽然模糊，但是生成一个网站 logo [![](https://h4ck.org.cn/wp-content/uploads/2025/02/logo-512.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/logo-512.png)应该是可以的。宝可梦的字符串是基于这个项目创建的：

https://gitlab.com/phoneybadger/pokemon-colorscripts.git

翻了半天代码发现，并不是通过图片生成的文本，而是本身就已经是文本：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250213-143409-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/02/Jietu20250213-143409.jpg)

这就尴尬了，也就是说通过这个项目的代码将图片转为文本已经不可能了。

google 上搜索 convert image/picture to text 或者convert image/picture to ascii,发现返回的都是 ocr 相关的内容，这该死的人工智能，现在已经没人有这种需求了吗？我是真的要讲图片转为文本，而不是要识别图片上的文本。翻了数十页，有用的信息 一条也没有。

这时突然灵光一现，直接搜索转化的文本：

```
https://www.google.com/search?q=%5B38%3B2%3B0%3B0%3B0m%E2%96%84%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B99%3B132%3B173m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84++++++++++++++++++++%0D%0A++%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B99%3B132%3B173m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B99%3B132%3B173m%1B%5B48%3B2%3B99%3B132%3B173m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B0%3B0%3B0m%E2%96%80%1B%5B0m+++++++++++++++%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B255%3B255%3B255m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B0%3B0%3B0m%E2%96%80%1B%5B0m++%0D%0A+%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B0%3B0%3B0m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B99%3B132%3B173m%1B%5B48%3B2%3B99%3B132%3B173m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B99%3B132%3B173m%1B%5B48%3B2%3B99%3B132%3B173m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B99%3B132%3B173m%1B%5B48%3B2%3B65%3B65%3B65m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B65%3B65%3B65m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B255%3B255%3B255m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B255%3B255%3B255m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B255%3B255%3B255m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B189%3B189%3B189m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B99%3B132%3B173m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84+++%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B255%3B255%3B255m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B255%3B255%3B255m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B255%3B255%3B255m%1B%5B48%3B2%3B255%3B255%3B255m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B255%3B255%3B255m%1B%5B48%3B2%3B65%3B65%3B65m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B65%3B65%3B65m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84%1B%5B38%3B2%3B0%3B0%3B0m%E2%96%84%0D%0A%1B%5B38%3B2%3B0%3B0%3B0m%1B%5B48%3B2%3B0%3B0%3B0m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B99%3B132%3B173m%1B%5B48%3B2%3B90%3B99%3B123m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B99%3B132%3B173m%1B%5B48%3B2%3B99%3B132%3B173m%E2%96%80%1B%5B0m%1B%5B38%3B2%3B99%3B132%3B173m%1B%5B48%3B2%3B65%3B65%3B65m%E2%96%80%1B%5B0m%1B%5...