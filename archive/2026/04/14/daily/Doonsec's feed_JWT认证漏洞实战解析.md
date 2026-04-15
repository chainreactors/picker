---
title: JWT认证漏洞实战解析
url: https://mp.weixin.qq.com/s/AZZMN6ojyX0-hOEBGxyiCg
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:42:08.436944
---

# JWT认证漏洞实战解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eDXiba58htLfkJ6n54vG57SDrXn4VHssXYxp0TzHzZbgjtFryWlsiaaGMFuOlVzKAlb3pvx3r2U6StySKED1417yajLCP63rT2OCSn9ow2VN0/0?wx_fmt=jpeg)

# JWT认证漏洞实战解析

小石学习笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于洞悉安全团队
，作者洞悉安全团队

![](http://wx.qlogo.cn/mmhead/VHU8bI7BOJDTsjNkxW2lmzljt7Zsict7TwpQibAK4dQefHIgKo6TgCXtnLr6Ye18dhbzDSYKPLTc8/0)

**洞悉安全团队**
.

洞悉安全-专注网络安全实战对抗、众测项目漏洞挖掘。

在Web安全领域，JWT认证可以说是最常用的身份验证方式之一，不管是日常开发的接口防护，还是渗透测试中的权限绕过，都绕不开它。

很多开发者觉得“用了JWT就安全了”，却忽略了其隐藏的漏洞的风险——一个配置不当的JWT，可能直接让攻击者绕过身份验证，获取敏感权限，甚至控制整个系统。

今天就从基础到实战，手把手教你搞懂JWT！

PART 01

先搞懂：JWT到底是什么？

JWT（JSON Web Token），简单说就是一种“身份通行证”，由服务器生成，发给客户端（比如浏览器），客户端后续请求时携带这个“通行证”，服务器验证通过后就允许访问。

它的结构非常简单，由 3段字符串 组成，用英文句号（.）分隔，格式如下：

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30
```

第一段（Header）

主要包含两个核心信息：令牌类型（默认JWT）和签名算法（比如HMAC-SHA256、RSA等）。

注意：这一段是用Base64编码的， 编码不是加密 ，任何人都能解码看到里面的内容，只是为了格式化传输，不是为了保密。

第二段（Payload）

这是JWT的核心，包含了“声明”——也就是有关用户的基础信息（比如用户ID、用户名、是否是管理员等）。

重点提醒： 这里绝对不能放敏感信息 （比如密码、手机号、身份证号）！因为和Header一样，它也是Base64编码，解码后就能看到所有内容，毫无保密性可言，仅用于“证明用户身份”。

第三段（Signature）

这是JWT的“安全防线”，也是最关键的一段。它需要用编码后的Header、编码后的Payload，加上服务器自定义的 密钥 ，再用Header中指定的签名算法进行加密生成。

服务器收到JWT后，会重新计算签名：如果计算出的签名和客户端携带的签名一致，说明JWT没有被篡改，身份合法；如果不一致，就会拒绝请求。

简单总结：Header（算法）+ Payload（用户信息）+ Signature（防伪签名），三者结合就是JWT的完整逻辑。

PART 02

重点实战：JWT 3类常见漏洞

JWT的漏洞，大多出在“签名验证”和“算法配置”上——很多开发者为了图方便，简化了验证逻辑，直接给攻击者留下了可乘之机。下面3类漏洞，是渗透测试中最常遇到的.

漏洞1：未验证签名

核心问题：服务器只验证了Payload中的内容（比如用户ID、权限标识），却没有验证Signature的有效性。

也就是说，攻击者只要修改Payload中的信息（比如把普通用户ID改成管理员ID），不需要修改签名，就能绕过认证，获取更高权限。

检测与利用步骤：

1. 先获取目标JWT（通常在请求头的Authorization字段，或Cookie中）；
2. 解码Payload，修改其中的关键信息（比如将"admin":false改成"admin":true）；
3. 不修改Signature，直接将修改后的JWT发给服务器，观察是否能正常访问（比如进入管理员页面）；
   补充测试：尝试删除Signature（保留最后一个.），或随便修改Signature中的字符，看服务器是否报错——如果不报错，说明确实未验证签名。注意：部分服务器会验证JWT的完整性（必须是3段，且包含两个.），所以不要删除Header和Payload，只修改Payload内容即可，避免触发格式验证。实战案例：
4. 访问目标系统，该系统无法进行注册

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLf8gVmguDqU4M14pLN4yzibI4mjsZF9ibYJdnxbL2RuQwDbUtohCGvGvTScmq7Aj9HU2zYCj8n1xeYEowzWicbndc0lj66PDxHjAM/640?wx_fmt=png&from=appmsg)
5. 从其他同类型站点可以获取到用户的jwt，修改为管理员

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLep2EAMbatQpX6erHybfiae93jib6a6utpxe2dfvLNFblCh2oMG0LxWdJl4QsV7E6OYep66wxiaZaGndMh2vg67g8JcxoIiaQDI88E/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLficwpG4VNgicQAMQPt1bugAOBibrbSvewzo5yKiaWcx7ubicuUuEOBR3cXyPLAAiakw4k0qeFUE7LeNwQAcTGKiaRmk9uSErLOl3CY14/640?wx_fmt=png&from=appmsg)
6. 利用该jwt会话调用管理员接口，直接获取管理员系统全部数据，包括大量用户登录数据，账号密码等：

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfy1M4NOSoSOcp8CKm58T7j2vR2BJgxF25VyaxgmZALcGzLBL8kBjibUaR0L0yyntzp9b7ErwuTk4W9qg0AQkWy7iaEEicIGnQCwg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLeS696fSV7cgYhno0tjTZveLp8bribibdibODlkShPNzjsyamD80Gx6IlEIjQhic08NALEHoPThdYcoPuzNFQwnYB913dqTYQaLFXU/640?wx_fmt=png&from=appmsg)

漏洞2：未验证JWT标头

核心问题：服务器没有验证Header中的签名算法（alg字段），攻击者可以将算法改为“none”或置空，让服务器跳过签名验证。

原理：JWT协议中有一个特殊规定——当alg字段为“none”时，服务器会认为该JWT不需要签名验证，只要格式正确，就会通过认证。

检测与利用步骤：

1. 解码JWT的Header，将其中的alg字段（比如"alg":"HS256"）改成"alg":"none"；
2. 解码Payload，修改需要的信息（比如提升权限）；
3. 删除Signature部分（保留签名前的.，确保JWT格式为“Header.Payload.”，注意末尾有一个.）；
4. 将修改后的JWT发给服务器，即可绕过签名验证，成功访问目标资源。
   举个例子：修改后的JWT格式如下：
5. 首先使用用户账号访问会话：

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfJHWfFarJEvGeeAb6136wJQcr92Aicl97yZBs9d2zuicGmDFCkIgtzY1a19E3vmItWJRnkM0ORaQ7JpZjXEzmLCKQJJYrSXUsQU/640?wx_fmt=png&from=appmsg)
6. 对jwt解密，使用的是RS256：

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfo83MLLOb6FlHQdVTu82iaqYMrCqv3iaibXS12VCCq8sXiacoCYdlPjKAEicLzcTu1pmb0gDE3Fah8Wg5KmdiceVMBBprazecn4pdzg/640?wx_fmt=png&from=appmsg)
7. 将alg修改为none ,并且删除sign部分（注意要符合jwt格式，保留后面的.），修改为管理员权限

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfmkXZa5yHh1dFv5a0Eje1K4GQCibRMnzDWkyCt31J7MmJpjndn6rPxlxhMKKQMVd54HR0BNo2aKSPzQHgpN4qFroKvalQgB4icU/640?wx_fmt=png&from=appmsg)
8. 修改jwt，直接越权到管理员权限：

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLcv3mGyk8UmRLqoqUvnTTE5S2qbZg8iaJTqfia3rQjxfJ896diaqmnXqWeDurkn0PX8UpByj2lPoFJy0iaSp9347IDVsIFNibYfZCGM/640?wx_fmt=png&from=appmsg)

```
eyJhbGciOiJub25lIiwiYXVkIjoiaHR0cDovL2V4YW1wbGUuY29tIn0.eyJ1c2VySWQiOjEsImFkbWluIjp0cnVlfQ.
```

漏洞3：密钥暴力破解

核心问题：当JWT使用HS256算法（HMAC-SHA256）时，签名密钥（Secret Key）是一个自定义字符串——如果密钥过于简单（比如123456、admin、123qwe），攻击者可以通过工具暴力破解密钥，进而伪造合法JWT。

这里重点用 jwt\_tool 工具实操

前提准备：

* 确保电脑安装Python 3（建议3.7及以上版本）；

* 进入atools文件夹，找到jwt\_tool工具，安装依赖（如果未安装）；

```
```
python3 -m pip install requirements.txt
```
```

* 准备一个字典文件（比如jwt-common.txt，包含常见密钥，可自行补充，工具也会自动生成常用密钥列表）

暴力破解+伪造JWT步骤：

步骤1：查看JWT详情（确认算法和内容）

运行命令（将jwt替换成你获取到的目标JWT）：

```
```
python jwt_tool.py jwt
```
```

执行后，工具会自动解码JWT的Header和Payload，显示算法（比如HS256）、用户信息等，确认算法是HS256后，再进行下一步。

步骤2：字典暴力破解密钥

运行命令（jwt替换成目标JWT，jwt-common.txt替换成你的字典文件路径）：

```
```
python jwt_tool.py jwt -C -d jwt-common.txt
```
```

工具会自动用字典中的密钥尝试验证签名，破解成功后，会显示“Found secret key!”，并输出破解出的密钥（比如jwt-secret-key）。

补充：如果知道具体密钥，也可以直接验证，命令如下（password\_here替换成猜测的密钥）：

```
```
python jwt_tool.py jwt -C -p password_here
```
```

步骤3：用破解的密钥伪造新JWT

破解出密钥后，就可以修改Payload中的信息（比如提升权限），再用密钥重新签名，生成合法JWT。

运行命令（jwt替换成原JWT，hs256替换成目标算法，jwt-secret-key替换成破解出的密钥）：

```
```
python jwt_tool.py jwt -S hs256 -p jwt-secret-key
```
```

执行后，工具会生成新的JWT（已用正确密钥签名），将这个新JWT发给服务器，即可成功绕过认证。

案例：

1. 用户登录后获取用户会话jwt：

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLd4DS1ef1EiaZZqCbiald90deShQG0ibbWFiaTtwrUdh2PPeCfLGoQiaVKoBh2u8J9Q2SHYnbVBol2qbP5dTCJPVpl1HPHbmJ56rvic8/640?wx_fmt=png&from=appmsg)
2. 使用jwt\_tool爆破密钥，爆破出弱密钥为secret1

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfs8Viba5cFdZsx8My7rFlQKPf0hzIXdTAqeeteFxdjZVkyCynwpSyFp8orxXQBWfDq0A193RbVf79MpMDaD99SJTRxP8XXQZicA/640?wx_fmt=png&from=appmsg)
3. 修改用户为管理员，利用爆破的密钥重新生成jwt

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLdtQiaqJJljposC0IhzTubI1CXbOGkuNrE9ic2Pb2abXKzFLk68A8wYpJrJibUPic55Vl2AaJ9qhOsZaDk9b5vs16Rg3ptp1NhuTBo/640?wx_fmt=png&from=appmsg)
4. 利用生成的jwt，成功获取到管理员账号数据

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfRtYn6vdayiafmrhV3jec6o8dom8VxOkrQcRhpgUcALyyiaqU5dfibF468JDv5yVAUiawjynTrlzUl1Cbrw73m1g8hrqZP7RibAZAs/640?wx_fmt=png&from=appmsg)

PART 03

补充：JWT漏洞防御建议

了解漏洞的同时，更要知道如何防御——不管是开发还是测试，都要牢记这几点，避免踩坑：

* 必须验证签名：服务器端一定要验证JWT的Signature，确保未被篡改，不要只验证Payload内容；

* 严格验证算法：禁止使用alg:none算法，服务器端要明确指定允许的签名算法（比如只允许HS256、RS256），拒绝未知算法；

* 密钥要足够复杂：使用HS256算法时，密钥要设置为长字符串（建议16位以上，包含字母、数字、特殊符号），避免使用简单密码，定期更换密钥；

* 避免敏感信息泄露：Payload中绝对不能放密码、手机号等敏感信息，Base64编码可轻易解码，无任何保密性；

* 缩短JWT有效期：设置合理的过期时间（比如1小时），减少JWT泄露后的风险，过期后强制重新登录。

PART 04

最后总结

JWT本身是安全的，但漏洞往往出在“人为配置”上——未验证签名、未限制算法、密钥过于简单

对于渗透测试者来说，掌握漏洞的检测和利用方法，能快速突破目标系统的身份验证；对于开发者来说，牢记防御建议，能从源头避免JWT带来的安全风险。

公众号后台留言：jwttool获取工具

扫码加入我们的交流群，群内分享众测项目漏洞挖掘技巧~

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfmmR5bbPSfHJzs11biaR8VqFiaofzzqIS0xhKTnjsMwhLGcZBTyWzcH65ibpJdT37YPn48PStsyKyNu2YQIUNchc8gA6RSLJrtng/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icJLfUrOKojQ3l96TfOS0sgD4ERSJOMSfkfz3SuXv7357q72NSNPkPOhby4rw6Pz17t336gHGQ8VeWOeos6Crbw/0?wx_fmt=png)

小石学习笔记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icJLfUrOKojQ3l96TfOS0sgD4ERSJOMSfkfz3SuXv7357q72NSNPkPOhby4rw6Pz17t336gHGQ8VeWOeos6Crbw/0?wx_fmt=png)

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