---
title: 云打包系统搭建
url: https://blog.upx8.com/3229
source: 黑海洋 - WIKI
date: 2023-02-22
fetch_date: 2025-10-04T07:43:21.611522
---

# 云打包系统搭建

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 云打包系统搭建

发布时间:
2023-02-21

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
15767

## 功能介绍

- 支持打包ios应用
- ios带绿标域名（可自定义域名）
- ios不跳转浏览器
- ios顶部无网址显示（更逼真）
- 一次打包终身使用
- 自助本地打包（不是接口版本）
- 安卓可注入js.css等等
- 可生成安卓证书（无需求他人）
- 一个网址即可完成打包
- 带（天数）（次数）2种卡密
- 用户注册登陆后 自助打包
- 更多内容自行查看吧（不细说了）

## 技术栈

- 语言：nodejs java
- Web框架：express框架
- 日志：无
- 数据库： SQLite
- API文档：更新中

## 安装教程

默认后台信息【第一次运行默认密码 admin 123456 】
- 前台地址：IP或域名:5088/pack
- 后台地址：IP或域名:5088/admin

## Tips:

 - 防止泛滥（需要许可）（免费）
- 用户任何用途于原作者无关
- 使用node 16.15.0 版本 其他可能会有不可预知的问题

**安装方式一：PM2启动守护（分步骤安装启动）**

1. `strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX`
3. `#系统缺失libstdc.so_.6.0.26 执行如下命令 查看有否GLIBCXX 1.3.8`
5. `cd /usr/local/lib64/`
6. `` # 下载最新版本的`下载最新版本的libstdc.so_.6.0.26` ``
7. `wget http://www.vuln.cn/wp-content/uploads/2019/08/libstdc.so_.6.0.26.zip`
8. `# 解压`
9. `unzip libstdc.so_.6.0.26.zip`
10. `# 将下载的最新版本拷贝到 /usr/lib64`
11. `cp libstdc++.so.6.0.26 /usr/lib64`
12. `cd /usr/lib64`
13. `# 查看 /usr/lib64下libstdc++.so.6链接的版本`
14. `ls -l | grep libstdc++`
15. `# 删除原先的软连接(不放心可以备份)`
16. `rm libstdc++.so.6`
17. `# 使用最新的库建立软连接`
18. `ln -s libstdc++.so.6.0.26 libstdc++.so.6`
19. `# 查看新版本，成功`
20. `strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX`
22. `# 安装程序额外的java 环境`
23. `yum install -y wget && wget -O install.sh --no-check-certificate https://cdn.365api.cn/onePack/Pack.sh && sh install.sh`
25. `# 下载程序`
26. `git https://github.com/souying/APP.git`
28. `# 进程序目录`
29. `cd xxx`
31. `# 安装依赖`
32. `npm install`
34. `# 启动`
35. `npm start`
37. `# PM2启动`
38. `pm2 start bin/www`

**安装方式二、Docker 暂时不支持**#脚本一键安装

1. `yum install -y wget && wget -O install.sh --no-check-certificate https://cdn.365api.cn/onePack/onePack.sh && sh install.sh`

## 开发计划

开发计划 & 进度：暂定

**【联系方式】**

github：[https://github.com/souying/APP](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3NvdXlpbmcvQVBQ)   欢迎star

tg频道：[https://t.me/saobingtt](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL3Nhb2Jpbmd0dA)

[取消回复](https://blog.upx8.com/3229#respond-post-3229)

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