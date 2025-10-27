---
title: FeelUOwn，一款开发了 8 年的音乐播放器 - V2EX
url: https://buaq.net/go-140484.html
source: unSafe.sh - 不安全
date: 2022-12-19
fetch_date: 2025-10-04T01:53:12.701658
---

# FeelUOwn，一款开发了 8 年的音乐播放器 - V2EX

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/3f72372f8437e6e13ad462453b40cdfe.jpg)

FeelUOwn，一款开发了 8 年的音乐播放器 - V2EX

开发了 8 年，都有点啥 特性 ？21 世纪 10~20 年代播放器都有的：支持多音源，比如网抑云，酷我，哔哩哔哩等21 世纪 20 年代播放器即将都有的：看视频听歌有图有真相。看视频必须得有
*2022-12-18 18:18:21
Author: [v2ex.com(查看原文)](/jump-140484.htm)
阅读量:77
收藏*

---

## 开发了 8 年，都有点啥 **特性** ？

### 21 世纪 10~20 年代播放器都有的：支持多音源，比如网抑云，酷我，哔哩哔哩等

![image](https://user-images.githubusercontent.com/4962134/208276950-0914e42e-7b04-455c-815e-34556d86192c.png)

### 21 世纪 20 年代播放器即将都有的：看视频听歌

有图有真相。看视频必须得有画中画，这不就可以边发帖，边看视频了。
![image](https://user-images.githubusercontent.com/4962134/208279258-8f082fad-462d-448c-8bc8-ddc6ac48f972.png)

### 20 世纪软件都有的：一切皆文本

* 基于文本的歌单，方便与朋友分享、设备之间同步

```
+++
title = "Library"
updated = 2022-11-30T02:02:20.386310
+++
fuo://netease/songs/115794      # 一生不变 - 李克勤 - Purple Dream - 04:22
fuo://netease/songs/330107      # 自作多情 - 周慧敏 - 冬日浪漫 - 05:22
fuo://netease/songs/4874121     # 我们的纪念 - 李雅微 - 放羊的星星 电视原声带 - 04:25
fuo://netease/songs/4875127   # 美丽的神话Ⅰ - 成龙 & 金喜善 - 神话 电影原声带 - 04:50
```

* 提供基于 TCP 的交互控制协议

```
$ fuo play 沧海一声笑
select: fuo://netease/songs/170749          # 沧海一声笑 - 许冠杰 - 沧海一声笑 - 02:55
options::
        fuo://kuwo/songs/26413118           # 沧海一声笑 - 那英&周杰...
        fuo://bilibili/songs/BV13y4y157GB   #  [ 4K60FPS ] 黄霑《沧海一声笑》...
```

* 类似 `.vimrc` 和 `.emacs` 的配置文件 `.fuorc`

```
就不展示了，嘿嘿！可以点下面这个链接
```

<https://github.com/cosven/rcfiles/blob/master/fuorc>

## 有木有想试用一下？

### 安装使用

Arch Linux

```
yay -S feeluown          # 安装稳定版，最新版的包名为 feeluown-git
yay -S feeluown-netease  # 按需安装其它扩展
yay -S feeluown-kuwo
yay -S feeluown-qqmusic
yay -S feeluown-bilibili
```

macOS

```
brew tap feeluown/feeluown
brew install feeluown --with-battery # 安装 FeelUOwn 以及扩展
feeluown genicon                     # 在桌面生成 FeelUOwn 图标
```

FeelUOwn 是用 Python3 + PyQt5 + mpv 开发的，因此基本上所有系统都可以运行，比如 Windows, Gentoo, NixOS 等。你可以在这个文档上查找到合适的方法 <https://feeluown.readthedocs.io/en/latest/quickstart.html> 。

### 来来来

* 项目： <https://github.com/feeluown/FeelUOwn>
* 交流群：[telegram 交流群](https://t.me/joinchat/H7k12hG5HYsGy7RVvK_Dwg)
* 文档（安装使用 /开发）： <https://feeluown.readthedocs.io/>

文章来源: https://v2ex.com/t/903258#reply5
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)