---
title: 多维度漏洞挖掘突破与实践探索
url: https://mp.weixin.qq.com/s/4UER9vNsWEmErEh_WR3Hyg
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:40:07.178698
---

# 多维度漏洞挖掘突破与实践探索

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQ96fvibwGkwsX9Jc3icc2VNFoqGicJOFSL6N9DicEahhETNF1DGN0VaZHK3400golqIWN1Y5olicic1Qfiae2QZFPdzeRPFDKawZs4oI/0?wx_fmt=jpeg)

# 多维度漏洞挖掘突破与实践探索

一天要喝八杯水
一天要喝八杯水

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

**免责声明**

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:一天要喝八杯水原文链接:https://forum.butian.net/index.php/share/4325
```

前言

刚入门漏洞挖掘的新手常陷入浅层测试困境，仅验证基础功能点。本文整合了其他优秀师傅分享的思路与笔者实践经验，萃取其中精华，旨在拓宽读者挖掘视角。这些分散的优质思路此前缺乏系统归纳 我将一部分优化思路汇总，期望实现思路价值的叠加效应。

### 前置基础

熟悉各种请求以及状态码,在功能点无从下手时,未授权往往在这种信息中;很多人忽略了这个点,接口测试只测试第一层找到的接口,并不会仔细的去看接口的前置目录是否正确,一味的爆破得到`404`,并且第一次找到的接口拼接后也是看一眼功能而已,并不会去观察字节大小加载的新信息去尝试二度拼接

#### 请求 and 状态

**请求方法**

```
GET：获取资源。GET请求用于从服务器获取指定的资源。它是最常见的请求方法，通常用于请求和读取服务器上的数据。

POST：提交数据。POST请求用于向服务器提交数据，通常用于创建新的资源或在服务器上执行某些操作。

PUT：更新资源。PUT请求用于向服务器更新指定的资源，通常用于修改或替换现有数据。

DELETE：删除资源。DELETE请求用于从服务器删除指定的资源。

HEAD：获取资源的元数据。HEAD请求与GET请求类似，但它只返回资源的响应头部信息，而不返回实际的资源内容。

OPTIONS：询问服务器可接受的请求方法。OPTIONS请求用于向服务器查询支持的请求方法。

PATCH：部分更新资源。PATCH请求用于对服务器上的资源进行局部更新，只修改指定的字段或属性。

TRACE：追踪请求的路径。TRACE请求用于在客户端和服务器之间进行往返检查，以查看请求在传输过程中是否被修改。

CONNECT：建立代理服务器隧道。CONNECT请求用于与代理服务器建立隧道连接，通常用于通过代理访问SSL加密的资源
```

**状态码**

```
200 OK： 请求成功。服务器已成功处理请求

301 Moved Permanently： 永久重定向。请求的资源已被永久移动到新的位置。

302 Found：临时重定向。请求的资源临时被移动到另一个URL

304 Not Modified：未修改。自从上次请求后，资源没有发生变化，可以使用缓存的版本

400 Bad Request：错误请求。服务器无法理解请求，通常是由于客户端错误 缺少参数

401 Unauthorized：未授权。请求要求用户的身份验证。

403 Forbidden：禁止访问 服务器理解请求但拒绝执行。可能是因为权限问题。

404 Not Found：未找到 服务器上没有找到请求的资源。

405 Method Not Allowed：方法不被允许。请求行中指定的请求方法不能被用于请求相应的资源

408 Request Timeout：请求超时。服务器等待请求时发生了超时。

500 Internal Server Error：内部服务器错误。服务器遇到了阻止其完成请求的意外情况。

501 Not Implemented：未实现。服务器不支持请求的功能，无法完成请求。

502 Bad Gateway：错误网关。作为网关或代理工作的服务器从上游服务器收到了无效的响应。
```

#### 405接口拼接

`GET`拼接接口没什么好讲的,重点就是`POST`方法以及状态码为`405`的情况

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTvoJiaBPZUibpuR2zT3b13MDQOCUmjl7P61DPNo1GoEy4ydyHKeHQLwM9Csg8ibsAs2nLUISCWLhEicmUQHaicj8gk6qLPA08hkhNE/640?wx_fmt=png&from=appmsg)

**处理方法则是修改请求为`POST`数据下方加入空`json`体,因为某些时候单独的修改方法但是请求没有`JSON`格式响应包也不会有数据返回,这样去做拼接会意向不到的惊喜,再通过接口的响应如果缺少什么参数就找什么参数,**

```
POST

Content-Type: application/json

{
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTjVmkvK1bgq6dHwqzGPVmoqYTBiblXA8J0F3E12AdPn2mJqvw86fTtF1q1nqECtosInXsmyr2XLkeFmIms4AvfxQuCwek8Oef0/640?wx_fmt=png&from=appmsg)

**正确跑出接口后就是根据字节长度找到关键，`size`字节大肯定加载了新的东西新的`JS`,再在新的接口基础上再去浏览器带着接口访问,逐步测试.....**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSOniberOZkMjxcsZy5ViaYhoQ29q3dgm4yJDVCZiaKS2c6aItmlW4Ay2SSIRtynG61QYMyyyGWIq635nHP3gZrDeiaxl29L1G8nxA/640?wx_fmt=png&from=appmsg)

### 403 未授权 权限问题

接口测试及JS信息想进阶一步强烈推荐关注L@2uR1te师傅公众号《HW专项行动小组》,通过JS接口测试挖掘高质量漏洞案例和深层的Java文章相关知识,是不可多得的宝藏公众号,好的文章思路值得被广泛传播。

#### 瞬间后台页面

在访问后台时会在一瞬间加载出后台界面,又重定到登录页面,这里提供两个测试方法,我重点阐述方法2

1. 利用`burp`卡住进入后台的包不要放过去,然后就是去后台处点击,点击结束后再一个个放包,这样又可以测试未授权,但是效率比较慢,需要对功能逐个点击,2是有时候加载新的接口并没有出现在页面中
2. 卡住登录包,等待一下就会加载后台的`JS`然后熊猫头探测到接口 拿到这些后台接口就可以直接批量测试测试未授权了,下图是典型的后台页面,卡住后就不会发送重定向数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRWOvBI6qpEianvgTJyibmkiaMDleSrvg8ekkOribNvGicsep2uQqfG3HGHPqt9vyia8okdXs141eAL3ZYyeqKOdXD9p8ibgDQkoJdCy0/640?wx_fmt=png&from=appmsg)

**如果后台页面并不会一闪而过,开局登录框手动输入账户密码,然后拦截响应改为`ture` ,如果校验不合格会一瞬间进入后台,然后重定向.如果可行的就可以按第二种方法继续测试未授权, 微信公众号文章学习到的思路**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTibw1r2Ky242s38ShHCa5pRNSNf7Cg4PnT5D1vsX2xtvibyaia7dXLlIhRLvWIYnfkr908wbIzunK0rIvGXyp04qaaeQuTtq3Tia8/640?wx_fmt=png&from=appmsg)

#### `type`管理员类型参数

当我们编辑或者出现权限不对等的功能点,比如管理员 编辑者 创作者 查看者,类型不一致 靠数字绝对尝试修改类型参数,通过参数修改代替高权限的身份去操作

```
type:0// 查看者

type:1// 编辑者
```

#### 无权限`URL`添加资源后缀绕过

[微信案例](https://mp.weixin.qq.com/s?__biz=MzU5OTMxNjkxMA==&mid=2247486725&idx=1&sn=0c9a187ce2100c38161fbf4279afab7a&scene=21#wechat_redirect)

`URL`混淆漏洞是指服务器和解析`URL`时，由于不同组件或系统的解析规则不一致，攻击者可以利用这种不一致来绕过安全控制或获取敏感信息,对路径进行编码添加后缀的方式从而进行绕过

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSiaItRCUUydBDsvBfo8UicWo2wbFN86wmch9ISP3RLRf9zvrRicVLNo5GoGBU38qibMXGrE4ZibUoWtBV1Zqibx1YDVXJ8XudyYgVZM/640?wx_fmt=png&from=appmsg)

**正常接口无权限**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSRdtNemj9vylfpo2X3yCaeztBEwMKuOtbxbU21BgNSlX20omfRyiaqownCU9ZLj7ibInk1TCZ8CibfQ9Tr8mRLF94f4EVqMhiaCXY/640?wx_fmt=png&from=appmsg)

**对最后的接口后面添加混淆,利用字典去`Fuzz` 添加.`json`绕过,测试鉴权相关的漏洞时，可以尝试`url`混淆，接口多个位置`fuzz` 添加资源文件后缀**

```
/api/user ----&gt; 未授权403
/api/user.json/css/png --- 200 ok
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR88kicnV0ibTMwrQNicJT4qAaVqHO5UXAjBVm6VE1bcLRJ5YFO33FbicDNibJtxNCUCm9EwKPGSB9icicWjjTYmPeqCthfv2qaHY1HUM/640?wx_fmt=png&from=appmsg)

**资源文件绕过字典,一般遇到`403`可疑接口我都是利用`Onesacn`去帮我在接口不同位置拼接测试，在插件中设置好字典,有`403`接口就发过去跑,利用资源文件进行多个位置拼接**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSKG8ExU2e1J38H5WEuY374VQW8ZVxvgdWCcqxLdVMOkV2Kadg9BCWDxSokmU3XaW2icUXZqbaya0wrtRUmeeO2jv5OMwFYWM3A/640?wx_fmt=png&from=appmsg)

**如果出现状态码为`200`且字节长度很场很大概率又加载出了新东西,我们也就能测试更多地方**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQYzCnQkIBbbQcWHI6Nian6yCxATjbEQTfYPOgq1QWnG2XRvjja1icsTy9vsLyBxyWicauOJfKBnwibyMILFXY5h6OKYvicpH0TKNbA/640?wx_fmt=png&from=appmsg)

**资源文件字典**

```
%09%20%23%2e%2f/%2e////..;///..;//%20/%09/%00/.json/.css/.html/?/??/???/?testparam/#/#test//./////.//./~.;..;。;%09;%09..;%09..;;%2f..*.json../..;/?a.css?a.js?a.jpg?a.png../admin..%2f./.%2f..%00/..%0d/..%5c&amp;#@???\..\.\.././/;/.%2e/..\..%ff/%2e%2e%2f%3f?.css?.js%3f.css%3f.js%26%0a%0d%20%0d%0a%3b\.\
```

`BP`插件

https://github.com/0x727/BypassPro 也可以处理`403`接口

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSfuiapnPHSic7030KocecFCLdoCyXInLiaUMJ6PqhunROJibCgKum6w3OYN4oph0lbj1BC2fay24ribt5GMeNKUMYgibqicyrOP4X13g/640?wx_fmt=png&from=appmsg)

#### Vue框架带#未授权二次拼接

vue框架前置有`#` 注释 数据包是抓不到的,熊猫头找到的这一批接口无法直接在`bp`通过爆破器拼接,这个时候几个方法可以测试未授权

```
https://xxxxxxxxxx/rental/#/login/
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRIibdmoVLLiasgt46HicyoyZRlLJp1Z0N4PR0kHueADtuAkrrFX2As7ANjRhFkY4awI8cwOhsjNlgKmibZmwb5YGfaXwFKhJxRH4c/640?wx_fmt=png&from=appmsg)

**1.手动拼接如果出现有效可访问接口就可以**在有效接口的基础上再去看熊猫头加载的新接口得到新的接口再拼接未授权**,逐此反复**

```
https://xxxxxxxxxx/paypage/#/riskReport?transld=
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSt8HicdEFibJiar6RD8hPqNVicSFvjmDKJe1iaS45ibCtbmytqOXXlSMjPK1JGEnSWql5XSQHCIDNx6qxTaKxHo7yliaQXMic3mvjiceeE/640?wx_fmt=png&from=appmsg)

**2.`urlfind`扫描.注意看字节`size`大小 ,当字节变化代表加载到了不同的数据不同的`JS`就可以再用 熊猫头测到新的接口,注定看`urlFinde`的新的接口信息,然后在新的接口基础上又去看新的泄露接口二次拼接**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTxwhNFRsA5mJlC2zNE85gibkWibgD3ticPNrPQJ6EVM7Hkxv5kO6c16w8gJKtru8vorQFz9BEWicn7mKEiaYJjoxZOa4Lz48R60Lg0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSTZf8OY4gT0bckzezDhpGmml8D6uUt925QUR9V128PxyTaYicuHIxicpJ5DJvIibGAuiaMTEk2pBbpNX0IybLocgw3iciaXeSPWLPl8/640?wx_fmt=png&from=appmsg)

#### 前置接口共性

`/rebateBillSettlementList`接口出现在`BP`但是前置的接口`/api/gw/rent/rebateBillSettlementList`都没有见过,代表可能会以这个前置目录去拼接得到的`JS`接口,把找到的接口以这个目录为前置去爆破试试,有些时候不一定，都可以尝试;

所以说SRC最好是针对一家去挖掘,熟悉业务这个概念其实很模糊,新手常常疑问为什么要熟悉业务?不都是挖嘛,挖啥不是挖呢,我对于熟悉业务的理解是,理解开发代码的习惯,同一批站点会有很多相似的地方,Web和小程序如果是一套,那么假设一个可以登录注册一个只存在空白页面那么token是否可以替换?a站点普通用户权限b站点有管理员权限,那么接口调换一下呢,举一反三的概念,当然大佬可不惯着你上去就嘎嘎出高危,当我们还无法对漏洞信手拈来的时候能做的就是对每一个数据包做好分析，每一个思路做到记录并实践！久而久之出货只是时间问题

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTFTzGibB5VpBKsFE7YTPu8HvicqLNcHMSMCaesRH6ZOOIr0Oo618p7y3aWP0zN4ccm1ul2yzzzd25v5sjJxstywzJ1XDfYbYc84/640?wx_fmt=png&from=appmsg)

**如果经常对一场厂商挖掘可以继续下业务的接口,有时候会能多套系统部署同一个接口 `A`站点的接口可以给`B`站点使用,`A B`站点接口组合一下又会出现新的接口,得到更多的攻击面**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQrx0KNpmqf2uwciaPfOwIf6EwUSDamAzz2V4Y2da69bJ4sxZx7PpZ8clQ6QkUtibCr5f92yUtOlK5WCJb1b49kZlkMUb107yQ0M/640?wx_fmt=png&from=appmsg)

### 越权查询/操作

#### 各类功能点越权

[任何交互处都可能存在越权](https://mp.weixin.qq.com/s?__biz=Mzg2NDY2MTQ1OQ==&mid=2247515579&idx=1&sn=469e69bc8273677d3762af563592852f&scene=21#wechat_redirect)

#### 查询信息日历接口

查询的还是需要测试`XSS`或者其他的查看响应包是否有回显这种,使用`%`测试通配符注入这些

深度挖掘 所有能点的地方全点开看

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRf9SSJk6zHDnicEY7yke41FRykoMHYFt6OClv0BnnyzPpuze0AiazzribLggvnpNqPkyXDok8alkDficfibA2EYFKjGjCdibAaC5...