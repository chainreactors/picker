---
title: EasyTools渗透测试工具箱V2.0.9更新(新增mysql、sqlserver等诸多数据库连接、优化便携发包等功能)
url: https://mp.weixin.qq.com/s/vdwMbOmEynAegQMWSVm0AA
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:36:13.269021
---

# EasyTools渗透测试工具箱V2.0.9更新(新增mysql、sqlserver等诸多数据库连接、优化便携发包等功能)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7fvjX482azJ9P7fA3uq3zZE49jugOKcUzgJfbWSeEsWTK7sSYS7e0licHW6GTEr5LlNkv6PBRf5Vj2ErdUQm5JA/0?wx_fmt=jpeg)

# EasyTools渗透测试工具箱V2.0.9更新(新增mysql、sqlserver等诸多数据库连接、优化便携发包等功能)

原创

沐寒

渗透云记

![]()

在小说阅读器中沉浸阅读

**免责声明**

由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJZJ4pVQHOicqtkQntqLduTfPaVvVnZ4iaGc0DaBeQqNoicYUrzzyOpIsJWbSgNUqV3SodRwKFOIq3Lw/640?wx_fmt=png&from=appmsg)

欢迎关注本公众号，长期推送技术文章

## 前言

距离上次发文，目前EasyTools又已经更新迭代了很多功能，这里给各位看官老爷们汇报一下：

1. 优化漏洞扫描模块，支持暂停任务与断点恢复功能，支持多任务同时扫描
2. 新增自定义主题功能;
3. 新增mac类型的顶部栏
4. 优化程序代理功能，支持系统代理设置(win专属)
5. 免杀模块新增自动dll转发生成功能
6. 简练助手新增mysql、redis、mariadb、postgres、sqlserver、sqlite、mongodb等诸多数据库的连接功能，支持自动获取已保存的ssh信息进行隧道连接;
7. 优化主机扫描的口令爆破功能，支持扫描结果联动发送简练助手进行一键连接

目前的更新主要集中于完善基础功能，在将常用的功能补充完善之后，再进行进一步的利用模块完善。（ps，增加redis漏洞一键梭哈、参考mdut实现数据库提权等，这个就慢慢来吧~~~）

## 新增功能

#### 1. 主机扫描

优化端口扫描模块，现改名为主机扫描，支持多任务同时扫描，支持联动目录扫描、指纹识别、口令爆破等模块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJ9P7fA3uq3zZE49jugOKcUuvy18h5U6V9EkhXp3Xa0PLEia23WYbFW9icEOuTFOictaV4xlXblJALZA/640?wx_fmt=png&from=appmsg)

口令爆破的结果会发送至漏洞扫描界面进行保存，支持联动简练助手模块，自动填充获取的服务账号密码信息进行连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJ9P7fA3uq3zZE49jugOKcUOhStVibia36IejsMnxiaL08qCwUibSicMBd3zO2NTlFCNa3bjfs5c7xGBkg/640?wx_fmt=png&from=appmsg)

#### 2. 简练助手

简练助手模块以往仅仅支持ssh、redis以及ftp连接，经过一段时间的测试，现在完善增加了mongodb、mysql、sqlserver、maridb、sqlite等诸多数据库的连接管理。（ps，数据库连接可能因为测试案例不足存在部分bug，如各位大师傅们发现了，烦请提交issues或者直接私信即可，谢谢）

注： redis、mongodb连接放在nosql数据库模块下

mysql、sqlserver等数据库放在数据库管理模块下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJ9P7fA3uq3zZE49jugOKcUw688jssGBI3e4GibhKfLGUoqWG3LabTFqzIN8h7KPWxmo7yW4pib1jAA/640?wx_fmt=png&from=appmsg)

查看数据信息的时间，建议全屏，这样看起来舒服点^\_^

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJ9P7fA3uq3zZE49jugOKcUiaxxym71XN7peLAJ4658F42LxiatypxmrbL7yibE8wguickfQmmEvo6yhQ/640?wx_fmt=png&from=appmsg)

#### 3. 自动dll代理转发功能

支持上传任意dll文件，对其进行代理转发，用于权限维持使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJ9P7fA3uq3zZE49jugOKcUldOT3HSnMjvBX2Z5rqLuNAUvBmsZ9AfuQBottpjvicA8KuI3Qa1k5tg/640?wx_fmt=png&from=appmsg)

#### 4. 便携发包

针对便携发包，现在经过一段时间的优化，基本上已经可以轻松实现swagger接口批量测试、类似于postman的接口测试、数据包直接发包测试、文件上传的bypass测试

针对以往手动添加参数之后，发包如果失败的话，无法看见详情，现在增加了查看数据包的功能，便于直接寻找发包失败的bug

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJ9P7fA3uq3zZE49jugOKcUc0AniaOAQrzKCf1ZDZwuW9jdNQZ4esKX8r1fsfM5XjR7jzDHHEfnfdQ/640?wx_fmt=png&from=appmsg)

## 获取

私信回复：EasyTools

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLbE8HiaQapVkBwypwXhsmWWEwZyOx2Frhw9bDjyRnVSMtubJkZJY9NX2Hw8Igx7fDmuZnYXzPUvDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK0JBUq0N1g9hpXvZiaWm32V2kibRficfdehadlNxb8ibickibcgHFOr9FXF5qibRy3pDw984iaZP8InvejUQ/640?wx_fmt=png&from=appmsg)

往期精彩：

[【重大更新】EasyTools渗透测试工具箱v2.0.5（它支持自定义主题啦，不再是以前那单调的白，同时优化诸多允许逻辑bug）](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484688&idx=1&sn=66e4a1510be5adb03d0d82abf8bdf09e&scene=21#wechat_redirect)

[【圣诞节快乐】EasyTools渗透测试工具箱V2.0.3更新(新增白加黑挖掘与自动编译、文件上传自动bypass测试等功能)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484672&idx=1&sn=42b9f5c9cba2b1c4618844a9caa46cae&scene=21#wechat_redirect)

[EasyTools渗透测试工具箱V2.0.2更新(新增漏洞扫描功能，优化存在的诸多bug)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484654&idx=1&sn=6cda01489ccdb21cb669bd316dd2905a&scene=21#wechat_redirect)

[EasyTools渗透测试工具箱V2.0.1更新(优化便携发包功能，新增端口、目录、指纹扫描功能)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484633&idx=1&sn=82ec8a8d4025be7ff7237f8015cad3b0&scene=21#wechat_redirect)

[【工具分享】DllProxyGenerate，dll代理转发脚本一键生成](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484546&idx=1&sn=1d41675f6f32872c86f2b6d634a9bbe5&scene=21#wechat_redirect)

[【知识学习】利用DLL代理技术进行权限维持](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484546&idx=2&sn=ffd686e5ece32ac7dc39624b9c84839b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK5R6NYcibf6ADO4U7BvUHupNyYDu3RwMYRL9ickjZNUMoHeGcAS7fgF2zcyWaODWcOuqjqkeAibjkPQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

渗透云记

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

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