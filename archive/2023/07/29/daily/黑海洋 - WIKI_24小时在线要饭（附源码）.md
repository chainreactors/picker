---
title: 24小时在线要饭（附源码）
url: https://blog.upx8.com/3718
source: 黑海洋 - WIKI
date: 2023-07-29
fetch_date: 2025-10-04T11:54:59.825429
---

# 24小时在线要饭（附源码）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 24小时在线要饭（附源码）

发布时间:
2023-07-28

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
18324

# 7X24小时在线要饭?，欢迎?各位老板打赏，打赏一分也是爱

1. 纯原生js手撸，无任何框架
2. 不用数据库，不用部署服务器上
3. 零成本，代码部署GitHub，CF托管加速，数据托管在`leancloud`
4. 移动端交互体验超棒，一键打赏，免去app来回切换
5. 微信内分享打赏更方便，长按即可（需域名备案

# 食用教程：

## 克隆代码

`git clone https://github.com/yong-s/alms.git`

## 修改配置

### 替换为自己的收款码

在`images`内分别替换微信、支付宝的收款码

### 替换为自己的scheme url

支付宝替换：`qrcode`后面的值改为自己的收款码链接

`alipays://platformapi/startapp?saId=10000007&qrcode=https%3A%2F%2Fqr.alipay.com%2Ffkx17568wleuqk0ebdb8ia3`

### 替换为自己的leancloud API key

1. 没有去注册[leancloud](https://blog.upx8.com/go/aHR0cHM6Ly9jb25zb2xlLmxlYW5jbG91ZC5hcHAvYXBwcw)，国际版不用备案
2. 使用开发版（免费
3. 设置-应用凭证-复制`AppKey`
4. `custom.js`内修改`App_Key`为上一步复制的
5. 国际版需要使用自定义的域名，`API_BASE_URL` 改为自己的，先去设置-域名绑定

## 部署

### GitHub pages等服务器

通过GitHub pages，域名托管在cloudflare上，几块钱买一年的域名，完美搞定

### 对象存储

优点：免去域名备案，微信内直接打开，腾讯云cos按量计费 缺点：?️，要说有，就是不知道这个口子啥时候会被关了

1. 去腾讯☁️后台，找到对象存储，新建存储桶，基础配置，静态网站打开
2. 上传`index.html` `assets` `images`
3. 直接访问给的域名即可

# TO DO

* [x]
* [ ]  国际化，中英文显示
* [ ]  支持国际（PayPal）收款，开启全世界要饭模式?
* [ ]  支持加密货币收款₿

# 感谢

1. 模版来自[HTML5 UP](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3lvbmctcy9hbG1zL2Jsb2IvbWFpbi9odG1sNXVwLm5ldA)
2. [部分灵感参考](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0RvbWVlbm9IL0hleG8tRG9uYXRl)
3. [donate](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLmRvbWlub2guY29tL2RvbmF0ZQ)
4. 感谢ChatGPT?，纯原生js，通过GPT辅助完成✅
5. 感谢Midjourney?提供背景图片
6. [favicon](https://blog.upx8.com/go/aHR0cHM6Ly9mYXZpY29uLmlvL2Vtb2ppLWZhdmljb25zL2Jvd2wtd2l0aC1zcG9vbi8)提供favicon支持

[取消回复](https://blog.upx8.com/3718#respond-post-3718)

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