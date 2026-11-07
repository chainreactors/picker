---
title: 【安全圈】隐形后门寄生 CWP 面板，访问日志全程沉默
url: https://mp.weixin.qq.com/s/p7vACUuTInVAxChYd28e_Q
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:57:46.130014
---

# 【安全圈】隐形后门寄生 CWP 面板，访问日志全程沉默

# 【安全圈】隐形后门寄生 CWP 面板，访问日志全程沉默

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

后门

攻击指令藏在带签名的 HTTP 请求头里，执行完不留一行访问日志。奇安信 XLab 本周披露了一个寄生在 Control Web Panel（CWP）服务器组件里的后门，取名 **cwpdoor**——它不是新增文件，而是面板 Web 服务器程序 cwpsrv 本身，被重新编译后塞进了私货

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyEib676xg6ULNdzicOvfLP9BDd0oD3jjQImS1NQjex1HC89Kko56kTQwYx8MibeTedD7M2lv5glFEia3aYthMeicuTCiazMZOiaeaTxqU/640?wx_fmt=other&from=appmsg)

## 🔍 后门本体：重编译的 cwpsrv

CWP 是管理 Linux 主机的免费面板，cwpsrv 是它的 Web 服务组件。cwpdoor 就藏在这个二进制里，平时行为与原版几乎一致，触发靠一套自定义请求头：请求携带有效时间戳与签名、且头名以 X-Ngx-Integrity 开头时，cwpsrv 执行请求中携带的命令。命令执行与通信走 Unix socket ngx\_http\_integrity\_helper，**访问日志里没有任何记录**

> 安装后门需要 root 权限——攻击者执行安装器之前已经控制了服务器。他们最初怎么进来的，XLab 至今没有答案

## 📦 安装器：伪装成版本更新的 shell 脚本

XLab 6 月 29 日捕获安装器 cwpsrv\_update.sh——一个伪装成版本更新的 shell 脚本。它只覆盖两个版本的 cwpsrv：1.15.10 与 1.24.0

换件手法相当小心：替换 cwpsrv 文件后把时间戳改回原值，ls 与 stat 检查看不出变化；样本在 VirusTotal 上 63 个引擎**零检出**

9 月 30 日，一份含后门的压缩包从巴西上传至 VirusTotal，XLab 据此判断"野外已有真实受害者"，但没有给出受感染服务器数量。同一份压缩包里还躺着 Ebury——一个自 2009 年活跃至今的 OpenSSH 后门兼凭据窃取器。两者是否同源，研究员表示无法确认，也可能是不同攻击者先后驻留在同一台服务器上

## ⚠️ 三条命令自查

XLab 给出的排查路径很直接：

* `ss -axp | grep integrity`

  ——出现 ngx\_http\_integrity\_helper 这个 Unix socket 即为中招信号
* `ps aux | grep cwpsrv`

  ——排查 cwpsrv 拉起的异常 helper 进程
* `strings /usr/local/cwpsrv/bin/cwpsrv | grep X-Ngx-Integrity`

  ——在二进制里搜后门的头名字符串

在研究员的示例里，目标服务器开放端口一切正常，靠 socket 检查才把后门揪出来

## 🎯 中招之后怎么清

* ① 用安装器留在 /usr/local/cwpsrv/bin 的 cwpsrv.prev-\* 备份恢复原文件。注意安装器换件成功后会清理临时文件与备份，这份副本可能已经不在
* ② 升级到最新版本，再确认 `ss -axp | grep integrity` 无任何输出
* ③ 更换全部面板凭据。后门能执行任意命令，整台服务器按失陷对待，同步排查其他威胁

## 📌 IOC 清单

* MD5 `e505d4ffa21cf494a5dc2d7c8f4f1236`（安装脚本 cwpsrv\_update.sh）
* MD5 `965aea67fb40de1bab5169ada993349f`（后门版 cwpsrv 1.15.10）
* MD5 `d3f4e95113d49ab3991b45e457bda75b`（后门版 cwpsrv 1.24.0）
* IP `136.0.141[.]71`（下载服务器）
* URL `https://136.0.141[.]71/static/cwpsrv_update.sh` 及同目录下的 cwpsrv\_1.15.10、cwpsrv\_1.24.0

***END***

阅读推荐

[【安全圈】白宫专网被卖做代理？总统办公室设备疑遭植入后门](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079711&idx=1&sn=05bdbc8ba75d9805145596493772fbf6&scene=21#wechat_redirect)

[【安全圈】潜伏近三个月！DreamHost漏洞致大量主机凭据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079711&idx=2&sn=63979c6dc888fb4e4dbc4da49a266ae8&scene=21#wechat_redirect)

[【安全圈】币安63亿被盗余震！Coinbase转超99%资产至冷钱包](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079711&idx=3&sn=b21a981adb4002765fad3dad5018fe73&scene=21#wechat_redirect)

[【安全圈】9.8分Linux内核高危RCE！无需认证隔空打穿](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079699&idx=1&sn=dfbd72f6698a155131d20cada69f5589&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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