---
title: timwhitez starred go_proxy_pool
url: https://buaq.net/go-136270.html
source: unSafe.sh - 不安全
date: 2022-11-19
fetch_date: 2025-10-03T23:11:32.229141
---

# timwhitez starred go_proxy_pool

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

![](https://8aqnet.cdn.bcebos.com/4119a58ad5a5529748a0be640c783776.jpg)

timwhitez starred go\_proxy\_pool

一款无环境依赖开箱即用的免费代理IP池内置12个免费代理源，均使用内置的简单正则获取支持调用插件扩展代理源，返回的数据符合格式即可，无开发语言限制支持webApi获取
*2022-11-18 18:36:20
Author: [github.com(查看原文)](/jump-136270.htm)
阅读量:28
收藏*

---

一款无环境依赖开箱即用的免费代理IP池

内置12个免费代理源，均使用内置的简单正则获取

支持调用插件扩展代理源，返回的数据符合格式即可，无开发语言限制

支持webApi获取、删除、更新等代理池内的IP

支持隧道代理模式，无需手动更换IP

遇到bug或有好的建议，欢迎提issue

## 隧道代理

隧道代理是代理IP存在的一种方式。

[![zVIfSA.png](https://camo.githubusercontent.com/f86f1e52672d76bc2cf487625e7220031835f9dae19b004a21bd62d90c8fa039/68747470733a2f2f73312e617831782e636f6d2f323032322f31312f31362f7a56496653412e706e67)](https://imgse.com/i/zVIfSA)

下载

```
git clone [email protected]:pingc0y/goProxyPool.git
```

编译（直接使用成品，就无需编译）
以下是在windows环境下，编译出各平台可执行文件的命令

```
SET CGO_ENABLED=0
SET GOOS=windows
SET GOARCH=amd64
go build -ldflags "-s -w" -o ../goProxyPool-windows-amd64.exe

SET CGO_ENABLED=0
SET GOOS=windows
SET GOARCH=386
go build -ldflags "-s -w"  -o ../goProxyPool-windows-386.exe

SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=amd64
go build -ldflags "-s -w" -o ../goProxyPool-linux-amd64

SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=arm64
go build -ldflags "-s -w" -o ../goProxyPool-linux-arm64

SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=386
go build -ldflags "-s -w" -o ../goProxyPool-linux-386

SET CGO_ENABLED=0
SET GOOS=darwin
SET GOARCH=amd64
go build -ldflags "-s -w" -o ../goProxyPool-macos-amd64

SET CGO_ENABLED=0
SET GOOS=darwin
SET GOARCH=arm64
go build -ldflags "-s -w" -o ../goProxyPool-macos-arm64
```

运行
需要与config.yml在同一目录
第一次运行会去抓取代理，大概需要3分钟

代理源中有部分需要翻墙才能访问，有条件就设置下config.yml的代理配置

```
proxy:
  host: 127.0.0.1
  port: 10809
```

## webAPi说明

查看代理池情况

获取代理

```
http://127.0.0.1:8080/get?type=HTTP&count=10&anonymity=all
可选参数：
type        代理类型
anonymity   匿名度
region      地区
source      代理源
count       代理数量
获取所有：all
```

删除代理

```
http://127.0.0.1:8080/del?ip=127.0.0.1&port=8888
必须传参：
ip      代理ip
port    代理端口
```

删除代理

```
http://127.0.0.1:8080/del?ip=127.0.0.1&port=8888
必须传参：
ip      代理ip
port    代理端口
```

更换隧道代理IP

```
http://127.0.0.1:8080/tunnelUpdate
```

开始抓取代理

```
http://127.0.0.1:8080/upload
```

## 配置文件

```
#使用代理去获取代理IP
proxy:
  host: 127.0.0.1
  port: 10809

# 配置信息
config:
  #web监听的IP
  ip: 0.0.0.0
  #web监听端口
  port: 8080
  #隧道代理端口
  tunnelPort: 8111
  #隧道代理更换时间秒
  tunnelTime: 60
  #可用IP数量小于‘proxyNum’时就去抓取
  proxyNum: 10
  #代理IP验证间隔秒
  verifyTime: 1800
  #抓取/检测状态线程数
  threadNum: 50

#ip源
spider:
    #代理获取源1
  - name: '齐云代理'
    method: 'GET'
    #使用的请求头
    Headers:
      User-Agent: 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    #获取的地址
    urls: 'https://proxy.ip3366.net/free/?action=china&page=1,https://proxy.ip3366.net/free/?action=china&page=2,https://proxy.ip3366.net/free/?action=china&page=3'
    #获取IP的正则表达式，
    ip: '\"IP\">(\d+?\.\d+?.\d+?\.\d+?)</td>'
    #获取端口的正则表达式
    port: '\"PORT\">(\d+?)</td>'
    #获取代理模式（匿名，透明）的正则表达式
    anonymity: "\"匿名度\">(.+?)</td>"
    #是否使用代理去请求
    proxy: false
    #代理模式文本替换，用于统一格式
    replace:
      匿名: '普匿'

#通过插件，扩展ip源
spiderPlugin:
  #插件名
  - name: test1
    #运行命令，返回的结果要符合格式,是json格式
    run: './test1.exe'
```

### 扩展返回格式

```
[
{
"Ip": "58.246.58.150",
"Port": "9002",
"Info1": "",
"Info2": "",
"Info3": "",
"Isp": "",
"Type": "",
"Anonymity": "透明",
"Time": 0,
"Speed": 0,
"SuccessNum": 0,
"RequestNum": 0,
"Source": "xx代理"
},
{
"Ip": "223.84.240.36",
"Port": "9091",
"Info1": "",
"Info2": "",
"Info3": "",
"Isp": "",
"Type": "",
"Anonymity": "匿名",
"Time": 0,
"Speed": 0,
"SuccessNum": 0,
"RequestNum": 0,
"Source": "xx代理"
}
]
```

文章来源: https://github.com/pingc0y/go\_proxy\_pool
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)