---
title: 用Go语言重写了gh-proxy加速
url: https://buaq.net/go-256720.html
source: unSafe.sh - 不安全
date: 2024-08-18
fetch_date: 2025-10-06T18:02:15.364768
---

# 用Go语言重写了gh-proxy加速

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

用Go语言重写了gh-proxy加速

支持 git clone , wget , curlDome：gh.jiasu.in测试：https://gh.jiasu.in/https://git
*2024-8-17 23:21:0
Author: [www.upx8.com(查看原文)](/jump-256720.htm)
阅读量:14
收藏*

---

支持 git clone , wget , curl

源码：[https://github.com/0-RTT/ghproxy-go](https://www.nodeseek.com/jump?to=https%3A%2F%2Fgithub.com%2F0-RTT%2Fghproxy-go)

安装go

```
sudo apt update
sudo apt upgrade
wget https://golang.org/dl/go1.22.5.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.22.5.linux-amd64.tar.gz
sudo nano /etc/profile
export PATH=$PATH:/usr/local/go/bin
source /etc/profile
go version
```

配置ghproxy.service

```
sudo bash -c 'cat << EOF > /etc/systemd/system/ghproxy.service
[Unit]
Description=ghproxy
After=network.target

[Service]
ExecStart=/usr/local/go/bin/go run /main.go所在路径
Restart=always
User=root
Group=root
WorkingDirectory=/main.go所在路径

[Install]
WantedBy=multi-user.target
EOF'
```

示例：

```
[Unit]
Description=ghproxy
After=network.target

[Service]
ExecStart=/usr/local/go/bin/go run /www/wwwroot/gh.jiasu.in/main.go
Restart=always
User=root
Group=root
WorkingDirectory=/www/wwwroot/gh.jiasu.in

[Install]
WantedBy=multi-user.target
```

设置开机自启：`systemctl enable ghproxy.service`

启动：`systemctl start ghproxy.service`

重启：`systemctl restart ghproxy.service`

查询运行状态：`systemctl status ghproxy.service`

配置nginx反代

```
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
```

#### CF worker版：<https://github.com/0-RTT/ghproxy>

文章来源: https://www.upx8.com/4285
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)