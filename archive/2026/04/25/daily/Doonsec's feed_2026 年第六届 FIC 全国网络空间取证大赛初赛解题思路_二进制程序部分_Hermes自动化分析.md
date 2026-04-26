---
title: 2026 年第六届 FIC 全国网络空间取证大赛初赛解题思路|二进制程序部分|Hermes自动化分析
url: https://mp.weixin.qq.com/s/8Xcap7u_eZo9dyGuakPlDQ
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:57:25.614482
---

# 2026 年第六届 FIC 全国网络空间取证大赛初赛解题思路|二进制程序部分|Hermes自动化分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RPq1g3ib528hEBLM09SY4Efw4q7jwSlqmfHNRB90n9X5gvYhEWAJQhVVreayxrb4SKaDeXeaMibn7wlAOagn9ibsCpGcDPcwX70GQeQDFEQQSo/0?wx_fmt=jpeg)

# 2026 年第六届 FIC 全国网络空间取证大赛初赛解题思路|二进制程序部分|Hermes自动化分析

原创

0xSec笔记本
0xSec笔记本

0xSec笔记本

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 📢 免责声明

本文所述技术仅用于合法授权的安全研究、教学演示及防御机制开发。作者及发布平台不承担因读者误用、滥用本内容所导致的任何法律责任。请严格遵守《中华人民共和国网络安全法》及相关法律法规。

换电脑后没装取证软件，电脑上只装了虚拟机，使用Hermes尝试做了一下今天的FIC初赛题目，自己对逆向基本看不懂，用ai来分析的感觉不要太舒服！！！哈哈哈

> 本文使用 Hermes 自动化取证框架对赛题进行分析，完整还原从 E01 镜像到交易数据提取的全流程。环境：Kali Linux，工具链：Sleuth Kit / exiftool / radare2 / python-openpyxl。

---

# Hermes自动化分析，基本一次性全部得到答案

        检材为一个 E01 格式取证镜像（`检材4-U盘.E01`），考察方向涵盖：镜像解析、PE 文件静态分析、逆向工程、加密解密与数据统计，共五道小题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528gd7xGZqgb6LgVJEoBPFicZL2fIRZ7wAOTWrjtSlKYtbYjsHeLuqrf9346CyAU2PdLheWh2f5vdTsuNXuokBsp8fFWh8cKAEVQA/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528iaEic0GHQ8P1Q2XNI02Qdqz31yDHoZMKWX0icTgVJ8fUibZibsMd9ddbcUQQiaQlUzcYCia15ibcUrP863KBdYs6vicmFXup1zUzjVZYpU/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528jY36o8iaAbAotaNIfnMQJC81kIZch8GSmia3hG6vVwwa8GAlq3G3zwU0mV2WpBdK80pSFKsdhUibUiaS9nvXSHGNhRXJMyxxoweBg/640?wx_fmt=png&from=appmsg)

# Hermes详细版分析流程

---

## 确认检材类型

拿到 `.E01` 文件后，第一步不是直接挂载，而是确认它的镜像格式和基本信息。

### 使用工具

```
1

2

3

file
ewfinfo
command -v
```

### 执行命令

```
1

2

3

file /home/kali/Desktop/检材4-U盘.E01

ewfinfo /home/kali/Desktop/检材4-U盘.E01
```

同时检查后续会用到的工具是否存在：

```
1

2

3

4

5

6

7

8

9

10

11

12

command -v ewfmount
command -v mmls
command -v fsstat
command -v fls
command -v icat
command -v tsk_recover
command -v md5sum
command -v exiftool
command -v r2
command -v rabin2
command -v 7z
command -v python3
```

### 关键结果

`file` 显示：

```
1

EWF/Expert Witness/EnCase image file format
```

`ewfinfo` 显示：

```
1

2

3

4

5

6

File format: FTK Imager
Media size: 57 GiB
Bytes per sector: 512
Number of sectors: 121610240
MD5: d58b8a184cb32af1c4bb3f8b1c3f9131
SHA1: 1f7119dcb3b0384324cb19122b5d5f080ce082b1
```

说明该检材是由 FTK Imager 生成的 E01 取证镜像，对应一个约 57GB 的物理磁盘或 U 盘镜像。

---

## 枚举文件系统，定位关键文件

题目明确提到需要分析 U 盘中的 `SampleVC.exe`，所以接下来需要在镜像中找到这个文件。

### 准备目录

```
1

mkdir -p /home/kali/u4_ewf /home/kali/u4_extract /home/kali/u4_recover /home/kali/u4_vhd_extract
```

### 尝试挂载 E01

```
1

ewfmount /home/kali/Desktop/检材4-U盘.E01 /home/kali/u4_ewf
```

虽然过程中出现了 FUSE 权限提示：

```
1

2

fusermount3: failed to access mountpoint /home/kali/u4_ewf: Permission denied
Unable to fuse mount file system.
```

但目录下仍然生成了 `ewf1`：

```
1

/home/kali/u4_ewf/ewf1
```

因此可以继续使用 Sleuth Kit 对其进行分析。

### 识别文件系统

```
1

fsstat /home/kali/u4_ewf/ewf1
```

关键输出：

```
1

2

3

File System Type: NTFS
Volume Serial Number: 84064D70064D6470
Version: Windows XP
```

说明镜像内部文件系统是 NTFS。

### 枚举文件

```
1

fls -r -p /home/kali/u4_ewf/ewf1
```

发现两个关键文件：

```
1

2

r/r 40-128-3: SampleVC.exe
r/r 39-128-3: vc
```

其中：

* • `SampleVC.exe`：题目要求分析的加密程序
* • `vc`：疑似被加密的数据文件

---

## 导出 SampleVC.exe 和 vc

为了避免直接修改镜像，使用 `icat` 将目标文件导出到工作目录中。

```
1

2

3

icat /home/kali/u4_ewf/ewf1 40 > /home/kali/u4_extract/SampleVC.exe

icat /home/kali/u4_ewf/ewf1 39 > /home/kali/u4_extract/vc
```

---

## 问题一：分析u盘检材，找到其中保存的加密程序SampleVC.exe，请给出该SampleVC.exe 的 MD5 是什么？

### 计算 MD5

```
1

md5sum /home/kali/u4_extract/SampleVC.exe
```

输出结果：

```
1

764789dd9c095d74b6b258cf0f7568b2  /home/kali/u4_extract/SampleVC.exe
```

### 答案

```
1

764789dd9c095d74b6b258cf0f7568b2
```

需要注意的是，题目问的是 `SampleVC.exe` 文件本身的 MD5，不是 E01 镜像的 MD5，也不是分区或磁盘的 MD5。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528jxqTjdHeV60wkGUQibam1VQhwFQ0Ho6qicKeED2tS0VNhheXJEZV7ibtibhnOuBFCuic5XBWmPVHliawfDoqelqA2Wlox5T5VFzQBdM/640?wx_fmt=png&from=appmsg)

---

## 问题二：分析SampleVC.exe，该程序编译的日期可能是什么？

### 查看 PE 元数据

```
1

exiftool /home/kali/u4_extract/SampleVC.exe
```

关键字段：

```
1

2

3

4

5

File Type : Win64 EXE
Machine Type : AMD AMD64
Time Stamp : 2026:04:17 01:53:20-04:00
PE Type : PE32+
Subsystem : Windows GUI
```

### 使用 rabin2 交叉验证

```
1

rabin2 -I /home/kali/u4_extract/SampleVC.exe
```

看到：

```
1

compiled Fri Apr 17 01:53:20 2026
```

### 答案

完整时间可以写为：

```
1

2

3

4

2026-04-17 01:53:20 -04:00

# 北京时间 UTC + 8  05:53:20 + 8:00 = 13:53:20
2026-04-17 13:53:20
```

如果题目只要求日期，则写：

```
1

2026-04-17
```

PE 文件头中的 Time Stamp 通常可以作为程序链接或编译时间的参考依据。虽然该字段理论上可以被伪造，但在这类取证题中，它通常就是标准答案来源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528iafT8GsgibCqnnyak0SC9LpTeku5ByzaxJUicRvTTOwhF7G73PicoovetV1wXicjElcNlLJ6TlKTsV2PnOIBsCiacmPRZgq6b3xWURE/640?wx_fmt=png&from=appmsg)

---

## 问题三： 分析SampleVC.exe，正确的密码是什么？

这一题不能仅靠猜测，需要结合程序逆向和解密验证。

### 先查看字符串

```
1

2

3

strings -a -n 4 /home/kali/u4_extract/SampleVC.exe

strings -a -el /home/kali/u4_extract/SampleVC.exe
```

Unicode 字符串中出现了：

```
1

.vhd
```

这说明程序的输出很可能与 VHD 虚拟磁盘有关。

### 查看导入表

```
1

rabin2 -i /home/kali/u4_extract/SampleVC.exe
```

发现程序导入了虚拟磁盘相关 API：

```
1

2

3

4

OpenVirtualDisk
AttachVirtualDisk
GetVirtualDiskPhysicalPath
DetachVirtualDisk
```

这说明程序可能会把解密结果作为虚拟磁盘处理。

### 使用 r2 分析关键逻辑

```
1

2

3

r2 -q -e bin.relocs.apply=true -c 'aaa; s 0x140002200; pd 260' /home/kali/u4_extract/SampleVC.exe

r2 -q -e bin.relocs.apply=true -c 'aaa; s 0x140001cf0; pd 260' /home/kali/u4_extract/SampleVC.exe
```

逆向过程中看到几个关键条件：

```
1

cmp rcx, 0x10
```

说明密码长度必须是 `0x10`，也就是 16 个字符。

同时还看到类似字符范围判断：

```
1

2

sub ax, 0x20
cmp ax, 0x5e
```

说明密码字符需要位于可打印 ASCII 范围内。

此外，程序还调用了：

```
1

WideCharToMultiByte
```

这说明 GUI 输入框中的 Unicode 密码会被转换成多字节字符串，再参与后续校验或解密。

### 为什么确认密码是 PleaseRunAsAdmin？

最终确认密码为：

```
1

PleaseRunAsAdmin
```

原因有四点：

1. 1. 长度正好 16 个字符；
2. 2. 全部为可打印 ASCII；
3. 3. 使用该密码作为 RC4 key 解密 `vc` 可以得到合法 VHD；
4. 4. 解密后的 VHD 中能够提取出交易记录 Excel 文件，证据链闭环。

### 答案

```
1

PleaseRunAsAdmin
```

---

## 问题四：分析u盘检材，利用SampleVC.exe解密U盘中被加密的文件，解密后的文件的后缀是什么？

### 在 E01 镜像中找到关键文件

先对 U 盘镜像做文件系统枚举，确认其中存在：SampleVC.exe、vc

关键命令

```
1

fls -r -p /home/kali/u4_ewf/ewf1
```

```
1

2

3

4

5

6

- SampleVC.exe
   - vc

# 说明：
   - SampleVC.exe 是解密程序
   - vc 是被加密的数据文件
```

### 导出程序和密文文件

使用 icat 从镜像中导出文件：

```
1

2

icat /home/kali/u4_ewf/ewf1 40 > /home/kali/u4_extract/SampleVC.exe
icat /home/kali/u4_ewf/ewf1 39 > /home/kali/u4_extract/vc
```

```
1

这样后续可以在工作目录中独立分析。
```

### 分析 SampleVC.exe，确认它和 VHD 有关

```
1

先用 strings 和 rabin2 查看程序特征：
```

```
1

2

strings -a -el /home/kali/u4_extract/SampleVC.exe
   rabin2 -i /home/kali/u4_extract/SampleVC.exe
```

关键现象

可以看到：

```
1

2

3

4

5

- .vhd
   - OpenVirtualDisk
   - AttachVirtualDisk
   - GetVirtualDiskPhysicalPath
   - DetachVirtualDisk
```

这说明程序会把解密结果处理成虚拟磁盘格式，也就是 VHD。

但是这一步只能说明“中间产物可能是 .vhd”，还不能直接作为最终答案。

### 用正确密码解密 vc

已通过前面题目确认密码为：PleaseRunAsAdmin，然后使用对应解密逻辑把 vc 解开，输出为：vc.vhd

解密后验证文件类型：

```
1

2

file /home/kali/u4_extract/vc.vhd
7z l /home/kali/u4_extract/vc.vhd
```

关键现象
7z 输出中明确显示：

```
1

Type = VHD
```

并且还能继续看到 VHD 内部存在 NTFS 文件系统，以及其中的真实文件：

```
1

usdt_transaction_ledger_70_records.xlsx
```

这一步非常关键，说明：

```
1

.vhd 不是最终业务文件，它只是承载真实文件的容器
```

### 答案

```
1

.xlsx
```

---

## 问题五：分析u盘检材，找到被加密的交易记录，统计李安弘虚拟币收款地址钱包总收款金额为

解密后的 VHD 中包含交易记录文件：

```
1

usdt_transaction_ledger_70_records.xlsx
```

因此需要先提取 VHD 内容，再统计 Excel 中的交易数据。

### 解压 VHD

```
1

7z x -y -o/home/kali/u4_vhd_extract /home/kali/u4_extract/vc.vhd
```

查看提取结果：

```
1

find /home/kali/u4_vhd_extract -maxdepth 4 -type f | sort
```

发现目标文件：

```
1

/home/kali/u4_vhd_extract/usdt_transaction_ledger_70_records.xlsx
```

### 查看 Excel 表格结构

```
1

2

3

4

5

6

7

8

9

10

11

python3 - <<'PY'
from openpyxl import load_workbook
from pathlib import Path

p = Path('/home/kali/u4_vhd_extract/usdt_transaction_ledger_70_records.xlsx')
wb = load_workbook(p, data_only=True)
ws = wb.active

for row in ws.iter_rows(min_row=1, max_row=15, values_only=True):
    print(row)
PY
```

表头为：

```
1

2

3

4

5

交易时间
发送方地址 (From)
接收方地址 (To)
金额 (USDT)
交易说明
```

在记录中发现核心钱包地址：

```
1

T9yZD7iNUXm3WvCca9W4Xh8K3mNqR5sTkL2wP
```

统计逻辑如下：

* • 当该地址出现在 `To` 字段，且金额为正数时，视为收款；
* • 当该地址出现在 `From` 字段，且金额为负...