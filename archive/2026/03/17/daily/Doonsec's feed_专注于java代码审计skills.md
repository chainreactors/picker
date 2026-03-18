---
title: 专注于java代码审计skills
url: https://mp.weixin.qq.com/s/HE7bQMDtny2KA07N6FkE7g
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:16:35.964307
---

# 专注于java代码审计skills

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnSeqOIs1xPI6MKkRCeLbzhRAKmdwuaJyqX9EWdneHbib2DZ2GLY9lpMutB8D69ic778tzW21ZpLZkOfc6EraffdV7k7XrEzfEiaU/0?wx_fmt=jpeg)

# 专注于java代码审计skills

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 624，阅读大约需 4 分钟

## 前言

项目地址：https://github.com/RuoJi6/java-audit-skills

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlpbr1eiajaQl3rs9PAUm5QB6ib1TKtA58MyqusyG3NGPkAAPeYBzG259GqCtEUbJ5qpJ4VNOlwxOnfic0icYbEYfp1biaHaxiaWNH7c/640?wx_fmt=png&from=appmsg)

559236ee61fef0910122633d794b3e94.png

专注于 Java 代码审计的 Claude Skills 集合，提供自动化源码分析、路由提取、参数映射等功能，辅助安全研究人员和开发者进行 Java Web 应用的安全审计工作。

## 功能特性

* • **自动路由识别**：自动识别 Java Web 项目中的 HTTP 路由结构
* • **多框架支持**：支持 Spring MVC、Servlet、JAX-RS、Struts 2 等主流框架
* • **参数结构解析**：提取 Path、Query、Body、Header、Cookie 等各类参数
* • **反编译集成**：集成 Java 反编译器，支持分析已编译的 .class 和 .jar 文件
* • **Burp Suite 集成**：生成可直接用于 Burp Suite Repeater 的请求模板
* • **接口文档生成**：为无 API 文档的项目生成接口清单
* • **路由调用链追踪**：追踪从 Controller 到 DAO 层的完整调用链，分析参数流向
* • **鉴权机制审计**：识别鉴权框架实现，分析鉴权绕过和越权访问风险
* • **SQL 注入审计**：识别 SQL 执行框架，检测 SQL 注入漏洞风险
* • **文件上传审计**：识别文件上传入口，分析路径穿越和可执行文件上传风险
* • **文件读取审计**：识别文件读取操作，分析路径遍历攻击风险
* • **XXE 审计**：识别 XML 解析操作，检测外部实体注入漏洞风险
* • **组件漏洞检测**：扫描第三方依赖，匹配 130+ 条 CVE 规则，生成安全报告
* • **全链路审计流水线**：使用 agent team 编排多个审计 skill（含动态扩展的调用链追踪 worker），一键完成完整安全审计

## 安装

安装 java-decompile-mcp
https://github.com/RuoJi6/java-decompile-mcp

CFR jar 包下载：：https://github.com/leibnitz27/cfr

MCP 中配置

```
{
  "mcpServers": {
    "java-decompiler": {
      "type": "stdio",
      "command": "uvx",
      "args": ["java-decompile-mcp"],
      "env": {
        "CFR_PATH": "/你的路径/cfr-0.152.jar"
      },
      "disabled": false
    }
  }
}
```

将 skills 目录下的内容复制到 Claude Code 的 skills 配置目录中。

## 使用 Skill

自动编排多个 agent（含动态扩展的调用链追踪 worker）完成完整审计流程：路由分析 → 鉴权审计 → 组件漏洞 → 交叉筛选（风险分级+漏洞汇总）→ 调用链追踪（分批并行）→ 漏洞深度分析（按 sink 类型并行，含可利用前置条件）→ 质量校验。

## 最佳实践

1. 1. 优先使用源码，仅在必要时使用反编译
2. 2. 记录每个路由的源文件位置便于追溯
3. 3. 输出格式统一，便于后续处理
4. 4. 遇到无法解析的配置时记录并跳过

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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