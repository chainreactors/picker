---
title: 网络设备通用漏洞挖掘由黑到白
url: https://mp.weixin.qq.com/s/-Q2r9raSwKhD5ST-_iE9cQ
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:34:36.060826
---

# 网络设备通用漏洞挖掘由黑到白

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Pms46XiaGB2wp4tKUHM0CATLyYwvCMMVIZupEgxnXA12MibxPU1wxRKm8sACPorhib9xsDwnPlSjVQZe7eoolnATkaEGIRszpxJXKEKdQMjTeE/0?wx_fmt=jpeg)

# 网络设备通用漏洞挖掘由黑到白

轩公子谈技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于我不懂安全
，作者Vlan911

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6Cj8BL0RFU05hV3SpgOHicCaQjCdVl5fNG2N5Ze9BGQeg/0)

**我不懂安全**
.

分享挖掘漏洞小技巧，分享安全案例以及一些安全动态，分享实用技术

本文知识点：

* 通过大量的公开设备寻找弱口令，从而进入后台获取突破点
* 进入后台快速寻找RCE漏洞，获取更高权限
* 打包源码，实现白盒代码审计
* 代码加密，如何解密
* 获取不需要权限的任意文件下载漏洞，组合拳获得数据库文件
* 还原加密效果，上传可被系统解析的webshell

首先随便输入个密码，然后查看返回包，通过错误密码发现里面的特殊关键字

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2xuQWsia7R9S0UEPzKVfm2uyK8tt41FH7Pc9boRPfIOJgiczn6f6mgZSJLwvNrxfqgicrVTxZ2L7bWtYYKh7cS6qnQ1CcIGcNT5yc/640?wx_fmt=png&from=appmsg)

这种情况可以直接筛选返回包不存在“Authentication failed”关键字的，即可认为他登录成功，虽然有误报的可能，但是机会还是很大的；将所有的目标资产收集好以后，批量测试一下密码admin的弱口令，成功的发现了几个存在弱口令的目标

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2z6WSEWga6UL5nTxK4ytq62C1HicWwgQNULBwibZLibwjSdxk31nVUibakG7y2BMyIWQic75icIO1H5mfJVv5ibslIJGUjU65VxDcG9d8/640?wx_fmt=png&from=appmsg)

而后登录进行，快速的定位到了一个RCE漏洞，这块也是老演员了，很多网络设备的命令注入漏洞都在这里

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2w6Ib9MG2fKYTtwQRfu5m4HYKkbTOJaOp2ibVJrnYYNKtYQaZsHibGnFCd4Ts7E09T3oaibiamRToj2TXEabZB48QIjDiaTzZKlBXTg/640?wx_fmt=png&from=appmsg)

运气很好，这块还是个未授权

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2wq9jZpUHqhglSeSuL1T52sHgX6iabbnw9Q39XHaJrP0ZuFfFrfAdhCcV5wVGTjOL8HZJfiaZEbk8vfPtSbDm3xr0oYHOw7cpJfE/640?wx_fmt=png&from=appmsg)

看了下固件版本号，发现版本应该是最新的，也可能是次新的，但是经过批量测试发现效果反响平平，不是所有设备都存在这个漏洞，不排除修复的可能，但是我猜测更多的是这里的未授权修复了，因为我批量测试的时候是利用未授权的方式进行测试的

利用tar指令将源码进行备份打包，而后存放到web目录即可下载，下载到本地后，发现代码是MVC架构，但是又不全是，上面发现的ping功能的代码很显然就不符合，奇奇怪怪的

定位到代码打开查看，发现代码加密了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2z52SWibHAtgRwZZFu3JGgPCbQCqyCRfzGbgvshnzqxoIu08LB3SdaseYNicdK6YLMg7oNnQGCbVvTkTUqicS14ibVT43GJeric9wfA/640?wx_fmt=png&from=appmsg)

通过PM9SCREW能大致推测出加密方法，screw加密，这个项目在github是有的，想要解密文件需要找到他的加密密钥和加密的长度，这个东西其实藏在 php\_screw.so  文件里，想要找到这个文件，要不就是在他的phpinfo里找到 extension-dir 目录，要不就通过find指令直接搜索，正好这里有命令注入，通过命令注入漏洞可以进行检索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2wmiasFZeOmspPdnyGiaEeWJUQasPM2UmfPYLMRMF6l98Y5gzMMHNkrQ6pPBWEl4bpql9AR1d9rSCptgy9Drt9Q7wRiaZeYnWf0dk/640?wx_fmt=png&from=appmsg)利用cp指令将so文件拷贝到web目录而后下载，并使用ida打开进行分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2xtIJCKiawe7VkJg3bg9EJd0IIf4uppic6uiaV1bd18maB3Bsjr1Muk7tyuCZLVQlHWHIGTpTicY46SFtZSn1LcUYWeK8zuG9icdLIY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2xuvwicLOtrIcVPs0MxXThzGfQOeTHicua0P3Tj41zUC6hFib2OCIDxuVy3DMic7Ar6o7IZdM8rEVLdmNibWc8TQztnuA2FPpvAFmng/640?wx_fmt=png&from=appmsg)

也可以下载工具https://github.com/DaBoQuan/php\_unscrew

将文件解压到kali里，然后编译，这个工具也可以获取key和length

g++ unscrew.cpp -o unscrew -lz

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2xLjGibatXV1ADPV6bADibJvf9ERAwquDGXJDZOlvlv1MgNCslEbIPU3oyF7cknUKDPYcxcQiabeyLym8VibuG2Y9HLJUT30dvLjNc/640?wx_fmt=png&from=appmsg)

```
objdump -s -j .data php_screw.so
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2x5Aduc2zLtEFJX3wYbGDWlezNUIicBARIeTlbyPlYEFoFAR1AvvuB7ib4v90oqjo9fnibRXTIyKN2y5dAt5WHiaQPNVjcwY3aU3Vc/640?wx_fmt=png&from=appmsg)

```
objdump -s -j .rodata php_screw.so
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2zeKOYdMqTtAcJQXRZico6y5HqFjJNiaLleFgbUvgPAw4zmnQb40icKwicgNiaq5CY2uoFkh3VbqNfTGLPmAu0hhvmWduGYIAlXCexs/640?wx_fmt=png&from=appmsg)

./unscrew config.php 10 e1xxxxxxxxxxxxx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2zzUZMlstQ5EU40zu4dKUECjtpaPzkRI4F28wBlzk6nwribGstVEndnPkibENvBEeu6bktpibIEv4L8bviccJibo2tesiczJS6v3mRh8/640?wx_fmt=png&from=appmsg) 编写shell脚本，批量对php文件进行解密

```
#!/usr/bin/env bash

set -o nounset
set -o pipefail

UNSCREW="./unscrew"
KEY="10"
MODE="xxxxxx"

# 确认 unscrew 存在
if [[ ! -x "$UNSCREW" ]]; then
    echo "[!] unscrew not found or not executable"
    exit 1
fi

# 遍历当前目录及子目录所有 php 文件
find . -type f -name "*.php" ! -name "*_decode.php" | while read -r file; do
    out="${file%.php}_decode.php"

    # 跳过已解密的
    if [[ -f "$out" ]]; then
        echo "[SKIP] $out already exists"
        continue
    fi

    echo "[+] Decoding: $file"

    if "$UNSCREW" "$file" "$KEY" "$MODE" > "$out" 2>/dev/null; then
        if [[ -s "$out" ]]; then
            echo "    -> OK: $out"
        else
            echo "    -> FAIL (empty output)"
            rm -f "$out"
        fi
    else
        echo "    -> ERROR"
        rm -f "$out"
    fi
done
```

此时再次查看漏洞接口代码，发现程序从请求里获取hostname，然后拼接到cmd变量里执行sudo指令，最后利用popen完成实际执行步骤，因此这里有回显并且存在系统命令注入风险；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2y3xFROlFpibiaXufPEqqjrgHPpUsTYIceZ3hANzc1NEIIGTr3OKn0wQVwzia1ZTaL4nKEROgSF3MZatLRib2lyvSZIib1tAia5vFhUw/640?wx_fmt=png&from=appmsg)

同时在此接口里没有任何对session的校验，因为不需要认证即可完成命令执行；

代码拿到手了，还是希望能想办法拿下更多的漏洞，于是先看了下代码的登录逻辑，发现这个程序的数据库是sqllite

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2zlDOico0JR0ecVhmiaNASv595ibMCfJyicjVOGDgKGc4jec4mpVvmQHft9ibPHZ12micK4rxr4OO0icdzY7HghFJtTTJOZS2ic1LMzjibU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2xqJTPJrAsm4yyheep2qmoSwMCoMEwDaXI9PpPfkiaup9W3FVqmc3uAzvuFH5iaWJ61k0ibBM7Rd7TxBXIhL6xYl1mjpVmAWfS95g/640?wx_fmt=png&from=appmsg)

可以看到，通过用户名获取对应密码，然后进行md5编码，与sqllite数据库里的值进行比较，所以下一步就是如何能获取这个数据库？

通过进一步的代码审计，发现了一处不需要认证的任意文件下载漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2zvsdSDGTJOh5Dks3SvLXc66INrb9aq4e11tWHqgNpbYCpGQljibdvkMXREC9FicVSdeyWdq6zfRdytVoYkTsdhoqhg2Xj2MQxEs/640?wx_fmt=png&from=appmsg)

很好，非常的光棍，让我们验证一下漏洞效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2wuibL2YpSKkxK4LkndWGPDab4CPCniaicBNQsKh1ZCBVibgP2KIYSBzPseygwhSVDYbyJ4PLPpZcZBhrx4Nx2rWZyEYHUpL8yXiajY/640?wx_fmt=png&from=appmsg)

把文件下载到本地后，利用navicat打开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yHaPkCO90FW1QTqy5xrudARuO3l9mj8xKv5Nvta7R8UUDKteEXfiafDicN5p91Dxr2pTmLpDk4e7y30xiaoUw3VvaN4m3cGZIuPA/640?wx_fmt=png&from=appmsg)

而后只需要解密md5即可获取admin用户的密码，这样就能做到登录效果了，这么做的原因是因为有一些漏洞是做了认证的，只有经过认证才能进行漏洞利用，比如这个注入漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2wzSKOMfAibKWcZ039t0UUWK8ic1gokFbYXEq5AbCmiaFgldTUhtP5diavzTnePbJ4EQ3Ibln0iaiavMpRpdfibPWNSvPnEa0qwXxenbM/640?wx_fmt=png&from=appmsg)

因为后边发现了一些漏洞是需要认证才能用的，所以获取密码是有必要的，获取密码后构造登录数据包获取session值，而后就可以针对一些其他型号的设备进行测试，扩大攻击面，代码就不展示了

后发现的漏洞不多，就很尴尬，因为这几个洞都能黑盒测出来，可能是运气成分，接下来说一下如果想上传webshell想解析，应该怎么做

首先在github下载项目https://codeload.github.com/Luavis/php-screw/zip/refs/heads/master

apt-get install php-dev

phpize    #编译环境

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2xuCE4AG1xE4w5jibfN6jv1lNq66JmuXZAwuc9XianymyzVdBFXJiaHfOLwiaC6FhLa17m94fV3JWZ39huVAf8m2gnHgQRaPa36c84/640?wx_fmt=png&from=appmsg)

./configure

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2wfwFic9wgum6p6iaK0nLsvKhkZfrzWrk7drt3EwH9XPvAPh77xG27gutpTY202symZ4rONPY8l8ycgjYSveamHuWh2MEDRNjsYo/640?wx_fmt=png&from=appmsg)

修改密钥和长度

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2w5EmfiacFRcyQibJiaWwys6mj3GGJ4zdLkic0h1v6ZY2ia4RAoibanibiaNSp8SXF6HlGYY47Ds8BBoahM3ReIpXNVWDC6Kz07cpxhEVo/640?wx_fmt=png&from=appmsg)

进入到tools目录进行编译

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2wBibTkibcLXwic7IiaP9GqwEbaEAQCqicclDoq9GBaqc61bHwcLxRsAZxRIrFfo5EwsDqonGRHNjIQsOcMkCTPYaODYlBicccaT6Atg/640?wx_fmt=png&from=appmsg)

加密info文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2xO5szMwUL3M9A7W2eNoKSz6R45FhTU4FGuKNdz0NQo1pQNF9Oo9fVHDH2iaET8JdFib5j81WvrvWQljbpPo6ciaiawb0AXicYokFew/640?wx_fmt=png&from=appmsg)

参考：https://www.cnblogs.com/StudyCat/p/11268399.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

轩公子谈技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

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