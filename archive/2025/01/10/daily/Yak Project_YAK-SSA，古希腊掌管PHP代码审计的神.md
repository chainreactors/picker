---
title: YAK-SSA，古希腊掌管PHP代码审计的神
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247527451&idx=1&sn=4b2437412b3ace4a09c992456162bad7&chksm=c2d110bff5a699a9734277d9db22716b10c1dc66637932c73b7170faadfc1818227b8088fcb9&scene=58&subscene=0#rd
source: Yak Project
date: 2025-01-10
fetch_date: 2025-10-06T20:09:49.055810
---

# YAK-SSA，古希腊掌管PHP代码审计的神

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZfJmOMMoESIlf9ibldFD1zibD2iaMYkyj76FyvrlSr2iaPpurOa7oTCSyPsiaDlfeWSr3lKibyMM84B2lkg/0?wx_fmt=jpeg)

# YAK-SSA，古希腊掌管PHP代码审计的神

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

之前的文章中曾为大家简单介绍过

**线上代码审计平台ssa.to**

今天牛牛就来为大家详细介绍一下

如何用ssa进行PHP的代码审计

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudic6NWfMSJWFgz2JwxI10Z4Qoxs5YLH3oibnffYlSbojWtzPDMOvPh2ZA/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGH3K8HYicjeoOvSxlmt6NPlV6aZGXIUFjD0nzos7x3Sk2zj6X0tFbtsg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbG2TCcECTich3iccqicLIpD9HibJeIVLEiaQQOhXYsfmAzOKy32T4ibHQ73S8A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGWzFK5efozUKbPK8y07ibfibZBOIj02d21jxicYc52ibUeRKoKW09rKeCIw/640?wx_fmt=png&from=appmsg)

* tp封装的辅助参数，I/request方法
* thinkphp中的封装了请求对象，$request
* 路由参数绑定

> 在thinkphp中，I方法的过滤并不是时时刻刻都会起作用，在底层中，I如果没有显示的指定过滤参数，其过滤参数需要去config文件中去指定，如果也没有指定，就和传统的参数获取没有区别。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGDDpSEibdseLJaHYmqrAILgv5TL4TyLNh4FyCmv6ic9IK8z4LH4TLhalg/640?wx_fmt=png&from=appmsg)

在tp中，会涉及到一些底层API的封装，开发者不必利用底层API的实现，只要学会使用即可。所以在代码审计的时候，可以找到这些函数，实现从source点到sink点的路径缩短。实现更加精确的数据流分析。

##### 数据库相关：

```
Db::table()xx->insert()xx->update()xx->delete()$model::where()Db::transaction()
```

##### 文件上传相关：

在tp底层中，常见的文件上传辅助函数有：

```
$file->move()$file->check()$file->save()Filesystem()等$file->error()$file->getError()
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGV3IpbyR2eyBA2ZNgUhvEZ5Rkuic6tuljr8CPSc6Z6Nq27IJVq6VrxrA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGrUunB3ibzruPLUXGSfODeDb0SkuqzvWdrW9libFEibISPPgODG6NXLSYw/640?wx_fmt=png&from=appmsg)

在之前的文章中，会涉及到很多规则编写部分，而ssa官网也提出了syntaxflow的简单实用，重点功能为：

```
$source #-> as $sink  //顶级定义$source --> as $sink  //底级实用
其次：比较重要的两个configinclude: 路径上有（包含）exclude: 路径上无（排除）
```

> 在上面的基础上，可以配合过滤器的使用和集合运算，来实现更多的自定义规则

##### 简单的规则编写：

###### 在寻找顶级定义的过程中排序路径上的某些内容

```
<?php
$a = 1;if($a){    $a = filter($a);}else{    $a = unsafe($a);}eval($a);
```

画出来的控制流图为：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGRGpjwCQdofk4eALtKc9FMbUxYYyQsdaa7cEoFlSyhMnVksG1ADEsqw/640?wx_fmt=png&from=appmsg)

一共有两个分支到达done block，想到无过滤器的一条路径，规则如下：

```
//寻找顶级定义的过程中，排除路径上filter的

*a #{exclude: `*?{have: filter}`}-> as $sink
/*  $sink:    t75: Undefined-unsafe        .:7:10 - 7:16    t66: 1        .:3:6 - 3:7*/
```

但是会发现，这个并不是想到的内容，原因就出现在，我们需要让它与可控变量做交集 。需要让它的顶级调用者中，出现可控变量，这样的话，再次改写代码。

```
// 寻找顶级定义的过程中，路径上包含与_POST相交的点，并且排除filter_POST as $source*a #{exclude: <<<CODE*?{have: filter}CODE,include: <<<CODE* & $sourceCODE}-> as $sink
```

在这样的一个简单demo学习之后，我们就可以进入实战演示。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGicpVqNHshoEAaQtdjh3TIt2R4wcVcH73dMV4iaHY7GdtF4ycelFtEx0A/640?wx_fmt=png&from=appmsg)

在github中找到一个cms，在yakssa中进行编译。

> 在编译过程中，会发现，代码多之后编译的很慢，这是因为在php中会有依赖，像go一样，而这些依赖一般都是用来辅助开发者去完成某项功能，比如imageutil、wechat等依赖，可以在编译的过程中，跳过这些依赖的编译，虽然代码不是完整的，但是ssa也可以实现审计。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGCSDPxJG4YcHuviavNlSpVRY1YibQHYscQ0tLSvVe98ykWgq4ltkCiaeRQ/640?wx_fmt=png&from=appmsg)

搜索thinkphp中常见的可控变量。然后写成一条规则。

```
request() as $source1input() as $source3i() as $source4*request.get() as $source5*request.post() as $source6.input() as $source7.param() as $source8.post() as $source9$source1+$source3+$source4+$source5+$source6+$source7+$source8+$source9 as $source
```

```
![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGEwl4ru6jFUSPVgl9jkCQVE3QAGYCgLttRAoFgIZIYhyIjyJ0V7QmIg/640?wx_fmt=png&from=appmsg)
```

xss分为很多种，这里以最简单的反射和存储来进行说明。

* 反射xss ：由用户手动控制，直接输出到页面。
* 存储xss：由用户手动控制，但存储到数据库中。

这里写一条存储xss的sf语句。

```
request() as $source1input() as $source3i() as $source4*request.get() as $source5*request.post() as $source6.input() as $source7.param() as $source8.post() as $source9$source1+$source3+$source4+$source5+$source6+$source7+$source8+$source9 as $source
.add() as $func5.save() as $func6$func5 +$func6 as $func
$func #{include: `* & $source`}-> as $sink
```

审计出来的内容很多，这里我们一一查看。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGuCpIKbVd1W8gK0hokr80q0q6R0owV2O81kia8aso6tBFmqXRoSdVXZg/640?wx_fmt=png&from=appmsg)

定位到system.php文件中，先做了请求判断，如果有的话返回已经存在，如果没有的话，将内容进行添加，这里跟进发现。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGia0vdnwme2t4PLSugyrMZx3ZzTjhHjCLnib2IGo5TxcH2wicfVVZdXLmA/640?wx_fmt=png&from=appmsg)

会将最后的内容存放到数据库中。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbG496YNtCX0vlHnLkrpQzKR3mPfNpVQFH3KCped9VeSXFJuX1myuUFYg/640?wx_fmt=png&from=appmsg)

> 注意：不是所有的I方法都有漏洞，在之前tp的代码审计中提到，参数可以配置默认过滤。

此项目中，因为没有配置默认过滤，可以直接根据路由传入参数。

```
POST /index.php/admin/sys.Auth/groupAdd HTTP/1.1Host: 10.211.55.11:8092Upgrade-Insecure-Requests: 1Accept-Language: zh-CN,zh;q=0.9Referer: http://10.211.55.11:8092/index.php/admin/indexUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Cookie: think_lang=zh-cn; PHPSESSID=655381238c1f39ebb2ccbc7cb5d7830e; Hm_lvt_d7fcc824c81abdf6e6d33ffc0e10c071=1736077733,1736168831; Hm_lpvt_d7fcc824c81abdf6e6d33ffc0e10c071=1736168831; HMACCOUNT=8C60E645EC57F215Connection: keep-aliveAccept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded
title=<script>alert(1)</script>
```

根据syntaxflow找到的内容，基本上都有xss漏洞，至少3处。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbG7dYaBvfhAIqdKA3ibyrRDlL31pq7lzDvskMj8XrbdAK4bXiaqgulIhqA/640?wx_fmt=png&from=appmsg)

```
.request().file() as $source1request().file() as $source2
$source1+$source2 as $source
$source
```

定位到文件upload.php中，可以看到是过了一层校验，thinkphp validate，这里可以去看下，简单来说就是对数组进行过滤。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGTiaictMoU5icbyZGIco5XfcWja8PVxcaFmg1u48Ov1mUyicgbrAXv4Y7Eg/640?wx_fmt=png&from=appmsg)

此处的过滤器写的有问题，正确的过滤器如下。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGc9YBV7rFcFgEzUibTmN1VnCajFNRAsSBx8wLfDlMesVUbUQveI0fDLA/640?wx_fmt=png&from=appmsg)

上传文件即可。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGicYrOJuibsxllmHuYd2KkH415WQujcy5Ky2zfRGrAVrqczhYwu233Siag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGEXnqYC1cmzJiakPqnQdb02qSCkClY1RKgcLzJTnWz5kMO8pOcfcLUVQ/640?wx_fmt=png&from=appmsg)

通过对输入点的审计，找到这样一段代码。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGYLovbibxB19Y4yUKxafY5zibJDdSu6jjc0BpKM9u8XBGeK4CoCM8ibXYQ/640?wx_fmt=png&from=appmsg)

* 时间戳校验
* appid校验
* 签名校验

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGcfjRZhic24SAa6KUpD3ahdTBfUCNh4IIBcJbnfPzuibMrniaTMnnyW5tQ/640?wx_fmt=png&from=appmsg)

是根据输入来计算的MD5（可以使用热加载来写）

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGwXeJpsKm65OBetX62D0SPMCGEibUR0wyLb2m08LCSibGvibqs3q8mZ2gw/640?wx_fmt=png&from=appmsg)

而数据库中有默认的appid和appsecret。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGlO3eXrNLgYKicNLxFAjGkL34sqcs3bCLwVZhoo7qakpvYLEnQWP0BWw/640?wx_fmt=png&from=appmsg)

判断是否有用户名，并且进行密码校验。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdchaKJMENDtyicNXVR5MXbGncGTODwgPndEYlfMKAZDia8Vz41FibR8ea1nCF1yzapKlicXPH6viaur1Q/640?wx_fmt=png&from=appmsg)

```
// 使用标签 {{yak(handle|param)}} 可触发热加载调用handle = func(param) {    // 在这里可以直接返回一个字符串}
// 使用标签 {{yak(handle1|...)}} 可触发热加载调用handle1 = func(param) {    // 这个特殊的 Hook 也支持返回数组    return ["12312312", "abc", "def"]}
// beforeRequest 允许发送数据包前再做一次处理，定义为 func(origin []byt...