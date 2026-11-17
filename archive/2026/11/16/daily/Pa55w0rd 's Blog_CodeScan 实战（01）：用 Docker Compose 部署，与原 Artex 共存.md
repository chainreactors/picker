---
title: CodeScan 实战（01）：用 Docker Compose 部署，与原 Artex 共存
url: https://www.pa55w0rd.online/codescan-01/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:35.930397
---

# CodeScan 实战（01）：用 Docker Compose 部署，与原 Artex 共存

# [Pa55w0rd 's Blog](/)

## [代码审计、威胁建模与企业安全实践](/)

[首页](/)
[归档](/archives)
[威胁情报](/threat-broadcast)
[关于我](/about)
[留言](/comments)
[公益404](/404.html)

2026-11-16

[开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)►[CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)

约 1.3k 字
约 4 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（01）：用 Docker Compose 部署，与原 Artex 共存

# CodeScan 实战（01）：用 Docker Compose 部署，与原 Artex 共存

[系列目录](/codescan-00/) · 第 01 篇 · 部署与更新

本地已经运行原 Artex 时，新项目最先要解决的是共存：端口、数据库、卷和登录状态都需要核对。只换一个访问端口，隔离工作还没有结束。

这一篇记录 CodeScan-Artex 的本地部署方式。命令以 PowerShell 7 和 Docker Desktop 的 Linux 容器模式为例，示例路径需要替换成自己的源码位置。

## 0x01 先确认拿到的是哪份程序

本地配置使用上游运行镜像提供基础环境，再把当前工作树构建出来的后端、审计工具和内嵌前端放进去。

这意味着，直接拉取上游镜像，不能据此认定已经得到本系列全部改造。部署前需要取得包含对应修改的源码，并核对 `dist/local/build-manifest.json` 中的版本与摘要。

主要文件如下：

| 文件 | 职责 |
| --- | --- |
| `deploy-local.ps1` | 检查环境、选择端口、生成本机配置、构建与启动 |
| `compose.local.yml` | 独立应用、PostgreSQL、网络和数据卷 |
| `Dockerfile.local-runtime` | 把当前构建产物放入运行镜像 |
| `dist/local/build-manifest.json` | 记录构建版本及程序摘要 |

## 0x02 首次部署

先准备 Docker Compose、Go 和 Node.js/npm。Go 版本以工作树里的 `go.mod` 为准；前端依赖按锁文件安装。

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` Set-Location -LiteralPath 'D:\projects\code-audit\CodeScan-Artex' .\deploy-local.ps1 -Port 17878 ``` |

本地约定使用 `codescan-artex-local` 作为 Compose 项目名，对外只绑定 `127.0.0.1:17878`。原实例使用的 `8787` 保留。

要改成另一个空闲端口，可以显式传入 `-Port 17879`。显式端口被占用时应先处理冲突，避免把别的服务误认为本次部署结果。

脚本生成的 `.env.local` 属于本机私有配置，保存数据库口令和本地执行记录签名密钥。文章不提供固定口令，也不把实际配置文件放进示例。

## 0x03 启动后核对什么

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` docker compose --project-name codescan-artex-local --env-file .env.local -f compose.local.yml ps docker compose --project-name codescan-artex-local --env-file .env.local -f compose.local.yml logs --tail=100 app ``` |

浏览器打开 `http://127.0.0.1:17878`，完成管理员设置，再配置模型服务。一次验收至少需要回答：

1. 应用与数据库是否就绪，访问到的版本是否对应本次构建？
2. 前端是否为真实后端模式，静态文件是否能正常加载？
3. 应用和数据库分别挂载了哪些卷？
4. 原实例的容器标识、端口和卷是否保持预期？

主进程健康只说明服务可响应。模型可用性和一次完整审计，需要后续分别验证。

## 0x04 模型地址要从容器视角理解

模型服务运行在 Windows 主机上时，容器内的 `127.0.0.1` 指向容器自己。开发环境可以使用下列地址形式：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` http://host.docker.internal:8000/v1 ``` |

这里的端口和模型名称都是示例，应替换成实际服务配置。还需要确认协议格式、鉴权、模型标识、上下文窗口和输出上限。

连接测试成功只能证明一条最小调用路径可用。长上下文排队、流式响应和工具调用，应在后续测试中逐项核对。

[![原Artex的8787入口与CodeScan的17878入口使用各自应用、数据库和状态卷，CodeScan容器通过host.docker.internal访问主机模型。](/assets/codescan/01-deployment-boundaries-v1.webp)](/assets/codescan/01-deployment-boundaries-v1.svg "本地部署：同机共存与访问边界")

图 01｜本地共存与网络访问示意，模型端口以实际配置为准。 [打开 SVG 原图](/assets/codescan/01-deployment-boundaries-v1.svg)

## 0x05 已有实例更新，要先保护状态

首次部署和带数据更新的检查重点不同。已有任务时，我先记录容器、卷、任务状态及模型配置，再备份数据库、现有构建产物和登录签名密钥。

本次环境中特别需要注意 `/app/jwt.key`：它位于应用容器文件系统，不能仅凭业务数据卷还在，就认定重建后登录也会保留。

可以先导出密钥到受控的本地备份目录：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` docker cp codescan-artex-local-app-1:/app/jwt.key .\data\maintenance\jwt.key ``` |

执行前先创建备份目录；密钥应按私有文件保护。真正替换应用时，还要保存它原有的权限与归属，在新容器启动前恢复，并核对摘要。数据库备份则应使用与当前版本匹配的 `pg_dump` 流程，核验导出结果。

更新计划通常只需要重建本项目的应用容器。数据库容器、状态卷及其他项目都不应顺手重建。对于暂停或失败的任务，也应保留原状态，避免升级顺带恢复模型请求。

## 0x06 这一篇的验收边界

本系列后续的部署记录会给出各轮版本和测试范围。部署方法本身不证明审计能力，也不能替代一次恢复演练。

源码入口是 `deploy-local.ps1`、`compose.local.yml`、`Dockerfile.local-runtime` 和 `server/auth.go`。常规更新前还应核对这些文件有没有变化，尤其是密钥路径、卷挂载和构建方式。

[上一篇：系列导读](/codescan-00/) · [下一篇：三个项目怎样集成](/codescan-02/)

<https://www.pa55w0rd.online/codescan-01/>

分享到
[留言](/codescan-01/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [Docker](/tags/Docker/)
* [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-01/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据](/codescan-02/)
[**下一篇 →**

CodeScan 实战（00）：从一次代码审计需求，到一套可追溯的工程实践](/codescan-00/)

## 留言

欢迎补充、纠错或交流；发表评论需使用 GitHub 账号登录。

正在加载留言…

请启用 JavaScript 以查看留言。

### 近期文章

* [CodeScan 实战（00）：从一次代码审计需求，到一套可追溯的工程实践](/codescan-00/)
* [CodeScan 实战（01）：用 Docker Compose 部署，与原 Artex 共存](/codescan-01/)
* [CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据](/codescan-02/)
* [CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁](/codescan-03/)
* [CodeScan 实战（04）：把威胁建模接进真正的任务生命周期](/codescan-04/)

### 分类

* [note](/categories/note/)46
* [web安全](/categories/web%E5%AE%89%E5%85%A8/)14
* [安全建设](/categories/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/)31
* [应急响应](/categories/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)4
* [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)25
  + [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)18
* [移动安全](/categories/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/)3

### 标签云

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%...