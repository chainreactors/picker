---
title: 上架Google马甲包 思路 攻略 等
url: https://blog.upx8.com/3075
source: 黑海洋 - WIKI
date: 2022-11-13
fetch_date: 2025-10-03T22:38:09.208091
---

# 上架Google马甲包 思路 攻略 等

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 上架Google马甲包 思路 攻略 等

发布时间:
2022-11-12

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
12436

# 1.Google马甲封掉的大致原因

①. 上过马甲包的同学都知道，Google审核马甲包特别的严格变态，一般来说，审核时间越久，越容易出问题，通常都是机器审核后有问题，会交给人工审核， 一般机器审核差不多两到三个工作日，如果，三到四个工作日没出结果，十有八九这个马甲是有问题的

②. 关联问题，最为严重的和值得思考的问题，咋也不知道Google的审核是怎么判断关联的，个人通过上架很多马甲包得出这几个途径，

1：class文件高度相似，2：res资源文件和xml布局文件   3：后台数据返回格式  4：Google账号及环境   5：马甲UI   6：电脑关联

其实仔细想一想，差不多这几大类。

# 2.Google解决封掉办法

①：再此之前，可以了解下 [Google混淆](https://blog.upx8.com/go/aHR0cHM6Ly9saW5rcy5qaWFuc2h1LmNvbS9nbz90bz1odHRwcyUzQSUyRiUyRmp1ZWppbi5jbiUyRnBvc3QlMkY3MDc5OTU1MDE0ODIyNjc0NDY4JTNGc2hhcmVfdG9rZW4lM0RmNjc1NTlmYS0yMDk5LTQzOWItOTgxNS1kYTZhMWRmNzUzOTg) 这篇文章，提升马甲时间

②：想解决马甲被封，被关联，最重要的就是要新，最好不要和上一个马甲有任何关联，视作一个新包来看待

③：自己总结的几点经验：从项目来说

1.必须要创建新的项目，创建新的包名，

2.项目中所有的lib和module最好打乱，路径子目录最好每次都打乱，

3.所有的类名，路径，xml中的id必须更换名字，res图片让ui更换MD5，马甲ui首页最好每次都换种不同的风格

4.混淆可以用上面这个，部分java类可以转kotlin，kotlin可以转转java等，保证最大程度与旧包不一致

5.关联问题： 每次必须用新的Google账号，包括电脑，上一个马甲，必须换掉电脑，每个电脑只能上架一个马甲包，每个电脑，每个马甲包，必须都要有一个大陆外的手机卡，用来测试，或者上架时，当作vpn来打包使用，也就是一个马甲包一个大陆之外得IP

6.最好不要测试，先上架，审核通过后，再从GooglePlay中下载测试，

7.新马甲项目，必须要在新的电脑上，创建jks文件，不要再自己电脑上创建，创建jks文件的时候，可以连接新手机(大陆之外的手机卡)进行创建，包括生成sha1和256及散列密钥，这些都要保证在新的设备上获取

8.打包aab的时候，也必须链接新手机(大陆之外的手机卡)进行打包。有些同学说vpn不行吗，说实话，如果做过vpn的话，就知道，这个真不行，不信可以用vpn进行打包，

9.大致就是：每个马甲都要对应一套新设备如：大陆之外手机卡   新电脑  新项目  新账户，以免产生关联     代码 目录结构，能多改就多改！ui，能变就变！数据返回格式，能改就改(不用太大改动,就比如每个马甲包返回的时候，外层再套一层大的data)！

# 3.XmlClassGuard混淆任意类，上架GooglePlay的杀手锏利器

[Google混淆](https://blog.upx8.com/go/aHR0cHM6Ly9saW5rcy5qaWFuc2h1LmNvbS9nbz90bz1odHRwcyUzQSUyRiUyRmp1ZWppbi5jbiUyRnBvc3QlMkY3MDc5OTU1MDE0ODIyNjc0NDY4JTNGc2hhcmVfdG9rZW4lM0RmNjc1NTlmYS0yMDk5LTQzOWItOTgxNS1kYTZhMWRmNzUzOTg)  这个是大佬的最新的一篇混淆文章，可以用这个，节省时间

在这里，自己也用几次，打算把整个实现流程写下来，说实话，这个是真的很好用，希望后面的同学不要在这个地方踩坑，在这里就不过多描述了直接上步骤，简单易懂

1.万物万事先倒依赖

> **maven{ url’https://raw.githubusercontent.com/martinloren/AabResGuard/mvn-repo’ }**
>
> **classpath”com.bytedance.android:aabresguard-plugin:0.1.6″**
>
> **classpath”com.github.liujingxing:XmlClassGuard:1.0.1″**

![](https://googleplayaab.com/wp-content/uploads/2022/08/image-7-1024x661.png)

2. 在app中添加，多module中，其余的不用配，只需要在app中

> applyplugin:”xml-class-guard”
>
> applyfrom:’aabresguard.gradle’

![](https://googleplayaab.com/wp-content/uploads/2022/08/image-8-1024x188.png)

3.运行

![](https://googleplayaab.com/wp-content/uploads/2022/08/image-9.png)

4.这个工具需要在新版上运行  要下载最新版as，gradle必须是7.2  别的版本会报错  [as官网](https://blog.upx8.com/go/aHR0cHM6Ly9saW5rcy5qaWFuc2h1LmNvbS9nbz90bz1odHRwcyUzQSUyRiUyRmRldmVsb3Blci5hbmRyb2lkLmdvb2dsZS5jbiUyRnN0dWRpbyUyRiUyM2Rvd25sb2Fkcw)

![](https://googleplayaab.com/wp-content/uploads/2022/08/image-10.png)
![](https://googleplayaab.com/wp-content/uploads/2022/08/image-11-1024x233.png)

> 如有报错，或者 xml-class-mapping.txt 文件抱错，请在评论区留言，

最后，aabresguard 白名单配置，在app目录下   如下，，请自行创建白名单文件，这里发不了

![](https://googleplayaab.com/wp-content/uploads/2022/08/image-12-1024x425.png)

> applyplugin:”com.bytedance.android.aabResGuard”
>
> aabResGuard{
>
> //    mappingFile = file(“mapping.txt”).toPath() // 用于增量混淆的 mapping.txt 文件
>
>     // 白名单规则
>
>     whiteList = [
>
> “\*.R.raw.\*”,
>
> ]
>
> obfuscatedBundleFileName =”mua.aab” // 混淆后的文件名称，必须以 `.aab` 结尾
>
>     mergeDuplicatedRes =true // 是否允许去除重复资源
>
>     enableFilterFiles =true // 是否允许过滤文件
>
>     // 文件过滤规则
>
>     filterList = [
>
> “\*/arm64-v8a/\*”,
>
> “META-INF/\*”
>
>     ]
>
> enableFilterStrings =false // 过滤文案
>
>     unusedStringPath = file(“unused.txt”).toPath()// 过滤文案列表路径 默认在mapping同目录查找
>
>     languageWhiteList = [“en”,”in”]// 保留en,en-xx,zh,zh-xx等语言，其余均删除
>
> }

[取消回复](https://blog.upx8.com/3075#respond-post-3075)

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