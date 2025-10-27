---
title: Feiyang Digital Telegram 群管机器人
url: https://blog.upx8.com/4730
source: 黑海洋 - Wiki
date: 2025-04-11
fetch_date: 2025-10-06T22:05:14.028761
---

# Feiyang Digital Telegram 群管机器人

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Feiyang Digital Telegram 群管机器人

发布时间:
2025-04-10

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
84423

![](https://cdn.skyimg.de/up/2025/4/10/jvxapz.webp)

基于 **SpringBoot** 和 **Telegrambot-Api** 打造的多功能 Telegram 群管理机器人，有效查杀18+违规视频、贴图、图片，AI识别各种博彩，违规图片、文字，可设置正则自定义关键字回复、违规词汇删除等功能，支持每日词云统计，进群欢迎等多种实用群管功能，**Powered By OpenAI And Google Cloud Vision**。

## 1️⃣ 开始之前

# 强烈推荐观看保姆级部署视频教程：[点击观看](https://blog.upx8.com/go/aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj1RZ3JQUmdSNXRlaw)

# 使用文档：[点击下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4udjEubWsvJUU2JUFGJThGJUU2JTlDJTlGJUU4JUE3JTg2JUU5JUEyJTkxJUU0JUI4JUFEJUU3JTk0JUE4JUU1JTg4JUIwJUU3JTlBJTg0JUU2JTk2JTg3JUU0JUJCJUI2JUU1JTg4JTg2JUU0JUJBJUFCLyVFNSVBRiU4NiVFNyVBMCU4MTEyMy0yMDIzLjA5LjI1JUU2JTlDJTlGLnppcA)

* **创建你的 Telegram 机器人:**

  1. 前往 [@BotFather](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL2JvdGZhdGhlcg) 以创建机器人。
  2. 记录下机器人的 `token` 和用户名。
  3. 不熟悉的话，可以[查阅此具体步骤](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3doYXRkYXkvYXJ0aWNsZS9kZXRhaWxzLzExMzc0NzI5NA)。
* **准备环境:**

  + [安装 Docker 和 Docker-Compose](https://blog.upx8.com/go/aHR0cHM6Ly93d3cud3h5OTcuY29tL2FyY2hpdmVzLzc3)。

## 2️⃣ 终端运行

```
curl -o start.sh https://ghproxy.com/https://raw.githubusercontent.com/youshandefeiyang/feiyangdigital-bot/main/start.sh && chmod +x start.sh && ./start.sh
```

## 3️⃣ 配置机器人

* 前往 `/home/feiyangdigitalbotconf/` 目录，编辑 `conf.json` 文件：
  1. 填入你的 `username` 和 `token` 到 `botConfig` 的 `name` 和 `token` 字段。
  2. 保存更改。

## ▶️ 运行机器人

* 确保你的网络可以连接到 Telegram 服务器。如果使用软路由，请使用增强代理。
* 在 `/home/feiyangdigitalbotconf/` 目录下执行：

```
docker-compose up -d
```

## ⏸️ 暂停容器

* 在 `/home/feiyangdigitalbotconf/` 目录下执行：

```
docker-compose stop
```

## 🔥 重启容器

* 在 `/home/feiyangdigitalbotconf/` 目录下执行：

```
docker-compose restart
```

## 🔍 查看日志

在 `/home/feiyangdigitalbotconf/` 目录下执行：

```
docker-compose logs -f
```

## 🔄 更新

在 `/home/feiyangdigitalbotconf/` 目录下进行以下操作： 1.停止并移除卷：

```
docker-compose down
```

2.删除数据库持久卷（❗️危险操作，你需要对比本仓库里的数据库文件是否更新过，否则不要执行，删除之前请备份各种关键词文档）：

* 首先备份数据库至`/home/`目录下

```
docker exec -it feiyangdigitalbotconf-mysql-1 mysqldump -uroot -ppassword bot  > /home/bot.sql
```

* 删除数据库持久卷

```
docker volume rm feiyangdigitalbotconf_mysql-data
```

3.拉取最新镜像：

```
docker-compose pull
```

4.使用新镜像重新启动容器：

```
docker-compose up -d
```

5.在宿主机的`/etc/sysctl.conf`文件中添加或修改以下行并重启：

```
vm.overcommit_memory = 1
```

[取消回复](https://blog.upx8.com/4730#respond-post-4730)

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