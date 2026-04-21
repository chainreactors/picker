---
title: Dockerfile语法全解析：从构建原理到分层构建的实战指南
url: https://mp.weixin.qq.com/s/PVvVzbU-oQ9rOQu6kESIhw
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:48:54.679284
---

# Dockerfile语法全解析：从构建原理到分层构建的实战指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RJrNBTwulvc36ORqs6Wq9jQAkIuic6baZKtOCP6tKpDox3Rtz4zrNxEBdkahibTaVke4GBsQvQCpOcltxQLic0ujmvxia16FYR2vBAVibxDzznaU/0?wx_fmt=jpeg)

# Dockerfile语法全解析：从构建原理到分层构建的实战指南

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Dockerfile语法全解析：从构建原理到分层构建的实战指南

## 缘起

终于写到Dockerfile，构建应用docker镜像是使用docker打包应用的基础，而dockerfile，就是构建docker镜像的灵魂。

## 什么是Dockerfile

Dockerfile就是一个纯文本文件，里面包含了一条条的指令，用来描述如何自动构建一个Docker镜像。

可以理解为这是一个详细的操作说明书，按照步骤一步一步的定制一个docker镜像。dockerfile的存在，让docker镜像有了：

1. 标准化了构建过程，确保开发、测试和生产环境的高度一致性
2. 版本控制与可追溯性：作为纯文本文件，Dockerfile可以像代码一样被Git管理，任何环境变更都有迹可循
3. 自动化CI/CD的基石：结合Jenkins、GitHub Actions等工具，实现一键自动构建和部署

## Dockerfile的基本结构

一个典型的Dockerfile通常分为四个部分：基础镜像信息、维护者信息、镜像操作指令、容器启动时执行指令，先看个例子：

```
# 1. 基础镜像信息：这是构建的起点FROM ubuntu:20.04
# 2. 维护者信息：告诉别人谁负责这个镜像LABEL maintainer="hello@world.com"
# 3. 镜像操作指令：安装软件、配置环境等RUN apt-get update && apt-get install -y nginxCOPY index.html /var/www/html/
# 4. 容器启动时执行指令：启动容器时默认运行的命令CMD ["nginx", "-g", "daemon off;"]
```

## 核心语法指令

### FROM 万丈高楼平地起

每个Dockerfile的第一条非注释指令必须是FROM，它指定了你的基础镜像

```
FROM ubuntu:20.04
```

Dockerfile每一条指令都会在镜像上创建一个新的层:，这也是镜像体积优化的关键：

***当有多个镜像公用一个基础镜像（FROM 同一个基础镜像）的时候，系统只存储一份，然后使用类似于超链接的方式，来节省存储空间。***

\*\*最佳实践：\*\*尽量选择官方镜像，明确指定标签（tag，如20.04），避免使用latest：这是个游标tag，永远指向最新版本，以防止底层不可控的更新导致程序奔溃。

### LABEL：镜像的身份证

用于添加元数据，如作者、版本、描述，例子：

```
LABEL maintainer="hello@world.com" version="1.0" description="Hello World App"
```

### WORKDIR：设置工作目录

```
WORKDIR /app
```

简单理解就是cd到当前目录，后续的相对目录就是以此目录为基础路径。

### COPY 与 ADD：把文件搬进容器

1. COPY：纯粹的复制文件
2. ADD：除了复制，还支持自动解压本地tar包和从URL下载文件

```
COPY package.json /app/# ADD package.tar.gz /app/  # 会自动解压
```

***最佳实践：*** 推荐使用简单的命令：意思是如果只是复制文件，就用COPY，不要用ADD

### RUN：在构建阶段执行命令

```
# Shell格式RUN apt-get update && apt-get install -y curl
```

run用于执行命令，这里有点讲究：每条命令会产生一个层，所有合理的合并、分拆命令组合，能够做到减少存储和镜像大小：

***最佳实践***

1. 合理分拆： 举例你有2个镜像需要构建构建，他们都是基于debian:12,然后a镜像需要安装软件a、b、c，b镜像需要安装如那件a、b、d，那么你可以把安装a、b的命令放在一个RUN指令里，安装c和d的命令放在另一个RUN指令里，这样就能让a和b镜像共享安装a、b的层，节省存储空间。
2. 合理合并： 当你有2条命令，分别安装2个软件，但是这俩个软件只有这个镜像使用，就可以合并到一条指令里面安装

```
# 👎 产生3个层RUN apt-get updateRUN apt-get install -y curlRUN rm -rf /var/lib/apt/lists/*
# 👍 仅产生1个层，镜像更小RUN apt-get update && apt-get install -y --no-install-recommends curl \    && rm -rf /var/lib/apt/lists/*
```

注意： 这里只是以安装软件为例，所有的命令都适用分拆合并规则。

### CMD 与 ENTRYPOINT：容器的启动命令

1. CMD：提供容器启动的默认命令。一个Dockerfile只有最后一个CMD生效（就是顺序排，后面的替代前面的），且可以被docker run命令行参数直接覆盖。
2. ENTRYPOINT：定义容器的主命令，不会被docker run的参数覆盖，而是将docker run后的参数作为附加参数传给ENTRYPOINT： 可理解这个是指明运行环境：python表示使用python运行cmd的命令，bash就是用bash运行cmd命令……

```
# 示例：组合使用，实现灵活启动ENTRYPOINT ["python"]CMD ["app.py"]  # 默认执行 python app.py# 如果 docker run myimage server.py，则执行 python server.py
```

### EXPOSE  声明端口

```
EXPOSE 8080
```

仅作为文档说明，告知使用者容器监听的端口。

### ENV 设置环境变量

```
ENV NODE_ENV=productionENV PATH="/app/bin:${PATH}"
```

设置构建和运行时的环境变量

### VOLUME 声明数据卷

```
VOLUME ["/data"]
```

声明容器中需要持久化存储的目录：数据库、日志文件、上传目录等。

### ARG：构建时参数化

这是一个非常实用的命令，将多次用到的数据、字符、版本等等变量化，这样当需要修改的适合，只需要修改一次了：

```
# 在Dockerfile中定义默认值ARG APP_VERSION=1.0# 在构建指令中使用#第一次用RUN echo "Building version $APP_VERSION"#第二次用RUN echo "Building version $APP_VERSION"# 第三次用...RUN echo "Building version $APP_VERSION"
```

### HEALTHCHECK 容器健康检查

你可能在运行容器的适合，看过一些容器是这样的：caddy(healthy),能实现这个的就是这个命令了：

定期检查容器的健康状态，确保服务可用:

```
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \  CMD curl -f http://localhost:8080/health || exit 1
```

## 多阶段构建：分层构建的实战指南

理解多阶段构建的需求，得先明白一个知识：

构建环境与运行环境

java程序员肯定都知道jdk和jre的区别，这就是开发环境和运行环境，其大小有很大的区别，其他语言也一样。

这就产生了多阶段构建的需求：编译程序的时候，使用开发环境，最后运行，使用运行环境，可以大大减少镜像的体积：

```
# ================= 第一阶段：构建阶段 (Builder Stage) =================# 使用包含Maven的官方镜像进行编译打包FROM maven:3.8.6-openjdk-17 AS builder
# 设置工作目录WORKDIR /app
# 1. 先只拷贝pom.xml文件，利用缓存预下载依赖# 这一步是关键优化：如果pom.xml未变更，Docker会复用缓存层，跳过依赖下载COPY pom.xml .RUN mvn dependency:go-offline -B
# 2. 拷贝源代码并进行打包COPY src ./srcRUN mvn clean package -DskipTests
# ================= 第二阶段：运行阶段 (Runtime Stage) =================# 使用轻量级的OpenJDK运行时镜像FROM openjdk:17-jdk-slim
# 设置工作目录WORKDIR /app
# 3. 从构建阶段仅复制生成的JAR包到最终镜像# 这是多阶段构建的核心：只保留运行所需的最小文件集COPY --from=builder /app/target/*.jar app.jar
# 暴露应用端口（Spring Boot默认8080）EXPOSE 8080
# 添加健康检查指令HEALTHCHECK --interval=30s --timeout=3s --retries=3 \  CMD curl --fail http://localhost:8080/actuator/health || exit 1
# 设置容器启动命令ENTRYPOINT ["java", "-jar", "app.jar"]
```

对springboot镜像构建，推荐：

[探索springboot程序打包docker的最佳方式](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651111&idx=1&sn=efd1e7bab6a8d95247470fb876f39915&scene=21#wechat_redirect)

## 小结

凭借记忆，写了一些常用的命令，肯定给还有遗漏的

本系列其他文章：

1. [Docker 入门之基本概念](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651207&idx=1&sn=a2f78e7c80d0a950cd43df8efb4b2d0a&scene=21#wechat_redirect)
2. [Docker 入门之网络基础](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651229&idx=1&sn=5a2f71c14af29d9f4b426045fdb3274b&scene=21#wechat_redirect)
3. [Docker 入门之overlay网络](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651251&idx=1&sn=13ac3a92e3b07dcd3ff81a77307e0903&scene=21#wechat_redirect)
4. [Docker 入门之单机常用命令总结](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651283&idx=1&sn=f2da6548f93cf6aec0588428b31e6437&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

一只岸上的鱼

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过