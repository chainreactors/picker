---
title: 改了一个目录参数，我上传的图片替换了别人网站首页：2026年OSS直传签名越权实录
url: https://mp.weixin.qq.com/s/pKKhOeunwErfQnTWdz23VA
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:48:23.473058
---

# 改了一个目录参数，我上传的图片替换了别人网站首页：2026年OSS直传签名越权实录

# 改了一个目录参数，我上传的图片替换了别人网站首页：2026年OSS直传签名越权实录

原创

www.KLSEC.COM
www.KLSEC.COM

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

上周测一个在线教育SaaS。我在个人设置里上传了一张测试图片，Burp抓到了前端直接上传到阿里云OSS的请求。请求头里带着`x-oss-security-token`和`x-oss-credential`，说明用的是STS临时凭证。但更关键的是，请求体里的`key`参数——也就是文件在OSS里的存储路径——是明文的：`uploads/avatar/user_88421/test.jpg`。

我把它改成了`uploads/../../index.html`。上传成功。然后我访问那个网站首页，看到的是我上传的图片。如果那不是图片而是一段HTML/JS代码，首页已经被我接管了。

这不是什么高深的攻击。它利用的是OSS直传中一个根深蒂固的信任错位：**前端生成的签名凭证，在后端看来是“已完成身份校验”的通行证。但前端可以决定这把通行证用在哪个路径上。**

**一、OSS直传的信任边界：签名验的是“你是谁”，不是“你往哪传”**

要理解这个漏洞，先得搞清楚OSS直传的工作流程。

传统上传是前端把文件发给自己的服务器，服务器再转发给OSS。但这种方式带宽成本高，所以现在流行“直传”——前端从自己的服务器申请一个临时凭证（STS Token或Pre-signed URL），然后带着这个凭证直接向OSS发起上传请求，不经过自己的服务器。

服务器在生成临时凭证时，会附带一个Policy（策略），规定这个凭证能做什么。一个正常的Policy长这样：

```
{  "Version": "1",  "Statement": [    {      "Effect": "Allow",      "Action": ["oss:PutObject"],      "Resource": ["acs:oss:*:*:my-bucket/uploads/avatar/${user_id}/*"],      "Condition": {        "StringLike": {          "oss:Prefix": "uploads/avatar/${user_id}/"        }      }    }  ]}
```

看起来资源被限制在了`uploads/avatar/${user_id}/`目录下。但问题在于：**OSS在验证签名时，验证的是“这个请求是否由持有有效凭证的调用者发起”，而不是“这个请求的路径是否在凭证最初设定的范围内”。**

如果STS Token的权限给的是`oss:PutObject`，而Resource写成了`acs:oss:*:*:my-bucket/*`，那攻击者就能往Bucket里的任意路径写文件。如果Resource写对了但后端没有在服务端对`key`参数做二次校验，攻击者就可以在前端把`key`从`uploads/avatar/user_88421/test.jpg`改成`uploads/../../index.html`，路径穿越到Bucket根目录甚至更上层。

2026年的真实案例：某企业OSS直传策略中，STS权限被错误地赋予了整个Bucket的写入权限，攻击者通过篡改前端参数，上传了一个伪装成PDF的`/etc/shadow`文件，该响应被CDN缓存后，HR员工点击链接的瞬间就把服务器密码哈希交到了攻击者手里。

**二、三种攻击形态：从改目录到接管Bucket**

在我过去半年的测试中，OSS直传签名漏洞主要有三种利用方式。

**形态一：`key`参数路径穿越**

最直接的一种。上传请求中的`key`参数（或`object_name`、`filename`、`path`）由前端控制。后端不校验这个`key`是否真的在用户自己的目录下，只校验了请求的签名是否有效。

攻击者构造`key=uploads/avatar/../admin/config.json`或`key=../../index.html`。如果OSS的路径规范化逻辑（WHATWG URL算法）在签名之前把`..`折叠掉，签名的路径和实际写入的路径就会不一致。CVE-2026-73658就是典型：Trigger.dev的签名客户端在签名前把`url.pathname`设置为用户控制的key，WHATWG算法折叠`..`段，导致签名URL指向了租户前缀之外。

**形态二：`dir`参数篡改（我这次用的手法）**

有些系统不直接传完整的`key`，而是把路径拆成`dir`（目录）和`filename`（文件名）两个参数。后端生成签名时，用`dir + filename`拼出完整路径。如果后端信任了前端传来的`dir`，攻击者就可以把`dir`改成任意路径。

我的测试中，请求体是：

```
{  "dir": "uploads/avatar/user_88421/",  "filename": "test.jpg"}
```

我把`dir`改成`uploads/avatar/user_88421/../../../`，`filename`改成`index.html`。后端拼接后的路径是`uploads/avatar/user_88421/../../../index.html`，OSS解析后落在Bucket根目录。如果该网站的前端部署在同一Bucket的根目录，首页就被我替换了。

**形态三：签名URL的`Key`值绕过**

这是2026年2月阿里云OSS Python SDK V2暴露的一个严重问题：Pre-signed URL的Key值校验存在缺陷，攻击者可以修改URL中的Key值上传任意文件，且预设的超时时间形同虚设——设为60秒有效期的URL，数小时后仍可正常使用。

这意味着：即使你拿到的是一个“只能上传这一张图片”的签名URL，你也可以把它改成一个“可以上传任意文件到任意路径”的万能URL。临时授权机制完全失效。

**三、实战：从一张头像到首页替换的完整攻击链**

下面是我在在线教育SaaS上测试的脱敏过程。

**目标：** 某在线教育平台，用户头像上传使用OSS直传，前端直接向`my-edu-bucket.oss-cn-hangzhou.aliyuncs.com`发起PUT请求。

**第一步：正常上传，抓包**

上传一张测试头像，Burp抓到的请求：

```
PUT /uploads/avatar/user_88421/test.jpg HTTP/1.1Host: my-edu-bucket.oss-cn-hangzhou.aliyuncs.comx-oss-security-token: CAISuQJ1q6Ft5B2yfSjIr5bdI...x-oss-credential: LTAI5tRmhx5JSrbvuNF4WQbs/20260910/cn-hangzhou/oss/aliyun_v4_requestx-oss-signature: a3f9c2e1b8d74f6a...Content-Type: image/jpeg
[二进制图片数据]
```

路径`/uploads/avatar/user_88421/test.jpg`直接在URL里，明文可见。

**第二步：测试路径穿越**

我把URL里的路径改成`/uploads/avatar/user_88421/../index.html`，请求体换成一段HTML代码。OSS返回200。说明签名没有绑定到具体路径。

**第三步：测试更激进的穿越**

我尝试`/uploads/avatar/user_88421/../../../../index.html`。仍然成功。OSS的路径规范化把`..`折叠后，文件落在了Bucket根目录的`index.html`。

**第四步：确认首页替换**

该SaaS平台的前端静态文件（HTML/CSS/JS）就存放在这个Bucket的根目录，通过CDN加速对外提供服务。我访问他们的主域名，看到的是我上传的HTML页面——一个测试用的“此站点已被安全测试，请联系管理员”的提示页。

如果这是一次真实攻击，我可以上传一个钓鱼页面，窃取所有访问者的登录凭证。

**第五步：测试其他路径**

既然能写到根目录，我尝试写入`/uploads/avatar/user_88421/../../../.well-known/acme-challenge/`目录——如果能控制这个目录，我就能为该域名申请任意SSL证书。测试成功。

**四、为什么这个漏洞在2026年还如此普遍？**

**1. STS权限过大。** 很多团队在生成STS临时凭证时，为了“图方便”，把Resource设置成了`acs:oss:*:*:my-bucket/*`，而不是精确到用户目录。这样攻击者拿到凭证后，就能往Bucket里的任意位置写文件。正确的最小权限应该是`acs:oss:*:*:my-bucket/uploads/avatar/${user_id}/*`。

**2. 后端不校验前端传来的路径参数。** 后端信任了前端传来的`dir`或`key`，没有在服务端重新计算用户应该有的路径，然后与前端传来的路径做比对。只要签名有效，后端就放行。

**3. OSS的路径规范化逻辑与业务预期不一致。** OSS在处理`..`时，会按照WHATWG URL标准折叠路径。这意味着`uploads/avatar/user/../index.html`在OSS看来就是`uploads/avatar/index.html`。如果业务代码在签名时没有做同样的规范化，签名和实际路径就会不一致。

**4. Pre-signed URL的Key值校验缺陷。** 如阿里云OSS Python SDK V2的问题所示，签名URL的Key值可以被修改，超时时间也不生效。这放大了漏洞的利用范围。

**五、防御：把路径控制权收回到服务端**

**1. 服务端重新计算路径。** 不要信任前端传来的`dir`或`key`。后端根据当前登录用户的身份（从Session或JWT中读取），重新计算该用户应该有的上传路径，然后生成签名。前端只能决定文件名（且文件名要经过严格的字符过滤），不能决定目录。

**2. STS权限最小化。** 生成STS凭证时，Resource精确到用户目录：`acs:oss:*:*:my-bucket/uploads/avatar/${user_id}/*`。不要用通配符覆盖整个Bucket。如果业务需要跨目录，单独授权，不要图省事给大权限。

**3. 路径规范化后做前缀校验。** 如果业务确实需要用户传路径（比如多级目录），在服务端对路径做规范化（折叠`..`、解码URL编码），然后校验规范化后的路径是否仍然以用户目录为前缀。不是前缀就拒绝。

**4. 使用V4签名，弃用V2。** V4签名对路径的处理更严格，对`..`和URL编码的规范化逻辑更接近RFC标准。V2的签名宽限缺陷已经被证明可以被利用。阿里云、AWS、腾讯云都已经推荐迁移到V4。

**5. 监控异常上传路径。** 在OSS的日志中监控包含`..`、`%2e%2e`、`//`的`key`，以及上传到非预期目录（如Bucket根目录、`.well-known/`）的请求，触发告警。

**六、写在最后**

OSS直传签名漏洞的根因，是**把信任边界搞错了**。前端是攻击者完全可控的环境，它传来的任何东西——路径、文件名、Content-Type——都是不可信的输入。后端可以信任“签名”来验证调用者的身份，但不能信任“签名”来验证调用者的意图。

我见过太多团队，在Web应用层做足了鉴权、越权、注入的防护，却在OSS直传这一层把大门敞开。因为云存储看起来“不是代码”，是“基础设施”。但攻击者不管这些，他看到的只是一个可以上传任意文件到任意路径的API端点。

下次你测一个用了OSS直传的系统，别只看它的业务逻辑漏洞。抓上传包，改路径，试穿越。你可能会发现，整个Bucket都在等你写入。

**严正声明**
本文所述技术仅用于合法授权的安全测试。所有案例均已脱敏处理，测试均在SRC平台授权范围内进行。利用OSS签名漏洞进行未授权上传或覆盖属于违法行为，与作者无关。请遵守法律法规，守护云上数据安全。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zL8x37G6prKFHZF4gTaajT0RYoRj81C6Rod7btfah6ZiaFaxIibKsVXNU7SMqnZia2FOtCYLFFgMor803P3ysbiba9ruW8LoMzjQw/0?wx_fmt=png)

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