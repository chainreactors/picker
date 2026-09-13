---
title: 私钥未失，4000枚比特币（21亿RMB）却凭空蒸发？Liquid事件撕开网安“遮羞布”
url: https://mp.weixin.qq.com/s/lE4tiEo0kqZ9Aq5E-WUK_g
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:47.955186
---

# 私钥未失，4000枚比特币（21亿RMB）却凭空蒸发？Liquid事件撕开网安“遮羞布”

# 私钥未失，4000枚比特币（21亿RMB）却凭空蒸发？Liquid事件撕开网安“遮羞布”

原创

周小粥
周小粥

周小粥讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**关注**👆🏻公众号→回复“**1**”自取0基础攻防教程

身为网安人总是潜意识秉持一个基本共识：“只要私钥在手，资产便绝对安全。”然而，近期比特币侧链Liquid Network遭遇的安全事件，彻底打破了这一刻板认知。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9SOa6QezVa9Ffp1jmhKbj3QFmv1E619p152k1mR8KIVN9MY8QuDlG10ohDpibiaiaL1A3Tjia4YgFAIa0744tGic16QSQQr834qVwUc/640?wx_fmt=jpeg)

> 近日，Liquid Network的核心储备钱包内的4000枚比特币（价值约21亿RMB）在短短几分钟内被转移，然而官方事后确认：联盟成员的私钥并未泄露，密码系统也未被暴力破解。

钥匙依然完好，资金却凭空消失，这起堪称“教科书级”的安全危机，不仅造成了巨大的经济损失，更暴露出当前网络安全体系中深层次的隐患。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9TbQrtfMjBky0Y4dJqstGPHsxuNOOHtlky3RY8qPoFga14h4MvjJCjB6eaicEpuJ5K0q9Fs4Uwnb3icEbh2DwEjicnUCyJtPicqBIs/640?wx_fmt=jpeg)

---

### 01 | 危害

要理解此次事件的危害，首先需要了解Liquid Network的运作机制。

作为由全球80多家交易所和机构共同维护的比特币侧链，其核心逻辑是：用户将真实的比特币锁定在联盟钱包中，系统再发行等值的L-BTC代币，以提升交易结算速度。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9TQLh7UWiceBlfiajlvLpShzceOoibl9zjl7xZp1rALbZEHHQYP62tCdMgLcUmfnBpOEiah1ofNeEMUHciaJWvPLwGoxJvNH1RGribOI/640?wx_fmt=jpeg&from=appmsg)

* 在此次事件中，攻击者并未直接窃取私钥，而是利用系统漏洞，凭空“铸造”了近4000枚没有真实比特币背书的L-BTC，随后，攻击者通过平台正常的赎回通道，用这些凭空生成的代币，将联盟钱包中的真实比特币全部兑换并转移。

这相当于有人利用系统的规则漏洞，凭空印制了假钞，并成功从银行柜台换走了真金白银。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QWuGq7YpBiaZZkrC3FRAMwxveN9kdMATP1LYEVwTgFDSAOWZbQgf6tKrSdRXJe29gSSXk9SEfLBp9bHam0XLQ9RtyHSyh4WQ08/640?wx_fmt=jpeg)

事发后，联盟钱包的储备资金仅剩不到5%，整个生态的锚定机制面临崩溃，网络被迫紧急暂停交易，行业信誉也遭受重创。

---

### 02 | 原因

攻击者是如何做到“合法”搬空金库的？答案并非高深的密码学破解，而是底层软件Elements中的一个业务逻辑缺陷。

* 在验证交易时，为了降低计算成本，系统会将验证成功的结果进行“缓存”。攻击者构造了一个无效的交易证明，使其恰好命中了缓存中之前验证过的有效结果。系统在检查时，直接调用了缓存记录，跳过了实际的验证计算，从而“合法”地放行了这批伪造的代币。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9QtLMhJBwPgSoS7jC9QGiag7wG0hPdtQZTUnrMJhyUiaa64cncnib12s2vBOrY5Wiag3Su7nq4OYicguEOB2WNFpPxhhjr3lHXKJwnc/640?wx_fmt=other&from=appmsg)

这起事件暴露出行业长期存在的“系统性傲慢”：过度迷信单一防线，将“代码开源”等同于“绝对安全”，将“离线存储”等同于“万无一失”，当底层的业务逻辑出现盲区时，再精巧的密钥管理机制也形同虚设。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9RM3EORziaX48aJRbIXWaREtIplrfNeNKRFN2wuasO8bumesicwWCqiaK368acthhZWAkGBOZEYFaOl7T68xTjRp3G45IZBuOvxJM/640?wx_fmt=jpeg)

---

### 03 | 结果

事件发生后，攻击者在链上留言，自称是“白帽黑客”（即道德黑客），声称此举是为了提示系统缺陷，并承诺在漏洞修复后归还资金。

在开发团队紧急部署补丁后，攻击者确实归还了3400枚比特币，剩余的却被其扣留，并要求项目方支付10%的“赏金”才肯交出。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9SvemlrS2beCSfNZw8C3GoicxaiaCxcQ1womNNZlNI1GMwaKVsqMIBWMfx9SOiciabdwpkOlvaA5ChAKtL2QO9UibxVNrSZzH2cVhicI/640?wx_fmt=jpeg&from=appmsg)

这种“先抽干资金，再谈判要价”的行为在业内争议颇大，真正的白帽黑客通常会选择私下披露漏洞，而非先转移绝大部分资产再谈条件。硬件钱包厂商Ledger的首席技术官公开指出，这种行为“看起来更像敲诈勒索，而非白帽黑客行为”。

目前，剩余资金的归属仍在僵持，网络信任的重建也面临漫长挑战。

---

### 04 | 回归技术

Liquid事件为整个网络安全行业敲响了警钟：这世上不存在绝对安全的方案，只有尚未被攻破的假设。

面对日益复杂的攻击手段，我们的技术防线必须进行全面升级：

**1. 代码审计需穿透至业务逻辑层**

传统的安全审计往往侧重于防范重入攻击或整数溢出等常规漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QnnydwqNHNWWgoJeJ305LqMqzLQtoZo62p5EXg8tVqCT6C9aqXKtXXEml17VOHHcHaBr9IsreialdC4syiaGzgXZzQKIHFo3ooc/640?wx_fmt=jpeg&from=appmsg)

未来，必须引入专业的红队测试，深挖缓存机制、授权逻辑等容易被忽视的业务层面。系统是如何判断交易真伪的？其中是否存在捷径可走？这应当成为审计的核心。

**2. 建立实时的异常熔断机制**

安全防御不能仅停留在事后追溯。系统必须具备实时的链上行为监控能力，一旦检测到短时间内出现极其反常的大额铸造或赎回，系统应能自动触发熔断机制，及时阻断交易，将损失降至最低。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9Rp5c4k3hhF5Dic2zUh0ibrIPbnyu5JDvflibkEGkbiaD9pj4ia1Pht1aMoktNiaJJPgYiaMNc8MyZ8tY9CXRMxXYfImUfzh4Zl8Ly3YU/640?wx_fmt=jpeg)

**3. 构建真正的纵深防御体系**

从热钱包到冷钱包，从底层网络到应用层，攻击面早已全面扩展。安全不再仅仅是运维或开发部门的单一职责，而是需要贯穿整个产品生命周期的系统工程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9TNTibn13iaaef8CQjk9cZKibD5lgLThJrIwY7oYKher0poLpPCsqBSAmDeq9gGaGcOYDHO7jEKW6Wn9t6vISsgiaaZ1dGKpVm86S8/640?wx_fmt=jpeg)

总之，技术这条路没有尽头，攻防博弈也永远在路上，我们只有时刻对技术保持敬畏，不断去升级咱们的安全防线，才能真正守住底线。

---

---

### 「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

---

如果你还需要其他学习思路可以去看一下我的往期文章：

[0基础该如何转行网络安全？值得吗？](http://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484313&idx=1&sn=e62e92639b5b1577ad802a3129f11ad0&chksm=c2fc9043f58b195548dd0009fdf1fdeccd2b3bd68e144ae4a42c78bde7d5ead281c2a53f8287&scene=21#wechat_redirect)

[【工具/案例篇】神仙级渗透测试入门教程(非常详细)，从零基础入门到精通](http://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484278&idx=1&sn=2475864a18fd158f1100b0d7e3dd33e3&chksm=c2fc90acf58b19ba8bfe9f656831d79ceb6529807de784998bc2b0afe2fa40f0b5361521b298&scene=21#wechat_redirect)

[网络安全自学（超详细）：从入门到精通学习路线&规划，学完即可就业](http://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484267&idx=1&sn=2e6844ce1608081cee498900169e3e7b&chksm=c2fc90b1f58b19a7eb633cfe7e082652d2adac80e2a815100762b531691baa759fc5560577d9&scene=21#wechat_redirect)

**周小粥专属网络攻防技术资料**

@网络安全-周小粥：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTiclOnwqZc9T2SWU4Ytbgk67F5oS2kibMC7iaiaHAPzvfCiaD5Gdv9PWR1c3SzvGpyZJ5NbDuic8rENeHQ/640?wx_fmt=png&from=appmsg)

**部分技术资料预览**

**01**

**视频教程**

和360一起研发，覆盖从入门到进阶的***全套视频教程***（从零到精通：基础攻防→渗透测试→应急响应→CTF实战，5大模块200+课时）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqQQAbb583x7rnkuAgtzeXYDGUNCYrkQxccs2iadybesPicVXxBFuklPVnrw0afJoIEBZibMgrHH15ibQQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPQVyePJAlTHZictVmp6jI3HrNINrNbKMiaeKHApiaRia6dcMPGBAaibc97hw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**0****2**

**学习路线**

***2026详细网安学习路线***（包括各类技术的学习顺序和学习时长、学完技术后的发展方向和建议等）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPXGjfl2TiaQ05ZIPFMznOLcr76aP8V4ibDSp5SjxMTdORLaak23mgP3gw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPSEZicfjyPtnILjb076LOEmkPbFa2ffk6jSIX7lWgwg1hyoObwt6Wufw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**0****3**

**书籍Pdf**

99+入行网络安全必看的书籍和文章的Pdf（市面上的技术书籍确实太多了，这些是我精选出来的）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/CsKJlMFPH9QpA8gfIqwuchDXRn63kzLVaDicoIohnpLTHkIzZKw3PKaeYq4vDA2PgpP5YEbZQCnMKR9AHERPBrBJ2RqdKHDr74GsuyibDmM8Y/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**0****4**

**安装包/靶场**

所有视频教程所涉及的***工具安装包***和***靶场项目***等

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9TOmGf5saFdTXDvCmMAGPdMUoALy6OgqrhoQZ18O8YnQCxk11toibkvq5MQZ9iag1qEfZYaHMwlq2YtqkmkHJy7iaMWJkwsgeEpss/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9SKrvGiaA0T3xhgdcD31dgfpm1tSfbt3SnutdQCZ40dbpD7WQsRg7o5Nq8nibLRPXX5K7CBVJhzwJ1JbEFphI4KRtb2KKlunyakI/640?wx_fmt=jpeg)

**0****5**

**面试试题/经验**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPiaKcFwOp5adPyCbWpj9JDe49cOOZ0YxAhqCQYwt0ldrKtwFeKJ8Utgw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTiclOnwqZc9T2SWU4Ytbgk67F5oS2kibMC7iaiaHAPzvfCiaD5Gdv9PWR1c3SzvGpyZJ5NbDuic8rENeHQ/640?wx_fmt=png&from=appmsg)

@网络安全-周小粥：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTk5CbPZbQltff81fWAianO5baZC5UyfUVPsKfCPia0F1VlvLicw5hHbiaPbPibbxOCn6tg1B8x8OneWVw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**往期精彩**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTk5CbPZbQltff81fWAianO5baZC5UyfUVPsKfCPia0F1VlvLicw5hHbiaPbPibbxOCn6tg1B8x8OneWVw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqRG5oB85wG66TXpUc6CG5d6wKyMGDIMYUf0pfHWfnSZtPU3Psys58XC5mlg8dl1zK8OtMJlGic1kaA/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484337&idx=1&sn=7440b757243bc5120af4c08bcc4d104c&chksm=c2fc906bf58b197d6aeaf924627838dcf7dd1a35a88109a50e8d57fd5478974cc95881d8b9d1&scene=21#wechat_redirect)

**光挖漏洞每月就有1w+？？！这也就是网安人才能感受的到吧**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTnMJW3ol...