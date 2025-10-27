---
title: Xcode垃圾清理、Xcode瘦身精简
url: https://www.uedbox.com/post/68596/
source: 体验盒子
date: 2022-10-23
fetch_date: 2025-10-03T20:41:33.113285
---

# Xcode垃圾清理、Xcode瘦身精简

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

# Xcode垃圾清理、Xcode瘦身精简

* 发表于 2022年10月22日
* [IOS](https://www.uedbox.com/design/ios/) , [macOS](https://www.uedbox.com/entertainment/macos/)

目录表

Toggle

* [Xcode垃圾清理](#Xcode%E5%9E%83%E5%9C%BE%E6%B8%85%E7%90%86)
  + [1、 ~/Library/Developer/Xcode/DerivedData/ （约10G+）](#1%E3%80%81_LibraryDeveloperXcodeDerivedData_%EF%BC%88%E7%BA%A610G%EF%BC%89)
  + [2、 ~/Library/Developer/CoreSimulator/Devices/ （约50G+）](#2%E3%80%81_LibraryDeveloperCoreSimulatorDevices_%EF%BC%88%E7%BA%A650G%EF%BC%89)
  + [3、 ~/Library/Developer/Xcode/iOS DeviceSupport/](#3%E3%80%81_LibraryDeveloperXcodeiOS_DeviceSupport)
  + [4、 ~/Library/Developer/Xcode/Archives/](#4%E3%80%81_LibraryDeveloperXcodeArchives)
  + [5、 ~/Library/Developer/Xcode/Products/](#5%E3%80%81_LibraryDeveloperXcodeProducts)
  + [6、 ~/Library/Developer/XCPGDevices/](#6%E3%80%81_LibraryDeveloperXCPGDevices)
  + [另外，Xcode12占用空间过大的解决精简simruntime](#%E5%8F%A6%E5%A4%96%EF%BC%8CXcode12%E5%8D%A0%E7%94%A8%E7%A9%BA%E9%97%B4%E8%BF%87%E5%A4%A7%E7%9A%84%E8%A7%A3%E5%86%B3%E7%B2%BE%E7%AE%80simruntime)

## Xcode垃圾清理

作为iOS开发者，mac空间不足，主要原因都在Xcode，清理方法如下：

### 1、 ~/Library/Developer/Xcode/DerivedData/ （约10G+）

这个文件夹中保存的是Xcode的缓存文件，曾经在Xcode跑过的所有项目的索引、build的信息等都会保存在这里。删除后在下次打开项目编译的时候将会重新生成。由于这里包含了大量已经没用的项目的信息又懒得去筛选，于是把整个文件夹里面都删了。

### 2、 ~/Library/Developer/CoreSimulator/Devices/ （约50G+）

一堆模拟器的数据。每个文件夹里包含的就是一个特定系统版本的设备的数据。每个文件夹对应哪个设备可以在其下device.plist中查看。亲测删除之后的效果跟在模拟器里重置相同。省得一个个去重置了，删吧。（删除后可能模拟器会运行不了，在XCode删掉模拟器重新添加就可以了）

### 3、 ~/Library/Developer/Xcode/iOS DeviceSupport/

每次把一个设备接入电脑进行真机调试之前，电脑会对设备建立索引，也在此文件夹下生成对该设备系统的支持文件。于是这里存在了一堆对旧版本iOS设备支持的文件。而我最近基本只对iOS9.3的设备进行真机调试。于是删除了所有低于9.3的文件夹。

### 4、 ~/Library/Developer/Xcode/Archives/

每次打包App的dSYM等数据就保存在这里，把一些没用的版本删了。如果是上线了的版本还是保留吧。

### 5、 ~/Library/Developer/Xcode/Products/

同上，把没用的删了。

### 6、 ~/Library/Developer/XCPGDevices/

这里保存了playground的项目缓存，全删了。

### 另外，Xcode12占用空间过大的解决精简 `simruntime`

iOS.simruntime日常使用删不得，
`tvOS.simruntime`
，
`watchOS.simruntime`
，大部分开发者接触不到，如果用不到可直接删除，可以减少12g

文件路径：

|  |  |
| --- | --- |
| 1  2  3 | Xcode.app/Contents/Developer/Platforms/WatchOS.platform/Library/Developer/CoreSimulator/Profiles/Runtimes/watchOS.simruntime    Xcode.app/Contents/Developer/Platforms/AppleTVOS.platform/Library/Developer/CoreSimulator/Profiles/Runtimes/tvOS.simruntime |

点赞(3)

打赏

分享

标签：[Xcode](https://www.uedbox.com/post/tag/xcode/)  原文连接：**[Xcode垃圾清理、Xcode瘦身精简](https://www.uedbox.com/post/68596/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[TypeScript和JavaScript区别在哪？有何不同？](https://www.uedbox.com/post/68592/ "TypeScript和JavaScript区别在哪？有何不同？") [MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM](https://www.uedbox.com/post/68600/ "MAC ParallelsDesktop安装精简系统PE/ESD/ISO/WIM")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![iPhone is busy: Preparing debugger support for iPhone解决办法](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

iPhone is busy: Preparing debugger support for iPhone解决办法](https://www.uedbox.com/post/68582/ "iPhone is busy: Preparing debugger support for iPhone解决办法")

[![免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/post/68706/ "免升级Xcode 解决 “Unsupported OS version”")

[![解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP](https://www.uedbox.com/post/68707/ "解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP")

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
* [谷歌识图，以图搜图](https://www.uedbox.com/post/3902/ "谷歌识图...