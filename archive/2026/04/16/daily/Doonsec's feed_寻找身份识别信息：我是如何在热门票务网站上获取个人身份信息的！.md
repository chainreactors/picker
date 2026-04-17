---
title: 寻找身份识别信息：我是如何在热门票务网站上获取个人身份信息的！
url: https://mp.weixin.qq.com/s/nnRc0y-WnaTW1uJX9wwFfQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:48:44.620138
---

# 寻找身份识别信息：我是如何在热门票务网站上获取个人身份信息的！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnsBXiaSVmPwXUfEjCIMBm2uNfb3E3YFlSK9ySygEMw1W1z5B0ibSUSjojqcQ8d405GnfVocPWIhqUknouiawMoKBjv4BlMO6o3tibY/0?wx_fmt=jpeg)

# 寻找身份识别信息：我是如何在热门票务网站上获取个人身份信息的！

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

## 侦察阶段

目标平台是一个广泛使用的机票、火车票和巴士票预订平台。我的方法通常是先以已认证用户的身份梳理核心功能，密切关注应用程序如何处理用于数据检索的 API 请求。

我进入了账户中记录失败机票预订的部分。为了了解具体情况，我将浏览器流量通过代理服务器路由，然后点击查看其中一笔失败交易的详细信息。

## 发现漏洞

查看 HTTP 历史记录时，我注意到一个标准的 GET 请求，用于获取预订详情。该请求依赖于作为参数传递的特定行程标识符（例如，trip-id=[已编辑]）。

这种行为立即引起了我们的警觉。该应用程序似乎仅仅依赖用户提供的标识符，而没有充分验证已认证的会话令牌是否真正拥有该特定资源。如果后端只是简单地解析 ID 并返回数据库条目而不进行授权检查，则很容易受到 IDOR 攻击。

按回车键或点击查看完整尺寸的图片

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnuK740HC2MeHbOiaHPG7Y25vwOIxiblribIshvDsAj5kDqIkGBp1Hc5RvHUlbYAzicmjibums5gzicD5lia8ibeQcZTRzJGJibkrJulkfbU/640?wx_fmt=jpeg&from=appmsg)

## 行业工具

为了验证并记录这一发现，我采用了一种简单但有效的技术栈：

* Burp Suite（代理和HTTP历史记录）：对于拦截初始请求和识别易受攻击的GET端点及其参数至关重要。
* Burp Suite（Repeater）：用于手动修改 trip-id 参数，并验证服务器是否返回了 200 OK 状态和数据，以确认不存在授权检查。
* Burp Suite（Intruder）：用于自动化攻击阶段。我针对预订标识符的后四位数字进行攻击，并通过模糊测试来展示漏洞的规模。
* ChatGPT：API 响应返回了一个庞大的、未格式化的 JSON 数据块，其中包含了泄露的用户数据。为了让我的概念验证清晰明了，便于分诊团队理解，我使用 ChatGPT 立即解析了原始 JSON 数据，并将受害者的数据（例如 PNR、票价和联系方式）以清晰、带标签的摘要形式呈现出来。

工具设置完毕后，我将截获的请求发送到 Burp 的 Intruder 选项卡。我没有猜测完全随机的字符串，而是选择了预订 ID 的最后四位数字（例如 4697），并使用一系列数字运行有效载荷攻击。

结果立竿见影：多个请求（例如 5206、2949 和 4588）均返回了 HTTP 200 OK 状态码。通过检查这些成功请求的 JSON 响应，我发现我可以访问平台上其他用户的完整票务信息——包括那些已成功完成预订的用户。

按回车键或点击查看完整尺寸的图片

![](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnuZ3X46HJpZE5dIPJxuuBQkxOib5icZWRBjxFDaAjINW5kTw29zhS1GfnBGvKok008YetibfyzFe0mhB0Nt8Bj5cD0J7JadkvTEKo/640?wx_fmt=jpeg&from=appmsg)

按回车键或点击查看完整尺寸的图片

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnuia9RokibncR5jYcicqLmQlUIBWI1oNWOJJo5pQavCO2W0N49zwsGibLeafMjleg1ZLCB1zGX8ECorQHKrLxV0bKrqcmyLhuCPXia8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnvibrz5DsGlMvzbX2l0kxGBqL05aicJSNvQJw4PHrFwWZvMiatT89qv1TOqHWAH0jlq1jBzicEGTsic1ac42ib54gmZfKnHUlzelOY4o/640?wx_fmt=jpeg&from=appmsg)

## 影响

该漏洞的严重性非常高。攻击者只需枚举预订 ID，即可通过编程方式窃取大量敏感用户数据，包括：

乘客全名及出生日期；
详细行程安排、PNR编号和电子客票号码；
票价明细及支付网关信息；
联系方式（邮箱和电话号码）。

这种泄露行为会造成严重的隐私侵犯，违反数据保护法规，并为有针对性的社会工程或网络钓鱼攻击打开方便之门。

## 缓解策略

为防止此类漏洞，处理敏感用户数据的平台必须实施严格的访问控制。我在报告中建议采取以下缓解措施：

强制执行服务器端授权检查：在查询数据库之前，务必验证已认证用户是否实际拥有或拥有访问所请求资源的明确权限。

避免直接引用：用间接引用或安全映射的 UUID 替换顺序或可预测的 ID。

安全会话授权：确保根据已登录用户的会话令牌获取敏感数据，而不是盲目信任客户端请求参数。

## 结果

我已负责任地将我的发现（包括详细的报告和视频概念验证）披露给了公司安全团队。他们迅速回应，确认了该漏洞的存在。但是，他们告知我，该问题已在公司内部被发现，目前正在与其他相关发现一起进行跟踪。

虽然这次它被标记为重复漏洞，没有带来赏金，但在如此大规模的生产环境中发现关键的IDOR漏洞始终是一件令人欣慰的事情。这也提醒我们，永远不要想当然地认为应用程序会在你登录后验证你的权限。

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx

##

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBns0d8QwbHTnYHJTtWVKPXdz9LyDdg1OLRibHhZcqA6W7mhw3OzwBKYN7TKwGLSVFtspNNjnOmTAonyoD91iaKvOLEanZVdxUzebo/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsNUop1xm6mAk7KzKpd5Rc68ibM0icgSbe19Snot40Zib0RhuAb4pia8KBXA5vQRNLQRfvDmuPOFpkpibW0MyQnhqkTibGcaNSLb2lbY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

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