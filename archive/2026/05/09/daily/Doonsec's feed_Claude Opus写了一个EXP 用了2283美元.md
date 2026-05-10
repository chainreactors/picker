---
title: Claude Opus写了一个EXP 用了2283美元
url: https://mp.weixin.qq.com/s/EJg9-fa6YaH_wiWXR6gwKg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:29:32.061483
---

# Claude Opus写了一个EXP 用了2283美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lYWDmickZ2myPw6ia4JGF0AU5Npqskkz8SPF20RAvW9aYT8c5h5xoC8o0Rxam9R38FsMWJpg3MJnhCRCGc328o6g2G60qpIlicnV0jQhJLDn3A/0?wx_fmt=jpeg)

# Claude Opus写了一个EXP 用了2283美元

数世咨询

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点亮上方「★星标 」更多干货内容，不再错过！

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mymGPAIkMxIER0whgicBuSkUlN7libnk3jDzsiaDfniaK7K47OK83nFYfr4Y732GY3OAA4dGbpseK70tFuMjt34H2b0fxsdiaYaDiaU8/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542077&idx=1&sn=c63f262d4bb66895352b76087521895e&scene=21#wechat_redirect)

**本文关键看点：**

![](https://mmbiz.qpic.cn/mmbiz_gif/15I7jtE1uriaTpqMbLz5A8YygCg8eaYBUk0tJibjWvQrJONna1vQMDpOOafQaMjkeicDqcD9A02T81IYoKrqzrnzA/640?wx_fmt=gif)

**#****01**

Hacktron的首席技术官使用Opus 4.6完成了针对Chrome浏览器V8 JS引擎的漏洞利用。一周的时间，23亿代币，花费2283美元。

**#****02**

“Mythos是否被过度炒作并不重要。如果不是Mythos，那就是下一个版本或者再下一个版本。最终，任何有耐心和API密钥的脚本小子都能在未打补丁的软件上弹出shell。问题是时间，而不是“是否”。

**#****03**

谷歌和Discord漏洞奖励计划的理论奖金是15,000美元。

********▍********以下正文内容基于英文原文编译，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

Anthropic将Mythos——其漏洞发现模型——保密不对公众开放，因为担心它会让攻击者在任何人来得及反应之前就找到并利用漏洞。

但该公司的Opus 4.6模型（已在周四被 Opus 4.7 发布所超越）已经能够开发出可用的漏洞利用代码。

![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mwE1piaFRcW3G1iatKWicdD4jBK6KJlKWT645TU2bl34yjicczRWS5ic2MQLHCI9gg6VLuxValfjSS1nRWtGtjsR0GYf566wOzIBS18/640?wx_fmt=png&from=appmsg)

周三，Hacktron首席技术官Mohan Pedhapati（s1r1us）在一篇博客文章中描述了他如何使用 Opus 4.6 创建了一条针对Chrome 138中V8 JavaScript引擎的完整漏洞利用链——Chrome 138正是当前版本Discord所绑定的。

"我们使用的V8越界错误来自Chrome 146，与Anthropic自家Claude Desktop运行的版本相同，"他写道。"来回折腾了一周，23亿代币，2283美元的API费用，还有大约20小时是我把它从死胡同里拽出来的时间。终于，弹出了calc。"

"弹calc"是打开计算器应用的俚语——这是概念验证漏洞利用代码中的常用表达，用来表明确认攻击已成功入侵目标系统。

Pedhapati说，虽然2283美元对个人来说是一笔不小的数目，但如果考虑一个人独立开发类似漏洞利用所需的时间，这个成本就微乎其微了。即使再加上Pedhapati调教模型所耗费时间的几千美元，仍然远远低于谷歌和Discord漏洞奖励计划可能给出的理论奖金（约15,000美元）。而这还只是合法市场——谁知道犯罪分子愿意为某个热门的零日漏洞付出多少？

根据Opus 4.7系统卡片，"Opus 4.7在网络能力上与Opus 4.6大致相当。"但明显弱于Mythos Preview，且配有"自动检测并阻止表明禁止或高风险网络安全用途请求的安全防护"。

但对Pedhapati来说，具体用哪个模型并不是问题所在。真正的问题是代码生成能力持续进步，这要求安全姿态和流程必须改变。

"无论Mythos是否被过度炒作都无关紧要，"Pedhapati说。"曲线没有变平。如果不是Mythos，那就是下一个版本，或者再下一个版本。最终，任何有耐心和API密钥的脚本小子都能在未打补丁的软件上弹出shell。这是时间问题，而不是是否问题。"

对于基于Chrome的Electron框架的应用（如Slack、Discord等），真正的问题是：他们何时会将代码库更新到最新版本——而这个版本仍然落后于最新的Google Chrome发布。

Electron 41.2.1（4月15日发布）捆绑了Chrome 146.0.7680.188，仅比当天发布的桌面版Google Chrome（147.0.7727.101/102）落后一个版本。但Electron应用的开发者并不一定会立即更新依赖项并发布新版本，用户也不一定能立即获得这些更新。

Pedhapati说他选择Discord为目标是因为"它运行的是Chrome 138，落后当前版本九个主要版本。"

Pedhapati认为，随着AI模型在漏洞利用开发方面越来越有能力，补丁窗口正在缩小。

"每个补丁本质上都是一个漏洞利用提示，"他争辩道，并补充说，这对开源项目来说尤其困难，因为修复往往在修订版本发布之前就已在代码中公开可见。

他给开发者的建议是：在代码推送之前更多关注安全性，并更密切关注依赖项，以便能够快速做出更改。他还认为安全补丁应该自动执行，这样人们不会因为忘记接受更新而处于漏洞风险中。他还说，像V8这样的开源项目在公开漏洞细节的时机上应该更加谨慎。

"每个公开提交都是对任何拥有API密钥和能够将漏洞武器化的高水平团队成员的发令枪。"他说。

\* 本文为泽钧编译，原文地址：

https://www.theregister.com/2026/04/17/claude\_opus\_wrote\_chrome\_exploit/

注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrGADwibHso9Bicpccu5Oe06s25Kz1rp9KUaUGaHbA3TG9R1iaqOxQbKlzz3q45urLLiaNm3r8x4LowhA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539099&idx=1&sn=8820d80fdc92ac1f321b5e0a3ff0653e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqodJDDGgZLvcLHLjonO6D6SWFh5QdgUTDZJI2uWWhL2pvdicCoic8jhlmXDDmqnUreFaQeJvEMF12dA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539436&idx=1&sn=676908ed11008cd016b253d1d8e6ba8a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjT7Pxib7vCX6T9TTuWQLuAx3KSUpryl4ZvTnpJSBJCZ8SgoowVjD1BVg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540181&idx=1&sn=e0cd678638b098f969f257b408062b91&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrBJ7QP9nU3wQmMvolcOV1gCuk81sv95ev7tRqTxnh4ib8kqibgFJPFxaF0iaKtiaLicoF6B6iaggtVH8Ww/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540845&idx=1&sn=ec923893881e69010ad830ec852b0abb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrgBb4f5DIe21U8to7y1VMziaQ7ahiaKEkib894mtlFoxDBF62D1wGlQNm5vghS5XGSALN6YY4ZFJHJg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539573&idx=1&sn=a721e2933ad640a3a4b3c72f74d76685&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgzKcal7yWn6SZcgqEr0keAmz0xMbg93YD4my88Np43CkMAEdZHXtlxw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514185&idx=1&sn=8015c07a68a5e2b6074efd2c77f20085&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjOQz7r8ibPUG4znENuDuosPYHByfLHsh7jPxvyiaFianIJgfEV9HX4icpbQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539380&idx=1&sn=da5e8afa28247b4212a544750ece924d&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgjAGO2xBRC4TjicDA4jPbLyeLJbhlLs26gV3dyHrBL6O7H33PPeibFoYw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514336&idx=1&sn=e69b1126e86ab2c59c8ca8e315637031&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgaGg7wIzbRTBJwle4uBxXUJcCG0AibMSAKnJ6qdE9l2HgeAWpxfVAfIw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247530968&idx=1&sn=3d712e23b322ad37cee46d27adb08ed0&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoUdBA8wdHsOh02x6PfOicR0fqdOTPLahE5Y2UPZqZ0Viat6BrAJYrzEyDA9CI3N1uP45zwLjHFTysw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538943&idx=1&sn=7f95d33eb069aab1cba23c41d68c9759&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgqUkHibDR3uvnsb4JEozX3XJgFnPQSoMCqWYTZNrr0jvCy11yibml4Wgg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247515942&idx=1&sn=bc9ba104b8eb1c0e914d90c8c9a34542&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg1RBWLvLVSHPqQJ613ib6sKvgDPCfa8wYrog3uFFP8pc4pCycQQ3a0nA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247532302&idx=1&sn=2c6afc5d39c89c86f79020099ea44baa&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg0sUJC8RzqMWibMF0LfCLyEcesDzHTJOlIFyibtUyCZy2bJswaUK56ZdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247512372&idx=1&sn=5d06a830f00953a0ab75157fc023ae56&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg6GdM2ic2q54fZEIdWz3LqKpPODruTaeEzRMArzYJWZD4reLgYGgG6DQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540892&idx=1&sn=4c2c4b434d9731b3181760d45759d47b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcs0NU7ZEWiaTufjAkmrhLqnxywvopoNWA60bErgfSXD17qZ57dkxvue6A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247537068&idx=1&sn=3a3e7c08d93638c1a6018c7862b13bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcsic2hQICquOt1dwrexbbJanpAMLl2UFGG14LgYTzDtOHHSouF067yP1w/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk...