---
title: 文件上传操作漏洞场景挖掘思路
url: https://mp.weixin.qq.com/s/AgRxUV_Q_BpxXMN50uJS3A
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:32:45.115054
---

# 文件上传操作漏洞场景挖掘思路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboTSNaK5kOKZVWsgTYfGt4NBMEZyiaGBAnYwFOPiaBUK7Rh0YiaBichbXcOPQh00OL49dicfGFx6gPMrLoaq63DPtHevnvficw4mqSe5I/0?wx_fmt=jpeg)

# 文件上传操作漏洞场景挖掘思路

xiaoY
xiaoY

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:xiaoY原文链接:https://xz.aliyun.com/news/18107
```

## 下载读取

### 文件可疑ID遍历/注入

下载接口出现铭感信息的(自己独有的东西)有用户的汇集的地方就很可能存在漏洞

* 出现数字ID遍历,越权下载其他人文件,GET``POST皆切换尝试,利用IDOR越权,但是有鉴权字段就无效了

```
userId=19230239023923232 NickName =232193299321324343orderid=1989885454549549
```

* 注入思考是\*\*+1 -1\*\*,观察数值有没有被带入执行,可以是选择性数字的导入/下载数字是否带入数据库查询

导出Excle功能点,输入1的时候，表示导出第一列数据，此处包长为6360

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS0uZnvD1icdtU9e4SyvMaYA78h5Kq4pG0encjUKRcM6q0O8xZbZYTQGOsJYZjZwJDia4ldDjrK2Tn5nokjc3hnqCIg1iaTHldibIE/640?wx_fmt=png&from=appmsg)

在我输入2的时候表示导出前2列数据，此时包长为6364

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTeN1KXGy4d00XbYFsjRv3801LX2YgtHbceWkJjNU5aaqicltazp3VhSj7kgYvCmQ58yB5h7NgUZ1h4nS99lwLjrFDtStZFTk04/640?wx_fmt=png&from=appmsg)

当我输入xxx?id=2-1时，此时导出的是开始第一列1列数据，包长为6360了，这就很明显的用户可以操控拼接进SQL语句进行正则运算,所以遇到文件id 测试遍历及注入有时候也会有意想不到的惊喜

```
假设原本的 SQL 查询语句为：SELECT column_name FROM table_name WHERE id = '用户输入的id';
```

探测到注入无过滤情况就可以构造恒真条件永远为真，导致查询返回所有记录，从而绕过了原本的查询条件，获取了所有列的数据,假设存在过滤条件就慢慢探测了，只能靠个人思路绕过

```
如果用户输入的 id 是 1' OR '1'='1，那么拼接后的 SQL 查询语句会变成：SELECT column_name FROM table_name WHERE id = '1' OR '1'='1'';
```

### file参数下载接口任意读取

读取文件功能点接口,按照读取的文件id返回对应的文件,字段file=xxxx,同上文不同的是虽然功能也是为文件相关,但相关字段并不是idfileidinode这种明确表示依靠文件id输出文件的,而是file表示文件相关字段,此类场景不仅仅可以测试注入、越权、遍历、还可以测试任意文件读取,类似的参数还有filesname file files, 不外乎功能点,只能接口字段出现此类就可以测试,只是这种漏洞出现在操作文件读取下载场景较多,下面会介绍到利用伪协议读取场景

```
file=189839434343 //可以尝试读取file=../../ect/passwd
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTyZvdye1GKRORXhwzRf6uLkBsogUF3ibLJPTbkWnCTlnuHW4hhjU1rGgk3wyFNiaxFsxeMmP7jkD7v3L59nJ4iafPXa71UQjeVEk/640?wx_fmt=png&from=appmsg)

列如apis/xxxxxxx/download?filePath=接口，于是便可以尝试任意文件读取，成功下载etc/passwd

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSiadlnlVDecS7RJrdXTWGXLfibj47IhuzudKeTjpXLCrQgfDqlpL8K4Zx5ndZYb014zLibyzicCEQIFv2b2vgMXoJTvLVcjkq5v7k/640?wx_fmt=png&from=appmsg)

整理好通用字典,形成自己的测试规范,遇到好的绕过Payload做好记录,

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQatJutRKvlGpxvicKwHiakQdrSsb96DiakUK9rnaWeN5D5XNRcPfE64J9KJicszDT1vOuDcP1EzcIbpCr6PMLMTZXAaG1w5FScF9k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQkAg6hUXdmGsHgAU4B5KpgnaG92Mwr92ogEnI6WlrdPzW7ac1ADjn8SA1oQticSF0pTHgvUTFOgk3G3aHlcQBic450oaib6eib73g/640?wx_fmt=png&from=appmsg)

### 图片链接http://file/1.png

图片的链接形式是http://file//xxxxx.png可以测试成file//etc/passwd或者只保留http://file对路径无处理可能会列出该目录下所有的文件

```
http://file//a0b24dbc24f3d24530999e10e11a88c7242338c0a849d91aa0ee47369cd2b6147f.pnghttp://file// etc/passwd http://file//
```

### type类型任意文件读取

接口中出现type类型参数时,尝试读取文件,最不起眼的参数也可能隐藏着重大的安全风险,设计要文件相关的参数都需要铭感起来filename

```
GET /api/saber?type=xxxxx GET /api/saber?type=../../../../../../etc/passwd
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRtznYiaiaKicibSX0ibMyn6mFWkO6QuPjUuFLrYeib3seYbdhvoZsMaD072zzicw7zVRHfYyaP8gOyuibbrKoJlb08uUo1E3kH4SRFqUc/640?wx_fmt=png&from=appmsg)

### 400状态码任意读取

推特国外大牛挖掘遇到的情况,在路径上进行路径遍历,本以为参数带入才可以路径遍历,有时候骚的思路路径就是参数,响应包为400试试看路径遍历

```
payload:  ///////./././././etc/passwd
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS5eDUsR2z9HsoutZfzfcrphj5iaFbMBQNAniaKbg292BpvkepVftIxJNueicH2ulVia0OfKicGxR0SkibyCyupu8ibrzo1dKVlbDh5G0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSPsYDYKyHoDpG6O92xWpeOdEfNZmAaZI7YxVqzjkzwgHZ1KmGJTfxL2mHjA4icnPGreQLt5lxvZxbgLmc96cX7wAZNRo9KyWgA/640?wx_fmt=png&from=appmsg)

### 文件包含任意文件读取区别

文件包含会包含文件然后输出,任意文件读取只能读取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQN2qmzjYTdd8FMib0kgQ3Zu61GYiabrbIQIUusQQkZSFrDYQh1sCTErYlia0jNYv5X9Ribqjyia2iclwlZ4mibY6hLicPOYibg10TWicImE/640?wx_fmt=png&from=appmsg)

文件包含和任意文件读取都支持伪协议还有远程地址,但是文件包含一般会有漏洞文件的前缀

```
http://baidu.com/ saber.php ?name=../../../../Windows./system.ini saber.php<?php  $file=$_GET['name'];  include($file);?>
```

根据功能点分析这个地方会是SSRF还是任意文件读取,请求网络功能如下必须测试DNSlog

```
http://baidu.com/saber?file=htttp:sxxxxx
```

无响应办法就测试任意文件读取file协议,能读文件了就可以读其他记录IP的铭感文件,需要注意权限的问题，权限决定我们能**读取/下载文件**范围,尝试读取root/.bash\_history看自己是否有root权限,此文件只能是root用户读取它包含了root用户操作命令的记录如果没有,只能按部就班的利用../来逐层跳转读取

```
# etc/passwd记录了系统所有用户信息http://baidu.com/saber?file=file://etc/passwd  # /etc/shadow 是用于存储用户账户密码等安全相关信息的文件 只有root用户才能读
```

不带协议文件包含

理解http://xxxx/saber?name=etc/passwd与http://xxxxx/saber?name=file://etc/passwd之间的差异

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRpqibH81AcIE5bUu6ypudg9WdbSNSQGtPz0hDFh1Xd9jxMvzPaLib5OJVibJhyOyrsMBCd3wzribPlfwRDNGibbBUk1ENf2EdRpXp0/640?wx_fmt=png&from=appmsg)

### 任意文件读取攻防利用思路

参考文章

* [https://mp.weixin.qq.com/s/7prdLc9ml6q2chrRxdsdEQ](https://mp.weixin.qq.com/s?__biz=Mzk0NjE0NDc5OQ==&mid=2247518434&idx=1&sn=0a28059b83aa0a7318ccf997426a4f24&scene=21#wechat_redirect)
* [https://mp.weixin.qq.com/s/PdFm\_Y3FNDkCMrsHXcm\_2w](https://mp.weixin.qq.com/s?__biz=MjM5Mzc4MzUzMQ==&mid=2650260890&idx=1&sn=f46073f31278972785b097461b3b66bb&scene=21#wechat_redirect)
* [https://mp.weixin.qq.com/s/Zkw68UPDWcHBn6cayVdITg](https://mp.weixin.qq.com/s?__biz=MzkwODc1NTgyMg==&mid=2247484148&idx=1&sn=e4a9e276702006c6bc2408be1fddb72e&scene=21#wechat_redirect)

拿到任意读取漏洞思路先读取管理员root用户.bash\_history命令记录 ,看自己是否有root权限,此文件只能是root用户读取它包含了root用户操作命令的记录，读取此用户的登录私钥包括历史记录记录，如果用户配置了可以通过密钥登录，那么读取私匙到本地 也可以完成 登录,私匙验证的东西远程下载下来,然后可以直接拿私匙到自己电脑上去远程登录对方ssh

```
/root/.bash_history # 读取root用户历史命令可能会出现ssh私钥存储位置或其他铭感文件路径/proc/self/status   # 当前用户运行进程状态
```

无法读取管理员.bash\_history,尝试读取/proc/self/status进程的uid和gid判断 当前用户权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQXHuzFEkJkcFHRZogUhHvol3nIoqdk1L7sez0yeeNfuNDhCmHOh6JpBQR3CX8Mf3sc5kTB1aicd6nXaPdMCjWBeoUQA3KKAkwY/640?wx_fmt=png&from=appmsg)

后读取/etc/password的内容对比进程知道自己是什么用户,此文本会显示系统所有的用户,搜索home /bin/zsh就是实际存在且可以登录系统的用户以及root用户

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSrcJGE5az8sz3pBA4emSzmsUXbyC3tic9ZBFD6Sc9pRrvVcxeumic4tk7aQF0QnQ6fwqnPiciasnWUhQeHiaafsZX1SuKslKc9DCeU/640?wx_fmt=png&from=appmsg)

攻防中首先尝试身份去读取/root/.bash\_history,获取管理员的历史命令记录,如果读取不了代表当前并没有root权限,则寻找其他可登录的用户,以它的身份去读取文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRouYv4nUqrSXVhzucXtgmN2LA9q1NrqodYWhErprREbu14MOef1CZCwPiaojX1dWGicQ5IIqkTLDtiaHTDYoFfQj6TNibibe6H5HbY/640?wx_fmt=png&from=appmsg)

```
/home/saber/.zsh_history  # 读取saber用户历史命令可能会出现ssh私钥存储位置/hoem/saber/.ssh/id_rsa  # 尝试读取普通用户默认私钥  /root/saber/.ssh/id_rsa root用户默认地址/root/.ssh/id_rsa   # root 默认地址
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR5swfKLGKfyOShGxCrnGsxRDzchAnzfTDrrAZycIvEaHicr1ibEufWrT7eTwov8gmM0BBpMZR36uiaUB1NUxiapn6tFlWBb9Nuiarc/640?wx_fmt=png&from=appmsg)

file读取机器文件获得内网IP

Linux系统

```
/etc/hosts                包含了主机名与 IP 地址的映射关系，可能会记录内网 IP 信息/etc/network/interfaces   存储网络接口的配置信息，其中可能包含内网 IP 地址/proc/net/fib_trie        包含了路由表信息，从中可以获取到内网 IP 地址~/.ssh/id_rsa             Linux系统中用户的SSH 私钥默认位置
```

Windows系统

```
类似于 Linux 系统的/etc/hosts文件，存储了主机名与 IP 地址的映射关系C:\Windows\System32\drivers\etc\hosts：
```

常见中间件日志路径

```
/var/log/apache2/access.log/var/log/apache/access.log/var/log/apache2/error.log/var/log/apache/error.log/usr/local/apache/log/error_log/usr/local/apache2/log/error_log/var/log/nginx/access.log/var/log/nginx/error.log/var/log/httpd/error_log
```

dicr协议探测内网端口读取到IP就可以这样这样爆破操作

如果读取到IP端口并且未授权就连接Redisdict这个协议也可以操作Redis执命令

```
dict://127/0.0.1:6379/info/  # SSR伪造协议读取redis信息cat /etc/hosts          #读取网络信息
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS44ciabX7wEbbufTrrWxzXYQyI6BBjfCqgIxE3QsV8TCTDUic0qp8NP3v5AUNZyoyVa2sZhatvwvmENRF22rHFWoiaO6MRFvibhFc/640?wx_fmt=png&from=appmsg)

读取或包含Redis密码记录网站存在文件包含可以 读取redis配置文件信息,或者是其他的Spring boot heapdump等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQSTryIkzqkw9ediageSibonoJ0BV4UAJBv8yc4aAib6Aico8K6v1TwGvfPBcK3qdMZFJQV8J33da4M5NXj3hYyLiaiaBgXsclGJQrL8/640?wx_fmt=png&from=appmsg)

![]...