---
title: Windows最新微信小程序抓包方法
url: https://www.uedbox.com/post/68640/
source: 体验盒子
date: 2022-12-06
fetch_date: 2025-10-04T00:34:53.233832
---

# Windows最新微信小程序抓包方法

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

# Windows最新微信小程序抓包方法

* 发表于 2022年12月05日
* [周边](https://www.uedbox.com/web-security/safety/)

目录表

Toggle

* [最新微信小程序抓包](#%E6%9C%80%E6%96%B0%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F%E6%8A%93%E5%8C%85)
  + [一、安装 fiddler（5款常用《网络抓包工具》）](#%E4%B8%80%E3%80%81%E5%AE%89%E8%A3%85_fiddler%EF%BC%885%E6%AC%BE%E5%B8%B8%E7%94%A8%E3%80%8A%E7%BD%91%E7%BB%9C%E6%8A%93%E5%8C%85%E5%B7%A5%E5%85%B7%E3%80%8B%EF%BC%89)
  + [二、配置](#%E4%BA%8C%E3%80%81%E9%85%8D%E7%BD%AE)
  + [三、打开电脑端小程序](#%E4%B8%89%E3%80%81%E6%89%93%E5%BC%80%E7%94%B5%E8%84%91%E7%AB%AF%E5%B0%8F%E7%A8%8B%E5%BA%8F)

## 最新微信小程序抓包

### 一、安装 fiddler（[5款常用《网络抓包工具》](https://www.uedbox.com/post/59475/)）

官网下载：<https://www.telerik.com/download/fiddler>

### 二、配置

打开
`fiddler tools-> options，genneral:`
全选

![Windows最新微信小程序抓包方法](https://www.uedbox.com/wp-content/uploads/2022/12/1002766279.jpg)

**https**:

![Windows最新微信小程序抓包方法](https://www.uedbox.com/wp-content/uploads/2022/12/1398340308.jpg)

**connections**: 配置代理地址

![Windows最新微信小程序抓包方法](https://www.uedbox.com/wp-content/uploads/2022/12/761028094.jpg)

**gateway**:

![Windows最新微信小程序抓包方法](https://www.uedbox.com/wp-content/uploads/2022/12/2059808853.png)

### 三、打开电脑端小程序

退出微信，登录微信时设置代理

![Windows最新微信小程序抓包方法](https://www.uedbox.com/wp-content/uploads/2022/12/65946589.png)

打开小程序，查看**`fiddler`**，抓包成功

![Windows最新微信小程序抓包方法](https://www.uedbox.com/wp-content/uploads/2022/12/1485934669.jpg)

如果没成功

打开小程序、打开任务管理器，找到小程序进程，打开文件所在位置

![Windows最新微信小程序抓包方法](https://www.uedbox.com/wp-content/uploads/2022/12/944554242.jpg)

退出微信，删除\WMPFRuntime 下所有文件，再次登录打开小程序就可以了

`C:\Users\backlion\AppData\Roaming\Tencent\WeChat\XPlugin\Plugins\WMPFRuntime`

点赞(3)

打赏

分享

标签：[fiddler](https://www.uedbox.com/post/tag/fiddler/) , [小程序](https://www.uedbox.com/post/tag/%E5%B0%8F%E7%A8%8B%E5%BA%8F/) , [微信](https://www.uedbox.com/post/tag/%E5%BE%AE%E4%BF%A1/) , [抓包](https://www.uedbox.com/post/tag/%E6%8A%93%E5%8C%85/)  原文连接：**[Windows最新微信小程序抓包方法](https://www.uedbox.com/post/68640/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[AdSense收款招商银行电汇教程](https://www.uedbox.com/post/68634/ "AdSense收款招商银行电汇教程") [微信小程序抓包方法汇总](https://www.uedbox.com/post/68649/ "微信小程序抓包方法汇总")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![微信小程序抓包方法汇总](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

微信小程序抓包方法汇总](https://www.uedbox.com/post/68649/ "微信小程序抓包方法汇总")

[![微信营销7步骤](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

微信营销7步骤](https://www.uedbox.com/post/6797/ "微信营销7步骤")

[![小程序清除定时器clearinterval无效的原因](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

小程序清除定时器clearinterval无效的原因](https://www.uedbox.com/post/54887/ "小程序清除定时器clearinterval无效的原因")

[![微信分享带标题/图片/摘要/链接](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

微信分享带标题/图片/摘要/链接](https://www.uedbox.com/post/6972/ "微信分享带标题/图片/摘要/链接")

[![微信小程序计算两点间距离(经伟度距离)](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

微信小程序计算两点间距离(经伟度距离)](https://www.uedbox.com/post/54894/ "微信小程序计算两点间距离(经伟度距离)")

[![绕过限制，在PC上调试微信手机页面](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

绕过限制，在PC上调试微信手机页面](https://www.uedbox.com/post/7595/ "绕过限制，在PC上调试微信手机页面")

[![AndroidHttpCapture：一款Android手机抓包软件](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AndroidHttpCapture：一款Android手机抓包软件](https://www.uedbox.com/post/56408/ "AndroidHttpCapture：一款Android手机抓包软件")

[![微信 Mac 版终获更新2.0](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

微信 Mac 版终获更新2.0](https://www.uedbox.com/post/8612/ "微信 Mac 版终获更新2.0")

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
* [服务](https://www.ued...