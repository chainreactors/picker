---
title: 水洞+1，功德+N
url: https://mp.weixin.qq.com/s/EJ-I4et12Va_cLWvQ70rjg
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:13:44.352228
---

# 水洞+1，功德+N

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1v42WSp5tAHPf4icAoRVsqNPExv69PA0rznEicQRG7IYveiaMWMJMHHic0xImA68ibtichhRFcC9nqicob8iaI5cibS7fG8KHQ5P8iaMpYbg/0?wx_fmt=jpeg)

# 水洞+1，功德+N

原创

liudehong
liudehong

十月的进阶之路

![]()

在小说阅读器中沉浸阅读

# 1. 基础知识

### 1.1 什么是 DLL 劫持

**DLL 劫持**是利用 Windows 系统 DLL 默认搜索机制的特性，将恶意 DLL 伪装成程序需要加载的合法 DLL，诱导程序启动时错误加载并执行恶意代码的攻击技术。

攻击原理：利用 Windows DLL 搜索顺序缺陷，诱导程序加载恶意 DLL 而非正版 DLL。

### 1.2 攻击流程

1. **程序启动时**：按固定搜索路径查找依赖的 DLL
2. **攻击者操作**：将同名恶意 DLL 放置到优先级更高的目录
3. **程序行为**：优先加载恶意 DLL 而非正版 DLL

### 1.3 Windows DLL 默认搜索路径（优先级从高到低）

| 优先级 | 路径类型 | 描述 |
| --- | --- | --- |
| 1 | **进程所在的可执行目录** | EXE 文件所在目录，优先级最高 |
| 2 | **系统目录（System32/SysWOW64）** | 系统核心 DLL 存放目录 • 32 位 Windows：`C:\Windows\System32` • 64 位 Windows：`C:\Windows\System32`（64 位 DLL） • 64 位系统运行 32 位程序：`C:\Windows\SysWOW64`（32 位 DLL） |
| 3 | **16 位系统目录** | 兼容旧版 16 位程序的目录 `C:\Windows\System`（极少使用） |
| 4 | **Windows 目录** | `C:\Windows` 存放系统基础组件和通用 DLL |
| 5 | **当前工作目录** | 进程运行时的”当前操作目录” 不等于程序（EXE）所在目录，是操作系统分配的”默认文件夹” 程序如果不指定完整路径，读写文件/加载 DLL 时会优先查找此目录 |
| 6 | **环境变量 PATH 指定的目录** | 优先级最低，包含系统预设和用户自定义的路径 |

### 1.4 劫持的核心操作

#### 1.4.1 伪装恶意 DLL

* 分析目标进程依赖的合法 DLL 名称
* 将恶意 DLL 的文件名修改为合法名称
* 确保文件名完全一致（包括大小写）

#### 1.4.2 放置到高优先级路径

* 将伪装后的恶意 DLL 复制到目标程序的”可执行文件所在目录”
* 利用优先级最高的搜索路径实现劫持

### 1.5 劫持的前提条件

1. **目标程序存在 DLL 依赖**

* 程序必须明确调用某个外部 DLL（静态依赖或动态依赖）
* 才会触发 DLL 搜索流程

2. **未使用绝对路径加载**

* 程序加载 DLL 时只使用文件名，不使用完整路径
* 才会触发系统按搜索路径查找

3. **未进行签名校验**

* 程序未对 DLL 进行数字签名校验
* 无法识别 DLL 是否为官方正版，从而加载恶意 DLL

4. **权限可访问目标目录**

* 具备向目标程序所在目录的写入权限

---

## 2. 案例

### 2.1 目标与准备

**目标**：保障程序正常运行的同时能够弹出计算器。

**准备工作**：

1. 在程序目录下选择一个 DLL 尝试进行修改
2. 检验该 DLL 是否存在完整性校验
3. 建议选择程序自带的 DLL，而不是系统自带的 DLL
4. 本案例选择 `ffmpeg.dll`

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1soN7RID4mBtaIa6csQcC8N6QpnEKBcrG2FXoiaMyoJicVcvhLFqiaKknJzCnSRdpGohW8VOMl478TcNysrQFatkaAKxHeKAibcxNg/640?wx_fmt=png&from=appmsg)

程序目录结构

### 2.2 识别可利用的 DLL

**工具**：使用 ZeroEye 在目标文件夹下挖掘可利用的 DLL 文件

* 带 `+` 号表示存在签名校验
* 不带 `+` 号表示可利用

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1sNmMtpibMDMdenN5VXmAnXgHzRLssc1jjXVw2gFlvzW1J4zJcdFgmotskq0iaSosDiatflLbQicwKVwk6ZnVtGGjqNlajq6uh6RsM/640?wx_fmt=png&from=appmsg)

ZeroEye 工具界面

### 2.3 分析目标 DLL

**工具**：使用 IDA Pro 进行二进制分析

**操作步骤**：

1. 用 IDA Pro 打开目标 DLL
2. 选择视图 → 打开子视图 → 十六进制转储
3. 查看二进制文件的原始十六进制字节数据和对应 ASCII 字符
4. 点击编辑 → 修补程序 → 更改字节
5. 完成修改后，再次点击编辑 → 修补程序 → 应用补丁到输入函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sgF5dwJ3kGosonD5uhe57iaNXWv2Qujc9HFqgvxziblzibMWuS1l6MMjsdKPkeNMrn7f9elA5EOW7dDtxiaia3qYib7QIe7dCsN91qM/640?wx_fmt=png&from=appmsg)

IDA Pro 分析界面

### 2.4 验证完整性校验

**验证方法**：

1. 替换原来的 DLL
2. 运行 EXE 程序查看是否成功
3. 替换后成功运行说明没有完整性校验
4. 此时可以进行 DLL 劫持

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1sua48Qw9wE62h5j955fLRL9LQ5iaegqo6WAIlGg6lTfPvehgDzhqTdXwfxibNLYL8gy9XKR4Bd4XgxibHn09AibTzQDjMnAIc9Gw0/640?wx_fmt=png&from=appmsg)

验证完整性校验

### 2.5 反编译目标 DLL

**工具**：使用 AheadLib 对 `ffmpeg.dll` 进行反编译

**输出**：得到源代码文件

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1s0dAuHgonkicpNqnfF3naCtZFIOGmLm2mNTMZk1rVbjeu3d1eE5FicMrWYqic1oq5ICvqXAT2upicXF7fZHaWibcQibjUqGLLBKibpEs/640?wx_fmt=png&from=appmsg)

AheadLib 反编译界面

### 2.6 创建 Visual Studio 项目

**步骤**：

1. 打开 Visual Studio
2. 使用动态链接库模板创建一个新项目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1u7aHpcHibwwsqaTgiaqPMh1yiajdwhdTfJQJo0xfZT8DEFKl2xWbCqiaR0dgcHmWXBkOooSf0Sl0SyrUic8FxyiaITuSMGXXsAPibMCg/640?wx_fmt=png&from=appmsg)

创建 VS 项目

### 2.7 配置项目文件

**操作**：

1. 新项目在源文件中会生成 `dllmain.cpp` 文件
2. 将之前生成的 `ffmpeg.cpp` 内容复制到 `dllmain.cpp` 中

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1vLVfya1wpwuPuYmCo2Pqa59tISa2xmAjmJla8jIKiaEiaibPoyiaWTrAz92vWOmY3znAhFhGp33p7MJRiaW0eVJtAmwsJibu02iaOpqQ/640?wx_fmt=png&from=appmsg)

复制源代码

### 2.8 添加汇编文件

**步骤**：

1. 将工具生成的 `ffmpeg_jump.asm` 文件复制到 VS 项目目录
2. 在解决方案管理器中右键点击”源文件”
3. 选择”添加” → “现有项”
4. 选择 `ffmpeg_jump.asm` 文件添加

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1szwNWUcdCQBWuQphsrjiboGw6eUPANxyDibpm7E8sgDnccY8PenvKWjqHrl2RpYsRS1QibVNFhzBYDeFapxicqn38hqiboXNDE38xc/640?wx_fmt=png&from=appmsg)

添加汇编文件

### 2.9 配置汇编文件属性

**操作**：

1. 添加完现有项后，根据 `ffmpeg_jump.asm` 内容进行配置
2. 选择此文件，右键点击”属性”进行配置

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1vC3U4HLMp4R4ezBX94C5wR58UMcNByX9fn7noDeqiaSiadnMT5XQ4cAfQ27QvAjECzYJV9jgVHG4NnFvkx5ib7PicC7U7jbHufsMU/640?wx_fmt=png&from=appmsg)

配置汇编文件属性

### 2.10 设置自定义生成工具

**步骤**：

1. 选择应用后，在配置属性中会出现”自定义生成工具”
2. 将 `ffmpeg_jump.asm` 的内容填入相应位置

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tty7RUC1HAgmrPicQNsejVW8j5cZY1KlDeicYZLtrZHllXs9uaCibtc6eiaqO4aP5b1pW5lMibCtTagMDnMrM9TaFj31SGGdYZlrrM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uz6zvvQzOJuNc9GVrbiaPPZSowFIOj052eA2ic7so6uXYkcCDjH6LBHOPsGWAVic5ga0ibGhhmwh43lpEfXsB1atuYicVdKhBbOvu0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1vQa8eIUPBvJPekAqaRIouLHicEFFeEadEe0hM10hMh5V1Kk5gVicyEq5hcibuXSAwP5yUEWghF8OU7A2aW9Yjdes0mCf0mDxcUSE/640?wx_fmt=png&from=appmsg)

### 2.11 修改源代码

**配置完成后，回到 `dllmain.cpp` 中修改代码**：

1. **取消第一个红框代码的注释**
2. **注释掉第二个红框代码**
3. **第三个红框处修改为原始 DLL 修改后的名字**

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1vvQtmQEgwtg1G9uOZibeAq4ZU76Ih0BGCfibJ0UobaDLTXxUtAmlJvQYE3XjzgBMljH9ZwTwdTtA3yBlft6OWbOIGeTKjvysEQ8/640?wx_fmt=png&from=appmsg)

代码修改示意图

### 2.12 关键代码解释`// 让程序优先加载该目录下的恶意文件，动态获取程序当前目录（关键） GetModuleFileName(NULL, tzPath, MAX_PATH); PathRemoveFileSpec(tzPath);`

**作用**：动态获取程序当前目录，确保恶意 DLL 被优先加载。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uMSJEccKnSoGnpibJEyt2bcswOBBq2iaiclBcSbztlibuxlHRjBTgtwRvMZRKn5qv52ViaKNCMAlLqEn2ia1hZNmQ9XBtUUDAfDfibak/640?wx_fmt=png&from=appmsg)

关键代码位置

### 2.13 修改宿主进程名

**同时修改下面的宿主进程名配置**：

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1sN9icYEIvUU31kP2p2thAOwZb3wHIoYmTAk70HbTTpsuiazkDicHXFlOaQDjadsaJY4H2BhuL9JcBXTsL4IbXfZNGMMm4vTkzoaQ/640?wx_fmt=png&from=appmsg)

修改宿主进程名

### 2.14  成功替换

**剩余代码可以借助 AI 辅助完成**。

**完成后的操作**：

1. 将恶意文件伪装成正常 DLL 的同名文件
2. 对原始正常 DLL 完成重命名
3. 借助 DLL 转发机制，在触发计算器弹窗的同时，保障程序原有功能不受影响、正常运行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uE8E2uCtEEiaAQiasWupgIqdXo1ic2erXv3zRNaCf3qMQHZ4cj9oFxETc9dVIF5Wcero2WRbGp5JiaCFHkBNKy1juIhHN1iaolIMaU/640?wx_fmt=png&from=appmsg)

最终效果展示

### 2.15 验证结果

**验证成功条件**：

1. 程序能正常运行
2. 计算器成功弹出
3. 可以正常输入账号
4. 在进程中也能查看到相关进程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uRI4Of2NJCIghYh5UWsKuFozwhXUvzdzeSxQ3aiakX9AJe4zIaPwZ1m0NYuJaAUoHO4IZpdaibibfOsDBj4FRmLeIYPnV8KkSKsA/640?wx_fmt=png&from=appmsg)

验证结果

---

## 3. 总结

DLL 劫持是一种利用 Windows 系统特性的攻击技术，通过伪装恶意 DLL 并放置在高优先级搜索路径中，诱导程序加载并执行恶意代码。成功实施需要满足多个前提条件，包括目标程序存在 DLL 依赖、未使用绝对路径加载、未进行签名校验，以及攻击者具备目录写入权限。

在防御方面，建议：

* 程序加载 DLL 时使用绝对路径
* 对加载的 DLL 进行数字签名校验
* 设置合适的文件权限，防止未授权写入
* 使用安全软件检测异常行为

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

十月的进阶之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

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