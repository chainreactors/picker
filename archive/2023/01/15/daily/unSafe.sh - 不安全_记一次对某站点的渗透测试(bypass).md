---
title: 记一次对某站点的渗透测试(bypass)
url: https://buaq.net/go-145532.html
source: unSafe.sh - 不安全
date: 2023-01-15
fetch_date: 2025-10-04T03:55:55.638108
---

# 记一次对某站点的渗透测试(bypass)

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/4052a2b78c5eb0e9739150e6aa35f7e5.jpg)

记一次对某站点的渗透测试(bypass)

0x01、起因某天A把我留下，想让我检测一下某站点的安全程度（有授权的，领导的任务罢了）我想了没想就拒绝了，说，上次不是给你挖出过一个sql注入了吗他说，不亏
*2023-1-14 17:7:0
Author: [xz.aliyun.com(查看原文)](/jump-145532.htm)
阅读量:51
收藏*

---

## 0x01、起因

某天A把我留下，想让我检测一下某站点的安全程度（有授权的，领导的任务罢了）

我想了没想就拒绝了，说，上次不是给你挖出过一个sql注入了吗

他说，不亏待你，有额外奖励的

不是因为奖励啊，只是单纯的喜欢渗透网站罢了

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114160226-c8bffbbc-93e1-1.jpeg)

垃圾水文，轻喷

## 0x02、一战

先访问某站（原谅我不放图片，不然无法过审）

看样子是一个平平无奇的网站

看到.action后缀，立马想到java环境，多半是tomcat+struts2

直接掏出大宝贝一把嗦

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114160400-00d879a2-93e2-1.png)

很明显失败了

不慌，再看看别的啥的

扫了端口发现oa系统，通过信息收集手段获取账号密码

但我认为此处功能点没什么用，故暂时放弃（打脸了）

掏出lijiejie的神器一顿扫，也只发现了一处DS\_Store文件泄露

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114161127-0b476320-93e3-1.png)

棒极了，啥都没有

接下来还发现了一处反射xss

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114161200-1f0010a6-93e3-1.png)

但这种漏洞要是交差，估计会被A骂死

身为聪明勇敢的读书人，怎么可能会放弃呢

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114161232-324d1ffa-93e3-1.png)

备份文件，扫不到；目录爆破，啥都没有；中间件漏洞，不存在；端口服务开放，做梦呢

就连废弃系统都在嘲笑我

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114161243-38803cb8-93e3-1.png)

好在天无绝人之路，我在网站底部看到了一丝希望

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114161412-6dce2eb6-93e3-1.png)

此时我的思路是:fofa找相同系统站点------getshell------拖源码审计------再回到主站

直接fofa大宝贝一把梭

但站点少的可怜，拿lijiejie的神器跑了一轮，也没有啥泄露。。。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114161958-3c3071c4-93e4-1.png)

还是硬着头皮看了一眼

这次运气挺好，使用相同系统的站点存在struts2漏洞

果断上传拿shell

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114162553-0f45760e-93e5-1.png)

工具也有不准的时候，虽然显示上传失败了，但仍然能getshell

冰蝎连接成功！芜湖，起飞

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114162730-4936e640-93e5-1.png)

但接下来这权限着实把我整吐了，systeminfo无法执行，rar也用不了，但我又懒得一个一个下载源码

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114162756-5889e2f0-93e5-1.png)

因为本人太菜了，提权基本上不会

但身为聪明勇敢的读书人，怎么能放弃呢？

这里就去讨教了一下某前辈

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114162912-86182fd8-93e5-1.png)

对某前辈表示感谢

因为此处使用的windows环境，不太方便反弹shell，把木马换成了哥斯拉的马儿

哥斯拉下有个模块，方便操作shell

监听——nc直连——运行systeminfo文件。成功！

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114163326-1d5845e0-93e6-1.png)

复制补丁号，然后找到了一下缺失的补丁

在此推荐某位师傅的网站：[https://bugs.hacking8.com/tiquan/，方便查找](https://bugs.hacking8.com/tiquan/%EF%BC%8C%E6%96%B9%E4%BE%BF%E6%9F%A5%E6%89%BE)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114163455-529601c0-93e6-1.png)

这里采用Potato提权

但生活总喜欢在为我关了一扇窗后，再用门狠狠的夹我的脑子

提权一直失败，换用了其它的方式也不行

后面才知道，原来SweetPotato源码中的默认路径与我的环境不符，要重新修改后再编译

编译完，再重新执行

成功提权！

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114163512-5c9fedac-93e6-1.png)

然后就是源码打包，下载

(PS：用哥斯拉默认的源码打包，下载下来后文件会报错，而且缺失很多，也不知道为什么，但权限提升后用7z打包就好了，很奇怪。如果有知道的表哥，在下方留个联系方式)

接下来就是java源码审计了

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114163616-82e23614-93e6-1.jpeg)

大体目录是这样的。老规矩，先翻看一下配置文件，看一下它用了哪些框架

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114163636-8e7ee72e-93e6-1.jpeg)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114163929-f5adc2b2-93e6-1.png)

看样子是使用了Hibernate+Struts2+Spring框架

用jd-gui快速反编译class文件，获取java源码

将Hibernate和Struts2框架的相关配置文件、action对象、filter大体熟悉以后，就开始审计了

这里不得不吐槽一句，这个开发是真的懒，部分源码还留着与该站点相关的注释

既然是为了证明危害，那么基本是以getshell-sql-信息泄露为主

全文查找文件上传的地方

在搜索处发现了一处可以upload的地点

（此处图片找不到了，假装我是图片1）

查看对应java文件源码，发现无任何过滤

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114164225-5e91f000-93e7-1.png)

去掉注释，上传，不过不知道为什么会出现这种状况，查询了很多资料也没弄明白

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114164238-6647cebe-93e7-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114164304-75cb07ca-93e7-1.png)

直接构造接口上传，发现会有拦截，但本地源码审计无拦截，估计是某站点二次开发了

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114164708-079dc20a-93e8-1.png)

### 第一处水洞：账号密码可爆破

顺便看了一下oa系统

成熟的框架，也导致了sql注入和越权不存在

但是逻辑漏洞仍然存在，修改密码处未限制，能批量爆破账号改密码

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114164736-18354066-93e8-1.png)

后面因不可抗力，A也叫停了我，遂暂停了测试

## 0x03、二战

几个星期后的某天，A又提到了某站点，从它口中得知，该站点翻新了

那我上次的源码也约等于白费了。。。

果不其然，A又找到了我，我也是很《轻松》且《愉快》的接下了任务

### 第一处漏洞：弱口令

我想了想，既然翻新了，那多多少少会加点东西

更新后发现了部分文章页面泄露了某editor的组件信息

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114164921-568b047c-93e8-1.png)

抱着尝试的心态，来到了登录页面

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114164957-6c07957c-93e8-1.png)

结果发现，admin/admin一发入魂

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165159-b4fc20ea-93e8-1.png)

### 第二处漏洞：部分源码+密钥泄露

四处翻看目录，偶然间发现一个压缩包

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165213-bd055216-93e8-1.png)

看了看大小，感觉像是源码，下载下来了

果然，泄露了很多secret，有关aliyun、钉钉、wechat、云盘等等

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165302-da7b3072-93e8-1.png)

其中部分还与其它公司资产相关联

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165353-f8a6f536-93e8-1.png)

oss也能成功接管，也涉及了很多的敏感信息（不敢多说，保命要紧）

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165408-01e71248-93e9-1.png)

但还是高兴早了，class相关文件没打包下来。。意味着只能看jsp的源码，也就只有对找接口来说，会方便一些

通过配置文件查看，发现站点改成SSM框架，晕，别想与sql注入相遇了

### 第三处漏洞：bool ssrf

上面下载下来的源码对接的是oa系统，而第一次的源码对应的是主站，所以我将重心又重新转回了oa系统

根据上方的源码可以看到增添了ueditor组件，1.4.3的jsp版本，相信大家都懂

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165450-1ab9ea8e-93e9-1.png)

### 第四处漏洞：bypass 多个waf--->getshell

又是通过新的源码，我找到了oa内一个极为隐蔽的上传点

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165516-2a98bbc4-93e9-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165529-31cedb58-93e9-1.png)

话不多说，登录oa，找到页面开始上传

一开始我先传了个jpg，发现能正常解析

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165656-662425c0-93e9-1.png)

再传了个html，直接g了，显示Connection reset

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165857-ae4018a0-93e9-1.png)

我心里一惊，常规应该不会那么拦截，多半是有硬件waf

通过大小写上传SVG文件发现，此处应该采用了黑名单，心想，90%是稳了

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165926-bf8c0f9c-93e9-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114165951-ce305ada-93e9-1.png)

然而后面的情况让我挺绝望的，光是后缀名这里我就绕过了很久

换行、多个等号、加点、脏数据、不常见后缀名、去掉引号绕过等组合手段，都无一例外的被干掉了

在这里苦苦绕了一晚上

也算是比较好玩吧，这里的开发有一个逻辑，你把content-type改成text/html，再把filename里改成xxx时（不加后缀，直接xxx），系统会自动帮你重命名成时间戳.xxx

于是乎，后缀名就成功绕过了

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114170016-dd68d360-93e9-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114170030-e5bfea44-93e9-1.png)

可内容拦截比较变态，出现一点java特征都不行，连赋值都会被干掉（el表达式除外）

既然是硬件waf，我想到了脏数据绕过，jsp内容中可以包含html的注释

最终经过测试，大约80w的脏数据可以成功绕过

可上传上去冰蝎马后，无法连接，估计是落地就被干掉了，怀疑存在AV，于是厚着脸皮向某前辈白嫖了免杀马

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114170058-f608a1fc-93e9-1.png)

上传成功

这次连接成功，没有被杀掉

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114170111-fda8fb78-93e9-1.png)

看了一眼，艹，全家桶啊简直

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114170124-057087f4-93ea-1.png)

最后，象征性的whoami，结束战斗

![](https://xzfile.aliyuncs.com/media/upload/picture/20230114170135-0c4307a0-93ea-1.png)

（本来想进内网的，但想了想，不节外生枝了，如果有机会再说）

## 0x04、结尾

站在前辈们的肩膀上，结合实际情况，巧妙了绕过了waf，也是蛮开心的

最后也是从A手中拿到了应有的奖励

~~安全，狗都不学~~

文章来源: https://xz.aliyun.com/t/12041
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)