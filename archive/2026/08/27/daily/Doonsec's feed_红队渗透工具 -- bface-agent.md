---
title: 红队渗透工具 -- bface-agent
url: https://mp.weixin.qq.com/s/UD8iv_LmAQnGxTeFThV6dw
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:35:39.734026
---

# 红队渗透工具 -- bface-agent

# 红队渗透工具 -- bface-agent

gmeier909
gmeier909

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

基于 Claude Code 的认知驱动全栈红队 agent。核心理念：认知架构 > 工具堆砌。不是又一个"Web 控制台 + 自写 agent 编排 + 工具列表"，而是把 Claude Code 的原生能力（CLAUDE.md 记忆 / skill 方法论 / subagent 分工 / plan+todo 编排 / 文件工具）组织成一套有记性、有方法论、有验证闭环的渗透工作流。主要功能清单：

```
信息收集（资产测绘）三平台聚合：FOFA / Hunter(鹰图) / Quake 一键查询，跨平台按 ip:port 去重合并方言自动适配：写一次 FOFA 风格 query（如 icp="赛力斯"），自动转各平台语法（Hunter icp.name=、Quake icp:），无需记三套语法翻页拉全：max_pages 参数（1-20，默认 5），按各平台真实页大小智能判断末页停止，不空耗测绘积分多域名累积：同一 ip:port 的多个关联域名全部保留（Asset.Domains），不再只留首个丢数据资产面板：分页（page/total）+ 搜索（IP/域名/标题）+ 平台/协议分布统计 + 每行「前往」跳转链接MCP 工具：gather_assets（project_id + query + size + max_pages）双入口：MCP 工具（stdio/远程）+ Web /api/assets/refresh三平台 key 配置：config.yaml 的 fofa / hunter / quake 段，空 key 自动跳过该平台C2（Command & Control）4 种监听器：tcp_reverse / http_beacon / https_beacon / websocket18 种任务：exec / shell / pwd / cd / ls / ps / kill_proc / upload / download / screenshot / sleep / exit / self_delete / port_fwd / socks_start / socks_stop / load_assembly / persistPayload 生成：oneliner（6 种 shell）+ build（4 OS × 3 arch 交叉编译）Profile 伪装：Malleable Profile（UA / URIs / 头 / body / jitter）会话管理：心跳 / 看门狗 / 批量删除 / set_sleep事件总线 + SSE：实时推送浏览器监听器恢复：重启自动拉起 running listener（3 次退避重试）Beacon 加密：AES-GCM CSB1 魔数 + Legacy shell 兼容WebShell 管理9 个 MCP 工具：连接 CRUD + test + exec + file list/read/writeWeb 终端 + 文件浏览器
```

**0x02 安装与使用**

端到端验证

```
启动 server 模式 → 浏览器打开 Web 管理面 → 登录创建 TCP listener → 启动 → 生成 oneliner → 本地执行反弹 shellC2 会话上线 → 下发 exec/ps/ls 命令 → Web 实时看到事件流编译 beacon → 上线 → socks_start → 验证代理可用新建项目 → upsert 事实带 edges → 生成攻击图 mermaid登记漏洞 → Web 账本统计 → 验证三态流转知识库浏览/搜索 → 验证文件自动扫描配置 FOFA/Hunter/Quake key → gather_assets 收集资产（如 icp="xxx"）→ Web 资产面板分页/搜索/前往链接
```

网盘下载链接（一定要在虚拟机运行）：

```
后台回复：20260827获取下载链接，仅一天有效
```

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_jpg/U7LDNXUGXQuibiciaRzwfw5QtjwDHvtwKHBLVriaD1picuNUblTthG4Tk5T547z2glCmTFXcVNtTcMmwiavVcbtgLuy4kZKEEPG6QjHYkkEJCGtSU/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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