---
title: 好靶场杯第一届综合赛-古法赛道-流量分析webshell3-上
url: https://mp.weixin.qq.com/s/53Z48tB8wbFw3i2h6klMCw
source: Doonsec's feed
date: 2026-10-22
fetch_date: 2026-10-23T06:44:38.572380
---

# 好靶场杯第一届综合赛-古法赛道-流量分析webshell3-上

# 好靶场杯第一届综合赛-古法赛道-流量分析webshell3-上

原创

曾董
曾董

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

# 1.提交攻击者IP地址

过滤http

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibXXbPRpSeVqRYkfwlMnwbgxa4ibx6y01BNMTqvsOAwYictuwA62drBdBtJwSQ2IgzibpBOwa3cK14MicvRxlSLEteWJKBF7XsGDyA/640?wx_fmt=png)

看到192.168.99.28向192.168.99.59发送请求遍历路径查看账号信息文件

答案：192.168.99.28

# 2.提交受害服务器 IP 地址

见上题

答案：192.168.99.59

# 3.攻击者使用什么工具进行了内网资产探测？

过滤攻击者ip

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9NbwuffOcNHbicI0fSDFnVdXlibibhINoJRbdJclxibEglQYVtDKAOrB6icK5o8ku3ZpCl5SlXO996EOwian1CQ1et1yuT2xhdIh6TM/640?wx_fmt=png)

我们可以看到这个攻击者先对整个192.168.99.0/24进行探活，之后批量进行端口扫描

这种“先探活、再扫端口、再识别服务”的行为特征是 fscan

答案：fscan

# 4.攻击者内网扫描了哪些存活主机 IP？（从小到大，逗号分隔）

扫描就是icmp协议

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibic3nkxeSRl0xvSXG89dKaRNQtwMNicbU2oRPeJjeib1SO4wYvGuv8lPicIlAvb9ryuLUDOTFf3fJuHia5tNDjtCSs7zX33hjnABqdI/640?wx_fmt=png)

因为是存活的主机，会给攻击机响应，所以过滤ip.dst

答案：192.168.99.58，192.168.99.59，192.168.99.60，192.168.99.61，192.168.99.62，192.168.99.128

# 5.受害服务器开放了哪些端口？

找开放端口就过滤

tcp.flags.ack==1&&tcp.flags.syn==1

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibiceqWMAERV24Tbry787Mw2IxlTM82ZmWibFpEia0tM6W0hNvM00xWBtLd8ibvp4Q1GUwoLwMX2F4vs9OFvcDkh4nic1mXRbhffy0Ms/640?wx_fmt=png)

可以看到开放端口有80，445，135，139，3306，5985

# 6.受害服务器 Web 中间件及版本是什么？

常见web中间件:nginx,apache,tomcat

过滤找一条最大的包

http.response.code==200&&ip.addr==192.168.99.59

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib9fSVw4TtgmjNVmHiar1vTib4aAqicAz5O2JdibFibJ7R7icIkxCoVIgF0jiak6bAiaxicIqQhXTlQicV63EMoK8ma7L9fJIb9xf8JfGlqcI/640?wx_fmt=png)

答案：nginx/1.15.11

# 7.受害服务器使用的 WordPress 主题名称和版本号是什么？

WordPress 是一个用 PHP + MySQL 开发的开源内容管理系统（CMS）

过滤包含主题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib8SLWxPXwzYjdvYk9844DqyT22CWPaGMBbl5ZDOxAjR1ia9Ano6NjDBa8447rNQ9hl2JHozQR82IHMaZQKQ64HF6Xm9sXMcw46M/640?wx_fmt=png)

在这里就可以看到主题名称和版本号

答案：WebStack-1.2024

# 8.攻击者利用了哪个 CVE 漏洞？

从上一题我们知道主题是WebStack-1.2024

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibACecDG4xaEAfOQ0jKkXMdIfkWfMj2GPNK4BeKDJV6obA2CbWhofnibPCGcFoZ5MpUfjRfL2WS8RBntMSj7icONiaQUWF5Qg9cco/640?wx_fmt=png)

在网上搜索就可以知道是任意文件上传漏洞

答案：CVE-2026-1555

# 9.攻击者漏洞利用的完整请求路径（含参数）是什么？

根据上一题我们已经知道是那个cve漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibib5DSxm2CGScA2RC5l7pic9uiayftCahbwXsJ2q9HYsOiaWxvDtwtnZZt7uJ8Qib0kXOnhkuoGghWwzWDRW2kw7YecYZdV6NeEQHSY/640?wx_fmt=png)

漏洞造成的原因是因为io\_img\_upload()这个函数，我们再过滤post请求的时候可以发现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib8HAf2Pv4uVwruia2TQO8Syv83W6aeR236KnVv3eRRVz4urR8iasXRYjxibN1EDqzTKDfuI2Q8lMp1KJ4Qpic5DqIEkWyT8b9bZNLQ/640?wx_fmt=png)

所以完整的请求路径就是wp-admin/admin-ajax.php?action=img\_upload

# 10.攻击者上传 Webshell 时使用的客户端工具是什么？

追踪流

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9oibFapkhZHADF2PO1Y3PmoSc2iabW7reAXjCLI5AlQGYicHukY1ZWowPvOwOJnSxBeXibRFF63taWF11RhtR6L4BsCx264vRWeJ8/640?wx_fmt=png)

还找到了文件名是web.php

答案：User-Agent: curl/8.5.0

# 11.攻击者上传的 Webshell 在服务器上的完整 URL 是什么？

可以看到上传的webshell就在这下面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9icbefHdNoP5icAMs2zwbvhHceBO1icIfmjiaicSFhwMgM9W3nRRqT14HTAZt4miakicsBiaibEf8gzCNX7icuibefv7ibsWrnyEcsXaVOkp0/640?wx_fmt=png)

这里还要带上前面的ip

所以完整的就是

答案：http://192.168.99.28/wp-content/uploads/2026/06/20260617192508\_4dc56fd5.php

# 12.攻击者上传的 Webshell 原始文件名是什么？

见10题

答案：web.php

# 13.攻击者使用的 Webshell 管理工具是什么？

webshell管理工具就是一类用于批量连接、控制和管理 Webshell 的软件

也就是蚁剑，中国菜刀，哥斯拉，冰蝎这种

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibBWJtI9TYKnDgrEmzg5A96RznrkadcxS8Tdw0ytQibnPtMdwfibCLpoaicy3ToT9jRxHSKCzA9Uqo5AlF7ILAWmAV0bQ75n0Ah3A/640?wx_fmt=png)

典型的哥斯拉特征

四种主流 Webshell 管理工具的特征对比如下

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 工具 | 通信加密 | 一句话木马特征 | 流量特征 | 默认 UA |
| 中国菜刀 (Cknife) | 弱/可自定义（Base64、chr 拼接） | 短小，大量 `@eval`/`assert`+`$\_POST` | POST 体有明显的 Base64 + `;` 分隔参数 | 无固定特征，可自定义 |
| 冰蝎 (Behinder) | AES 加密（动态密钥协商） | 固定代码结构，带 `session\_start` | 首次请求有密钥交换（返回 16 位密钥），后续全是密文 | 默认 Java 类 UA，但可改 |
| 哥斯拉 (Godzilla) | XOR 异或加密（自定义密钥） | 含 XOR `encode` 函数、`getBasicsInfo` | POST 体为 XOR 密文，响应也是密文 | 可自定义 |
| 蚁剑 (AntSword) | 可自定义编码器（默认 Base64） | `eval/assert` + 解码函数 | POST 体带明显 Base64 特征，结构规整 | 默认 `antSword/v...` 可识别 |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

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