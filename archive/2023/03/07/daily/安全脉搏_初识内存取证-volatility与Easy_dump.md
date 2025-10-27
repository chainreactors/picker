---
title: 初识内存取证-volatility与Easy_dump
url: https://www.secpulse.com/archives/197037.html
source: 安全脉搏
date: 2023-03-07
fetch_date: 2025-10-04T08:47:51.063310
---

# 初识内存取证-volatility与Easy_dump

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

# 初识内存取证-volatility与Easy\_dump

[工具](https://www.secpulse.com/archives/category/tools)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-06

12,588

## volatility

Volatility是一款非常强大的内存取证工具,它是由来自全世界的数百位知名安全专家合作开发的一套工具, 可以用于windows,linux,mac osx,android等系统内存取证。Volatility是一款开源内存取证框架，能够对导出的内存镜像进行分析，通过获取内核数据结构，使用插件获取内存的详细情况以及系统的运行状态。

在不同系统下都有不同的软件版本，官网地址：https://www.volatilityfoundation.org/26

## volatility工具的基本使用

### 命令格式

`volatility -f [image] --profile=[profile] [plugin]`

在分析之前，需要先判断当前的镜像信息，分析出是哪个操作系统
`volatility -f xxx.vmem imageinfo`
如果操作系统错误，是无法正确读取内存信息的，知道镜像后，就可以在--profile=中带上对应的操作系统

#### 常用插件

下列命令以windows内存文件举例

#### 查看用户名密码信息

`volatility -f 1.vmem --profile=Win7SP1x64 hashdump`

#### 查看进程

`volatility -f 1.vmem --profile=Win7SP1x64 pslist`

#### 查看服务

`volatility -f 1.vmem --profile=Win7SP1x64 svcscan`

#### 查看浏览器历史记录

`volatility -f 1.vmem --profile=Win7SP1x64 iehistory`

#### 查看网络连接

`volatility -f 1.vmem --profile=Win7SP1x64 netscan`

#### 查看命令行操作

`volatility -f 1.vmem --profile=Win7SP1x64 cmdscan`

#### 查看文件

`volatility -f 1.vmem --profile=Win7SP1x64 filescan`

#### 查看文件内容

`volatility -f 1.vmem --profile=Win7SP1x64 dumpfiles -Q 0xxxxxxxx -D ./`

#### 查看当前展示的notepad内容

`volatility -f 1.vmem --profile=Win7SP1x64 notepad`

#### 提取进程

`volatility -f 1.vmem --profile=Win7SP1x64 memdump -p xxx --dump-dir=./`

#### 屏幕截图

`volatility -f 1.vmem --profile=Win7SP1x64 screenshot --dump-dir=./`

#### 查看注册表配置单元

`volatility -f 1.vmem --profile=Win7SP1x64 hivelist`

#### 查看注册表键名

`volatility -f 1.vmem --profile=Win7SP1x64 hivedump -o 0xfffff8a001032410`

#### 查看注册表键值

`volatility -f 1.vmem --profile=Win7SP1x64 printkey -K "xxxxxxx"`

#### 查看运行程序相关的记录，比如最后一次更新时间，运行过的次数等

`volatility -f 1.vmem --profile=Win7SP1x64 userassist`

#### 最大程序提取信息

`volatility -f 1.vmem --profile=Win7SP1x64 timeliner`

## 电子取证之Easy\_dump(2018护网杯)

### 查看镜像信息

`volatility -f easy_dump.img imageinfo`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095954.png "null")

查看结果，推测可能是Win7SP1x64的镜像

### 指定镜像进行进程扫描

volatility -f easy\_dump.img --profile=Win7SP1x64 psscan

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095955.png "null")

也可以使用pslist参数
发现存在notepad.exe，查看一下内容。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095959.png "null")

### 导出进程中内容

volatility -f easy\_dump.img --profile=Win7SP1x64 memdump -p 2616 -D /xxx/xxx/xxx/
其中procdump：是提取进程的可执行文件
memdump：是提取进程在内存中的信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095963.png "null")

### 使用strings查找flag信息

strings -e l 2616.dmp | grep "flag"
发现提示是jpg

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095964.png "null")

### 读取jpg文件

volatility -f easy\_dump.img --profile=Win7SP1x64 filescan | grep "jpg"
发现图片phos.jpg

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095969.png "null")

导出图片

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-16780959691.png "null")

查看图片，无法正常打开

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095970.png "null")

使用binwalk查看，发现存在zip文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095971.png "null")

### 分离文件

foremost file.None.0xfffffa8008355410.vacb

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095974.png "null")

分离后自动生成output文件夹，查看内容
解压00004372.zip，得到message.img
继续使用binwalk提取文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095975.png "null")

得到hint.txt

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095976.png "null")

### 使用脚本进行转换

查看其他大佬说可能是左边，使用脚本进行转换

```
#脚本文件
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
with open('hint.txt','r') as f:
    datas = f.readlines()
for data in datas:
    arr = data.split(' ')
x.append(int(arr[0]))
y.append(int(arr[1]))

plt.plot(x,y,'ks',ms=1)
plt.show()
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095978.png "null")

扫描二维码得到提示，一个是维吉尼亚加密，秘钥是aeolus。一个是加密文件被删除了，需要恢复。

### 恢复文件

使用testdisk进行恢复
testdisk message.img

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095979.png "null")

红色为需要恢复的文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095983.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095989.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095993.png "null")

使用ls -a查看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095996.png "null")

使用strings查看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-16780959961.png "null")

最后一句字符串尝试解密
得到最终结果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197037-1678095998.png "null")

### 参考资料

https://www.cnblogs.com/zaqzzz/p/10350989.html https://blog.csdn.net/weixin\_42742658/article/details/106819187

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注...