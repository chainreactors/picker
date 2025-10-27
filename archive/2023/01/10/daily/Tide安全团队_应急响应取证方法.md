---
title: 应急响应取证方法
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247506123&idx=1&sn=8426c7cb82387c3ba40a7463adc28182&chksm=ce5dfaaaf92a73bcde96a47c026f1d2d04ad287bbe1a216b2341ededc9b42fa76b4e5667e502&scene=58&subscene=0#rd
source: Tide安全团队
date: 2023-01-10
fetch_date: 2025-10-04T03:25:54.122358
---

# 应急响应取证方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7e9sw4WZVwf2QXxCXRFTCTCyFYUHFOuXnX4dSAJAI6RNnUUHrNbCXTQ/0?wx_fmt=jpeg)

# 应急响应取证方法

原创

菜鸟的菜

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVhN8RQR8c6zEaACxatlch2rgdzYzYAiahr1GUq1cLMMGVnvKpF8biaWA/640?wx_fmt=png)

# 1、简述

在用户遭受到攻击时，除了进行快速响应，可能还会进行取证，主要是对内存、硬盘、入侵流量、浏览器历史等方面内容进行取证。针对vmware虚拟环境，取证相对比较简单，直接拷贝相关目录下虚拟机目录即可，本文主要是对非虚拟环境系统进行取证，分别介绍常见的linux、windows系统的取证方法。

# 2、windows系统

## 2.1 内存取证

针对虚拟机获取内存，暂停vm并取出.vmem文件即可，很多木在马程序都有较高的隐秘性，可能会修改系统调用的返回值，但是在内存中的数据是真实存在的，所以在应急的时候如果无法从系统中找到痕迹，可看看内存中是否有相关字段，尤其是针对一些仅存于内存中，关机就消失的情况，内存取证是最好的办法。针对内存取证主要介绍两种工具，dumplt 、volatility两种工具。

### 2.1.1 DumpIt提取内存信息

取证过程：工具下载地址：

```
https://www.toolwar.com/search?q=dumpit
```

该软件大小只有200k，使用也比较简单，直接运行就会将内存存储到raw文件中

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7oibiaB1ibNVJicCHSEMw96ZBITbZx3hQx67lFVKTDKoCpia0IbqKdPQD1dQ/640?wx_fmt=png "null")

运行完成后在当前目录下生成内存存储文件

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7wcwpDMIDFbcKp6RhqyvnI3oOWoA6gtBcKZn7KCXe0A0y4gYkOclyyQ/640?wx_fmt=png "null")

内存分析过程：redline: 取证结束接下来就是进行内存分析，内存分析采用redline工具 工具下载地址：

```
https://fireeye.market/apps/211364
```

下载之后进行安装即可，安装完成后界面如下，双击已经获取内存镜像，加载之前保存的镜像即可(在进行内存备份时，由于系统使用情况的不同，所以最终备份的大小也不同，有的可能几十个g,所以在备份时建议使用大的硬盘或盘）)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT79kjcB5ncsdPyI4GyJ5tib9tUibTHibDe8lBs7nhA2lk4MMRZYzsBKjnOQ/640?wx_fmt=png)

加载完raw文件下一步后可编辑script脚本，主要修改内容如下，勾选strings选框

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7VZ114Aic79DU0wwkC6Hrj9OpmUOpjHL96O6mwzViciavvS3BMDeYrcYwQ/640?wx_fmt=png)

加载的后的页面如下，由于我保存后的内存大小大约为5G，所以过程可能会慢一些

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7ZmUBc5fC8mMZY9CmCY34OibVDodRLnibwkT3gsmPjO7mZumOzibgs2gZA/640?wx_fmt=png)

在打开该软件进行分析时就一直卡在这里，所以还是建议利用Volatility进行分析。Volatility: 该软件功能还是很强大的，是用python编写，下载地址：

```
https://github.com/volatilityfoundation/volatility
```

上述地址为volatility2.6的版本，所以首先需要python2.7的环境，具体安装过程可参考网上资料：

```
https://www.bnessy.com/archives/%E7%94%B5%E5%AD%90%E6%95%B0%E6%8D%AE%E5%8F%96%E8%AF%81-volatility
```

介绍几个常用的功能：

```
vol.py -h
```

查看一些常用的的用法

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7loON4IBiao3j6fwy9GUKaSEK6tL2CiapyjHricS3bSUeD4zrlDvIkstFA/640?wx_fmt=png)

`vol.py -f win.raw imageinfo 查看备份镜像相关信息`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7JHvI4VzOcIqiaz1m7PpGaMUaicbZGW0V80rYZt1eLxAL9S108eWX0vfw/640?wx_fmt=png)

`vol.py -f win.raw --profile=Win7SP1x64 pslist 查看内存中运行的进程信息`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7NGyRGMeaMSwzVMveAoIsLfAVt2ibFXxE0fjiaycHpU9oGVmOFAvUqYTg/640?wx_fmt=png)

查看注册表中的用户信息：

```
vol.py -f win.raw --profile=Win7SP1x64 printkey -K "SAM\Domains\Account\Users\Names"
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7RgO03GhsAK2S56WGgrg6hMvAjL1J1OvXJSuV5LGq6TfuHN8dAdEDSw/640?wx_fmt=png)

获取系统最后登录的账号

```
vol.py -f win.raw --profile=Win7SP1x64  printkey -K "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7d2JsU3bl2QzhicGB0DjAhh691RTdFSggskl87icv5ibZLGxU32M3qdBDA/640?wx_fmt=png)

获取当前用户正在运行的程序

```
vol.py -f win.raw --profile=Win7SP1x64  userassist
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7lBbQibCT8WVCkRIokYp02Nv5UJx0EDcg4b8eiclO5YDJ02J9JqWQwWpg/640?wx_fmt=png)

显示cmd历史命令

```
vol.py -f win.raw --profile=Win7SP1x64  cmdscan
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT72l5Drt8mwx8OxlbvhXZLhuficS1xMwYI3sKXJpVtOasB5iapbA0yPuLA/640?wx_fmt=png)

查看网络连接，已经侦听、建立、关闭的连接

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7nv7TibsU7eCDVlicdoXCeZYxIReP7uS6Yiazb0AeKibU5GWzJOQD1oHuvw/640?wx_fmt=png)

查看ie浏览记录

```
vol.py -f win.raw --profile=Win7SP1x64  iehistory
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7OH79B2rXwE82I4fCwoPgicWoVic4QdXicN9riaZMJvKty3wevlWbEib3pJg/640?wx_fmt=png)

时间线：

```
vol.py -f win.raw --profile=Win7SP1x64  timeliner
```

从多个位置收集大量活动信息

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7JBw30SE0WPp28ufRFSMRtIxic6lPwHNBkYialQdSO3eAqnyduicZ350KA/640?wx_fmt=png)

查看密码：

```
vol.py -f win.raw --profile=Win7SP1x64    hashdump
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7BkApCgd6wtP0akibLibxlAsYp93L0jAYEvpMFzQic7hPC6bbx7BpB5s3g/640?wx_fmt=png "null")

hash破解网站：

```
https://crackstation.net/
```

内存文件搜索，由于搜索的文件会比较多，可用grep进行过滤，很多时候可能需要分析的数据很多可利用 > aa.txt,这样就可以将文件保存下来，封方便去查看。

```
vol.py -f win.raw --profile=Win7SP1x64    filesacn | grep nessus
```

文件转储：

```
vol.py -f win.raw --profile=Win7SP1x64    dumpfiles -Q 0x00000000523afd80 -D ./
```

进程转存，将看到的可疑进程存储下来

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7cQJCyrt4gDdGqlOBkMx3nPEE6hdkicjWAr93W8EdkDFgZqC4YMX06zw/640?wx_fmt=png "null")

看了很多资料Volatility在ctf中取证题目中这个工具用到的比较多，在应急场景中也是可以用到的，方便进行后续的分析以及证据留存，还有很多其他的命令具体可参考网上前辈整理的一些资料：

```
https://m0re.top/posts/c6e31ef3/
```

## 2.2 硬盘取证

想来想去，其实硬盘取证就是将硬盘打包成一个镜像，网上类似的工具很多，可使用windows自带的dism命令，还可以采用备份软件，如傲梅备份软件进行数据备份，具体操作过程比较简单，但是在备份时需要准备个大空间的硬盘

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7HUNVmnG2dWE6Dy3n4YLX3ic3memHMzu9oEE9hgpdacSrue7Kr7hPKkQ/640?wx_fmt=png)

# 3、linux系统

## 3.1 内存取证

linux内存取证利用LiME 工具，下载地址：

```
https://github.com/504ensicsLabs/LiME
```

使用方法：在编译的时候可能会报错，但是不影响使用

```
cd src
make
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7TD2Ke8RAPe0WYEuib16unADMvOQap1jzJyMUia6bb88rKOQdNXO6wdCQ/640?wx_fmt=png)

make结束后会生成lime-5.4.0-26-generic.ko内核模块 加载生成的内核模块来获取系统内存，insmod 命令会帮助加载内核模块；模块一旦被加载，会在你的系统上读取主内存（RAM）并且将内存的内容转储到命令行所提供的 path 目录下的文件中。另一个重要的参数是 format；保持 lime 的格式，如下所示。在插入内核模块之后，使用 lsmod 命令验证它是否真的被加载。

```
insmod ./lime-4.18.0-240.el8.x86_64.ko "path=../RHEL8.3_64bit.mem format=lime"
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT70qwzcpibsKEZndqfvibKZXU7xpAZ1ZXkgQMjRRLOFX3PAIUiauSoSZtBA/640?wx_fmt=png "null")

在LiME目录下生成.mem文件

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7Sebp0YDJ6hOIgZyKVA9ysEXDdaHibjJplEqyia7fWlR2wSbIoD8Tz2eA/640?wx_fmt=png "null")

查看文件信息

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7M4UjeNgjDEiajmsxvOSOia0OyLYwrz1Ubc9OT3p13myVgMS1bm4yYyFg/640?wx_fmt=png "null")

这样就将内存文件dump下来了，然后在利用Volatility工具进行分析。

## 3.2 硬盘取证

linux有自己的dd命令，在取证之前需要准备新的磁盘空间 复制磁盘：将/dev/sda完整的复制，dd命令时需要包含if=表示源磁盘，和of=表示目标磁盘

```
dd if=/dev/sda1  of=/dev/sdb
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RV1mpl9uCGlJ1mqpjzJQeT7dgRHm2FgDqRXL89Y5HqwI4JFEEpem6Qzb45oT9QN6DqlFtuw5lyoyQ/640?wx_fmt=png "null")

我在本地进行测试时提示空间不够，所以需要准备足够大的硬盘空间 磁盘镜像：

```
 dd if=/dev/sda of=/home/sdadisk.img
```

还原镜像：

```
dd if=sdadisk.img of=/dev/sdb
```

还可以采用异地备份的方式：通过ssh连接进行备份，如将服务器x.x.x.x的sda文件复制到本地

```
 ssh username@x.x.x.x "dd if=/dev/sda | gzip -1 -" | dd of=backup.gz
```

这里只是列举了dd的部分用法，更多的用法可参考前辈总结：

```
 https://cloud.tencent.com/developer/article/1720348?from=15425
```

取证方法还是有很多的，这次只是列举了几个操作相对比较简单的方法，方便在工作中使用，在进行取证之前建议准备个大空间的硬盘，不管是内存镜像还是硬盘镜像往往都是需要很大的磁盘空间。

往期推荐

[敏感信息泄露](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247500219&idx=1&sn=8da48a9a049bab2f9215ad373868a1a5&chksm=ce5de3daf92a6acc7c2a58329c913062e9c34a9615ce742b761b2775916781abb50159a7d2d7&scene=21#wechat_redirect)

[潮影在线免杀平台上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499902&idx=1&sn=59cba8d980b4ecb0deefff99edaabd4d&chksm=ce5de21ff92a6b09a8972a0144557b0099e443aa8e018b17151c816fc7f08f3615ecb22617fc&scene=21#wechat_redirect)

[自动化渗透测试工具开发实践](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498466&idx=1&sn=085c15679436dedb06a179ca8d47951a&chksm=ce5dd883f92a5195ef74ac517741f6d3da0da40b5501d72016e52cb70344904bb85b8aef65ba&scene=21#wechat_redirect)

[【红蓝对抗】利用CS进行内网横向](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid...