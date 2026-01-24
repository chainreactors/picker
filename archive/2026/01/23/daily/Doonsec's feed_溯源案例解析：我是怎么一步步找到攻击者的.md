---
title: 溯源案例解析：我是怎么一步步找到攻击者的
url: https://mp.weixin.qq.com/s/8-9nH6bni-abRj86Go1O-g
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:28:02.888234
---

# 溯源案例解析：我是怎么一步步找到攻击者的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZQ41hzZ0onJlrvELeeUZKmc7CMJEicocu0lKjx7aLicz6e1hjqtJveT0g/0?wx_fmt=jpeg)

# 溯源案例解析：我是怎么一步步找到攻击者的

原创

Ikun
Ikun

0xSecurity

![]()

在小说阅读器中沉浸阅读

#### 事件发现

2023年xxxxxx，114.116.x.x对我司xxx资产x.x.x.x进行大量扫描攻击，属于违规攻击时间。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZA9cGPeQLv2rWUqJW4Ey3EqqfrQrQzjeP2dnKNPslNdKYYd8kI2s3eg/640?wx_fmt=jpeg&from=appmsg)

#### 反制

通过对攻击者ip的溯源分析，ip地址为北京联通IDC服务器资产，搭建cs，已被标记2022红队标签、1条IDC服务器相关。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9Z0CwnYAu8AMcnhymEhm4KNicyW4MYFJ5P2bztYWMLFsPhASYKvSWyjtQ/640?wx_fmt=jpeg&from=appmsg)

对该站进行网站信息收集，发现开放7001端口，搭建weblogic服务。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZrCAKV9fy0JicUbRlqicgduC8hgzOVib5tscfNwRGsoOYBPJ1dfHwfiaJVA/640?wx_fmt=jpeg&from=appmsg)

经过测试，发现存在CVE\_2020\_2551漏洞，上传webshell进行连接，拿到权限。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZXQwXYsxQ2ticGrnFRDE4iaic7rSmrdJyic1ZDwOjhUaotLzGFdjxMTfd8Q/640?wx_fmt=jpeg&from=appmsg)

#### 执行命令

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9Zh7iaRw5ibMdSuI9Kk6bJMCHHRWc167VEFALRlHLYTyzPzklWq5kia26Gg/640?wx_fmt=jpeg&from=appmsg)

翻阅网站信息，找到boot.pripoerties文件，存在加密账号密码

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZqSD2vfsdU3jPKTkbcmgg8d6GWd6s33UxlYRarQSLqeyO6qQtM3icbGQ/640?wx_fmt=jpeg&from=appmsg)

将图中.dat文件下载到本地，使用解密文件解密weblogic账号密码。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZUkMl86Y0jhBC4ryfmvWhpvOrdN94y7UHoFJjUh95kXP5NRsb65TJqg/640?wx_fmt=jpeg&from=appmsg)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZuhMh06gt0SiahPI2K6kFLkW6zI0icgH4FzwNAFXrApI8ReZoPM5XVNsQ/640?wx_fmt=jpeg&from=appmsg)

登录到 weblogic 控制台。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9Z4ysacn65hUXjRamJPSCLeXldFdXETibZAmgBe1Iz9geeToPahiaAkayA/640?wx_fmt=jpeg&from=appmsg)

#### 事件发现

2023年2月9日11:50:18，47.xx.xx.45对我司xxx资产x.x.x.x进行扫描攻击。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZWzgKlvLVTIaKUeQRNiaiaFpiaoWcU7qw4FM79Pdcy0Abuw7JTnhXd2nGQ/640?wx_fmt=jpeg&from=appmsg)

#### 溯源

通过对攻击者ip的溯源分析，ip地址为上海市阿里云资产。ip网段有过hvv、红队、搭建Cobaltstrike历史。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9Z2GLNBADp4P9qJCJMXSrWFlZaWiczEBqsQzVkE4T65ia29Iiapg3QWLicBg/640?wx_fmt=jpeg&from=appmsg)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZLrmZgtP1xNpaI3icY2UUr91re5hWKI1aTgLT15T5sOUUVwFQM9hQiaicA/640?wx_fmt=jpeg&from=appmsg)

5

5的微步在线情报结果

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZZPk3EAvTdDVoP6SxRLlTUbpJC6sjRTQa0rGib3tOvtU9aOcNke8YBiaw/640?wx_fmt=jpeg&from=appmsg)

#### 对该ip进行信息收集，发现开放以下端口。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9Zic6xknxcDTW0ECn9OuqjYJPg1jibS3sGXgRNlfzZW6P6erBHY4LCsf1A/640?wx_fmt=jpeg&from=appmsg)

访问443端口，发现搭建网络安全博客。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZoFvtb1h6iaUjgYicOosy2bxIp0BhFXYLrWbGRc6LkNSXLeuML2QzOKOQ/640?wx_fmt=jpeg&from=appmsg)

对该ip进行域名反查询，发现该ip绑定域名xxxx.top。、

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZS3wCnNqTWvJiazibmrkDkE60iaXNH0AdiaJmC3KbRnKro2kaiaZmmeGTT5Q/640?wx_fmt=jpeg&from=appmsg)

通过该域名，查询备案信息，发现该注册该ip真实姓名为xxx

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9Zeo905YGofuYPgEwnq8JpDPNPKXy9bic6IPxDIYasNZZuTmhsmzhTQUw/640?wx_fmt=jpeg&from=appmsg)

根据已有信息对该人进行网络信息找到该人身份证、和手机号。

| 姓名 | xxx |
| --- | --- |
| 身份证 | 3xxxxxxxxxxxxxxxxxx |
| 手机号 | 18xxxxxxxxxx |
| QQ | 11xxxxxxxxxx |

通过QQ查询，昵称为xxx，与之前查询昵称一致。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZQ8NQWaqa3Xb34PEic390yDcG6gichKVWZ2N1vHPBExUGbE7Yk1sQXnJw/640?wx_fmt=jpeg&from=appmsg)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZYP1okTEUtRZQB1CMwpbx6nZia6qMgGNbkhjnrPpCn6unqF2PVd4Uicog/640?wx_fmt=jpeg&from=appmsg)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZVmPaQPM7V0PrFQv73vra45HCCoATjzmsvLlQO6amBOichic3yicUELhzQ/640?wx_fmt=jpeg&from=appmsg)

#### 加好友

查看该QQ空间，发现此人为学生，学校为xxx学院

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZXjCNBywJuo4hyhQcoqKD2e8wicfHPJAeG3pZxEk6ticNyvQGeGSib6RoA/640?wx_fmt=jpeg&from=appmsg)

曾经有过挖 src 经历。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZzdiakhibiaGOF0UWAyO9rwVdYx5cs90702I7cFsuBb6xrZzALq3koWMQw/640?wx_fmt=jpeg&from=appmsg)

在微信查询该手机号，昵称为xx。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZibmpaQ1y2BhzTAvQdw3LkuYTz2ZvHOsQwU8YLib7HyvwUXKhia7hvH18g/640?wx_fmt=jpeg&from=appmsg)

在支付宝查询该手机号，通过了实名校验。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZV1hudWibVKB6W5jtytiatvg8Om9XhrV3eECZZDEEFaAWrDqVpgwUEQvA/640?wx_fmt=jpeg&from=appmsg)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZJM5C6r870fZugx9xyZLzLmHQFiacUklib2AaU0v9FQxCUPxc99U8P6dQ/640?wx_fmt=jpeg&from=appmsg)

2022年6月份参加网络安全相关面试，推测为hvv面试

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9Z2PgmC0CiaXS8ZzCMrTfB9JX2ACMyWibBFPibELb7W1KHDria9nBib3LjQ2A/640?wx_fmt=jpeg&from=appmsg)

2022年7月26日凌晨发空间，为2022年hvv期间，推测为在hvv值守。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9Z2Wnst6icDedsugf4dianrX5OAkXUW4jvibECPQVUr54g35LkQTia793mPw/640?wx_fmt=jpeg&from=appmsg)

通过溯源发现，此人多方昵称均为 xx,对该昵称进行百度、谷歌等搜索，找到其 CSDN、github 账号。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZXWondvhJvBr7F9sM00s5jg4ZK4aapKRwSMcXianwbhHFLaNxeiaFzDZA/640?wx_fmt=jpeg&from=appmsg)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/umfmicibSEUbgUHa6UX1nic75QDenghxe9ZD5BuFwwMlFIjicLzfn0HpJxDWLupM371Y4VYSB3ntkjoJIxI45hGY3Q/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/umfmicibSEUbh3njCWzKrGE2uj3jicFkAqjVIHpJKhnC78W3CS7OGrfItJxbfRKCxwY4fNYP1j8ric9Gk8bAun4Cibw/0?wx_fmt=png)

0xSecurity

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/umfmicibSEUbh3njCWzKrGE2uj3jicFkAqjVIHpJKhnC78W3CS7OGrfItJxbfRKCxwY4fNYP1j8ric9Gk8bAun4Cibw/0?wx_fmt=png)

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