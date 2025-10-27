---
title: TypeScript和JavaScript区别在哪？有何不同？
url: https://www.uedbox.com/post/68592/
source: 体验盒子
date: 2022-10-19
fetch_date: 2025-10-03T20:16:13.437436
---

# TypeScript和JavaScript区别在哪？有何不同？

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

# TypeScript和JavaScript区别在哪？有何不同？

* 发表于 2022年10月18日
* [TypeScript](https://www.uedbox.com/design/typescript/)

![TypeScript和JavaScript区别在哪？有何不同？](https://www.uedbox.com/wp-content/uploads/2022/10/1597593610760.png)

目录表

Toggle

* [什么是TypeScript？](#%E4%BB%80%E4%B9%88%E6%98%AFTypeScript%EF%BC%9F)
* [什么是 JavaScript？](#%E4%BB%80%E4%B9%88%E6%98%AF_JavaScript%EF%BC%9F)
* [TypeScript和JavaScript区别在哪？](#TypeScript%E5%92%8CJavaScript%E5%8C%BA%E5%88%AB%E5%9C%A8%E5%93%AA%EF%BC%9F)
  + [其它不同](#%E5%85%B6%E5%AE%83%E4%B8%8D%E5%90%8C)
* [讲白话](#%E8%AE%B2%E7%99%BD%E8%AF%9D)

## 什么是TypeScript？

TypeScript简称
`TS`
，**JavaScript的超集**，就是在JavaScript的基础上做一层封装，封装出TS的特性，最终可以编译为JavaScript。

TS最初是为了让习惯编写强类型语言的后端程序员能快速编写web应用，因为 JavaScript 没有强数据类型，所以 TypeScript 提供了静态数据类型，这是 **TypeScript** 的核心

随着项目不断壮大，越来越多的情断意识到静态数据类型的重要性。随着 TypeScript 越来越完善，拥趸越来越多，需求越来越大。最后由前端3大框架之一Angular2.x带头使用。

## 什么是 JavaScript？

JavaScript 是一种脚本，一门编程语言，它可以在网页上实现复杂的功能，网页展现给你的不再是简单的静态信息，而是实时的内容更新，交互式的地图，2D/3D 动画，滚动播放的视频等等。JavaScript 怎能缺席。它是标准 Web 技术蛋糕的第三层，其中 HTML 和 CSS 我们已经在学习中心的其他部分进行了详细的讲解。

## TypeScript和JavaScript区别在哪？

* 语言层面：
  `JavaScript和TypeScript都是ECMAScript`
  （ECMA-262）的具体实现。
* 执行环境层面：浏览器引擎和Node.js都能够直接运行
  `JavaScript`
  ，但无法直接运行
  `TypeScript`
  。
* 时序层面：TypeScript被真正执行前，会通过编译转换生成JavaScript，之后才能被解释执行。
* 厂商层面：JavaScript由Netscape率先推出，现在主要由各大浏览器厂商实现。而TypeScript is a trademark of Microsoft Corporation，目前由微软进行设计和维护。

TypeScript是ECMAScript 2015的语法超集，是JavaScript的语法糖。
`JavaScript程序可以直接移植到TypeScript，TypeScript需要编译（语法转换）生成JavaScript才能被浏览器执行`
。

### 其它不同

* TypeScript 能使用JavaScript 中的所有代码和编码概念
* TypeScript 从核心语言方面和类概念的模塑方面对 JavaScript 对象模型进行扩展
* JavaScript 代码可以在无需任何修改的情况下与 TypeScript 一同工作，同时可以使用编译器将 TypeScript 代码转换为 JavaScript
* TypeScript 通过类型注解提供编译时的静态类型检查
* TypeScript 中的数据要求带有明确的类型，JavaScript不要求
* TypeScript 为函数提供了缺省参数值
* TypeScript 引入了 JavaScript 中没有的“类”概念
* TypeScript 中引入了模块的概念，可以把声明、数据、函数和类封装在模块中

至于什么该使用TS或JS，我认为在构建复杂大型web应用时TS是首选，项目不复杂时只需灵活运用JS就已经足够了。

来看个示例代码

![TypeScript和JavaScript区别在哪？有何不同？](https://www.uedbox.com/wp-content/uploads/2022/10/typescript_javascript_e.webp)

左边TS右边JS

## 讲白话

javascript是一个**弱类型语言**，Typescript是Javascript的一个超集，最大区别就是**`Typescript（Ts）提供了类型系统`**。TypeScript 只会进行静态检查，如果发现有错误，编译的时候就会报错。

比如给一个约定参数为String的函数传入了包函数字的数组，直接在编辑器中就会提示错误，编译时也会出错：

> Argument of type 'number[]' is not assignable to parameter of type 'string'.

但是依然会生成js文件。

**TypeScript 编译的时候即使报错了，还是会生成编译结果**，我们仍然可以使用这个编译之后的文件，也可以设置不使用。

我们在写js的时候直接运行在浏览器。而写ts需要按照约定的类型系统去编写代码，然后编译成浏览器识别的js再去执行，正是因为TS的类型系统，多了编译为Js代码的步骤，所以依赖于类型系统，为程序员提前规避了很多错误，而不是等到执行代码的时候才发现错误。

点赞(3)

打赏

分享

标签：[Javascript](https://www.uedbox.com/post/tag/javascript/) , [TypeScript](https://www.uedbox.com/post/tag/typescript/)  原文连接：**[TypeScript和JavaScript区别在哪？有何不同？](https://www.uedbox.com/post/68592/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[IOS蓝牙框架方案CoreBluetooth、MultipeerConnectivity](https://www.uedbox.com/post/68589/ "IOS蓝牙框架方案CoreBluetooth、MultipeerConnectivity") [Xcode垃圾清理、Xcode瘦身精简](https://www.uedbox.com/post/68596/ "Xcode垃圾清理、Xcode瘦身精简")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![jquery：倒计时插件 （jquery.countdown）多国语言版](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

jquery：倒计时插件 （jquery.countdown）多国语言版](https://www.uedbox.com/post/1958/ "jquery：倒计时插件 （jquery.countdown）多国语言版")

[![jQuery实现锚点scoll效果](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

jQuery实现锚点scoll效果](https://www.uedbox.com/post/2499/ "jQuery实现锚点scoll效果")

[![精品JS代码收藏](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

精品JS代码收藏](https://www.uedbox.com/post/1882/ "精品JS代码收藏")

[![几个常用且实用的原生JavaScript函数](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

几个常用且实用的原生JavaScript函数](https://www.uedbox.com/post/1822/ "几个常用且实用的原生JavaScript函数")

[![一个网页设计需求方眼中的网页设计(摘录）](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

一个网页设计需求方眼中的网页设计(摘录）](https://www.uedbox.com/post/1979/ "一个网页设计需求方眼中的网页设计(摘录）")

[![纯JS无间隙文字向上滚动代码](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

纯JS无间隙文字向上滚动代码](https://www.uedbox.com/post/29/ "纯JS无间隙文字向上滚动代码")

[![树形菜单组件(dtree)](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

树形菜单组件(dtree)](https://www.uedbox.com/post/3193/ "树形菜单组件(dtree)")

[![瀑布流布局](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

瀑布流布局](https://www.uedbox.com/post/4339/ "瀑布流布局")

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
*...