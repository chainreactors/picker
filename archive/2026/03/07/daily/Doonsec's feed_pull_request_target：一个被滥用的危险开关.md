---
title: pull_request_target：一个被滥用的危险开关
url: https://mp.weixin.qq.com/s/0DJMkxXZP0vK5QCM9fy2Pw
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:04:42.413810
---

# pull_request_target：一个被滥用的危险开关

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeNV39SFddjriaGChEbibAK7U4vrbT0MRZeJXwIZoFEDTyWO8rTibibFEiclbxnPwLneds8r4of7RX8WcZH0JcyJTu3oPTZVg5a8gZE/0?wx_fmt=jpeg)

# pull\_request\_target：一个被滥用的危险开关

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 开源安全团队Orca揭露了一个由GitHub Actions工作流配置错误引发的供应链攻击风险。多个知名开源项目，包括谷歌、微软等巨头的仓库，都因为一个叫`pull\_request\_target`的触发器而暴露在远程代码执行（RCE）和数据窃取的危险之下。这篇文章将带你了解攻击是如何发生的。

## 拉取请求怎么就成了噩梦？

想象一下，一个外部开发者给你的开源项目提了个代码拉取请求（Pull Request）。你觉得没问题，CI/CD流水线会自动运行测试。但就在这个看似平常的环节，你的仓库可能已经沦陷了。

Orca安全研究团队发现，问题的核心在于一个叫`pull_request_target`的GitHub Actions事件触发器。这个触发器和更常见的`pull_request`触发器有着本质区别。`pull_request`运行时，使用的是fork分支的上下文，权限较低。但`pull_request_target`不同，它会在**基础仓库的上下文**中运行，这意味着它能直接访问仓库的机密信息（secrets），并且默认拥有GITHUB\_TOKEN的读写权限。

这个触发器的本意是好的，用来安全地处理一些需要高权限的任务，比如给PR打标签、进行分类。

name: Labeler
on: [pull\_request\_target]

jobs:
  label:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
    - uses: actions/labeler@v4
      with:
        repo-token: "${{ secrets.GITHUB\_TOKEN }}"

上面这个例子很常见，就是用PR来触发自动标签机器人。`pull_request_target`在这里是必须的，因为“打标签”这个动作需要有写权限来修改PR的元数据。

但问题就出在，如果工作流不仅仅是打标签，而是去执行了来自PR的、不受信任的代码，那么`pull_request_target`提供的所有高权限，都会成为攻击者的武器。

## 当CI/CD执行了恶意代码

漏洞的关键在于，这些被攻陷的工作流都犯了一个相同的错误：**在拥有高权限的上下文中，检出了外部PR提交的代码并执行了它。**

我们来看一个危险的例子：

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

这个工作流用`pull_request_target`触发，配置了`contents: write`权限。接着，它通过`github.event.pull_request.head.sha`这个变量，直接检出了PR提交者的分支代码，然后执行了里面的`scripts/run.sh`脚本。

这下完了。原本只该对PR进行分类或验证的任务，现在毫无戒备地执行了一个外部贡献者提交的、任意内容的脚本。这个脚本运行在拥有基础仓库写权限的GitHub Runner上，攻击者现在可以为所欲为。

> 这个配置模式是许多漏洞的根源：用高权限（pull\_request\_target）去处理不可信的数据（外部PR代码）。

在分析中，Orca团队总结了几个反复出现的、危险的错误配置：

* **过于宽泛的令牌权限**

  ：工作流直接赋予外部贡献者向仓库推送代码的能力。
* **机密信息泄露**

  ：敏感的API密钥、令牌被内嵌在配置不当的工作流中，让攻击者轻松窃取。
* **自托管Runner被外部利用**

  ：通过自动批准的错误配置，将功能强大的自托管云服务器暴露给外部用户使用。
* **遗留的粗粒度令牌**

  ：许多在GitHub 2021年改进令牌细粒度权限控制前创建的老仓库，还在使用权限过大的旧令牌。

具体影响因项目而异，但根本风险都一样：**让不受信任的代码，以过高的特权运行。**

## 漏洞早已在现实中蔓延

这不是理论推演。在研究中，Orca团队发现多个出自名门的、不同组织的开源仓库都中了这招。

他们利用这些漏洞，成功做到了一些“危险动作”：

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfpyL8fkibutKpwusKFuic54IsJQQ4pz8gO8me9kia03MtwgAwg4IOpoGPOOiaE4J7UbAVh0AJ6c0GnpSYyp7ibuVwnLpPVtpiansXx8/640?wx_fmt=webp&from=appmsg)

▲ 利用被攻陷的Github Actions Runner向main分支写入代码

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcEjoAgHicPWDu8jkZma4Vce1EzEtxP9ap4feI2lz8zPGgI3RN4vz0XmhpNoAU5nPoQ5wuKKEuSsh3CA1qgFPEOrFwyib9jLOA8s/640?wx_fmt=webp&from=appmsg)

▲ 利用被攻陷的Github Actions Runner操纵Pull Request

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeFj8yibNbHqrcPgGIt1Uj8EHLia8I46pgeykOlHPuwZXGGbskcdiaMXLwIHicI8fsHNricRNHIb9tLC9zgwOLCpjwv8T4uQjaegr4I/640?wx_fmt=webp&from=appmsg)

▲ 利用被攻陷的Github Actions Runner向组织级GitHub包仓库推送内容

有些漏洞暴露了敏感的API密钥；有些让我们能力直接向包括`main`在内的受信任分支推送代码；更有甚者，让我们得以滥用云端的后台资源。

说实话，看到谷歌、微软这样的公司也会在开源仓库里留下这种配置隐患，让人有点意外。这恰恰说明，`pull_request_target`的误用和CI/CD安全，是一个需要整个开发社区严肃对待的系统性问题。

单一的一个错误配置的流水线，通过一个看似无害的fork PR，就可能演变成一次完整的供应链攻击。

> Orca表示，他们已通过负责任的披露程序，将发现报告给了受影响的组织。本文仅仅是第一部分。9月30日发布的第二部分，将带你进入真实事件的幕后，一步步复盘攻击链，看看那些微小的配置疏漏是如何被串联起来，造成灾难性后果的。

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