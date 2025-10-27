---
title: NinjiaTag，兼容Apple Find My网络的开源防丢神器
url: https://www.uedbox.com/post/119688/
source: 体验盒子
date: 2025-09-13
fetch_date: 2025-10-02T20:05:58.412942
---

# NinjiaTag，兼容Apple Find My网络的开源防丢神器

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

# NinjiaTag，兼容Apple Find My网络的开源防丢神器

* 发表于 2025年09月12日
* [周边](https://www.uedbox.com/web-security/safety/)

NinjiaTag 是一个与Apple Find My网络兼容的开源防丢系统。与 [go-haystack](https://github.com/hybridgroup/go-haystack) 、[Macless-Haystack](https://github.com/dchristl/macless-haystack) 等基于OpenHaystack 的开源项目类似，无须真实Mac设备或虚拟机的情况下，就可以借助Apple Find My网络跟踪自定义的类AirTag硬件。

![NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/wp-content/uploads/2025/09/NinjiaTag.png)

## DIY 兼容 FindMy 网络的定位标签/设备（长期记录）

> “NinjiaTag”并非拼写错误，而是我们对物联网产品价值的重新定义：它不仅是敏捷的防丢工具（Ninja），更是对下一代分布式物联网（IOT）技术的憧憬，为分布式蓝牙标签（Tag）的新一代解决方案。名称中的 ‘jia’ 也寓意 ‘协作之家’，期待与你共同构建！

相对于 go-haystack 、Macless-Haystack 这些项目目标用户主要为极客和有技术背景的用户，NinjiaTag的目标用户是普通用户物品防丢与老人守护的核心需求，解决涵盖开源硬件、软件一体化解决方案，在使用习惯上更加适合中国人习惯。

**NinjiaTag 针对的核心痛点及需求：**

* 目前类似AirTag以及各种主流防丢器都无法长期存储轨迹，历史记录通常仅保留 7 天；
* 安卓/PC 用户无法直接查看苹果生态的轨迹数据，跨平台兼容性差；
* 专业轨迹记录设备需频繁充电，需要手动按下记录和停止（码表）

**NinjiaTag 的解决方案：**

* 永久轨迹存储：云端或自建服务器无限期保存位置历史
* 一键导出 GPX：兼容所有支持 GPX 格式的 APP （如一生足迹、两步路、世界迷雾）
* 无感记录：超低功耗设计（ CR2032 电池续航 1 年+），无需充电或手动开关

**项目目前实现的核心功能：**

* 服务器端后台运行 request\_report 获取位置，定期下载位置数据并储存在本地服务器数据库，储存时间不限（目前市面上主流产品记录时长最多为 7 天），轨迹可永久保存于服务器
* 支持任意时间段任意物品轨迹查询和显示，支持轨迹点的经纬度和时间点显示，可随意缩放查看，方便回溯。
* 支持热图显示（ Hotspot ），类似地理信息系统的人流密度显示，经常去过的地方颜色更深，不去或偶尔去的地方颜色浅。
* Web 前端支持密钥管理
* 地图采用开源的 Mapbox-GL 三维地图引擎，支持三维地形显示，渲染更加美观
* 支持选择单/多物品任意时间段 GPX(GPS eXchange Format)文件导出

有动手能力的，可以基于NinjiaTag 打造自己兼容AirTag的防丢硬件及搭建服务，不想折腾的，可以直接找开发者购买硬件及服务。

项目地址：<https://github.com/zhzhzhy/NinjiaTag-backend>

点赞(0)

打赏

分享

标签：[airtag](https://www.uedbox.com/post/tag/airtag/) , [IOT](https://www.uedbox.com/post/tag/iot/)  原文连接：**[NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐") [最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![浅析 Find My 及 AirTag 原理](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

浅析 Find My 及 AirTag 原理](https://www.uedbox.com/post/69225/ "浅析 Find My 及 AirTag 原理")

[![家庭摄像头会遭遇攻击吗?](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

家庭摄像头会遭遇攻击吗?](https://www.uedbox.com/post/6440/ "家庭摄像头会遭遇攻击吗?")

[![Mysql综合利用工具](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Mysql综合利用工具](https://www.uedbox.com/post/5823/ "Mysql综合利用工具")

[![那些强悍的PHP一句话后门](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

那些强悍的PHP一句话后门](https://www.uedbox.com/post/6051/ "那些强悍的PHP一句话后门")

[![CSDN免积分下载精灵](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

CSDN免积分下载精灵](https://www.uedbox.com/post/5831/ "CSDN免积分下载精灵")

[![用JS给XP的右键加上“打开文件位置”](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

用JS给XP的右键加上“打开文件位置”](https://www.uedbox.com/post/6125/ "用JS给XP的右键加上“打开文件位置”")

[![burpsuite pro v1.4.07破解版](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

burpsuite pro v1.4.07破解版](https://www.uedbox.com/post/4650/ "burpsuite pro v1.4.07破解版")

[![一篇关于360四引擎免杀文章](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

一篇关于360四引擎免杀文章](https://www.uedbox.com/post/5207/ "一篇关于360四引擎免杀文章")

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![最新 绕过Cloudflare最佳实践](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

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

[![让一个 Git 项目丢弃之前的提交历史，只保留当前版本并将其作为最新版](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

让一个 Git 项目丢弃之前的提交历史，只保留当前版本并将其作为最新版](https://www.uedbox.com/post/119343/ "让一个 Git 项目丢弃之前的提交历史，只保留当前版本并将其作为最新版")

* [好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")
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
`体验...