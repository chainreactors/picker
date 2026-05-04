---
title: 个人博客Hugo接入阿里云腾讯云ESA边缘加速实战指南
url: https://mp.weixin.qq.com/s/6kPq1dRi4GBDPmXLlqk-Hw
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:28:18.854681
---

# 个人博客Hugo接入阿里云腾讯云ESA边缘加速实战指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6EuqF9cSY2lhiaTl16mks4r2QGbsQq3OBJwrVOd1mNkiavLhlJDT8hN5xDpbhiaA3XYVmuo98Kgx1gbxOJOl6buibzfOpPaYuuQlBkDjQdtKAgo/0?wx_fmt=jpeg)

# 个人博客Hugo接入阿里云腾讯云ESA边缘加速实战指南

原创

xiejava
xiejava

fullbug

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2l65XUsvCrfuibZ8GnjvSs0pnDk5RKj1iaE6dMXlGu6ff6DvcP4KCowxs7tb143a37IAM8mxdpe9zX15miaQEe2PKxtLNdss2dRIY/640?wx_fmt=jpeg)

我的个人博客 xiejava.ishareread.com 是基于 Hugo 搭建的静态博客，托管在 GitHub Pages 上。虽然 GitHub Pages 免费稳定，但在国内访问速度一直不太理想，DNS 解析慢、连接延迟高，部分地区甚至出现无法访问的情况。

为了提升国内用户的访问体验，我分别采用了两种方案进行加速：一是通过**阿里云 ESA（边缘安全加速）**对 GitHub Pages 进行反向代理加速，二是通过**腾讯云 EdgeOne Pages** 将博客直接部署到边缘节点。经过实际测试，访问速度提升了 **60%~85%**，效果非常显著。

本文将详细介绍为什么要用 ESA 加速、两种加速方案的配置步骤以及加速后的实际效果。

## 一、为什么要用 ESA 进行加速

### 1、GitHub Pages 国内访问的痛点

GitHub Pages 是一个非常优秀的免费静态网站托管服务，但对于国内用户来说，存在以下问题：

* **DNS 解析慢**

  GitHub Pages 的域名 `github.io` 使用的是国外的 DNS 服务器，国内解析延迟较高
* **连接延迟高**

  服务器部署在海外，国内用户访问需要经过多次跨境跳转
* **部分地区访问不稳定**

  受网络环境影响，部分地区可能出现加载缓慢甚至无法访问的情况
* **静态资源加载慢**

  CSS、JS、图片等资源都是从海外服务器加载

### 2、传统 CDN vs ESA

相比传统 CDN，ESA（边缘安全加速）有明显的优势：

| 对比项 | 传统 CDN | ESA |
| --- | --- | --- |
| 接入方式 | 需要单独配置每个子域名 | 支持根域名一站式接入，所有子域名自动覆盖 |
| DNS 托管 | 不支持 | 支持，减少 DNS 延迟 |
| 安全防护 | 基础或无 | 集成 WAF、DDoS 防护 |
| 动态加速 | 不支持 | 支持智能路由优化 |
| SSL 证书 | 需手动配置 | 自动颁发和管理 |
| 边缘计算 | 不支持 | 支持 Serverless 边缘函数 |

### 3、阿里云 ESA 和腾讯云 EdgeOne 简介

**阿里云 ESA（Edge Security Acceleration）** 是一个全球分布式的边缘网络平台，通过遍布全球的 3200 多个边缘节点，提供一站式的网络加速、安全防护和边缘计算服务。

**腾讯云 EdgeOne** 是腾讯云基于 EdgeOne 基础设施打造的边缘安全加速平台，提供全球边缘网络加速、智能缓存和安全防护能力。

两者都提供了免费套餐或入门套餐，对于个人博客这种小型网站来说，成本几乎为零。

## 二、如何接入阿里云 ESA 进行加速

### 1、前提条件

在开始接入之前，确保你已经准备好以下内容：

* 一个**自定义域名**（如我的 `ishareread.com`）
* 博客已部署到 **GitHub Pages** 并且可以通过 `username.github.io` 正常访问
* 在 GitHub Pages 的仓库设置中已绑定自定义域名（通过 CNAME 文件）

### 2、创建 ESA 站点

登录阿里云 ESA 控制台，点击「添加站点」：

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2l18wU78glUU9TVEYLIMzf2sSF2sjJQQ6t97PYmktQ9X1el1feutKQ23yF5U3whmnDI5cm49I1djolLib2lxMPLlZ8mtyhs2III/640?wx_fmt=png&from=appmsg)

输入你的域名（如 `ishareread.com`），选择接入方式。ESA 支持两种接入方式：

* **NS 接入**

  （推荐）：将域名的 NS 记录指向阿里云，由阿里云托管 DNS 解析
* **CNAME 接入**

  ：在原有 DNS 服务商处添加 CNAME 记录指向 ESA

> **建议**：如果你只有一个域名且不涉及复杂的 DNS 配置，推荐使用 NS 接入，配置更简单，DNS 解析也更快。

### 3、配置 DNS 解析

选择 NS 接入后，阿里云会给出需要修改的 NS 记录地址。到你的域名注册商处，将域名的 NS 服务器修改为阿里云提供的地址：

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2l2As87IGgv5O28nP90N5xLuprEiasSna8HGicVUXSOnQHsUDKvccctgE2Jic54TicooodeEjPvJbWgE8bjnRHDFThBjfjdI6BXGHA/640?wx_fmt=png&from=appmsg)

NS 记录生效后（通常需要几分钟到几小时），在阿里云 ESA 的 DNS 管理中添加以下解析记录：

| 记录类型 | 主机记录 | 记录值 | 说明 |
| --- | --- | --- | --- |
| CNAME | `xiejava` （你的子域名） | `xiejava1018.github.io` | 指向 GitHub Pages |
| A | `@` | ESA 提供的 IP（可选） | 根域名直接访问 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6EuqF9cSY2kgZQUV4Xy4aQv7icAeuvoFicUnlHFIueO10a1Im86vZwUbBDW4exc33NMic41jyLqibPvbRzr4t4tyclOvhqEGAcgDUrDN8ibk2510/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6EuqF9cSY2n46wwlky3glD80QKeKfNkbkR1UmyFBWdtqkdB0pRR6psKyMsvcRttO8Lq06CdFibl3VhqPyB5Co2kDYKRyuhDmmuiaJexAnLXmU/640?wx_fmt=png&from=appmsg)

### 4、配置缓存规则

进入站点设置 → 缓存 → 缓存规则，配置合适的缓存策略。对于 Hugo 静态博客，推荐以下配置：

**默认缓存规则：**

| 资源类型 | 缓存时间 | 说明 |
| --- | --- | --- |
| HTML 页面 | 1 小时 | 博客页面，更新频率适中 |
| CSS/JS 文件 | 7 天 | 静态资源，变更少 |
| 图片文件 | 30 天 | 图片等媒体资源 |
| 字体文件 | 30 天 | 字体文件几乎不变 |

也可以通过「规则引擎」自定义更精细的缓存规则。例如：

* URL 路径匹配 `/posts/*` 的页面缓存 1 小时
* 文件扩展名 `.css`、`.js`、`.png`、`.jpg` 的资源缓存 30 天
* 首页 `/` 缓存 30 分钟，便于及时更新

### 5、配置 SSL 证书

ESA 会自动为你的域名申请和管理 SSL 证书，支持泛域名证书。进入站点设置 → SSL/TLS，确认以下配置：

* **SSL/TLS 加密模式：选择「完全（严格）」，确保 ESA 到源站也走 HTTPS**
* **边缘证书：开启「始终使用 HTTPS」，自动将 HTTP 请求重定向到 HTTPS**
* **最低 TLS 版本：建议设置为 TLS 1.2**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6EuqF9cSY2mx4B242HpRibicf34s5PM03mTIGK4iaUEyHHAJXVKMvTD3bye9cUiaHNhnbPRmcDdP9d7G3qUkibOCXYZzOrnmSlicCmffrgxnrD6ic4/640?wx_fmt=png&from=appmsg)

### 6、配置源站

在站点设置中配置源站地址，指向 GitHub Pages：

源站地址填写 `xiejava1018.github.io`，协议选择 HTTPS，端口 443。

## 三、如何通过腾讯云 EdgeOne Pages 部署加速

与阿里云 ESA 的"反向代理加速"方式不同，腾讯云 EdgeOne 提供了 **Pages** 服务，可以直接将 Hugo 博客项目部署到边缘节点上。这种方式的优势是：**每次 Git 推送更新，边缘节点会自动构建和刷新缓存，网站内容实时更新**，无需手动刷新 CDN 缓存。

### 1、EdgeOne Pages vs ESA 加速方式对比

| 对比项 | 阿里云 ESA（反向代理） | 腾讯云 EdgeOne Pages（直接部署） |
| --- | --- | --- |
| 源站 | GitHub Pages | 无需源站，直接部署到边缘 |
| 更新方式 | 推送到 GitHub，ESA 回源拉取 | 推送到 GitHub，自动触发构建部署 |
| 缓存刷新 | 需要手动或等待过期 | 自动刷新，每次部署即时生效 |
| 构建流程 | 不参与构建 | 自动构建 Hugo 项目 |
| 适用场景 | 已有源站需要加速 | 静态站点直接托管部署 |

> **提示**：如果你的博客是纯静态站点，推荐使用 EdgeOne Pages 直接部署的方式，更简单高效。

### 2、添加 edgeone.json 配置文件

在 Hugo 项目根目录下创建 `edgeone.json` 文件，用于指定构建配置：

```
{    "hugoVersion": "0.160.1",    "buildCommand": "hugo --minify --buildFuture",    "outputDirectory": "public"}
```

配置说明：

* **hugoVersion：指定 Hugo 版本，建议与本地版本一致。EdgeOne Pages 内置 Hugo Extended 版本，支持 SCSS/SASS 编译**
* **buildCommand：构建命令，`--minify` 压缩输出，`--buildFuture` 构建未来日期的文章**
* **outputDirectory：Hugo 默认输出目录为 `public`**

将此文件提交到 Git 仓库。

### 3、在 EdgeOne Pages 控制台创建项目

登录腾讯云 EdgeOne Pages 控制台，点击「创建项目」：

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2mApfEMpsLogsAI4nPq2miaqGWibJ4xz788yTzlFba6mwmwIw9uZqmXCpyBd6dLPl8YLykIFRIDqctBTme2J3dBuiahYUn1GdRLtg/640?wx_fmt=png&from=appmsg)

EdgeOne Pages 提供三种创建方式：

* **通过导入 Git 仓库创建**

  ：适合已有 Hugo 项目（推荐）
* **通过模板创建**

  ：创建全新的 Hugo 站点，使用官方 hugo-starter 模板
* **通过上传文件创建**

  ：适合纯静态网站，内容基本不更新

对于已有的 Hugo 博客项目，选择「**通过导入 Git 仓库创建**」。

### 4、导入 GitHub 仓库

点击「导入 Git 仓库」，授权 GitHub 账号后，选择你的 Hugo 博客仓库（如 `xiejava1018/xiejava1018.github.io`）

### 5、配置构建设置

导入仓库后，需要配置构建设置：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6EuqF9cSY2k3ibkHQ8n37MALiaJk9TUfILlZcmvcOOibEky4Qk8lTBnIwick97IBaDCicpSMk7teBH2XMcA2g5OouxZeaNyHkicVL3s2tNibvmDcZg/640?wx_fmt=png&from=appmsg)

关键配置项：

| 配置项 | 推荐值 | 说明 |
| --- | --- | --- |
| 加速区域 | 全球（含中国大陆） | 已备案域名选择此项，覆盖国内用户 |
| 框架预设 | Other 或 Hugo | EdgeOne 已内置 Hugo 自动检测 |
| 根目录 | `/` | Hugo 项目根目录 |
| 输出目录 | `./public` | Hugo 默认输出目录 |
| 构建命令 | `hugo --minify --buildFuture` | 与 edgeone.json 中一致 |

> **注意**：如果域名已备案，加速区域建议选择「全球（含中国大陆）」，国内用户访问速度更快。免费套餐每月 500 次构建，个人博客完全够用。

### 6、触发部署并绑定自定义域名

配置完成后，点击「部署」，EdgeOne Pages 会自动：

1. 拉取 GitHub 仓库代码
2. 检测到 Hugo 项目（通过 `hugo.toml` 等配置文件）
3. 安装指定版本的 Hugo Extended
4. 执行构建命令生成静态文件
5. 将构建产物部署到全球边缘节点
   ![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2nPpUyj0EHjHqYKz3aSmqHCuQPlOnaAH4BZOdvF1AMHLqgTTlK024gsjV7icGpooz9LgyQ9P9ic4q91LuVU0j4HqBvkSYSLwSOhQ/640?wx_fmt=png&from=appmsg)

部署成功后，系统会分配一个 `https://<random>.edgeone.app` 的默认域名。你可以在项目设置中绑定自定义域名：

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2neicaAzDhbehkSDfH4uzFRay2ToDb4Efegg7vtfPxjpia8Diat5eaofAUm0r0bsUfJ7KTwTV960Kvc3Zic0B4NaXU3cnFEicunpSLI/640?wx_fmt=png&from=appmsg)

根据提示，到域名 DNS 服务商处添加 CNAME 记录，将子域名指向 EdgeOne Pages 提供的地址即可。

### 7、自动部署流程

绑定完成后，后续的博客更新流程非常简单：

1. 本地编写 Markdown 文章
2. `git push`

   推送到 GitHub
3. EdgeOne Pages 自动检测到代码变更，触发构建部署
4. 边缘节点缓存自动刷新，新内容即时上线

整个过程无需手动操作，实现了完全自动化的 CI/CD 部署。

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2lvWuUr58ZnfibnNgu6tkFttLUPQx91qL7QZ42qqIBgehYLAic3SNNYdsNN8RUYV1kQNibcbkL9vlOlEeq9Us7vf1ruMLc8OZiczlk/640?wx_fmt=png&from=appmsg)

## 四、ESA 加速后的效果

### 1、速度测试对比

我使用 curl 对比测试了接入 ESA 加速前后多个页面的访问速度，每个页面测试 3 次取平均值：

| 页面 | ESA 加速 | GitHub Pages 原始 | 提升幅度 |
| --- | --- | --- | --- |
| 首页 | 0.117s | 0.762s | **84.6%** |
| 分类页 | 0.181s | 0.745s | **75.7%** |
| 标签页 | 0.152s | 0.397s | **61.8%** |
| 文章列表 | 0.180s | 0.472s | **61.9%** |
| 关于页 | 0.144s | 0.374s | **61.5%** |

从测试数据可以看到：

* **首页加载**

  从 0.762s 降到了 0.117s，提升了近 **85%**
* **分类页**

  从 0.745s 降到了 0.181s，提升了 **76%**
* 所有页面的首字节时间（TTFB）都在 **200ms 以内**，基本达到了国内网站的访问水平

### 2、测速工具推荐

如果你想自己测试加速效果，推荐以下测速工具：

**综合性能分析：**

* WebPageTest — 最详细，支持选择全球不同节点，提供瀑布图分析
* GTmetrix — 基于 Lighthouse，给出性能评分和优化建议
* PageSpeed Insights — Google 官方测速工具，核心 Web 指标评分

**国内多节点测速：**

* 卡卡网 — 国内老牌多节点测速
* Web测Ping — 全国节点首次访问和缓存访问测速

**DNS / CDN 检测：**

* What’s My DNS — 全球 DNS 解析对比
* IPIP.net — 全国 Ping 延迟测试

建议使用 WebPageTest 选择国内节点（上海/北京）分别测试两个域名，对比瀑布图可以直观看到 ESA 在 DNS、连接、首字节等各环节的加速效果。

### 3、实际体验总结

接入 ESA 加速后，最直观的感受就是：

* **页面秒开**

  原本需要 0.5~0.8s 才能加载的页面，现在基本在 0.1~0.2s 内完成
* **访问稳定**

  不再出现偶尔打不开的情况，全国各地访问速度一致
* **搜索友好*...