---
title: Apache NiFi 连爆四漏洞，权限失控与内存炸弹问题亟待修复
url: https://mp.weixin.qq.com/s/zbQk3U7q_UquNiiKogsI2Q
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:55:26.915576
---

# Apache NiFi 连爆四漏洞，权限失控与内存炸弹问题亟待修复

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0FicBfdA9I42SLeGx6Fhsdr36Q1tCpOicSFUkQjlH9oqYNNnuYNNnibk3cYiacpHHgdCcFTLQKxJlvThyvQsgBbJwTaDE7uDuT7iaw/0?wx_fmt=jpeg)

# Apache NiFi 连爆四漏洞，权限失控与内存炸弹问题亟待修复

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，Apache NiFi 项目组一次性发布了四个安全漏洞的修复公告，涉及权限校验绕过、参数验证滥用以及内存耗尽型拒绝服务攻击。**所有漏洞均在 2.11.0 版本中完成修复，**官方呼吁用户尽快升级。

这四枚漏洞分别瞄准了 NiFi 的核心参数管理机制和 Web API 接口，攻击面广，**影响版本跨度从 1.5.0 一直延伸到 2.10.0。**

**1**

**高危风险一：只读用户竟能“偷改”配置（CVE-2026-62354）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1ibP4zWKPPU7icNdmDAUA2qVcDtlYiba9h1ZnXy15Sq3VbELTSmCLCqu7L4JEA6cJTop9ckibK5HVjKf7gqNHJYDA30CduqXYeibZw/640?wx_fmt=png&from=appmsg)

影响版本：1.10.0 – 2.10.0

严重程度：高危

该漏洞存在于参数上下文的验证请求中。**原本只拥有“只读”权限的用户，竟然可以在提交验证请求时夹带“私货”——即自定义的参数值。**系统在验证过程中会临时采用这些外部传入的值，从而覆盖掉当前正在使用的配置。

这就好比给了访客一张“参观证”，结果访客却能顺手修改工厂流水线的工艺参数。**攻击者虽然不能直接写入配置，但可以通过反复验证摸清系统反应，甚至让验证逻辑跑出预期结果。**从 2.11.0 开始，提交验证请求必须拥有写入权限。

**2**

**高危风险二：小压缩包制造“内存黑洞”（CVE-2026-68981）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1qcVAqsoXXF3gpzAYRz7NkZ88CHEfuiaicfSbbNTBicSMY6XfNJ1MDvSDE9AXTBbbsk7k7ctNwzJiaAg5wdXnJRavJuPP5uUXb8NE/640?wx_fmt=png&from=appmsg)

影响版本：1.5.0 – 2.10.0

严重程度：高危

这是一个典型的“放大器”攻击。NiFi 的 REST API 原本会限制请求体的大小，但**限制只针对压缩前的体积，而非解压后的真实数据量。**

攻击者只需发送一个很小的 gzip 压缩包，解压后却可能膨胀数千倍，瞬间占满服务器内存，导致服务响应缓慢甚至直接崩溃。**这类似于传说中的“Zip Bomb”攻击在 API 场景下的翻版。**新版本在 Jetty 服务端层面处理压缩逻辑，并关闭了对 gzip 请求的解压支持，从源头堵住了这一风险。

**3**

**中危隐患：改一个参数，动全局组件（CVE-2026-68979）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0daDPica78vBK3bsKvxicZYudibjb7libpU6bq5ibLLF733Yg6tDW5gcar4LKOnF2SCotdDFZSNKLEiaFtP86uyTNCSP70OXV0gdbicw/640?wx_fmt=png&from=appmsg)

影响版本：1.10.0 – 2.10.0

严重程度：中危

这是一个**权限蔓延**问题。当用户被允许修改某个参数上下文中的值时，NiFi 并未向下校验那些引用该参数的组件是否也属于该用户的管辖范围。

这就导致了一种“越权操作”：**你可以修改一个不属于你管理范围的处理器里的参数值。**更危险的是，如果该参数恰巧包含一段可执行脚本，且该组件处于停止状态，系统在自动验证时可能会触发脚本执行。官方强调该场景利用条件较为苛刻，但仍建议立即修复。2.11.0 已补全针对所有引用组件的鉴权逻辑。

**4**

**低危但需警惕：删错资产的“乌龙指”（CVE-2026-68980）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1DY3EGAicDibRoPOKrMFq3wR7jnRDlrqyqxc01ZLYHvylaGXlc212I10nDqLYQtUeIeB0zCUGf9ZibvniciaC1muQCve2rpdanjBxc/640?wx_fmt=png&from=appmsg)

影响版本：2.0.0 – 2.10.0

严重程度：低危

在资产删除操作中，API 仅校验了用户提供的参数上下文 ID 是否合法，却没有核实待删除的资产是否真的属于该上下文。在启用了细粒度权限策略的多租户环境中，这可能导致用户误删其他上下文中的资产。新版本已增加所有权确认步骤，防止“张冠李戴”。

**5**

**安全建议**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0jTpoSrg9IHw8fsIeeibEyDUnjia4ZAbOgXxzesC4OicIeb5s36rH5dedRcWst0awyaSE5d8BHwRn9y0VRzgFnKgPBX6vB5q4GkE/640?wx_fmt=png&from=appmsg)

如果您正在使用 Apache NiFi 1.5.0 至 2.10.0 之间的任意版本，请立即将部署升级至 2.11.0。

升级后，请同步检查参数上下文的读写权限策略，并重点排查含有脚本内容的参数值，尤其是那些关联到停止组件的参数。

*资讯来源：cybersecuritynews*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1FDtnr5zibNS26DiaIFCJqjBIbrW1wj5VPwy3Gp1INNUc5DJcliaQza6uIUqUkYBiaOFmTCzyiceQwl6omDicUVcKSnJvq9h9kocrVc/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K2csoNBPibJ5yBkicM9IWNvuJF2zwACV8Jpk089llOReuialAZlxrERoQFPmLyE8wM4fbxAx8ictaT2Mlic16vD8j8zORNggQQWrvFk/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K2ZGE8y5XJjibicmgibPian1Xu0w1wrJz8jQyDlxibEN8pLTH6iakZ8mZq1IUj33rkWcunoF5xbyrJBibDIK4ibk1Ylbx9lCzbL0gH5SLY/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K1SoMzconMFSsU5m9TB9a9Wg3HHXGS156abuuPzXV29M7W4k0Mej6AzNkjHz2aNpsJEBkVibhxbFJvQwfFG0ibYXdncY1ZhkKgibc/640?wx_fmt=gif&from=appmsg)

**球在看**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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