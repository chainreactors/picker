---
title: UptimeRobot 状态监测监控页
url: https://blog.upx8.com/3290
source: 黑海洋 - WIKI
date: 2023-03-19
fetch_date: 2025-10-04T10:02:53.802196
---

# UptimeRobot 状态监测监控页

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# UptimeRobot 状态监测监控页

发布时间:
2023-03-18

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
11089

![](https://img.776161.xyz/img/20230318/2577302713.jpg)

demo：[https://status.nange.cn](https://blog.upx8.com/go/aHR0cHM6Ly9zdGF0dXMubmFuZ2UuY24v)

Github项目：[https://github.com/hadis898/UptimeRobot](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2hhZGlzODk4L1VwdGltZVJvYm90)

修改说明：

1. 前端改为中文显示；
2. 改变页面显示宽度；
3. 修改显示数据为最近 60 天（原版 45 天）；
4. 增加显示当前日期数据（原版只显示到前一天）；
5. 修改时区为东八区；
6. 其它布局微调。

#### 安装部署

##### Docker 环境下部署使用

* 获取 Docker 文件

```
wget https://raw.githubusercontent.com/hadis898/UptimeRobot/master/docker-compose.yml
```

* 修改配置文件 `docker-compose.yml`

```
version: "3"

services:
  status:
    image: nangle/status-page
    # build: .
    environment:
      - PORT=3000
      - LOG_LEVEL=info
      - CRON_TIME=*/1 * * * *
      - UPTIME_ROBOT_API=ur94****-4d**687*****a1917******
      - UPTIME_ROBOT_NAME_PATTERN=%group|%index|%name
      - WEBSITE_TITLE=服务状态
      - WEBSITE_COPYRIGHT=楠格
    # To use config file for more flexible configure,
    # please uncomment next block
    # volumes:
     #  - ./config:/app/config
    ports:
      - 127.0.0.1:8082:3000
```

* 启动

```
docker-compose up -d
```

* Nginx 反代 `8082` 端口或直接访问 `ip:8082` 即可。

##### 常规环境下部署使用

* 克隆代码

```
git clone https://github.com/hadis898/UptimeRobot.git && cd StatusPage
```

安装依赖

```
npm i && yarn install && yarn cache clean
```

* 构建

```
yarn build
```

* 修改 config/default.yml
* 运行

```
node build/bootstrap
```

* Nginx 反代 `3000` 端口或直接访问 `ip:3000` 即可。

[取消回复](https://blog.upx8.com/3290#respond-post-3290)

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