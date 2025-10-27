---
title: timwhitez starred subsocks
url: https://buaq.net/go-171651.html
source: unSafe.sh - 不安全
date: 2023-07-11
fetch_date: 2025-10-04T11:51:23.358217
---

# timwhitez starred subsocks

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

![]()

timwhitez starred subsocks

A Socks5 proxy that encapsulates Socks5 in other security protocolsIntroductionSu
*2023-7-10 19:5:24
Author: [github.com(查看原文)](/jump-171651.htm)
阅读量:43
收藏*

---

A Socks5 proxy that encapsulates Socks5 in other security protocols

[![build](https://camo.githubusercontent.com/c0bd1cf9e1b9454a6066b5e84cf070ad0d4baa8b97af825e7a74b1b3a4849ca8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f776f726b666c6f772f7374617475732f6c7579756875616e672f737562736f636b732f4275696c64)](https://github.com/luyuhuang/subsocks/actions)
[![release](https://camo.githubusercontent.com/07b6785783f6bdbd7e0854a11deacac439dff0b25ecb257b1036c9013ca3f454/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f6c7579756875616e672f737562736f636b732e737667)](https://github.com/luyuhuang/subsocks/releases)
[![docker](https://camo.githubusercontent.com/e734e003822a0603192913055e72b369ec164c60cbc606f7f0124a84e96cb5d9/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f696d6167652d73697a652f6c7579756875616e672f737562736f636b73)](https://hub.docker.com/r/luyuhuang/subsocks)

## Introduction

Subsocks is a secure Socks5 proxy. It encapsulate Socks5 in other security protocols such as HTTPS and Websocket instead of using Socks5 directly. Socks5 is fully supported (Connect, Bind, UDP associate), and extending Socks5 to make UDP over TCP possible. It helps you optimize your network or bypass firewalls that only allow some particular protocols.

[![protocols](https://github.com/luyuhuang/subsocks/raw/master/protocols.svg)](https://github.com/luyuhuang/subsocks/blob/master/protocols.svg)

* Fully support Socks5 (Connect, Bind, UDP associate)
* Support HTTP proxy
* Transport over HTTP / HTTPS
* Transport over Websocket
* HTTP authorization
* Smart proxy

## Installation

### go get

Subsocks is written by Go, If you have Go environment, using `go get` is one of the easiest ways.

```
go get github.com/luyuhuang/subsocks
```

### Docker

```
docker pull luyuhuang/subsocks
```

### Binary file

Download the binary file from the [release page](https://github.com/luyuhuang/subsocks/releases).

### Build from source code

You can also build from source code.

```
git clone https://github.com/luyuhuang/subsocks.git
cd subsocks
go build
```

## Usage

### Getting started

A Subsocks instance may be a client or a server, determined by the configuration. A Subsocks client receives Socks5 data from Apps and encapsulate Socks5 data into a security protocol like HTTPS, then forward it to the Subsocks server. The Subsocks server unpacks the data from the client and accesses the internet.

[![forward](https://github.com/luyuhuang/subsocks/raw/master/forward.svg)](https://github.com/luyuhuang/subsocks/blob/master/forward.svg)

Create the client configuration file `cli.toml` with the following content:

```
[client]
listen = "127.0.0.1:1030"

server.protocol = "https"
server.address = "SERVER_IP:1080" # replace SERVER_IP with the server IP

http.path = "/proxy" # same as http.path of the server
tls.skip_verify = true # skip verify the server's certificate since the certificate is self-signed
```

Then start the client:

Similarity, create the server configuration file `ser.toml`:

```
[server]
listen = "0.0.0.0:1080"
protocol = "https"

http.path = "/proxy"
```

And then start the server:

### With Docker

Download `docker-compose.yml`:

```
wget https://raw.githubusercontent.com/luyuhuang/subsocks/master/docker-compose.yml
```

Create the configuration file `config.toml`:

```
[server] # no one will use docker for the client, right?

# must be "0.0.0.0:1080". It's just the address in the
# container, modify the real address in docker-compose.yml
listen = "0.0.0.0:1080"

protocol = "https"
# other fields ...
```

Launch:

> NOTICE: If you want to use a custom certificate, edit `docker-compose.yml` and create a volume to map it to the container.

## Configuration

Subsocks configuration format is [TOML](https://github.com/toml-lang/toml), which is easy and obvious.

### Client configuration

The client configuration format is as follows:

```
[client] # client configuration

listen = "127.0.0.1:10030"

username = "admin"
password = "123456"

server.protocol = "wss"
server.address = "10.1.1.1:443"

http.path = "/proxy"

ws.path = "/proxy"

tls.skip_verify = false
tls.ca = "server.crt"
```

#### Basic fields

* `listen`: string, the client socks5/http listening address.
* `username`, `password`: string, username and password used to connect to the server.
* `server.protocol`: string, protocol of the server, the value may be:
  + `socks`: pure socks5;
  + `http`, `https`: HTTP and HTTPS;
  + `ws`, `wss`: Websocket and Websocket Secure.
* `server.address`: string, address of the server.

#### HTTP

If `server.protocol` is `http` or `https`, `http.*` is enabled.

* `http.path`: string, HTTP request path. Default `/`.

#### Websocket

If `server.protocol` is `ws` or `wss`, `ws.*` is enabled.

* `ws.path`: string, Websocket handshake path. Default `/`.

#### TLS/SSL

If the protocol is over TLS, i.e. `server.protocol` is `https` or `wss`, `tls.*` is enabled.

* `tls.skip_verify`: boolean, skip verifying the server's certificate if the value is true. Default false. It's not safe to skip verifying the certificate, if the server's certificate is self-signed, please set `tls.ca` to verify the certificate.
* `tls.ca`: string, a certificate file name. It's optional. If set, Subsocks will use the specific CA certificate to verify the server's certificate.

#### Smart Proxy

If there is a `rules` field, enable smart proxy. Smart proxy is only available for the Connect method since we don't know the real peer when using Bind or UDP Associate. There are two ways to configure proxy rules. One is setting the `rules` field to a table containing proxy rules:

```
[client.rules]
"www.twitter.com" = "P"
"*.github.com" = "D"
"8.8.8.8" = "P"
"1.0.1.0/24" = "D"
"2001:db8::/32" = "P"

"*" = "A"
```

Each pair in the table is a rule. The left side of `=` is the address, which can be:

* Domain, a wildcard `*` indicates all subdomains of the domain;
* IP and CIDR;
* A single wildcard `*` represents all other addresses.

The right side of `=` is the rule, which can be:

* `P`, `proxy`: always via the server;
* `D`, `direct`: always direct connect;
* `A`, `auto`: automatic detection, proxy if the direct connection fails.

Another way is using a separate file to configure rules and set the `rules` field to a string representing the file name:

The contents of `rules.txt` are as follows:

```
www.twitter.com     P
8.8.8.8
2001:db8::/32

*.github.com        D
1.0.1.0/24

# all others is automatic detection
*   A
```

Each line is a rule, except empty lines and comment lines(starting with `#`). Each line contains an address and an optional rule, separated by several spaces. If a line doesn't have a rule, its rule is the same as the previous line.

#### Authorization

If there is a `users` field, then enable authorization. In this case, applications that use proxy via the client must be authorized. There are two ways to configure the user list. One is using the [htpasswd](https://httpd.apache.org/docs/2.4/programs/htpasswd.html) file, setting the `user` field to a string indicating the htpasswd file name:

Another way is configuring username-password pairs directly. Setting the `users` field to a table containing username-password pairs:

```
[client.users]
"admin" = "123456"
"guest" = "abcdef"
```

### Server configuration

The server configuration format is as follows:

```
[server] # server configuration

protocol = "wss"
l...