---
title: 加密流量、内存密钥与文件重组
url: https://lucifer11.xyz/knowledge/forensics/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:54.027977
---

# 加密流量、内存密钥与文件重组

![0xfd's blog](/images/fifteen-katana-zero-katana-zero.gif)
[0xfd's blog](/)

by 0xfd

* [首页](/)
* [知识库](/knowledge/)
* [导读](/guide/)
* [分类](/categories/)
* [标签](/tags/)
* [归档](/archives/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [分析重点](#%E5%88%86%E6%9E%90%E9%87%8D%E7%82%B9)
2. [案例与技术索引](#%E6%A1%88%E4%BE%8B%E4%B8%8E%E6%8A%80%E6%9C%AF%E7%B4%A2%E5%BC%95)
3. [内存密钥与 Beacon 流量解析](#%E5%86%85%E5%AD%98%E5%AF%86%E9%92%A5%E4%B8%8E-Beacon-%E6%B5%81%E9%87%8F%E8%A7%A3%E6%9E%90)
4. [文件重组与 WinRM 解密](#%E6%96%87%E4%BB%B6%E9%87%8D%E7%BB%84%E4%B8%8E-WinRM-%E8%A7%A3%E5%AF%86)
5. [Meterpreter TLV 与破损 RSA 材料](#Meterpreter-TLV-%E4%B8%8E%E7%A0%B4%E6%8D%9F-RSA-%E6%9D%90%E6%96%99)

![253](/images/fifteen-katana-zero-katana-zero.gif)

253

漏洞分析、利用机制、二进制研究与安全工程

[83
日志](/archives/)

[65
分类](/categories/)

[312
标签](/tags/)

GitHub

E-Mail

Twitter

FB Page

YouTube

Instagram

infosec.exchange

![Creative Commons](https://cdnjs.cloudflare.com/ajax/libs/creativecommons-vocabulary/2020.11.3/assets/license_badges/big/by_nc_sa.svg)

0%

链接

* atsud0
* 记忆里的纯真
* 小离

# 加密流量、内存密钥与文件重组

发表于
2026-11-25

分类于

[协议与取证](/categories/%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%8F%96%E8%AF%81/)
，
[流量与内存](/categories/%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%8F%96%E8%AF%81/%E6%B5%81%E9%87%8F%E4%B8%8E%E5%86%85%E5%AD%98/)

阅读次数：

本文字数：
15k

阅读时长 ≈
54 分钟

流量解密依赖包结构、会话状态和可验证的密钥材料。本章保留 Cobalt Strike、WinRM 与 Meterpreter 的原解析脚本，把提取、解密、导出和最终文件对应起来。

流量解密依赖包结构、会话状态和可验证的密钥材料。本章保留 Cobalt Strike、WinRM 与 Meterpreter 的原解析脚本，把提取、解密、导出和最终文件对应起来。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/forensics/source.md)
展开全部技术记录

## 分析重点

Beacon 的 AES/HMAC 密钥通过 callback 验证，Meterpreter 另有 XOR 头和 TLV 结构。

WinRM 案例从多个 TCP 流重组账户材料，并记录 pyshark 字段兼容问题。

Response 的残缺 RSA 文件需要同时处理 Base64 对齐、整数参数与最终私钥验证。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [内存密钥与 Beacon 流量解析](#case-decrypt-cs-traffic) | decrypt-cs-traffic | PCAP、Cobalt Strike、AES、HMAC |
| [文件重组与 WinRM 解密](#case-decrypt-winrm-traffic) | decrypt-winrm-traffic | WinRM、PCAP、NTLM、取证 |
| [Meterpreter TLV 与破损 RSA 材料](#case-msf-meterpreter-traffic-decrypt) | msf-meterpreter-traffic-decrypt | Meterpreter、TLV、AES、RSA |

## 内存密钥与 Beacon 流量解析

原挑战将 PCAP 和进程内存对应起来，通过 callback 验证 AES 与 HMAC 密钥。后续保留解密、文件导出和会话证据。

来源 decrypt-cs-traffic · 原记录 2022-01-05 · 8 个代码块 · 6 处图片引用

查看分析过程、攻击步骤与完整代码

#### 介绍

本文记录 Hack The Box 取证挑战《Strike Back》的解题过程。

#### 分析pcap流量包和freesteam.dmp文件

使用Wireshark打开capture.pcap文件，发现第4到第10个数据包是freesteam.exe通过HTTP协议被下载到受害者机器上，然后按顺序点击File > Export Objects > HTTP，会打开一个窗口让我们轻松的将freesteam.exe文件从capture.pcap数据包中提取出来。

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/decrypt-cs-traffic.png)

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ┌──(root💀kali)-[~/hackthebox/challenge/forensics/Strike_Back] └─# file freesteam.exe freesteam.exe: PE32 executable (GUI) Intel 80386 (stripped to external PDB), for MS Windows ``` |

将freesteam.exe上传到VirusTotal在线网站上，显示它是Cobalt Strike的木马程序

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/decrypt-cs-traffic1.png)

pcap中有很多的HTTP流量，但被加密了，所以现在转移到.dmp文件了。如果使用file命令，可以看到这是一个MiniDuMP崩溃dump。

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ┌──(root💀kali)-[~/hackthebox/challenge/forensics/Strike_Back] └─# file freesteam.dmp freesteam.dmp: Mini DuMP crash report, 17 streams, Fri Nov 19 20:45:38 2021, 0x469925 type ``` |

通过使用radare2分析，可以确定这是一个freesteam.exe进程的dump。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` ┌──(root💀kali)-[~/hackthebox/challenge/forensics/Strike_Back] └─# r2 freesteam.dmp [WARN] Invalid or unsupported enumeration encountered 21 [WARN] Invalid or unsupported enumeration encountered 22 [INFO] Parsing data sections for large dumps can take time, please be patient (but if strings ain't your thing try with -z)! [0x02dd0000]> iSq~exe 0x400000 0x409000 ---- C:\Users\npatrick\Downloads\freesteam.exe 0x400000 0x409000 ---- C:\Users\npatrick\Downloads\freesteam.exe ``` |

通过搜索”Cobalt Strike memory dump”的变化，可以看到，它可能从freesteam.dmp的流量派生一个解密key，然后将该key应用到pcap文件。

#### 解密cs流量

从dump中提取密钥的方法会因cobalt strike beacon的版本而有所不同。在版本3中，key的前面是一组元数据字符串，除了false positives外，可以很容易提取。这种方法在这个例子中无效，所以假设这个example来自版本4。在本example中，提供了加密的callback，并且可以使用Didier Stevens编写的脚本来测试dump中针对该callback的所有可能的key。一旦成功，它将打印key，然后就可以解密流量了。Stevens的这篇blog详细介绍了这种方法：

* Quickpost: Decrypting Cobalt Strike Traffic

从76号数据包得到了加密callback, POST /submit.php?id=1909272864 HTTP/1.1。然后使用memory dump提取AES和HMAC key:

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/decrypt-cs-traffic2.png)

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 00000040317639faf73648274ba8a66d11182283f7fa26fe44b3982a36d80f6ffba4949e5ec759fffb372775d2ac002425547a11ddf2e05c2cb914e09ac033f01db0b60c ``` |

解密脚本github地址:

* Beta

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` ┌──(root💀kali)-[~/hackthebox/challenge/forensics/Strike_Back] └─# python3 /root/Beta/cs-extract-key.py -c 00000040317639faf73648274ba8a66d11182283f7fa26fe44b3982a36d80f6ffba4949e5ec759fffb372775d2ac002425547a11ddf2e05c2cb914e09ac033f01db0b60c freesteam.dmp File: freesteam.dmp Searching for AES and HMAC keys Searching after sha256\x00 string (0x4048a) AES key position: 0x00447f81 AES Key:  3ae7f995a2392c86e3fa8b6fbc3d953a HMAC key position: 0x0044b2a1 HMAC Key: bf2d35c0e9b64bc46e6d513c1d0f6ffe SHA256 raw key: bf2d35c0e9b64bc46e6d513c1d0f6ffe:3ae7f995a2392c86e3fa8b6fbc3d953a Searching for raw key Searching after sha256\x00 string (0x441a49) AES key position: 0x00447f81 AES Key:  3ae7f995a2392c86e3fa8b6fbc3d953a HMAC key position: 0x0044b2a1 HMAC Key: bf2d35c0e9b64bc46e6d513c1d0f6ffe Searching for raw key ``` |

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/decrypt-cs-traffic3.png)

为了解密实际的pcap数据包，必须使用HMAC和AES key与另一个脚本，以获得以下结果:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 ``` | ``` ┌──(root💀kali)-[~/hackthebox/challenge/forensics/Strike_Back] └─# python3 /root/Beta/cs-parse-http-traffic.py -k bf2d35c0e9b64bc46e6d513c1d0f6ffe:3ae7f995a2392c86e3fa8b6fbc3d953a capture.pcap -e  Packet number: 12 HTTP response (for request 7 GET) Length raw data: 14336 HMAC signature invalid Packet number: 47 HTTP response (for request 23 GET) Length raw data: 206401 HMAC signature invalid Packet number: 69 HTTP response (for request 66 GET) Length raw data: 48 Timestamp: 1637354721 20211119-204521 Data size: 8 Command: 27 GETUID  Arguments length: 0  Packet number: 76 HTTP request POST http://192.168.1.9/submit.php?id=1909272864 Length raw data: 68 Counter: 2 Callback: 16 BEACON_GETUID b'WS02\\npatrick (admin)'  Packet number: 101 HTTP response (for request 86 GET) Length raw data: 87648 Timestamp: 1637354781 20211...