---
title: 挖了几天0收获？新手SRC挖洞的【3大核心技巧】与【8大避坑指南】
url: https://mp.weixin.qq.com/s/I1aP1_eoD86Hgz75OicZUA
source: Doonsec's feed
date: 2026-07-30
fetch_date: 2026-07-31T05:27:14.138922
---

# 挖了几天0收获？新手SRC挖洞的【3大核心技巧】与【8大避坑指南】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kzUNKm24hOqn4jnbU59ebgzAickicklu6tb935ic9yex6iaSgstnFToHKQnFEUCZxLEmHFTcGWMcIVksnnELdgaibcvjxiadibMSY5uHmxdSibXkiabI/0?wx_fmt=jpeg)

# 挖了几天0收获？新手SRC挖洞的【3大核心技巧】与【8大避坑指南】

沧海讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多新手刚接触SRC漏洞挖掘时，满腔热情地冲进去，挖了几天毫无收获，就开始怀疑自己是不是不适合这行？

![你选择冷落她,会让她陷入自我怀疑,她不知道自己做错了什么](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9Rsjyfh2K05ZrHaicdKeeAIoYUdhzfsnSWFZ0IxKIErBVGhW3JaIyjSbptNeKNGHE0DscVWxSXRiaR73MAuurBNiblHnH0Vx7ZxW0/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

其实，挖不到洞往往不是技术问题，而是**方法和方向出了问题**。

今天这篇文章，我会把新手最需要的 **3个核心技巧**和 **8个高频避坑点**讲透，帮你快速找到方向、少走弯路。

---

### 🎯 技巧一：深耕边缘资产

这是新手最容易忽略、却最能快速出成果的策略。

#### 为什么不要碰主站？

企业的主站通常经过多轮安全测试、WAF防护、代码审计，漏洞早已被反复清理。你面对的不是一个网站，而是一整支安全团队。新手硬刚主站，大概率是浪费时间。

#### 什么是边缘资产？

边缘资产是指企业名下**非核心、非主站**的各类线上资产，它们往往防护薄弱、测试不充分，是新手挖洞的"富矿区"。

常见的边缘资产包括：

* **子域名**：如`test .example .com、dev .example .com、old .example .com`

* **小程序 / APP内嵌H5页面**：前端代码可反编译，后端接口可能缺少鉴权
* **旧版系统**：如 `v1.crm.example.com`，常年不更新，存在大量已知漏洞
* **新上线业务 / 活动页面**：如 activity .example .com 赶工期上线，安全测试不充分
* **第三方集成服务**：企业接入的支付、统计、客服等第三方组件

> 💡 核心思路：主站是"别人啃过的骨头"，边缘资产才是"还没人碰过的蛋糕"。新手要从蛋糕入手，而不是去抢骨头。

---

### 🎯 技巧二：关注新上线业务

企业新上线的业务，漏洞发现率远高于成熟业务，这是SRC挖洞领域公认的规律。

#### 为什么新业务漏洞多？

* **安全测试不充分**：很多新业务为了赶上线节点，安全测试被压缩甚至跳过

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QzkCVPkPG61kJNwsibQrvWM9XQfZNffUeGAKibMFDQr5iaWkBbD5niaKnXLvPmibBWdo8dRp3dAllZqFoUsnZviaQRYt353TntibdF4A/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

* **开发团队安全意识参差不齐**：新功能由不同团队开发，安全规范执行不到位
* 没有经过实战检验：旧业务经过多年白帽子测试，漏洞基本被清理干净；新业务则是一块"处女地"
* 代码变更频繁：新功能上线初期迭代快，容易引入新的安全问题

据统计，新上线业务的漏洞率是成熟业务的**3倍以上**。

#### 如何第一时间发现新业务？

**渠道一：SRC平台公告**

大多数SRC平台（如阿里ASRC、字节ByteSRC、腾讯TSRC）会在官网或公众号发布"新增测试范围"公告，第一时间关注这些公告，你就能抢在别人前面测试新资产。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9QwccquViagZJmPhpWIRJ45jPeiaNBkUtBe0OQdj044FhfW2wtR4a4BSWh4vqOMqiak13fMuKYN9HF6ias8wNCC6x5rxFEHQzZFYxQ/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**渠道二：企业官方动态**

关注目标企业的官方公众号、产品更新日志、应用商店的版本更新记录。当企业发布新版APP、上线新活动页面时，第一时间去测试。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9THrhKLDC1pQx6ibicNuA5vDUmYnj1Czdv2cPVib0793aIRcvsMQeiabzXttAibQKs5wb1B3jwc4xyznNwQpSbzHePmrr6yFgTqqztU/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**渠道三：子域名监控**

定期对目标域名做子域名收集，对比历史数据，新出现的子域名往往就是新上线的业务。例如，你上个月收集到的子域名列表里没有 `promo.example.com`，这个月突然出现了，那它很可能是一个新的营销活动页面。

> 💡 核心思路：新业务的漏洞有一个"窗口期"，越早发现、越早提交，成功率越高。养成定期监控新资产的习惯，是新手拉开差距的关键。

---

### 🎯 技巧三：多看公开报告

新手最大的误区之一是"闭门造车"——不看别人的成果，自己闷头摸索。事实上，**模仿是最高效的学习方式**。

#### 为什么要看公开报告？

各大SRC平台会定期公开部分漏洞报告，这些报告是真实场景下的挖洞案例，包含了完整的：

* **信息收集方法**：别人是怎么找到目标资产的
* **漏洞探测思路**：别人是怎么发现漏洞的
* **Payload构造技巧**：别人用了什么样的测试语句
* **报告编写规范**：别人是怎么写复现步骤的

读10篇高质量公开报告，胜过盲目打100次靶场。

#### 怎么看报告才有效？

不要只是"看一遍就过了"，建议按以下步骤拆解每篇报告：

**第一步：还原信息收集路径**

看作者是从哪个入口找到目标资产的，用了什么工具、什么语法，能不能复现他的信息收集过程。

**第二步：理解漏洞触发逻辑**

不要只记Payload，要理解"为什么这个Payload能触发漏洞"。比如看到一个SQL注入的Payload是 `' OR 1=1 --`，你要理解它的原理是"闭合原始SQL语句，构造永真条件"。

**第三步：举一反三，迁移到自己的测试中**

看完一篇"未授权访问"的报告后，下次你遇到类似的后台管理页面，就应该主动尝试直接访问 `/admin`、`/api/user/list` 等路径，验证是否存在同类漏洞。

> 💡 核心思路：公开报告就是你的"免费导师"。每天花30分钟拆解1篇报告，坚持一个月，你的挖洞思路会有质的飞跃。

---

### ⚠️ 新手高频8大避坑点

技巧学完了，接下来是同样重要的"防坑指南"。以下8个坑，几乎每个新手都会踩，提前记住，能帮你避免大量无效劳动。

* #### 避坑1：不看平台规则，盲目测试

每个SRC平台都有明确的测试范围（哪些域名可以测、哪些不能测）和禁止行为（不能DoS、不能爆破用户数据等）。

* **建议**：注册平台后，第一件事就是通读测试规则，把授权范围截图保存。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/CsKJlMFPH9T1tNpBj8H6GaBCDiclySeTfoFeQ9vfBgskpqkqjpRBOvOs3dJGC2WlqJ2ia4hvY0ccNlia7cQlpQLrLWGiciaIYJWmLoBOmRBeI74A/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

* #### 避坑2：报告写得模糊，无法复现

审核人员每天处理大量报告，如果你的报告复现步骤不清晰、截图不完整、Payload缺失，审核人员无法复现，只能直接拒绝。

* **建议**：报告按"漏洞标题 → 漏洞描述 → 复现步骤（分步截图） → 修复建议"的模板来写，确保任何人照着步骤都能复现。

* #### 避坑3：提交无危害的"伪漏洞"

简单的页面报错、排版问题、404页面、无关信息泄露，这类"漏洞"不会被收录，还会拉低你的账号权重，导致后续报告审核变慢。

* **建议**：提交前自问——"这个漏洞如果被恶意利用，能造成什么实际危害？"如果答不上来，就不要提交。

* #### 避坑4：急于求成，直接挑战高危漏洞

新手一上来就想挖RCE（远程代码执行）、0day，难度太高，不仅挖不到，还会严重打击信心。

* **建议**：循序渐进。先从信息泄露、未授权访问、反射型XSS等低危漏洞入手，积累经验后再进阶到SQL注入、逻辑漏洞、越权等中高危漏洞。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9TZ4ibVIICllg1Hga0fZNg2rCyacBehlTS0OvGUkhrc5tGbibibMfNfDWTkrzFA1QSlmnCBiasUoY3jvOoo7BEDUBCiakgPDr7ZXzsY/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

* #### 避坑5：窃取、传播敏感数据

即使你在测试中发现了用户数据、系统配置等敏感信息，**仅需截图证明漏洞存在即可**，严禁下载、留存、传播任何敏感数据。

* **后果**：触碰规则红线，可能承担法律责任。这不是危言耸听，是法律底线。

* #### 避坑6：重复提交、伪造漏洞

提交前一定要在平台查询该漏洞是否已被他人提交。伪造漏洞截图、编造复现步骤，会被平台扣除积分、拉黑，取消所有奖励。

* **建议**：每次提交前，搜索平台已公开的同类漏洞，确认没有重复。

* #### 避坑7：工具使用不熟练，误判漏洞

没有熟练掌握Burp Suite、SQLMap等核心工具，容易把正常现象误判为漏洞，提交大量无效报告。

* **建议**：先在DVWA、Pikachu等靶场把工具练熟，再投入实战。工具是武器，不会用武器就上战场，只会伤到自己。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QsX2nOWyOibch6NfGVcfmowu0zEIPD5ibS8y2Bckf7v9ogMH5A4N21Q0tOzUKU6565kicOibo2G40FcVEV9HwLS0VGqBL2rRLYvfE/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

* #### 避坑8：心态浮躁，半途而废

新手挖了1-2天没出成果就放弃，这是最常见的"死法"。SRC挖洞需要耐心和细心，大多数新手的第一个有效漏洞，都是在坚持1-2个月后出现的。

* **建议**：每天按照正确的学习路线投入1-2小时，保持节奏，不要追求"一天挖10个洞"。心态决定成长速度，坚持本身就是竞争力。

挖洞这条路，拼的不是天赋，是**方法论+耐心**。找对方向，坚持执行，你的第一个漏洞，可能就在下一次测试中。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QDvyzKSNwveRic2RWVW47Yic0gE2ic3haP2zrJFp4N0O3gvwNB4hibciaFy2EiaHeqO9YbSeOhyGJuERGORhNIxicdu4ibqbk7lrKkXeY/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

---

---

「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

**沧海专属黑客/网络攻防技术资料**

@沧海讲安全：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

**部分技术资料预览**

**01**

***视频教程***

从0到进阶主流攻防技术视频教程（包含红蓝对抗、CTF、HW等技术点）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcYaRKqWc1cxP8sBrX6KZasFTJEVibWmdyoGAuRO4AbzaVjUJ8guoWAzQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcCP8oaOCQm8Cp2qhpCxWiaOjzYrOoA1iac5eSafBicPxSQcpYtchyfVvxA/640?wx_fmt=jpeg&from=appmsg)

**0****2**

***书籍Pdf***

入门必看攻防技术书籍pdf（书面上的技术书籍确实太多了，这些是我精选出来的）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcUumOTUmUznuo7MzKl1JiaEQIeSh4ibkO6jxY68zVZz7iayrwGRtGu2bHw/640?wx_fmt=jpeg&from=appmsg)

**0****3**

*安装包/源码*

主要攻防会涉及到的工具安装包和项目源码（防止你看到这连基础的工具都还没有）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcvsT9h4B1hS9VEPengMcOtNL24949kb4cibKLS9HkIb1k2htW8GYqzMQ/640?wx_fmt=jpeg&from=appmsg)

**0****4**

***面试试题/经验***

网络安全岗位面试经验总结（谁学技术不是为了赚$呢，找个好的岗位很重要）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6Kqcm6J0eAql29R6DIM8bJW4rweVBicM8ibGMOmLNFTpdcQ0gFvefMTOg9dA/640?wx_fmt=jpeg&from=appmsg)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

@沧海讲安全：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kWXbooRKsCUic8In0GE4Hd6nTM7iclEUG0UewS479kicpBqGcfpOAaTibhgwsEsblvqe0EsP95XKBe2E90T9g02cQg/0?wx_fmt=png)

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