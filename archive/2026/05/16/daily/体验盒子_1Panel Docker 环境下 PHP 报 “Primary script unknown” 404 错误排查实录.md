---
title: 1Panel Docker 环境下 PHP 报 “Primary script unknown” 404 错误排查实录
url: https://www.uedbox.com/post/119799/
source: 体验盒子
date: 2026-05-16
fetch_date: 2026-05-17T05:47:53.772099
---

# 1Panel Docker 环境下 PHP 报 “Primary script unknown” 404 错误排查实录

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观察](https://www.uedbox.com/entertainment/ "观察")
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

# 1Panel Docker 环境下 PHP 报 “Primary script unknown” 404 错误排查实录

* 发表于 2026年05月16日
* [Linux](https://www.uedbox.com/design/linux/) , [周边](https://www.uedbox.com/web-security/safety/)

目录表

Toggle

* [背景](#%E8%83%8C%E6%99%AF)
* [原因](#%E5%8E%9F%E5%9B%A0)
* [解决](#%E8%A7%A3%E5%86%B3)
  + [方案一：修复父目录权限（推荐，符合 1Panel 规范）](#%E6%96%B9%E6%A1%88%E4%B8%80%EF%BC%9A%E4%BF%AE%E5%A4%8D%E7%88%B6%E7%9B%AE%E5%BD%95%E6%9D%83%E9%99%90%EF%BC%88%E6%8E%A8%E8%8D%90%EF%BC%8C%E7%AC%A6%E5%90%88_1Panel_%E8%A7%84%E8%8C%83%EF%BC%89)
  + [方案二：临时开放进入权限（快速修复）](#%E6%96%B9%E6%A1%88%E4%BA%8C%EF%BC%9A%E4%B8%B4%E6%97%B6%E5%BC%80%E6%94%BE%E8%BF%9B%E5%85%A5%E6%9D%83%E9%99%90%EF%BC%88%E5%BF%AB%E9%80%9F%E4%BF%AE%E5%A4%8D%EF%BC%89)
  + [验证](#%E9%AA%8C%E8%AF%81)
* [总结](#%E6%80%BB%E7%BB%93)

## 背景

在 1Panel 面板中部署 PHP 项目（如 ThinkPHP），访问
`.php`
文件时页面显示 **404 Not Found**​ 或 **File Not Found** 或 502。Nginx 错误日志出现
`FastCGI sent in stderr: "Primary script unknown"`
，且 PHP-FPM 容器无相关错误日志。

## 原因

核心原因是 **Linux 文件系统权限链断裂**。

1. **现象**：Nginx 配置正确，宿主机文件存在且权限为 777。
2. **诊断**：使用
   `namei -l /path/to/file.php`
   检查权限链。
3. **真凶**：父目录（如
   `/www/sites`
   ）权限为
   `drwxr-x--- (750)`
   ，属主为
   `root`
   。
4. **结果**：PHP-FPM 容器内的
   `www-data`
   用户（即使 UID 相同）属于“其他人(Others)”，因父目录无
   `x`
   （执行/进入）权限，导致无法进入目录读取文件，从而报 “Primary script unknown”。

## 解决

打通权限链，确保 PHP-FPM 进程能进入并读取文件。

### 方案一：修复父目录权限（推荐，符合 1Panel 规范）

将
`/www/sites`
的属主改为与 PHP 容器内一致的用户（通常为
`www-data`
），无需开放全局权限。

|  |  |
| --- | --- |
| 1  2  3  4  5 | # 查看容器内 www-data 的 UID（通常为 1000）  docker exec -it <php-container> id www-data    # 在宿主机修改目录属主为 UID 1000  chown -R 1000:1000 /www/sites |

### 方案二：临时开放进入权限（快速修复）

若不想变更属主，可单独给父目录增加“其他人”的执行权限，允许进入目录。

|  |  |
| --- | --- |
| 1 | chmod o+x /www/sites |

### 验证

修复后，再次使用
`namei -l`
检查，确保每一级目录对 PHP 进程用户均可见。

|  |  |
| --- | --- |
| 1  2 | namei -l /www/sites/your-site/index.php  # 预期结果：sites 目录属主变为 www-data 或权限包含 --x |

## 总结

Docker 环境下，宿主机文件权限与容器内用户 UID 的映射是关键。遇到 PHP 404 时，优先使用
`namei -l`
检查**整个路径链**的权限，而非仅关注文件本身。

点赞(0)

打赏

分享

标签：[1Panel](https://www.uedbox.com/post/tag/1panel/) , [docker](https://www.uedbox.com/post/tag/docker/)  原文连接：**[1Panel Docker 环境下 PHP 报 “Primary script unknown” 404 错误排查实录](https://www.uedbox.com/post/119799/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[Flutter APK 体积144MB到23MB：瘦身实战](https://www.uedbox.com/post/119797/ "Flutter APK 体积144MB到23MB：瘦身实战")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/post/119359/ "AutoGen Studio 容器化部署与维护指南")

[![家庭摄像头会遭遇攻击吗?](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

家庭摄像头会遭遇攻击吗?](https://www.uedbox.com/post/6440/ "家庭摄像头会遭遇攻击吗?")

[![Mysql综合利用工具](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Mysql综合利用工具](https://www.uedbox.com/post/5823/ "Mysql综合利用工具")

[![那些强悍的PHP一句话后门](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

那些强悍的PHP一句话后门](https://www.uedbox.com/post/6051/ "那些强悍的PHP一句话后门")

[![burpsuite pro v1.4.07破解版](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

burpsuite pro v1.4.07破解版](https://www.uedbox.com/post/4650/ "burpsuite pro v1.4.07破解版")

[![一篇关于360四引擎免杀文章](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

一篇关于360四引擎免杀文章](https://www.uedbox.com/post/5207/ "一篇关于360四引擎免杀文章")

[![SubDomainScanner旁站及二级米查询](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

SubDomainScanner旁站及二级米查询](https://www.uedbox.com/post/6167/ "SubDomainScanner旁站及二级米查询")

[![看完这篇免杀的文章后，你基本可以成为免杀高手了!](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

看完这篇免杀的文章后，你基本可以成为免杀高手了!](https://www.uedbox.com/post/5295/ "看完这篇免杀的文章后，你基本可以成为免杀高手了!")

[![Flutter APK 体积144MB到23MB：瘦身实战](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Flutter APK 体积144MB到23MB：瘦身实战](https://www.uedbox.com/post/119797/ "Flutter APK 体积144MB到23MB：瘦身实战")

[![免费Developer打包IPA没小组件权限](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

免费Developer打包IPA没小组件权限](https://www.uedbox.com/post/119778/ "免费Developer打包IPA没小组件权限")

[![2025年最新9大真正免费AI大模型API汇总](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

2025年最新9大真正免费AI大模型API汇总](https://www.uedbox.com/post/119756/ "2025年最新9大真正免费AI大模型API汇总")

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

* [1Panel Docker 环境下 PHP 报 “Primary script unknown” 404 错误排查实录](https://www.uedbox.com/post/119799/ "1Panel Docker 环境下 PHP 报 “Primary script unknown” 404 错误排查实录")

* [2025 BT磁力搜索引擎大全【最新优质】](https://www.uedbox.com/post/54994/ "2025 BT磁力搜索引擎大全【最新优质】")
* [怎么用图片搜索番号？以图搜图AI搜图，一张截图秒出源](https://www.uedbox.com/post/55287/ "怎么用图片搜索番号？以图搜图AI搜图，一张截图秒出源")
* [this channel is blocked because it was used：Telegram群组/频道屏蔽解决方法](https://www.uedbox.com/post/56387/ "this channel is blocked because it was used：Telegram群组/频道屏蔽解决方法")
* [2025免费在线影视/动漫番剧神站，合集汇总更新](https://www.uedbox.com/post/69704/ "2025免费在线影视/动漫番剧神站，合集汇总更新")
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
...