---
title: 如何使用Mangle修改已编译的可执行文件以绕过EDR检测
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247532672&idx=3&sn=9c865bc9f4d1201fe73e7d779cb794a3&chksm=fa93f641cde47f57b9fc5dbec14ca8686e29bc45f9c317b2f4849085354557dc0bfef6d9c979&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-11-12
fetch_date: 2025-10-03T22:33:06.041873
---

# 如何使用Mangle修改已编译的可执行文件以绕过EDR检测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mvUjsggs7btQtSWc06u50vCZzEUs92eYBB4YX6d0Jj7g4e63w4DbfvLibFSgbeElq331zv2xKMgOA/0?wx_fmt=jpeg)

# 如何使用Mangle修改已编译的可执行文件以绕过EDR检测

网络安全应急技术国家工程中心

以下文章来源于FreeBuf
，作者Alpha\_h4ck

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM44FYfJ7GCP22pqkVUnTy8uqVR5bWNRIsyrSc23ffYDCg/0)

**FreeBuf**
.

中国网络安全行业门户

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mvUjsggs7btQtSWc06u50vTvib33TN53vSEJWiapE8qE7WQqYgbE1XAicFmYXX4MibD6QFclokEMKwOw/640?wx_fmt=jpeg)

**关于Mangle**

Mangle是一款功能强大的代码处理和安全测试工具，该工具基于Golang开发，可以帮助广大研究人员从各个方面对已编译好的可执行程序（.exe或DLL）进行修改，从而实现EDR检测绕过。

**工具运行机制**

Mangle可以删除基于字符串的入侵威胁指标（IoC），并将其替换为随机字符，然后通过增加文件大小来避免EDR检测，而且还可以通过合法文件来克隆代码签名证书。在整个过程中，Mangle可以帮助加载器绕过磁盘和内存扫描工具的检测。

**工具安装**

首先，该工具基于Golang开发，因此我们需要在本地设备上安装并配置好Golang环境。接下来，使用下列命令将该项目源码拉取到本地，然后安装该工具所需的依赖组建，并编译项目代码：

```
```
go get github.com/Binject/debug/pe
```
```

然后，使用下列命令构建项目源码：

```
```
go build Mangle.go
```
```

## 工具使用

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39Pqllf4GM9lWR4c0SqelyDe06PrUZNk9hpvs6XwntnbUZxD7jc2UXShUaC8PgFWsXOic8vFuHWzDQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**参数解释**

###

> -C 字符串：包含需要克隆的证书路径；
>
> -I 字符串：原始文件路径；
>
> -M 字符串：编辑PE文件以替换/去除Go标识符指定的字符串；
>
> -O 字符串：新文件名称；
>
> -S 整数：需要增加多少文件大小；

### **字符串**

Mangle可以获取研究人员提供的可执行文件并寻找那些安全产品可能会搜索或触发安全警报的已知字符串。这些字符串并不是唯一的检测因素，因为反病毒产品一般会将这些字符串和其他（遥测）数据结合起来检测。而Mangle可以找到这些已知的字符串，并用随机值替换掉字符串的十六进制值，然后移除原始字符串。需要注意的是，这种替换方式并不会改变文件大小，这样可以防止文件报错。

字符串修改样例：修改前。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39Pqllf4GM9lWR4c0SqelyDeVRpMRVbpZtZGbGTud30kXWDshqPA5Fx1fbh67rgnEUhNMTYLhmniaQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

字符串修改样例：修改后。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39Pqllf4GM9lWR4c0SqelyDpqeic43b8BdlFk5ibxQ9ImMpM3N5FNKjbx1VXuKScNToLSJ2nGAE9ibuQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

### **文件体积增加**

几乎所有EDR都无法扫描磁盘或内存中超过一定大小的文件，因为大文件需要更长的时间来查看、扫描或监视，而EDR不希望通过降低用户的生产率来影响性能。Mangle通过在文件末尾创建空字节（零）填充来增加文件体积，这样可以确保文件内的任何内容都不会受到影响。建议将大小增加95-100 MB，不建议制作2 GB或以上的文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mvUjsggs7btQtSWc06u50vDvmeod4CVcVQJA4mSpqPMEmLBwm5UfkJf3PRgx10gsuN37LysHWzJg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mvUjsggs7btQtSWc06u50vILKicRj067njzKeiag7czd4w2Q1j9ZnlToba8qh2WSicxyiaRibQlKNqGpg/640?wx_fmt=jpeg)

### **证书克隆**

Mangle还可以从一个文件中获取合法代码签名证书的完整链和所有属性，并将其复制到另一个文件。其中包括签名日期、反签名和其他可测量的属性：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39Pqllf4GM9lWR4c0SqelyDqZRlj2l1UQVI1zrALiaibGticibux140CBcZsOMR1niadsHq4XdSEziaVmlg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**许可证协议**

本项目的开发与发布遵循MIT开源许可证协议。

**项目地址**

Mangle：https://github.com/optiv/Mangle

## **参考资料：**

## https://github.com/Tylous/Limelighter

## https://github.com/Binject/debug

##

##

原文来源：FreeBuf

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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