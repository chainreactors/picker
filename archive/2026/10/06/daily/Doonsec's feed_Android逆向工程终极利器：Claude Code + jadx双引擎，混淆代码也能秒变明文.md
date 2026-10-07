---
title: Android逆向工程终极利器：Claude Code + jadx双引擎，混淆代码也能秒变明文
url: https://mp.weixin.qq.com/s/1rRlK5troJdplWmg4KpwYg
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:39.810583
---

# Android逆向工程终极利器：Claude Code + jadx双引擎，混淆代码也能秒变明文

# Android逆向工程终极利器：Claude Code + jadx双引擎，混淆代码也能秒变明文

原创

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 功能特性

| 功能 | 说明 |
| --- | --- |
| **多格式反编译** | 支持APK、XAPK、JAR、AAR文件 |
| **双引擎支持** | 使用jadx或Fernflower/Vineflower进行反编译（支持单引擎或并排对比） |
| **API提取** | 自动提取Retrofit端点、OkHttp调用、硬编码URL、身份验证头信息和令牌 |
| **调用链追踪** | 追踪从Activity/Fragment → ViewModel → Repository → HTTP调用的完整流程 |
| **架构分析** | 分析应用结构：清单文件、软件包、架构模式 |
| **混淆处理** | 支持ProGuard/R8混淆代码的导航策略 |

## 环境要求

* Java JDK 17+
* jadx（命令行版本）

## 可选依赖（推荐安装）

* Vineflower 或 Fernflower — 处理复杂Java代码时输出质量更佳
* dex2jar — 使用Fernflower处理APK/DEX- 文件时需要

![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHaRNg9rz7zE7gp74tG0pqic1ULW4JEMtafP6H0RDibELOzIpWoHwpCnww4icIrsrgR2M935nTYY4FX3ouCJtKQUKMffOHSyvu0vM/640?wx_fmt=png&from=appmsg)

## 安装方式

方式一：通过GitHub安装（推荐） 在Claude Code中执行以下命令：

```
/plugin marketplace add SimoneAvogadro/android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill
```

方式二：本地克隆安装

```
git clone https://github.com/SimoneAvogadro/android-reverse-engineering-skill.git
```

然后在Claude Code中执行：

```
/plugin marketplace add /path/to/android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill
```

### 使用方法

1. 斜杠命令（快捷方式）

```
/decompile path/to/app.apk
```

2. 自然语言触发

| 触发短语 |
| --- |
| "反编译此APK" |
| "对这款安卓应用进行逆向工程" |
| "从该应用中提取API端点" |
| "按照LoginActivity的调用流程进行分析" |
| "分析此AAR库" |

3. 独立脚本使用

```
# 检查依赖是否完整
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/check-deps.sh

# 自动安装缺失依赖（支持自动检测操作系统和包管理器）
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/install-dep.sh jadx
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/install-dep.sh vineflower
```

### 反编译操作

```
# 使用jadx反编译APK（默认引擎）
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh app.apk

# 反编译XAPK（自动解压并反编译内部所有APK）
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh app-bundle.xapk

# 使用Fernflower反编译
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh --engine fernflower library.jar

# 双引擎对比模式（带反混淆）
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh --engine both --deobf app.apk
```

### API提取

```
# 查找所有API调用
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/

# 仅提取Retrofit相关调用
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/ --retrofit

# 仅提取URL
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/ --urls
```

### 项目结构

```
android-reverse-engineering-skill/
├── .claude-plugin/
│   └── marketplace.json                    # 插件市场目录
├── plugins/
│   └── android-reverse-engineering/
│       ├── .claude-plugin/
│       │   └── plugin.json                 # 插件清单
│       ├── skills/
│       │   └── android-reverse-engineering/
│       │       ├── SKILL.md                # 核心工作流（5个阶段）
│       │       ├── references/             # 参考文档
│       │       │   ├── setup-guide.md      # 安装指南
│       │       │   ├── jadx-usage.md       # jadx使用说明
│       │       │   ├── fernflower-usage.md # Fernflower使用说明
│       │       │   ├── api-extraction-patterns.md  # API提取模式
│       │       │   └── call-flow-analysis.md       # 调用流程分析
│       │       └── scripts/                # 脚本目录
│       │           ├── check-deps.sh       # 依赖检查
│       │           ├── install-dep.sh      # 依赖安装
│       │           ├── decompile.sh        # 反编译脚本
│       │           └── find-api-calls.sh   # API提取脚本
│       └── commands/
│           └── decompile.md                # /decompile 命令定义
├── LICENSE
└── README.md
```

### 项目地址

```
https://github.com/SimoneAvogadro/android-reverse-engineering-skill
```

## 低价出售安全证书不限于cisp、pte等cnvd、请Vme～建了一个项目群，想进群的请回复进群即可

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

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