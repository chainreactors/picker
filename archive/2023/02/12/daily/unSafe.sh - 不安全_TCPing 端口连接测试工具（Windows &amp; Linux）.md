---
title: TCPing 端口连接测试工具（Windows &amp; Linux）
url: https://buaq.net/go-148963.html
source: unSafe.sh - 不安全
date: 2023-02-12
fetch_date: 2025-10-04T06:25:26.399709
---

# TCPing 端口连接测试工具（Windows &amp; Linux）

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

![](https://8aqnet.cdn.bcebos.com/dde2349733c71cc6e7121d12033cd77b.jpg)

TCPing 端口连接测试工具（Windows &amp; Linux）

平时我们Ping服务器的IP，只是ICMP协议传输获得的延迟，而某些IDC会把ICMP的延迟优化的很棒，实际上一走TCPing 就暴露了;而且我们使用
*2023-2-11 17:10:0
Author: [blog.upx8.com(查看原文)](/jump-148963.htm)
阅读量:38
收藏*

---

* 平时我们`Ping`服务器的IP，只是`ICMP`协议传输获得的延迟，而某些`IDC`会把`ICMP`的延迟优化的很棒，实际上一走`TCPing` 就暴露了;而且我们使用过程中主要是`TCP`协议传输数据，所以可以测试一下`TCPing`得到的延迟;另外因为`TCP`协议的握手步骤原因，他会比`ICMP`得到的延迟高一点点，如果高很多，那么怕是`ICMP`协议被特殊优化过；
* 除了上面说的情况，我们还能用`TCPing`来检测目标`IP`的某个端口是否开放（或者通顺，如果服务器防火墙开放了，而你测试确无法访问，那么说明端口被封），当然这个功能`Windows`自带的`telnet`客户端组件也能实现，不过今天只说TCPing；
* 如果一个服务器禁Ping，那么就无法使用`ICMP`协议的`Ping`来检测延迟了，那么你就可以用`TCPing`来检测延迟，当然前提是你知道哪个端口是开放的，因为`TCPing`必须要知道一个开放的端口才能正常运作；

**更新系统软件源**

```
# CentOS
yum update -y

# Debian/Ubuntu
apt-get update -y
```

**安装依赖**

```
# CentOS
yum install -y tcptraceroute bc

# Debian/Ubuntu
apt-get install -y tcptraceroute bc
```

**下载执行文件**

```
# 切换目录
cd /usr/bin

# 下载执行文件
wget https://raw.githubusercontent.com/sunpma/cdn/master/other/tcping

# 赋予执行权限
chmod +x tcping
```

**测试TCPing**

```
tcping 114.114.114.114 53
```

**测试结果**

```
# 用法：tcpping [-d] [-c] [-C] [-w sec] [-q num] [-x count] ipaddress [port]
# -d 在每个响应时间前，打印时间戳
# -c 以列表形式显示
# -C 输出类似于fping工具中-C选项的结果
# -w 等待时间（默认 3）
# -r 每N秒重试一次（默认 1）
# -x 限定测试总时长 (默认 无限)
```

下载需要使用的`TCPing`工具
解压后将`tcping.exe`放在`C盘`根目录即可，无需安装；
TCPing 下载地址：

**TCPing 下载地址：<https://sunpma.lanzoui.com/i678hxg>**
在电脑端开始菜单中打开`CMD`即`命令提示符`
测试命令如下：

```
# 进入C盘
cd/
# 进入指定路径（例：进入C盘下test目录）
cd /d C:\test
# 常规端口测试命令
tcping +IP +端口
# 例（注意中间有空格）
tcping 8.8.8.8 443
```

其他常用命令：

```
# -t     : 连续 TCPing ，直到使用 Ctrl+C 键停止
tcping -t 114.114.114.114 80

# -n 5   : TCPing 5次后停止
tcping -n 5 114.114.114.114 80

# -i 5   : 每隔 5秒 TCPing 一次
tcping -i 5 114.114.114.114 80

# -w 0.5 : 设置超时时间为 0.5秒（1秒=1000毫秒），单位 秒
tcping -w 0.5 114.114.114.114 80

# -d     : 在每行返回信息中加入时间信息
tcping -d 114.114.114.114 80

# -s     : 当 TCPing 测试成功后（在超时时间以内返回 TCPing 延迟数据）自动停止 TCPing
tcping -s 114.114.114.114 80

# -4     : 优先 IPv4（如果一个域名有 IPv4 和 IPv6 解析，那么走 IPv4）
tcping -4 www.baidu.com 80

# -6     : 优先 IPv6（如果一个域名有 IPv4 和 IPv6 解析，那么走 IPv6）
tcping -6 www.baidu.com 80

# --file : TCPing 将逐行循环遍历文件内的 服务器IP/域名 信息（一行一个，支持端口，例如：114.114.114.114 80）
tcping --file D:\abc\1.txt

# -v : 显示版本号
tcping -v

# 如果你没有写服务器地址的端口，那么默认为 80 端口
```

**测试结果**
[![](https://sunpma.com/usr/uploads/2021/06/2517640151.png)](https://sunpma.com/usr/uploads/2021/06/2517640151.png)

文章来源: https://blog.upx8.com/3216
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)