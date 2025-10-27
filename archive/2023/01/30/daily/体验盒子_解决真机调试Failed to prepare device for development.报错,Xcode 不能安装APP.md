---
title: 解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP
url: https://www.uedbox.com/post/68707/
source: 体验盒子
date: 2023-01-30
fetch_date: 2025-10-04T05:10:24.942768
---

# 解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP

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

# 解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP

* 发表于 2023年01月29日
* [IOS](https://www.uedbox.com/design/ios/)

目录表

Toggle

* [错误信息](#%E9%94%99%E8%AF%AF%E4%BF%A1%E6%81%AF)
  + [Failed to prepare device for development.](#Failed_to_prepare_device_for_development)
* [解决](#%E8%A7%A3%E5%86%B3)
* [还是无法解决？](#%E8%BF%98%E6%98%AF%E6%97%A0%E6%B3%95%E8%A7%A3%E5%86%B3%EF%BC%9F)

## 错误信息

### **Failed to prepare device for development.**

This operation can fail **if** the version **of** the OS **on** the device is incompatible **with** the installed version **of** Xcode. You may also need **to** restart your mac and device **in** **order** **to** correctly detect compatibility.

不能装APP，说版本不对。

## 解决

1. Check /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/ for directory name 15.4 (your iOS version).
2. If the directory is missing download support files for 15.4 (your iOS version) from [github.com/filsv/iPhon…](https://github.com/filsv/iPhoneOSDeviceSupport) and place it in the above path.
3. Restart Xcode.

检查
`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/`
这里面是不是有IOS对应版本的文件夹, 如果没有，下载装进去！

下载地址：[github.com/filsv/iPhon…](https://github.com/filsv/iPhoneOSDeviceSupport)

或者地址（这个更全面）：[https://github.com/iGhibli/iOS-DeviceSupport/](https://github.com/iGhibli/iOS-DeviceSupport/tree/master/DeviceSupport)

重启Xcode，解决了！

## 还是无法解决？

如果你是IOS 16或更高系统，看这里《[IOS 16下必须开启开发者模式才能真机](https://www.uedbox.com/post/68709/)》

这个其实和[免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/post/68706/)是相同的解决方法。

点赞(1)

打赏

分享

标签：[Xcode](https://www.uedbox.com/post/tag/xcode/)  原文连接：**[解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP](https://www.uedbox.com/post/68707/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/post/68706/ "免升级Xcode 解决 “Unsupported OS version”") [升级 iOS 16 后没有开发者模式怎么办？如何打开开发者模式？](https://www.uedbox.com/post/68710/ "升级 iOS 16 后没有开发者模式怎么办？如何打开开发者模式？")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![iPhone is busy: Preparing debugger support for iPhone解决办法](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

iPhone is busy: Preparing debugger support for iPhone解决办法](https://www.uedbox.com/post/68582/ "iPhone is busy: Preparing debugger support for iPhone解决办法")

[![Xcode垃圾清理、Xcode瘦身精简](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Xcode垃圾清理、Xcode瘦身精简](https://www.uedbox.com/post/68596/ "Xcode垃圾清理、Xcode瘦身精简")

[![免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/post/68706/ "免升级Xcode 解决 “Unsupported OS version”")

[![IOS 16下必须开启开发者模式才能真机](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

IOS 16下必须开启开发者模式才能真机](https://www.uedbox.com/post/68709/ "IOS 16下必须开启开发者模式才能真机")

[![升级 iOS 16 后没有开发者模式怎么办？如何打开开发者模式？](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

升级 iOS 16 后没有开发者模式怎么办？如何打开开发者模式？](https://www.uedbox.com/post/68710/ "升级 iOS 16 后没有开发者模式怎么办？如何打开开发者模式？")

[![了解Nearby Interaction探索与第三方硬件的近距离交互](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

了解Nearby Interaction探索与第三方硬件的近距离交互](https://www.uedbox.com/post/68717/ "了解Nearby Interaction探索与第三方硬件的近距离交互")

[![Xcode 无法找到和创建 iOS Simulators](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Xcode 无法找到和创建 iOS Simulators](https://www.uedbox.com/post/69465/ "Xcode 无法找到和创建 iOS Simulators")

[![解决Xcode：Unable to boot device because it cannot be located on disk.](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

解决Xcode：Unable to boot device because it cannot be located on disk.](https://www.uedbox.com/post/69703/ "解决Xcode：Unable to boot device because it cannot be located on disk.")

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
* [解决Play商店...