---
title: 跨目录上传+任意文件读取进行getshell
url: https://mp.weixin.qq.com/s/kukWovzEuitqxDiLTonf8g
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:49:00.898438
---

# 跨目录上传+任意文件读取进行getshell

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQkxylTRB5BkA8TES1ZtlnVg5atNyH4e7LtsicZWU4DrWxibnngibGhla7PwQXeG03djANib1ljdetQlUjupop0RhoDzuyd4MBKgRs/0?wx_fmt=jpeg)

# 跨目录上传+任意文件读取进行getshell

中铁13层打工人
中铁13层打工人

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
作者:中铁13层打工人原文链接:https://forum.butian.net/share/2350
```

#### 1.跨目录上传

对某系统进行测试时，发现有一处上传附件的功能，常规上传个文件试试

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQN9Zto6ciarQNicuFqqWYwrJcPBpZFtII4xOZVjCiaL60KrkicHiaY9FeYbnEicl8Ok8iaq7XYmd4Ds8JUiaJusKXkQNLYaccAwrdg7ag/640?wx_fmt=png&from=appmsg)

发现返回包返回了重命名后的文件名称和系统的绝对路径

继续看上传的文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQkc2M2s7GjficY4esB6PraXmBRdoXoUXjr7L7kWOFwamYiafWkwsic65y50QpBdYvlLiaYRBGhnGS2sc2wTzekiad38UtJh6icMUJTA/640?wx_fmt=png&from=appmsg)

只有一个预览的功能，访问直接下载该文件（请求链接为`DownloadServlet?type=W***J&filename=QQ%E5%9B%BE%E7%89%8720230414145425.jpg&pyName=9be6c164-d5a9-4a1e-a555-139ec1ce383d.jpg`），并没有什么用

回头仔细看上传的数据包，发现上传的参数type的值返回在了系统的绝对路径中，猜测type的值即为上传的文件夹，将type改成1尝试，印证了猜想，且是可以直接上传jsp的！

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQK9K6nEQmQF6kjmmIMGuLUBdI6qhVE8WqE9LpbPaUV5xvNB9MoFPicRsmm7WCCJw8mlN1jTODRbibNicrZOsGbFgwZd3ZLqTdj0Y/640?wx_fmt=png&from=appmsg)

既然上传文件参数可控，尝试使用../看是否可以跨目录上传，发现也是可以的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTtN7re6X6qSpt8NPTf3N4cuWlcId6NZ1wuptcOXmk056m5GIcm0dDr5gHlfqNKgZwP4TfUkPr5dRRlXjhPJkQsVoDg9Ksv5AM/640?wx_fmt=png&from=appmsg)

至此得到一个上传路径可控的有效上传点，且通过上传返回的绝对路径知道了当前的user名称（这个后面很关键）。

那么接下来的思路就是寻找系统的web路径，直接上传脚本getshell。尝试了一些常用的手法例如构造报错等均未找到目标，尬住了一会儿后，想到了之前的跨目录上传，既然上传处可以使用../进行跨目录，那么上传后的预览处呢？

#### 2.任意文件读取

回到刚才的上传预览处

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRMqogJsOnHJUwYicEoa9uhXAPVxlXhnCzlR7IibyXullAd979jn6Nhqb1dTopC5aEqAy9UgHEzv5yfPaWf3wY0tsibtU83InfVWo/640?wx_fmt=png&from=appmsg)

将预览功能处的请求链接`DownloadServlet?type=W***J&filename=QQ%E5%9B%BE%E7%89%8720230414145425.jpg&pyName=9be6c164-d5a9-4a1e-a555-139ec1ce383d.jpg`中的filename与pyname进行构造尝试，果不其然，发现一处任意文件读取

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTL6zlYpaSfFyuIa027hPcQlJT5vvKLHrI0ztVIXyff0ygCnXoiaTJGD9qcTTduZX9DdCbBIPER2U4jAaCrdfzF52QcjS8YpG8w/640?wx_fmt=png&from=appmsg)

得到任意文件读取后可以通过读取中间件的默认配置文件寻找更多信息，例如

* tomcat
  `/usr/local/tomcat(tomcat-1.1.1(具体版本号))/conf/tomcat-users.xml`

  `/usr/local/tomcat(tomcat-1.1.1(具体版本号))/bin/catalina.sh`(其中日志的配置路径)
* apache

  `/var/log/apache2/access.log`
  `/var/log/apache2/error.log`
  `/var/log/httpd/access_log`
  `/etc/httpd/logs/access_log`
  `/etc/httpd/logs/error_log`
  `/etc/httpd/logs/error.log`
* nginx

  `/var/log/nginx(nginx-1.1.1(具体版本号))/access.log`
  `/var/log/nginx(nginx-1.1.1(具体版本号))/error.log`
  `/usr/local/var/log/nginx(nginx-1.1.1(具体版本号))/access.log`
  `/usr/local/nginx(nginx-1.1.1(具体版本号))/logs`

  `/etc/nginx(nginx-1.1.1(具体版本号))/nginx.conf`

通过旁站的其他端口的web指纹，发现使用的是tomcat

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSRx9UfibQKRAK2lqWibEiaR2zunaoGoVU52ibQYPWoSCGp7j6Ria57UwVM1VDgPfabq3XYtJHn1gXSysZgLJiaHchQFSJ8hrEEHm2tU/640?wx_fmt=png&from=appmsg)

直接尝试读取tomcat的默认配置文件，均失败：）

接着尝试读取操作系统的默认路径，linux下常用路径如下

```
/etc/passwd                     账户信息
/etc/shadow                     账户密码文件
/etc/my.cnf                     mysql配置文件
/root/.ssh/id_rsa               ssh-rsa私钥
/etc/redhat-release             系统版本
/root/.bash_history             用户历史命令记录文件
/home/user/.bash_history        特定用户的历史命令记录文件
/root/.mysql_history            mysql历史命令记录文件
/var/lib/mlocate/mlocate.db     全文件路径
/proc/net/fib_trie              内网IP
/proc/self/environ              环境变量
/proc/self/loginuid             当前用户uid
```

最终通过/home/user/.bash\_history中成功找到了tomcat的web路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSKuAZW9dYXpS2iawLZ0lrzrxmURart8cEiau6hD2QE5l1NickfEB0KoZMP50TuGTNCPzw190XKwUnNYX6cicxOeoxdicdfmzOoJf3M/640?wx_fmt=png&from=appmsg)

#### 3.getshell

万事具备，直接上传至根目录下，访问

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTCasz444YnLDXibPuLsULbicic9m8LQUViaHiar0OicFAQia51AKv1spX57rf0Y9o7qJf2SqCDHuoVTloFxdlPBZdl2QLEKAlicZiaQROM/640?wx_fmt=png&from=appmsg)

根目录下不解析，直接跳转到了登录页面，但是可以看到跳转目录携带了我们访问的jsp。

这种情况下，有账号的话(本系统提供了注册功能)，直接登录后访问即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTsDU3ibgpMFrLlJkgsqXVqjgibKFeo9Ob8AVCibE99Wiaicz6eqNVic34VbWicwPIHdCntcia1ZMXWZ318WfEVVydOpULyYZw595EFsx8/640?wx_fmt=png&from=appmsg)

#### 4.一些拓展

上述的情况都是登录后测试的，如果上传点是fuzz出来的，没有目标系统的账号，也可以采取如下几种方案。

1.尝试直接上传至系统的静态目录，例如系统自动加载的js文件的目录。

2.尝试绕过fillter的鉴权，一般从fillter对目录的白名单或是文件后缀的白名单两个角度绕过入手。

附一些实战的案例。

目录白名单绕过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ64qriahQVw8GEWFia3DibXgNuRMLrpqJXLLQH72gc3PqY7wsoX9oEck9YrPzJYtpic3feWNuE90fgETfPUXcBnm4hTfz6v9bmEh8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQq3cyib601Ohbo1hA16qXHYlJry7fobX0icBxHjuP7Akic0xX8AeuX7Zpz2F7Fza8UsG2EMnCmlRMBqGc3ZknQEm6arOkT0Y0OwY/640?wx_fmt=png&from=appmsg)

文件后缀白名单绕过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQRPU6ybK53gPVelODGAbhuKWLdLmgYQmmicbe8k5pCc9osaiaL1O5PKdSoz1pJf4VHURiaibbdibLQJ2v5cNn4iaTYsXHlICaQghGXk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSAnYsFA8LEAMibZoNYCqMpl0LyFgUAErib5Jbibkkibd24r7gQciajT8TVyey57jghKgdVxyhV2OZXtEhA7m7RppC0QgzUjhQvahXs/640?wx_fmt=png&from=appmsg)

其他情况绕过

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTHL6xrSEysbUjV7kkTNWt8kaQZYTe1hEZz6XneuCIh3iadgSANteJ5x4rRKXquuYibhhGx1Ju1MFgSXjFA88GKdaEm2c7LJcpicA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT9kTKRUlvo0qxumVFZmaeL91oiaFC0EUY3kN1oDWQ78u7cVFEic1bWKIwb3wrDSH2temD0yBjdnCDt0eS8BAcxiaSDu6q9V4laUI/640?wx_fmt=png&from=appmsg)

3.寻找其他的web可以直接访问且知道路径的目录

例如本案例中的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRiaMWsZzd5S4Kojia6c7WNc3DicDITRwlFNCjsAUsMwCylaBicr2ugcOGCLv9YaulQcwymD4iaicFnM1Yxem6lpP46ib7pWCGtiaDsDjQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQgUQYEC7VXstRUbFSIYo2yA25pDCUMCydL2icUJ1XtJVbDq6bickBgcZWke0kKdO5ic2AZictrON5AXw6zfG3zcHxiasfzMe7mPmO4/640?wx_fmt=png&from=appmsg)

直接构造上传

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRzPDWTzdEEz5b8kCjictotGC9qa2n5mq14SeIDmbxLibhZHCDV6Os2ibiaDPiaWjkuRcth3iagMPPy1VJevqjX9iaQcPHmCmZwYHoJAo/640?wx_fmt=png&from=appmsg)

浏览器访问，成功rce

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1p99QHmJzd8ebLScjOqjZ10cNH4UgJQabLfttibiaGJMXYiayNdSfxiaq562PmY4xkicia0yH1sf41MSqlKZBnKqIAesqhicH41CPSw/640?wx_fmt=png&from=appmsg)

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKW...