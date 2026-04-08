---
title: 对用于攻击 CrowdStrike EDR 的 0day 漏洞进行逆向工程
url: https://mp.weixin.qq.com/s/Wedx3iYuT8vq7D5Z6RVyVw
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:32:00.242896
---

# 对用于攻击 CrowdStrike EDR 的 0day 漏洞进行逆向工程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnsupIpnt6MbavFSibjE1rqKheYJ7kXUAmOyX833t15DqdWVuTayHN7sd1Uo54Etbmk8TjyvrqMZflXRoW7Imvic6VgOFAx0k3aWY/0?wx_fmt=jpeg)

# 对用于攻击 CrowdStrike EDR 的 0day 漏洞进行逆向工程

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

##

## 驱动及其变种

在这张图片中，我们可以看到该驱动及其多个变种（15+ 个变种）内部代码完全相同。

![driver variants](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBntBGhRgAQuKP0Nrzqw4oUFw9TUIK54jVEib5hBox82jslGdPZe8th7Qpj2UicjcJMuIYa7nvMRebybll4QRPxFHDXrdYM9q2udQQ/640?wx_fmt=jpeg&from=appmsg)

---

## 📌 已识别的驱动（Identified Drivers）

所有这些驱动都由微软签名，签名有效，并且没有被任何机构阻止或吊销。

![drivers signed](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntenr20nvnXTQWYkO9NbTYFauKVIRS99NMMr5Fx61TeBjsoTcAWmTY64NiceG11iahOia5Cb1m685IWZicEmaa1vkQ8c1VALj2ZdFI/640?wx_fmt=jpeg&from=appmsg)

---

## 📌 VirusTotal 检测

当我们将其中一个驱动上传到 VirusTotal 时，可以看到它没有被任何杀毒软件（AV）或 EDR 厂商检测到。

链接：
https://www.virustotal.com/gui/file/6fbaad2f00afaa94723fa7d5bd46e7ea4babb7ce478a8e7229ce7bd4b85e0f51/detection

![vt scan](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBntLWaFZbGF5G0Z9u1y18XQox7Wt9iblnobHKXZoAFpvtzgK45cuVP6zxBQ34RsbIzk68Ij991O55syvtm1RNp1MRtgjBfIqftW8/640?wx_fmt=jpeg&from=appmsg)

---

# 🔍 逆向工程（Reverse Engineering）

现在进入逆向工程部分，我使用 IDA Pro 打开并加载了该驱动。但 IDA Pro 无法反编译驱动中的主函数（DriverEntry）。

这是一个已知问题：当驱动使用非标准栈帧，或者其入口点被混淆时，IDA 往往无法正确反编译。
因此我没有继续纠结 DriverEntry，而是直接跳到 dispatch handler（调度处理函数），因为真正有价值的逻辑在那里。

---

## ❌ DriverEntry 反编译失败

![driverentry fail](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntWaRib8NTUmk02u8JKTUCrzSdMO3UdDyw0EZdWpxicGCtMvx5FOe9dp0MJnCTugXu0u7hqQIVgLEafGtmaJuowb6dXpXofIx83A/640?wx_fmt=jpeg&from=appmsg)

---

## ⚙️ DeviceIoControlHandler

DeviceIoControlHandler 函数虽然被反编译出来了，但代码看起来非常糟糕：

* 使用 CurrentStackLocation 字段的原始偏移
* 子函数没有命名
* 变量名毫无意义

---

### 修复前

![before](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnsaCFAgh6JibPIYjeIpia9Q0l3sIibAtUfibSmqFWp4WdEbaPU7bljic86ibbc400yV0jotlCxw2Eg1EIG30Uo15wfYvkCIpoft91Nhk/640?wx_fmt=jpeg&from=appmsg)

---

### 修复后（类型和命名修正后）

![after](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnssWWWQicoGZGoS7un4OQtiayZwWKjH2qumsXbianHDLiccGfg3XiasvxqucJpBUrr0qd8khcWqzj2OzINzbfesx8Nfhiapibs4VAaKibk/640?wx_fmt=jpeg&from=appmsg)

---

我们可以看到有两个 IOCTL：

* 第一个没有深入分析
* 第二个（0x22E010）会进入一个用于终止进程的函数，我将其命名为 **procKiller**

---

## 🔪 procKiller 函数

打开 procKiller 的反编译代码后，依然非常混乱，需要像之前一样进行修复。

---

### 修复前

![proc before](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnuHTEboKneKyAQ8gjLChZycRO6YADb8nEN2MGo5N2flstAuteBF8DAP4EPEAn5aeZEvUGMcIHzVSm3dHuiaXdzXdmATohPptgA4/640?wx_fmt=jpeg&from=appmsg)

---

### 修复后

![proc after](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnuTxKbbRZAoZIvUqvXyHDAkPQaHLHPRuGgqZFxNnwluAtHViaPLyctDZQ4KsMAubkBcaqpLN10Xjojv7iaicg8VxGRQUMB9ZnG8n4/640?wx_fmt=jpeg&from=appmsg)

---

## 📌 procKiller 函数流程

1. IOCTL 输入缓冲区被当作一个以 null 结尾的 ASCII 字符串，表示十进制 PID
2. 驱动调用 `atoi()` 将其转换为整数
3. 将该整数传递给 `TerminateProcess`
4. 如果成功，则向输出缓冲区写入 `"ok"`

👉 这就是整个接口逻辑，非常简单粗暴

---

## ⚙️ TerminateProcess 内部逻辑

![terminate](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnswWicDmpEsphkzluYg9iaTRbNE415icoTs3oRKkrHn3ic5LzYIOdFRVM84gHP38ibnSpzY2f0uH9o6z7CTRS2vQwwnIWm0GyibCib32E/640?wx_fmt=jpeg&from=appmsg)

该函数执行流程如下：

1. 使用 `ZwOpenProcess` 根据 PID 打开目标进程并获取句柄
2. 使用 `ZwTerminateProcess` 通过该句柄终止进程

---

## ❗ 为什么可以杀死 CrowdStrike

这也解释了为什么 CrowdStrike（以及其他以 PPL 方式运行的 EDR）可以被终止：

* 在用户态：
  调用 OpenProcess 访问 PPL 进程会返回 **Access Denied**
* 在内核态：
  `ZwOpenProcess`**不受该限制**

👉 所以内核驱动可以直接干掉受保护进程

---

## 🔗 符号链接（关键缺失点）

虽然已经找到了终止进程的 IOCTL，但还缺少一个关键组件：

👉 驱动的符号链接（symbolic link）

没有它，就无法从用户态发送 IOCTL 请求。

---

## 🔍 查找符号链接（动态分析）

我采用了动态方法：

* 加载驱动
* 使用 WinObj 观察是否出现新的符号链接

最终成功找到了该驱动的符号链接：

![symlink](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnsFDPacyAricAEJFm3gImN9AicicOIibRgW3Q7aRQFNxPeu3EEcffDcuhhlpJDcYIJa4NfRKNUpDkwMleib5rRhZkVrdic4ibh1YoObeo/640?wx_fmt=jpeg&from=appmsg)

---

## 📌 关键参数总结

驱动符号链接：

```
\\.\{F8284233–48F4–4680-ADDD-F8284233}
```

终止进程 IOCTL：

```
0x22E010
```

---

# 💻 创建 PoC（概念验证）

首先将符号链接和 IOCTL 定义为变量：

![vars](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnsYanX3srEms4wJWvA2BhiaMyGuOquCvEpVPGr7WIC6PaMaSplICRyIheMvrqjTX1UY9yYnN7Q2xIXg5QibKzG3lx2tHrERyJCWs/640?wx_fmt=jpeg&from=appmsg)

---

## 📌 主函数流程

1. 使用 `CreateFileW` 打开设备：

   ```
   \\.\{F8284233–48F4–4680-ADDD-F8284233}
   ```
2. 将 PID 转换为十进制 ASCII 字符串
3. 使用 `DeviceIoControl` 发送 IOCTL（0x22E010）
4. ✅ 进程被终止

---

### main 函数（部分1）

![main1](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnvTOD6G4TxJdtqlpHE4kkuZJAcU235DMBWCkD4Rr1Yb7sVroDgPkwx1bs2mU50cicW6zAtUdAb0sZFFt5Cw8WUCbQS4Lich8cRbU/640?wx_fmt=jpeg&from=appmsg)

---

### main 函数（部分2）

![main2](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnt4P4ATx3xgbfKNarJibRXlvfyERn5KfrR0e5CZt4mZHvQMhUiaRUWc4cAOlm6CTr5Kic0LbVTHl34ImqI6dNgOCf1DDxMI0Y01yA/640?wx_fmt=jpeg&from=appmsg)

---

# 🧪 测试 PoC

## 📥 加载驱动

首先使用 OSRLOADER 加载驱动。

也可以使用 `sc.exe`：

```
sc.exe create PoisonX binPath="C:\Path\to\Driver.sys"type=kernel
sc.exe start PoisonX
```

![loader](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnuG1wr86KJqzoaQ7E7GzOUNXicwPMs3d58VE2dU1le3ic391FzfHTGDFn8PPt46CPDp65QxY4enRKWK2EReGDAZz7jadtGxuRuTg/640?wx_fmt=jpeg&from=appmsg)

---

## ▶️ 运行前

![before poc](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnv9an243GcsibqkLMQm9ZW1ictYmkVkxWRu92TfKM1lsZPLtOLKRzaccPJribibMcmOgBgXrcn9VDWSjs8vO9mOz9oeIPPqicpQic2jI/640?wx_fmt=jpeg&from=appmsg)

---

## 💀 运行后（进程被终止）

![after poc](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsFfHaHuZIPB8JWPXB6q4h8e2t42MAicoPJFhCSLnIyOzgTJ2xAH3KTMyguiaYE2az9cBpMh3hKCQq07FBwRiaQrkqvkTB1ibM2kAo/640?wx_fmt=png&from=appmsg)

---

## 📎 项目地址

PoC 和驱动已发布在 GitHub：
https://github.com/j3h4ck/PoisonKiller/

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx

##

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuCJsTmUzYrdaEIG1lzeOJNXqbZ1260iats4bvYoLowDTAfzFicAPPiaOOIDuP5fkOQmC1dxDq6xJWoibHUBwaNdQdu72Pwk1LFibhs/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsJXRZhRId06dj9NnXJ44a6JqPmtMJtdYyurufSblPXFkQHmJDrWJmKZO7ho5AcicJZlbcQHbvh46jHLqSWYaZarlVn4icqXx08I/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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