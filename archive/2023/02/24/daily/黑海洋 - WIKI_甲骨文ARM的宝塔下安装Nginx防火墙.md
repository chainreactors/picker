---
title: 甲骨文ARM的宝塔下安装Nginx防火墙
url: https://blog.upx8.com/3235
source: 黑海洋 - WIKI
date: 2023-02-24
fetch_date: 2025-10-04T07:58:30.242170
---

# 甲骨文ARM的宝塔下安装Nginx防火墙

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 甲骨文ARM的宝塔下安装Nginx防火墙

发布时间:
2023-02-23

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
12461

众所周知，甲骨文免费ARM用料很足，有人测过腾讯轻量4H8G编译Nginx需要40s，甲骨文ARM 4H24G只要20s，在看看腾讯266元/月的价格，你说甲骨文ARM香不香。
但可是，ARM作为服务器里的新人，兼容性却很难让人满意，就说很多人最常用的宝塔面板，x86下运行的很稳，可是一旦安装到ARM上就水土不服了，比如我常用的Nginx防火墙、网络监控报表2个插件，我试过很多方法，有时虽然能安装上，可运行过程中经常出些小问题，昨天(2021-12-28)宝塔发布了7.8.0，我就随手更新了，又试了一下2个插件，结果就神奇的完美运行，没有error弹窗，没有Nginx故障，没有cc不拦截，没有网站数据不显示，反正就是完美。下面新创建一个arm实例复现一下，顺便做下记录。
[![](https://chenyu.me/usr/uploads/2022/07/1080089093.webp)](https://blog.upx8.com/go/aHR0cHM6Ly9jaGVueXUubWUvdXNyL3VwbG9hZHMvMjAyMi8wNy8xMDgwMDg5MDkzLndlYnA)

[![](https://chenyu.me/usr/uploads/2022/07/1148163899.webp)](https://blog.upx8.com/go/aHR0cHM6Ly9jaGVueXUubWUvdXNyL3VwbG9hZHMvMjAyMi8wNy8xMTQ4MTYzODk5LndlYnA)

## 运营环境

实例：甲骨文ARM 1H6G
系统：Ubuntun 20.04
宝塔面板：7.8.0正式版
Nginx防火墙：8.9.9
网站监控报表：6.6

## 步骤

#### 创建nginx\_prepare.sh

进入宝塔面板，文件->根目录/www/server/panel/install，创建编译安装脚本nginx\_prepare.sh：

#### 创建nginx\_configure.pl

再创建nginx\_configure.pl文件：

1. --add-module=/www/server/nginx/src/ngx\_devel\_kit --add-module=/www/server/nginx/src/lua\_nginx\_module

#### 修改权限

更改两个文件的权限600，所有者root
[![](https://chenyu.me/usr/uploads/2022/07/2967634147.webp)](https://blog.upx8.com/go/aHR0cHM6Ly9jaGVueXUubWUvdXNyL3VwbG9hZHMvMjAyMi8wNy8yOTY3NjM0MTQ3LndlYnA)

#### 清理脚本

ssh执行下面命令：

1. #清理脚本换行符，避免编译安装失败
2. sed -i 's/\r//g' /www/server/panel/install/nginx\_prepare.sh
3. #如Nginx用1.20.2版，则命令中nginx版本写为1.20
4. cd /www/server/panel/install && bash install\_soft.sh 0 update nginx 1.20

等待执行完成，然后重启宝塔面板，退出重新登录，安装Nginx放火墙、网站监控报表，就可以了。

## 终极解决法

换nginx openrsty版本试试，软件商店里，Nginx版本换成nginx openrsty！

[取消回复](https://blog.upx8.com/3235#respond-post-3235)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")