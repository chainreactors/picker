---
title: 黑客是如何入侵网站？为什么企业网站需要做渗透测试？
url: https://mp.weixin.qq.com/s/oxi3TxpoMBgNanXOdxPpmA
source: Doonsec's feed
date: 2026-07-30
fetch_date: 2026-07-31T05:27:40.570220
---

# 黑客是如何入侵网站？为什么企业网站需要做渗透测试？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CkwxvMGmWhdr03m6XQrv6ggY76lhlznYyhqjqLMpKNpj5UdT2WBrKvGa4BqojeOHH7VDyYcK7NpL1cXcpoZQyVjRyuicrtXd7165OdHib1jXQ/0?wx_fmt=jpeg)

# 黑客是如何入侵网站？为什么企业网站需要做渗透测试？

强哥
强哥

网络漏洞侦探

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

作为公司的网络安全人员，特别是中大型企业，网站被攻击，网站打不开是一件再平常不过的事情了。今天我们就来说说黑客是如何入侵你的网站导致用户无法正常访问的。

由于关注我们的用户有一些是企业运维者，所以我在后面再说下为什么企业网站需要做渗透测试。

---

## 目前的网站可分为三大块：个人运营、团队/公司运营、政府运营。

个人网站比例还是很大的，这种网站多数采用开源系统。

如博客类：Wordpress、Emlog、Typecho、Z-blog、More…，

社区类：Discuz、PHPwind、StartBBS、Mybb等等。

团队/公司网站使用常用的开源CMS比例也是非常大，政府类网站基本上外包开发较多。

当然互联网公司自家产品应用必然都是公司自主开发：淘宝？知乎？豆瓣？等等。

如果更广泛的话，可分为两大块：开源与闭源。

能够有效说明网站伪安全的就是从实战出发的角度去证明到底是不是真的固若金汤。

这里之所以讲到入侵方法不是为了教大家如何入侵网站，而是了解入侵的方法多种多样，知己知彼才能百战不殆。

菜刀能够用来切菜，同样也能够用来杀人。

下面我们就来说下黑客入侵网站的一些普通的流程。

![](https://mmbiz.qpic.cn/mmbiz_png/CkwxvMGmWhc04FG6J1DRT735CQpfm6FrvDMod5NYWkn2Zy0yu4icxXKGmpWibL4ycJ5ibjNbLVNtMwc63Dl72rXibFLjUdPwiaxiaYxMJ3lH1hiaUQ/640?wx_fmt=png&from=appmsg)

## 黑客们入侵网站普遍的流程

### 1、信息收集

1.1 Whois信息–注册人、电话、邮箱、DNS、地址

1.2 Googlehack–敏感目录、敏感文件、更多信息收集

1.3 服务器IP–Nmap扫描、端口对应的服务、C段

1.4 旁注–Bing查询、脚本工具

1.5 如果遇到CDN–Cloudflare（绕过）、从子域入手（mail，postfix）、DNS传送域漏洞

1.6 服务器、组件（指纹）–操作系统、web server（apache，nginx，iis）、脚本语言

1.7 More…

通过信息收集阶段，攻击者基本上已经能够获取到网站的绝大部分信息，当然信息收集作为网站入侵的第一步，决定着后续入侵的成功。

### 2、漏洞挖掘

2.1 探测Web应用指纹–Discuz、PHPwind、Dedecms、Ecshop…

2.2 XSS、CSRF、XSIO、SQLinjection、权限绕过、任意文件读取、文件包含…

2.3 上传漏洞–截断、修改、解析漏洞

2.4 有无验证码–进行暴力破解

2.5 More…

经过漫长的一天，攻击者手里已经掌握了你网站的大量信息以及不大不小的漏洞若干，下一步他们便会开始利用这些漏洞获取网站权限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CkwxvMGmWhc3lyM6Nn1gwibFEOCqdcmgKps323ia0r7WNYHZnrejFIgv0jgFcnHSCtPaS4LPA0mRFtZlPbREsPgyu7IFKOXJaQ5fBlgeJKslc/640?wx_fmt=jpeg&from=appmsg)

### 3、漏洞利用

3.1 思考目的性–达到什么样的效果

3.2 隐藏，破坏性–根据探测到的应用指纹寻找对应的EXP攻击载荷或者自己编写

3.3 开始漏洞攻击，获取相应权限，根据场景不同变化思路拿到webshell

### 4、权限提升

4.1 根据服务器类型选择不同的攻击载荷进行权限提升

4.2 无法进行权限提升，结合获取的资料开始密码猜解，回溯信息收集

### 5、植入后门

5.1 隐蔽性

5.2 定期查看并更新，保持周期性

### 6、日志清理

6.1 伪装性，隐蔽性，避免激警他们通常选择删除指定日志

6.2 根据时间段，find相应日志文件 太多太多。。。

说了那么多，这些步骤不知道你看懂了多少？其实大部分的脚本小黑显然不用这些繁琐的步骤，他们只喜欢快感！

通常他们会使用各种漏洞利用工具或者弱口令（admin,admin888)进行攻击。

当然，这种“黑客”仅仅是出于“快感”而去想入侵你的网站，如果是别有它意的人，麻烦就来了。

说完入侵的流程，我们来说下为什么企业网站需要做渗透测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CkwxvMGmWhdIArNrreGY88dFtC6iaNBPOJOmeL1W3nvic34Is0wtq7QWG7wt4R9xrC0yiavEVibTLou9efmIcyPlaxYCkm3rrxlyWrTcj1WIwj8/640?wx_fmt=jpeg&from=appmsg)

## 为什么要做渗透测试？

### 第一：网络安全法规定

2017年6月1日正式实施的网络安全法中明确要求：第三十三条，至第三十八条针对关键信息基础设施运营者所做的规定（如关键信息基础设施运营商应当自行或委托网络安全服务机构对其网络安全性和可能存在的风险每年至少进行一次检测评估，并将检测评估情况和改进措施报送相关负责关键信息基础设施安全保护工作的部门），具有相当的强制性——在法律责任部分明确提到若不履行这些规定，则由有关主管部门责令整改、给予警告；

拒不改正或导致危害网络安全等后果的，处十万元以上一百万元以下罚款，而且还对直接负责的主管人员除以一万元以上、十万元以下罚款。

值得关注的是，在信息安全风险评估中，渗透测试是一种常用且非常重要的手段。

### 第二：渗透测试助力PCI DSS合规建设

在PCI DSS（Payment Card Industry Security Standards Council支付卡行业安全标准委员会）第 11.3中有这样的要求：至少每年或者在基础架构或应用程序有任何重大升级或修改后（例如操作系统升级、环境中添加子网络或环境中添加网络服务器）都需要执行内部和外部基于应用层和网络层的渗透测试。

### 第三：ISO27001认证的基线要求

ISO27001 附录“A12信息系统开发、获取和维护”的要求，建立了软件安全开发周期，并且特别提出应在上线前参照例如OWASP标准进行额外的渗透测试 。目前北京安普诺信息公司已经获得ISO27001的认证。

### 第四：银监会多项监管指引中要求

依据银监会颁发的多项监管指引中明确要求，对银行的安全策略、内控制度、风险管理、系统安全等方面需要进行的渗透测试和管控能力的考察与评价。

### 第五：最大限度减少业务损失

除了满足政策的合规性要求、提高客户的操作安全性或满足业务合作伙伴的要求。最终的目标应该是最大限度地减小业务风险。

企业需要尽可能多地进行渗透测试，以保持安全风险在可控制的范围内。

网站开发过程中，会发生很多难以控制、难以发现的隐形安全问题，当这些大量的瑕疵暴露于外部网络环境中的时候，就产生了信息安全威胁。

这个问题，企业可以通过定期的渗透测试进行有效防范，早发现、早解决。经过专业渗透人员测试加固后的系统会变得更加稳定、安全，测试后的报告可以帮助管理人员进行更好的项目决策，同时证明增加安全预算的必要性，并将安全问题传达到高级管理层。

![](https://mmbiz.qpic.cn/mmbiz_png/CkwxvMGmWhcvaFAmFJweQwRmVdjW9gbdX1ACRkIqg04CC3Qun2pbQQUEJ9ribw9YYGG2tV6exre0gJUCibO4LlFiafp93cxCia0GZSysvRhUicFo/640?wx_fmt=png&from=appmsg)

## 渗透测试与安全检测的区别

渗透测试不同于传统的安全扫描，在整体风险评估框架中，脆弱性与安全扫描的关系可描述为“承上”，即如上面所讲，是对扫描结果的一种验证和补充。

另外，渗透测试相对传统安全扫描的最大差异在于渗透测试需要大量的人工介入的工作。

这些工作主要由专业安全人员发起，一方面，他们利用自己的专业知识，对扫描结果进行深入的分析和判断。

另一方面则是根据他们的经验，对扫描器无法发现的、隐藏较深的安全问题进行手工的检查和测试，从而做出更为精确的验证（或模拟入侵）行为。

**网络安全学习资源分享:**

给大家分享一份全套的网络安全学习资料，给那些想学习 网络安全的小伙伴们一点帮助！

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

因篇幅有限，仅展示部分资料，朋友们如果有需要全套《网络安全入门+进阶学习资源包》，请看下方扫描即可前往获取
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xPHxpNUDnJgLY3DEzvwe3Me2iavhqpHLhmpucyY1iaTLF9ib21toFsQR9fOuicYibnh1zicKJ87jyT1aiarpLqVMBiceHw/640?wx_fmt=png&from=appmsg)
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_gif/CkwxvMGmWhe2f7RkvEFCW2Dbdq98XBHDmc7rSIricibxcv4iaYibthJ1ZAY8nRVztC4d8W0uksAjqgAK54adBhxx0xBKtric7n99mqOoXF8gziajY/640?wx_fmt=gif&from=appmsg)
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/CkwxvMGmWhcibue2m3JSGqbTEgNKjnnkhtyQbSVbQ3rLuDTTNe0pTYDVTGPnZv8T0lL4ofVDSM4ibz1OodqwQ3kvcoBVSHplmqPh78Kib6QB3s/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xPHxpNUDnJhubALicHt8GEIEzsayquN9qYKaVgWicbrglsqlzDRCeZiabIC0QRMV35sdD934lX1zrNLfWuNPDbe4g/0?wx_fmt=png)

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