---
title: 通过php2shell余威破局的一次真实溯源
url: https://mp.weixin.qq.com/s/yeR6IjVgGXNSz92Negitwg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:51.649530
---

# 通过php2shell余威破局的一次真实溯源

# 通过php2shell余威破局的一次真实溯源

原创

星宇Sec
星宇Sec

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 起因

之前自己的一个站写了一个简单的蜜罐，今天突然想起来，打算上去看看有没有倒霉蛋

然后打开一看，还真有，于是打算从头溯源一遍看看

![蜜罐后台](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQp7ywJ9fiaZpsjOU1JfibNyXw69TicRzfOpsqtd81cZCiaiaZz8um9jdcaV4wkOMN6uRxic8dfb7NsCuPzRB8JicfcwRdJDleibh7MxdjI/640?wx_fmt=webp&from=appmsg)根据日志，第一波就得到了这些目标：

```
27.XX.XXX.X0
27.XX.XXX.XX4
27.XX.XXX.XX6
27.XX.XXX.XX0
27.XX.XXX.XX6
27.XX.XXX.XX3
```

## 初步探测

看后台记录的请求包里面也没什么有用的信息，这些请求的UA还是curl，感觉像是自动脚本+代理

这些目标很容易看出来规律，它们都是一个大段的，于是查了一下ASN

![ASN](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpDOyURCFCBicdG8ouB4FTXic7IoP3Y360iagLJJKCf12RfiakP98LOd9Ako6FCJoreYQnWGlIavblJz1JRfu37ryyy81QxaTTzGTI/640?wx_fmt=webp&from=appmsg)

ASN

可以看到该网段由CNNIC注册，实际承载在Cloudie HK机房，没什么有用的信息

继续查一下反向解析![rdns](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpSlml498NibwS16Puic7ouR5wxiab36QNUHmjibMYqicss1J1uZ1uIbrpkljmbUAbVMv7xCHaeaKmVbPSBLd8FvkqeskCNNibwwBicnI/640?wx_fmt=webp&from=appmsg)非常好，有结果了。这六个IP的PTR记录全部指向`XXXX.XXXX.Xs`，更换权威NS查询的结果也一样

## 进一步深入

这个域名下面有不少子域，不知道什么原因我本地dns对不存在的子域名全部返回198.18.X.X，于是直接搜了一个公共DoH查记录

![DoH](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQoey0GTCetDB8OeMN6UnYgImrIOx8acJiaES8SE4O1c55IIH1cmDFQibLOwAf5x1mArXjVc7R7HtqPbnIk6ONMYPAYBNVbicZePgc/640?wx_fmt=webp&from=appmsg)

DoH

直接访问这个域名，发现是一个叫go-admin管理系统的登录页面。项目看起来像开源的![go-admin](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQraju2Wta40eLzAP2t0yykw1B5JNUA84bQuIsO10PZ5B3iaAtHBgj9qiaCicZcX426w8Fo1DBagicWEBy2QGkKNcAUA6LicfaSgk4S4/640?wx_fmt=webp&from=appmsg)

但是很可惜，findsomething和Wappalyzer都没发现什么有用的东西![findsomething](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQoQyo4Quo1qsd82q7CoSfnQj2suVbyJAAKVGFcEtJ3hDiajjJ5kg6ArRpEYuJDYZbK0icBccK8WENqiaUtjuwbUTOfHMnFxHMt1K4/640?wx_fmt=webp&from=appmsg)

接着直接f12大法，看看页面里面有没有什么特征信息![source code](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQqu44ChiaWLZiaOmul9lOPsINyt4IonD6E88rWibW0icfl8vFnBO2ZHSd1cFwtgmg87WI1Ft5hlibLjeh9eAs7w9PHiaA2N8PgXMLpCU/640?wx_fmt=webp&from=appmsg)看到description我就知道猜对了，肯定是开源项目的。直接丢进谷歌

![google](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQoQsXWibuODW584BibvMK6EDDicEkpsZxiaXVHTU7nnOO70aIkDkxVY4iazFIGv23gw2UnZ0821mlYZAkaaZLlueJyH5CeZ5ofYpsdM/640?wx_fmt=webp&from=appmsg)结果一看好家伙，还是个大项目，破万star了![github](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQq0n6RzMFmYN5yOjE9ZQSOAt8xLArjqGIMAK1ZfFxIUdeA0q8WhvVyOzLohdlo9tHhaicNzwht9RZa2ELpUT95ZRIkFia5tz2D3Y/640?wx_fmt=webp&from=appmsg)

这时候就要请出AI大人发力了，经过一系列操作之后，AI大人也是成功的发现了一个核弹级0day。![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQrC0SBT4CNTZKpjvWeRYicSfmurKcsXDqwiaWGY3b2qGtEKfnTSFHVrznv9ibwjeF3EWDUXZhglDmVSanalLm97CdszCUscju5K0E/640?wx_fmt=webp&from=appmsg)他的jwt默认密钥没改。。。。

然后使用ai大人生成的payload一键注入之后，新的问题又出现了。这个网站的后台死活进不去，页面一直白屏，加载遮罩也关不掉，一直报错。 继续f12大法，看一下network![Newwork](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQrH5NyZYJlsFcC9AS1AL9udUjqwVP753da8e8wCeHdunWh6noGEmqiaZZoiccABn5P1cEaa1icbNCmAE4dtl8CrJovC2iavO7ricicLU/640?wx_fmt=webp&from=appmsg)结果又有了新发现，他的全部baseurl都指向了另一个站XX.XXXX.com

也就是说，XXXX.Xs只是当时的入口别名，XX.XXXX.com才是这套系统实际请求的生产地址

## 转向新目标

对新目标ping了一下，结果他套了cdn，找不到源站ip![itdogs](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQowNnC1pXSygcXbFpO8CtUHibXYE70xB6cNqhOia16fiaQM1SBA6zibMfVJnfLBgpOEh5IRZE3hh2W9RpmKW5KzrJfWpLWTiapj3mvE/640?wx_fmt=webp&from=appmsg)

正当我打算继续研究他的web页面的时候，一个状态接口在错误信息里直接把回源地址带了出来，里面的IP是1XX.XX.XX.X9

源站拿到了之后什么都不问，先来一遍nmap全端口扫描

（忘了截图了，假装这里有nmap扫描结果）

扫描后发现，比较稳定的端口有22、80、888、1234、3306、8080和32454

那还说什么，顺序肯定是8080、1234、32454，都不行的话再说别的

很遗憾8080访问不了，于是转向1234端口。接着，高手来了

1234端口的服务页面没有正常业务内容，只有一句伪造的Windows路径报错![1234error](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQqM7pJnPlA0vQrmh9DwF21oFQYFtRibJHqT3uANk9Wa11S7YgpAaDJAgQ6FdKoHhz9rf45vwsS5bWXSFkTLPa7zweTXiaKLDcmYo/640?wx_fmt=webp&from=appmsg)虽然显示404，但是status code还是200，你好歹装的像点啊....

这是他的真实报错页![404 Page](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQr3EAsyk31lv5ibwoVxrNWPs5pmoMvj5nibA4x44OIcr822sjcbBNvB9TOFKxQS1XQYia9e5YYeZS4icZV2hvLkBMmtHACPiaPbaLJ0/640?wx_fmt=webp&from=appmsg)

接着fuzz了一下路径，发现了一个list.php![yakit fuzz](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQo6Tz21ED2JsnkEs6IiauT8Q18mvMibVOz0Yx2G5s6uPTfZXnod6RicYvBKqQnlUGicvZQVRQ2qlwRdHpXJdrTx0asOs7RqCv45daI/640?wx_fmt=webp&from=appmsg)

访问之后我直接乐了，都扔我脸上了![mysql error](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQoA1nrpCqLuQf4OXpic2piaibMXRw57kDLMZQgBgj7Z7OUax5tSIDxIYf3n7iaAkoiafiaTXjKHCkviakLaeVbu1Kk1c6apwlXETicjTIY/640?wx_fmt=webp&from=appmsg)

一眼就能看出来，缺少的参数叫pass。简单的sql注入测试之后发现没有结果，接着直接上yakit爆破一下pass试试![image](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrIiaCzwFy78uw2JAfHLyMuVH4gia3DRyibyfDYLIDyMg6S3hUuhYqvFXwicJczQnEaXnTMExdEprIcTMzkv4GXWmR5qkZpTUdaL3I/640?wx_fmt=webp&from=appmsg)pass还挺简单，就是个几位纯数字

先GET拼接一下参数试试![image](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpiaBrz56Hxeq3ib8WHnD6ict5ZGeMH9RRyuHMHgfGgKvialNEO6fWXNYtNhkic8UibURR3cu50hd0QBLIg1M2WeTxBiaHupcjHFI4XFY/640?wx_fmt=webp&from=appmsg)结果真给我ls出来了。。。。。

挑了一个顺眼的sfz.php，访问一看，好家伙又是报错，缺一个sfzh参数![mysql error](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQodLpAQt26AMcup24kQvbTlMMtektUFG7Ro9HLZt2zxGfvSp0rWIiblCu6Rn0gr2p30UpTw4Fic5TYHyD7nEImRHqibyg2w5fMeXc/640?wx_fmt=webp&from=appmsg)

后面加单引号，页面直接返回

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''' at line 1
```

出金了，双引号和bool测试都有变化，sql注入基本可以实锤了

简单看了一下，db的账号有FILE权限，并且secure\_file\_priv也没限制目录，结合之前的路径，基本就能直接写shell了

```
-1
UNION SELECT
  0x<PHP代码的十六进制>,
  2,3,4,5,6,7,8,9,10,
  11,12,13,14,15,16,17,18
INTO OUTFILE
  '/XXX/XXXX/XX/1.php'
```

上传成功![shell](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQoJuKxtA9jH6YSicDK1o7aPYXjYtHOiaibjsiaTkgLASUp6DPzL3nUVRaPm6vbgpkRlSVtUWDdzI6iawP7c2wFGQc6IxYMAWOe0iaSX8/640?wx_fmt=webp&from=appmsg)

调用一下看看![connect](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpDvYeZsVHoiaWlOqIoIZLNSZ92AqnmB3jIXA3JlPHDqjB1ZtfmianbgA0bZsHiaFlKoTrSvVHPwunRhnrZEvJicWMWZeUHo8CHD0o/640?wx_fmt=webp&from=appmsg)

www权限

## 提权

既然有shell了，还是www权限，那肯定要继续想办法提权到root

基本信息是

```
uid=1000(www) gid=1000(www) groups=1000(www)
Linux XX 6.8.0-139-generic
Ubuntu 24.04.5 LTS
```

常规提权项看了一圈，www不在docker组里，SUID文件都是Ubuntu自带的正常程序，能力位里没有明显可以直接利用的对象，root的cron目录也没有对www开放写权限

继续执行sudo -n -l时，发现了这个服务器的一个配置问题：www虽然不能执行普通sudo命令，但可以免密执行一个维护脚本

```
User www may run the following commands on XXX:
    (root) NOPASSWD: /usr/local/sbin/web-XXXXXX
```

并且这个维护脚本由root执行，但它会继续从Web目录读取 .maintenance-task并交给/bin/bash

而且Web目录本身又属于www，等于root主动执行了一个普通Web用户可以修改的文件

所以现在只需要把命令写进.maintenance-task，再调用维护脚本就可以

```
printf 'id > /tmp/1\n' > /XXX/XXXX/XX/.maintenance-task

sudo -n /usr/local/sbin/web-XXXX
cat /tmp/1
```

最后读取/tmp/1，直接是uid=0(root) gid=0(root) groups=0(root)

这里就提权成功了

## 深入探索

有root权限了，直接一步到位写入ssh pub key

```
cat > /XXX/XXXX/XX/.maintenance-task <<'EOF'
#!/bin/bash
mkdir -p /root/.ssh
chmod 700 /root/.ssh
touch /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
grep -qxF 'ssh-ed25519 PUBKEY 1@1' /root/.ssh/authorized_keys || \
  printf '%s\n' 'ssh-ed25519 PUBKEY 1@2' >> /root/.ssh/authorized_keys
EOF

sudo -n /usr/local/sbin/web-XXX
```

确定写入成功并且权限配置正确之后，直接ssh连接，探索一下服务器信息。![root](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQq6LCibcorzDv1lzoPw7EticwwUOwMjSy9ENcBz7XWodXuWOKnEPN8lWgMB5moIJN2lWictc3onh4PQzQglUdyIG46UYwZPgwr98c/640?wx_fmt=webp&from=appmsg)

看了一下进程，发现这个服务器还有宝塔面板，这里可以直接参考

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQpSRTvgV6sv0zIT7mf1h4pS7lRqpeicup3iaFnHG0OBxCdRbsg5b8EVV9g2hhJia9icF1NomickxYKOficlicCicEF6qpFPAITtribjic7TU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQqia5gQyCZfLibkypngLbYYCYI9l93aFhlu4Q5eXx3phXwIt8wQtsAsJVHYPzEHX3SSrSYxYhcnIaCydEast1Aap7JX5sQRzNFgo/640?wx_fmt=png&from=appmsg)

（我以为我发过宝塔面板一键登录的文章，然后最后编辑的时候找了半天没找到，最后想起来是之前讲课时候写在ppt里面的）

都有宝塔了肯定不要看丑陋的命令行。直接拿到登陆态然后在f12 console注入![bt panel](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQq6ll46CevWVwTlDETUvGUgicCIGoaDx3eYmg8XQyFY5ENVkWibg7aQiaIGNZBwzP90JKhIQib8HuleQCSAIUFxP5Pl8dfFlzsJvsg/640?wx_fmt=webp&from=appmsg)

成功登陆

## 溯源

这一步其实简单的超出我的想象。翻了一下他服务器的文件，在一个已经被暂停的站点目录里面，看到了早已经失传的照妖镜源码![照妖镜](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQq6vJZGFTeaasj...