---
title: typecho开源主题Butterfly
url: https://blog.upx8.com/3380
source: 黑海洋 - WIKI
date: 2023-03-31
fetch_date: 2025-10-04T11:15:19.070931
---

# typecho开源主题Butterfly

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# typecho开源主题Butterfly

发布时间:
2023-03-30

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
20832

在typecho控制台点击点击外观后，会自动检测主题最新版本,当你启用主题后点击设置外观，主题会自动提交你的域名到主题作者服务器,本人承诺不会收集你的任何隐私，仅用于统计主题安装量，统计代码采用cdn的方式加载，不会在本地加载并且代码加密，提交采用15位key验证，中途不会发生泄密，提交完成后，会在本地存储提交信息，防止重复提交（当你清除浏览器数据后会重新进行一次），你可以在浏览器控制台查看提交日志。感谢你对主题的支持与理解。

## 主题截图

![](https://img.776161.xyz/img/20230330/3560234047.png)

---

##

# Typecho-Butterfly

[![master version](https://camo.githubusercontent.com/a7d9bebd4b154b8e0e5864cda338b661c8635c5b3b9474140aefac88bdcafa95/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f776568616f782f5479706563686f2d427574746572666c793f736f72743d73656d766572)](https://blog.upx8.com/go/aHR0cHM6Ly9jYW1vLmdpdGh1YnVzZXJjb250ZW50LmNvbS9hN2Q5YmViZDRiMTU0YjhlMGU1ODY0Y2RhMzM4YjY2MWM4NjM1YzViM2I5NDc0MTQwYWVmYWM4OGJkY2FmYTk1LzY4NzQ3NDcwNzMzYTJmMmY2OTZkNjcyZTczNjg2OTY1NmM2NDczMmU2OTZmMmY2NzY5NzQ2ODc1NjIyZjc2MmY3MjY1NmM2NTYxNzM2NTJmNzc2NTY4NjE2Zjc4MmY1NDc5NzA2NTYzNjg2ZjJkNDI3NTc0NzQ2NTcyNjY2Yzc5M2Y3MzZmNzI3NDNkNzM2NTZkNzY2NTcy) [![typecho version](https://camo.githubusercontent.com/689c14f4ba9fd8e5fd6392d914590abad510302fe3f6235ce638a2d90a2a5bec/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5479657063686f2d312e322e302d677265656e)](https://blog.upx8.com/go/aHR0cHM6Ly9jYW1vLmdpdGh1YnVzZXJjb250ZW50LmNvbS82ODljMTRmNGJhOWZkOGU1ZmQ2MzkyZDkxNDU5MGFiYWQ1MTAzMDJmZTNmNjIzNWNlNjM4YTJkOTBhMmE1YmVjLzY4NzQ3NDcwNzMzYTJmMmY2OTZkNjcyZTczNjg2OTY1NmM2NDczMmU2OTZmMmY2MjYxNjQ2NzY1MmY1NDc5NjU3MDYzNjg2ZjJkMzEyZTMyMmUzMDJkNjc3MjY1NjU2ZQ) [![php version](https://camo.githubusercontent.com/1a9616d6ea175ba41658545a93a27f1263e1fa8d5a4776bdf2fe9922690c0362/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5048502d372e342b2d396366)](https://blog.upx8.com/go/aHR0cHM6Ly9jYW1vLmdpdGh1YnVzZXJjb250ZW50LmNvbS8xYTk2MTZkNmVhMTc1YmE0MTY1ODU0NWE5M2EyN2YxMjYzZTFmYThkNWE0Nzc2YmRmMmZlOTkyMjY5MGMwMzYyLzY4NzQ3NDcwNzMzYTJmMmY2OTZkNjcyZTczNjg2OTY1NmM2NDczMmU2OTZmMmY2MjYxNjQ2NzY1MmY1MDQ4NTAyZDM3MmUzNDJiMmQzOTYzNjY) [![license](https://camo.githubusercontent.com/b8ff2be1b6df10e75a63112bd440bfccc533e86bb659f295c96cf596f5243b5b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f776568616f782f5479706563686f2d427574746572666c793f636f6c6f723d464635353331)](https://blog.upx8.com/go/aHR0cHM6Ly9jYW1vLmdpdGh1YnVzZXJjb250ZW50LmNvbS9iOGZmMmJlMWI2ZGYxMGU3NWE2MzExMmJkNDQwYmZjY2M1MzNlODZiYjY1OWYyOTVjOTZjZjU5NmY1MjQzYjViLzY4NzQ3NDcwNzMzYTJmMmY2OTZkNjcyZTczNjg2OTY1NmM2NDczMmU2OTZmMmY2NzY5NzQ2ODc1NjIyZjZjNjk2MzY1NmU3MzY1MmY3NzY1Njg2MTZmNzgyZjU0Nzk3MDY1NjM2ODZmMmQ0Mjc1NzQ3NDY1NzI2NjZjNzkzZjYzNmY2YzZmNzIzZDQ2NDYzNTM1MzMzMQ)

这是 Typecho 版本的 butterfly 主题 主题好看，但是由于经常换设备并且hexo操作还是不方便，某些功能受限于第三方 所以就移植了

原主题：[hexo-butterfly](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2plcnJ5YzEyNy9oZXhvLXRoZW1lLWJ1dHRlcmZseQ)

Demo：[WeHao‘s Blog](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLndlaGFveC5jb20v)

使用文档：[使用文档](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLndlaGFveC5jb20vYXJjaGl2ZXMvdHlwZWNoby1idXR0ZXJmbHkuaHRtbA)

## 安装

你最好从[Release](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3dlaGFveC9UeXBlY2hvLUJ1dHRlcmZseS9yZWxlYXNlcw) 页面下载，code页下载代码可能更新遗漏或者更新提前导致页面出错
下载好后放进博客usr/theme内解压即可

## 帮助主题发展(加快更新)

* 如果你发现主题bug或者建议可以去[issues](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3dlaGFveC9UeXBlY2hvLUJ1dHRlcmZseS9pc3N1ZXM)提交反馈
* 如果你一定能力可以向主题提交[PR](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3dlaGFveC9UeXBlY2hvLUJ1dHRlcmZseS9wdWxscw)来丰富主题
* 如果你只是一个普通是使用者，你可以在右上角给主题点一个[star](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3dlaGFveC9UeXBlY2hvLUJ1dHRlcmZseS9zdGFyZ2F6ZXJz)来鼓励作者来加快更新

## 移植特色

1. 方便原hexo的博文转移，因为都是md文档
2. 原butterfly的用户可以直接使用原版butterfly主题的css文件，拥有原先同样的效果
3. 注意：移植并非为最新版butterfly,你的index.css可能会在本主题出现bug
4. 由于使用动态博客，大部分功能可以让程序去实现，不用借助第三方api(可在主题外观设置中自定义)
5. 在线编辑文档
6. 搜索、加密和置顶文章可以直接使用(相比hexo无需太多额外配置)
7. 相比hexo，程序安装更加方便，使用更加高效
8. 网站咨询显示同时在线人数(某些虚拟主机似乎无法使用)
9. 可在后台设置侧边栏信息以及侧边栏的隐藏和显示
10. 后续将开发更多功能

## 已实现的功能

* [x]
* [x]  全站加密或禁止访问
* [x]  一键开启魔改主题
* [x]  单独设置文章过期提醒
* [x]  文章加密（博客程序自带）
* [x]  后台设置需要置顶文章
* [x]  后台设置友链并可以使html自定义友链
* [x]  文章内可设置回复可见
* [x]  卡片化设计
* [x]  支持二级目录
* [x]  双栏设计
* [x]  响应式主题
* [x]  夜间模式
* [x]  Pjax
* [x]  文章阅读模式
* [x]  简体和繁体转换
* [x]  电脑和手机都可查看TOC目录
* [ ]  内置多种代码配色（darker/pale night/light/ocean/mac/mac light），可自定义代码配色
* [x]  代码块显示代码语言/关闭或展开代码块/代码复制/代码自动换行
* [ ]  可关闭文字复制/可开启内容复制增加版权信息）
* [x]  本地搜索
* [ ]  Mathjax 和 Katex
* [x]  内置404页面
* [x]  显示字数统计
* [x]  显示相关文章
* [x]  过期文章提醒
* [ ]  多种在线聊天（Chatra/Tidio/Daovoice/Gitter/Crisp）
* [x]  谷歌广告/手动广告位置
* [x]  修改网站配色
* [ ]  打字特效 activate\_power\_mode
* [ ]  多种背景特效（静止彩带/动态彩带/Canvas Nest）
* [x]  多种鼠标点击特效（烟花/爱心）
* [ ]  内置一种 Preloader 加载动画
* [x]  Fancybox大图模式
* [ ]  照片墙
* [x]  图片懒加载
* [x]  Snackbar弹窗
* [ ]  PWA

---

## 主题下载

[https://pan.wehaox.com/s/jbauV?path=%2F](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ud2VoYW94LmNvbS9zL2piYXVWP3BhdGg9JTJG)

[https://github.com/wehaox/Typecho-Butterfly](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3dlaGFveC9UeXBlY2hvLUJ1dHRlcmZseQ)

[取消回复](https://blog.upx8.com/3380#respond-post-3380)

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