---
title: 解决WordPress上传svg/ico/webp，您无权上传此文件类型
url: https://www.uedbox.com/post/69734/
source: 体验盒子
date: 2024-10-08
fetch_date: 2025-10-06T18:51:07.974382
---

# 解决WordPress上传svg/ico/webp，您无权上传此文件类型

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

# 解决WordPress上传svg/ico/webp，您无权上传此文件类型

* 发表于 2024年10月07日
* [WordPress](https://www.uedbox.com/design/wordpress/)

一些WordPress用户的部分主题在上传svg、ico、webp文件时出现“ ”的提示，意思是这类图片格式不允许上传，今天这个教程能解决这个问题

目录表

Toggle

* [WordPress默认允许上传的文件类型](#WordPress%E9%BB%98%E8%AE%A4%E5%85%81%E8%AE%B8%E4%B8%8A%E4%BC%A0%E7%9A%84%E6%96%87%E4%BB%B6%E7%B1%BB%E5%9E%8B)
* [为什么 WordPress 不允许所有文件类型](#%E4%B8%BA%E4%BB%80%E4%B9%88_WordPress_%E4%B8%8D%E5%85%81%E8%AE%B8%E6%89%80%E6%9C%89%E6%96%87%E4%BB%B6%E7%B1%BB%E5%9E%8B)
* [如何在 WordPress 中允许未知文件类型](#%E5%A6%82%E4%BD%95%E5%9C%A8_WordPress_%E4%B8%AD%E5%85%81%E8%AE%B8%E6%9C%AA%E7%9F%A5%E6%96%87%E4%BB%B6%E7%B1%BB%E5%9E%8B)
  + [允许上传的文件类型](#%E5%85%81%E8%AE%B8%E4%B8%8A%E4%BC%A0%E7%9A%84%E6%96%87%E4%BB%B6%E7%B1%BB%E5%9E%8B)
    - [步骤一](#%E6%AD%A5%E9%AA%A4%E4%B8%80)
    - [步骤二](#%E6%AD%A5%E9%AA%A4%E4%BA%8C)

## WordPress默认允许上传的文件类型

出于安全考虑，WordPress 默认限制了能上传的文件类型。默认允许上传的文件类型有：

图片：.jpg .png .gif .jpeg .ico
文件：.pdf .doc .ppt .odt .xls .psd
音频：.mp3 .m4a .ogg .wav
视频：.mp4 .mov .avi .mpg .ogv .3gp .3g2

这些文件比较安全，不会影响 WordPress 正常运行。

## 为什么 WordPress 不允许所有文件类型

WordPress 限制文件扩展名来保护网站免受潜在的安全风险或滥用的影响。

比如允许用户上传 .exe 扩展名的文件，就可能被执行恶意软件，黑客可以进入网站后台甚至控制整个服务器。一些文件可能会损害网站声誉、被窃取信息、索要赎金，并面临其他可能的威胁。

这就是为什么当你尝试上传 WordPress 不允许的文件类型时，会看到一条警告提示：对不起，出于安全原因，不允许使用此文件类型。

## 如何在 WordPress 中允许未知文件类型

有两种方法可以允许未知文件类型。第一种是允许上传任何文件类型到 WordPress 媒体库。第二种是允许上传指定的文件类型。显然第一种不够安全，第二种才安全。

### 允许上传的文件类型

#### 步骤一

在网站根目录，编辑 wp-config.php，在里边填入代码：

|  |  |
| --- | --- |
| 1 | define('ALLOW\_UNFILTERED\_UPLOADS', true); |

#### 步骤二

在你主题所在模板文件夹根目录找到 functions.php 文件，添加以下代码：

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | add\_filter('upload\_mimes', 'tbi\_upload\_mimes');  function tbi\_upload\_mimes($mimes = array()) {  $mimes['svg'] = 'image/svg+xml';  $mimes['ico'] = 'image/x-icon';  $mimes['webp'] = 'image/webp';  return $mimes;  } |

此时你应该可以上传特定文件而不会触发警告消息了。

点赞(2)

打赏

分享

标签：[WordPress](https://www.uedbox.com/post/tag/wordpress/)  原文连接：**[解决WordPress上传svg/ico/webp，您无权上传此文件类型](https://www.uedbox.com/post/69734/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/post/69717/ "cursor, 一款基于 vscode 的 AI IDE") [Flutter 中设置 Google Maps 样式深色模式](https://www.uedbox.com/post/69760/ "Flutter 中设置 Google Maps 样式深色模式")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![体验盒子 Sunrise 主题](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

体验盒子 Sunrise 主题](https://www.uedbox.com/post/5694/ "体验盒子 Sunrise 主题")

[![WordPress宠物！](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress宠物！](https://www.uedbox.com/post/4600/ "WordPress宠物！")

[![WordPress 3.0.1官方中文版发布啦](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress 3.0.1官方中文版发布啦](https://www.uedbox.com/post/1397/ "WordPress 3.0.1官方中文版发布啦")

[![WordPress 3.0.1 wp-admin/plugins.php模块跨站脚本漏洞](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress 3.0.1 wp-admin/plugins.php模块跨站脚本漏洞](https://www.uedbox.com/post/1565/ "WordPress 3.0.1 wp-admin/plugins.php模块跨站脚本漏洞")

[![wordpress添加Ctrl+Eenter快捷回复方法](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

wordpress添加Ctrl+Eenter快捷回复方法](https://www.uedbox.com/post/1771/ "wordpress添加Ctrl+Eenter快捷回复方法")

[![WordPress中Pre标签自动换行兼容IE/Opera/Firefox/Chrome](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress中Pre标签自动换行兼容IE/Opera/Firefox/Chrome](https://www.uedbox.com/post/154/ "WordPress中Pre标签自动换行兼容IE/Opera/Firefox/Chrome")

[![WordPress自动添加关键词优化的代码](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress自动添加关键词优化的代码](https://www.uedbox.com/post/2448/ "WordPress自动添加关键词优化的代码")

[![wordpress猜解密码脚本](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

wordpress猜解密码脚本](https://www.uedbox.com/post/4524/ "wordpress猜解密码脚本")

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
* [解决Play商店“从服务器检索信息时出错DF-DFERH-01”](https://www.uedbox.com/post/6628...