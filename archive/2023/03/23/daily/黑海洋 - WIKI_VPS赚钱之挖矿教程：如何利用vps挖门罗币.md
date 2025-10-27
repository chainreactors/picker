---
title: VPS赚钱之挖矿教程：如何利用vps挖门罗币
url: https://blog.upx8.com/3325
source: 黑海洋 - WIKI
date: 2023-03-23
fetch_date: 2025-10-04T10:22:53.179628
---

# VPS赚钱之挖矿教程：如何利用vps挖门罗币

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# VPS赚钱之挖矿教程：如何利用vps挖门罗币

发布时间:
2023-03-22

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
21070

# 免责声明

首先，利用vps挖矿这件事对于vps厂家来说，很多都是不允许的，因为挖矿会耗费更多的cpu资源，机房也会更耗电，所以一般情况下，在注册免费主机或者购买vps时候，都会有明确的提示：严谨挖矿的重要提醒。

所以，本教程只交代实现挖矿的步骤和技术问题，不做主机推荐；若遇到删机、甚至封号问题，概不负责。

# 简介

挖矿就是是指透过执行工作量证明或其他类似的电脑演算法来获取加密货币，这个过程是一种电力损耗，所以挖矿对于一些电力稀缺的地区也是被禁止的。目前挖矿主要就是利用GPU或者CPU的算力，显卡挖矿投入比价大，也能够平稳地收回成本，例如BTH和ETH都可以用GPU来算；CPU的运算能力差一些，现在用CPU可以挖狗狗币、门罗币，算来算去，还是门罗币（CMR）比较合算。

# 收益

本文介绍的挖矿收益是利用闲置vps资源，群友提供的收益为2核的vps：0.5-0.6元/天，理论上是核心数越多越好，vps越多越好，对内存和硬盘倒是没有太多要求。

# 准备工作

1、门罗币钱包
2、矿池随便选择
3、VPS，并启动挖矿程序

# 详细步骤

## 准备钱包

门罗币的钱包其实就是个地址，一搜索一大堆，不过我推荐用欧易，因为挖到门罗币其实就是变现的，欧易可以非常轻松的出售虚拟币，其他钱包则需要转币到交易所，这个过程就要损失一些利润，最后还是要转到欧易、币安，咱们不用那么麻烦，直接用欧易钱包。

*此过程大约需要8分钟！*

1、在 [https://www.cnouyi.care/join/15769557](https://blog.upx8.com/go/aHR0cHM6Ly9pd2VlYy5jb20vZ28vYUhSMGNITTZMeTkzZDNjdVkyNXZkWGxwTG1OaGNtVXZhbTlwYmk4eE5UYzJPVFUxTnc9PQ) 注册，（这里必须使用中国IP地址注册）

2、注册使用邮箱和手机号码均可，邮箱注册最后还是要绑定手机，自己弄吧，这个过程简单，认证为lv1即可；

3、在欧易app内，或者是欧易网页版，进行下面的操作：点击`资产管理`-`充币`，在币种这里选择并搜索`xmr`，网络选择`XMR-Monero`，然后你就得到了你的门罗币地址。

![钱包.png](https://iweec.com/usr/uploads/2023/03/196702764.png "钱包.png")

解释：

1、这里的充币并不是让你充值哦，充币地址是就你的门罗币钱包地址，一大长串的！

2、欧易交易所支持N多种币种，都可以用这个方法获得你的专属地址，如比特币、ETH等等！

3、下载欧易，或者注册后登录欧易官网的时候，需要网络支持，推荐用：飞瓜云，最低15元/月（ [https://www.feiguayun.com/#/register?code=jZy5gPJG](https://blog.upx8.com/go/aHR0cHM6Ly9pd2VlYy5jb20vZ28vYUhSMGNITTZMeTkzZDNjdVptVnBaM1ZoZVhWdUxtTnZiUzhqTDNKbFoybHpkR1Z5UDJOdlpHVTlhbHA1TldkUVNrYz0) ）比较稳定；ios版本需要外区ID。

4、妥善保存钱包地址，复制保存，缺少一个字母也不行。

## vps的操作

我们使用的是xmrig， GitHub地址：[https://github.com/xmrig/xmrig](https://blog.upx8.com/go/aHR0cHM6Ly9pd2VlYy5jb20vZ28vYUhSMGNITTZMeTluYVhSb2RXSXVZMjl0TDNodGNtbG5MM2h0Y21sbg) 官网：[https://xmrig.com/](https://blog.upx8.com/go/aHR0cHM6Ly9pd2VlYy5jb20vZ28vYUhSMGNITTZMeTk0YlhKcFp5NWpiMjB2)

1、在vps中下载xmrig，具体要先看 [https://github.com/xmrig/xmrig/releases](https://blog.upx8.com/go/aHR0cHM6Ly9pd2VlYy5jb20vZ28vYUhSMGNITTZMeTluYVhSb2RXSXVZMjl0TDNodGNtbG5MM2h0Y21sbkwzSmxiR1ZoYzJWeg) 中，选择对应的版本，有很多人出现了因为版本不对无法运行，然后遇到困难就放弃了的。主要看操作系统和cpu架构，请注意根据你的vps进行选择：

xmrig-6.19.0-bionic-x64.tar.gz：用于Ubuntu Bionic操作系统上的64位版本
xmrig-6.19.0-focal-x64.tar.gz：用于Ubuntu Focal操作系统上的64位版本
xmrig-6.19.0-freebsd-static-x64.tar.gz：用于FreeBSD操作系统上的64位静态版本
xmrig-6.19.0-gcc-win64.zip：用于Windows操作系统上的64位版本，使用GCC编译器
xmrig-6.19.0-linux-static-x64.tar.gz：用于Linux操作系统上的64位静态版本
xmrig-6.19.0-linux-x64.tar.gz：用于Linux操作系统上的64位版本
xmrig-6.19.0-macos-arm64.tar.gz：用于基于ARM64架构的MacOS系统上的版本
xmrig-6.19.0-macos-x64.tar.gz：用于MacOS操作系统上的64位版本

补充：Linux可以自己构建，方法见官网；

2、选择好之后，可以直接下载压缩包，或者在vps中执行 wget下载，解压；

例如：

```
wget https://github.com/xmrig/xmrig/releases/download/v6.19.0/xmrig-6.19.0-focal-x64.tar.gz
tar zxvf xmrig-6.19.0-focal-x64.tar.gz
```

3、现在你就有了这个目录，里面的三个文件：config.json SHA256SUMS xmrig，xmrig是可执行文件，config.json是配置文件。

在文件config.json中，`"max-threads-hint": 100,`是设置cpu利用率，按照自己的需求设置；
`"url": "donate.v2.xmrig.com:3333",`和 `"user": "YOUR_WALLET_ADDRESS",`，分别是矿池地址和钱包地址；

钱包地址不用说吧，改成你在欧易获得的地址；矿池地址在[https://xmrig.com/wizard](https://blog.upx8.com/go/aHR0cHM6Ly9pd2VlYy5jb20vZ28vYUhSMGNITTZMeTk0YlhKcFp5NWpiMjB2ZDJsNllYSms) 选择一个吧。

4、两种方法启动挖矿程序：

第一种是配置好config.json文件，然后执行./xmrig；第二种是命令行执行：

```
./xmrig --donate-level 5 -o pool.hashvault.pro:443 -u 87uv5yCkgq7XJy8zZRBwYGZo4t6HbTnuyShXzovhTDrgHbHQ2n1zPQQFjm1ueGdtGDJeTRWqRM2idKJ3s1TwRi1hL8piHGJ -p aa -k --tls
```

解释：

上个命令中，分别是：执行 xmrig，捐赠5%（自己可设置成1%），-u后是钱包地址， -p 后是矿工名字，这个代码可以在 [https://xmrig.com/wizard](https://blog.upx8.com/go/aHR0cHM6Ly9pd2VlYy5jb20vZ28vYUhSMGNITTZMeTk0YlhKcFp5NWpiMjB2ZDJsNllYSms) 生成；
xmrig这个程序最低抽水是1%，意思是你vps运行的100分钟里，有1分钟是给xmrig打工的；
矿池地址其实可以任选，自己随意，与vps近距离的矿池最好；
运行程序后，下面的输出，说明挖矿已经开始：

![开始挖矿.png](https://iweec.com/usr/uploads/2023/03/3812458791.png "开始挖矿.png")

# 设置后台运行

```
apt install vim screen -y
screen -S stream
```

然后在这里运行程序；

```
screen -ls
screen -d id
```

[取消回复](https://blog.upx8.com/3325#respond-post-3325)

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