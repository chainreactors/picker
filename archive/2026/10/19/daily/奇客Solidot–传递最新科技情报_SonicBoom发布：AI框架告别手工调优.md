---
title: SonicBoom发布：AI框架告别手工调优
url: https://www.solidot.org/story?sid=85645
source: 奇客Solidot–传递最新科技情报
date: 2026-10-19
fetch_date: 2026-10-20T06:52:36.934829
---

# SonicBoom发布：AI框架告别手工调优

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261019)
  [往日投票](/polllist)
* 皮肤

  [蓝色](/?theme=blue)
  [橙色](/?theme=yellow)
  [绿色](/?theme=green)
  [浅绿色](/?theme=clightgreen)

* 分类:
* [首页](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [科学](//science.solidot.org/)
* [科技](//technology.solidot.org/)
* [移动](//mobile.solidot.org/)
* [苹果](//apple.solidot.org/)
* [硬件](//hardware.solidot.org/)
* [软件](//software.solidot.org/)
* [安全](//security.solidot.org/)
* [游戏](//games.solidot.org/)
* [书籍](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [云计算](//cloud.solidot.org/)
* [高飞的电子替身](//story.solidot.org/)

## 关注我们：

solidot新版网站常见问题，请点击[这里](/QA)查看。

## 消息

**本文已被查看 3245 次**

## SonicBoom发布：AI框架告别手工调优

[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Wilson](/~Wilson) (42865)发表于 2026年10月19日 14时37分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85645&appkey=1370085986&title=SonicBoom%E5%8F%91%E5%B8%83%EF%BC%9AAI%E6%A1%86%E6%9E%B6%E5%91%8A%E5%88%AB%E6%89%8B%E5%B7%A5%E8%B0%83%E4%BC%98 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自河流之女**

Nala Ginrut 写道：
*SonicBoom是全新的AI运行时框架[0]，采用 GPLv3 许可证，由 HardenedLinux 社区主导开发。它提供语言无关的C API接口，这意味着你可以用任意语言绑定这个库，从而实现任何编程语言都能进行高性能AI研发。目前 GNU Guile 是官方支持的语言，同时利用 Guile 的 delimited continuation 实现了应用层的“死计算消除”，只有真正有效的计算才会进入运行时。

而运行时包含 LLVM MLIR，它将会把计算图再次优化，进一步去掉无效的计算图，并利用 LLVM 根据硬件具体生成 kernel，而不是手工根据硬件去优化 kernel。

对于 AI 研究而言，应用层绑定的动态语言将提供 pytorch 的灵活性，以及超越 llama.cpp 的单点推理性能。其实际运行的时候会自动将计算图进行编译优化，这样同时实现了 pytorch 的动态图弹性，以及 tensorflow 的静态图性能。

对于推理部署而言，无需应用层动态语言的支持，可以直接加载模型进行高效推理。但研究和生产部署使用的是完全相同的运行时图编译器优化栈，这意味着你研发完就能直接部署到产品。部署成本压缩到一个三百多MB的 .so 文件。没有几十个G的 python 全家桶。

llama.cpp 依靠非常有经验的工程师进行 kernel 调优，已经将性能优化到极致。而 SonicBoom 直接利用 llama.cpp 已有的 kernel，在 kernel 优化不变的情况下，依靠图编译器的优化，将原始性能提升20%（rtx3050 8G)，并且还在持续增加中。

目前 SonicBoom 社区版仅提供单点推理的能力，分布式推理能力计划于企业版提供。SonicBoom 的野心并不局限于 LLM 推理，它对标 pytorch，将在之后将更高的性能推向 image, video, tts 计算。

目前 SonicBoom 仅支持 CPI 和 CUDA，之后计划支持 Vulkan，为 non-nvidia 和纯自由软件爱好者提供更好的选择。我们目前缺乏足够多样的 GPU 评测数据用于优化，所以在 rtx 3050 之外可能测试数据会发生波动，您的评测数据能帮助我们把优化扩散到更多 GPU。

目前 v0.0.3 正在邀请社区贡献者参与不同 Nvidia 平台的评测，我们准备了非常简单那的脚本一行就能完成，不过测试时间可能比较长，请安排好自己的时间再参与，每位测评贡献者都会出现在贡献者名单中。[1]

如果您暂时没有硬件条件或者时间参与贡献，欢迎star，或者转发让更多有兴趣的朋友一起来玩。*
[0] https://github.com/hardenedlinux/SonicBoom
[1] https://github.com/hardenedlinux/SonicBoom/issues/2

[回复](/comments?sid=85645&op=reply&type=story)

﻿

罗马帝国灭亡的其中一个主要原因是他们没有0 - 这样他们就没法给自己的C程序指明成功退出的路--Robert Firth

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261019)
* [过去的投票](/polllist)
* [编辑介绍](/authors)
* [隐私政策](/privacy)
* [使用条款](/terms)
* [网站介绍](/introd)
* [RSS](/index.rss)

本站提到的所有注册商标属于他们各自的所有人所有，评论属于其发表者所有，其余内容版权属于 solidot.org(2009-) 所有 。

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP 服务器")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache 服务器")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

京ICP证161336号    [京ICP备15039648号-15](http://beian.miit.gov.cn) 北京市公安局海淀分局备案号：11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

举报电话：010-62641205　涉未成年人举报专线：010-62641208 举报邮箱：jubao@zhiding.cn　网上有害信息举报专区：<https://www.12377.cn>