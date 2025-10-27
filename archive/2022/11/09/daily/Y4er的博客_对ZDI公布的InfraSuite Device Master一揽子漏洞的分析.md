---
title: 对ZDI公布的InfraSuite Device Master一揽子漏洞的分析
url: https://y4er.com/posts/infrasuite-device-master-cves/
source: Y4er的博客
date: 2022-11-09
fetch_date: 2025-10-03T22:01:36.635807
---

# 对ZDI公布的InfraSuite Device Master一揽子漏洞的分析

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [前言](#前言)
* [基础架构](#基础架构)
* [CVE-2022-41778](#cve-2022-41778)
* [构造payload](#构造payload)
* [CVE-2022-41657](#cve-2022-41657)
* [CVE-2022-41772](#cve-2022-41772)
* [CVE-2022-41688](#cve-2022-41688)
* [CVE-2022-40202](#cve-2022-40202)
* [总结](#总结)

## 目录

* [前言](#前言)
* [基础架构](#基础架构)
* [CVE-2022-41778](#cve-2022-41778)
* [构造payload](#构造payload)
* [CVE-2022-41657](#cve-2022-41657)
* [CVE-2022-41772](#cve-2022-41772)
* [CVE-2022-41688](#cve-2022-41688)
* [CVE-2022-40202](#cve-2022-40202)
* [总结](#总结)

# 对ZDI公布的InfraSuite Device Master一揽子漏洞的分析

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [代码审计](/categories/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)

2022-11-08  2022-11-08  约 1661 字
 预计阅读 8 分钟

目录

* [前言](#前言)
* [基础架构](#基础架构)
* [CVE-2022-41778](#cve-2022-41778)
* [构造payload](#构造payload)
* [CVE-2022-41657](#cve-2022-41657)
* [CVE-2022-41772](#cve-2022-41772)
* [CVE-2022-41688](#cve-2022-41688)
* [CVE-2022-40202](#cve-2022-40202)
* [总结](#总结)

警告

本文最后更新于 2022-11-08，文中内容可能已过时。

看到zdi发了一堆洞，有反序列化、目录穿越、权限绕过等等，还是dotnet的，于是有了此文。

# # 前言

ZDI爆的洞如图

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/7e6763e3-fce8-9410-8ba0-eba3d72579aa.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/7e6763e3-fce8-9410-8ba0-eba3d72579aa.png "image.png")

image.png

# # 基础架构

exe对应端口

text

```
C:\Program Files\InfraSuite Device Master\Device-DataCollect\Device-DataCollect.exe 3000
C:\Program Files\InfraSuite Device Master\Device-Gateway\Device-Gateway.exe  3100 3110
C:\Program Files\InfraSuite Device Master\Device-Gateway\Device-Gateway.exe 80 443
```

# # CVE-2022-41778

<https://www.zerodayinitiative.com/advisories/ZDI-22-1478/>

这个漏洞在3100和3110端口

从TCP服务器到业务处理的逻辑如下

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/7e7b643c-e258-dcb1-b0e5-66ca337612e5.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/7e7b643c-e258-dcb1-b0e5-66ca337612e5.png "image.png")

image.png

StartGatewayOperation中设置了网关服务的一些配置

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/1dbec158-8eee-e877-ef55-c0c0ab0953ff.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/1dbec158-8eee-e877-ef55-c0c0ab0953ff.png "image.png")

image.png

初始化TCP端口

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a5a305b5-cb64-9043-3c5c-f221477907a5.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a5a305b5-cb64-9043-3c5c-f221477907a5.png "image.png")

image.png

监听IPv4 v6，端口DEFAULT\_TCP\_PORT

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/f9ec626c-945e-b7e2-b5f2-6e8f0e65d179.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/f9ec626c-945e-b7e2-b5f2-6e8f0e65d179.png "image.png")

image.png

this.InitialWebEngine()中配置了web服务器

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/069ec782-d232-7a07-2401-a51fefabc1d3.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/069ec782-d232-7a07-2401-a51fefabc1d3.png "image.png")

image.png

在StartControlLayer中起worker线程跑业务逻辑

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/be097f5a-1cfd-d10e-c0b3-bce33de67bbf.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/be097f5a-1cfd-d10e-c0b3-bce33de67bbf.png "image.png")

image.png

也就是MainLoop

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/be8bc5ee-2301-63a5-c67e-d852ab097cd7.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/be8bc5ee-2301-63a5-c67e-d852ab097cd7.png "image.png")

image.png

在DoUpperLayerNWPacket中根据PacketData的sHeader字段的i32PayloadType进行switch case。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/6ae69209-d8fa-4cf3-fec6-6aa605d62cc4.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/6ae69209-d8fa-4cf3-fec6-6aa605d62cc4.png "image.png")

image.png

随便进入一个case

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/4d6bd007-1bdc-811c-93c5-77811af81616.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/4d6bd007-1bdc-811c-93c5-77811af81616.png "image.png")

image.png

看到 `Serialization.DeSerializeBinary(sPacket.payload, out obj)`

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a4ba7f22-c20c-117d-5fee-6f21e37a5d56.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a4ba7f22-c20c-117d-5fee-6f21e37a5d56.png "image.png")

image.png

直接binaryformatter，没啥好说的。关键点在于怎么构造payload。

# # 构造payload

构造需要研究其tcp的处理逻辑，在ControlLayerMngt的构造函数中

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ef5df9ee-ceaa-4559-94e2-62d42340a603.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ef5df9ee-ceaa-4559-94e2-62d42340a603.png "image.png")

image.png

初始化了一个TCPServerConnectionMngt，在ModuleInitialization中定义了TCP链接的send和receive事件。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/fa38d405-f177-0438-310a-ebf3d960ad7f.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/fa38d405-f177-0438-310a-ebf3d960ad7f.png "image.png")

image.png

我们发送给server的请求是receive事件，被ReceiveCallBack处理。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/5e323f66-c722-453a-3467-a342680c9cec.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/5e323f66-c722-453a-3467-a342680c9cec.png "image.png")

image.png

分别进行add、check操作

在add中将传入的buffer赋予自身this.\_gRxPacketBytesBuffer，变长存储字节数据。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ee22d7ae-c838-ef66-b366-aea4d083abbf.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ee22d7ae-c838-ef66-b366-aea4d083abbf.png "image.png")

image.png

check中检查数据包格式，重组PacketData对象

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8a2d186e-5178-aaa6-1b21-1ce5428b92f5.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8a2d186e-5178-aaa6-1b21-1ce5428b92f5.png "image.png")

image.png

并调用this.AddRxPacket(packetData)将重组的packet对象加入this.\_gRxPacketList

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/40c25c42-a6c7-da0e-0af4-6c9baa5a1103.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/40c25c42-a6c7-da0e-0af4-6c9baa5a1103.png "image.png")

image.png

回看MainLoop

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/3d886b3f-9993-3dca-ce6d-5c3afc151982.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/3d886b3f-9993-3dca-ce6d-5c3afc151982.png "image.png")

image.png

this.CheckUpperLayerNWPacket();
this.DoUpperLayerNWPacket();

Check调用ReceivePacket判断this.\_gRxPacketList中是否有数据包

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/58772bea-fcbf-d58d-d088-8b6f0af2f7c0.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/58772bea-fcbf-d58d-d088-8b6f0af2f7c0.png "image.png")

image.png

ReceivePacket调用GetFirstRxPacket拿到第一个数据包packet

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a5237c99-3f69-f0af-0ef3-0a3b42355544.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a5237c99-3f69-f0af-0ef3-0a3b42355544.png "image.png")

image.png

然后调用this.\_gUpperLayerNWPacketQueue.AddToSyncQueue(packetData)将数据包加入到同步队列中。

DoUpperLayerNWPacket就是拿到队列中的第一个数据包

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/dbae1a...