---
title: 宝塔面板搭建PeerTuBe
url: https://blog.upx8.com/3149
source: 黑海洋 - WIKI
date: 2022-12-14
fetch_date: 2025-10-04T01:24:28.564559
---

# 宝塔面板搭建PeerTuBe

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 宝塔面板搭建 PeerTube 详细步骤指南

发布时间:
2022-12-13

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
31895

此方案于 WebP2P 领域颇具潜力，然其官网文档状况堪忧，系基于旧版编制且久未更新，致使诸多信息陈旧滞后。常用管理功能亦存在缺漏，若欲实际运用，使用者非得具备深厚相关知识底蕴以自行调适配置不可。就当下情形而言，或仅适宜自行搭建以供赏玩，权作收藏心仪之彩色视频之途。吾每日潜心钻研十分钟有余，耗时数日仍未攻克 AWS S3 与 MinIO 对接之难题。再者，直播端口之设置，非仅开放 1935 即可，尚需开启 1936 端口方能周全。

# 基于Docker安装

创建目录

```
mkdir /你的目录/peertube/
cd /你的目录/peertube/
```

拉取最新的Docker配置文件

```
curl https://raw.githubusercontent.com/chocobozzz/PeerTube/master/support/docker/production/docker-compose.yml > docker-compose.yml
```

这里我给出一下我的`docker-compose.yml`的配置,因为我本地有安装nginx,为了避免冲突,我去掉了peertube自带的

```
services:

  peertube:
    # If you don't want to use the official image and build one from sources:
    # build:
    #   context: .
    #   dockerfile: ./support/docker/production/Dockerfile.bullseye
    image: chocobozzz/peertube:production-bullseye
    # Use a static IP for this container because nginx does not handle proxy host change without reload
    # This container could be restarted on crash or until the postgresql database is ready for connection
    networks:
      default:
        ipv4_address: 172.18.0.42
    env_file:
      - .env

    ports:
     - "1935:1935" # Comment if you don't want to use the live feature
     - "9000:9000" # Uncomment if you use another webserver/proxy or test PeerTube in local, otherwise not suitable for production
    volumes:
      - assets:/app/client/dist
      - ./docker-volume/data:/data
      - ./docker-volume/config:/config
    depends_on:
      - postgres
      - redis
    restart: "always"

  postgres:
    image: postgres:13-alpine
    env_file:
      - .env
    volumes:
      - ./docker-volume/db:/var/lib/postgresql/data
    restart: "always"

  redis:
    image: redis:6-alpine
    volumes:
      - ./docker-volume/redis:/data
    restart: "always"

networks:
  default:
    ipam:
      driver: default
      config:
      - subnet: 172.18.0.0/16

volumes:
  assets:
```

拉取环境变量env文件`

```
curl https://raw.githubusercontent.com/Chocobozzz/PeerTube/master/support/docker/production/.env > .env
```

然后编辑你的`docker-compose.yml`

根据你自己的情况选择要或者不要的服务

* `webserver`:web 服务,供浏览器访问.(如果你已经安装其他web服务,可以不选.另外我不建议你用nginx来反向代理,因为nginx反向代理之后流媒体需要缓存完毕以后才会发送到客户端,所以基本是播放不了的状态.)
* `peertube`:核心,你能不选吗?
* `redis`:缓存服务,必选.
* `postgres`:数据库,必选.
* `postfix`:如果你要提供开放式的服务,就选上,如果是自己搭建的好玩,不选.
* `certbot`:自动申请证书,没卵用,没有可以选.

然后编辑`.env`来修改你的数据库信息和域名.

* `<MY POSTGRES USERNAME>`
* `<MY POSTGRES PASSWORD>`
* `<MY DOMAIN>` 不带 `https://`
* `<MY EMAIL ADDRESS>`
* `<MY PEERTUBE SECRET>`

这一切都准备好以后,就直接开始跑起来吧:

```
cd /你的目录/peertube
docker-compose up -d
```

完成以后可以通过你填写的域名加9000端口来访问了

# 管理员密码获取

Peertub安装完是不显示什么管理员密码的,搞不太懂.可以通过一下命令在安装目录执行获取到root账号密码

```
docker-compose logs peertube | grep -A1 root
```

或者你直接查看Log文件,找到下面的信息也一样.

```
#查看日志
cat /你的目录/docker-volume/data/logs/peertube.log
#会输出一些信息，找到如下信息，密码就是xxxxxx
{"message":"Username: root","level":"info","timestamp":"}
{"message":"User password: xxxxxxxxxx","level":"info","timestamp":"}
```

你也可以选择不用Docker,但是我嫌麻烦,参考这里:[https://docs.joinpeertube.org/install-any-os](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLmpvaW5wZWVydHViZS5vcmcvaW5zdGFsbC1hbnktb3M)

# 升级Peertube

拉取最新的镜像

```
#进入你的目录
cd /你的目录/peertube
#然后拉取最新的包
docker-compose pull
```

停止删除容器和卷

```
docker-compose down -v
```

然后再跑起来

```
docker-compose up -d
```

# 项目地址

官网:[https://joinpeertube.org/](https://blog.upx8.com/go/aHR0cHM6Ly9qb2lucGVlcnR1YmUub3JnLw) (可能要借助魔法才能访问)

Gayhub:[https://github.com/Chocobozzz/PeerTube](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0Nob2NvYm96enovUGVlclR1YmU)

最后需留意，我尚未尝试过此方案的升级操作，因我对 Docker 的使用较为有限。此外，Peertube 的 docker 版本其配置文件与常规版本存在差异。诸位若有相关操作打算，建议先行随意搭建一个进行尝试，待确认无误后再行升级，抑或提前做好完备的备份工作，以防不测。

出处：[https://mrx.la/724](https://blog.upx8.com/go/aHR0cHM6Ly9tcngubGEvNzI0)

1. ![Mrx](//q2.qlogo.cn/headimg_dl?dst_uin=5086153&spec=100)

   **Mrx**

   2024-01-14 18:04:53

   [回复](https://blog.upx8.com/3149/comment-page-1?replyTo=28432#respond-post-3149)

   好的老板

[取消回复](https://blog.upx8.com/3149#respond-post-3149)

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