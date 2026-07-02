---
title: 使用AI进行自动化APP逆向 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/20999812
source: 博客园 - 渗透测试中心
date: 2026-07-01
fetch_date: 2026-07-02T05:56:58.974775
---

# 使用AI进行自动化APP逆向 - 渗透测试中心

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [使用AI进行自动化APP逆向](https://www.cnblogs.com/backlion/p/20999812 "发布于 2026-07-01 13:28")

### 一、前言

对于安卓逆向传统方法是 脱壳→分析代码→写脚本hook→编写自动化加解密脚本。当前的AI方法是先借助ida mcp+jadx mcp进行分析。再让AI编写frida脚本去hook。通过AI写处加解密脚本，并让AI写出mitmproxy自动化请求重放的脚本。

当前利用**“Trae + MCP + Skills + Unidbg”** 组合构建一个 **AI 驱动的全自动移动安全分析流水线（AI-Powered Mobile Security Pipeline）**。以下是基于你提供的工具链（IDA MCP, Jadx MCP, Frida MCP, Unidbg）构建的一套 **AI 自动化逆向安卓解决方案**。

### 二、**核心架构：AI 逆向流水线 (The Stack)**

这套系统的核心逻辑是让 AI 扮演“总工程师”的角色，指挥不同的工具完成特定任务。

| 阶段 | 工具 | 作用 | MCP 项目参考 |
| --- | --- | --- | --- |
| 1. 静态分析 (Java) | Jadx MCP | 分析调用链，定位关键 Java 函数，寻找 JNI 入口 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) |
| 2. 静态分析 (Native) | IDA MCP | 分析 .so 文件，还原算法逻辑，识别加密/签名特征 | [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) |
| 3. 动态验证 (Runtime) | Frida MCP | Hook Java/Native 层，获取运行时参数（Key, IV, Data） | [1193776794/frida-mcp](https://github.com/1193776794/frida-mcp) |
| 4. 算法还原 (Emulation) | Unidbg | 模拟执行 Native 函数，解决无法直接 Python 化的复杂逻辑 | [zhkl0228/unidbg](https://github.com/zhkl0228/unidbg) |
| 5. 控制中枢 | Trae + Skills | 编写 Python 脚本，整合上述工具的输出，生成最终 API | 你的核心逻辑 |

### 三、**分步实施方案**

#### 1.**第一步：环境搭建 (Setup)**

你需要先将这些开源工具集成到你的本地环境，并注册到 Trae/Claude 中。

1. **安装依赖：**
   * Python >= 3.10
   * IDA Pro 8.3+ (用于 Native 分析)
   * Jadx-GUI (用于 Java 分析)
   * Frida Server (在手机或模拟器上)
   * Android Studio (用于运行 Unidbg)

**配置 MCP Servers：**
需要将三个 MCP 服务器配置到你的 Trae 对应配置文件中：

```
 {
   "mcpServers": {
     "frida-agent": {
       "command": "frida-mcp"
     }
   }
 }
```

```
 {
   "mcpServers": {
     "jadx-mcp-server": {
       "command": "C:\\python3\\python.exe",
       "args": [
         "E:\\mcp\\jadx-mcp-server-6.3\\jadx_mcp_server.py",
         "--jadx-port",
         "8650"
       ]
     }
   }
 }
```

```
 {
   "mcpServers": {
     "ida-pro-mcp": {
       "url": "http://127.0.0.1:13337/mcp"
     }
   }
 }
```

#### 2.**第二步：编写 Trae Skills (核心逻辑)**

这是让 AI 自动化的关键。你需要编写几个自定义的 Skills（Python 脚本），让 AI 能够调用。

**Skill 1: `reverse_engineer_app` (全链路分析技能)**

* **输入：** APK 路径，目标 URL (如 `/api/sign`)
* **AI 动作：**
  1. 调用 **Jadx MCP** (`get_source`, `search_method`) 找到发起请求的 Java 类。
  2. 识别出是 Java 实现还是 JNI (Native) 实现。
  3. 如果是 Native，提取 .so 文件名和函数名。

**Skill 2: `analyze_native_algorithm` (IDA 深度分析技能)**

* **输入：** .so 文件路径，函数名
* **AI 动作：**
  1. 调用 **IDA MCP** (`decompile`, `get_asm`) 获取伪代码。
  2. **Prompt 关键点：** "请分析这段代码，指出哪些是 AES/MD5/RSA，哪些是自定义魔改算法。如果是标准算法，请直接给出 Python 实现；如果是魔改，请标记出关键的 Magic Number。"

**Skill 3: `generate_unidbg_starter` (Unidbg 模拟生成技能)**

* **输入：** .so 文件，函数签名，参数类型
* **AI 动作：**
  1. 基于 Unidbg 模板，自动生成一个 Java 项目代码，用于加载该 .so 并调用该函数。
  2. *原理：* 利用 AI 的代码生成能力，将 IDA 分析出的参数类型（int, char\*, struct）自动转换为 Unidbg 的调用代码。

**Skill 4: `write_mitmproxy_script` (自动化脚本生成技能)**

* **输入：** 算法逻辑（Python 实现或 Unidbg 调用逻辑）
* **AI 动作：**
  1. 生成 `mitmproxy` 脚本。
  2. 实现：抓包 -> 修改 Request -> 调用 Python 算法计算签名 -> 注入 Header -> 发送。

  #### 4.**AI 提示词 (Prompt) 设计**

  为了让这套系统跑起来，你的 System Prompt 需要非常明确地定义工作流。

  "你是一名顶尖的 Android 逆向工程师，拥有 Jadx、IDA Pro、Frida 和 Unidbg 的操作权限。你的任务是帮助用户分析 App 的加签逻辑并生成抓包脚本。

  **工作流规则：**

  1. **侦察阶段：** 使用 Jadx MCP 分析 APK，找到网络请求入口，判断签名是在 Java 层还是 Native (.so) 层。
  2. **分析阶段：**
     + *Java 层：* 直接阅读代码，生成 Python 版本。
     + *Native 层：* 使用 IDA MCP 加载对应的 .so 文件，分析函数逻辑。
  3. **验证阶段：** 使用 Frida MCP Hook 关键函数，打印输入输出，确认算法逻辑。
  4. **还原阶段：**
     + *标准算法：* 使用 Python (pycryptodome) 直接重写。
     + *复杂/魔改算法：* 调用 `generate_unidbg_starter` Skill 生成模拟执行代码。
  5. **交付阶段：** 编写 mitmproxy 脚本，集成上述逻辑，实现一键重放。

### 四、jadx1、jadx安装与配置

1.下载jadx并对其进行安装

<https://github.com/skylot/jadx>

![image-20260403101718434](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132750524-434717675.png)2.配置与项目同级，不需要使用的时候，就把缓存删了

![image-20260403111602454](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132751222-434301966.png)

### 2.jadx-ai-mcp安装与配置

1.下载jadx-ai-mcp和jadx-mcp-server

<https://github.com/zinja-coder/jadx-ai-mcp>

下面两个文件都要下载，一个安装在jadx上，一个是用于启动mcp联动大模型。

![image-20260403111704319](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132751868-625003558.png)

2.安装jadx-ai-mcp插件

![image-20260403112154737](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132752457-1756498853.png)

插件安装成功：

![image-20260403112238918](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132753111-1187085544.png)

查看插件状态：

![image-20260403112321424](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132753698-1825866985.png)

![image-20260403112330122](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132754317-203794620.png)

### 3.jadx-mcp-server安装和配置

当前目录：

![image-20260403112639583](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132754830-768791829.png)

我使用的Python版本3.11.2

![image-20260403112712465](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132755378-690329398.png)

使用pip3对其进行安装：

pip3 install -r requirements.txt

4、trae配置MCP

查看运行`jadx-ai-mcp`的python.exe路径

![image-20260403112915375](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132755871-84227560.png)

添加MCP

```
 {
   "mcpServers": {
     "jadx-mcp-server": {
       "command": "C:\\python3\\python.exe",
       "args": [
         "E:\\mcp\\jadx-mcp-server-6.3\\jadx_mcp_server.py",
         "--jadx-port",
         "8650"
       ]
     }
   }
 }
```

![image-20260403113045475](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132756445-22048034.png)

配置成功

![image-20260403113028282](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132757012-1792480879.png)

MCP默认在 **Builder with MCP**中

![image-20260403113144829](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132757718-520761973.png)

如果有多个MCP，不想混在一起用的话，可以自定义一个智能体

![image-20260403113206269](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132758407-1200248383.png)

### 4、jadx+mcp+trae使用

要正常使用，需要我们新建项目或者选择一个文件夹，并在`@`里选择需要得智能体

![image-20260403113452469](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132759066-1766601565.png)

2.trae打开apk的目录窗口
提示词输入：

借助jadx-mcp工具，分析这个APP的网络通信报文的加解密流程以及分析 AndroidManifest.xml 存在哪些安全风险（进行自动化分析）

### 五、Unidbg

Unidbg是一个基于QEMU的Android Native层模拟框架，能够帮助我们在不依赖实际设备的情况下进行逆向分析。

1.安装Java JDK

在开始之前，需要确保安装了Java JDK，因为Unidbg是用Java编写的。

访问Oracle官网下载适合您操作系统的Java JDK版本。

![image-2026040...