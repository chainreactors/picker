---
title: A-Mobile 2022 参会小记
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493067&idx=1&sn=e05b49a57a285ba3163f468f9fa5a369&chksm=c063cb12f714420445503710fcbc665e75835d17f8ca270b8923398c6baa670bbfdcdd04e9e3&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-10-29
fetch_date: 2025-10-03T21:14:24.104610
---

# A-Mobile 2022 参会小记

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3g7knImBNDqtWUpYB3FMlzaP7qVk7bhvFH2r3p74UVjqXHAyQ1yEqUg/0?wx_fmt=jpeg)

# A-Mobile 2022 参会小记

原创

\_qweasd

安全研究GoSSIP

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3CkPNREdZlokRcJ8D9gFc5X79HoiaLNqpUYia8osguGsLnKP8iabmzohvw/640?wx_fmt=png)

第五届A-Mobile’22会议(与ASE '22共同举办）旨在汇集移动应用分析领域的国际研究人员和从业人员，介绍和讨论新兴的Mobile领域相关技术，讨论会于2022年10月10日美国东部时间早晨8点30开始，整个研讨会共有三个特邀报告，分别来自Monash University的Li Li教授、George Mason University的Kevin Moran教授和University of California, Irvine的Joshua Garcia教授，以及四篇学术论文报告。我们在线参加了本次讨论会，对相关的报告内容做了相关记录，与公众号的读者们分享。

Keynote Speech 1: Taming Android Fragmentation

来自澳大利亚莫纳什大学的Li Li教授为我们介绍了他们团队关于Android碎片可控化相关的研究进展。安卓生态系统本身的快速发展和不同智能手机制造商定制及独立维护带来的结果是安卓平台的差异化越来越大，这就是碎片化的通俗说法。当系统和软件具有一定一致性时，才能保证软件和设备完全兼容。碎片化严重不仅造成安卓系统混乱，也导致安卓应用的隐形开发成本的增多。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3Im06ATkf1BOBdPCoYgldZ33FEFhJ1wfAQdoMzo4K1snGYfAbAl11Eg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3NnnFjqnuQ3q0dNYialw4V4UiaYN0uxY5GOYo6kib2sQNlC2zp81rMJEAw/640?wx_fmt=png)

Li Li教授提到他们的研究主要从三个角度开展：安卓兼容性问题检测方法的现状，现有的最先进的兼容性问题检测工具的可复制性研究以及现有的兼容性问题检测工具比较。通过文献综述确定了9篇论文的研究及工具用于检测安卓应用程序中的兼容性问题，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3NGFTfvh0al93icfGXYAuUSyWj6swRicfrdDZwhFYlMoG1sP82m5NtYdA/640?wx_fmt=png)

接着总结了其他研究人员报告的五种不兼容的问题：evolution-induced(Method)，evolution-induced(Method),device-specific(Method),device-specific(Field)以及overwrite/callback。确定兼容性问题检测工具的可执行且和研究的相关性后，共对四种工具：CiD、IctApiFinder、CIDER及FicFinder分别使用其原始数据集进行测试并确认所选工具的可重复性。可重复性研究表明以上研究中所产生的大部分实验结果都可以复现，无法复制的少数案例主要是由于工具版本更新或缺乏维护。最后对所选择的四种工具进行了实证比较其兼容性问题检测的能力，实验发现四种工具的检测结果并没有很大重叠。研究结果表明，兼容性问题的检测仍处于早期阶段，相应的检测工具开发也需要Android社区更多的关注以不断改进，以实现良好的兼容性问题的检测。

Keynote Speech 2: The Promise of (Machine) Learning from User Interfaces to Support Software Engineering for Mobile Apps

来自George Mason University的Kevin Moran教授给我们带来了第二讲，他所在的实验室主要目标是针对开发者在软件开发和维护中的需求设计有针对性的自动化解决方案。现有的软件文档自动化技术通常用对代码和自然语言进行推理，然而这个过程往往很复杂——因为抽象的自然语言和结构化的编程语言之间的存在词汇差距。而图形用户界面（GUI）是弥补这一差距的一个潜在桥梁，因为GUI本身就是由底层代码构成的的功能基于像素的数据显示。

Kevin教授在本文中对图形用户界面和软件的功能、自然语言描述之间的联系进行了首次全面研究：

1. 收集、分析并开源了一个大型的GUI功能描述数据集Clarity，其中包括来自Android应用程序的10204张截图及45998个描述。这些描述全部为人工标签且有相应的质量控制机制。
2. 研究了四种Neural Image Captioning模型在以屏幕截图作为输入时预测不同粒度的自然语言描述的能力。
3. 使用常见的机器翻译指标对这些模型进行定量评估,展示了它们在视觉和词汇程序信息之间弥合语义差距的能力,并通过一项大规模的用户研究对其进行定性评估。

Keynote Speech 3: Analyzing Android Native Code: Where Are We? Where Should We Go?

最后一篇特邀演讲来自美国加州大学尔湾分校的Joshua Garcia教授，他为我们带来了恶意软件和Android应用程序本地代码中的安全更新及漏洞方向上取得的进展。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3Djd5veoOKkKNrxeVia7Hvf9d7Cj6F2WicFichY2EZicPb7gG5JPtf2yOBw/640?wx_fmt=png)

在这个特邀报告中，Joshua Garcia教授介绍了他们对Android APP中的native code进行分析的系列工作。

Lightweight, Obfuscation-Resilient Detection and Family Identification of Android Malware

如果安全分析人员可以从识别恶意Android应用程序所属的家族而不是只检测单个应用程序那么会给恶意软件检测工作带来什么影响呢？Joshua教授提出了一种基于机器学习的新型Android恶意软件检测和家族识别方法RevealDroid。RevealDroid不需要进行复杂的程序分析或提取大量的特征集，而是选择是分类后Android API使用的特征、基于反射的特征以及来自应用程序的本地二进制文件的特征。研究使用了一个由54,000多个恶意、良性应用程序组成的大型数据集评估RevealDroid的准确性、效率和抗混淆能力。实验表明，RevealDroid在检测恶意软件时达到了98%的准确率，在确定恶意软件家族上达到了95%的准确性。

Too Quiet in the Library: An Empirical Study of Security Updates in Android Apps' Native Code

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3rXBsaHHURwcX7GggricUccWqFRzKOHxumbZ1DwkOCfrAFWGEuYInjGg/640?wx_fmt=png)

Android应用开发者将预编译的第三方本地库添加到他们的项目中来提高性能和重用功能。而这些库经常被忽视或者放弃更新。所以尽管明明对应的库已经有更安全的更新版本，人们还在继续使用有未修补安全漏洞的过时的本地库的app。由于本机库的普遍使用和落后的更新带来的安全问题，他们创新性的提出了一种新的方法命名为LibRARIAN旨在识别未知的本地库及其版本。下图显示了Librarian的整体工作流程：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3IicdWjPsQaftoJia37zstiaoYOJZe2wwicYMVEswLwky8BrbK5bj0q4rFg/640?wx_fmt=png)

1. 特征向量提取：从二进制文件中提取Metadata和Data中能反应库的代码要素且跨平台稳定的的共六个特征。
2. 相似计算：bin2sim比较法使用Metadata中提取的五个特征计算相似性评分。
3. 版本识别字符串比较：与识别库的版本信息的字符串进行匹配。

给出一组从Android应用中提取的带有未知库名的二进制文件和一组手动收集的已知库的版本，LibRARIAN通过如上流程将未知的版本与已知的库版本进行匹配，输出一套最终的第三方所需库的检测版本。使用LibRARIAN他们建立了一个大规模的Android应用及其原生库的仓库其中包含从2013年9月至2020年5月期间Google Play上最受欢迎的200个免费应用的7678个版本，发现53/200个流行的应用程序（26.5%）包含已知CVE的脆弱版本。研究发现，应用程序开发人员平均需要528.71天才会发布应用程序的安全补丁，而库的开发人员仅在54.59天后就会发布安全补丁——更新速度慢了10倍。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3JhmwRnON6UnJFaBFhz6UyqB0Vlzs2iceicicFtPJAwCQTKJ1juQVMc3iaA/640?wx_fmt=png)

除此之外，Joshua教授还对一些本机代码相关的其他研究进行了简单介绍：Jucify可以通过静态分析可以检测出恶意软件依赖本机代码隐藏他们调用Android框架敏感代码的行为；DroidReach是一种静态方法可以用于评估Android应用中本地函数调用的可达性，用于判断Android应用中过时的本地库中的已知漏洞是否会产生直接的安全问题。

Paper 1: E-MANAFA：Energy Monitoring and ANAlysis tool For Android

论文部分的第一位演讲者是来自University of Minho的Rui Rua ,他们的研究小组一直致力于帮助开发者们建立可持续的和有效的解决方案。

本篇文章主要介绍了他最新开发的工具E-MANAFA，它可以监测和估测安卓设备上软件的能耗。E-MANAFA从制造商提供的特定设备文件power\_profile.xml，Android的batterystats电池电量服务和由谷歌开发的用于性能检测和跟踪分析的生产级开源堆栈Perfetto中提取信息，系统性的估测每个部件的能耗。在github上有E-MANAFA（https://github.com/greensoftwarelab/E-MANAFA）的开源代码。

Paper 2: Privacy Analysis of Period Tracking Mobile Apps in the Post-Roe v. Wade Era

接下来是来自北京邮电大学的Zikan Dong, Liu Wang, Hao Xie, Guoai Xu 以及华中科技大学的Haoyu Wang带来的研究工作，作者针对知名的Roe v. Wade案判决结果在2022年被美国最高法院推翻（关于堕胎自由权之争）之后，对经期追踪应用程序进行了隐私分析。现在市面上有很多经期跟踪应用程序，帮助女性记录经期和经前症状、预测经期的周期和避孕。Roe v. Wade案判决被推翻之后，带来的巨大影响也让安全专家们担心——经期跟踪程序收集到的数据会让考虑或决定堕胎的女性受到惩罚。本文收集了来自Google Play的35个最受欢迎的经期跟踪程序并对其分别进行了静态分析和流量分析，分析了在使用过程中这些应用程序收集到的敏感信息；分析了各应用程序的隐私政策并验证它和应用程序行为的一致性；观察研究用户对应用程序的评分和评价，找出美国高院对Roe v. Wade案重新诠释后，带给经期跟踪程序用户的担忧。

Paper 3: A First Look at CI/CD Adoptions in Open-Source Android Apps

来自Monash University的Pei Liu和Xiaoyu Sun, Yanjie Zhao, Yonghui Liu, John Grundy和Li Li 教授等作者，在本文中介绍了CI（Continuous Integration，持续集成）/CD（Continuous Delivery，持续交付）在开源Android应用程序中的应用探索。

CI（Continuous Integration，持续集成）/CD（Continuous Delivery，持续交付）是指将传统开发过程中的代码构建、测试、部署以及基础设施配置等一系列流程的人工干预自动化的方法，能帮助开发人员更及时、更可靠地交付代码。谷歌、Mozilla、微软等公司和众多开源软件开发团队也在使用CI/CD并且大量减少了研发成本。尽管许多开源项目已经对CI/CD有所研究，但是Android还从未涉猎。

作为最先关注到Android应用项目中CI/CD服务使用情况的人，本研究对常见的开源代码仓库（包括Github、GitLab和Bitbucket）中的Android应用进行了广泛的实证调查。研究结果表明大多数应用开发者在开发中没有采用CI/CD服务。在由CI/CD服务处理的Android项目中，最受欢迎的三个服务是Github Actions、TravisCI和CircleCI。有趣的是，数据表明，有CI/CD服务的项目通常比不涉及CI/CD的项目更受欢迎。

Paper 4: Scaling Arbitrary Android App Analysis

来自Paderborn University的Felix Pauck介绍他最新的研究，他的研究方向主要是Cooperative Android App Analysis。在对Android应用程序做污点分析时可能会因为设备或者库版本出现兼容性问题导致分析报错或者apk文件过大导致分析超时，有时我们需要为应用程序添加需要的库并且移除不必要的库和类。Felix开发的APK-Simplifier就可以用于这个过程中Android应用程序的库检测。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3np3p8tppjo9XPmGial8HLU4Pt9CNZzU9DFtRPfY8VOGcibWMZkc38hbA/640?wx_fmt=png)

2、解析：从输入的应用程序获得库并从Google Repository下载它们。从库和应用程序中提取（和反编译）各个类，每个相似类的两个版本都被转发到JPlag（通过在多组源代码文件中找到相似之处的系统，主要用于检测软件开发中的抄袭剽窃行为），检查它们是否在某个可配置的阈值范围内相等（或相似）。解析结束时，会输出一个相等的、被信任的类的列表。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EHWicXcdu32u0o2YGk7HFQ3E8KS4wFUsACD8pYXM8Kaiaaib70BsAhmBdt35Tm8LQEenjfokddD6TuQ/640?wx_fmt=png)

1. 简化：使用Soot将受信任的库类从应用程序中移除。

实验表明，APK-Simplifier的三个模式都能有效移除可信任库减小Android应用程序apk文件的大小并且成功在6个污点分析工具共9个不同版本的测试中都有非常亮眼的表现，污点分析超时行为大大减少。

---

关于会议特邀报告的PDF，可以关注本公众号并留言后获取哦~

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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