---
title: 解决Xcode：Unable to boot device because it cannot be located on disk.
url: https://www.uedbox.com/post/69703/
source: 体验盒子
date: 2024-09-05
fetch_date: 2025-10-06T18:26:39.793104
---

# 解决Xcode：Unable to boot device because it cannot be located on disk.

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# 解决Xcode：Unable to boot device because it cannot be located on disk.

* 发表于 2024年09月04日
* [macOS](https://www.uedbox.com/entertainment/macos/)

目录表

Toggle

* [报错](#%E6%8A%A5%E9%94%99)
* [解决](#%E8%A7%A3%E5%86%B3)

## 报错

**Unable to boot device because it cannot be located on disk.**

原因分析：清理过模拟器数据，错误挂起或异常停。停止所有模拟器并重置就行：

## 解决

在命令行终端运行

|  |  |
| --- | --- |
| 1 | xcrun simctl shutdown all && xcrun simctl erase all |

现在再打开模拟器，正常了！

点赞(3)

打赏

分享

标签：[Xcode](https://www.uedbox.com/post/tag/xcode/)  原文连接：**[解决Xcode：Unable to boot device because it cannot be located on disk.](https://www.uedbox.com/post/69703/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[Flutter使用JsBridge方式处理Webview与H5通信](https://www.uedbox.com/post/69699/ "Flutter使用JsBridge方式处理Webview与H5通信") [2025免费在线影视/动漫番剧优质网站，合集汇总更新](https://www.uedbox.com/post/69704/ "2025免费在线影视/动漫番剧优质网站，合集汇总更新")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![Xcode 无法找到和创建 iOS Simulators](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Xcode 无法找到和创建 iOS Simulators](https://www.uedbox.com/post/69465/ "Xcode 无法找到和创建 iOS Simulators")

[![更新Xcode提示空间不足“Not enough free space”解决](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

更新Xcode提示空间不足“Not enough free space”解决](https://www.uedbox.com/post/66475/ "更新Xcode提示空间不足“Not enough free space”解决")

[![Can’t build Flutter application: Unable to locate DeviceSupport directory解决](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Can’t build Flutter application: Unable to locate DeviceSupport directory解决](https://www.uedbox.com/post/66881/ "Can’t build Flutter application: Unable to locate DeviceSupport directory解决")

[![Command CompileSwift failed with a nonzero exit code解决](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Command CompileSwift failed with a nonzero exit code解决](https://www.uedbox.com/post/66979/ "Command CompileSwift failed with a nonzero exit code解决")

[![iPhone is busy: Preparing debugger support for iPhone解决办法](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

iPhone is busy: Preparing debugger support for iPhone解决办法](https://www.uedbox.com/post/68582/ "iPhone is busy: Preparing debugger support for iPhone解决办法")

[![Xcode垃圾清理、Xcode瘦身精简](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Xcode垃圾清理、Xcode瘦身精简](https://www.uedbox.com/post/68596/ "Xcode垃圾清理、Xcode瘦身精简")

[![免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/post/68706/ "免升级Xcode 解决 “Unsupported OS version”")

[![解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP](https://www.uedbox.com/post/68707/ "解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP")

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![最新 绕过Cloudflare最佳实践](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

[![NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")

[![好用的Mac清理卸载软件推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

[![AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/post/119359/ "AutoGen Studio 容器化部署与维护指南")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/post/119352/ "🔥 最新免费域名资源大全 | 永久免费域名获取")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

* [最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")
* [NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")
* [Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

* [2025 BT磁力搜索引擎大全【最新优质】](https://www.uedbox.com/post/54994/ "2025 BT磁力搜索引擎大全【最新优质】")
* [怎么用图片搜索番号？以图搜图AI搜图](https://www.uedbox.com/post/55287/ "怎么用图片搜索番号？以图搜图AI搜图")
* [this channel is blocked because it was used：Telegram群组/频道屏蔽解决方法](https://www.uedbox.com/post/56387/ "this channel is blocked because it was used：Telegram群组/频道屏蔽解决方法")
* [2025免费在线影视/动漫番剧优质网站，合集汇总更新](https://www.uedbox.com/post/69704/ "2025免费在线影视/动漫番剧优质网站，合集汇总更新")
* [最新ESET NOD32 License Key/激活码/许可证密钥/用户名密码](https://www.uedbox.com/post/58618/ "最新ESET NOD32 License Key/激活码/许可证密钥/用户名密码")
* [谷歌识图，以图搜图](https://www.uedbox.com/post/3902/ "谷歌识图，以图搜图")
* [No Access-Control-Allow-Origin 跨域错误解决](https://www.uedbox.com/post/50992/ "No Access-Control-Allow-Origin 跨域错误解决")
* [7款常用《网络抓包工具》更新](https://www.uedbox.com/post/59475/ "7款常用《网络抓包工具》更新")
* [手机BT/种子下载，手机磁力链下载软件整理](https://www.uedbox.com/post/56509/ "手机BT/种子下载，手机磁力链下载软件整理")
* [404.php webshell](https://www.uedbox.com/post/7182/ "404.php webshell")
* [一个绕过Google谷歌验证码（reCAPTCHA）的方法](https://www.uedbox.com/post/59017/ "一个绕过Google谷歌验证码（reCAPTCHA）的方法")
* [网络安全“Cyber security”和“Network security”的区别](https://www.uedbox.com/post/51126/ "网络安全“Cyber security”和“Network security”的区别")
* [用uBlock Origin过滤广告，享受最好的广告拦截体验](https://www.uedbox.com/post/55544/ "用uBlock Origin过滤广告，享受最好的广告拦截体验")
* [9部有史以来最好的黑客电影](https://www.uedbox.com/post/54446/ "9部有史以来最好的黑客电影")
* [解决Play商店“从服务器检索信息时出错DF-DFERH-01”](https://www.uedbox.com/post/66281/ "解决Play商店“从服务器检索信息时出错DF-DFERH-01”")

![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)

* [关于](https://www.uedbox.com/about)
* [博文](https://www.uedbox.com/blog)
* [分享](https://www.uedbox.com/share)
* [存档](https://www.uedbox.com/archives)
* [服务](https://www.uedbox.com/service)

体验盒子所发布的一切资源仅限用于学习和研究目的。不得用于非法用途，否则，一切后果用户自负。

2024 [体验盒子](https://www.uedbox.com/), [滇ICP备15006848号-1](https://beian.miit.gov.cn/)

×

#### 扫码分享

![网络安全](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/wx_qr.jpg)

验证：
`体验盒子`

##### 扫码分享

×

![网络安全](https://www.uedbox.com/wp-content/themes/UB2019/functions/qr/?m=5&e=L&p=6&url=https://www.uedbox.com/post/119346/)

##### 打赏零钱

 ×

* [支付宝打赏](#alipay)
* [微信打赏](#wx_pay)

![](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/alipay.png)

![](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/wx_pay.png)