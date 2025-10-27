---
title: 解决Error: php@7.4 has been disabled because it is a versioned formula
url: https://www.uedbox.com/post/68765/
source: 体验盒子
date: 2023-02-22
fetch_date: 2025-10-04T07:43:16.418495
---

# 解决Error: php@7.4 has been disabled because it is a versioned formula

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

# 解决Error: php@7.4 has been disabled because it is a versioned formula

* 发表于 2023年02月21日
* [macOS](https://www.uedbox.com/entertainment/macos/) , [PHP](https://www.uedbox.com/design/php-dev/)

目录表

Toggle

* [问题](#%E9%97%AE%E9%A2%98)
* [解决方法](#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)

## 问题

brew安装php7.4报错

|  |  |
| --- | --- |
| 1 | Error: php@7.4 has been disabled because it is a versioned formula! |

## 解决方法

|  |  |
| --- | --- |
| 1 | brew install shivammathur/php/php@7.4 |

更新
`PATH`
in
`.zshrc`
:

|  |  |
| --- | --- |
| 1  2  3 | echo 'export PATH="/opt/homebrew/opt/php@7.4/bin:$PATH"' >> ~/.zshrc  echo 'export PATH="/opt/homebrew/opt/php@7.4/sbin:$PATH"' >> ~/.zshrc  source ~/.zshrc |

检查版本

|  |  |
| --- | --- |
| 1  2  3  4  5 | $ php -v  PHP 7.4.33 (cli) (built: Jan 21 2023 06:43:54) ( NTS )  Copyright (c) The PHP Group  Zend Engine v3.4.0, Copyright (c) Zend Technologies  with Zend OPcache v7.4.33, Copyright (c), by Zend Technologies |

点赞(5)

打赏

分享

标签：[brew](https://www.uedbox.com/post/tag/brew/)  原文连接：**[解决Error: php@7.4 has been disabled because it is a versioned formula](https://www.uedbox.com/post/68765/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/post/68725/ "ChatGPT热，一大波 ChatGPT 开源项目诞生了！") [Mac右键终端：快速打开当前目录的终端](https://www.uedbox.com/post/68767/ "Mac右键终端：快速打开当前目录的终端")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![brew update 更新错误 shallow clone](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

brew update 更新错误 shallow clone](https://www.uedbox.com/post/66874/ "brew update 更新错误 shallow clone")

[![brew update慢，brew install慢如何解决？](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

brew update慢，brew install慢如何解决？](https://www.uedbox.com/post/57246/ "brew update慢，brew install慢如何解决？")

[![chromedriver安装 for MAC](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

chromedriver安装 for MAC](https://www.uedbox.com/post/57257/ "chromedriver安装 for MAC")

[![Php实现中国公民身份证号码有效性验证](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Php实现中国公民身份证号码有效性验证](https://www.uedbox.com/post/9221/ "Php实现中国公民身份证号码有效性验证")

[![$O00OO0=urldecode 解密](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

$O00OO0=urldecode 解密](https://www.uedbox.com/post/6109/ "$O00OO0=urldecode 解密")

[![Chrome彻底使用Html5播放器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Chrome彻底使用Html5播放器](https://www.uedbox.com/post/8879/ "Chrome彻底使用Html5播放器")

[![[转]用PHP下妹子图](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

[转]用PHP下妹子图](https://www.uedbox.com/post/6935/ "[转]用PHP下妹子图")

[![PHP GD库国旗一面](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

PHP GD库国旗一面](https://www.uedbox.com/post/5153/ "PHP GD库国旗一面")

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