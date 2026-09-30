---
title: 当Claude遇上Metasploit：一句话从Root Shell到域控SYSTEM全流程
url: https://mp.weixin.qq.com/s/Y21NeplNnhF0BX5jbTK58Q
source: Doonsec's feed
date: 2026-09-29
fetch_date: 2026-09-30T07:41:10.366160
---

# 当Claude遇上Metasploit：一句话从Root Shell到域控SYSTEM全流程

# 当Claude遇上Metasploit：一句话从Root Shell到域控SYSTEM全流程

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于潇湘信安
，作者raj

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

专注于网络安全知识、个人实战经验分享！
我的备用号 @Hack分享吧，欢迎关注！

概述

本文记录了一次端到端的智能体渗透测试。Claude Desktop 通过模型上下文协议（MCP）连接到 Metasploit 框架，将纯英文任务转化为真实的攻击操作。助手能够扫描网络、选择并启动漏洞利用模块、管理会话、执行后渗透操作，甚至构建和投递自定义载荷——首先攻陷一台存在漏洞的 Linux 主机，然后横向移动到 Windows 域控制器。Metasploit 负责执行具体工作；权限门控确保每一步攻击操作都由人工掌控；所有操作均针对作者自有的私有隔离实验室环境。

本演练分为三个部分：构建 MCP 桥接、攻陷 Linux 目标、以及横向移动到域控制器。最后以具体的缓解策略和对智能体工具在攻防两端意义的前瞻性总结收尾。

## 引言

模型上下文协议让 Claude Desktop 超越了对话范畴，可以直接调用外部工具。当指向一个 Metasploit MCP 服务器时，助手成为操作者的力量倍增器：它理解简短指令、回忆精确的模块语法、链式执行步骤，并在上下文中报告结果——大大减少了通常拖慢渗透测试的摩擦。

本文完整展示了这一工作流程。操作者无需手动输入 Metasploit 命令，只需发出诸如"scan 192.168.1.8"或"exploit port 21"之类的目标指令，助手便会提出并执行相应的操作。结果是对自然语言接口如何重塑实际安全测试的生动展示。由于这些技术授予了对真实系统的控制权，它们只能在明确授权测试的资产上使用。

---

## 实验环境

本次测试在一个隔离的 192.168.1.0/24 网段中进行，使用 VMware 搭建。一台 Kali Linux 机器作为攻击机，同时托管 Claude Desktop 和 Metasploit 框架。两台靶机完成整个场景：一台故意设置了漏洞的 Metasploitable 2 Linux 主机和一台 Windows Server 2019 活动目录域控制器。各主机及其角色总结如下。![实验环境拓扑图](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNLOl6EvWeZaGD4glNlbYoZe40weznoMvryVPiceUaVJPlibuGfic0R7ASaS0aqJ8Ov1v5Y356qVVO1B8owqGJ9K8tcvFCVicpHTCGg/640?wx_fmt=png&from=appmsg)

实验环境拓扑图

在架构上，Claude Desktop 通过 MCP 桥接与 msfrpcd 通信，Metasploit 通过实验室网段到达目标。此环境中的任何设备均未连接到生产网络。

---

## 构建 Metasploit MCP 桥接

在执行任何攻击操作之前，我们需要将助手连接到 Metasploit。以下步骤将安装桥接、启动框架服务、部署 Claude Desktop 并注册服务器。

### 安装 Metasploit MCP 服务器

我们首先安装桥接，它将 Metasploit 的 RPC 接口暴露为 MCP 工具，如 `run_exploit`、`run_post_module` 和 `list_active_sessions`。

```
sudo apt install metasploitmcp
```

![安装 Metasploit MCP 服务器](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNJHaEibhic0D01Ic1AcjjTIQqicyaic7NMhEVuMahTUeicgzEZ0L4aLnVJqwM2ofhM9icZg8RJNbOkps5BqgnkEJmibJnlYa8QEibHxia30/640?wx_fmt=png&from=appmsg)

安装 Metasploit MCP 服务器

### 启动 PostgreSQL 和 MSF RPC 守护进程

Metasploit 依赖 PostgreSQL，桥接通过 msfrpcd 通信。我们启动数据库，然后启动绑定到 localhost 的 RPC 守护进程；它会自动后台运行并报告一个活跃的 PID。

```
sudo service postgresql start
msfrpcd -P <msf-password> -S -a 127.0.0.1 -p 55553
```

![启动 PostgreSQL 和 MSF RPC 守护进程](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNIa0kXvkXo3cup4ffBtiahia4P2BMzOxTOOGy8fOtLIZwGibkiajiauq6jz3doNRToI1hv6zrNYF4jkr4YicP2VkMiaWfLaveanlicDZaI/640?wx_fmt=png&from=appmsg)

启动 PostgreSQL 和 MSF RPC 守护进程

### 在 Kali Linux 上安装 Claude Desktop

Kali Linux 基于 Debian，因此 amd64 Debian 包适用于标准的 64 位 Intel/AMD Kali 安装。从发布页面的 Assets 部分下载 amd64 .deb 包。

**claude-desktop\_1.21459.0\_amd64.deb**

```
https://github.com/aaddrick/claude-desktop-debian/releases
```

**![下载 Claude Desktop Debian 包](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNISU2joQe1HscUrKKpuPwfeJHOic2wasyJhczbqjgjXtwnofkNyKYYJlVFat1sYWK9MpicTmrDp0t9t8LkQF326gEv1z94VyzKFI/640?wx_fmt=png&from=appmsg)**

下载 Claude Desktop Debian 包

打开终端，进入包含已下载 Debian 包的目录。如果浏览器将文件保存在 Downloads 目录中，运行：

```
cd Downloads
```

使用 dpkg 安装包：

```
sudo dpkg -i claude-desktop-unofficial_1.21459.0-3.2.1_amd64.deb
```

安装过程会解包、配置 Claude Desktop、更新桌面数据库，并设置所需的 chrome-sandbox 权限。安装成功后会返回到终端提示符，不会出现致命错误。

![使用 dpkg 安装 Claude Desktop](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNKIxAX8sJ6ZlqwPbzYtTSeQ34V7rThZyvWRy2IfOGeTtOL2wDKesEcBD4y2zsWZTcOu2zSZBJukUrW8mF1sAnNlQdwsKkaicl0A/640?wx_fmt=png&from=appmsg)

使用 dpkg 安装 Claude Desktop

### 打开 Claude Desktop 设置

启动客户端后，我们打开账户菜单并选择 **Settings** 以进入配置面板。

![打开 Claude Desktop 设置](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNLSu5IMlvLS98XBDYGFBIZQn2ichGzYeqnLicFdp9HeqbnufcIwpsGxHkWUg3H2T88x6Sp6SIeZvicibC1c7anVnQz8IWOcDAVib4u8/640?wx_fmt=png&from=appmsg)

打开 Claude Desktop 设置

### 定位本地 MCP 服务器面板

在设置中，我们打开 **Developer** 标签页以访问本地 MCP 服务器，然后点击 **Edit Config** 打开定义它们的 JSON 文件。

![本地 MCP 服务器面板](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNIGGeedtCpF02kuHNlnKtibME0icbmX65HNkBG6EsCYn1zG3maHQBklI7dnE8CiazPhyM5OiaiasyMnSeGCVPYArscXoZO6TdrxjOCs/640?wx_fmt=png&from=appmsg)

本地 MCP 服务器面板

### 定位配置文件

Edit Config 指向 Claude 配置目录中的 `claude_desktop_config.json`，我们在文本编辑器中打开它。

```
~/.config/Claude/claude_desktop_config.json
```

![配置文件位置](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNKp1FhkZ7qhTiax6oV5HDJmbs820eAhTXlqtmyyzGe6qYDDDb5PsNk3gphbekp7Vre5peajnRvJFhZSLia9OVEuwmpF1WsOaTmAc/640?wx_fmt=png&from=appmsg)

配置文件位置

### 查看默认配置

该文件最初只包含客户端偏好设置——注意其中的 remoteToolsDeviceName "kali"。我们将在此设置旁边添加一个 mcpServers 块。

![查看默认配置](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNIXTvaTBcgSTlibsUyc1q9wAvAb1HmjRZSuYYia0jDmEWwJIKq4FyneRgqICJcqeesqzOibEMLnHN1ubeSSelj5pH9B7p4UR24fZU/640?wx_fmt=png&from=appmsg)

查看默认配置

### 参考 MetasploitMCP 模板

MetasploitMCP 项目页面提供了一个模板 mcpServers 块，指定了命令、参数和 MSF\_PASSWORD 变量，我们根据安装环境进行适配。**Metasploit MCP 配置**

![MetasploitMCP 模板](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNJNVGDsSmqWbV5vwCozzMFtiawN7dKLj3BvGCMGclVx64dwxMZZLbuQ0QRFvf4aohac5t9hE6PUlfCP5CN9U36R678z7IgmibAbk/640?wx_fmt=png&from=appmsg)

MetasploitMCP 模板

### 注册 Metasploit 服务器

我们编辑配置：命令设为 `metasploitmcp`，传输方式为 `stdio`，MSF\_PASSWORD 携带与 msfrpcd 相同的密码。

```
{
  "mcpServers": {
    "metasploit": {
      "command": "metasploitmcp",
      "args": [
        "--transport",
        "stdio"
      ],
      "env": {
        "MSF_PASSWORD": "Ignite@987"
      }
    }
}
}
```

![注册 Metasploit 服务器配置](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNI45jKVfibfasqGGX2s4AGtVIFDqDNxeHPfV22CPDzHBRaFrkP1krn7eBA3xjFQ6HMUiaOo3ibdAonVsLb6LW5WUqnfKy9Qxibia4Xk/640?wx_fmt=png&from=appmsg)

注册 Metasploit 服务器配置

### 确认服务器正在运行

回到设置页面，本地 MCP 服务器面板列出 Metasploit 并显示绿色的 **running** 徽章——桥接已上线，Metasploit 工具现在可供助手使用。

![确认服务器正在运行](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNJOJFftFJDl3QClaW5kGD7fl2CYL88DUVs6icqMZ86bb3Aef5AzaazpRITOVNyEib69LDF0ib0W5bRVKSw1JCpyWVVRcFJVHu71k4/640?wx_fmt=png&from=appmsg)

确认服务器正在运行

---

## 场景一

### 攻陷 Linux 目标

桥接上线后，我们将助手指向 192.168.1.8 的 Metasploitable 2 主机，仅使用自然语言任务从侦察推进到 root shell。

### 指派 Claude 扫描目标

我们发出了一个刻意简短的任务——没有标志，没有模块名。助手必须自行确定方法。

```
scan 192.168.1.8
```

![指派 Claude 扫描目标](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNJPGZ2gOPObw7cBXExalDvGrO5IiaM5AqprRoAYh12MAA4IJwfhz9vw6wZCkUwG4je0NWTvlPzibytcVJ3PJyMVNCnC3MLqqubo0/640?wx_fmt=png&from=appmsg)

指派 Claude 扫描目标

### 初始端口发现

Claude 分析了自身约束——沙箱中没有原始套接字 Nmap——提出了替代方案，通过连接器运行扫描，并返回了首批开放端口：FTP、SSH、Telnet、SMTP、HTTP、SMB、MySQL 和 VNC。![初始端口发现](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNLh5aGIc1O1oH9uibTosL6Kx4BfGk5z6QdG8s1FdgXTBp4MKKov1qMcFUoUurdibPqSr0K1H5zianxQ2mhI2HQUnPq2LuDsJCianbU/640?wx_fmt=png&from=appmsg)

初始端口发现

### 完整端口映射

在被要求进行完整扫描时，助手返回了全部 31 个开放端口，并附带了安全上下文注释——标记了 vsftpd 2.3.4、Samba usermap\_script 漏洞、distccd 远程代码执行、ingreslock 后门和 UnrealIRCd 后门。

```
complete port scan
```

![完整端口映射](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNKSdkV2XZ3uqKLic5dppkJxzfgmfT3ZlW2Ql3j8vrCotibgXRjiaTuxPDvw2lJEEUue0as4vXr9po4M44VQWY7ycfByHbXxicK9M4k/640?wx_fmt=png&from=appmsg)

完整端口映射

### 利用 vsftpd 后门

我们从观察转向行动。Claude 将请求映射到 `unix/ftp/vsftpd_234_backdoor` 模块，设置 RHOSTS，并请求 `run_exploit`。权限门控暂停了执行，直到人工明确批准。

```
exploit port 21
```

![利用 vsftpd 后门](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNLbu4ib6MY5lWcahO1D63A5JFbvvXYSe5m4yyMz4pI0IoRxrcC16nMeGU4icsjjgyIXzFsibyeyxWCYzsR7VujPkaphIrJL48ryqY/640?wx_fmt=png&from=appmsg)

利用 vsftpd 后门

### 获取 Root Shell

批准后，后门触发，一个 Meterpreter 会话以 root 身份在 metasploitable.localdomain 上打开，从 192.168.1.17 的 Kali 隧道连接。![获取 Root Shell](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNIz7bAQ0RSxOJgxGvBu91088jWrAnJxKIbZyaPibtaAcjP4W5NqMWbFEUNKQrMSwgEz8fMyA6MSZuYg7ZVibRQZNgEribHmMKpdiaw/640?wx_fmt=png&from=appmsg)

获取 Root Shell

### 列出活动会话

我们确认了立足点。`list_active_sessions` 工具报告了一个活跃的 root Meterpreter 会话，可用于后渗透操作。

```
list_active_sessions
```

![列出活动会话](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNLkq77rSS7jnO6L0RtdjwScmNBnhrAT079tUHG5qYWN8HV9PA6b6EkIRDMQ6WOOxJPpFQOew8L2SwwGkCniaic6rsngN5UP8Pu3o/640?wx_fmt=png&from=appmsg)

列出活动会话

### 后渗透：枚举 SMB 共享

Claude 运行了一个 SMB 辅助模块，正确地将 `smb_enumshares` 识别为辅助模块而非后渗透模块，并返回了共享列表——包括一个全局可写的 tmp 共享——同时指出 Samba 3.0.20 存在 usermap\_script 漏洞（CVE-2007-2447）。

```
run_post_module scanner/smb/smb_enumshares
```

![枚举 SMB 共享](https://mmbiz.qp...