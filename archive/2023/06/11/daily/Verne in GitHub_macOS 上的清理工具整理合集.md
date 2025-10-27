---
title: macOS 上的清理工具整理合集
url: https://einverne.github.io/post/2023/06/macos-cleaner-apps.html
source: Verne in GitHub
date: 2023-06-11
fetch_date: 2025-10-04T11:44:33.052772
---

# macOS 上的清理工具整理合集

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# macOS 上的清理工具整理合集

Posted on 06/10/2023
, Last modified on 06/10/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-06-10-macos-cleaner-apps.md)

最近 macOS 系统磁盘空间告急，之前就出现过因为磁盘空间不足导致系统卡顿还出现[突然黑屏](/post/2021/03/repair-macos-smc-nvram.html)的状态，所以这次就看到还剩余几十个 GB 的时候就开始清理工作了。清理的同时顺便就整理一下常用的几个清理工具。

## 如何发现大文件

在清理之前首先要对本地磁盘文件做一个整体的了解，虽然 macOS 自带一个存储管理的查看面板，但是实在是太简陋，也只能提供非常简单地查找大文件的工具。

![A14X](https://photo.einverne.info/images/2023/06/10/A14X.png)

比如说从系统提供的 Storage 预览中能看到 Documents 占用的空间最多，可以点开后面的圆形 i 图标，可以看到其中占用空间很大的几个文件。

![ACei](https://photo.einverne.info/images/2023/06/10/ACei.png)

比如说对于我，就是我安装的两个虚拟机占用了比较多的空间，但这也是预想之内的。

### gdu

上面的方式只能找出来系统中的大文件所在，如果我想知道每一个文件夹所占用的空间大小，我之前的文章中介绍过[gdu](/post/2021/07/gdu-fast-disk-usage-analyzer.html) ，这个时候就派上了用场。

```
brew install gdu
```

然后直接对想要统计的目录运行 `sudo gdu ~/`

![ARx8](https://photo.einverne.info/images/2023/06/10/ARx8.png)

## 几款 macOS 上的清理工具

* [[Clean My Mac]] 收费软件
* [[Pretty Clean]] [Pretty Clean](https://pretty-clean.github.io/) 免费
* [[App Cleaner]] 免费，卸载应用
* [[Clean Me]] [Clean Me](https://kevin-de-koninck.github.io/Clean-Me/) 是一款开源的清理磁盘工具

## Pretty Clean

[PrettyClean](https://www.prettyclean.cc/) 是一款 macOS 上的免费清理工具，界面非常简单。

![AW10](https://photo.einverne.info/images/2023/06/10/AW10.jpg)

## App Cleaner

[App Cleaner](https://freemacsoft.net/appcleaner/) 是一款可以用来快速卸载应用以及应用相关残留文件的应用，非常小巧，但是非常强大。

![AdJ6](https://photo.einverne.info/images/2023/06/10/AdJ6.png)

## 脚本

* [mac-cleanup-py](https://github.com/mac-cleanup/mac-cleanup-py) 是一个使用 Python 编写的 macOS 上的清理脚本。

## Related Posts

* [VibeTunnel 将终端带到浏览器 开启移动化 Vibe Coding](/post/2025/08/vibetunnel.html) - 08/12/2025
* [macOS 上的多栏文件管理器 QSpace](/post/2024/07/qspace-multi-pane-finder.html) - 07/30/2024
* [macOS 迁移助手迁移后 Syncthing 设备 ID 相同问题解决方案](/post/2024/07/after-macos-migration-syncthing-id-sama-solution.html) - 07/10/2024
* [借助 BLEUnlock 实现 macOS 自动锁定](/post/2024/03/mac-lock-screen-bleunlock.html) - 03/02/2024
* [修复 macOS 时区和时间错误](/post/2023/11/macos-wrong-datetime-zone.html) - 11/16/2023
* [我买了一台 Mac mini 以及记录一下 Mac mini 初始化设定](/post/2023/11/i-bought-mac-mini-and-setup.html) - 11/12/2023
* [macOS 上的清理工具整理合集](/post/2023/06/macos-cleaner-apps.html) - 06/10/2023
* [macOS 上好用的 ChatGPT 客户端整理](/post/2023/06/macos-chatgpt-app.html) - 06/03/2023
* [macOS 上轻便的 Docker 容器以及 Linux 运行环境：OrbStack](/post/2023/03/orbstack-docker-runtime-and-virtual-linux.html) - 03/28/2023
* [解决 Clash for Windows 节点测速 timeout 问题](/post/2022/09/clash-for-windows-timeout.html) - 09/30/2022
* [从 mkv 文件中提取字幕文件](/post/2022/07/extract-subtitle-from-mkv.html) - 07/31/2022
* [图片压缩工具 Squoosh 离线版](/post/2022/04/squoosh-desktop-version.html) - 04/28/2022
* [Linux 下 journal 日志清理](/post/2021/11/linux-journal-size.html) - 11/29/2021
* [espanso：Rust 编写的跨平台开源文本扩展工具](/post/2021/09/espanso-text-expand.html) - 09/17/2021
* [macOS 间歇性休息提醒应用：Time out](/post/2021/08/mac-app-time-out.html) - 08/24/2021
* [使用 gdu 快速查看磁盘空间占用](/post/2021/07/gdu-fast-disk-usage-analyzer.html) - 07/16/2021
* [手工编译安装 macOS 下的 Rime（鼠须管）](/post/2021/07/manully-build-rime-squirrel-for-mac.html) - 07/11/2021
* [手工编译安装 librime](/post/2021/07/build-librime-from-source-for-mac.html) - 07/02/2021
* [使用了半年 macOS 之后 我又回到了 Linux 的怀抱](/post/2021/03/come-back-to-linux-after-using-macos-half-an-year.html) - 03/31/2021
* [在 Linux 上使用 Clash 作代理](/post/2021/03/linux-use-clash.html) - 03/15/2021
* [WhatPulse 使用记录](/post/2021/01/whatpulse-usage.html) - 01/10/2021
* [『译』我最喜欢的命令行工具](/post/2020/10/my-favorite-cli-tools.html) - 10/30/2020
* [跨平台的 GPU 加速终端 kitty](/post/2020/08/cross-platform-gpu-based-terminal-emulator-kitty.html) - 08/27/2020
* [使用 dotbot 管理 dotfiles 配置文件](/post/2020/08/use-dotbot-dotfiles-management.html) - 08/15/2020
* [使用 asdf-vm 管理编程语言多个版本](/post/2020/04/asdf-vm-manage-multiple-language.html) - 04/25/2020
* [清理 macOS 磁盘](/post/2020/03/clean-up-mac-other-storage.html) - 03/01/2020
* [每天学习一个命令：du 找出哪个文件夹占用空间](/post/2018/03/du-find-out-which-fold-take-space.html) - 03/04/2018
* [v2ray 使用和总结](/post/2018/01/v2ray.html) - 01/26/2018
* [Vim 中不同模式间的切换](/post/2015/05/vim-mode-switch.html) - 05/05/2015

---

* [← Previous（前一篇）](/post/2023/06/listmonk-open-source-newsletter-mailing-list-manager.html "使用 Listmonk 搭建自己的 Newsletter")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/06/xml-signature.html "XML 数字签名及 Java 实现")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/06/macos-cleaner-apps.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [整理合集 64](/categories.html#整理合集)

* [macos 49](/tags.html#macos)
* [cleanup 1](/tags.html#cleanup)
* [mac 24](/tags.html#mac)
* [gdu 3](/tags.html#gdu)
* [linux 435](/tags.html#linux)
* [disk-space 3](/tags.html#disk-space)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").