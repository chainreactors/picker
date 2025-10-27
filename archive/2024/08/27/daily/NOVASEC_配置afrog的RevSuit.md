---
title: 配置afrog的RevSuit
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247489680&idx=1&sn=e813d5f3dc38e2b379c574b91a34a149&chksm=fad4c587cda34c9172943597b0e76caae53de09998f604e1fff916289051a05acb9c83f636f8&scene=58&subscene=0#rd
source: NOVASEC
date: 2024-08-27
fetch_date: 2025-10-06T18:06:38.728046
---

# 配置afrog的RevSuit

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/toroKEibicmZDtI4uEXpW0KrPpkRnDALtTmQC0X5pa32HZSlibF6WicFg1Lmof39ozVYo4QbWrUxOg22WeFPRhpWhA/0?wx_fmt=jpeg)

# 配置afrog的RevSuit

原创

酒零

NOVASEC

## 0、预备资源

```
公网VPS：6.6.6.6  [假设]域名DNS：yourdns.com  [假设]
```

## **1、配置DNS域名解析**

```
新建 A 记录：logns.yourdns.com 指向VPS公网IP 6.6.6.6新建NS记录：log.yourdns.com指向上一步配置的域名logns.yourdns.com
```

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDtI4uEXpW0KrPpkRnDALtT7091rEOqgWGKxkjcw4e9bMSSibX8no7hrrlXp6XMI6ibOALxd2SibWibXw/640?wx_fmt=png)

解释：

使用 logdns.yourdns.com (IP 6.6.6.6)作为 域名log.yourdns.com的DNS服务器。

所有对域名log.yourdns.com的dns查询，都会在logdns.yourdns.com (IP 6.6.6.6)的53端口被监听。

注：本次使用cloudflare接管DNS解析配置功能。

注：logdns子域名是可以自定义的,后续没有用到,可以任意修改.

注：log子域名是可以自定义的，修改的话需要后续同步修改配置中的log字段.

注：开启cloudflare的CDN功能不影响功能使用

## **2、下载测试revsuit可执行程序：**

```
应用主页：https://github.com/Li4n0/revsuit    下载测试：curl -L -O https://github.com/Li4n0/revsuit/releases/download/v0.7.1/revsuit_linux_amd64chmod +x revsuit_linux_amd64./revsuit_linux_amd64
```

注：初次运行会生成 config.yaml文件

注：如果提示so文件缺失，请参考readme的源码安装方案。

## **3、简单修改revsuit config.yaml**

```
config.yaml内容：注：以下配置仅启用HTTP和DNS功能+++++++++++++++++++++++++++++++++++++version: 1.5addr: :80                      # 必须 指定HTTP请求端口token: 自定义Token             # 必须 指定HTTP请求TOKendomains: [log.yourdns.com]     # 必须 指定DNS请求域名external_ip:admin_path_prefix: "/helplog"  #自定义API请求目录 默认是/revsuit    database: revsuit.dblog_level: infocheck_upgrade: false           ip_location_database:  database: "qqwry"                # qqwry or geoip.  geo_license_key: ""               # Mandatory field, if you choose to use GeoIP.           http:  ip_header:dns:  enable: true                                     # 必须 开启DNS查询监听功能  addr: :53++++++++++++++++++++++++++++++++++++++
```

## **4、使用config.yaml启动revsuit**

```
后台运行：nohup ./revsuit &
管理地址：http://6.6.6.6:80/helplog/admin
注：管理地址中的端口:80 和 路径/helplog 取决于config.yaml配置
```

## **5、编写提取规则**

##

## 启动revsuit服务器后默认还没不支持提取请求内容，需要配置提取规则.

提取规则可以手动填写，或者直接导入导出以前的配置规则

###

### **手动添加HTTPlog提取规则**

```
访问HTTP Rules配置页 -> 点击 +New Rule填写 Name (规则名称)   http填写 Flag Format (规则提取正则)   /log/(.*)点击 submit提交保存
注：规则含义为提取 http://6.6.6.6:80/log/ 后的所有数据作为http记录
```

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDtI4uEXpW0KrPpkRnDALtTzYn1xicWHlRR0dZbEv6zbdMAd3W2pBTsT14hdy9cOpHJ4JouEvEzkkg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDtI4uEXpW0KrPpkRnDALtTueEzobKrNyKV93Px7N1vOjzficcNPicCqMNPSuiaKn0aIgPiczmoRl99lQ/640?wx_fmt=png)

### **手动添加DnsLog提取规则**

```
访问DNS Rules配置页 -> 点击 +New Rule           填写 Name (规则名称)   dns    填写 Flag Format (规则提取正则)   (.*).log填写 Value 域名响应内容 8.8.8.8  （可随意配置）点击 submit提交保存
注：规则含义为提取 log.yourdns.com 前的所有数据作为dns记录
```

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDtI4uEXpW0KrPpkRnDALtTmMUhDTv5KLicS2cTicEHmAJzpEUrpf3LyhNBzrtdb5Hicd0jXGC18zS2Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDtI4uEXpW0KrPpkRnDALtTTianCAvIxOgux2Y4hvcEbd3vWmandDF8OxxoSyic2TZbzLcmicqK6y06w/640?wx_fmt=png)

### 导出和导入配置规则配置

在Setting面板 -> RULES 子面板可以导入导出已配置的revsuit规则

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDtI4uEXpW0KrPpkRnDALtTM3zs1mCkkERBW6WiawbDO8NqaFzau9077RFuQUxML3B7zrjvTX8Y07Q/640?wx_fmt=png)

## **6、afrog配置使用**

afrog v3.0.7及之后版本支持联动 revsuit进行OOB检测

afrog-config.yaml  revsuit配置项介绍：

```
revsuit:      token:密钥（参考 revsuit 教程）  dns_domain: 记录 dns log 的域名  http_url: 记录 http log 的 url  api_url: revsuit 的验证接口（参考 revsuit 教程
```

本教程的afrog revsuit配置项：

```
revsuit:  token: 自定义Token  dns_domain: log.yourdomain.com  http_url: http://6.6.6.6:80/log/  api_url: http://6.6.6.6:80/helplog
```

afrog-config.yaml配置参考：

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDtI4uEXpW0KrPpkRnDALtTBcYdMLNdoYqMjc6bqzj92Lq55oiaOibHjIialrFnpoKn20MSXibGibOn3dw/640?wx_fmt=png)

注：http\_url中的/log/目录是由HTTP提取规则所限定的,如需修改,请同步修改HTTP规则

注：dns\_domain中的log子域名是由DNS提取规则所限定的,如需修改,请同步修改DNS提取规则和DNS解析域名。

预览时标签不可点

个人观点，仅供参考

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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