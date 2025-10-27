---
title: 解决 the “listen … http2” directive is deprecated
url: https://www.uedbox.com/post/119302/
source: 体验盒子
date: 2024-12-28
fetch_date: 2025-10-06T19:38:43.130043
---

# 解决 the “listen … http2” directive is deprecated

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

# 解决 the “listen … http2” directive is deprecated

* 发表于 2024年12月27日
* [后端](https://www.uedbox.com/design/backend/)

目录表

Toggle

* [错误](#%E9%94%99%E8%AF%AF)
* [解决方法](#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
  + [检查现有配置形式如：](#%E6%A3%80%E6%9F%A5%E7%8E%B0%E6%9C%89%E9%85%8D%E7%BD%AE%E5%BD%A2%E5%BC%8F%E5%A6%82%EF%BC%9A)
  + [修复：nginx >= 1.25.1 的新格式为](#%E4%BF%AE%E5%A4%8D%EF%BC%9Anginx_%3E_1251_%E7%9A%84%E6%96%B0%E6%A0%BC%E5%BC%8F%E4%B8%BA)

## 错误

|  |  |
| --- | --- |
| 1 | nginx: [warn] the "listen ... http2" directive is deprecated, use the "http2" directive instead |

## 解决方法

### 检查现有配置形式如：

|  |  |
| --- | --- |
| 1  2 | server {  listen      443 ssl http2; |

### 修复：nginx >= 1.25.1 的新格式为

|  |  |
| --- | --- |
| 1  2  3 | server {  listen      443 ssl;  http2  on; |

更多参考：<https://github.com/nginxinc/kubernetes-ingress/issues/4237>

点赞(2)

打赏

分享

标签：[nginx](https://www.uedbox.com/post/tag/nginx/)  原文连接：**[解决 the “listen … http2” directive is deprecated](https://www.uedbox.com/post/119302/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[Prism：也许是目前理想的WordPress代码高亮方案](https://www.uedbox.com/post/103216/ "Prism：也许是目前理想的WordPress代码高亮方案") [vscode运行flutter项目ios真机](https://www.uedbox.com/post/119313/ "vscode运行flutter项目ios真机")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![nginx维护错误面nginx error_page](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

nginx维护错误面nginx error\_page](https://www.uedbox.com/post/7014/ "nginx维护错误面nginx error_page")

[![三个方法透过Nginx代理获取客户端真实IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

三个方法透过Nginx代理获取客户端真实IP](https://www.uedbox.com/post/57606/ "三个方法透过Nginx代理获取客户端真实IP")

[![Nginx配置WebSocket【同时支持WSS与WS】](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx配置WebSocket【同时支持WSS与WS】](https://www.uedbox.com/post/68560/ "Nginx配置WebSocket【同时支持WSS与WS】")

[![ngx_lua_waf：一个基于OpenResty（Nginx+Lua）的web应用防火墙](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ngx\_lua\_waf：一个基于OpenResty（Nginx+Lua）的web应用防火墙](https://www.uedbox.com/post/58048/ "ngx_lua_waf：一个基于OpenResty（Nginx+Lua）的web应用防火墙")

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![CentOS7/Linux开机自启动Nginx/PHP-FPM/mysqld](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

CentOS7/Linux开机自启动Nginx/PHP-FPM/mysqld](https://www.uedbox.com/post/58825/ "CentOS7/Linux开机自启动Nginx/PHP-FPM/mysqld")

[![Nginx配置Basic Auth登录认证，要求用户名密码](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx配置Basic Auth登录认证，要求用户名密码](https://www.uedbox.com/post/58980/ "Nginx配置Basic Auth登录认证，要求用户名密码")

[![nginx HTTP请求源码泄露和拒绝服务漏洞](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

nginx HTTP请求源码泄露和拒绝服务漏洞](https://www.uedbox.com/post/122/ "nginx HTTP请求源码泄露和拒绝服务漏洞")

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