---
title: fscan免杀研究，过国内所有最新版杀软以及Defender
url: https://mp.weixin.qq.com/s/ImVANdkjqg6UQtlb7r0pUw
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:59:00.187072
---

# fscan免杀研究，过国内所有最新版杀软以及Defender

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfO6RfcA0HL4I4UZeJJicMiafkwzJjzY3JOdkktXTR1ibKwAH8eEtoUjmueR4yY8JEG49kf4ibc6CEOJXOCGllSbjG7lQcVpCx9VkjA/0?wx_fmt=jpeg)

# fscan免杀研究，过国内所有最新版杀软以及Defender

原创

仙草里没有草噜丶
仙草里没有草噜丶

泷羽Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

先来看看效果，当前fscan版本为2.1.3，github最新版，上周发布的，

`https://github.com/shadow1ng/fscan/`

![image-20260521194955437](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfOUDGvwyzvmVDLJ6L1aiaMk1WicUUfP8ESEOBIfqVDE3cEW6RTcKrb90iaclcZr3GtoLNvX58K7doDWBI1QwgnV3hZLmI5qoViaDdg/640?wx_fmt=other&from=appmsg)

image-20260521194955437

![image-20260521194543031](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfMWDntEO2yOxj5uGib5thmsSs8JibzyABX04QJpGQwKzHmQramCv0ia7QwLR3BDDjicCbnJH4VQr9N0ZUIiap5Bpr1n2okz3VOPvTFE/640?wx_fmt=other&from=appmsg)

image-20260521194543031

![image-20260521193627111](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfO75ickfB51zkSakSia5MyJ1Kl0HYUHficpHD7d2IZs77VVzKSvlTmI64NylwGsSHW0YQJ5MoSw8z1ciadWBwvTOmibRL5TrdCWBkPA/640?wx_fmt=other&from=appmsg)

image-20260521193627111

设置好代理

```
$env:GO111MODULE = "on"
$env:GOPROXY = " https://goproxy.cn ,direct"
```

编译方法

```
go build -ldflags="-s -w" -trimpath main.go
```

## 1、特征替换

比如

![image-20260521142456571](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPhibvcZ2kq5a6Xjeo8MtravXdabKFDRTHhHsVO9RIia3ZUia8qkV0IpQcka6U2qiayAuXLOmpEz4aw1ickxicJeibqRR3DCX0pGlhuBA/640?wx_fmt=other&from=appmsg)

image-20260521142456571

改！

![image-20260521142913020](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPeDIasOI3oxCgria7napOkWz3hic29HXzrcJPT3ynNXb9wicOdia9y7I37lp2q0WmcmiaPGDFiaXcicHHLiacalKS1TpzvXInpUbzdI1o/640?wx_fmt=other&from=appmsg)

image-20260521142913020

windows下的批量替换脚本

```
Get-ChildItem -Recurse -Filter "*.go" | ForEach-Object {
    (Get-Content $_.FullName) -replace 'github.com/shadow1ng/fscan', 'xiaoyu' | Set-Content $_.FullName
}
```

## 2、版本信息

在flag.go中能找到这些信息

![image-20260521144125973](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfP599OCD4ibFOprkvjhwjibXqKGDRtq22xfUPYxmibKGuaoH0eg6EhicYKpaeljaibCrcpBot2sRyVEcaYc3SWOYEUJUe8OFa28b1dM/640?wx_fmt=other&from=appmsg)

image-20260521144125973

改！

![image-20260521144205849](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfPtvXaqs7GHZdYbbaIeZRlIs4zfdk0kABElwHZOpDsicdj7A6Br1GhrUjgnqafrWKib8RTfPlY7phP8HYl9oTuvxP0OwZRgqCadk/640?wx_fmt=other&from=appmsg)

image-20260521144205849

## 3、清除残留字符

`commin/logger.go`

改！

![image-20260521144932748](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMj6Cn3IGxPoRLWqy2ztBkeib7M2e1aXvHGQsqibALeNdpJ5bOMvNia2WwnYPloicibEiciatZkdIcTBVSxk4OCskgia3TTILoyqLfNFX0/640?wx_fmt=other&from=appmsg)

image-20260521144932748

`core/port_scan.go` 修改 PE 头信息

![image-20260521145158954](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfN8qNuibSm0JgyhLoDibP4MD7ziaVZlbJsnDaDaKa2iauqJm8Eo5uFLQPTUxqWVSK1SliaIqMQIMfHSicU85lNaaQpYwhpzATAMap77o/640?wx_fmt=other&from=appmsg)

image-20260521145158954

`core/web_scanner.go`

改！

![image-20260521145317714](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfNhiaXHtGoPA37HxU5DBcrwK80f0q8R6icMk84ybOMLb6p0RlibsRxjKlbbDsnAIf85SdWWTCLJKcCyLxFmEgmWegXfyXYPpSlS9U/640?wx_fmt=other&from=appmsg)

image-20260521145317714

`web/api/result.go`

改！

![image-20260521153132295](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfNKnib4WAEicnmTgiaSQVAyNr7v0xbsq9qS2GU9dwYz6ibaOc5uyN4z9o62bB4icYiaxhJJfXzE2eo38KLMlZGvQeUuS0gR8rSHk3VtE/640?wx_fmt=other&from=appmsg)

image-20260521153132295

## 4、修改banner

同样的也在flag.go中

![image-20260521144338786](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfOOGUlIr5eAqp0bvyxgHThdCH94fu7iavgPCra08jOANibz3rGZN6ibz6ka5bZvO1QzaXoWrgr8Lju58SpENHTicPFP0aX9icaapbYw/640?wx_fmt=other&from=appmsg)

image-20260521144338786

改！

![image-20260521150054601](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMCXGECcWfs4zGC5BJHIlO2LaqzDyFDL51I8Fdgu73cs0xvNUIfAKaWysTRexykhtx9spDvVl895brickI56NXPHEVddw4MdWBI/640?wx_fmt=other&from=appmsg)

image-20260521150054601

## 5、打包

`go.mod`最上面一行，否则会导致编译不成功，改！

![image-20260521145834339](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPjstyQX281XcVGbzerbDiayenW0Zj9C2AlmVc1yCkKVTmxLO03sh5HY8zm7FhMZqb1sS6NKUtTv88cptTA5eegHEiaFOJicSPqmQ/640?wx_fmt=other&from=appmsg)

image-20260521145834339

打包

```
go build -ldflags="-s -w" -trimpath main.go
```

火绒被杀

![image-20260521150448495](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMAeU9gpkKBoIL4TO4IHoia3erhZHTg7gdkZXXgU5CLT2ILYhHEMmXlDHe6sdPKKLBwOKj759Q1rYSLZmfUh99r8PicGOrBJSXiaQ/640?wx_fmt=other&from=appmsg)

image-20260521150448495

换一种打包方案

```
$env:GOOS="windows"; $env:GOARCH="amd64"; go build -ldflags="-s -w" -trimpath main.go
```

还是被火绒杀掉

无窗口模式

```
go build -ldflags="-s -w -H=windowsgui" -trimpath -o fscan_no_window.exe main.go
```

还是被杀

## 6、加壳

![image-20260521151014244](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMU1Rqs7wwn4CT29vHKYNyU0xYUWJDibJWOZAVYDRlBy9u0fhiaTeWP36ictklrwEK0s3SOqrLLia0BiclFA6grAGvDkTS68wuE6ibicA/640?wx_fmt=other&from=appmsg)

image-20260521151014244

被杀

## 7、安装garble

```
go env -w GOPROXY=https://goproxy.cn,direct
go install mvdan.cc/garble@latest
go mod tidy
```

garble基础混淆，被杀

```
go run mvdan.cc/garble@latest -seed=random build -ldflags="-s -w" -trimpath -o xiaoyu.exe .
```

garble 加上 `-literals` 字符串加密，被杀

```
go run mvdan.cc/garble@latest -seed=random -literals build -o xiaoyu.exe main.go
```

其他免杀操作，比如添加大量无用代码/虚假函数/变量/结构体，改变变量名称，添加大量虚假运算、控制流、数据结构，添加虚假网络操作，反调试技术，DLL等等

我有一刀，可斩宇宙！[狗头]

![文章配图-2](https://mmbiz.qpic.cn/mmbiz_gif/1E8ULvdwpfPVkUkPRB2UUkCZNOk77MzeMTbBHPf8wXYrXOEcpUGDibHLbYecyeO2e5fXyjyzjBFy2Oaia9pyStBhJwmcqEvEujsER5rG5o99I/640?wx_fmt=gif&from=appmsg)

文章配图-2

![image-20260521181018679](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfP39VqeDibjpZzpLINZOnQibicCQ9iasWaGMibeCE3As0emBKTVL2x1ufUJdocUaU7J2AHuShA8H9KRAmM0MPw9fnuCb0s5BM6384Ys/640?wx_fmt=other&from=appmsg)

image-20260521181018679

![image-20260521180916173](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfPDHPsTeVkfPQn3LMJZn1NXY05pEgDJkE7ticM7dvMjgl3pzLeVmDJIembHBOJia48c6VFuJgJ3dNicdg1ktpKVTI3V1GSwZNuI90/640?wx_fmt=other&from=appmsg)

image-20260521180916173

360防护引擎全开

![image-20260521204116137](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfMu4kLapvTS4eXHjLsXn6EC08Mer9s57D6DtHv3JmB3IRFbk2td3p7lVGMibMqA7Ich4pSqU0tvEtyQ7ZcOaWNFGmiaFGswmORvQ/640?wx_fmt=other&from=appmsg)

image-20260521204116137

![image-20260521204319824](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfP7G9JCELmE8RS7ibNgjrI61oscAe6GxvpXdxJSDibEoNVa2FCpwUwlNgWgBkaEf17l229qYSiaejcpeJIbnD4jBVDkvYlcRBeGxs/640?wx_fmt=other&from=appmsg)

image-20260521204319824

本地执行一切正常没有被杀

![image-20260521181236517](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfOdrhok3sW8VOPRfhetS2u5lJIsI583fOBjgzMeQH1uf2Ysxp3O2ia5whCVmu4mBEWRmicFm96WDgQicI4dpnxbDr6Z74B1aYAHxg/640?wx_fmt=other&from=appmsg)

image-20260521181236517

火绒内存查杀全开

![image-20260521204447479](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfO3e8XZR1lo5nibCRkU33vOSsow69UPRmWW15LuiaZOg6I8ClxyR4lSSOBYxCG030853xTXvHsicBfUymHtz8OVw741fB3W4zzlwY/640?wx_fmt=other&from=appmsg)

image-20260521204447479

windows安全中心

![image-20260521193627111](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfO8cueQM9y816EUyKed19OpUJBrGEdPSvadZeEqWPPvw9HzRRAMd5UHVpTGrEP7PTAric6cvc0t25ChzG2Uym6FO0FCbtibFiavJY/640?wx_fmt=other&from=appmsg)

image-20260521193627111

分析时间，2026年5月21日，晚18点55分

![image-20260521200044714](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfMITEricSULibRQyrP6TzmhUicmiaXEk1oQtyhFZjYz7J0Nue7KBlmtL99llskALc9OhTYvHnFibVlcadDSpOFTkzc72V6ynIWf76QE/640?wx_fmt=other&from=appmsg)

image-20260521200044714

> 白小羽
>
> 注：因部分人原因，本文仅提供免杀学习参考，不分享任何文中所使用到的工具，小羽我技术菜，工具过不了卡巴，就别喷了

## 往期推荐

[WxProbe，一款自研的公众号敏感信息收集工具](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247512630&idx=1&sn=2332c0a83ea2f5b8f2f35969e018c98a&scene=21#wechat_redirect)

[真！2026最新sqlmap汉化版，教学必用！](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247512723&idx=1&sn=e3f1dde3751072c0705475e124c8dcf5&scene=21#wechat_redirect)

[MemShellParty 一款主流 Web 中间件内存马生成工具](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247512581&idx=1&sn=7e62a9bfb5764e3bea0df154120e40f4&scene=21#wechat_redirect)

[HVV在即，红队高频面试题【WAF 绕过】](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247512558&idx=1&sn=...