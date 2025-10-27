---
title: heiher/hev-socks5-tunnel: Tunnel over Socks5 proxy (tun2socks) for Linux/Android/FreeBSD/macOS (IPv4/IPv6/TCP/UDP)
url: https://buaq.net/go-150048.html
source: unSafe.sh - 不安全
date: 2023-02-20
fetch_date: 2025-10-04T07:32:11.678589
---

# heiher/hev-socks5-tunnel: Tunnel over Socks5 proxy (tun2socks) for Linux/Android/FreeBSD/macOS (IPv4/IPv6/TCP/UDP)

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

![](https://8aqnet.cdn.bcebos.com/c430b0019005722a1d48376e5f7871f3.jpg)

heiher/hev-socks5-tunnel: Tunnel over Socks5 proxy (tun2socks) for Linux/Android/FreeBSD/macOS (IPv4/IPv6/TCP/UDP)

A tunnel over Socks5 proxy (tun2socks) for Unix.FeaturesIPv4/IPv6. (dual stack)Re
*2023-2-19 14:44:26
Author: [github.com(查看原文)](/jump-150048.htm)
阅读量:399
收藏*

---

[![status](https://camo.githubusercontent.com/1bde0a472f2210d73d7b5de23e0f342afac9d037b1b5f7ec33ce8176df349693/68747470733a2f2f6769746c61622e636f6d2f6865762f6865762d736f636b73352d74756e6e656c2f6261646765732f6d61737465722f706970656c696e652e737667)](https://gitlab.com/hev/hev-socks5-tunnel/commits/master)

A tunnel over Socks5 proxy (tun2socks) for Unix.

## Features

* IPv4/IPv6. (dual stack)
* Redirect TCP connections.
* Redirect UDP packets. (Fullcone NAT, UDP in UDP/TCP)
* Linux/Android/FreeBSD/macOS.

## Benchmarks

See [here](https://github.com/heiher/hev-socks5-tunnel/wiki/Benchmarks) for more details.

### Speed

[![](https://github.com/heiher/hev-socks5-tunnel/wiki/res/upload-speed.png)](https://github.com/heiher/hev-socks5-tunnel/wiki/res/upload-speed.png)
[![](https://github.com/heiher/hev-socks5-tunnel/wiki/res/download-speed.png)](https://github.com/heiher/hev-socks5-tunnel/wiki/res/download-speed.png)

### CPU usage

[![](https://github.com/heiher/hev-socks5-tunnel/wiki/res/upload-cpu.png)](https://github.com/heiher/hev-socks5-tunnel/wiki/res/upload-cpu.png)
[![](https://github.com/heiher/hev-socks5-tunnel/wiki/res/download-cpu.png)](https://github.com/heiher/hev-socks5-tunnel/wiki/res/download-cpu.png)

## How to Build

### Unix

```
git clone --recursive https://github.com/heiher/hev-socks5-tunnel
cd hev-socks5-tunnel
make
```

### Android

```
mkdir hev-socks5-tunnel
cd hev-socks5-tunnel
git clone --recursive https://github.com/heiher/hev-socks5-tunnel jni
ndk-build
```

## How to Use

### Config

```
tunnel:
  # Interface name
  name: tun0
  # Interface MTU
  mtu: 9000
  # IPv4 address
  ipv4:
    address: 100.64.0.2
    gateway: 100.64.0.1
    prefix: 30
  # IPv6 address
  ipv6:
    address: 'fc00::2'
    gateway: 'fc00::1'
    prefix: 126

socks5:
  # Socks5 server port
  port: 1080
  # Socks5 server address (ipv4/ipv6)
  address: 127.0.0.1
  # Socks5 UDP relay mode (tcp|udp)
  udp: 'tcp'
  # Socks5 server username
# username: 'username'
  # Socks5 server password
# password: 'password'

#misc:
   # task stack size (bytes)
#  task-stack-size: 20480
   # connect timeout (ms)
#  connect-timeout: 5000
   # read-write timeout (ms)
#  read-write-timeout: 60000
   # stdout, stderr or file-path
#  log-file: stderr
   # debug, info, warn or error
#  log-level: warn
   # If present, run as a daemon with this pid file
#  pid-file: /run/hev-socks5-tunnel.pid
   # If present, set rlimit nofile; else use default value
#  limit-nofile: 1024
```

### Run

```
bin/hev-socks5-tunnel conf/main.yml

# Bypass upstream socks5 server
sudo ip route add SOCKS5_SERVER dev DEFAULT_IFACE metric 10
sudo ip -6 route add SOCKS5_SERVER dev DEFAULT_IFACE metric 10

# Route others
sudo ip route add default dev tun0 metric 20
sudo ip -6 route add default dev tun0 metric 20
```

## Contributors

* **hev** - <https://hev.cc>

## License

MIT

文章来源: https://github.com/heiher/hev-socks5-tunnel
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)