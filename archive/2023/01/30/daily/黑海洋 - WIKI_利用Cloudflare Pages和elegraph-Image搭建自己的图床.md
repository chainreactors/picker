---
title: 利用Cloudflare Pages和elegraph-Image搭建自己的图床
url: https://blog.upx8.com/3205
source: 黑海洋 - WIKI
date: 2023-01-30
fetch_date: 2025-10-04T05:10:37.875854
---

# 利用Cloudflare Pages和elegraph-Image搭建自己的图床

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 利用Cloudflare Pages和elegraph-Image搭建自己的图床

发布时间:
2023-01-29

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
13737

**一、Telegraph-Image的特色**

1.无限图片储存数量，你可以上传不限数量的图片
2.无需购买服务器，托管于Cloudflare的网络上，当使用量不超过Cloudflare的免费额度时，完全免费
3.无需购买域名，可以使用Cloudflare Pages提供的\*.pages.dev的免费二级域名，同时也支持绑定自定义域名
4.支持图片审查API，可根据需要开启，开启后不良图片将自动屏蔽，不再加载

**二、Telegraph-Image的安装**

1.下载或是Fork本仓库：[https://github.com/cf-pages/Telegraph-Image](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2NmLXBhZ2VzL1RlbGVncmFwaC1JbWFnZQ)

2.打开Cloudflare Dashboard，进入Pages管理页面，选择创建项目，如果在第一步中选择的是fork本仓库，则选择连接到 Git 提供程序，如果第一步中选择的是下载本仓库则选择直接上传

[![Telegraph-Image：利用Cloudflare Pages和Telegraph无成本创建自己的图床](https://zhujiwiki.com/wp-content/uploads/2022/12/Telegraph-Image-1.png)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubGFvbGl1YmxvZy5jbi9nbz91cmw9YUhSMGNITTZMeTk2YUhWcWFYZHBhMmt1WTI5dEwzZHdMV052Ym5SbGJuUXZkWEJzYjJGa2N5OHlNREl5THpFeUwxUmxiR1ZuY21Gd2FDMUpiV0ZuWlMweExuQnVadz09)

3、按照页面提示输入项目名称，选择需要连接的git仓库（第一步选择的是fork）或是上传刚刚下载的仓库文件（第一步选择的是下载本仓库），点击部署站点即可完成部署

4、绑定自定义域名

在pages的自定义域里面，绑定cloudflare中存在的域名，在cloudflare托管的域名，自动会修改dns记录

[![Telegraph-Image：利用Cloudflare Pages和Telegraph无成本创建自己的图床](https://zhujiwiki.com/wp-content/uploads/2022/12/Telegraph-Image-2.png)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubGFvbGl1YmxvZy5jbi9nbz91cmw9YUhSMGNITTZMeTk2YUhWcWFYZHBhMmt1WTI5dEwzZHdMV052Ym5SbGJuUXZkWEJzYjJGa2N5OHlNREl5THpFeUwxUmxiR1ZuY21Gd2FDMUpiV0ZuWlMweUxuQnVadz09)

**三、开启图片审查**

1.请前往[https://moderatecontent.com/](https://blog.upx8.com/go/aHR0cHM6Ly9tb2RlcmF0ZWNvbnRlbnQuY29tLw) 注册并获得一个免费的用于审查图像内容的API key

2.打开Cloudflare Pages的管理页面，依次点击设置，环境变量，添加环境变量

3.添加一个变量名称为ModerateContentApiKey，值为你刚刚第一步获得的API key，点击保存即可

注意：由于所做的更改将在下次部署时生效，你或许还需要进入部署页面，重新部署一下该本项目

开启图片审查后，因为审查需要时间，首次的图片加载将会变得缓慢，之后的图片加载由于存在缓存，并不会受到影响

[![Telegraph-Image：利用Cloudflare Pages和Telegraph无成本创建自己的图床](https://zhujiwiki.com/wp-content/uploads/2022/12/Telegraph-Image-3.png)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubGFvbGl1YmxvZy5jbi9nbz91cmw9YUhSMGNITTZMeTk2YUhWcWFYZHBhMmt1WTI5dEwzZHdMV052Ym5SbGJuUXZkWEJzYjJGa2N5OHlNREl5THpFeUwxUmxiR1ZuY21Gd2FDMUpiV0ZuWlMwekxuQnVadz09)

**四、Telegraph-Image的Limitations**

1.由于图片文件实际存储于Telegraph，Telegraph限制上传的图片大小最大为5MB

2.由于使用Cloudflare的网络，图片的加载速度在某些地区可能得不到保证

3.Cloudflare Function免费版每日限制100,000个请求（即上传或是加载图片的总次数不能超过100,000次）如超过可能需要选择购买Cloudflare Function的付费套餐

已开源：[https://github.com/cf-pages/Telegraph-Image](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2NmLXBhZ2VzL1RlbGVncmFwaC1JbWFnZQ)
可讨论：[https://hostloc.com/thread-1092595-1-1.html](https://blog.upx8.com/go/aHR0cHM6Ly9ob3N0bG9jLmNvbS90aHJlYWQtMTA5MjU5NS0xLTEuaHRtbA)

[取消回复](https://blog.upx8.com/3205#respond-post-3205)

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