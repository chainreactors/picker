---
title: 去掉UkeySoft Screen Recorder 8.0.0 弹窗
url: https://h4ck.org.cn/2024/12/18738
source: obaby@mars
date: 2024-12-09
fetch_date: 2025-10-06T19:35:44.615515
---

# 去掉UkeySoft Screen Recorder 8.0.0 弹窗

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[破解/汇编『Crack/Asm』](https://h4ck.org.cn/cats/crackasm)

# 去掉UkeySoft Screen Recorder 8.0.0 弹窗

2024年12月8日
[48 条评论](https://h4ck.org.cn/2024/12/18738#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/微信图片_20241208095336-rotated.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20241208095336.jpg)

之前屏幕录像和截图一直用的UkeySoft Screen Recorder ，直到换了4k显示器之后发现不好使了，录像的时候直接崩溃。后来换了windows自带的snipping tool。

今天又看了下，最新版成了8.0

奔溃的问题解决了，可以录制，但是两个4k屏幕一起录制还是有问题。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-08-100312.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-08-100312.png)

使用7.0的注册信息，可以完成本地注册，但是重启之后就会提示授权校验错误：

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\GSLLC\21881]
"InitTime"=dword:61250d35
"WorkMode"=dword:00000002
"Registerd"=dword:00000001
"SN"="70807-07524-21881-57632-20916-75753"
"EMail"="root@obaby.org.cn"
"LastTime"="20210825"
```

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/BaiduShurufa_2024-12-8_9-46-49.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/BaiduShurufa_2024-12-8_9-46-49.png)

旧版本的还是32位的可执行文件，新版本已经是64位的了，直接x64dbg载入。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-08-100747.png)](https://h4ck.org.cn/wp-content/uploads/2024/12/Screenshot-2024-12-08-100747.png)

代码没有任何的混淆加密，对所有的CheckSNOnline函数下断点，运行：

启动后会断在下面的地址：

```
0000000000754345                         | E8 962CFFFF                        | call <JMP.&CheckSNOnLine2>                                                   |
000000000075434A                         | 89C3                               | mov ebx,eax                                                                  |
000000000075434C                         | 48:8B45 28                         | mov rax,qword ptr ss:[rbp+28]                                                |
0000000000754350                         | 48:8378 58 00                      | cmp qword ptr ds:[rax+58],0                                                  |
0000000000754355                         | 75 14                              | jne screenrecorderpro.75436B                                                 |
0000000000754357                         | 48:8B45 28                         | mov rax,qword ptr ss:[rbp+28]                                                |
000000000075435B                         | 48:8D48 58                         | lea rcx,qword ptr ds:[rax+58]                                                |
000000000075435F                         | 48:8D15 3E010000                   | lea rdx,qword ptr ds:[7544A4]                                                | 00000000007544A4:L"null"
0000000000754366                         | E8 E5BFCBFF                        | call screenrecorderpro.410350                                                |
000000000075436B                         | 83FB 01                            | cmp ebx,1                                                                    |
000000000075436E                         | 75 25                              | jne screenrecorderpro.754395                                                 |
0000000000754370                         | 48:8B45 28                         | mov rax,qword ptr ss:[rbp+28]                                                |
0000000000754374                         | 48:8985 80000000                   | mov qword ptr ss:[rbp+80],rax                                                |
000000000075437B                         | 48:8D05 BEF5FFFF                   | lea rax,qword ptr ds:[753940]                                                |
0000000000754382                         | 48:8945 78                         | mov qword ptr ss:[rbp+78],rax                                                |
0000000000754386                         | 48:8B4D 28                         | mov rcx,qword ptr ss:[rbp+28]                                                |
000000000075438A                         | 48:8D55 78                         | lea rdx,qword ptr ss:[rbp+78]                                                |
000000000075438E                         | E8 DDE7D5FF                        | call screenrecorderpro.4B2B70                                                |
0000000000754393                         | EB 62                              | jmp screenrecorderpro.7543F7                                                 |
0000000000754395                         | 83FB FF                            | cmp ebx,FFFFFFFF                                                             |
0000000000754398                         | 75 22                              | jne screenrecorderpro.7543BC                                                 |
000000000075439A                         | 48:8B45 28                         | mov rax,qword ptr ss:[rbp+28]                                                |
000000000075439E                         | 48:8945 70                         | mov qword ptr ss:[rbp+70],rax                                                |
00000000007543A2                         | 48:8D05 67F6FFFF                   | lea rax,qword ptr ds:[753A10]                                                | 0000000000753A10:"UVSH冹PH嬱H塎0H荅8"
00000000007543A9                         | 48:8945 68                         | mov qword ptr ss:[rbp+68],rax                                                |
00000000007543AD                         | 48:8B4D 28                         | mov rcx,qword ptr ss:[rbp+28]                                                |
00000000007543B1                         | 48:8D55 68                         | lea rdx,qword ptr ss:[rbp+68]                                                |
00000000007543B5                         | E8 B6E7D5FF                        | call screenrecorderpro.4B2B70                                                |
00000000007543BA                         | EB 3B                              | jmp screenrecorderpro.7543F7                                                 |
00000000007543BC                         | 83FB 02                            | cmp ebx,2                                                                    |
00000000007543BF                         | 75 36                              | jne screenrecorderpro.7543F7                                                 |
00000000007543C1                         | 48:8D8D 8C010000                   | lea rcx,qword ptr ss:[rbp+18C]                                               |
00000000007543C8                         | 48:8D95 88000000                   | lea rdx,qword ptr ss:[rbp+88]                                                |
00000000007543CF                         | E8 EC2BFFFF                        | call <JMP.&CheckSNWhenRegist2>                                               |
00000000007543D4                         | 48:8B4D 28                         | mov rcx,qword ptr ss:[rbp+28]                                                |
00000000007543D8                         | 8941 48                            | mov dword ptr ds:[rcx+48],eax                                                |
```

7.0我修改的verify.dll文件，这里直接修改主程序，将call <JMP.&CheckSNOnLine2>  一行nop掉。

[!...