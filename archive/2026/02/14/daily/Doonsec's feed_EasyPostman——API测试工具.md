---
title: EasyPostman——API测试工具
url: https://mp.weixin.qq.com/s/1Cgm-li-EDQy2flw4D-1Yw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:16:03.082305
---

# EasyPostman——API测试工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qqiaD4wiajgFzO4hOuAE6TJicls6LBAxQTHELkubexngia06z7oLZias0ic7n6F57mgF6tgWhrLHFG5NOLicrQ1JiawfPIXaOibj4TGcyk7xaDMyIBJk/0?wx_fmt=jpeg)

# EasyPostman——API测试工具

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

## 项目地址：

## https://github.com/lakernote/EasyPostman

## 项目概述

**EasyPostman** 是一款开源的 API 调试与性能测试工具。该项目旨在为开发者提供媲美 Postman 的本地 API 调试体验，同时集成类似 JMeter 的批量请求与压力测试功能 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFy6HWd71mJXUVGUI9dBvZepHiaYl5qUv2xzt66Qq0iaia9QdiauMqqibIibc2hBK0UwG0lfcM2vcUZ4Ec9Lr2hHokAYpkrlwZQTeoVew/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFwlUuPs115e6zTzaOciaBicWiaAlvjhPJUmjCjvEKKTmonW4Iiad2wxIO16IbV1T8XKec6RZXBF5ADgmI1mzvqM8mJjyoibFmmPRNEg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFxqwOQzicJbwLM7wjCdW2WMX9sK7ToibyI9Zpjmtmick4JB62vKnQlhRpOiaX0JwkR28hYpBPXrgOUL0AM2Aj5PeOYco40ToglLsibg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFxqtEELU5LiaYLQDSUiaee02KZhjLrYicoB76wdibLzFczaBBYKF5tqPOuJicjgk1W01yodgdSzLXfFibmwq8bNSDBMc2HsXS9bFkBias/640?wx_fmt=png&from=appmsg)

### 项目定位

* **目标用户**：后端开发者、测试工程师、DevOps 人员
* **核心场景**：API 接口调试、接口性能测试、团队协作
* **设计理念**：简洁而不简单，功能丰富而不臃肿

## 技术架构

### 系统架构图

plain

```
EasyPostman
├── 🎨 UI Layer (用户界面层)
│   ├── Workspace Management (工作区管理)
│   ├── Collections Management (集合管理)
│   ├── Environments Configuration (环境配置)
│   ├── History Records (历史记录)
│   ├── Performance Testing Module (性能测试模块)
│   └── NetworkLog Monitoring (网络日志监控)
│
├── 🔧 Business Layer (业务逻辑层)
│   ├── HTTP Request Engine (HTTP 请求引擎)
│   ├── Workspace Switching & Isolation (工作区切换与隔离)
│   ├── Git Version Control Engine (Git 版本控制引擎)
│   ├── Environment Variable Resolver (环境变量解析器)
│   ├── Script Execution Engine (脚本执行引擎)
│   ├── Data Import/Export Module (数据导入导出模块)
│   └── Performance Test Executor (性能测试执行器)
│
├── 💾 Data Layer (数据持久层)
│   ├── Workspace Storage Management (工作区存储管理)
│   ├── Local File Storage (本地文件存储)
│   ├── Git Repository Management (Git 仓库管理)
│   ├── Configuration Management (配置管理)
│   └── History Management (历史管理)
│
└── 🌐 Network Layer (网络通信层)
    ├── HTTP/HTTPS Client (基于 OkHttp)
    ├── WebSocket Client (WebSocket 客户端)
    ├── SSE Client (Server-Sent Events 客户端)
    └── Git Remote Communication (Git 远程通信)
```

### 技术栈详解

#### 核心技术

表格

| 组件 | 技术选型 | 用途 |
| --- | --- | --- |
| **开发语言** | Java 17 (LTS) | 现代 Java 特性支持 |
| **GUI 框架** | Java Swing | 原生跨平台桌面应用 |
| **UI 主题** | FlatLaf | 现代化外观、暗黑模式、HiDPI 支持 |
| **代码编辑器** | RSyntaxTextArea | JSON/XML/JavaScript 语法高亮 |
| **HTTP 客户端** | OkHttp | 高性能 HTTP/HTTPS 请求 |
| **脚本引擎** | Nashorn / GraalVM | JavaScript 运行时 |
| **打包工具** | jlink + jpackage | 生成原生安装包 |

#### 推荐运行环境

* **JDK**: JetBrains Runtime (JBR) - 针对 Swing 应用优化的 JDK 发行版

+ 更好的 Swing/AWT 渲染性能
+ 改进的字体渲染和 HiDPI 支持
+ 修复了标准 JDK 中的 Swing 相关 Bug

---

## 安装与部署

### 系统要求

表格

| 配置项 | 最低要求 | 推荐配置 |
| --- | --- | --- |
| **Java 版本** | Java 17+ | Java 17 LTS |
| **内存** | 512MB 可用 | 1GB+ 可用 |
| **磁盘空间** | 100MB | 200MB+ |
| **操作系统** | Windows/macOS/Linux | 最新稳定版 |

### 安装方式

#### 方式一：下载预编译安装包（推荐）

表格

| 平台 | 安装包类型 | 文件名格式 |
| --- | --- | --- |
| **macOS (Apple Silicon)** | DMG | `EasyPostman-{version}-macos-arm64.dmg` |
| **macOS (Intel)** | DMG | `EasyPostman-{version}-macos-x86_64.dmg` |
| **Windows** | EXE 安装包 | `EasyPostman-{version}-windows-x64.exe` |
| **Windows (便携版)** | ZIP | `EasyPostman-{version}-windows-x64-portable.zip` |
| **Ubuntu/Debian** | DEB | `easypostman_{version}_amd64.deb` |
| **通用跨平台** | JAR | `easy-postman-{version}.jar` |

**下载地址**：

* GitHub Releases: https://github.com/lakernote/EasyPostman/releases
* Gitee 国内镜像: https://gitee.com/lakernote/easy-postman/releases

#### 方式二：源码编译

bash

```
# 1. 克隆仓库
git clone https://github.com/lakernote/EasyPostman.git
cd EasyPostman

# 或使用 Gitee 镜像（国内更快）
git clone https://gitee.com/lakernote/easy-postman.git

# 2. 编译打包
mvn clean package

# 3. 运行应用
java-jar target/easy-postman-*.jar
```

#### 方式三：生成原生安装包

bash

```
# macOS
chmod +x build/mac.sh
./build/mac.sh

# Windows
build/win.bat
```

### 首次运行注意事项

**Windows 用户**：

* 如遇 SmartScreen 警告，点击"更多信息" → "仍要运行"
* 原因：未购买代码签名证书（开源项目常见情况）

**macOS 用户**：

* 如遇"无法打开"提示，右键应用 → 选择"打开"
* 或在终端执行：`sudo xattr -rd com.apple.quarantine /Applications/EasyPostman.app`

---

## 功能详解

### 工作区管理（Workspace）

EasyPostman 引入**工作区**概念实现项目级数据隔离，支持两种类型：

#### 本地工作区（Local Workspace）

* 适用于个人项目
* 数据完全存储在本地磁盘
* 隐私性最强，无需网络连接

#### Git 工作区（Git Workspace）

* 适用于团队协作
* 支持版本控制和多人协作
* 数据通过 Git 仓库同步

**创建工作区步骤**：

1. 点击左侧 **Workspace** 标签
2. 点击 **+ New** 按钮
3. 选择工作区类型（Local/Git）
4. 配置工作区名称、描述和存储路径
5. Git 工作区需额外配置：

* **Clone from remote**: 输入 Git 仓库 URL 和认证信息
* **Local init**: 创建本地 Git 仓库，后续可关联远程

### API 调试

#### 请求配置

* **URL**: 支持环境变量，如 `{{baseUrl}}/api/users`
* **HTTP 方法**: GET/POST/PUT/DELETE/PATCH/HEAD/OPTIONS
* **请求头**: 可视化编辑，支持常用头部快捷选择
* **查询参数**: Key-Value 形式，支持批量编辑
* **请求体**:

+ Form Data（表单数据）
+ x-www-form-urlencoded
+ JSON（语法高亮、格式化）
+ XML（语法高亮）
+ Binary（二进制文件上传）

#### 高级功能

* **Cookie 管理**: 自动保存/手动编辑
* **文件上传**: 支持拖拽上传
* **文件下载**: 自动识别下载响应
* **请求链**: 支持请求之间的数据传递

### 环境管理

#### 环境变量类型

1. **全局变量**: 跨工作区共享
2. **环境变量**: 特定环境内有效（dev/test/prod）
3. **动态变量**: 内置函数生成

* `{{$timestamp}}`: 当前时间戳
* `{{$randomInt}}`: 随机整数

#### 变量引用语法

plain

```
{{variableName}}              # 基础引用
{{baseUrl}}/api/{{version}}   # 嵌套引用
```

#### 环境切换

* 一键切换不同环境
* 变量自动解析替换
* 支持环境导入/导出

### 5.4 请求历史

* **自动保存**: 所有请求自动记录
* **时间线视图**: 按时间顺序展示请求记录
* **搜索过滤**: 支持按 URL、方法、状态码筛选
* **一键复用**: 从历史记录快速恢复请求

---

## 团队协作与版本控制

### Git 工作流

EasyPostman 深度集成 Git，实现接口数据的版本管理：

#### 团队负责人操作

1. 创建 Git 工作区（Clone 或 Local init）
2. 配置 API 集合和环境变量
3. **Commit**: 提交本地更改
4. **Push**: 推送到远程仓库

#### 团队成员操作

1. 创建 Git 工作区（Clone from remote）
2. **Pull**: 获取最新接口数据
3. 本地修改后 **Commit** + **Push**

#### 日常协作流程

plain

```
开始工作 → Pull 获取最新代码 → 本地修改 → Commit 提交 → Push 推送
```

### 认证方式

Git 工作区支持多种认证方式：

* **用户名/密码**: 基础 HTTP 认证
* **Personal Access Token**: 推荐方式（GitHub/Gitee）
* **SSH Key**: 企业级安全认证

### 冲突处理

* 自动检测文件冲突
* 智能合并策略
* 手动冲突解决界面

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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