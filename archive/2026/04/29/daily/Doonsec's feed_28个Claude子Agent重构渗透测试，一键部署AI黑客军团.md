---
title: 28个Claude子Agent重构渗透测试，一键部署AI黑客军团
url: https://mp.weixin.qq.com/s/7UvpaAmzQtg7IQ21p8wuQw
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:28:52.269258
---

# 28个Claude子Agent重构渗透测试，一键部署AI黑客军团

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX311Xd7t7iaWCGhHEMLMrbcQGuc25VhK2WVIRjtPFZNmmkzuw4ChOxcjW0wOd13IicjxgAOicibJmvbtj7aaK34VZTjeq2mzZVnh64/0?wx_fmt=jpeg)

# 28个Claude子Agent重构渗透测试，一键部署AI黑客军团

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1TibEOBJp1XQqbpiaq7E1QBB0mNgCUXRGG7H6L3QZ8IPhfmOAB517Kog68hSpfTo6fBfJdCghXsWKh32Lyb4M2FZ7iaV4lEF73Sk/640?wx_fmt=png&from=appmsg)

##

## 一款名为pentest-ai-agents的全新开源工具包正在重新定义安全专业人员如何在渗透测试工作流程中利用AI技术。该工具将Anthropic公司的Claude Code转变为完全专业化的攻防安全研究助手，通过28个特定领域子Agent实现功能。

##

**Part01**

## ****专业化Agent架构****

由安全研究员0xSteph在GitHub发布的pentest-ai-agents包含28个Claude Code子Agent，每个子Agent在整个渗透测试生命周期中都具备深厚的领域专业知识。覆盖范围包括：

* 侦察阶段
* Web应用测试
* Active Directory攻击
* 云安全测试
* 移动端渗透
* 无线网络攻击
* 社会工程学
* 漏洞利用链构建
* 检测工程
* 取证分析
* 恶意软件分析
* 报告生成

与传统单一通用AI模型不同，该框架会自动将每个查询路由至最合适的专业Agent。

**Part02**

## ****一键式安装部署****

安装过程无需服务器、外部依赖或复杂配置，仅需执行以下命令：

```
curl -fsSL https://raw.githubusercontent.com/0xSteph/pentest-ai-agents/main/install.sh | bash
```

安装脚本会自动克隆代码库，将所有28个Agent文件复制到~/.claude/agents/目录。该脚本具有完全幂等性，重复执行可安全更新现有Agent。

额外安装选项支持：

* 项目级部署（--project参数）
* 成本优化的精简模式（--global --lite参数），可在Claude Haiku上运行咨询类Agent以减少token消耗

**Part03**

## ****双层执行模型****

工具包采用双层执行模型以确保安全性和灵活性：

* 咨询模式（Tier 1）：用户粘贴工具输出，Agent提供优先级分析、方法指导及后续命令建议
* 执行模式（Tier 2）：Agent直接针对已声明的授权范围编写和执行命令，每个命令执行前需经用户明确批准

Tier 2 Agent包括：

* 侦察顾问（nmap/whois/whatweb）
* Web猎手（ffuf/sqlmap/dalfox）
* AD攻击者（BloodHound/Impacket/CrackMapExec/Certipy）
* 漏洞链构建器
* PoC验证器
* 业务逻辑猎手

所有攻击行为都映射到MITRE ATT&CK框架标识符，并配有防御上下文说明。

**Part04**

## ****持久化存储与扩展支持****

内置基于SQLite的发现数据库（findings.sh）可跨Claude Code会话保存任务数据，支持多日连续操作的无缝交接。当findings.sh位于系统PATH时，Tier 2 Agent会自动写入该数据库。

报告生成Agent可输出专业渗透测试报告，包含：

* 执行摘要
* CVSS评分
* 修复路线图

对于隔离网络或隐私敏感环境，通过附带的opencode-setup.sh脚本可将Agent转换为兼容Ollama、LM Studio或任何本地模型的OpenCode自定义命令。

配套的MCP服务器（pentest-ai）扩展了生态系统功能，提供：

* 150+工具封装
* 自动化漏洞链构建
* 面向Claude Desktop、Cursor和VS Code Copilot的CI/CD流水线集成

**参考来源：**

pentest-ai-agents – 28 Claude Code Subagents for Penetration Testing

https://cybersecuritynews.com/pentest-ai-agents-tool/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX35G7k64c48B99uZkuuR671UZWGdEupiaVBicRMGWR12rkvSibdbNBAvkOKX1PTJgF2vaNOHAPibyvD1rRQZrPqspfk94jOC2kfgQg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337326&idx=1&sn=4b4825de0e4f83e00dad9cfa560df6f2&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3ZpWvGCRdgV47vowHRaKLyiabNqzzXsw8xayQB0syqrORNfrd3y68vNFTC4Ed7mTqWkNvkrhaeWqbJZUSWpFGFFEaAKafgmpsE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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