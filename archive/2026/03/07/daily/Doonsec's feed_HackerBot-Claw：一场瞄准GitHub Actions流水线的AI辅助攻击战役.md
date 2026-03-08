---
title: HackerBot-Claw：一场瞄准GitHub Actions流水线的AI辅助攻击战役
url: https://mp.weixin.qq.com/s/4-n3MSPMj5DQraoFIkc-7Q
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:04:47.830151
---

# HackerBot-Claw：一场瞄准GitHub Actions流水线的AI辅助攻击战役

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcR7lvc5tlo0K2icWQOGO3yqUZax8NPrjTz9055saBB7t5h1IibFicastIzt5xiaxogRRDrc2fFsJee311leW9POxOmy2Tx6Yhd3Y0/0?wx_fmt=jpeg)

# HackerBot-Claw：一场瞄准GitHub Actions流水线的AI辅助攻击战役

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 代号为“HackerBot-Claw”的自动化攻击活动，正系统地扫描公有代码库中配置不当的GitHub Actions工作流，将其武器化，窃取高权限令牌，最终控制整个仓库。这篇文章讲清楚了这个新兴攻击链，并分析了为什么CI/CD已成为安全新战场。

## 这不是演习

2026年2月底，连续几个高调的知名开源项目被发现遭受了协同攻击。事件被归咎于一个叫“HackerBot-Claw”的自动化操作。它利用的漏洞不是传统代码缺陷，而是项目里配置不当的GitHub Actions工作流。通过这些工作流，它实现了远程代码执行，并在CI/CD流水线里窃取到了高权限令牌。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibfts7LbGp9nLBxIeso7OywibaP0d0758LuevhIUZc3bjiaOKlJCJtpTzDwjl3cEq2icyDKq78OQHf5SdlAxic8FMtK80icZ04e3SNkk/640?wx_fmt=webp&from=appmsg)

时间线清晰地展示了这场攻击的节奏和波及面：

* 2月27日：微软和DataDog的项目分别通过分支名注入和文件名注入被瞄上。
* 2月28日：著名的awesome-go项目清单被成功利用，一个CNCF项目确认遭遇RCE，安全公司Aqua的Trivy项目因pull\_request\_target配置问题遭全面入侵。
* 甚至出现了针对基于Claude AI提示的自动化流程发起的提示注入攻击（被拦截了）。

说实话，这份受害者名单让你没法再觉得这只是“不小心”。从科技巨头到安全公司的核心工具，攻击者胃口不小，打法精准。

## 为什么GitHub Actions成了攻击者的新乐园？

现在，GitHub Actions差不多是现代开发者默认的CI/CD平台了。构建、测试、部署、安全扫描，都靠它自动化。可问题也在这儿。

工作流一旦配错了，就会给自动化引擎本不该有的权限。你以为是可信的自动化帮手，结果变成了攻击者现成的武器。这种“自动化信任”的滥用，是问题的核心。

早在2025年9月，安全研究就演示了如何利用GitHub Actions漏洞攻击数千个仓库，其中不乏微软、谷歌、英伟达这样的财富500强公司的项目。

关键就在于`pull_request_target`这个触发器。它可以用来运行来自不受信任的Pull Request的代码，但工作流本身却继承了仓库写级别的权限（比如`GITHUB_TOKEN`）。很多开发者没搞清楚这块，直接照着网上的例子配，权限就给大了。

> 下面这个配置就是典型的“高危”工作流示例。`pull_request_target`触发器加上`contents: write`和`pull-requests: write`的权限，再去checkout拉取请求的代码（`ref: ${{ github.event.pull_request.head.sha }}`），相当于让攻击者的代码在你的流水线里为所欲为。

name: Dangerous PR runner
on:
  pull\_request\_target:

jobs:
  run-pr-code:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull\_request.head.sha }}
      - name: Run script
        run: |
         scripts/run.sh

## HackerBot-Claw的攻击链：三部曲

这次攻击的手法非常标准化，可以拆解成三个清晰的步骤。

### 1. 扫描脆弱的CI工作流

HackerBot-Claw会扫描公有仓库里的`.github/workflows/*.yml`文件，找特定的危险模式。它的目标很明确：

* 使用`pull_request_target`触发的工作流。
* 权限开得过大（比如给了写权限）。
* 执行了不受信来源的代码。
* 复用了高权限的密钥。

找到这些，就等于找到了一个“可被武器化的自动化接口”。

### 2. 触发CI，窃取令牌

一旦锁定目标，就自动创建一个能触发该工作流的Pull Request。如果这个工作流真的有写权限运行（比如用了高权限的`GITHUB_TOKEN`），攻击者的代码就能在执行过程中把令牌给泄露出来。在Trivy的案例里，就是这么干的。

### 3. 滥用令牌，夺取控制

拿到令牌后，攻击者就能直接用GitHub API做很多事情了，比如：

* 删除已有的发布版本和关联的资产。
* 直接给仓库改名。
* 发布恶意制品，比如假冒的VSCode扩展。

这其实是一种CI权限提升攻击，和单纯的代码注入不太一样。它利用的是自动化流程的信任，直接拿到了系统的“钥匙”。

## 这不是孤例：CI滥用已成供应链攻击新宠

别以为只有HackerBot-Claw这么干。CI/CD系统的滥用已经是一种趋势。

2025年，一个被超过23000个工作流使用的官方Action——`tj-actions/changed-files`，就遭遇了供应链攻击。攻击者往Action的代码库里塞了恶意代码，导致使用它的工作流在日志里泄露了敏感密钥。

这两起事件说明了同一个问题：

* CI/CD系统里存着越来越多的敏感凭证和操作权限。
* 攻击者发现，攻击自动化逻辑本身，比攻击应用代码更高效，能直接收割、滥用或销毁关键的软件制品。

供应链的薄弱环节，从前端库、运行时依赖，现在蔓延到了构建和部署的自动化环节。

## 我们能做什么：防御建议

面对这种自动化攻击，被动补救不够，得主动加固。

首先，重新审视你的GitHub Actions工作流配置。核心原则是**最小权限**和**不信赖输入**。

* **慎用`pull_request_target`**

  ：除非绝对必要，别用这个触发器。如果要用，确保工作流本身不执行来自Pull Request的代码，或者用严格的沙盒环境。
* **收紧令牌权限**

  ：仔细设置`permissions:`块，只给工作流完成其任务所需的最小权限。`contents: write`这种大权限，一定要问自己是不是真的需要。
* **输入验证和净化**

  ：不要相信任何来自外部触发器的输入（分支名、提交信息、文件路径等）。

其次，检查你的项目是否在受影响仓库列表中。如果是，立即跟进维护者发布的官方通告和修复指南，更新配置，轮换可能泄露的凭证。

最后，把CI/CD安全纳入日常流程。这不再是“运维的事”或“可选的安全加分项”，而是保证软件交付链完整性的基础环节。定期扫描工作流配置，监控异常活动，像对待生产服务器一样对待你的构建环境。

> 攻击已经进化了。他们不再只是在你的代码里找bug，而是开始攻击你**构建和发布代码的机器**。如果我们还只盯着传统漏洞，就等于把大门钥匙挂在了最显眼的地方。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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