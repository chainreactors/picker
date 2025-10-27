---
title: 什么是ChkApi？（专为金融行业开源的API安全检测工具）
url: https://mp.weixin.qq.com/s?__biz=MzkwNTI3MjIyOQ==&mid=2247484132&idx=1&sn=721763ec693c93569325551122bb5e05&chksm=c0fb0c2ef78c85380ed2cb3e14dff253bd82118f740b9ff0c38dd08d365238d19bd7579adb3d&scene=58&subscene=0#rd
source: 0x727开源安全团队
date: 2025-01-21
fetch_date: 2025-10-06T20:12:49.517866
---

# 什么是ChkApi？（专为金融行业开源的API安全检测工具）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cg0dicbbn3XSkicTMYqicBEj5plC5iaCpyibcahYMWZU3r9wvL1LvS1IENXxIcTgIbaqFJPbicmC89IiahVMt7W4x7icCg/0?wx_fmt=jpeg)

# 什么是ChkApi？（专为金融行业开源的API安全检测工具）

原创

0x727

0x727开源安全团队

**前言：**

**我们为什么开源？**

**我们在业余时间完成了“ChkApi”的构建，帮助了我们大幅度的提升了API安全与大幅度降低了重复性的人工劳动。开源ChkApi的主要原因是为了共享我们在API安全领域“我们的理论与实践”，理论的价值在于指导实践，学习的目的全在于运用。同时也是为了让社区开发者的力量来不断完善和强化这一工具。通过开源，我们能够接收到来自不同背景和专业知识的贡献者的反馈和改进意见，这有助于提升ChkApi的性能和全面性。此外，开源也是一种推动API安全最佳实践普及的策略，使更多的组织也能够提升他们的API安全防护能力。**

**最后，我们坚定地相信，在网络和信息安全领域，是不区分“甲方”和“乙方”的（虽然我们是所谓的“甲方”）。关键在于我们如何使用这些技术来创造一个更安全、更可靠的数字世界。**

**注：可参考前文[《主动防护视角下的API安全实践》](https://mp.weixin.qq.com/s?__biz=MzkwNTI3MjIyOQ==&mid=2247484049&idx=1&sn=fbfdc3346951fa0d8d8dd951a51885eb&scene=21#wechat_redirect)**

**基于****数据安全视角下API安全实践方法论**

全面性、层次性、适应性、动态性和预防性。

全面性原则：要求从宏观角度考虑API接口涉及的所有主体，确保所有相关主体都得到识别和管理。

层次性原则：要求对每个主体进行深入分析，深入到每个主体的多层目录，其中不同层目录可能关联不同的系统。

适应性原则：要求适应各种不同的前端框架，确保无论在何种技术栈下，都能有效地进行接口管理。

动态性原则：要求具备高度的灵活性，能够及时更新和调整各种规则策略。

预防性原则：强调在安全问题发生前，通过持续监测及时发现潜在的安全漏洞，并迅速进行修复。

**ChkApi技术架构**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cg0dicbbn3XSkicTMYqicBEj5plC5iaCpyibcrPoJTwGkzbbApMRYRovoKywxkxYXl00Kkfut78Bib5OjjVuCCicNjsrw/640?wx_fmt=png&from=appmsg)

**ChkApi功能**

1、访问目标地址提取出自动加载的JS地址和静态地址

2、提取网页未自动加载的JS地址

3、从webpack（JavaScript 应用程序的模块打包工具）提取JS地址

4、Base URL发现

5、API接口的提取和Fuzz

6、Swagger各版本解析

7、过滤危险接口

8、无参三种形式请求所有API接口

9、智能提取参数

10、有参三种形式请求所有API接口

11、Bypass测试API接口

12、响应包内容差异化自动分析，快速过滤出有价值的数据

13、敏感信息规则匹配，提取敏感信息泄漏

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cg0dicbbn3XTW9S3DK8WiaD0aiblksUicUBDWv6Sib8o6ERtardqocpD2n0YNv6HMB2x56m7pTicLqaeGZHNFcyzbu4w/640?wx_fmt=png&from=appmsg)

ChkApi 是一个免费且开源的项目，我们欢迎任何人为其开发和进步贡献力量。

* 在使用过程中出现任何问题，可以通过 issues 来反馈。
* Bug 的修复可以直接提交 Pull Request 到 dev 分支。
* 如果是增加新的功能特性，请先创建一个 issue 并做简单描述以及大致的实现方法，提议被采纳后，就可以创建一个实现新特性的 Pull Request。
* 欢迎对说明文档做出改善，帮助更多的人使用 ChkApi。
* 贡献代码请提交 PR 至 dev 分支，master 分支仅用于发布稳定可用版本。

*提醒：和项目相关的问题最好在 issues 中反馈，这样方便其他有类似问题的人可以快速查找解决方法，并且也避免了我们重复回答一些问题。*

*（Swagger和Bypass正在完善中，后续会更新上去，敬请期待。）*

*感谢：项目参考了jjjjjjjjjjjjjs的部分思路，规则借用了HaE和wih。感谢jjjjjjjjjjjjjs、hae和wih作者*

项目地址

https://github.com/0x727/ChkApi\_0x727

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Cg0dicbbn3XQxlBicp1oKQE5JxlmOkUnYicnoGIWeU6iahnzuaibsvgq62uEUk5V0rYxeYCXiaGz5jXhgrt3t03aibaww/0?wx_fmt=png)

0x727开源安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Cg0dicbbn3XQxlBicp1oKQE5JxlmOkUnYicnoGIWeU6iahnzuaibsvgq62uEUk5V0rYxeYCXiaGz5jXhgrt3t03aibaww/0?wx_fmt=png)

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