---
title: PetoBin把EXE转成bin工具思路
url: https://mp.weixin.qq.com/s/DLrrq77xSglEKf-YZWNo_g
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:02:21.607804
---

# PetoBin把EXE转成bin工具思路

# PetoBin把EXE转成bin工具思路

原创

词不达意
词不达意

词不达意安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 工具免杀思路

在实现工具免杀时，我们常常使用petobin类的程序，`如Donut、EXEToShellcode`，将自定义的工具程序转换为.bin(raw shellcode类型)，再自实现加载器去运行工具，实现工具免杀

### tobin

使用ai实现了一个petobin的程序，方便自己使用，而且无开源的明显特征，接下来分享下实现思路。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkiaRBgeKPEfpGVQW4QuAApvY8lL2rwqb212k0EgPY9RBIypyvZVaxXv4XjuJ4ic3DicU3gVGk97uoUpT5qb4PLXc8YDjV7NW7d0p0/640?wx_fmt=png&from=appmsg)
普通 EXE 不能直接复制到内存后运行，因为 Windows 平时会替它完成很多准备工作：分配内存、复制节、修正地址、加载 DLL、填写函数地址，最后才跳到程序入口。tobin 生成的 out.bin，就是把这些准备工作一并打包进去。

### 整体流程

生成的.bin文件结构

```
out.bin
├─ 64 字节 bootstrap       自定位并找到 loader
├─ 192 字节 descriptor     描述各部分位置、大小和校验值
├─ PE loader               在内存中装载 EXE
├─ 可选默认参数
└─ 原始 EXE 文件
```

具体流程

```
输入 EXE
   │
   ▼
检查是不是合法 x64 PE
   │
   ▼
加入 bootstrap + descriptor + loader
   │
   ▼
生成 out.bin
   │
   ▼
普通 RAW loader 从 offset 0 调用
   │
   ▼
bootstrap 找到 PE loader
   │
   ▼
PE loader 在内存中还原并运行 EXE
```

### Builder 拼装器

它把各部分按照 16 字节边界排列，并生成 descriptor。descriptor 记录：

* • 整个 RAW 文件大小；
* • loader 的位置和大小；
* • 参数的位置和大小；
* • 原始 EXE 的位置和大小；
* • EXE 的 ImageBase；
* • SizeOfImage；
* • 入口 RVA；
* • EXE 使用了哪些 PE 功能；
* • 原始 EXE 的 SHA-256；
* • descriptor 自身的 CRC32。
  这样 loader 不需要猜测“EXE 从哪里开始”，只需要读取 descriptor。

### bootstrap 是什么

bootstrap只有 64 字节，可以理解为一个很小的“接力跳板”。
它做的事情是：

1. 1. 通过 RIP 相对寻址找到 out.bin 自身的内存基址。
2. 2. 保存 Windows x64 ABI 要求保护的寄存器。
3. 3. 调整栈对齐并预留 shadow space。
4. 4. 从 descriptor 读取 loader\_offset。
5. 5. 调用真正的 tobin\_loader。
6. 6. loader 返回后恢复寄存器并返回调用者。
   关键技术点是 PIC，也就是位置无关代码。无论 out.bin 被复制到哪个内存地址，它都能找到自己内部的 descriptor 和 loader。

### PE loader 做什么

相当于一个简化版 Windows PE 装载器，执行顺序大致为：

1. 1. 验证 descriptor 的 magic、版本和 CRC32。
2. 2. 计算 payload SHA-256，确认 EXE 没被修改。
3. 3. 再次解析内嵌 PE。
4. 4. 从 PEB 找到已经加载的 kernel32.dll。
5. 5. 从导出表解析所需 Windows API。
6. 6. 使用 VirtualAlloc 分配 SizeOfImage 大小的内存。
7. 7. 复制 PE 头和各个 section。
8. 8. 如果实际地址不同，处理 DIR64 重定位。
9. 9. 加载依赖 DLL，填写 IAT。
10. 10. 初始化安全 cookie 和部分 TLS 数据。
11. 11. 根据节属性设置最终内存权限。
12. 12. 刷新指令缓存。
13. 13. 跳转到 EXE 的 OEP，也就是原始入口点。
    它不会直接静态链接 Windows API。相反，它从 PEB 获取 kernel32.dll，再读取 PE 导出表找到 VirtualAlloc、LoadLibraryA 等函数。这也是 loader 能保持位置无关的重要原因。

### 使用教程

将mimikatz转换为out.bin，简单写个loader去加载执行，正常运行支持go、rust、c/c++程序转换
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkiavibrpGExQpjfiaXNGcULjBibciaOzlqfyH2VJq6kicwmlShqUHicVc3LIa7Aj8uMB32m33F2T0LgfPqtttf2jzxH5nc8ygtwVQ6IDg/640?wx_fmt=png&from=appmsg)

### 纷传介绍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkiaY9Td3qDtDGYGBia0ic3VTxR5tzCPa3wJjK6iaDI6LDEjyuiaqF99sqoBMZkuqn0nRZic4nl7RRsSep6n5iaWG9GqYp5aemDibtqtUrk/640?wx_fmt=png&from=appmsg)

### 圈子往期文件内容如下

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkjpekrj3zibpoZF67jJrQDq0xJgcXKlKYQy2xCQoU7hmADs0XaY5oZqb9DT0rMJJ0uCZCP8icy5GKxVArmJKu0gQf3ibAWGwkpaBw/640?wx_fmt=png&from=appmsg)
群友反馈![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjXShnSicGbFlmeGdC7QsJJ9GVrcGgHmGIhVZcDf1AX9ViaLCZH2AX3BkmMQdCZQbBwfPtibrtRs9AaBN45HmMQ2F83NFuaza1CFs/640?wx_fmt=png&from=appmsg)

* •冲锋马一键生成工具（一键生成免杀loader）
* •lnk文件一键生成工具（一键生成免杀钓鱼lnk文件）
* •bypass内存扫描插件（可绕过火绒、卡巴斯基等杀软内存扫描cs插件）
* •暗涌在线免杀平台（白文件patch免杀loader（分离、单文件）一键生成平台、支持反沙箱）
* •bypass任务计划工具（普通权限可添加、钓鱼快速免杀维权）
* •后渗透工具免杀（petobin，分离加载避免静态落地被秒）
* •BYOVD攻击一键结束赛门铁克进程
* •BinPatch免杀工具过国内主流杀软
* •白影(whiteShadow)自动化白加黑免杀工具v1.0
* •白影(whiteShadow)自动化白加黑免杀工具v2.1
* •Windows恶意软件常见API一览（PDF）
* •Maldev Academy 恶意软件开发完整课程（源码+VM镜像）
* •SplitRun一款exe免杀工具v1.0
* •cs4.5二开过火绒内存扫描
* •binfileBinder文件捆绑工具
* •RPC添加计划任务绕过360核晶
* •RunPack内部版单文件loader免杀1.3
* •VoidShell/VoidShell-fe内部版：x86-64 Linux ELF 加壳混淆工具
* •白影(whiteShadow)自动化白加黑免杀工具v2.4
* •RRR C2 v1.2

### 重要声明

本文所涉及的技术、思路和工具仅用于本地靶场安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担，禁止用于任何非法渗透测试，以及无授权违法测试，请遵守中华人民共和国网络安全法。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fQ2Bdxy1C5nUgyJyyHvl33mCCUsSib26NxViaiamWM5qOT7NAVcjlGAkGlkBYQF4j3dSHMprGM9aRTxjQ7ThqugRQ/0?wx_fmt=png)

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