---
title: Dozer2026招新赛WP
url: https://mp.weixin.qq.com/s/WcUZev4L-MhiuDZqMel0zg
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T06:58:01.527193
---

# Dozer2026招新赛WP

# Dozer2026招新赛WP

瞌睡虫小k
瞌睡虫小k

瞌睡虫小K

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBN8osDByCFiauva69kIUYdrEEY0HZfhKexpkoUVYx0ErsWgHq6OnduaiaeUUxAOaS5NAd7vlohrajaDt6pZ2DU116z7ibQkvB97zes/640?wx_fmt=png&from=appmsg)

**点击蓝字 关注我们**

**Let's go!**

# Web

## cubes2048

F12查看源码，发现提示

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBN8yuMSwX3FyVSnSmsDibOGaCRFiaG1xyKzYCVBKKo487Kzd9RIfsWdpyYKWedBRzoSicSzcaNBWg6NSfdcn3ma3p551u1PmkWedVs/640?wx_fmt=png&from=appmsg)

/robots.txt,发现Disallow，即不允许爬虫访问的URL，访问它试试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNicu5EcOiciateicssHCzf1pzSQ3JcJZHTDojQfXfTicFACRfZKUr1e8SrsztJuFjlzS0PRb2tTpbTxJibQXlwN4hWIaFdlxpf4TteY0/640?wx_fmt=png&from=appmsg)

跳转出php代码页面，进行代码审计

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBN8Omfribrib4IkAnl26KqnKFRK3WnibQmcg9tt4R0sYPFybF81SZQbqNlOyy53uicmPFA5acE8zD5T5rZCQ1qbGR6R9uDJhEkM7aQg/640?wx_fmt=png&from=appmsg)

WAF 校验：正则匹配原始字符串里是否包含`score`或`flag`（大小写不敏感），匹配到直接拦截

`parse_str`就是进行自动 URL 解码

`$params['score']`强转为 int，大于等于 65536 就输出 flag

所以我们就是要传入score参数，并对它进行url编码绕过waf，最后赋值大于等于 65536即可拿到flag

s→ `%73` c→ `%63` o→ `%6F` r→ `%72` e→ `%65`

**payload： ?%73%63%6F%72%65=65536**

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBN9tu2Ms2ibSoGfC7FDpokuzy6d1ZXsPHBghsmfjuFibdZqHMbn0mvOBZDVpibhQiauIYRYxwagA0ckl2hrGvlBRndV8yl8u7J2U6aM/640?wx_fmt=png&from=appmsg)

## 你的婚礼

首先发现2个链接，打开都是`/index.php?file=某个文件名`，这是文件包含的典型入口，后端多半会拿 `file` 去 `include`

根据hint.php和爬虫协议的内容可以确定，目标文件是your\_wedding，航母掉头说明要`../`,意思是：**往上退一层目录，**这里就是考查最简单的路径穿越，也叫目录遍历，意思是：**你让程序去读/写某个文件时，它以为你还在指定目录里，其实你用路径把访问位置带出了这个目录。**

接下来尝试构造payload

|  |  |  |
| --- | --- | --- |
| 传 | 结果 | 说明 |
| file=hint.php | 正常出草稿 | 白名单里的合法值 |
| file=notice.php | 正常出须知 | 另一个合法值 |
| file=your\_wedding | 此人不在名单上 | 文件名对，但不让包含 |
| file=../../your\_wedding | 此人不在名单上 | 直接穿越被挡 |
| file=php://filter/convert.base64-encode/resource=index.php | 此人不在名单上 | 伪协议被挡，读不到源码 |
| 直接访问 /your\_wedding | 404 | flag 不在 web 根 |

根据题目描述提示：**尤咏慈?我来接你放学了。系统觉得问号后面是情话，核对时只看名字。**

以及学校须知中：**不在名单上的收件人，系统会直接拒投**

可知，这是一道黑盒文件包含，有白名单

测试一下`hint.php?随便写`，发现不再报此人不在名单上，说明?有一个截断的作用，系统只认?前面的hint.php，因此就可以通过。同理，`notice.php`也可以通过，这俩都是白名单

所以，路径穿越就可以用`hint.php?`或`notice.php?`当一个假目录名从而绕过waf，最后用`../`一层层退出来直到读取到your\_wedding为止，就可以拿到flag

**payload：****`?file=hint.php?/../../../../your_wedding`**

## 我想当管理员

##

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBN9gjkR9UUlCJeahN5uWYyVianUTg2tjBeqZnb78DYNAxGeiaqzxN4kd5mCx8XGFV44t3oRRaOVeFGFicJmp6qpI5GQcKiahDcJBkAs/640?wx_fmt=png&from=appmsg)

F12一下，发现有注释提示，和session有关

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNibSdqDnvkZ5szOPRgNBFhkIPveJC4FglcgCxs3aldy8Tq5SfsONFolFHLg7PAn9FMSdYVcSlg22gcKb6AjzmsdPnMN3ibLB0kdA/640?wx_fmt=png&from=appmsg)

session值在cookie中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBN96nXqC9Q1IZjvGDKF0IiaGvjBVibcRT0ZJhlDFLHqCGdR8mzJ91ejss4ic6iaPejGlOicB8ibqJurL6YvdwViah3icBdB5ALjUNq0sfeI/640?wx_fmt=png&from=appmsg)

用hackerbar把guest修改成admin即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNib3sQe2Ek3ictRTgibs6DtkyHnfm7iaTXtIvv8kjbpdjPibMx1Beyv0njc9cCvpHuLCEYaMADlb1wnmdC1VlnxnlCwI93t4UT0mric8/640?wx_fmt=png&from=appmsg)

## 七锁通牒

### 第一关：get传参

很明显的提示是get传参，参数名和参数值都给了

Payload

```
?pass=moonlit-route
```

##

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBNibGoshBicHsrml7rv4bnKBUwUZINrqI3ShaqfEaIZhgB9bHWgONOYIwaibcc7icXBgobz585RzYH2u3Zmxe6icg6GaTRAggI5vj7G8/640?wx_fmt=png&from=appmsg)

得到的碎片是

```
RG96ZXJ7Z
```

### 第二关：POST传参

###

这一关其实出简单了，只需要把参数放在提交框中就有了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNicPtPEbVrLNKau7kibRc8FicHYlkeuNictcarsazI4AY6T2frIRSAk7VGJJ9icgWwtPSLundickdXwawELmMh1XHAMaRkyELortSk9w/640?wx_fmt=png&from=appmsg)

但其实是想要利用POST传参

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNibeHibKgPexwZmRscibIgWWhia4wB4x4vJ2ibNBzGHCViclcxf6QtduSAV3rckDZ8tVCaNarAHRLUJo64IQgUfkm1DndLxF2ib7fMY8Q/640?wx_fmt=png&from=appmsg)

Payload

```
```
seal=vermillion
```
```

碎片

```
```
WE3OTQyYz
```
```

### 第三关：回环地址

###

看到题目描述是这一关考的是本地回环地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNib8IPvvZGQrR9VTkeFLZpia3MlbEvj1GNPblz14ZQE8hy29wj9xvjn7JUybPr8B6dIr34lB4G6NaW80IazK9jeLX8syicSZS3zzY/640?wx_fmt=png&from=appmsg)

题目描述中写了“驿史只录本地之宾”，那就需要本地回环地址，利用XFF头上传

Payload

```
```
X-Forwarded-For: 127.0.0.1
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBN9PTkMTKBTnNicgp0YPRiamLtMIubvoIic31DhyfzszVjG90icTlbmNia8DjFZ3MUUiaGicTlBlYgVfznuI8B8VicEHy2NsMWY8s7VMGgE/640?wx_fmt=png&from=appmsg)

碎片

```
```
ctN2U2Yi0
```
```

### 第四关：UA头伪造

###

User-Agent请求头为CourierBrowser

Payload

```
```
User-Agent: CourierBrowser
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBN8siaQYHXnBp8R2qPdqG55F1VC2ibxMBmsTWkH7ypnzq1PNk60XiaVySeUeicpFWaGSveZ2MdeTj8BELt47vIMcHNIDLJCuPvwN8VI/640?wx_fmt=png&from=appmsg)

碎片

```
```
0YjkyLWI0
```
```

### 第五关：cookie身份伪造

题目提示“身份role为admin才能通行”，那就是要修改Cookie参数role，改为admin

```
```
Cookie: role=admin
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBN89ztMp5Aj87WnlIBuutQ3qN3PmiaCc8qPF5GfJ9JicWUibCLAyPjoFV5ZoN60mPJg5ouYl7XuiadsGwOFiaOENmMKHubWttepqse5M/640?wx_fmt=png&from=appmsg)

碎片

```
```
NGItNzBk
```
```

### 第六关：伪造请求头

###

Referer为http://huiyindian.com

```
```
Referer: http://huiyindian.com
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNicxRx1yeafZzOpDNfiaf7Iy0TVMex5ibQD0dLZtSWp4v6BaFVjYiclSLUQ5VjQSQ2VH99MAmiavZyOWkgAXkRNhLCXEyiaiaA7vdWs2Q/640?wx_fmt=png&from=appmsg)

```
```
ZGZiODY4
```

###
```

第七关：PUT请求

使用PUT请求方法，请求体内容为token=final-permit，利用bp构造请求包

Payload

```
```
token=final-permit
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBN9xXmYu5TBToMy20459UESKxljiabUtyxMwz0jVjffD54xQMCeibJ9bwj8gwW5rKaKfM04PcRRSk1atflwpKWbNMtxvX7OZlnq6w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBN9ozqmbRkCOAUHQYZef6O7frBEn64tqCTArsmDtOw1l1VJwmgIwbldP89Qic5yq2CFxWsLKKMhSpKMoA5a7uylctic2GV9CEM3eA/640?wx_fmt=png&from=appmsg)

碎片

```
```
N2NlfQ==
```
```

最后将所有碎片结合起来利用base

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBN8ZiaVAvH5PYGZDDqo8Pn1lwYlBlGkhpTImWWXt2LhRM7GdEtsSBpNpN7rWx1Wx6PyOPvJw0GNQRP75icKlLaU0OzwTdnicvHTIKY/640?wx_fmt=png&from=appmsg)

## ez\_upload

一开始是一个登录界面，说是管理员才可以登录，但是密码不知道，首先最常见的就是尝试弱口令爆破

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBN8MMpibcmnicDywT1N4RT64GrGauz5DdNfqLW4kZGhNCnEGwZv2YnH3RA8xNHWs7RgmzPUQtg0HiaGfFPuoBRG5561XcSk9Kvrv08/640?wx_fmt=png&from=appmsg)

利用bp抓包尝试爆破

开启拦截，在输入框中输入内容点击登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBN9vTHD2ibqO5ZR52ZH7DZxFUiciaYeMGlfOE52SOic38Rq6MujI9qyx4ic3rBnPibrYtibDl99q2W5YeaAGEuichsDxY4V0vXrltNibX3mw/640?wx_fmt=png&from=appmsg)

抓包成功，右击发送到重放器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNicy5Q9rH0PDTaBTfnjxvGZ1dTyOlbM1PWRon9WSuwUibBqBcYhdibicdvhdSyt5ZCkaSgl8CuDKVTXHdMVOhcIPvM0ko5ZrjE3IB4/640?wx_fmt=png&from=appmsg)

在重放器这里就可以看到请求包和响应包，可以发现是POST传参，参数是username和password

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNicjXciawdHWWNP1mKNLw2FxyGXxDHNw3X0RSVBqmrnEr4hnljEVb99tYIT2yCmN7Y2v7L9iaj2B50YU4FMFtS5IlmJVwp6ia95GFc/640?wx_fmt=png&from=appmsg)

因为已经知道是管理员账号了，所以只需要对password参数进行爆破，右击发送到攻击器

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBN9zibxPHTx1CZJWozBgXKhJ8EVoCIXghsKY7kKOu5faHibBic91L1Sbs9jiaSGmibJ730bicG8bpFC3wwr6XWGlWvtzLqOpg0fTOznDU/640?wx_fmt=png&from=appmsg)

选择“Sniper”攻击，添加password的payload，导入自己的密码字典，点击开始攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cg61RPYibBNicKn2Xyia8uzrLC18Y9dAXick7RLKCHpH6QuibWXMWP40knVoV3ykPibftpr4IlT6O8gpSaEJKrRQWuHF9QuXAkczJCia86zBaZiaJW4/640?wx_fmt=png&from=appmsg)

字典爆破的判断一般是通过长度或者状态码判断的，这里状态码都是200，那就看长度，但是长度也几乎一样，说明这份字典里面没有我们的密码

这时候就要看到题目描述，"情报已经泄露，我们的行动暴露了"，提到了情报泄露，就可以想到可能有信息泄露，访问一些常见的泄露文件比如www.zip

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBNib8apGwwVn3t2OGiaD3FdeZEh4Ggq5IqIPQ6d5nvCQR2RiaK49QYYHqcARI7eiaxAwCTxP9xkHrar2JibS0NMhwyJ6w1szP1aobtXM/640?wx_fmt=png&from=appmsg)

发现可以下载到一个压缩包文件，解压缩发现里面是password，也就是出题人提供的密码字典

![](https://mmbiz.qpic.cn/mmbiz_png/cg61RPYibBNibT7rV6mZXPDd7Z9Fz1v8DPrcb6ODXzCewfZF7r97Awialju4Z0ticFrOuhaz0z55Ck0loLwJea3tKhuKeffOKtS6FyN0DIq9gSY/640?wx_fmt=png&from=appmsg)

那就用这个字典尝试爆破，清空...