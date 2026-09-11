---
title: 紧急安全预警｜ArangoDB曝两枚严重漏洞，未认证攻击者可通过漏洞链实现Root级RCE
url: https://mp.weixin.qq.com/s/R4xjjcw1JpbAfMgnLWPmXg
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:51:05.008979
---

# 紧急安全预警｜ArangoDB曝两枚严重漏洞，未认证攻击者可通过漏洞链实现Root级RCE

# 紧急安全预警｜ArangoDB曝两枚严重漏洞，未认证攻击者可通过漏洞链实现Root级RCE

tuto
tuto

杂杂咱谈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、漏洞概述

安全研究人员在ArangoDB HTTP攻击面中发现两个Critical漏洞，核心问题都是服务端错误信任客户端提供的信息，并据此判断请求权限。

* 漏洞一: URL编码认证绕过，未认证攻击者可访问受保护API，并读取、修改、删除数据库数据。
* 漏洞二: isSystem 权限检查缺失，具备数据库写权限的攻击者可创建高权限System Task，突破JavaScript Sandbox，最终实现Root级代码执行。

两个漏洞可以组合形成：

```
未认证访问↓绕过认证↓获取数据库数据及Root密码哈希↓获得数据库写权限↓创建System Task↓Sandbox逃逸↓任意文件读写/SSRF↓Root级RCE
```

## 二、漏洞一：URL编码绕过认证

ArangoDB默认要求/\_api、/\_admin等路径进行身份认证，但认证组件检查的是原始URL，路由组件使用的是解码后的URL。

攻击者将：

```
/_api
```

中的\_替换为URL编码形式：

```
/%5fapi
```

认证层将其视为普通公开路径，而路由层解码后仍进入/\_api特权处理程序，从而绕过认证。

研究人员验证表明，攻击者无需密码、Token或Session Cookie，即可进一步读取、修改和删除数据库数据，并获取ArangoDB Root账户密码哈希。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xoBWaEOhvRGldM9zFAkXBicTbbhjialXZ524hNib09fYopgR3etsutf8MqRw3icg89c0k6A39KBuB2WicCsWNTYSgFofUjparLGVcT9JOto7pR2M/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/xoBWaEOhvRHqKZrzPEH9VibUeiae2icP160LalANF3iaaJvj6f0PkBX6b4Hm45oquz5ssib2YUTI6dey9rkmjHD3kzF1fnrwXs285lL2tlwxWIOs/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xoBWaEOhvRF8icKjfaB6ZYRoRFIaiaqb3F9AcR4Ir9qqP8cgkzfgVBoficF6oqGJib9C9gnsAkjcfd2nTics2BpJJtA41HUM3CjAQPkugxE6ACH8/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xoBWaEOhvRF3PTjI0ibWEia7Vmo9XAYAibXC1BUluuC4H6bibhM3qA5AlSZtSJPG4K1Q9FibGAibC77bbNQdL8WkEX82gZrZ7hKmbW1dKtMicFM2JI/640?wx_fmt=jpeg)

## 三、漏洞二：System Task导致Sandbox逃逸

ArangoDB允许通过HTTP接口创建后台JavaScript任务，其中isSystem字段决定任务是否进入内部高权限上下文。

问题在于，HTTP接口没有像内部JavaScript API一样检查调用者是否具有Internal权限。

攻击者只需控制：

```
isSystem: true
```

即可让任务进入ArangoDB的Internal Context。

成功逃逸后，攻击者可以：

* 读取宿主机任意文件；
* 写入任意文件；
* 访问内部HTTP服务和云Metadata；
* 获取TLS私钥、JWT密钥及环境变量中的敏感信息；
* 利用Root权限文件写入实现代码执行。

由于官方ArangoDB镜像中的arangod以Root运行，因此该漏洞最终可能导致完整宿主机接管。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xoBWaEOhvRF06SnSlZYDWuqAjsjsYcNibs8EyxyJJK7R4zqNdbuKXQvKJBg2HtfVEVicCMrFqx9RaxZSj1T4lzhc5s9RofCkHucLUM0SnJicXA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/xoBWaEOhvRGf5aibxc9e759JON9UWsgZRaFYGUU9xF6XD8kkHNXDxwpgsDcxqv6CCfL89ZOVXMpd6f5OqrziaF3OFNtdlVUveeO3o6uLyEJLI/640?wx_fmt=jpeg)

## 四、完整攻击链

```
未认证攻击者↓URL编码绕过认证↓访问特权API↓获取数据库数据/Root密码哈希↓获得数据库写权限↓创建System Task↓isSystem=true↓突破Sandbox↓任意文件读写 + SSRF↓Root级代码执行
```

## 五、漏洞披露时间线

* 2026年8月23日: 研究人员向ArangoDB报告两处安全漏洞。
* 2026年8月31日: ArangoDB发布3.12.11修复版本。
* 2026年9月6日: 官方公开发布两份安全公告，分别对应认证绕过和System Task权限控制问题。
* 2026年9月8日前后: 漏洞技术细节及完整攻击链陆续公开，两处漏洞可串联实现从未认证访问到Root级RCE。

## 六、影响范围

受影响版本：

```
ArangoDB ≤ 3.12.10.1
```

修复版本：

```
ArangoDB 3.12.11
```

两个漏洞均被评定为Critical：

| 漏洞 | 影响 | CVSS |
| --- | --- | --- |
| 漏洞一 | 未认证超级用户级数据库访问 | 9.8 |
| 漏洞二 | 数据库写权限 → Root级RCE | 9.9 |

## 七、修复与排查建议

1. 立即升级

将所有ArangoDB实例升级至：

```
3.12.11或更高版本
```

2. 排查网络暴露

重点检查ArangoDB是否直接暴露于互联网或其他不可信网络。

3. 检查Root账户

重点确认是否存在默认密码、弱密码以及多个实例共用凭据的情况。

4. 检查历史日志

* URL编码的`/_api`访问；
* 未认证数据库操作；
* 异常System Task；
* 非正常文件读写；
* SSRF请求；
* SSH Key、Cron、systemd等文件变化。

## 八、总结

此次ArangoDB漏洞的关键并非单纯的URL解析或参数校验错误，而是不同组件对身份、权限和请求含义的理解不一致。

两个漏洞结合后，可以形成：

> 未认证访问 → 数据库控制 → Sandbox逃逸 → 任意文件读写 → Root级RCE

企业应优先完成版本升级、互联网暴露面排查、Root凭据检查及历史日志审计。

#Simple #ArangoDB #RCE

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LCF75xtxMiaiaUiauC6TKOGdQ4TYySakdjbD0xCM5iakCGJ1S98zU7AahSSrSrtoqdNQUSjoQZ2ia7KHDichAXQSQsPw/0?wx_fmt=png)

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