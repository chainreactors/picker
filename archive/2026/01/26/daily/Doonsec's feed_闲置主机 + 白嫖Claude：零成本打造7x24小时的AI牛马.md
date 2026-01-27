---
title: 闲置主机 + 白嫖Claude：零成本打造7x24小时的AI牛马
url: https://mp.weixin.qq.com/s/y711hmhW9aox9TVvRGwEWw
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:34:56.948544
---

# 闲置主机 + 白嫖Claude：零成本打造7x24小时的AI牛马

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIS3aF7TCS4HqdwKJPrhaciaY8AFSePjurFGFC9msiaeQBUksuZE70VyXA/0?wx_fmt=jpeg)

# 闲置主机 + 白嫖Claude：零成本打造7x24小时的AI牛马

原创

yzddMr6
yzddMr6

网络安全回收站

![]()

在小说阅读器中沉浸阅读

Claude Code 自发布以来，在开发者圈子里掀起了 Agent 的热潮。配合 Claude Opus 模型，它能自动编写代码、调试程序、安装依赖，让无数程序员惊呼"这才是未来的编程方式"。

但在日常使用中，两个痛点逐渐凸显：

第一个痛点是物理限制。电脑必须 24 小时开机，人必须坐在电脑前。Agent 在跑任务时，不能关机、不能离开，甚至不能让电脑休眠。

第二个痛点是权限控制。Claude Code 直接在主机环境运行，每次操作都需要手动确认权限。为了防止误删重要文件或污染系统环境，又不敢把所有权限默认放开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIzwpywgBQQHOm40eVIGicNZbNQ5uArLc6q8tdg23qfv3rkehDbIJmiaNg/640?wx_fmt=png&from=appmsg)

实际上大部分操作都不需要人工干预。真正需要关心的只有最终任务能不能完成，完成后通知看看结果就行。

所以，能否打造一个 7x24 小时运行的 AI 助手，在我吃饭、打游戏、甚至睡觉的时候，都能在后台干活？

分析了一下，解决这个问题需要三个关键要素：一个隔离的 Runtime 环境让 Agent 随意折腾，一个成本可控的大模型供 Agent 调用，以及一个支持远程访问的 Agent 框架。

经过一番研究和实践，最终选择了 **PVE + LXC** 作为 Runtime 方案，**Antigravity Manager** 白嫖 Claude Opus，**OpenCode** 作为 Agent 框架，成功打造了这个 7x24 运行的 AI 牛马。

## 隔离环境：为什么选择 LXC

### Runtime 的重要性

Runtime 是 Agent 能力的基石。模型能在 Runtime 中获取真实的执行反馈、与外界环境互动，就像真人在操作电脑一样。

有了 Runtime，模型不需要害怕犯错。它可以根据报错信息不断调整决策，自己编写代码、运行脚本、安装缺失的依赖。缺少工具？自己去搜索、下载、配置。

有了 Runtime，文件系统成为天然的上下文存储，再也不用担心对话中途记忆丢失的问题。Claude Code 的成功验证了这一点，而更早的 Manus 项目更是领先一个大版本。

但与此同时，Runtime 也带来了安全风险。Agent 可能误删文件、污染系统环境，甚至遭遇供应链攻击。因此这个 Runtime 必须是隔离的，Agent 可以在里面随意造，出了问题就删掉重建，不影响主机环境。

基于这个需求，云服务化的独立运行环境成为最佳选择。

### 技术方案选择

我把家里闲置的小主机利用起来，安装 Proxmox VE（PVE）虚拟化平台后创建 LXC 容器，并打包成模板。这样每次环境被污染，直接克隆模板就能在几秒内新建一个干净的机器。

LXC 比虚拟机更加轻量，可以最大限度利用主机性能。

方案选型时需要考虑几个关键问题：

**为什么选择 LXC，而不是直接用 Docker？**

因为需要 Agent 运行在一个完整的、模拟真实服务器的环境中。Agent 在执行复杂任务时可能需要运行 Docker 容器，而 Docker in Docker 嵌套方案存在诸多限制和性能问题。

LXC 提供了完整的操作系统环境，Agent 可以像在真实服务器上一样操作。

**为什么不用 OpenHands 等开源方案？**

OpenHands 的 Agent 与沙箱耦合太严重。沙箱不是独立的完整操作系统，而是通过 API 接口下发命令。这种设计限制了 Agent 的自由度，与"给 Agent 一个真实环境"的理念不符。

下图是在 PVE 中创建的 LXC 容器列表，每个容器都是一个独立的隔离环境：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIfibRDcYG1cC8vLAiazeebR1dicr9h61tCsUQz2BkZTpPIvV62DpBk6C1Q/640?wx_fmt=png&from=appmsg)

### 容器配置与可视化

采用 Debian 作为基础容器镜像，预装了常用的 Python 库、Docker以及开发工具链。为了应对需要图形界面的任务，还在容器中部署了 **Webtop** 项目。

Webtop 是一个基于 Docker 的容器可视化方案，它能通过浏览器访问容器内的完整 XFCE 桌面环境。当 Agent 需要操作浏览器、运行 GUI 程序时，可以直接调用这个可视化界面。

通过浏览器访问 3001 端口（HTTPS），就能看到运行在容器中的图形化桌面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIvS018mSCQLxd1tBdupFjibNJ6ECAqyjKJCuRFewvsa5uvUqUMH1tM5A/640?wx_fmt=png&from=appmsg)

### 安全加固

虽然是隔离环境，但作为安全从业者，还是做了一些必要的加固措施：

1. 1. **内核更新**：及时更新 LXC 容器的内核版本，修复已知安全漏洞
2. 2. **取消特权模式**：禁用 LXC 特权容器，限制容器对宿主机的访问能力
3. 3. **网络隔离**：配置防火墙规则，禁止容器访问内网敏感资源
4. 4. **资源限制**：通过 cgroup 限制容器的 CPU、内存和磁盘使用

毕竟如果遭遇供应链攻击，隔离环境被突破，整个家庭网络都可能被偷家。

## 白嫖方案：零成本调用 Claude Opus

Runtime 环境搭建完成，第二个问题是模型选择。在我测试过的所有大模型中，Claude Opus 4.5 的能力是遥遥领先的——代码理解、复杂推理、上下文长度都碾压其他模型。

但问题在于，官方的 Claude API 价格实在太贵。如果让 Agent 7x24 小时运行，每月的 API 费用可能高达数百美元。对于个人开发者来说，这个成本难以承受。

这时候就要感谢大善人 Google 了。

Google 提供学生认证计划。通过学生邮箱认证后，就可以升级为 Gemini Pro 用户。Gemini Pro 用户可以使用 Google 推出的 **Antigravity** 代码编辑器，而 Antigravity 不仅支持 Google 自家的 Gemini 模型，还集成了 **Claude Opus 4.5！**

关键是，这个调用是免费的，没有硬性的 token 限制（有 rate limit 但足够个人使用）。

### Antigravity Manager 反代方案

但 Antigravity 是一个 IDE，无法直接给 OpenCode 等 Agent 框架调用。这时候就要用到开源项目 **Antigravity Manager** 了。

这个项目的核心功能是把 Antigravity 的 Claude 接口反向代理出来，转换成标准的 OpenAI API 格式或 Anthropic API 格式，供其他应用调用。它还支持：

* • **多账号管理**：轮流调用多个 Google 账号，分散 rate limit
* • **限流控制**：避免触发 Google 的频率限制
* • **日志监控**：记录每次 API 调用的详细信息
* • **模型映射**：将 Antigravity 的模型名称映射为标准格式
* • **负载均衡**：自动选择可用账号，实现高可用

下图展示了 Antigravity Manager 的管理界面，可以看到多个账号的调用情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclI7lrM2ic5Be8dADKnib3xdNL00DH9wyZUW5oHS9uU7K9H9KOUAvyzxOoA/640?wx_fmt=jpeg&from=appmsg)

它还提供 API 反代、流量日志等功能，可以学习官方的 Prompt 写法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIcia9AWrxhOicXnbve7lUXX3EsRqfbfOibh0pR4kNb95upaSg9NuwkpAxA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIiauOnzGKMdYqJl7Rb5qBjJjQbpbciaW5s21c5sLVFGaA61WBJUhvTbEA/640?wx_fmt=png&from=appmsg)

### 家庭组多账号策略（1+5）

Google 还有一个神仙功能：**家庭组（Google Family）**。一个主账号通过学生认证后，可以邀请最多 5 个其他账号加入家庭组。家庭组成员享有与主账号相同的 Gemini Pro 权限，可以同样免费使用 Antigravity。

这意味着，可以用 1 个学生账号 + 5 个普通账号，总共 6 个账号轮番调用 Claude Opus。配合 Antigravity Manager 的负载均衡功能，相当于 6 倍的 rate limit。

对比官方 API 动辄每月数百美元的费用，这套方案的成本为零。唯一的限制是 rate limit，但 6 个账号轮换已经足够个人使用，狠狠榨干最后一丝 token。

## Agent 框架：OpenCode 的优势

### OpenCode vs Claude Code

Runtime 和模型都准备好了，接下来要选择 Agent 框架。Claude Code 是 Anthropic 官方出品，稳定性和体验都很好。但它有两个限制：

1. 1. **模型绑定**：只能使用 Claude 系列模型，无法灵活接入任意厂商
2. 2. **闭源设计**：无法进行二次开发和定制

这时候 **OpenCode** 项目进入了视野。它可以看作是 Claude Code 的开源版，通过社区的力量增加了许多功能，在某些任务上体验甚至超过了官方版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIEbI77oenyYQzr7FwDC3dPgb9RLbGk3gYicicQblJoRjKTrFUR9xYzwxQ/640?wx_fmt=png&from=appmsg)

OpenCode 的核心优势在于开放性。它不仅支持 Claude、GPT、Gemini 等主流模型，还允许接入本地部署的开源模型。更重要的是，开源意味着可以进行深度定制——修改 prompt、调整工作流、添加自定义工具。

Github上作者也列出了OpenCode和Claude Code的对比：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIeoEfp2bxEGSc53NgyeOatUjm32icicjbVKFibAmVPKibJIkgQvwdMuLKNQ/640?wx_fmt=png&from=appmsg)

### 插件生态

OpenCode 最吸引人的地方是插件生态。社区开发了大量增强插件，其中最值得推荐的是 **oh-my-opencode**。

这个插件提供了 **ultrawork 模式**，可以防止模型"偷懒"。常见的情况是：Agent 执行任务时遇到一次错误，尝试修复失败后就直接放弃了。

ultrawork 模式可以让模型无限制地尝试下去，直到任务成功或达到预设的最大轮次。启用 ultrawork 后，Agent 会更加"执着"，不轻易放弃任务。这对于复杂的自动化场景非常有用。

### 使用Antigravity的接口

还有一个关键问题：如何让 OpenCode 调用 Antigravity Manager 反代出来的 Claude 接口？我研究了一下，总共有三种方式：

**方式 1：自定义 API 接口**

OpenCode 支持添加自定义的 API provider。由于 Antigravity Manager 可以反代出标准的 OpenAI 格式接口，可以将其配置为一个自定义 provider。

**方式 2：修改 baseURL**

OpenCode 允许修改 Claude provider 的 baseURL，让它重定向到 Antigravity Manager 的反代地址。由于反代接口协议兼容 Anthropic API，这种方式可以无缝接入。

**方式 3：使用 opencode-antigravity-auth 插件**

最简单的方式是安装 opencode-antigravity-auth 插件。它可以直接把 Antigravity Manager 的模型加入到 OpenCode 的模型列表中，无需手动配置复杂的 baseURL 和 API key。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU4cuIzWz2zgNR1a7XFlgiclIAJHRRFNX3vkialIKicGaibH2sibueIlYpRLyiaeic5yubpyqeBKzhdjLLQBQ/640?wx_fmt=png&from=appmsg)

这里贴一下完整配置，不想折腾的同学可以直接抄作业：

```
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-opus-4-5",
  "provider": {
    "anthropic": {
      "options": {
        "baseURL": "http://192.168.1.100:8045/v1",
        "apiKey": "sk-antigravity-xxxxxxxx"
      }
    },
    "google": {
      "models": {
        "antigravity-gemini-3-pro": {
          "name": "Gemini 3 Pro (Antigravity)",
          "limit": {
            "context": 1048576,
            "output": 65535
          },
          "modalities": {
            "input": ["text", "image", "pdf"],
            "output": ["text"]
          },
          "variants": {
            "low": { "thinkingLevel": "low" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-gemini-3-flash": {
          "name": "Gemini 3 Flash (Antigravity)",
          "limit": {
            "context": 1048576,
            "output": 65536
          },
          "modalities": {
            "input": ["text", "image", "pdf"],
            "output": ["text"]
          },
          "variants": {
            "minimal": { "thinkingLevel": "minimal" },
            "low": { "thinkingLevel": "low" },
            "medium": { "thinkingLevel": "medium" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-claude-sonnet-4-5": {
          "name": "Claude Sonnet 4.5 (Antigravity)",
          "limit": {
            "context": 200000,
            "output": 64000
          },
          "modalities": {
            "input": ["text", "image", "pdf"],
            "output": ["text"]
          }
        },
        "antigravity-claude-sonnet-4-5-thinking": {
          "name": "Claude Sonnet 4.5 Thinking (Antigravity)",
          "limit": {
            "context": 200000,
            "output": 64000
          },
          "modalities": {
            "input": ["te...