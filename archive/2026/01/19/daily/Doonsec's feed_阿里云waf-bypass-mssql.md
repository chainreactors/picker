---
title: 阿里云waf-bypass-mssql
url: https://mp.weixin.qq.com/s/I5l7RhhFPE96zTQld9nwkw
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:31:40.535397
---

# 阿里云waf-bypass-mssql

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HtVqoRw6DWiaQ8IKUVsC5EgrUj0rzqvMDBib0CUHrMAstzaia6eh1gWahQ/0?wx_fmt=jpeg)

# 阿里云waf-bypass-mssql

安全的黑魔法

![]()

在小说阅读器中沉浸阅读

编者荐语：

tql 师傅，感谢加白

以下文章来源于阿兰安全
，作者阿兰\_安音

![](http://wx.qlogo.cn/mmhead/5mxuSU5RGhbVjOIU4bBq6SSjnGY6FAkq8lNKeCVBPaNRtw5uzR98gbIpvAGSANiaJu3h7pV0f0VU/0)

**阿兰安全**
.

阿兰安全团队专注于攻防演练、代码审计、工具开发和漏洞trick等等，欢迎大家关注

**“** 仿佛是下一世，少年微笑着脸。**”**

# 声明

由于传播、利用本公众号阿兰安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号阿兰安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！本公众号文章的内容源自团队，未经许可严禁转载。

# 前言

这是团队中小伙伴挖到的一个mssql注入，但是存在阿里云waf，经过一番努力和团队中某位师傅的帮助下完成了bypass阿里云waf获取到了user和database

## 0x01 发现注入点

一个单引号成功的触发了报错信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HMOD4vaxt8MpVFibKtV1hJSodX43Gu1h88Eia2R4DbNibAQEMELIdiaALXw/640?wx_fmt=png&from=appmsg)

两个单引号正常回显

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HjUYLQKKlwA0mngGho6mzfRo5uh5KgCQVqaInSSJlSP1vYaRNvDrgLg/640?wx_fmt=png&from=appmsg)

继续深入发现存在阿里云waf

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HgJMnK6Wvrxvx160vQo8t6X4kicSkjZTT3BRovBrBvewcT4BzlGBT5iag/640?wx_fmt=png&from=appmsg)

也是花了不少的时间构造了一个payload，证明存在注入点

```
admin'and%1edatalength('nmsl')not%1ein(0)--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2H13VUaXDvGxhnXh0GyCgnRC13Mcc6qibK39iaWa30khDGFRfmvnxHcoRw/640?wx_fmt=png&from=appmsg)

随后也是利用substring获取到了suser\_sname()(当前连接到 SQL Server 的登录名)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HbO0ILs5OgG4gqXIQpUjlmqk9t6fA5Dcic6feZOx2SUOFhHAnlKiakcjg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HZibJQHQEXewybeMF91tC2j5nsak58swx6E9ibP1s8cyj4KDb8vnN3xlA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2H5rpIkfEMTo3iczGthmXbmPvYIe243MFKicHw0ph7wrgsaribMeF9yIjeA/640?wx_fmt=png&from=appmsg)

## 0x02 fuzz尝试 获取db\_name()

### 0x01 分块传输

利用工具：https://github.com/c0ny1/chunked-coding-converter

这是一款比较不错的sql绕过工具，利用分块传输来绕过waf，这里我们修改获一下payload把suser\_sname()换成db\_name()，可惜这一次的对手是阿里云waf，不幸GG

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2H3JK0GichAE2rXa8nfQ6CWUXjtA3wyhpdew1lxUPEicpicbQyBIK0ibvSrg/640?wx_fmt=png&from=appmsg)

### 0x02 charset编码

参考文章：https://www.t00ls.com/articles-73197.html

不知道师傅们有没有注意到，返回包中的 Content-Type: text/plain; charset=gb2312 我们尝试构造一下 gb2312编码的payload ，同时记得修改请求包中的Content-Type

```
payload = "admin"
gb2312_bytes = payload.encode('gb2312')
percent_encoded = ''.join(f'%{b:02X}' for b in gb2312_bytes)
print(percent_encoded)
```

admin --> %61%64%6D%69%6E 发包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HBnUtyjTpKTRJjyWctmVEu9j3Rk6ia9SvRKncdXgRMmtF45SxRqfEXVg/640?wx_fmt=png&from=appmsg)

跟utf-8编码的返回一致，说明是可行的，那我们来编码一下原payload依然替换成db\_name()，不幸还是GG

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HVFicm5WFtCh0dtnzv99tyBlA4LAmFp01moQAPFZibSW0CvQyJNI1gayQ/640?wx_fmt=png&from=appmsg)

### 0x03 iis特性

参考文章：https://cloud.tencent.com/developer/article/1416023

iis支持unicode编码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2Htvdd7gibXsUoz2Xxcay0ycemfRkxzO7P1rqRibEzxDWvJskInIkQFkzQ/640?wx_fmt=png&from=appmsg)

当然我们还能同时实现 gb2312编码

```
admin --> 完整unicode编码 --> %u0061%u0064%u006D%u0069%u006E
adm --> gb2312编码  %61%64%6D
in  --> unicode编码 %u0069%u006E
admin --> %61%64%6D%u0069%u006E
```

那么我们在来一个随机任意字符串进行fuzz，但是还是不幸全部GG

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HkvnySM6uzicKsVd13niaXmC43zgM2Vrca7UicyPpRyyKkHDgCM0xph3Tw/640?wx_fmt=png&from=appmsg)

### 0x04 HPP

HPP在实战中也帮助绕过了不少waf，当时尝试了很久最后用HPP绕过了payload如下:  但是本次利用还是不幸GG

```
id='aNd+casT(1/currenT_User%0aas%0adecimal)>0&ParamList=string&id='--
```

### 0x05 脏字符

脏字符这个其实在实战环境中也帮助绕过了不少waf，10w字符不够那就上20w，20w不够就上50w，再不行就100w。这一次就尝试到了50w脏字符，不幸GG

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HTxHtI6J9kqbb4VjYfKmblbgNIVCFyEicrVbZfQ38tFMskszmj2TDpIw/640?wx_fmt=png&from=appmsg)

### 0x06 真实ip

一般来说，大多数云WAF采用CDN架构，用户请求先经过WAF集群再转发至源站。若能获取未被CDN代理的真实服务器IP，直接访问该IP即可绕过WAF， 但是本次的目标就是真实IP访问，不幸GG

### 0x07 数据包变形

利用工具：yakit

这里就不放截图了，也是不幸GG

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HqwqSPgGTklqBBNqI1bqv24ZKoMfyeAD0T7xuW5lefjMicl66909KMIQ/640?wx_fmt=png&from=appmsg)

### 0x08 终极奥义

到了这里，安师傅已经有点小崩溃了，突然他想到了什么，打开了微信，点开了某个人的头像并发送了神秘代码，然后就成功绕过了WAF

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2H4pc4N2VQrBNZJia5a0eBO3MjvqayQ8iaYLqrqUclRCVHp2N6uoRKhsIw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HbQtVibPF3IYKM2y2A4JVJj7PKQG8TBSn4ed38XJm15SI84HIzNkJYSw/640?wx_fmt=png&from=appmsg)

## 0x03 绕过waf

根据某位师傅的指点，安师傅立马写好了脚本，获取到了user和db\_name() 开心的交洞去了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HSNmgTQwUO2E6tX5q3uYWdcm9cibfzNaZvjsLnuymFDEb4JcT8aeBZYw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HBLZlRhJa4MB0uLGoPB5WDKW5CVziaTSyrqKS9VlG6npAZYpX1CicAOpw/640?wx_fmt=png&from=appmsg)

## 0x04 order-by注入

这一次安师傅再一次遇到了mssql，不过是order by注入类型的，这一次他还能绕过吗？

```
测试payload:
user
[user]

/Api/agent/GetPageListSort?pageSize=20&pageIndex=1&orderBy=user
/Api/agent/GetPageListSort?pageSize=20&pageIndex=1&orderBy=[user]
```

/Api/agent/GetPageListSort?pageSize=20&pageIndex=1&orderBy=user

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2HxPaoQwtMgkSIHia7RH9OvDnSBtNJPXRJ3Uj6M0eOWCSQfWkZ9liajgBQ/640?wx_fmt=png&from=appmsg)

/Api/agent/GetPageListSort?pageSize=20&pageIndex=1&orderBy=[user]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8zJMziaOE7VUL25AiasWaVo3s2ia4UmjQ2H7J4SH5WB4xP1fvAO9ArTbRLzgKj20hWjfY8kicfJ8VV0rHbqkpFsOKQ/640?wx_fmt=png&from=appmsg)

## 0x05 获取payload

相关payload的获取，请添加阿兰微信。

考虑到团队成员，这里不会放出所有的payload。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/o85eMywxzFQVOalG3nNNjg72X0OYevicy8MLfiabc2UXPPO3zZwwMhZyjofqnWPqHaH6k0OCH9yzAvcfVhFOcCPw/0?wx_fmt=png)

安全的黑魔法

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/o85eMywxzFQVOalG3nNNjg72X0OYevicy8MLfiabc2UXPPO3zZwwMhZyjofqnWPqHaH6k0OCH9yzAvcfVhFOcCPw/0?wx_fmt=png)

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