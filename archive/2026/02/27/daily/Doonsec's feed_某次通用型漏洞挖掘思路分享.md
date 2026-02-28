---
title: 某次通用型漏洞挖掘思路分享
url: https://mp.weixin.qq.com/s/wyK_4e_7dc1WN00tgS87LQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:53:21.907798
---

# 某次通用型漏洞挖掘思路分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTrutTbKgjA1Iy8muXVleTQuaTtYqnhJVmTzraP6gAicYCiaeCcH1vibZznZ5v1jua8XLTgq1dHuyHk43Yz05fJr6IURKVQx8kU0U/0?wx_fmt=jpeg)

# 某次通用型漏洞挖掘思路分享

ajie
ajie

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:ajie原文链接:https://xz.aliyun.com/news/9987
```

## 0x01 前言

大概是在上半年提交了某个CMS的命令执行漏洞，现在过了那么久，也想通过这次挖掘通用型漏洞，整理一下挖掘思路，分享给大家

## 0x02 挖掘前期

### 一、CMS选择

如果你是第一次挖白盒漏洞，那么建议你像我一样，先找一些简单的来挖掘。
具体源码下载地址可以参考：
https://github.com/search?q=cms
https://search.gitee.com/?skin=rec&type=repository&q=cms
https://down.chinaz.com/
https://www.a5xiazai.com/

......
百度找找，肯定不止这些

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTDpW5ibJRGJiaEDcviaSn7D1I01q5VnKgkrib6HkGwvgkr7Y6h3MGd4ibNNObR5WtzibVLf3pibrjfC9LkHia3hNTEV9XJff36ntdw154/640?wx_fmt=png&from=appmsg)

那么应该怎么选择呢（这里我是站在第一次挖掘，或者仅使用过扫描工具扫描的师傅的角度这样说的，如果做过开发，代码功底很强等情况，emm...当我没说。）：

```
1、找最新版的版本较低的，例如1.1、1.22、找github star不多的3、找源码总容量小的4、尽量不要找使用tp、yii、laravel等框架型CMS
```

这里说一下理由：
1、如果cms版本高，说明开发有经常维护，同时也说明里面的简单漏洞已经被发现并且被提交并整改了。（具体这个可以看看CMS官网放出的更新日志）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQNDZQbicBsVYFrHdIicdN62rdH2yq2AJW5Hm3CoGyjCCFxStwfOllZqJgLv1RUzWKggzGuTCicUxo1JtMTB1bN0p0QWphjavhqB4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSpMYmeF4iapszKZNQPVCIoSrQqK3cvDE6l7usykYvtmpBovUCKDKibYNAtaC5KsePLsfQNN3J8xwKNdKXhWdHJVIFHibuhFwiaBF4/640?wx_fmt=png&from=appmsg)

2、为什么找github star不多的cms？很简单，使用的人不多，没人标星，功能也比较少。
3、源码少容易看啊，而且想着源代码就那么点，看着也不会太心累。
4、这是我个人的理解哈，因为就像很多人说的，第一个审的可以看看bluecms。为什么？因为简单啊，tp框架首先各种C方法，I方法的，就够头疼了。

```
扯了那么多,总结一句话:跟挖SRC一样，如果你一开始就瞄着阿里SRC、百度SRC等来挖掘，一直挖不到洞，是不是心态崩了呢；如果你一开始借助nday的poc，结合fofa搜集资产，一下子就能挖到简单、小型企业的漏洞，虽然可能漏洞奖金不多、但是满满的成就感有没有～代码审计也是一样的，一开始就找框架型的，MVC架构的CMS，不仅可能看不懂代码，还可能连路由都弄不懂呢。所以一开始还是找些简单的练练手比较好～
```

### 二、环境准备

### 1、PHPstudy

PHP、中间件、数据库，一个软件搞定，反正我是觉得用着很香。
下载地址：

https://www.xp.cn/

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS0dBRRwibKmTsicyZofnnHn2FD5zdBapynjicxFxgibS9oiaPAKwqB5GicqricT1aMfaicl1ROw2MrEQGzKxpYprBmPIUEv97J485xzwY/640?wx_fmt=png&from=appmsg)

### 2、代码扫描工具

目前的话我用的比较多的是seay和fortify。这里其实都一样，不是所有漏洞都是要通读代码来发现的，有的时候借助工具可以快很多。

https://github.com/f1tz/cnseay

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTu5L8cMdAQbG6CygmxKQAic2oZWhF6c4mzKibXnxjY8npNGu9fThvy6cU0eBBFTbv7ibGANhxth8mLbh7tzV6NB7tSicesOd3QtfA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRicxHDvCgFEqbwMbYh10VFXGZ1POyj7OuhPhklKhDldFRu4prm2Rfou9kGQkmzqN4Kx36L8YEcIyQ1BqcBoy5SpgC2YrQX4RNk/640?wx_fmt=png&from=appmsg)

### 3、BurpSuite

渗透测试神器级别的工具，这里不多介绍了，毕竟挖漏洞不抓包怎么行呢。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQAncWiamqluxVvZicNXxjZtnKN7lPKDT7cSnc2wlxLbKMcwED4ibzlJR2tU1J10AN4vDTjc0wJTtU1iaaJNWicianxqRK6MeDicYwJRg/640?wx_fmt=png&from=appmsg)

### 4、漏洞扫描工具

虽然我们拿到了源码，但是挖漏洞也不一定要从代码上进行呀，可以结合黑盒的方式，黑白盒一起，更容易挖到漏洞，也就是业内说的灰盒测试。

扫描工具这里推荐Xray+burp联动进行。随便抓几个包，有没有漏洞一目了然，让我们可以在测试漏洞的时候，还同时进行扫描。
下载地址：

https://github.com/chaitin/xray/releases

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSsXhX062LlL8dA4gZ52kn4ILZciahwzYd7YXibdfcTmHgib2Pqo2VaL0JjuUqB2iawibicVCdfsO9Jw3R0om5dJaJeuzicr2kLpdPHGE/640?wx_fmt=png&from=appmsg)

### 5、编辑器

编辑器的作用是方便查看代码，在有需要的时候才用，这里可以算是我水字数吧，我个人比较喜欢nopad++，当然别的也是可以的，phpstorm最好，可以快捷进行函数跳转。

### 三、搭建环境

1、首先下载源码，解压并放到phpstudy安装目录下的WWW文件夹中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRlgfggw6NMtWdafg48TF3K3pia5Q6jRaG9RSN7pSd9CabcB68jpuFVw4YNXf2PoMu2AmCJSryxm7OWWElwrGTK25TtcunPfMCw/640?wx_fmt=png&from=appmsg)

2、安装方法一般是请求

http://127.0.0.1/install/就可以了，按照提示输入信息。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ8riaF5RkG6oia0MeOPr9amuMuShn928Q0KVecmUofzic8vplIH21EtYBjG6sBB48xBpJv3bm0fjO23sA8rElibXIuPcpicaYIJmDM/640?wx_fmt=png&from=appmsg)

3、提示安装成功即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRrZGYHBsnMcBP7NRosTnGKrB4NFVHzRptJHVRB0KDiahWttDmeIqpQpgUCPgGYyPichUUhWuMx9SJTrGK3bYqfxYWOpPnqs3jm4/640?wx_fmt=png&from=appmsg)

## 0x03 挖掘中期

### 一、代码扫描

借助seay自带的自动审计功能进行代码扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQicicjjI7EEf3UFLYkogNDzVh6iaIyQrefzrGiaQpdAQPiagGI8icXR1KWtREwR8icy3gXyjPYCnthgI7iaI3iaQHNibRibRWC1PMvgyju68/640?wx_fmt=png&from=appmsg)

### 二、黑白盒配合发现漏洞

```
这个其实是很有搞头的，这里没有详细说是因为当时确实重心在白盒上，实际上我感觉这个发现漏洞再去找对应的代码，会更加有趣些
```

1、浏览器设置代理，指向burp：127.0.0.1:8080

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSVkJ9me2kaMKsrOU0dEwYWPXB0VrvZCic7lM4nHrQDCn3dJ1ZR01f8gSUiaFWsrZQiafLNIsLpyJVMbriaP5vLzQ3UHDMWY2jZ3QQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSC9hQ27JVkDbQktAjFRlk4X8qsZv9e3oRTicuc2tF52j3oK3d4NEjwdj0nKllWlg0GB4D9nXw7rYUQlLSLdGEV4jVny07sLDo4/640?wx_fmt=png&from=appmsg)

2、burp设置代理，指向xray：127.0.0.1:7777

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTEibrevhMCU6QUtNIBRWXZJOEfEQdCdgftZXeMk2SoK9qyvZBeU23TmfNtVylwpeAeIOXN1HqzsTYgPKJsggHMhASsfIVW37ms/640?wx_fmt=png&from=appmsg)

3、开启xray被动扫描，命令：

```
./xray_darwin_amd64 webscan --listen 127.0.0.1:7777 --html-output test.html
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTqok0GyiacDaQC1ichN9JxpDthPSrv6w7gFuiajVNftReMVOuBwyy5EkGcsMOBdkOZuEFiajy98rO3uJu4MicSqnIjEAQ18wW7yhaA/640?wx_fmt=png&from=appmsg)

4、在每个功能点都点一点，就跟正常测黑盒即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ8umCuUKL6vk7eSxdRbqmN2BSCZrNKsUk8Y79gyHSf2sHWOaEdvYjwVuV7eWSy8Dlav14V0lRBicMIQ3QF8m03D97U7Twb67Zg/640?wx_fmt=png&from=appmsg)

5、查看xray扫描结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQoYLm8CDmHdposXAq9gGlKGntxpCyXyUdpiaUNSq2z4xovdHhTtmZWlA4AFeGryjTVE9SjfaaTYGapMbu4NhoqlWj9YIVIKJYE/640?wx_fmt=png&from=appmsg)

6、查看代码扫描结果

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTHuedjZzVyNpPReYQXVM497G2ula7ibyWRW4FbbKeSnQuGcZHIkokFo90Bf01Rwq8vvuzqFYgcll6VhMQABowwZickicu6ibgAVtg/640?wx_fmt=png&from=appmsg)

### 三、分析扫描结果

1、将结果一个个点击查看，分析漏洞是否真实存在
因为工具是按照正则匹配来进行扫描的，总会出现一些可能存在，但是实际不存在的情况，例如这个：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTvI0qefdZaYcqIlQiaIuMA2Qibic0dgvNo5C1gBh6CN91RzhviaNQxtiaxiblS7f1SYabMiatlU8WpfnNAl3gVWQmxbN3MceeUXHVBLI/640?wx_fmt=png&from=appmsg)

因为$\_G['SYSTEM']['PATH']疑似为可控变量，所以爆出任意文件包含漏洞，那么实际上，往上看可以发现$\_G['SYSTEM']['PATH']其实已经事先定义好了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRldggNFtnwsic3iaEdptWTVD3SsER6vCkKGSn1gTxTkNGyy5q6pulC2TFKEc1sZ0YCLWKbFv3esqribXibFeQBzyqh9KicWvdNGIic4/640?wx_fmt=png&from=appmsg)

2、定位漏洞
1）发现一个file\_get\_contents，可控变量为$path

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQPjMDBCC88YiciahLt3Pqc2dVqQnE7ndUbuBIwEPVVP0pL7F16yjkEdp7ynJO0tGDLldrUFhOiakhqVUamggfjE4fp1cDv2R9R1I/640?wx_fmt=png&from=appmsg)

往前看，$path为我们直接get传入，只是做了一些限制与鉴权，没有进行过滤

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTDcfK6JdsZ5uDhMFFXb8qem1A9rZ85BlZZbsMaWbgVQjmA6BtzAbsInyqH14WicA16dyIN9j6DRS3Dcl9uojC9icCTKhKb8Usdw/640?wx_fmt=png&from=appmsg)

```
$path = realpath($_GET['path']);if (!$path) {    if (!InArray('edit,save,del,mkdir,mkfile', $type) && !$_G['GET']['JSON']) {        PkPopup('{content:"不存在的路径，请求路径：' . $_GET['path'] . '",icon:2,shade:1,hideclose:1,submit:function(){location.href="index.php?c=app&a=filesmanager:index&path="}}');    }    ExitJson('不存在的路径，请求路径：' . $_GET['path']);}$_G['TEMP']['PATH'] = iconv('GBK', 'UTF-8//IGNORE', $path);if (strpos($path, $spath) !== 0) {    if (!InArray('edit,save,del,mkdir,mkfile', $type) && !$_G['GET']['JSON']) {        PkPopup('{content:"越权操作，请求路径：' . $_GET['path'] . '",icon:2,shade:1,hideclose:1,submit:function(){location.href="index.php?c=app&a=filesmanager:index&path="}}');    }    ExitJson('越权操作，请求路径：' . $_GET['path']);}switch ($type) {    case 'edit' :        if (filetype($path) != 'file') {            if ($_G['GET']['JSON']) {                ExitJson('不存在的文件');            }            PkPopup('{content:"不存在的文件",icon:2,shade:1,hideclose:1,submit:function(){location.href="index.php?c=app&a=filesmanager:index&path="}}');        }        $suffix = substr($path, strrpos($path, '.') + 1);        if (!InArray($suffixs, $suffix)) {            if ($_G['GET']['JSON']) {                ExitJson('不支持的文件格式');            }            PkPopup('{content:"不支持的文件格式",icon:2,...