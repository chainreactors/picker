---
title: 告别工具切换内耗！我用AI开发一个桌面化安全工具全栈聚合平台
url: https://mp.weixin.qq.com/s/CrO_MIu2LrZ-ACPMz-YLfA
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:04:03.662106
---

# 告别工具切换内耗！我用AI开发一个桌面化安全工具全栈聚合平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mlsJQIePMtBLwCkzfAEoMUJbHMUZrzXuJx4yqchXBGuTmoBlJcH1IfhrxCKJialIXZ4g3fXUheiaxLCQib1JXoOtFbBZ0w2GFakZpEMt8Q9YME/0?wx_fmt=jpeg)

# 告别工具切换内耗！我用AI开发一个桌面化安全工具全栈聚合平台

原创

Attacker安全
Attacker安全

Attacker安全

![]()

在小说阅读器中沉浸阅读

**20****26**

点赞+关注，分享不迷路！

**Attacker安全**

专注于网络安全技术与工具分享

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtAu7llGmqjl0LqRKZ97yVf0Rfib0GElgkUdqHCVIP6C0N4bvINyib2fj39ezYI2g3QG2II5uO3lTr7Koicmpwiama9gTXnRRSmjIyk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtDiaPtOhcgJCqDEj8eGqGwyDh8rcLicLm4cLPibWariaTfhuTqHbmIpnYTeXwvIry1MdP02lzQHPYzO4cicH7cs8vLgMkibkakZUVtlE/640?wx_fmt=png&from=appmsg)

**2026期待您的关注**

**SHENGMING**

**声明**

本文仅用于技术讨论与学习，利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者及本公众号团队不为此承担任何责任。

***01***

**前言**

*2026·INVITATION*

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtCXtbdYibZOt1ptgQ9AAFh9upp5RNtBFcbKe4uvPFcGnL3YhfwBg4hVrvPOhbeAsxnIPUxibia7Xj4g6K5ukoRHic4ljez6ibWMxUbo/640?wx_fmt=png&from=appmsg)

        2025中旬左右，突然想做一款属于自己的工具，然后慢慢就构思它的功能创意，它的界面，但是理想很美满，现实很骨感，最终还是倒在了如何去开发制作的这条路上。。。慢慢地，时间久了也就遗忘了我还有这个心愿。但是有时晚上失眠的时候，一想不能算了，也就开始接触python，学习脚本，断断续续的，慢慢的有了deepseek，然后又有了Cursor，一切都变了，我的想法有了落地的可能性，从2025年8月份我开始了。如何一步一步的对软件进行构思，其中也参考学习了其他软件工具（感谢各位大佬），我这才有了清晰的思路，确定了软件工具的方向--安全工具集成平台。有了技术辅助，有了思路和方向，一切就那么开始了。

***02*****工具分享**

*2026·INVITATION*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtA54QXticLRRFd1qTpN5LoMh04icibYc8oxGaYviciaAbZVwRgicVXzdevgIkTicgmoHHHx49hZSzodQ7UpSYB1H3gCIrWiccZcDdaSFs0/640?wx_fmt=png&from=appmsg)

## 工具简介

**御界-Attacker安全**是一款桌面化安全集成工具箱（Electron + React），将常用的**资产入口（网址导航）**、**工具链管理（工具仓库）**、**POC 仓库与扫描（Nuclei 模板）**、**应急响应采集与分析**、以及多种**渗透攻防/辅助小工具**整合到统一界面中，帮助安全工程师减少工具切换成本、提升渗透攻防效率。软件启动时会自动拉起本地后端，并使用内置环境（Python/Java/Go/Node 等）提升“开箱即用”的运行体验。

### 配置与数据目录

        打包运行时会在 **exe 所在目录**创建 `Yujie/config`（并复制默认 `config`），用于存放 POC 等配置数据。

---

## 功能总览

* 🛡️**仪表盘**
* 🌐**网址导航**
* 🔧**工具仓库**
* 🎯**POC管理**
* 🚨**应急响应**
* 🛠️**辅助工具**

---

## 仪表盘

入口：侧边栏「仪表盘」

你会看到：

* 网址总数、工具数量、POC 数量统计
* 最近使用（快捷入口）
* 最近活动（可点击跳转工具仓库并定位/高亮）

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtC9rUy0B4b5IiacR2YTSMleYkYsyoHekDjgfcjhohtNibveqGdH1KmBXdQLrqIJA8htCpU5Ieydr6woZKP80j3uP03JFcxEibbkoo/640?wx_fmt=png&from=appmsg)

## 网址导航

入口：侧边栏「网址导航」

核心能力：

* 分类管理（支持子分类、右键改名/删除）
* 链接管理（添加/编辑/删除）
* 全量搜索（名称/URL/描述）
* 自动获取网站信息（标题/描述/icon，优先走后端避免 CORS）
* 一键外部打开链接
* 拖拽调整顺序（页面内）

使用方法（添加链接）：

1. 点击「添加链接」
2. 填写 **URL 标题 / URL / 分类 / 描述**
3. 可点「自动获取」补全标题、描述、图标
4. 保存后点击卡片打开；右上角按钮可编辑/删除

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtDUT9S7LMDMNHickvA5FhpVjtuU4w3EdBUDJhX6VqKZVTIWNmM8HdyqibBsc1MJcicPf2gyMKQOsGR8yGZhibGMrJnoDtIWGqxgNiaw/640?wx_fmt=png&from=appmsg)

## 工具仓库

入口：侧边栏「工具仓库」

目标：把 GUI/命令行工具统一成“可点击运行”的工具卡片。

核心能力：

* 分类目录管理（可改名/删除）
* 工具卡片管理（添加/编辑/删除）
* 支持运行：

+ **GUI 工具**

  ：静默启动（不弹终端）
+ **终端工具**

  ：打开 cmd 并保留窗口输出

* 支持「打开所在位置」

添加工具（推荐流程）：

1. 在工具列表空白处右键（或使用页面入口）打开“添加工具”
2. 填写：

+ **分类**

  ：可输入新分类名（自动创建目录）
+ **路径**

  ：工具所在文件夹或可执行文件位置
+ **命令**

  ：如 `python`、`java` 等；exe 可留空或直接填
+ **参数**

  ：例如 `sqlmap.py -u http://...`
+ **名称/描述/图标**
+ **终端开关**

  ：命令行工具建议开启；GUI 工具建议关闭

3. 保存后点击工具卡片即可运行；右键工具卡片可编辑/删除/打开所在位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtBcLT0IN5MARu8LMN5gCeBmIXtHbbOyOiaXlYWwmj0nSZfQibe0zt5vVSyk3cJpM7PHDTica3GG9KicRiaV3WpFiaGYqMaEElbOJbTks/640?wx_fmt=png&from=appmsg)

## POC管理（POC仓库 + POC扫描）

入口：侧边栏「POC管理」

### POC仓库（管理）

能力：

* 从 `config/POC` 读取 YAML POC 并展示（id/name/severity/tags 等）
* 搜索漏洞名、分页浏览
* 右键单条 POC：**扫描 / 编辑 / 删除**
* 批量勾选后进入扫描视图做批量扫描

导入 POC：

1. 点「导入」
2. 选择 yaml/yml 文件或文件夹（支持多选）
3. 系统会复制到 `config/POC` 并自动解析展示

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtCSsF3jfBKeOZwRQhll4Ct1gAqZ9PI5bUmthyjqgdlGDHuVyh1vkiccLgaCHBLoMXibtdL8n4ELR1hfIlo3LSlqmk2CYXH493364/640?wx_fmt=png&from=appmsg)

### POC扫描

使用步骤：

1. 目标输入框中输入目标（支持多行、空格分隔）
2. 选择要跑的 POC（可从管理视图同步选择；也支持默认全选）
3. 配置参数：并发数/超时（秒）/重试次数
4. 点「开始扫描」

结果解读：

* 状态：`危险 / 安全 / 错误`
* 支持只看“危险”过滤

若提示连接/超时，请降低并发、增大超时或减少目标与模板数量。

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtCvgibMiaOMRdE6klswpEDmScbJV0rHwk1doibXOMn8Ev90PWwcmcUvvtyVhLvb4weweGV2eiaZe1sylYETPjz06FibKb02Zics7w4g8/640?wx_fmt=png&from=appmsg)

## 应急响应

入口：侧边栏「应急响应」

### 模式说明

* **Quick（本机扫描）**

  ：当前机器快速拉取信息并展示
* **Deep（Agent分析）**

  ：面向更深入的分析流程（通常结合采集包/导入数据）
* **Agent**

  ：生成/使用采集工具，在目标机收集数据后回到本机分析

### 覆盖范围（主要围绕这些项）

* 系统信息、补丁信息
* 网络信息（只看威胁/只看外联/关键词搜索）
* 启动项（分组折叠、只看异常）
* 计划任务（只看异常）
* 进程（只看异常）
* 痕迹目录（prefetch / recent / temp）
* 日志（system/application/security；深度/agent 支持关键字搜索与展开行）
* 用户信息

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtBe1gIYmZicha791ppBfKGq9CTFjjUib3ckl8b9AHN6d9bckVibYAKgySib4IyLeBic7D9e3nciajicLd1am46icnwtF1z67RRsglRAJ6k/640?wx_fmt=png&from=appmsg)

### Agent 采集工具（Windows）

项目中包含 Windows 信息收集工具说明：可收集系统、网络、启动项、任务计划、进程、痕迹、日志、用户等，并在桌面生成 zip 包与汇总 json。

注意：部分采集（尤其安全日志）建议使用管理员权限运行。

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtCGibE4yTmfQx0oTBkPVF1icJNSRoFtOWOLfunbz7uQNI1uHMPWbTLXedDia3ibTwtt9mQt0ZaW07OE6yoCGdg3rLxRONcKfslvS40/640?wx_fmt=png&from=appmsg)

## 渗透攻防 / 辅助工具（集成工具页）

说明：这两个菜单复用同一页面，只是展示的工具集合不同：

* **渗透攻防**

  ：端口扫描、Web 指纹识别、目录枚举（dirsearch）、URLFinder、JWT Crack、服务爆破（Hydra）、报告生成器等
* **辅助工具**

  ：编码/解码、默认密码查询、数据提取器

### 编码/解码

粘贴输入 → 选择编码/解码方式 → 一键转换 → 复制结果。

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtBevtZFMHxpK7rzialuLOs3eOpO0BibQ34cBqKGDlBgRPBEhSbQOjr6LzL2bEUxHricYrucYaLzMqnrEJ3u8q5XTibENTgiasg27QWw/640?wx_fmt=png&from=appmsg)

### Hacker语法（Google Dork）

填写关键字段 → 自动生成 dork → 一键复制用于搜索引擎/资产测绘检索。

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtArDFQLoWXSic7Y3f0Y6yhxcu9PBUb1SjrQwfqiaQPC283LRc8lvsmP3VWVmN047icbSt44ibdJhew8UjTk5XwZCUJ3uibNKS4z9lCw/640?wx_fmt=png&from=appmsg)

### 端口扫描（端口探测 + 服务识别）

输入目标与端口范围 → 配置线程/超时 → 开始扫描（可选同步爆破）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtDVdEgdcFlibnudvsjZz1ywrmia3hCaKsHwYQWVxX47LNAODBJXdrtqtibGbmoYVZAZRz8ZfSm4qePYD0VhQcCVnSxdZBNZvXBVnw/640?wx_fmt=png&from=appmsg)

### Web 指纹识别

输入目标 → 运行扫描 → 过滤结果（内置过滤弹窗）→ 导出 CSV 归档。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtA7Dia9UvzD8ibSVicMJlR3ziaTHbyibb5qYLLiamzVCibr2tYCKOSKCqu4FeqKficIpcicSjXsWk0Q5viaItLnjRicCictyM1fCAMHeiaIoppg/640?wx_fmt=png&from=appmsg)

### 目录枚举（Dirsearch）

输入目标 URL → 配置扩展名/线程/状态码过滤/递归 → 开始扫描 → 解析成表格 → 导出 CSV。
![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtDqvtwmzNYBUTbNbqp6eVZDYtJa1aFoHe5eiak7wAMSu2cY8dawBrSVMtmjnibCicz2vE1Ls95mmPpb7CdqcnnbFebJMLjCAiaAiagE/640?wx_fmt=png&from=appmsg)

### URLFinder（URL 查找与提取）

支持单目标与批量模式 → 配置线程/超时/状态码/最大 URL 数等 → 运行并显示进度 → 生成结果文件（支持 json/csv/html）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtCPAkmXFOJftH5moA6HbdOBTQgthia6wQoDnpyhgVN8eJzsUI4iaMylN3QcToH7icvd0p3vmhib38GiaDcE1EO73ibNNuRGOh8cPzI6U/640?wx_fmt=png&from=appmsg)

### JWT Crack（JWT 解码/验证/密钥爆破）

粘贴 JWT → 解码查看 header/payload → 按需配置字典/候选密钥 → 运行爆破并回填 secret。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtAMe2mw7NtXAWwwuy8yl8cdbo2wx2gD0efiaKD0dLDd2mCVNRSsj2AkTzbQyv3HlSu3PoOtFMDEtZaPmiaNvsCibwwnWbjWWMR2S4/640?wx_fmt=png&from=appmsg)

### 默认密码查询

按设备/厂商/关键字搜索 → 查看默认账号密码与说明 → 支持复制。

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtB7iaPGH9j30mk9cUGX9MUEiaTiaJU2N1XbR8XmjKWDjywb0fQHjb8o9tjJj0oUcdu6PyViayjIpNHrLRNc4W5Nuicib5fFIrPDnr0TQ/640?wx_fmt=png&from=appmsg)

### 服务爆破（Hydra）

选择服务与端口 → 输入目标（支持逗号/换行/CIDR）→ 配置并发/超时/策略 → 配置字典 → 爆破 → 导出 CSV。
若频繁出现 “stack smashing”等崩溃提示，建议在 WSL 或原生 Linux 环境运行 Hydra。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtAJDYOfZIeHxcQVzFXUugN66ibwwnqWHUT5QUQOvsw7pbAia6DYtWaWyoKaDbKqcJ7mVVASbxMUCmrR9MUNR6ug25bWrW5KnHVia4/640?wx_fmt=png&from=appmsg)

### 报告生成器（渗透测试报告编写工具）

填写项目基础信息 → 添加漏洞信息（含验证过程与截图）→ 选择模板 → 生成 Word 报告。
目前“制作模板报告”还在待开发。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mlsJQIePMtDs8y9tujpVCbcdE5scMaKmEibPibvJVDjXlQs1Oiac3yLvibfj3JmgTYVbicKsNvnmnOXJDiaJn6FicmTJ5GiaOegCcysJJ8Zgb6EaDaI/640?wx_fmt=png&from=appmsg)

## 核心价值与推荐工作流  （从资产到归档的闭环）

* **日常积累**

  ：网址导航沉淀入口；工具仓库沉淀工具链；POC 仓库沉淀 YAML 模板
* **渗透评估**

  ：端口扫描 → 指纹识别 → 目录枚举 → URLFinder → POC 扫描验证 → 报告生成
* **应急响应**

  ：Quick 快速排查 → Agent 采集 → Deep 深入分析 → 输出处置结论与材料

***03*****下载**

*2026·INVITATION*

![](https://mmbiz.qpic.cn/mmbiz_png/mlsJQIePMtDXFH1fshjTi...