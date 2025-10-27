---
title: 记一次从登录框到前台rce
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247494486&idx=1&sn=10286369df3533012ecaba68da80c2a5&chksm=e8a5e135dfd268230250cef0bdd8aeb8a04ff00b10cc17f1aeabbc3c1ac52a589348d249d5b7&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-05-03
fetch_date: 2025-10-06T17:15:37.565032
---

# 记一次从登录框到前台rce

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4zeVmN65USIe5zSGxGaZNndNbCagTcBSCb8WLajGTmD7NYo9wenaZ2bHpCfPgo0ZdUUIiad7XENiaQ/0?wx_fmt=jpeg)

# 记一次从登录框到前台rce

迪哥讲事

以下文章来源于yudays实验室
，作者yudays

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7sPEUKMpk4lowa1VN2eBSX9O1sfup6GghZDGJzRYwygQ/0)

**yudays实验室**
.

安全相关与攻防实战分享

欢迎转发，请勿抄袭

        在某次众测项目中，开局发现是一个登录框，于是想放弃。经过弱口令工程师一顿输出，最终getshell。于是就有了这次分享～

1

接口未授权挖掘

        在网站未登录的情况下，由于不知道后台接口。唯一办法通过js文件、路径扫描。通过这种收集方式使用burp进行批量扫描，分别探测GET/POST请求。观察响应包跟状态码。判断响应包，确定存在未授权后，再构造数据包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4Vv0VYLOkaEwO2M6wAQZVsFQve07C4ydMhkjTMorSiaTAImLL1q2K0RtA/640?wx_fmt=png)

2

突破登录框

在测试站点中，很多时候不提供测试账号。此时，就需要一个尝试爆破账号，但是有时候会有验证码(重发登录包，50%假验证码)。正好这次没有验证码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4VZEZjJzABEPodPJIkRH8ZblyicJqeialiaRJlPlXyiaUzB2rtXkR4dCud8Q/640?wx_fmt=png)

拿到这种网站，先判断一下有无用户名猜解。判断存在与不存在账号。测试常见的admin、admin321，观察它们之间的提示。就算发现有这个admin账号，但是有密码错误锁定的情况，那么就尝试爆破账号。(手机号码与常规账号，总会有测试账号或者总会有人设置弱口令)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4Vhmia4HD9nnXLyw6BdJfMOLwxqbUvmdX7t7zwGic9cwPvcEB2we1LOOzg/640?wx_fmt=png)

密码设置为弱口令123456，账号为字典进行爆破，根据响应包大小进行判断。最终拿到测试账号。

3

后台漏洞挖掘

通过测试账号进入后台，额外注意接口跟上传下载点。由于这个我们没有网站代码，只能访问相关功能，并burp插件Autorize记录探测那些接口存在未授权。通过页面翻找，找到一个正常的上传点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4VXO4pXiaut5mZ1sKDjf7bODyG0Y0JMfarMSo8wtxzlykchQVQ69Nz9Rg/640?wx_fmt=png)

构造正常上传一个txt文件，发现这个功能先是上传后并读取该文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4V5J3bJHjGicDyPibDWTj42cKu8JovADstwrCvWCqzpRVPH8pk03GoCzOw/640?wx_fmt=png)

并尝将cookie凭证删除，发现仍然可以上传。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4Vzkib79ebkW3ApTE5ibmYWkSVHMPLSadnXibAtx7BE8Xpcpn1K1w6x7HPg/640?wx_fmt=png)

那么将它转成是前台的上传漏洞了。经过测试发现，目录也是可以穿越的，文件名可以任意。读取文件接口也存在穿越问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4V63slGch2kh3qicia53pqbsicWjxzFxEiayYjx69KicicNop8wlhIOjRd2csQ/640?wx_fmt=png)

根据接口判断，该网站是可能是springboot的，显然上传jsp是不行。那么还剩下两个方式拿权限。一是上传ssh登录凭证、二是写定时任务反弹回来。扫描了一下ip，发现ssh端口未对外。于是尝试定时任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4VdBOwz1sK2DJIPCyDH9b9CKbRXCQkOeUXSNPukeMhLHynrugkicw0tdQ/640?wx_fmt=png)

等了几分钟没反弹回来，通过于是又看了一下定时任务的日志。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4Vl1jXNuMDw44ehdNOBt1K4AQJOadBcianhv44Oic9727NOAAFE0YPEfMA/640?wx_fmt=png)

最近的定时任务日志是在前一天，要么就是服务器时间慢了一天，或者是定时任务管理器在前一天被停了。再次尝试写定时任务。

```
* * * * * *  whoami>/tmp/data.txt
```

仍然无法读取到tmp下面的data文件，至此确定定时任务真没起来。

4

柳暗花明

难道真的无法getshell了吗？通过下载接口，读取root用户的历史命令。找到网站路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4VRenbDOU7ebwWgmpbaKSwEMdhia8kac34HbLicgMic9c4M3xibWDicdQQf8w/640?wx_fmt=png)

看到这个webapps，瞬间精神了。直接构造上传路径，并输出jsp文件。上传shell～

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4VhrwwMLvV6iayqK7VFrAqcTKzzaTt713nEJ7gcK5gx7ibbKaboXzzjDbQ/640?wx_fmt=png)

哥斯拉连接上去，上个whoami截图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4V66f24s74MXHyVloKmKUSmBn0dciagmYw9DrPpynG7K1aL9ZzJONWgqA/640?wx_fmt=png)

通过检查网站文件，发现是一个tomcat里面有个目录是springboot。但是网站没见到其他的jsp文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BDzX6q5EsXkJbdvGS9q6rqV5eA1RZb4VJHl4vjqCfA4oc7a6JYhxOCOa1gXUx0B8kdpLRXS6iaiaPmgGibIxc1cIw/640?wx_fmt=png)

这种开发方式属实少见。网站也是通过war方式部署。

由于是未授权的上传点。也算是前台rce了～

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

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