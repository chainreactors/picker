---
title: 利用Cloudflare Worker部署免费的短链接平台
url: https://buaq.net/go-263256.html
source: unSafe.sh - 不安全
date: 2024-09-22
fetch_date: 2025-10-06T18:20:36.169092
---

# 利用Cloudflare Worker部署免费的短链接平台

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c8556ad356fdc6ffd6beef540357de4f.jpg)

利用Cloudflare Worker部署免费的短链接平台

介绍：020短链，利用Cloudflare Worker实现的简单免费的短链接平台部署方法：第一步：创建命名空间进入Workers & Pages栏目下
*2024-9-21 17:50:56
Author: [www.upx8.com(查看原文)](/jump-263256.htm)
阅读量:22
收藏*

---

## 介绍：

020短链，利用Cloudflare Worker实现的简单免费的短链接平台

## 部署方法：

### 第一步：创建命名空间

进入`Workers & Pages`栏目下的`KV`项目![](https://pic.imgdb.cn/item/64d502f81ddac507cc94dac2.jpg)

创建一个命名空间，点击`Create a namespace`

![](https://pic.imgdb.cn/item/64d503801ddac507cc964ac1.jpg)

记住创建的这个空间名称，一会要用

![](https://pic.imgdb.cn/item/64d503a81ddac507cc96c162.jpg)

## 第二步：创建Worker

进入`Workers & Pages`栏目下的`Overview`项目

点击`Create application`

![](https://pic.imgdb.cn/item/64d5048e1ddac507cc993c2c.jpg)

点击`Create Worker`

![](https://pic.imgdb.cn/item/64d504b21ddac507cc99a44a.jpg)

点击`deploy`

![](https://pic.imgdb.cn/item/64d505921ddac507cc9c1c86.jpg)

## 第三步：配置Worker

点击`Configure Worker`

![](https://pic.imgdb.cn/item/64d505d71ddac507cc9cdaf3.jpg)

进入`Settings`栏目下的`Variables`项目

![](https://pic.imgdb.cn/item/64d507f91ddac507cca30b42.jpg)

绑定`KV Namespace`

其中`Variable name`填写`LINKS`, `KV namespace`填写你刚刚创建的命名空间名称

![](https://pic.imgdb.cn/item/64d508601ddac507cca42fd8.jpg)

在`Triggers`中修改域名

![](https://pic.imgdb.cn/item/64d507391ddac507cca0ccdb.jpg)

例如这样：

![](https://pic.imgdb.cn/item/64d507701ddac507cca16ab9.jpg)

点击页面上方的`Quick edit`

![](https://pic.imgdb.cn/item/64d508aa1ddac507cca50aae.jpg)

填入以下内容

可以修改如下环境变量，Key均为对应大写：

![](https://pic.imgdb.cn/item/64d509611ddac507cca7173f.jpg)

1. 调整超时设置

演示模式生成的短链接超时无法访问，

2. 调整白名单

白名单中的域名设置短链接无视超时，
修改脚本开头的变量*white\_list*, 是个json数组，写顶级域名就可以，自动通过顶级域名和所有二级域名，

3. 关闭演示模式

只有演示模式开启才允许访客无密码添加非白名单地址，超时短链接会失效，
修改脚本开头的变量*demo\_mode*，为true开启演示，为false无密码且非白名单请求不受理，

4. 自动删除演示记录

针对演示模式开启情况下的超时失效的短链接记录是否自动删除，
修改脚本开头的变量*remove\_completely*，为true自动删除超时的演示短链接记录，否则仅是标记过期，以便在后台查询历史记录，

5. 修改密码

网页有个隐藏输入框可以输入密码，
密码正确情况无视白名单和超时设置，且支持自定义短链接，
修改脚本开头的变量*password*，这个私密信息比较建议直接在环境变量里配置，

6. 修改短链长度

短链长度就是随机生成的key也就是短链接的path部分的长度，
长度不够时容易出现重复，遇到重复时会自动延长，
修改脚本开头的变量*default\_len*,

## 相关地址：

GitHub地址：<https://github.com/AoEiuV020/Url-Shorten-Worker>
Demo：[https://020.name](https://020.name/)

文章来源: https://www.upx8.com/4344
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)