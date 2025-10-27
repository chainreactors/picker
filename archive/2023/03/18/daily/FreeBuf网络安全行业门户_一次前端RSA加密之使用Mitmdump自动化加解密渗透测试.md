---
title: 一次前端RSA加密之使用Mitmdump自动化加解密渗透测试
url: https://www.freebuf.com/articles/web/360596.html
source: FreeBuf网络安全行业门户
date: 2023-03-18
fetch_date: 2025-10-04T09:58:09.764332
---

# 一次前端RSA加密之使用Mitmdump自动化加解密渗透测试

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

一次前端RSA加密之使用Mitmdump自动化加解密渗透测试

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

一次前端RSA加密之使用Mitmdump自动化加解密渗透测试

2023-03-17 14:19:23

所属地 山东省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 写作背景

在一次实战渗透测试中，使用burp抓包遇到了js加密，通过js逆向找到了加密算法，最终利用mitmdump联动burpsuite实现了自动化加解密

## 遇到的问题

在得到授权的前提下，心情愉悦地打开burp抓包，进行日常地抓包改包测试，但是测试时发现请求体和响应体均被加密了，且密文都是d1，d2，d3格式，这就难受了≧ ﹏ ≦

![image-20230308164635930](https://image.3001.net/images/20230309/1678329371_6409461bd473912e225a3.png!small)

## js逆向（大佬可直接越过此部分看Mitmdump）

遇到上面地问题，首先当然是得定位加密函数了，F12打开浏览器控制台，直接搜索："d1:"

![image-20230308165347802](https://image.3001.net/images/20230309/1678329379_640946231d38c56de7094.png!small)

可以看到此处可以获得d1，d2，d3，其中d1是由a的值获取的，d2是由s的值获取的，d3是由u的值获取的，那么我们直接下断点在a的生成处，重新刷新网页，在a处断下，F9单步步入

![](https://image.3001.net/images/20230315/1678884983_6411c0774aa9821db1467.png!small)

先是来到v["f"]的生成处，再单步两次回到之前的界面，再单步一次即可进入Object(v["f"])函数内

![image-20230308165734530](https://image.3001.net/images/20230309/1678329402_6409463a54c381c4f55da.png!small)

可以看出来是使用了cbc模式，猜测使用了AES加密，此时我们在右侧作用域查看一下变量值：

![image-20230308165822099](https://image.3001.net/images/20230309/1678329405_6409463dd26c0b17fa0cf.png!small)

可以推测e为key值，i为iv值（e和i的值为前面n和o的值，后面会讲n和o怎么生成的），t为加密前的请求体值，但是此处有一个问题：iv值通常应该是16位才对啊，看来此处不能直接调用aes解密了（没学过密码学只能偷偷哭泣了/(ㄒoㄒ)/），看来只能硬抠代码了

这里d1的值已经弄明白了，我们再去看看d2和d3的值是怎么生成的，此处还是刷新网页，重新断下：

![image-20230308170156718](https://image.3001.net/images/20230309/1678329423_6409464f135a0014282c6.png!small)

可以看到d2也就是s的值是由Object(v["c"])函数生成的，传入两个参数，生成d2时传入n和r，生成d3时传入o和r，而r的值在上面可以看出来是rsa值，此时看一下这个值是啥：

![image-20230308170329231](https://image.3001.net/images/20230309/1678329426_64094652572af2df3786f.png!small)

已经明确了rsa的值，此处推测是服务端的公钥，那么再来看n和o的值，可以看出来是调用y(32)函数生成的，跟进查看：

![image-20230308170515117](https://image.3001.net/images/20230309/1678329430_64094656a3e814d785ddd.png!small)

简简单单的根据"0123456789ABCDEFabcdef"生成的32位随机值，那么到这里，加密过程就已经弄清楚了：

d1是由n和o作为key和iv值，对原始报文使用aes加密生成的，d2由服务端的公钥和随机值n生成的，d3由服务端的公钥和随机值o生成的

那么我们前面说到了响应体也是有d1，d2，d3，那么再去看解密流程，同样的思路分析下来可以知道：

响应体中的d2可以使用客户端私钥解密出n，d3可以使用客户端私钥解密出o，d1可以使用n和o解密出原始报文（**而私钥的获取方式同上公钥获取一样，下断点即可查看，解密函数就在加密函数下方**）

咳咳，这个加解密，属实厉害，接下来就是抠js代码了

## 抠js代码

这个过程属实痛苦，js挨个抠的话，还好，但是我们仔细观察一下这个网站，发现是webpack的，vue开发的网站，硬抠肯定得掉不少头发，此处讲一个快捷的webpack通用抠代码的方法：

首先抠webpack入口，通常会在html主页面内嵌入，此处讲一个快速定位入口函数的方法，在索引页面内搜索call，挨个查看一下，会有如下类似代码：

![image.png](https://image.3001.net/images/20230317/1679033944_64140658ae20e321735cb.png!small)

将函数抠下来，放在js文件里，定义成如下格式：

```
var test_module;
(function(e) {
var u={};
function f(c) {
if (u[c])
return u[c].exports;
var n = u[c] = {
i: c,
l: !1,
exports: {}
};
// console.log(c)
return e[c].call(n.exports, n, n.exports, f),
n.l = !0,
n.exports
}
test_module=f;
})({
//此处留下贴之后抠的代码
}）
```

在开头写个test\_module是为了后面好调用，接下来就是抠加密和解密函数，先抠aes的加密函数，往上找找到aes加密函数的最前面

![image-20230308192049978](https://image.3001.net/images/20230309/1678329437_6409465d74450a6819003.png!small)

往上找到如图所示位置：

![image-20230308192113699](https://image.3001.net/images/20230309/1678329440_64094660b9390222f0510.png!small)

往下找到如图所示位置

![image-20230308192151896](https://image.3001.net/images/20230309/1678329444_64094664e637ac096b7eb.png!small)

```
"4b2a": function(t, e, i) {
      "use strict";
      i.d(e, "a", (function() {
          return n
      }
      )),
      i.d(e, "c", (function() {
          return o
      }
      )),
      i.d(e, "b", (function() {
          return a
      }
      )),
      i.d(e, "d", (function() {
          return u
      }
      )),
      i.d(e, "f", (function() {
          return c
      }
      )),
      i.d(e, "e", (function() {
          return f
      }
      ));
      i("d3b7");
      var r = i("7c74").sm2;
      function n() {
          var t = r.generateKeyPairHex();
          return new Promise((function(e) {
              t && e(t)
          }
          ))
      }
      function o(t, e) {
          var i = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : 1
            , n = "04" + r.doEncrypt(t, e, i);
          return n
      }
      function a(t, e) {
          var i = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : 1
            , n = r.doDecrypt(t.substring(2), e, i);
          return n
      }
      var s = i("7c74").sm3;
      function u(t) {
          var e = s(t);
          return e
      }
      var h = i("7c74").sm4;
      function c(t, e, i) {
          var r = h.encrypt(t, e, {
              mode: "cbc",
              iv: i
          });
          return r
      }
      function f(t, e, i) {
          var r = h.decrypt(t, e, {
              mode: "cbc",
              iv: i
          });
          return r
      }
  },
```

抠下来代码如上，放置在之前抠的入口函数下的后面的中括号里，接下来就是挨个抠，js逆向俗称：缺啥补啥。为了方便，查看缺啥补啥，我们在入口处修改如下图所示：

![image-20230308192404280](https://image.3001.net/images/20230309/1678329449_640946698893dbd89bf24.png!small)

这样做的好处是会提示我们缺啥函数，再去js文件里抠出来，抠的过程中会遇到：i("d3b7");如果是像上面这样调用函数且没有声明变量去获取返回值，可以把（i("d3b7")）注释掉，不然还得挨个抠下来，会很麻烦，而且也用不上，遇到后面这个情况得保留（例：h=i("d3b7")），接下来的过程便不多说了，漫长的抠代码过程

这部分算是讲完了，那么最后贴一个调用方法（var test=test\_module("7a74")；然后就可以用test去调用其方法了）：

```
function test_enc(t, e, i) {
var test=test_module("7a74");
var r = test.encrypt(t, e, {
mode: "cbc",
iv: i
});
return r
}
```

## mitmdump中间人代理

抠完代码后，我们直接使用mitmdump对burp做上下游代理，这样我们可以在mitmdump代理层去修改数据包，然后在burp层看到的就是我们日常渗透未加密的数据，是真的很方便

该方法适用于如下三个场景（其中app和小程序需能看到加解密或防篡改的源代码）：

1. web网页端做了防篡改以及加解密
2. app端做了防篡改以及加解密
3. 小程序端做了防篡改以及加解密

这里往下叙述共分为三个模块：

> 第一个模块为编写使用mitmdump的脚本
>
> 第二个模块为响应体解密，此处使用二级代理即可（即burp上游代理）
>
> 第三个模块为请求体以及响应体加解密，此处需使用三级代理（即burp上下游代理）

#### 示例脚本

编写好js的加解密脚本后，使用如下模板（修改加解密函数以及request和response函数为适应自己的加解密代码，并命名为test.py）：

```
import execjs
from mitmproxy import flowfilter
from mitmproxy.http import HTTPFlow

#解决js代码中中文编码错误
import subprocess
import json
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

with open("test.js","r",encoding="utf-8") as f:
  js_code=f.read()
  f.close()
ctx=execjs.compile(js_code)

#请先修改公钥
publickey=""
#请先修改私钥
privatekey=""
def enc(data):
  [d1,d2,d3]=ctx.call("req_enc",data,publickey)
  return [d1,d2,d3]
def dec(d1,d2,d3):
  result=ctx.call("res_dec",d1,d2,d3,privatekey)
  return result

class FilterFlow:

  def request(self, flow):
      if flow.request.url.startswith("https://x.x.x.x/"):
          req=flow.request.get_text()
          if '"d1":' in req:
              return
          print("加密数据前：".format(req))
          data=enc(req)
          d1=data[0]
          d2=data[1]
          d3=data[2]
          json_data={"d1":d1,"d2":d2,"d3":d3}
          result=json.dumps(json_data)
          print("加密数据后：".format(result))
          flow.request.set_text(result)

  def response(self, flow:HTTPFlow):
      # print(flow.response.get_text())
      if flow.request.url.startswith("https://x.x.x.x/"):
          resp=flow.response.get_text()
          data=json.loads(resp)
          d1=data["d1"]
          d2=data["d2"]
          d3=data["d3"]
          result=dec(d1,d2,d3)
          flow.response.set_text(result)

addons = [
  FilterFlow(),
]
```

#### 响应体解密

此处仅需设置burp上游代理，方法如下：

```
mitmdump -p 9090 -s .\test.py --ssl-insecure
```

burp端设置：User Opti...