---
title: 可深度抓取网站JS文件的工具 Packer-InfoFinder
url: https://mp.weixin.qq.com/s/f93wUpkfoZo5LbJMhaYlpA
source: Doonsec's feed
date: 2026-02-25
fetch_date: 2026-02-26T04:10:44.505143
---

# 可深度抓取网站JS文件的工具 Packer-InfoFinder

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVlxdNLWKsZqiburd7je946gQvS8t8jKvyXyKSYZv35icjFNkzqJ8UjNgITqa6kleHaQkmbA2iaJ7R7ooFJRiaMiavcPHhbGSajBYp2o/0?wx_fmt=jpeg)

# 可深度抓取网站JS文件的工具 Packer-InfoFinder

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 597，阅读大约需 3 分钟

## 前言

朋友给我推荐了这个工具，说很好用。
https://github.com/TFour123/Packer-InfoFinder

![93189d369dbaed857582b6c8a93d7850.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlftsgtxBdicWGY1Hic3FdITGicjZO8NkVP1xHoYmg4ntRzMymE7EDhQMdDicRzBSAvNDoeFcXqn3DVKxyRr8VsOib8rnrmOVbyGSiaY/640?from=appmsg "null")

93189d369dbaed857582b6c8a93d7850.png

还有师傅在 issue 里专门感谢的
![9ad69e668094ab94630c902b8bfbbdb3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk1BnCibQCOGKQzauiaFpOwoKFkC2OsUHOVR3Tib6YSJ1Za0aYPlgl88PJE4Qhrk7Yc76ALCrBibCGfo7WhpjISoHSWB1SVmn0EzK8/640?from=appmsg "null")

9ad69e668094ab94630c902b8bfbbdb3.png

这下不得不安装体验一下了。

## 安装

访问 https://github.com/TFour123/Packer-InfoFinder/releases/tag/v1.5
![a0a58d2056084a812286fe620e829210.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmUUnibC96tUF7wzzbLXce3iawA06cB2MCH1AJbONGvQYtjoUkUQnE9icUtlbqVeW0JiaFErmy3TwyRhxeeYBZwc442PZeb1YdqGUI/640?from=appmsg "null")

a0a58d2056084a812286fe620e829210.png

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**安装 deno**

```
# win主机使用powershell使用命令安装
irm https://deno.land/install.ps1 | iex
# mac主机
brew install deno  安装deno
```

> Deno 是由 Node.js 的创始人 Ryan Dahl 开发的新一代 JavaScript/TypeScript 运行时环境，你可以把它理解为 **Node.js 的现代化升级版**，主要用于在浏览器之外执行 JavaScript/TypeScript 代码

![c5730101a3526ba7479ce19d66089202.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmOLotniaRibvADxlPA1ibsq715Bgq1VothPfSZa6rZxJGCCs23Qg0vLC5IibaqA65tNLbPFxw8vZDnr7WR9hdxaVTtqGzdbNBWETc/640?from=appmsg "null")

c5730101a3526ba7479ce19d66089202.png

## 使用说明

### 参数概览

```
-u, --url       目标URL
-l, --list      包含多个URL的目标文件
-c, --cookie    网站Cookie
-p, --proxy     代理地址 (例如: http://127.0.0.1:8080)
-d, --head      额外的HTTP头 (例如: 'X-Forwarded-For:127.0.0.1')
--finder        [重要] 启用JavaScript敏感信息扫描功能
-s, --silent    静默模式，只输出关键信息
```

### 使用示例

找个 webpack 打包的网站
![2eb014d6ac61911b931e2c7b1f8c968e.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkGr37HCyJzaXMtYg4aLZzbzjm9AePvvX5FibYm6fQDoXGoon52zNiaLQalLWzZHq5mmyAA5iaLCpHicic9zsWmXvdCmNsKFohGUSqY/640?from=appmsg "null")

2eb014d6ac61911b931e2c7b1f8c968e.png

**对单个目标进行 JS 文件抓取和 Webpack 还原**:

```
python Packer-InfoFinder.py -u "https://target.com"
```

把 webpack 打包的 60 个异步 JS 文件全保存到本地了
![cd89869ffa3fc77297c0c1345b4784c8.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlsaJPKQ7yLYsN8tDFeT0SdsRKAqiaJc6iaUy1MHsqgYS7I6TpQFXdWVIO4ticf9G3PMDdN8ibRtB62D10iaXIPicJJvJtDK9mVersk0/640?from=appmsg "null")

cd89869ffa3fc77297c0c1345b4784c8.png

这工具确实有东西啊。

我之前要下载未加载的 JS 文件，需要从 APP.js 等文件中找到相关的数组，然后依次拼接起来，再保存到本地，然后挨个查看。

这下直接全保存了。

**对单个目标进行完整扫描（包含敏感信息发现）**: 这是最常用的模式。扫描完成后，将在 `tmp/` 目录下生成 `finder_results` 文件夹，内含详细的 `sensitive_info.html` 报告。

```
python Packer-InfoFinder.py -u "https://target.com" --finder
```

路径下，还贴心的把 path 给我们了
![05b68242626c0b525b747e0c5bae3626.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmLdG0aN038YyHBT8cq9UMV8wiamF58X4qmMqRicN5ArhCAqGSGQN9yiaVlrjTScrzecYdo6uNicE7YqeDtdicYPHPic6XZ7Vw41feJU/640?from=appmsg "null")

05b68242626c0b525b747e0c5bae3626.png

HTML 页面
![38ac68f27b72f1783463460fc10dad0b.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlCYdnZFn1lT2974qzUJf6E6ye5AJXicMSibDiaTzCDy1W8NJ0YMvPaEkwQeQia8h05Pf4awIqPLy6EqtN0gQ5rzQz5b37uyvxJ78c/640?from=appmsg "null")

38ac68f27b72f1783463460fc10dad0b.png

**批量扫描多个目标（推荐）**: 从 `targets.txt` 文件中读取所有 URL，并对每个 URL 进行完整的敏感信息扫描。最终会在项目根目录下生成一份名为 `Finder_敏感信息总览报告.html` 的聚合报告。

```
# targets.txt:
# https://target1.com
# https://target2.com
# ...

python Packer-InfoFinder.py -l targets.txt --finder
```

**使用代理和 Cookie 进行扫描**:

```
python Packer-InfoFinder.py -u "https://internal-site.com" --finder -p "http://127.0.0.1:8080" -c "sessionid=xxxxxx"
```

## 总结

Packer-InfoFinder 用起来确实爽。

对 web 渗透测试来说，JS 可以说是极为重要的。因此，JS 文件收集的是否全面，可能就决定我们渗透项目的产出。

以后，我做 JS 信息收集时，肯定会有`Packer-InfoFinder`先过一遍了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过