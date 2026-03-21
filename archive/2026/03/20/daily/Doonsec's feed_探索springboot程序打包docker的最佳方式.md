---
title: 探索springboot程序打包docker的最佳方式
url: https://mp.weixin.qq.com/s/ajICjNsvdKupiHIhDN1f4w
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:06:03.185874
---

# 探索springboot程序打包docker的最佳方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RJrNBTwulvfEzpFCbDLEVfiadAPknpkojtYRSI9qsAyeamXyyTlnBBE9tmj1emyict7vx2pwNJ8QKEYKs58gjkrlHThoJN0J0E26ZpicIY9sJk/0?wx_fmt=jpeg)

# 探索springboot程序打包docker的最佳方式

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器中沉浸阅读

# 缘起

云计算时代的来临，有一门被誉为云计算伴生编程语言：golang

其与docker的天生的搭配，开启了云计算的黄金时代。

然而java确实一门不服老的语言，不断的进化着，springboot 4 和spring 7的发布，尤其是springboot4 ，GraalVM 25 直接从实验特性转向了生产。虚拟线程常态化也是值得学习的特性。

加上还有很多的老的项目还在用springboot技术，所以想把java的整个技术栈再捡起来学习一遍：后续会陆续写一些关于springboot4 、jkd 25 lts的一些文。

学到哪儿就写到哪儿：今天想试试springboot程序打包docker的几种方式的大小区别，探索一下最佳的方式！

## 开始

准备一个最简单的restful的程序，使用spring initializr 生成项目，基础配置如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvcrd2GqGREYv4ZavXBYibYhQGCcicibDUSUDx7Muia9MsKsjF06tvdvnTymWu5xwpeNXZU7hVsr6OQ3Z5JdCib79aYmOcv3judfNhaI/640?wx_fmt=png&from=appmsg)

注意2点：1、java 25  2、加入graalvm

一个hello world

```
package com.example.demo.controller;
import org.springframework.web.bind.annotation.GetMapping;import org.springframework.web.bind.annotation.RestController;
@RestControllerclass HelloController {    @GetMapping("/hello")    String sayHello(){        return "hello world!";    }}
```

显示编译一下代码，看看原始jar包有多大：

```
./gradlew build
```

一个包含mvc基本程序的一个hello world，大小79M

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvemnCP0y24O4bGiabrYF6HdBia4tib3THqv7ibW6ibvFbcqHh5Mp3o2wxOqcAdBCR2ic9ukjuwuIF1TrX9ibLQBAn4G32xZbQn2xUOoxE/640?wx_fmt=png&from=appmsg)

## 方式一：全默认方式的打包镜像

不做任何更多的配置，只使用springboot 4 和gradle的默认配置：

根据资料，springboot的默认使用paketobuildpacks/builder-jammy-tiny 镜像，这是一个以ubuntu 22为基础的镜像，大小50-70M：

注意：犹豫我们生成项目配置的时候加入了graalm支持，必须先注释调，否则默认会使用graal技术：

build.gradle 文件部分：

```
plugins {id 'java'id 'org.springframework.boot' version '4.0.3'id 'io.spring.dependency-management' version '1.1.7'	//id 'org.graalvm.buildtools.native' version '0.11.4'}
```

使用命令打包：

```
./gradlew bootBuildImage --imageName=hello:normal
```

大小337M，同时也可以看到打包下载的基础镜像：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdD6srQOJmcq73UD6VKazjDESwdUh2faTET4yvaKJShp8ic6A5taIefpRDwbrhzV3iaaNLHr6HIKgjkhjWBAvPqdPWqCMPN2tf98/640?wx_fmt=png&from=appmsg)

## 方式二： 默认配置graalvm打包

加入graalvm的配置（方式一注释调的部分），打包：

```
./gradlew bootBuildImage --imageName=hello:gralvm
```

大小123M:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulveDVsZw6uhg5dRP6yiayA6yFYiaB5KadQmobFO9icL8ThUULGyUnQicNZflDSoH2FJPia9Hbia9tT7wyNWLgka3wJ4Viagk7H1YiaiaCicTY/640?wx_fmt=png&from=appmsg)

## 方式三： 手工打包，使用标准openjdk镜像为基础

所谓手工打包，就是自己写dockerfile，自己设置基础镜像，先试试默认情况下常用的openjdk镜像

```
FROM openjdk:25-jdk-slim
WORKDIR /appRUN useradd -U springUSER spring:springCOPY build/libs/*.jar app.jar
EXPOSE 8080CMD ["java", "-jar", "app.jar"]
```

打包命令：

```
docker build -t hello:openjdk -f deploy/openjdk.Dockerfile .
```

大小：505M

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdMlhjfEpW3ibLjGhPxHeX91xas4j32TNUnOeRbe9vlclQhhTMRd02nfh9HWuLx6XQXcntthmjp2nTIJuop1JzCzqiaaNiaVXzRias/640?wx_fmt=png&from=appmsg)

## 方式四： 手工打包，使用jlink构建一个最小的运行jre环境，以alpine为基础

虽然现在的java不再单独提供jre环境了，但是可以通过jlink构建一个程序所需的最小运行环境，然后部署到alpine linux上

```
FROM eclipse-temurin:25-jdk-alpine AS jre-builder
RUN apk update && apk add binutils
RUN $JAVA_HOME/bin/jlink \         --verbose \         --add-modules java.base \         --strip-debug \         --no-man-pages \         --no-header-files \         --compress=2 \         --output /optimized-jdk-25
FROM alpine:latestENV JAVA_HOME=/opt/jdk/jdk-25ENV PATH="${JAVA_HOME}/bin:${PATH}"
COPY --from=jre-builder /optimized-jdk-25 $JAVA_HOME
RUN addgroup --system spring && adduser --system spring --ingroup spring
RUN mkdir /app && chown -R $APPLICATION_USER /appCOPY --chown=spring:spring build/libs/*.jar /app/app.jarWORKDIR /appUSER springEXPOSE 8080ENTRYPOINT [ "java", "-jar", "/app/app.jar" ]
```

构建命令：

```
docker build -t hello:alpine -f deploy/jlink.Dockerfile .
```

大小： 93M

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulve6gibKibF7S0ZKoMwoF98iaQNletJx4icicibnXCfPsjSXicBmfywnLviaia5LQibdtbBSeXnkib0KzCJ2icZQrmNzS1iaKkmibPIZ2kbQdJOSE/640?wx_fmt=png&from=appmsg)

有点不放心，跑一下试试：

```
docker run -it -p 8080:8080 hello:alpine
```

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvfzpsuI8nO3ibFe1wUNHT8Y7bVcgnL6WmhOft21W2FRZ8WIAnLOy2cknpJywfMCCN1TyWHcFdGcAQv6J2TU0aNLwm5wybXichlL8/640?wx_fmt=png&from=appmsg)

访问一下：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvdx4icgWia9vE2N4k4c8nwZmao2pP9tEsEgw9zN14emmBNbPDhJqPJ0fzmoImjDpTlLAS7xxic4LvLxXytcpaM29I11KGOswpodh0/640?wx_fmt=png&from=appmsg)

一切正常！

## 小结

以上只是比较了打包大小的不同，这对graalvm是不公平的，毕竟他的特点是增强 AOT（Ahead-of-Time）编译，降低内存占用，提高启动时间，还是得测试一下：

```
docker run -it -p 8080:8080 --name alpine hello:alpinedocker run -it -p 9090:8080 --name graalvm hello:graalvmdocker stats
```

看到资源占用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdCzohoE0jbKBGCibRQTT8ureGxKW7y9mJys073taFDGmf7klr4PK8lymzpPJgCbRek3V28RibMt0Y3G3UDr4qVmqqyia0PxjcePk/640?wx_fmt=png&from=appmsg)

graalvm的内存占用不到原始java代码的1/4！

所以：

1、对应新的项目，高版本jdk项目，尤其是最新的25版本，完全可以考虑以graalvm来编译打包

2、对应旧的项目，或者低版本jdk的项目，生产环境使用alpine定制jre的方式，就是方式4，测试环境就使用默认openjdk：毕竟包含了大量的工具，方便调测。

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