---
title: 【全网首发】Windows运行GTA6详细教程
url: https://mp.weixin.qq.com/s/Z5l3Et4DP_wvfFRnoauI-w
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:40:40.615412
---

# 【全网首发】Windows运行GTA6详细教程

# 【全网首发】Windows运行GTA6详细教程

原创

星宇Sec
星宇Sec

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQrStXNV8at4qXGdBazib21LLlPTuvH5rHCnp29zYkn1CAl4BOKsEqav9sdUNanicZJ4cXtMBDXwYoQQiae1icQXrXeL500R4xsj2z0/640?wx_fmt=png&from=appmsg)

# 一、 Xbox版本流出之后

2026年11月，Cyberleek声称放出了一份接近完整的GTA6 Xbox Series构建。最初流传的文件缺少游戏主程序，直到11月23日，Cyberleek才宣布补发该文件。社区随后开始尝试在PC上加载这份主机构建。

这篇教程使用的仓库源自Marvisak的VIctory，整合了多个分支在3D场景渲染、光照、显存管理和着色器翻译方面的改动。使用最新的源码快照，已实测在WSL2中编译出`victory.exe`，随后在Windows中通过账号选择页、进入主菜单并加载游戏。

**配套仓库下载链接在文末。**解压源码后从第三章开始，任选一条编译路线。已经编译好`victory.exe`的读者可以从第四章开始。

## 二、 VItoriaBr怎样在Windows运行主机版

### 2.1 游戏代码与主机服务

**Xbox Series游戏的主程序使用x86-64指令。**支持这些指令的PC处理器能够执行其中的CPU代码，但游戏还依赖Xbox提供的运行时接口。账号、输入、存档、文件访问和内存管理都要经过这些接口。VItoriaBr在自己的进程里加载游戏程序，补上相关接口，再将能够交给Windows处理的调用转交给系统。

### 2.2 游戏画面怎样交给显卡

兼容层要处理图形接口、资源和着色器。VItoriaBr将主机端D3D12.X调用转换为Windows端D3D12操作，并将GFX10着色器翻译成DXIL。显卡驱动再根据着色器、混合模式和其他渲染状态创建管线状态对象（PSO）。

菜单和3D场景会触发不同的渲染工作。初次进入世界时，资源读取、着色器翻译和驱动编译可能同时发生。因此验收分为三个阶段：能否打开游戏窗口、能否通过账号选择进入菜单、能否进场景并操作角色。

### 2.3 两个EXE分别负责什么

`victory.exe`由本文的Rust项目编译生成，负责读取配置并加载游戏。`game_scarlett_master.exe`是本次测试构建里的Xbox游戏主程序，它仍与原有的DLL和资源留在游戏目录。启动命令会把后者的路径传给前者。

![运行架构](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQorhIrDrO2I8pOApjkxZjw6oyQFH6q1mBrS0dtm8iceG5On2bAMYmQ1MvMx4JYmicaD0mZHXF7QibaDukmEehdG9fprAyBBjiczNRQ/640?wx_fmt=webp&from=appmsg)

运行架构

## 三、 安装依赖并编译victory.exe

### 3.1 下载源码并选择路线

下载VItoriaBr源码包，在文件资源管理器里右键解压，再打开解压后的文件夹。有的压缩包外面会多套一层同名目录，继续打开，直到同时看到下面这些文件。

```
VItoriaBr/
  Cargo.toml
  Cargo.lock
  rust-toolchain.toml
  victory.example.toml
  apps/
  crates/
```

这一层叫**项目根目录**。本章的`cargo build`从这里运行。编译兼容层只需要源码和工具链，游戏目录等生成EXE后再配置。

在Windows的「设置 → 系统 → 系统信息」里确认系统类型。本文命令以64位Windows和x64处理器为例。项目需要支持AVX2的CPU，以及支持D3D12、Shader Model 6.6和Mesh Shaders的显卡。磁盘空间要同时容纳源码、构建文件、解压后的游戏和运行缓存。

| 构建路线 | 需要安装的组件 | 命令在哪运行 |
| --- | --- | --- |
| WSL2交叉编译，见3.4节 | Ubuntu、Rust、Cargo、MinGW-w64 | Ubuntu编译，Windows启动 |
| Windows原生编译，见3.5节 | Rust、Cargo、MSVC v143、Windows SDK | Windows编译和启动 |

已经有WSL2 Ubuntu的读者可以沿用本文实测的交叉编译路线。只想使用Windows工具，或电脑已装有MSVC和Windows SDK，可以选原生路线。任选其一即可。

![构建流程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQruZDuYmRwUCrLj1LLD0wRPvQWK5hFZGS9Sg0xSWzUhbu4yzBW3NgcMicQ5GZmrJWD0RNL7iaO1Ym1RpG4kM2FdQOnDyIhFMlmXY/640?wx_fmt=webp&from=appmsg)

构建流程

### 3.2 认识终端与当前目录

从开始菜单搜索「PowerShell」可以打开Windows终端。提示符通常以`PS`开头。进入Ubuntu后，常见的提示符是`用户名@电脑名:~$`。复制代码块里的命令即可，提示符和示例输出都不用输入。安装过程出现错误时，先处理该步再往下执行。

终端总是在一个目录下工作。PowerShell里可以通过`Get-Location`查看当前位置，再用`Get-ChildItem -Name`确认文件。下面是示例路径，执行前换成自己解压源码的位置。

```
Set-Location -LiteralPath 'C:\Projects\VItoriaBr'
Get-Location
Get-ChildItem -Name
```

在Ubuntu里，用`cd`进入目录、用`pwd`查看当前位置、用`ls`查看文件。Windows的`C:\`在WSL里通常对应`/mnt/c/`。源码如果已解压到Ubuntu用户目录，直接用`$HOME`下的实际路径。

```
cd "/mnt/c/Projects/VItoriaBr"
pwd
ls
```

两个环境的文件路径和语法各自独立。全文示例路径都可替换，含空格时保留路径外围的引号。

### 3.3 安装Rust前先看版本和镜像

**Cargo会随Rust工具链安装。**`rustup`管理和下载工具链，`rustc`编译Rust代码，`cargo`负责拉取依赖和构建。本文使用`rust-toolchain.toml`里指定的Rust`1.98.1`。使用其他源码快照时，可以用记事本打开该文件，按`channel`填写对应版本。

慢在不同位置，改的地址也不同。网络正常时，直接跳到所选路线的安装步骤。

| 终端输出或表现 | 负责下载的工具 | 对应配置 |
| --- | --- | --- |
| `downloading component 'rustc'` 或`rust-std` | `rustup` | `RUSTUP_DIST_SERVER` |
| `Updating crates.io index` 或`Downloading crates` | `cargo` | 用户目录下的`config.toml` |
| `apt-get update` 缓慢或连接失败 | Ubuntu的`apt` | Ubuntu软件源 |

#### 3.3.1 更换Rust工具链下载地址

安装或更新Rust工具链之前，在对应终端里设置清华镜像。环境变量在当前终端生效，重开终端后需要重新设置。

```
$env:RUSTUP_DIST_SERVER = 'https://mirrors.tuna.tsinghua.edu.cn/rustup'
```

```
export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup
```

如果镜像尚未同步指定工具链或窗口提示找不到所需组件，清除变量后重新执行安装命令。PowerShell用`Remove-Item Env:RUSTUP_DIST_SERVER`，Ubuntu用`unset RUSTUP_DIST_SERVER`。

#### 3.3.2 更换Cargo依赖下载地址

执行`cargo build`前，在编译所在的环境配置Cargo。Windows和Ubuntu各有自己的配置文件，只改这次用到的那一份。

Windows PowerShell执行以下命令，记事本询问是否创建新文件时点「是」。

```
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cargo" | Out-Null
notepad "$env:USERPROFILE\.cargo\config.toml"
```

Ubuntu可以整段复制下面的命令。首次配置时，它会创建`config.toml`。已有Cargo配置时，命令会显示该目录，便于打开现有文件合并设置。

```
(
  set -eu
  cargo_dir="${CARGO_HOME:-$HOME/.cargo}"
  mkdir -p "$cargo_dir"
if [ -e "$cargo_dir/config.toml" ] || [ -e "$cargo_dir/config" ]; then
    printf'Cargo configuration already exists in %s\n'"$cargo_dir"
else
    set -C
    printf'%s\n' \
      '[source.crates-io]' \
      'replace-with = "tuna"' \
      '' \
      '[source.tuna]' \
      'registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"' \
      > "$cargo_dir/config.toml"
    printf'Saved %s/config.toml\n'"$cargo_dir"
fi
)
```

Windows手动配置或Ubuntu需要合并已有设置时，写入下方内容。已有`[source.crates-io]`时，在原区块中调整`replace-with`。`sparse+`和地址末尾的`/`都要保留。若Windows设置过`CARGO_HOME`，请在该变量指向的目录打开配置文件。

```
[source.crates-io]
replace-with = "tuna"

[source.tuna]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
```

然后在项目根目录执行本路线的构建命令。Cargo下载时若显示`Updating 'tuna' index`，说明正在读取镜像。镜像暂时缺少依赖版本时，撤回刚加的镜像配置后重试，保留源码包附带的`Cargo.lock`。发现同目录还有旧版`config`文件时，查看Cargo的加载提示，在它实际读取的文件里修改。

### 3.4 路线A 在WSL2 Ubuntu中交叉编译

#### 3.4.1 打开Ubuntu

在Windows PowerShell里执行下列命令，查看电脑上已有的Linux发行版。

```
wsl --list --verbose
```

列表中已经有Ubuntu且`VERSION`为`2`时，直接进入。名称如果显示`Ubuntu-24.04`之类的值，就用列表里的完整名称。

```
wsl -d Ubuntu
```

从未安装WSL和Ubuntu的读者，在开始菜单右键PowerShell，选择「以管理员身份运行」，再执行下面的安装命令。按系统提示重启后，从开始菜单打开Ubuntu，按提示设置Linux用户名和密码。之后运行`sudo`时需要输入这份密码。终端输入密码时通常没有星号或字符回显。

```
wsl --install -d Ubuntu
```

进入Ubuntu后执行`uname -m`，本教程的工具链对应`x86_64`。从下文的安装依赖到生成EXE，都在Ubuntu中执行。

#### 3.4.2 安装MinGW-w64和基础工具

`apt-get update`刷新软件包索引，第二条命令下载交叉编译器、链接工具和几个基础工具。它们会安装在Ubuntu里。

```
sudo apt-get update
sudo apt-get install -y ca-certificates curl build-essential file nano \
  gcc-mingw-w64-x86-64-posix binutils-mingw-w64-x86-64
```

运行这两条命令检查安装结果。第一条应输出编译器版本，第二条应输出目标架构`x86_64-w64-mingw32`。

```
x86_64-w64-mingw32-gcc-posix --version
x86_64-w64-mingw32-gcc-posix -dumpmachine
```

#### 3.4.3 一键切换Ubuntu的APT镜像

APT下载慢时，在Ubuntu终端整段复制执行。命令会识别新版的`ubuntu.sources`与旧版的`sources.list`，备份配置，把Ubuntu官方普通仓库地址替换为清华镜像，最后刷新索引。发行版代号、软件包分类和安全更新源沿用原来的配置。

```
(
  set -eu
  source_file=/etc/apt/sources.list.d/ubuntu.sources
if [ ! -f "$source_file" ]; then
    source_file=/etc/apt/sources.list
fi

  archive_url='https?://([[:alnum:]-]+\.)*archive\.ubuntu\.com/ubuntu/?([[:space:]]|$)'
if [ -f "$source_file" ] && grep -Eq "$archive_url""$source_file"; then
    backup="$source_file.$(date +%Y%m%d-%H%M%S).bak"
    sudo cp -a "$source_file""$backup"
    sudo sed -E -i "/^[[:space:]]*#/!s#${archive_url}#https://mirrors.tuna.tsinghua.edu.cn/ubuntu/\2#g""$source_file"
    printf'Backup: %s\n'"$backup"
else
    printf'Using the existing APT sources.\n'
fi
  sudo apt-get update
)
```

索引刷新成功后，回到3.4.2节执行`apt-get install`。换源后需要恢复时，用命令输出的`Backup:`路径覆盖其对应的原文件，再执行一次`sudo apt-get update`。

#### 3.4.4 安装Rust和Cargo

此前没装过`rustup`时，先在Ubuntu中执行下列命令。它从Rust站点下载安装脚本，仅安装工具链管理器，Rust编译器和Cargo在下一条命令中一起下载。

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
  | sh -s -- -y --default-toolchain none
```

执行`source`让当前Ubuntu终端加载Rust工具目录。需要清华镜像的读者，在下载工具链之前按3.3.1节设置Bash环境变量。已经安装`rustup`且能运行的读者可以直接安装指定版本。

```
source "$HOME/.cargo/env"
rustup toolchain install 1.98.1 --profile minimal --target x86_64-pc-windows-gnu
rustc +1.98.1 --version
cargo +1.98.1 --version
rustup target list --installed --toolchain 1.98.1
```

确认`rustc`和`cargo`均显示`1.98.1`，目标列表包含`x86_64-pc-windows-gnu`。前者是编译工具的版本，后者决定这次生成哪种程序。Ubuntu可以运行编译器，编译器最终生成的是64位Windows程序。

#### 3.4.5 设置链接器并生成EXE

按3.2节进入含`Cargo.toml`的源码目录。先运行`command -v x86_64-w64-mingw32-gcc-posix`确认能找到编译器。此前把MinGW-w64工具链单独解包到用户目录的读者，应先把实际的`usr/bin`放进`PATH`，再运行检测。

```
command -v x86_64-w64-mingw32-gcc-posix
```

确认有输出再执行以下设置。第一行让Cargo找到Windows链接器，第二行把构建输出放到Ubuntu用户目录，便于集中查找。

```
export CARGO_TARGET_X86_64_PC_WINDOWS_GNU_LINKER="$(command -v x86_64-w64-mingw32-gcc-posix)"
export CARGO_TARGET_DIR="$HOME/victory-build/target-gnu"
```

下载依赖缓慢时，可在执行构建前按3.3.2节配置Cargo镜像。下面这条是生成程序的命令。`+1.98.1`指定编译器版本，`--target`指定Windows GNU目标，`--release`生成发布版本，`--locked`沿用源码包固定的依赖版本。

```
cargo +1.98.1 build --...