---
title: 如何使用jscythe并通过Node.js的Inspector机制执行任意JS代码
url: https://www.freebuf.com/articles/system/349825.html
source: FreeBuf网络安全行业门户
date: 2022-11-16
fetch_date: 2025-10-03T22:53:15.632340
---

# 如何使用jscythe并通过Node.js的Inspector机制执行任意JS代码

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

如何使用jscythe并通过Node.js的Inspector机制执行任意JS代码

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

如何使用jscythe并通过Node.js的Inspector机制执行任意JS代码

2022-11-15 10:43:07

所属地 广西

![](https://image.3001.net/images/20221115/1668480025_6372fc1964099698c5350.jpg!small)

## 关于jscythe

jscythe是一款功能强大的Node.js环境安全测试工具，在该工具的帮助下，广大研究人员可以利用Node.js所提供的[Inspector机制](https://nodejs.org/en/docs/guides/debugging-getting-started/)来强制性让基于Node.js/Electron/v8实现的进程去执行任意JavaScript代码。值得一提的是，即使是在目标进程的调试功能被禁用的情况下，jscythe也能做到这一点。

当前版本的jscythe1⃣️在Visual Studio Code、Discord和任意Node.js应用程序上进行过完整测试，请广大研究人员放心使用。

## Node.js的Inspector机制是什么？

Node.js 提供的 Inspector 非常强大，不仅可以用来调试 Node.js 代码，还可以实时收集 Node.js 进程的内存、 CPU Profile 和堆栈内存快照等数据，同时支持静态、动态开启，是一种调试和诊断 Node.js 进程非常好的方式。

通过它可以收集 Node.js 进程的堆快照分析是否有内存泄漏，可以收集 CPU Profile 分析代码的性能瓶颈，从而帮助提高服务的可用性和性能。另外，它支持动态开启，降低了安全风险，同时支持对子线程进行调试，是一个非常强大的工具。

## 工具运行机制

> 1、定位到目标进程；
>
> 2、向目标进程发送SIGUSR1信号，此时将会打开一个端口并开启调试器；
>
> 3、通过在发送SIGUSR1信号之前和之后比较打开的端口来确定调试端口；
>
> 4、从http://localhost:<port>/json获取WebSocket调试URL和会话ID；
>
> 5、使用提供的代码发送一个Runtime. evaluate请求；
>
> 6、搞定！

## 工具下载

该工具基于Rust语言开发，因此我们首先需要在本地设备上安装并配置好Rust环境。

接下来，广大研究人员可以使用下列命令将该项目源码克隆至本地：

```
git clone https://github.com/evilsocket/jscythe.git
```

### 项目构建

切换到项目目录下，然后通过cargo命令完成项目代码构建：

```
cd /jscythe
cargo build --release
```

## 工具运行

指定一个目标进程，并执行一个基础表达式语句：

```
./target/debug/jscythe --pid 666 --code "5 - 3 + 2"
```

从一个文件执行代码：

```
./target/debug/jscythe --pid 666 --script example_script.js
```

example\_script.js文件中的代码可以require任何代码模块并执行任意代码，例如：

```
require('child_process').spawnSync('/System/Applications/Calculator.app/Contents/MacOS/Calculator', { encoding : 'utf8' }).stdout
```

通过表达式语句搜索进程信息：

```
./target/debug/jscythe --search extensionHost --script example_script.js
```

查看工具帮助信息：

```
jscythe --help
```

## 工具运行截图

![](https://image.3001.net/images/20221115/1668480135_6372fc8728a2549a8b450.jpeg!small)

## 许可证协议

本项目的开发与发布遵循[GPLv3](https://github.com/evilsocket/jscythe/blob/main/LICENSE)开源许可证协议。

## 项目地址

**jscythe**：【[GitHub传送门](https://github.com/evilsocket/jscythe)】

## 参考资料

```
https://nodejs.org/en/docs/guides/debugging-getting-started/
```

# 任意代码执行 # Node.js # 代码安全 # NodeJS安全

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

关于jscythe

Node.js的Inspector机制是什么？

工具运行机制

工具下载

* 项目构建

工具运行

工具运行截图

许可证协议

项目地址

参考资料

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)