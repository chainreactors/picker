---
title: 谈谈 Windows Redis 高版本 RCE 及 重要提示
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247489679&idx=1&sn=7afe9f1fd533070230fd9cf3a2bfaed1&chksm=fad4c598cda34c8ee9471ae8a052325752f4e15de96a19764229b57e366ed176ea55608881b0&scene=58&subscene=0#rd
source: NOVASEC
date: 2024-08-16
fetch_date: 2025-10-06T18:04:34.052526
---

# 谈谈 Windows Redis 高版本 RCE 及 重要提示

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/toroKEibicmZBfibfibmdVX8PEdThc05gHia0TfFJqePXJsEc4hxzarqHjKVvzKzrSCAalqudXAEgDF7aOmUox7KRiaQ/0?wx_fmt=jpeg)

# 谈谈 Windows Redis 高版本 RCE 及 重要提示

原创

酒零

NOVASEC

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDxicuqPkFfjdG2kcyzCXrXfiaOqkg7qkk63ibvpfNVSajOwXV5dg0xhupKGhQ3lugDyy0ehGIazYyEw/640?wx_fmt=png)

***△△△点击上方“蓝字”关注我******们了解更多精彩***

**0x00 简介**

官方的Windows版本Redis-Server还处于3.x版本。

但当前主流的Redis版本已经是redis6+了

Github有些项目开始发布高版本的 Windows Redis

```
redis-windows/redis-windows: Redis 6.0.20 6.2.14 7.0.15 7.2.4 7.4.0 for Windowshttps://github.com/redis-windows/redis-windows
```

因此，高版本Redis逐渐变得常见。并且由于Windows不像Linux那样有很多权限限制，成功获取到Administrator权限几率也是极大的。

本文就实战记录一下高版本Windows Redis的可行RCE方案。

注：一定要关注最后的注意事项!!!

**0x01 高版本REDIS RCE方案**

经过对Redis高版本环境的深度RCE研究，总结为如下几个方法：

```
1 Redis写Webshell2 Redis自定义模块RCE3 Redis延迟加载dll劫持RCE4 Redis写启动项等其他方案
```

**0****x02 Redis写Webshell**

使用Redis的save功能可以保存当前的键值对内容到指定文件中。

如果当前目标对外开放web服务，并且获取到网站路径时，可以尝试写文件到网站目录，从而获取webshell。

写文件方法除了常规的save以外，还有主从复制无损写文件，都是比较好的方案。

唯一难点在于如何猜测网站路径：

一般而言、Windows下常见的服务器是IIS和phpstudy，这两个环境都是存在默认路径的。

可以通过config set dir xxx 命令来遍历猜测当前网站目录。

该功能原来较为简单，可以使用代码实现批量猜测目录或文件。

**0x03 Redis自定义模块RCE**

Redis4及之后版本已经支持自定义模块功能，该方案和Linux下的Redis主从复制RCE原理是完全相同的。

唯一的差异在于：Linux加载so格式插件、Windows加载Dll格式插件。

使用自定义模块RCE要求拥有完善的DLL文件，因此不能够使用save直接保存dll内容，需要使用主从复制等无损复制方案。

如果主从复制不可用时，也可以尝试结合文件上传功能，上传自定义插件然后调用Redis加载。

插件加载小技巧：

1、加载插件的后缀可以为任意后缀、任意路径。

2、自定义DLL RCE也可以用于Bypass Disable等限制执行权限的操作。

**0x04 Redis dll劫持RCE**

Redis低版本可以通过上传NotFound的dbghelp.dll实现劫持dll。

经过几天深入研究学习可劫持DLL，发现在Redis6上也可以通过上传**cryptbase.dl****l**达到相同的劫持DLL效果**（干货）**。

劫持Redis的延迟加载dll的优势是，不需要重启就可以实现完成多次调用。

Redis DLL劫持的一些注意事项：

1、如果上传的不是针对某个dll的代理劫持dll，也是可以调用的，但是在redis重启前一定要上传原版可用的dll文件，这样不会影响Redis的重启。

（重启前dll都是可以覆盖掉的，最好本地测试，看看dll是不是写的正经，不正经的dll说不定会卡死，勤快的话，最好使用代理DLL）

2、分析过程中发现似乎还有其他的一些可劫持dll，但是没有经过验证。

3、和自定义DLL模块加载相同，需要使用无损的上传方案。

4、本种方案看似和上一种DLL模块加载方案有所重叠，实际上确实是有所重叠。

**0x05****Redis写启动项等其他方案**

在Windows Server中，用户启动的Redis的权限一般都是很高的，因此也可以使用其他的RCE方案。

例如：添加启动项任务、劫持公开DLL、劫持用户常用程序bat、lnk、exe、dll程序，等待用户点击或者重启。

提示：覆盖sethc.exe该方案默认只适合RDP能够直接到对方桌面登录框的常见，这种老版本Windows比较常见。已知Server2012+是不支持该方案的。

**0x06 重要注意事项**

思考一个问题：上传dll、上传exe时，如果存在AV或者其他禁止写入的防御错误会出现什么问题？

经过作者的实践测试、如果出现了这种情况，大概会出现如下提示：

**Error in execution; nested exception is io.lettuce.core.RedisCommandExecutionException: MISCONF Redis is configured to save RDB snapshots, but it is cu
rrently not able to persist on disk. Commands that may modify the data set are disabled, because this instance is configured to report errors during writes if RDB snapshotting fails (stop-writes-on-bgsave-error option). Please check the
Redis logs for details about the RDB error.**

并且后续将无法正常链接，只能等重启后重新链接，大概也会影响到生产环境的正常运行。

该问题主要是存在程序强制关闭了Redis快照功能（强制关闭本次Redis保存），然后Redis bgsave的默认错误处理方式就是提示错误并且停止写入。最终导致在每次客户端连接时，都无法正常链接、提示用户持久化失败。

如何解决该问题？

解决方案是修改bgsave-error的默认错误行为，不要在出现错误时停止写入功能。

```
config set stop-writes-on-bgsave-error no
```

重要提示：宕机属于严重生产事故哦!!!!

**0x07 总结**

Windows Redis RCE 方法涉及的知识面较多，除了常规的写文件外，还有钓鱼佬常用的DLL劫持技术。实战时，大概还会遇到DLL免杀、目录猜测等问题。

推荐个综合Redis利用工具：

```
yuyan-sec/RedisEXP: Redis 漏洞利用工具https://github.com/yuyan-sec/RedisEXP
```

已经把本文涉及到的大部分问题、技巧都与**@yuyan-sec**大佬沟通实现，希望大家都能够安全渗透、合法渗透。

渗透不规范，铁窗吃捞饭。

![](https://mmbiz.qpic.cn/mmbiz_gif/icZfUh6Tsbv0xAFjs5qQlsFCCmymOS3Vq8v6OSKDP0pw3aoCD4OTqojr5NMysBOcoMehddw6JUqYXVuurThNLsQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**0x99 免责声明**

在学习本文技术或工具使用前，请您务必审慎阅读、充分理解各条款内容。

1、本团队分享的任何类型技术、工具文章等文章仅面向合法授权的企业安全建设行为与个人学习行为，严禁任何组织或个人使用本团队技术或工具进行非法活动。

2、在使用本文相关工具及技术进行测试时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。如您仅需要测试技术或工具的可行性，建议请自行搭建靶机环境，请勿对非授权目标进行扫描。

3、如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。

4、本团队目前未发起任何对外公开培训项目和其他对外收费项目，严禁任何组织或个人使用本团队名义进行非法盈利。

5、本团队所有分享工具及技术文章，严禁不经过授权的公开分享。

如果发现上述禁止行为，我们将保留追究您法律责任的权利，并由您自身承担由禁止行为造成的任何后果。

END

如您有任何投稿、问题、需求、建议

请NOVASEC公众号后台留言！

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCP3AeicSCQAYIOvxVDSRUxpiadmBKZ8gtggx02BmG1WwCqoM23l72qV8AiabXSRKjGmk8S1HS1nTjXw/640?wx_fmt=png)

或添加 NOVASEC 联系人

![](https://mmbiz.qpic.cn/mmbiz_jpg/toroKEibicmZD7m4f7uBkNfCG8BjypNEukN0Ht6Ha0XsryrmS5PAmaVeyzb3JzsH5ibx6DmpHq9e8agwMkccrwNSQ/640?wx_fmt=jpeg "微信图片_20201214143605.jpg")

感谢您对我们的支持、点赞和关注

加入我们与萌新一起成长吧！

**本团队任何技术及文件仅用于学习分享，请勿用于任何违法活动，感谢大家的支持！！**

预览时标签不可点

个人观点，仅供参考

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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