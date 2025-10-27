---
title: How I created a Docker image for NuttX
url: https://buaq.net/go-146460.html
source: unSafe.sh - 不安全
date: 2023-01-23
fetch_date: 2025-10-04T04:35:10.640161
---

# How I created a Docker image for NuttX

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

How I created a Docker image for NuttX

Skip to contentThis is the step-by-step process I took to create the Doc
*2023-1-22 01:47:16
Author: [acassis.wordpress.com(查看原文)](/jump-146460.htm)
阅读量:71
收藏*

---

[Skip to content](#content)

This is the step-by-step process I took to create the Docker image.

Create a directory just to save the file:

```
$ mkdir ~/Docker
$ cd ~/Docker
```

Install Docker case you don’t have it yet and give permission to your user:

```
$ sudo apt  install docker.io
$ sudo usermod -aG docker ${USER}
```

Log out and log in again to get into this docker group, or alternatively:

```
$ su ${USER}
```

Create the Dockerfile with the instructions to install the needed files:

```
$ vi Dockerfile
```

```
# Ubuntu as parent file
FROM ubuntu

# Update the image to the latest packages
RUN apt-get update && apt-get upgrade -y

# Install needed tools
RUN apt-get install automake bison build-essential flex gcc-arm-none-eabi gperf git libncurses5-dev libtool libusb-dev libusb-1.0.0-dev pkg-config kconfig-frontends genromfs zlib1g-dev -y

# Create how nuttxspace
WORKDIR /nuttxspace

#clone needed files:
RUN git clone https://github.com/apache/nuttx /nuttxspace/nuttx
RUN git clone https://github.com/apache/nuttx-apps /nuttxspace/apps
```

Built it:

```
$ docker build .
```

Verify if it was created correctly:

```
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
<none>       <none>    f0a673f5538d   About a minute ago   3.9GB
ubuntu       latest    6b7dfa7e8fdb   6 weeks ago          77.8MB
```

Tag the image:

```
$ docker tag f0a673f5538d acassis/ubuntu-nuttx
```

Run the image:

```
$ docker run -it acassis/ubuntu-nuttx /bin/bash
```

If everything worked fine, you could wish to submit it to Docker hub

So, re-tag the image with a version number to submit:

```
$ docker tag acassis/ubuntu-nuttx acassis/ubuntu-nuttx:v1
```

Login in the docker:

```
$ docker login
```

Send the docker image:

```
$ docker push acassis/ubuntu-nuttx:v1
```

Everything done!

If for some reason you want to remove your local image:

```
$ docker rmi -f f0a673f5538d
```

文章来源: https://acassis.wordpress.com/2023/01/21/how-i-create-a-docker-image-for-nuttx/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)