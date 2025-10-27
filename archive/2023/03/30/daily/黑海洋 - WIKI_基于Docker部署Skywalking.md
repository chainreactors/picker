---
title: 基于Docker部署Skywalking
url: https://blog.upx8.com/3377
source: 黑海洋 - WIKI
date: 2023-03-30
fetch_date: 2025-10-04T11:07:49.290132
---

# 基于Docker部署Skywalking

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 基于Docker部署Skywalking

发布时间:
2023-03-29

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
13453

这里用的版本是9.2.0，如果用最新版，需查看配置是否需要更改，此处使用的为默认配置，如需修改配置请自行前往官网学习

https://skywalking.apache.org/docs/main/v9.2.0/en/setup/backend/backend-docker/

### 1、启动skywalking-oap服务

bash

```
# 拉取镜像
docker pull apache/skywalking-oap-server:9.2.0
docker pull apache/skywalking-ui:9.2.0
# 运行skywalking-oap容器
docker run --name skywalking-oap -e TZ=Asia/Shanghai \
 -p 12800:12800 -p 11800:11800 \
 --restart always -d apache/skywalking-oap-server:9.2.0
```

### 2、启动skywalking-ui服务，宿主机端口根据服务器实际情况来自定义分配

bash

```
# 运行skywalking-ui容器
docker run -d --name skywalking-ui \
 --restart=always \
 -e TZ=Asia/Shanghai \
 -p 8080:8080 \
 --link skywalking-oap:oap \
 -e SW_OAP_ADDRESS=http://oap:12800 \
 apache/skywalking-ui:9.2.0
```

### 3、Java jar在容器中连接

下载skywalking-agent的jar包 [https://skywalking.apache.org/docs/](https://blog.upx8.com/go/aHR0cHM6Ly9za3l3YWxraW5nLmFwYWNoZS5vcmcvZG9jcy8)

找到Java Agent下载对应版本

启动容器时挂载这个jar

bash

```
-v /home/root/skywalking/skywalking-agent:/home/root/skywalking/skywalking-agent
```

Dockerfile配置

bash

```
# 基础镜像
FROM  openjdk:8-jre
# author
MAINTAINER test
# 指定路径
WORKDIR /
# 复制jar文件到路径
ADD test.jar test.jar
# 指定时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 指定端口
EXPOSE 8080
# 启动系统服务
ENTRYPOINT ["java","-javaagent:/home/root/skywalking/skywalking-agent/skywalking-agent.jar","-Dskywalking.agent.service_name=test","-Dskywalking.agent.instance_name=test1","-Dskywalking.collector.backend_service=192.168.1.1:11800","-Xmn512M","-Xms512M","-Xmx1024M","-Dspring.profiles.active=test","-jar","test.jar"]
```

 配置的说明

bash

```
-javaagent:Java Agent Jar包的位置
-Dskywalking.agent.service_name=服务分组的名称
-Dskywalking.agent.instance_name=注册示例的名称
-Dskywalking.collector.backend_service=skywalking-oap的连接地址
```

[取消回复](https://blog.upx8.com/3377#respond-post-3377)

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