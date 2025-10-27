---
title: repackAPK
url: https://buaq.net/go-139020.html
source: unSafe.sh - 不安全
date: 2022-12-08
fetch_date: 2025-10-04T00:52:04.408442
---

# repackAPK

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/bce2653ab8d2e02585e4c1727ccd15d8.jpg)

repackAPK

前期准备使用该项目，推荐您拥有以下的产品权限 / 策略：服务/业务函数计算硬盘挂载
*2022-12-7 22:2:13
Author: [github.com(查看原文)](/jump-139020.htm)
阅读量:37
收藏*

---

[![](https://camo.githubusercontent.com/f0bf8090df58add9b5dc76caf4476fcefc8619f8abf7b7676679f3323075e050/687474703a2f2f656469746f722e646576736170702e636e2f69636f6e3f7061636b6167653d73746172742d72657061636b2d61706b26747970653d7061636b61676554797065)](https://www.serverless-devs.com)
[![](https://camo.githubusercontent.com/e41461d5d0e00755b7d96be66dd45cf748307b4f6c6161c4c5bea2a75317897c/687474703a2f2f656469746f722e646576736170702e636e2f69636f6e3f7061636b6167653d73746172742d72657061636b2d61706b26747970653d7061636b61676556657273696f6e)](http://www.devsapp.cn/details.html?name=start-repack-apk)
[![](https://camo.githubusercontent.com/1683b2bd5fd149739276cd5be17bc0792bd2ed720266849420c6140170c07f1a/687474703a2f2f656469746f722e646576736170702e636e2f69636f6e3f7061636b6167653d73746172742d72657061636b2d61706b26747970653d7061636b616765446f776e6c6f6164)](http://www.devsapp.cn/details.html?name=start-repack-apk)

## 前期准备

使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 | 硬盘挂载 | VPC | 其它(安全组) |
| --- | --- | --- | --- | --- |
| 权限/策略 | AliyunFCFullAccess | AliyunNASFullAccess | AliyunVPCFullAccess | AliyunECSFullAccess |

* [😺 源代码](https://github.com/devsapp/repackAPK/tree/main/src)

## 部署 & 体验

* 🔥 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-repack-apk) ，
  [![Deploy with Severless Devs](https://camo.githubusercontent.com/e713090d81c7de322c7f7e0f5f6b7080b26bb6b6a01a4b90bed62c6e89f205b8/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69312f4f31434e3031773552466258317634357338544958507a5f2121363030303030303030363131382d35352d7470732d39352d32382e737667)](https://fcnext.console.aliyun.com/applications/create?template=start-repack-apk) 该应用。

* 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  + [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
  + 初始化项目：`s init start-repack-apk -d start-repack-apk`
  + 进入项目，并进行项目部署：`cd start-repack-apk && s deploy -y`

**Serverless 实现实时 apk 渠道分包**

游戏分发平台的游戏 APK 包需要根据实时请求中的的参数获取指定的渠道号，并将渠道号写入 APK 文件固定位置， 如果每天有大量且不同渠道的下载请求， 能**实时**让用户**断点下载**指定渠道的 apk 游戏包

应用原理图如下：

[![](https://camo.githubusercontent.com/386790c6bb156466cd02030f25c15037c725e78a3904cb37b01deaecd8248676/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69322f4f31434e303139736550393031557857427439443868375f2121363030303030303030323538342d322d7470732d323132302d3636382e706e67)](https://camo.githubusercontent.com/386790c6bb156466cd02030f25c15037c725e78a3904cb37b01deaecd8248676/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69322f4f31434e303139736550393031557857427439443868375f2121363030303030303030323538342d322d7470732d323132302d3636382e706e67)

## CDN 配置

本应用部署后端函数，部署成功后， 您会获取一个 访问域名的 url， 比如为 `https://get-apk-apk-repack-evbilghzjb.cn-hangzhou.fcapp.run`

之后登录 [CDN 控制台](https://cdn.console.aliyun.com/) 完成配置：

### 添加域名

比如您有一个名为 `functioncompute.com` 的域名, 如下图所示， 我添加了 `apk-cdn.functioncompute.com`, 源站的域名为前面应用部署的访问域名 url(*注意是 host，不用填写前面的 https://*), 比如本示例为 `get-apk-apk-repack-evbilghzjb.cn-hangzhou.fcapp.run`

> 其中前缀 apk-cdn 可以随便， 由您这边自己想最后暴露出去的 url 决定

[![](https://camo.githubusercontent.com/587bc673b96db10bb317d98a868671fc17d184d9be0fb283bec0bab4764604e9/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69322f4f31434e30314b583646684c31736a703949315553384d5f2121363030303030303030353830332d322d7470732d313337322d3834302e706e67)](https://camo.githubusercontent.com/587bc673b96db10bb317d98a868671fc17d184d9be0fb283bec0bab4764604e9/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69322f4f31434e30314b583646684c31736a703949315553384d5f2121363030303030303030353830332d322d7470732d313337322d3834302e706e67)

### 域名管理

#### 1. 根据控制台引导， 完成域名的 CNAME 解析

[![](https://camo.githubusercontent.com/2ed079f619537f6c68d9d93afe97e55a514c4ce884b05083aeb365906e7c8e4a/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69342f4f31434e3031746d6c79433232326c6e305454724674315f2121363030303030303030373136312d322d7470732d3935362d313337322e706e67)](https://camo.githubusercontent.com/2ed079f619537f6c68d9d93afe97e55a514c4ce884b05083aeb365906e7c8e4a/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69342f4f31434e3031746d6c79433232326c6e305454724674315f2121363030303030303030373136312d322d7470732d3935362d313337322e706e67)

[![](https://camo.githubusercontent.com/edd66dcecddfd54f5ee7572c76e80c47d12ef6140589ea67e416db6553fd84a2/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69312f4f31434e3031687462694f6331445a4e734471444339435f2121363030303030303030303233302d322d7470732d323334382d3637302e706e67)](https://camo.githubusercontent.com/edd66dcecddfd54f5ee7572c76e80c47d12ef6140589ea67e416db6553fd84a2/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69312f4f31434e3031687462694f6331445a4e734471444339435f2121363030303030303030303233302d322d7470732d323334382d3637302e706e67)

[![](https://camo.githubusercontent.com/e1726162c2b0259223fc58b0c0acf4413df8f8f7059ddb680eebaeea8d1447e9/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69342f4f31434e3031764b5563473231524757424564386542545f2121363030303030303030323038342d322d7470732d323538362d3234342e706e67)](https://camo.githubusercontent.com/e1726162c2b0259223fc58b0c0acf4413df8f8f7059ddb680eebaeea8d1447e9/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69342f4f31434e3031764b5563473231524757424564386542545f2121363030303030303030323038342d322d7470732d323538362d3234342e706e67)

#### 2. 完成管理配置, 主要完成回源配置的域名和开启 Range 回源强制

[![](https://camo.githubusercontent.com/a5bb98b6b30a5d1d6552b3a1eb6997d1c1c258555f4b0fe3c2948d5bff2636c8/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69342f4f31434e30316439635273783233725a636b7759716d465f2121363030303030303030373330392d322d7470732d323634362d3731362e706e67)](https://camo.githubusercontent.com/a5bb98b6b30a5d1d6552b3a1eb6997d1c1c258555f4b0fe3c2948d5bff2636c8/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69342f4f31434e30316439635273783233725a636b7759716d465f2121363030303030303030373330392d322d7470732d323634362d3731362e706e67)

> 域名应用部署成功后返回的访问域名 url 的 host, 比如本示例为 `get-apk-apk-repack-evbilghzjb.cn-hangzhou.fcapp.run`

[![](https://camo.githubusercontent.com/93a4a4aa3b8c01dbd277964ae2fcfe0757bf793f66123451704f023e5c8b5e71/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69332f4f31434e3031573872506e47315231725644634b37544e5f2121363030303030303030323035322d322d7470732d323631322d3835342e706e67)](https://camo.githubusercontent.com/93a4a4aa3b8c01dbd277964ae2fcfe0757bf793f66123451704f023e5c8b5e71/68747470733a2f2f696d672e616c6963646e2e636f6d2f696d6765787472612f69332f4f31434e3031573872506e47315231725644634b37544e5f2121363030303030303030323035322d322d7470732d323631322d3835342e706e67)

#### 使用浏览器断点下载指定渠道 apk 包

比如:

`http://apk-cdn.functioncompute.com/foo?src=fc-imm-demo/test-apk/qq.apk&cid=uc`

`http://apk-cdn.functioncompute.com/foo?src=fc-imm-demo/test-apk/qq.apk&cid=xiaomi`

其中

* `apk-cdn.functioncompute.com` 表示 cdn 对外的域名
* `src=fc-imm-demo/test-apk/qq.apk` 表示处理的母包， 其中 fc-imm-demo 为 bucket(和函数在同一个region), test-apk/qq.apk 为 object
* `cid=xiaomi` 表示渠道为 xiaomi, 这个可以自定义

**Tips**

* 用户在自己程序中获取渠道信息， 只需要读取 apk 包中 `assets/dap.properties` 文件中的内容即可
* 换用自己的证书， 只需要换掉 target/cert 下面的文件即可：

  > jarsigner 将 .keystore 文件作为 RSA 密钥的来源，要将其转换为 gola...