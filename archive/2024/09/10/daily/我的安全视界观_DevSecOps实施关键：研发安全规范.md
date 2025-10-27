---
title: DevSecOps实施关键：研发安全规范
url: https://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247486304&idx=1&sn=a625dfefbe8e0a96e1505e50c43c07c6&chksm=eb6c2918dc1ba00ec0683d356c5a8e436d248e62786a65f9d027ac7ffa512ad15e0c4ae17df2&scene=58&subscene=0#rd
source: 我的安全视界观
date: 2024-09-10
fetch_date: 2025-10-06T18:28:19.223140
---

# DevSecOps实施关键：研发安全规范

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/UQ8MSNOhDKa1iajYvfOVInibJbqn509Ly0PmXy1nEMaevAzmvbJYNgXzAmyu7HSaZU2a7ia6K0rBpMvw72IplbibxA/0?wx_fmt=jpeg)

# DevSecOps实施关键：研发安全规范

原创

aerfa21

我的安全视界观

很久以前，就想写一篇关于SDL与DevSecOps的文章，但疏于实践一直未能动笔。想写的原因很简单，因为总是听到有人说SDL落后、DevSecOps相关技术更高超。一提到研发安全建设，不分研发模式都在赶时髦一样地说DevSecOps。从我的观察来看，不结合研发模式来做研发安全，都是不成功的。

在数字化浪潮的推动下，一些公司已经完全步入DevOps模式，有的则出现瀑布、敏捷或DevOps并存，且后者是居多的。所以如何在多种研发模式下进行有效的研发安全建设，成为一个必须解决的难题。经过近十年的实践，终于在探索解法上有一点点收获与经验，于是有了“深耕研发安全”这一系列文章。

本文是第六篇，DevSecOps实施的第三个关键准备（3/4），系统化的介绍研发安全相关规范体系。从设计思路、技巧到实践经验，描述了规范的应用，以全面支撑研发安全工作在公司层面的开展。

**01****规范建设是系统化工程**

好的规范设计是一个系统性工程，需要综合考虑公司的业务需求、研发流程、技术环境、法律法规和行业规定等多方面因素。然而，规范相关的工作常被轻视或忽视，尤其是在技术氛围浓厚的团队。

![](https://mmbiz.qpic.cn/mmbiz_png/UQ8MSNOhDKa1iajYvfOVInibJbqn509Ly0ia6BGUKaxJQ82VybKq1JibhrWpkmBv6LlOyVrCAan8DU3ibQwoyOX2roQ/640?wx_fmt=png)

按照体系化的思路，研发安全的规范和体系设计亦可以遵循四级原则，并且在研发流程中是如下体现：

* 开发框架（一级文件）：指公司级开发框架体系，是开发过程与公司战略目标承接的基础，指引所有研发团队的工作；

* 安全提测管理流程（二级文件）：描述研发过程中安全提测的操作步骤、要求和标准，是研发安全的最高级别文件，范围涵盖研发的各个阶段（需求管理、设计管理、开发管理、验证管理、发布管理和生命周期）；

* 研发安全相关规范和管理办法（三级文件）：在各研发阶段中的安全要求和规范，如安全需求规范、安全设计规范、编码安全规范、安全测试规范、应急响应管理办法、安全加固规范等；

* 研发安全相关模板和操作手册（四级文件）：支撑三级文件落地的具体指导书、实施细则、清单、操作手册和模板等，如安全需求基线（知识库）、安全设计基线（知识库）、威胁建模报告模板、安全测试报告模板等。

![](https://mmbiz.qpic.cn/mmbiz_png/UQ8MSNOhDKa1iajYvfOVInibJbqn509Ly0yyvBCJP5ia1vTcf5YkcZI7N1ctCmY5YlmN8WKYOQONNvfoTmsY6KVdw/640?wx_fmt=png)

**02****编码安全规范设计技巧**

每个研发安全团队几乎都会制定编码安全规范，提供给开发进行学习和参考，试图在开发过程中减少常见漏洞的引入，从而保护产品免受攻击。也就是说编码安全规范的质量好坏，一定程度上影响着整件事的成败。所以至少要注意以下三方面：

* 明确制作规范的目标：最初的目标肯定是为了规避安全漏洞，每个公司的技术栈不同、产出的漏洞类型也不一样，应该通过历史安全事件、安全测试结果等分析出内部的Top 10类型漏洞，制定先要解决的漏洞类型计划，从而编写规范内容；后期可能会为了合规性检查、供应链公司安全检查等，此时应避免提供内部针对性强的规范，要准备一份大而全的交出去，以免暴露典型漏洞；

* 三分借鉴七分得定制：在研发安全推进的初级阶段，大而全的编码安全规范产生的效果反而不太好，所以应该先聚焦解决3-5类漏洞，待漏洞逐渐收敛就可以追加内容。规范不是一成不变的，需要与时俱进的更新，与时是指当前公司内部的研发安全态势、当前的安全措施及效果等；

* 从开发人员视角出发：如果编写规范的参与者都是安全团队，则一定要小心写成自己熟悉、对开发陌生的语言。安全人员通常习惯漏洞描述、原理及解决方案的思路，而开发人员则更习惯看对输入与输出的处理、内部资源的操作。在规范中加入错误代码、正确代码示例也有助于理解，并且在写完后一定要组织资深开发或架构师进行评审，以确保规范的有效性。

**03****安全规范落地实践经验**

说起规范的落地，我们可能第一时间会想到培训和考试，这虽有作用但都只能解决知道的问题。在推行培训的过程中，需要“因地制宜”地考虑到不同场景，把培训尽可能融入流程、做成体系。比如，以编码安全规范的落地为例：

* 新员工入职组织培训：可以将安全培训嵌入到新员工入职的课程中，包括校招和社招开发序列人员。校招生估计没怎么接触过安全、社招人员的安全意识肯定参差不齐，这时候应围绕编码安全规范对他们进行常见漏洞介绍和攻击危害展示，使其明白安全的重要性及提升安全意识，并灌输自己写的代码自己负责安全质量理念，以及鼓励他们在日常工作中主动发现安全隐患并修复；

* 常写漏洞的开发人员：借鉴“解决不了问题，就解决人”的思路，针对每个BU经常写漏洞的研发人员，把他们集中起来组织安全培训和考试，重点介绍他们的漏洞案例，介绍危害性和不安全原由，引出编码安全规范并倡导自行引入白盒检测工具进行自检；

* 常态化的安全分享会：当编码安全规范有更新、白盒安全工具有新增或优化、外部发生重大漏洞时，在公司内部借助一些分享会或自行组织分享，传播研发安全的知识，提升大家的安全兴趣和意识。

做好上面的事儿，基本就能让开发人员知道编码安全。但知道并不等同于做到，从知道到日常工作中做到的路还比较远。所以一定要想出办法，能够及时提醒、监督或检查是否做到：

* 联动白盒检测工具：把编码安全规范尽可能的落到白盒的检测规则上，理想状态下是一一对应，但现实基本上是一对多（一条规范对应多条检测规则）。主流思路是依据规范来写检测规则，保障规范的有效落地，直接检查是否编码安全，也不让白盒检测工具因为规则多导致的误报而难以落地。不过也有例外的情况，比如已经知晓白盒工具上的某条、某些检测规则十分精准，此时规范中又没有要求，那么也可以上规则、后补充规范。此外，规范内容和工具检测规则均需要持续调优；

* 风险提示左移到IDE：目前比较“左移”的做法是在IDE上进行代码漏洞检测和风险提示，较为常见的方式是IDE联动白盒检测工具，因为检测规则都在工具上、IDE插件仅是串联作用。随着大模型的应用，后续在IDE上的效果应该会更好。（目前试过国内的几家，但检测漏洞方面表现都不够理想，至少还没到放心使用的水平。）

针对编码安全规范的落地，在流程上做了宣导，在技术上做了检测，那还会发生意外情况吗？答案应该是的，比如有针对bypass代码扫描流程的、假装完成编码安全培训的...为了应对诸如此类的奇葩情况，在安全提测管理流程设计时，就要把不按照要求执行产生漏洞或事件的情况考虑进去，最好的方式就是在事发后做处罚警示。实际不一定做，但要保留该权利，最好是想办法和BU的绩效考核挂上钩。

---

**长按识别二维码，和我交流**

![](https://mmbiz.qpic.cn/mmbiz_jpg/UQ8MSNOhDKblctsA0yeRibKPYm3JrocibHpmnImpp5E3gDUR6j8q87OlCMjKrnR3qlSQDsgA5xo5icUrQ7yRmGDnQ/640?wx_fmt=jpeg)

More...

****-- 深耕研发安全 ****--********

* [**数字化转型下的研发安全痛点**](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247486229&idx=1&sn=d3f8279f96fa8c0f366f83a1987349d4&chksm=eb6c296ddc1ba07b90004cb68353610f932f632da9a0c6ff10d0daecdb82fda2d1e187afdf5e&scene=21#wechat_redirect)
* [从安全视角，看研发安全](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247486243&idx=1&sn=c005d9685546b13a71a21808cc528ff4&chksm=eb6c295bdc1ba04d5457bcec5a58235f08566e6732a9c05590f6a1cf530d8db001d7e58b4ab1&scene=21#wechat_redirect)
* [基于研发过程的漏洞治理及经验](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247486266&idx=1&sn=6a0bac5a6525f4a2962bad03642efb5c&chksm=eb6c2942dc1ba054ddb43febab0efd4e847878581aa07502705c0acd2dc7ad620c77b2def8ba&scene=21#wechat_redirect)
* [DevSecOps实施关键：研发安全团队](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247486280&idx=1&sn=8740e7bab52e96b6c853a9a6c87573e4&chksm=eb6c2930dc1ba026268d7ea63c3e1d28a7e8c73990a263f0ac871101693d20efb14114c9fb65&scene=21#wechat_redirect)
* [DevSecOps实施关键：研发安全流程](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247486295&idx=1&sn=e3a89d428acfff15e59ab93398ecb393&chksm=eb6c292fdc1ba039ebdb06909a8aecf3a876778dbfa440dbc55d5ec6aca82c145c6bd0d1ff35&scene=21#wechat_redirect)

****-- SDL 100问 ****--********

* ******[SDL100问：我与SDL的故事](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485635&idx=1&sn=d1f3c10665061d46ee3042a932c32af5&chksm=eb6c2abbdc1ba3adc13596ff1174f5431e597f851cd4560e31daa7aa256e39aecca1c0f9c2a0&scene=21#wechat_redirect)******
* ******[SDL 1/100问：SDL与DevSecOps有何异同？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485702&idx=1&sn=cdb42998335935cce5513a731f2969e6&chksm=eb6c2b7edc1ba268d2847e2083231fe5f964efea2ab8c7d0ffb16d081683c79dda8529682693&scene=21#wechat_redirect)******
* ******[SDL 2/100问：如何在不同企业实施SDL？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485711&idx=1&sn=79e9ebca9eae85d4d4cb6fcf6639fcf5&chksm=eb6c2b77dc1ba2616e6adf76413422781c666d6a9f2cf734fb7097b791c5ddd2762ef4673547&scene=21#wechat_redirect)******
* ******[SDL 3/100问：SAST误报太高，如何解决？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485724&idx=1&sn=1d9fedf471d58919a2b0ddf99d10c9d0&chksm=eb6c2b64dc1ba2721a4cdcaee3036ed61dab0c91f97e794a6ed5a59b3be74872a233ed0eaf45&scene=21#wechat_redirect)******
* ******[SDL 4/100问：SDL需要哪些人参与？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485759&idx=1&sn=a362896234e1d0e7403befd9c2312567&chksm=eb6c2b47dc1ba2515c97c887e6b7ee6119c1d26e6ba9aad4eace374350f68c3566c1db005d03&scene=21#wechat_redirect)******
* ******[SDL 5/100问：在devops中做开发安全，会遇到哪些问题？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485772&idx=1&sn=37a833b95317746945bb08e3940d07ff&chksm=eb6c2b34dc1ba22200369c45c0e871cd708c86810da3b64c09e7c8c4ca39fedc4fefa7631ad3&scene=21#wechat_redirect)******
* ******[SDL 6/100问：如何实施安全需求？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485785&idx=1&sn=091cdd44050411ad490e95222221e3d8&chksm=eb6c2b21dc1ba2373c3f566a9500661bec26d4b805e5614cb4f726a4876e139014cb13c65abe&scene=21#wechat_redirect)******
* ******[SDL 7/100问：安全需求，有哪些来源？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485798&idx=1&sn=e7d01d58260deb4ea5f59f83227cf33e&chksm=eb6c2b1edc1ba20816d5738533156096cb6c8872924cba3dce37003af24e8228fd87365dff35&scene=21#wechat_redirect)******
* ******[SDL 8/100问：安全需求怎么实现自动化？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485811&idx=1&sn=73876a6b1c669c165657e3af62e0f10a&chksm=eb6c2b0bdc1ba21dbde4074b1c8c24223eab3a7a546fd2301fbfa7a2385bb2db682eaa3555b6&scene=21#wechat_redirect)******
* ******[SDL 9/100问：实施安全需求，会遇到哪些难题？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485824&idx=1&sn=667824a4531a35cd67ce2f8d6581f81d&chksm=eb6c2bf8dc1ba2eed4251327b82c27d36eac17b338bb7240fe23bdaa66daf1e7823d8a331a7a&scene=21#wechat_redirect)******
* ******[SDL 10/100问：安全需求和安全设计有何异同及关联？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485837&idx=1&sn=8b4f4c703994290e23feb0253b8da090&chksm=eb6c2bf5dc1ba2e3686c75ffe5d278ce534ff037401411662dda783344579497ac2d9745466b&scene=21#wechat_redirect)******
* ******[SDL 11/100问：设计阶段应开展哪些安全活动？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485850&idx=1&sn=21ed85d46c64552edfb2ca8da44b3c83&chksm=eb6c2be2dc1ba2f4ca6a95dd3dbc7bb916e9cbaba5d3f41b5eb470f4bcc5497db568bbdbe5cc&scene=21#wechat_redirect)******
* ******[SDL 12/100问：有哪些不错的安全设计参考资料？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485863&idx=1&sn=329eba45ab509e199463e371b1e99fcf&chksm=eb6c2bdfdc1ba2c97e40ee5d0b81df82469b5bf5ca1825de47dc9dc8acee2a4a7e8841fc7257&scene=21#wechat_redirect)******
* ******[SDL 13/100问：安全设计要求怎么做才能落地？](http://mp.weixin.qq.com/s?__biz=MzI3Njk2OTIzOQ==&mid=2247485876&idx=1&sn=2feca1c97cf0a17188fd...