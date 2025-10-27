---
title: AAB 打包及上架GOOGLE PLAY流程
url: https://blog.upx8.com/3083
source: 黑海洋 - WIKI
date: 2022-11-13
fetch_date: 2025-10-03T22:38:08.454939
---

# AAB 打包及上架GOOGLE PLAY流程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# AAB 打包及上架GOOGLE PLAY流程

发布时间:
2022-11-12

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
16621

AAB 即 Android App Bundle，是 Google 官方发布的一种新的 App 包格式，可以有效缩减 App 大小，提升用户安装和更新 App 的体验。从 8 月开始，在 Google Play 上架的 App 需要强制提交 AAB 格式，这对安卓 App 开发者以及 App 保护都有重大影响。以下介绍如何生成AAB包及在Google上架的流程。

## 1.生成 AAB 包

1、 在 Android Studio 工程界面，选择 Build->Cenerate Signed Bundle/APK 选项。

![](https://blog.virbox.com/wp-content/uploads/2021/07/generate-1.png)

选择 Build->Cenerate Signed Bundle/APK

2、选择要编译程序的类型-AndroidApp Bundle，点击 Next

![](https://blog.virbox.com/wp-content/uploads/2021/07/aab-1.png)

选择Android App Bundle

3、选择签名文件，输入别名和密钥（若没有可重新创建生成），点击Next

![](https://blog.virbox.com/wp-content/uploads/2021/07/sign-1.png)

选择签名文件

4、选择Build->Build Bundle(s)/APK(s)->Bunild Bundle(s)，Build成功后，生成aab包

![](https://blog.virbox.com/wp-content/uploads/2021/07/build_aab-1.png)

Build->Build Bundle(s)/APK(s)->Bunild Bundle(s)

以上就是快速生成 AAB 包的流程，生成 AAB 包后，如果需要对其代码做安全加固，可以使用 **Virbox Protector** 对 AAB 包进行加密，加密完成后，即可进行下一步的操作，即在Google Play 上架。

## 2.Google Play上架流程

### 2.1 创建应用

> 以 sense aab 包为例：
>
> 默认语言：en-GB
>
> 游戏类别：App
>
> 是否付费：Free

在 Create app 界面，设置 App name、Default language、App or game、Free or paid

![](https://blog.virbox.com/wp-content/uploads/2021/07/create_app_1-1.png)

## 2.2应用设置

### 2.2.1 app详情

1、填写应用名称及应用说明。

![](https://blog.virbox.com/wp-content/uploads/2021/07/app_details_2-2-1024x692.png)

2、上传icon（512 \* 512），置顶大图（1024 \* 500）和至少两张iphone截图即可。

平板电脑根据自己应用程序来提交。

![](https://blog.virbox.com/wp-content/uploads/2021/07/graphics_3-1.png)

### 2.2.2 商店设置

1、选择app的类型

![](https://blog.virbox.com/wp-content/uploads/2021/07/store_3-1.png)

2、输入电子邮箱、电话号码和产品网站

![](https://blog.virbox.com/wp-content/uploads/2021/07/store_4.png)

3、选择是否在 Google Play 之外宣传您的应用。

再次选择勾选。

![](https://blog.virbox.com/wp-content/uploads/2021/07/store_5.png)

### 2.2.3设置商品详情

1、应用访问权限，选择第一个：所有功能均无需特殊访问权限即可使用

![](https://blog.virbox.com/wp-content/uploads/2021/07/d_app_1.png)

2、选择app中是否包含广告

![](https://blog.virbox.com/wp-content/uploads/2021/07/d_ads_2.png)

3、应用程序的评估

![](https://blog.virbox.com/wp-content/uploads/2021/08/d_rat_3-1024x457.png)

4、选择app的类别。

![](https://blog.virbox.com/wp-content/uploads/2021/08/d_cate_4-1024x761.png)

5、app内容涉及，根据自己app需求选择。

![](https://blog.virbox.com/wp-content/uploads/2021/08/d_cate_5.png)
![](https://blog.virbox.com/wp-content/uploads/2021/08/d_cate_6.png)
![](https://blog.virbox.com/wp-content/uploads/2021/08/d_cate_7-1024x553.png)

6、连续下一步，最后保存提交即可。

### 2.2.4目标受众群体

![](https://blog.virbox.com/wp-content/uploads/2021/08/d_8.png)

### 2.2.5新闻应用

选择程序是否包含新闻

![](https://blog.virbox.com/wp-content/uploads/2021/08/d_9.png)

## 2.3应用发布

1、创建发布版本

![](https://blog.virbox.com/wp-content/uploads/2021/08/create_relese_6-1024x388.png)

2、签名选项设置

![](https://blog.virbox.com/wp-content/uploads/2021/08/sign_7-1024x607.png)

3、签名设置分为以下四个

根据自己需求选择

![](https://blog.virbox.com/wp-content/uploads/2021/08/sign_8.png)

以下为每个选项的具体截图

![](https://blog.virbox.com/wp-content/uploads/2021/08/sign_9.png)
![](https://blog.virbox.com/wp-content/uploads/2021/08/sign_10.png)
![](https://blog.virbox.com/wp-content/uploads/2021/08/sign_11.png)

5、上传aab包

输入应用名称和简短描述

![](https://blog.virbox.com/wp-content/uploads/2021/08/app_build_12.png)

6、保存配置，选择发布即可。

以上就是整个 aab 包发布及在Google Play 上架的流程文档。

[取消回复](https://blog.upx8.com/3083#respond-post-3083)

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