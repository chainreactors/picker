---
title: 第四届黄河流域公安院校电子物证个人赛程序逆向分析
url: https://mp.weixin.qq.com/s/oY1KBxskepgWKGL0HVv1TA
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T05:00:36.351344
---

# 第四届黄河流域公安院校电子物证个人赛程序逆向分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A8DiammjC4XA73Phib5ibKDhDTtK30cC4Q3ic5TSnGl4tqyXVhRVQiah6HIAF7XNopsQ8P5gwxe4TVITzgawNEf72wZFKoXFBaq6ZcCvzEibLFGm8/0?wx_fmt=jpeg)

# 第四届黄河流域公安院校电子物证个人赛程序逆向分析

怪叔叔
怪叔叔

取证与溯源

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 🏆 2026第四届黄河流域公安院校电子物证个人赛 — 程序逆向分析 Writeup

---

💡 **报告元数据**

* **首席取证官**：`yagami`
* **任务目录**：`/mnt/d/文档/hermes-work/2026黄河流域-程序逆向分析/`
* **生成时间**：2026-08-04
* **生成模式**：完整型取证交付 Writeup

---

## 🛠️ 工具链与环境底座

### 1. 算力与架构

| 组件分类 | 部署详情 |
| --- | --- |
| **自动化编排** | Hermes Agent |
| **基座大模型** | `Qwen3.6-27B-Uncensored-HauhauCS-Aggressive-Q6_K_P` |
| **运行架构** | 本地 (WSL / Windows Subsystem for Linux) |

### 2. 任务信息

* **考核范围**：程序逆向分析（APK静态分析 + PE二进制分析），共10题
* **检材来源**：`/mnt/z/2026第四届黄河流域公安院校电子物证个人赛检材/3.第三部分：程序逆向分析/`
* **检材内容**：TuoxinTask-v3.2.1.zip（内含APK）、HuangHe2026.zip（内含PE）
* **动态状态**：Q1-Q10 全部已验证，全量收敛
* **质控策略**：L1-L3多级验证，Java↔native交叉验证，本地Python解密双向验证

---

## 📊 考题最终答案汇总看板

| 题号 | 核心考点 | 权威标准答案 | 状态 | 等级 | 核心证据链检索摘要 |
| --- | --- | --- | --- | --- | --- |
| Q1 | APK包名提取 | `com.tuoxin.task` | 🟢 已验证 | L1 | AndroidManifest.xml package字段直接确认 |
| Q2 | 通讯录窃取写入文件 | `contacts_bak.json` | 🟢 已验证 | L1 | DataUploadService.a()方法openFileOutput参数硬编码 |
| Q3 | cfg.bin加密方式(多选) | `BCF` | 🟢 已验证 | L2 | Base64编码+AES-256-CBC+IV来自独立iv.bin，三源交叉 |
| Q4 | cfg.bin解密key | `47f32b6c3c50f7474f3a14787ef790f46d326e7a33a758d0c7e452cb120e0700` | 🟢 已验证 | L3 | HARD\_KEY hex = SHA-256(key source)，Java↔native交叉+本地解密双向验证 |
| Q5 | cfg.bin备份IP及端口 | `121.43.187.92:8080` | 🟢 已验证 | L2 | cfg.bin解密后JSON中sdk\_backup\_server字段 |
| Q6 | PE编译器识别 | `B` (Borland Delphi 6) | 🟢 已验证 | L2 | Borland\Delphi\RTL字符串+Delphi单元引用+名称修饰+oleaut32 BSTR函数，多特征交叉 |
| Q7 | PE节区数量 | `8` | 🟢 已验证 | L1 | PE头NumberOfSections=8，IDA确认8个节区 |
| Q8 | PE入口点VA | `0x492040` | 🟢 已验证 | L1 | ImageBase(0x400000)+RVA(0x92040)=0x492040，IDA交叉确认 |
| Q9 | 注册表值名 | `Start` | 🟢 已验证 | L1 | IDA字符串搜索ControlSet\Services\UsbStor，值名Start |
| Q10 | PE主要功能 | `D` | 🟢 已验证 | L2 | UsbStor+Start+.inf.disabled+MoveFileA+MessageBoxA，USB启用/禁用工具 |

---

## ⚔️ 深度取证与解题全链路复盘

### 🧩 Q1 — 刷单APP包名

* **标准答案**：`com.tuoxin.task`
* **状态等级**：🟢 已验证 / **L1**
* **解题主线**： 使用jadx MCP直接读取AndroidManifest.xml，提取package属性值。APK反编译后manifest文件中的package字段即为应用包名。
* **💡 关键证据**：

* 证据编号：FINDING-Q1-001, CMD-20260804-002
* AndroidManifest.xml中 `package="com.tuoxin.task"`，versionName="3.2.1"，application name="com.tuoxin.task.app.TxApplication"

* **🛠️ 核心命令**：

```
ounter(lineounter(line# jadx MCP读取AndroidManifestmcp_jadx_get_android_manifest()
```

* **📋 控制台回显**：

```
ounter(linepackage="com.tuoxin.task", versionName="3.2.1", application name="com.tuoxin.task.app.TxApplication"
```

* **验证闭环**：AndroidManifest.xml是唯一权威来源，package字段直接确认。

---

### 🧩 Q2 — 通讯录数据写入的JSON文件

* **标准答案**：`contacts_bak.json`
* **状态等级**：🟢 已验证 / **L1**
* **解题主线**： 使用jadx MCP搜索ContactsContract关键字定位通讯录读取点→找到DataUploadService类→分析a()方法完整数据流：从ContactsContract.CommonDataKinds.Phone读取通讯录→经ag0.xorFallback XOR加密→Base64编码→写入本地文件。文件名在openFileOutput()参数中硬编码为"contacts\_bak.json"，位于getFilesDir()目录下。
* **💡 关键证据**：

* 证据编号：FINDING-Q2-001, CMD-20260804-003
* DataUploadService.a()方法完整链路：ContactsContract读取→XOR加密→Base64编码→openFileOutput("contacts\_bak.json")

* **🛠️ 核心命令**：

```
ounter(lineounter(line# jadx MCP获取DataUploadService类源码mcp_jadx_get_class_source(class_name="DataUploadService")
```

* **📋 控制台回显**：

```
ounter(line方法a()读取通讯录ContactsContract.CommonDataKinds.Phone，写入文件 "contacts_bak.json"
```

* **验证闭环**：类源码中openFileOutput参数直接指定文件名，无歧义。

---

### 🧩 Q3 — cfg.bin加密方式(多选)

* **标准答案**：`BCF`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**： 分析assets/cfg.bin文件的多层处理流程：

1. **编码层**：cfg.bin文件内容为Base64编码文本（B正确，排除A的Base32）
2. **解码后结构**：Base64解码后前8字节为header("TX-WEB\0\x01\x00")，bytes[8:24]为IV(全0)，byte24起为加密数据
3. **加密算法**：AES-256-CBC（C正确，排除D的AES-512-CBC），key由SHA-256派生(32字节)
4. **IV来源陷阱**：Java代码中System.arraycopy(bArrDecode, 8, new byte[16], 0, 16)创建临时数组即丢弃，实际IV由native层从独立文件assets/iv.bin读取（16字节，9f4a2c18e6b7d053f8c1aa90d33b44e1）→ F正确，排除E

* **💡 关键证据**：

* 证据编号：FINDING-Q3-001, CMD-20260804-004/005/006
* cfg.bin为Base64编码，解码后744字节
* AES-256-CBC加密，key由SHA-256派生
* IV实际来源：assets/iv.bin（独立文件），非cfg.bin自身

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(line# jadx MCP分析decryptConfig类mcp_jadx_get_class_source(class_name="a.ih")# jadx MCP分析deriveKey方法mcp_jadx_get_class_source(class_name="a.ag0")# 提取并解密cfg.bin# Python: Base64解码→IV从iv.bin读取→AES-256-CBC解密→JSON解析
```

* **📋 控制台回显**：

```
ounter(lineBase64解码后744字节，IV从assets/iv.bin读取(9f4a2c18e6b7d053f8c1aa90d33b44e1)，AES-256-CBC解密成功，JSON包含sdk_backup_server: "121.43.187.92:8080"
```

* **验证闭环**：本地Python用PyCryptodome AES-256-CBC解密cfg.bin成功→有效JSON，反向加密与原始密文完全一致(True)。三重证据交叉验证。
* **⚠️ 修正复盘**：

* IV来源是本题最大陷阱：Java代码中System.arraycopy看似从cfg.bin自身提取IV，但创建的临时数组立即丢弃，实际IV由native层从iv.bin读取
* 多选题需逐项排除：A(Base32)→实际为Base64；D(AES-512-CBC)→实际为AES-256-CBC；E(IV来自文件自身)→实际来自独立iv.bin

---

### 🧩 Q4 — cfg.bin解密key

* **标准答案**：`47f32b6c3c50f7474f3a14787ef790f46d326e7a33a758d0c7e452cb120e0700`
* **状态等级**：🟢 已验证 / **L3 (三重交叉验证)**
* **解题主线**：**阶段1 — Java层密钥派生**： jadx反编译a.ag0.deriveKey()方法，发现执行SHA-256("tx2\_LIVE\_q1!v8c1a#|@0x7E::tuoxin.prod::")得到32字节AES-256密钥。

**阶段2 — native层HARD\_KEY分析**： IDA反编译native层obfuscate.cpp:17，发现HARD\_KEY数组存储为混淆值"live\_2026\_q1\_3f8c1a"，运行时去混淆后还原。关键发现：HARD\_KEY数组32字节的hex拼接值 = 47f32b6c3c50f7474f3a14787ef790f46d326e7a33a758d0c7e452cb120e0700。

**阶段3 — 交叉验证**：

* SHA-256("tx2\_LIVE\_q1!v8c1a#|@0x7E::tuoxin.prod::") = 47f32b6c...120e0700
* HARD\_KEY hex拼接 = 47f32b6c...120e0700
* 两者完全一致(Match: True)

**阶段4 — 本地解密验证**： 用该key + iv.bin中的IV，AES-256-CBC解密cfg.bin→有效JSON(含sdk\_backup\_server: 121.43.187.92:8080)，反向加密与原始密文完全一致。

* **💡 关键证据**：

* 证据编号：FINDING-Q4-001/002/003, CMD-20260804-010/011/013
* Java层：MessageDigest.getInstance("SHA-256").digest("tx2\_LIVE\_q1!v8c1a#|@0x7E::tuoxin.prod::".getBytes("UTF-8"))
* native层：obfuscate.cpp:17 HARD\_KEY数组32字节hex = 47f32b6c...120e0700
* ag0.verify()确认Java deriveKey == Native nativeGetKey

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line# Java层密钥派生分析mcp_jadx_get_class_source(class_name="a.ag0")# native层HARD_KEY交叉对比# Python本地验证import hashlib, binasciikey_source = "tx2_LIVE_q1!v8c1a#|@0x7E::tuoxin.prod::"sha_key = hashlib.sha256(key_source.encode('utf-8')).hexdigest()print(f"SHA-256 key: {sha_key}")# 输出: 47f32b6c3c50f7474f3a14787ef790f46d326e7a33a758d0c7e452cb120e0700# AES-256-CBC解密验证from Crypto.Cipher import AESfrom Crypto.Util.Padding import unpadimport base64key = bytes.fromhex(sha_key)iv = bytes.fromhex("9f4a2c18e6b7d053f8c1aa90d33b44e1")cfg_raw = open("cfg.bin", "rb").read()cfg_decoded = base64.b64decode(cfg_raw)cipher = AES.new(key, AES.MODE_CBC, iv)plaintext = unpad(cipher.decrypt(cfg_decoded[8:]), AES.block_size)print(plaintext.decode('utf-8'))  # → 有效JSON
```

* **📋 控制台回显**：

```
ounter(lineounter(lineounter(lineHARD_KEY = 47f32b6c3c50f7474f3a14787ef790f46d326e7a33a758d0c7e452cb120e0700与SHA-256("tx2_LIVE_q1!v8c1a#|@0x7E::tuoxin.prod::")完全一致(Match: True)AES-256-CBC解密cfg.bin成功→有效JSON(含sdk_backup_server: 121.43.187.92:8080)
```

* **验证闭环**：L3三重交叉验证 — (1)Java SHA-256输出 = (2)native HARD\_KEY hex = (3)本地Python解密成功+反向加密一致。
* **⚠️ 修正复盘**：

* **旧答案**：`tx2_LIVE_q1!v8c1a#|@0x7E::tuoxin.prod::`（key source字符串）
* **修正原因**：用户指出obfuscate.cpp:17 HARD\_KEY数组32字节hex拼接即为AES-256密钥，与SHA-256(key source)完全一致。题目问"解密key是多少"，答案为实际的32字节密钥(hex形式)，而非key source字符串
* **native层陷阱**：HARD\_KEY明文"live\_2026\_q1\_3f8c1a"是混淆存储形式，SHA-256(HARD\_KEY明文)解密→非UTF-8(失败)，证明需取HARD\_KEY数组的hex拼接值

---

### 🧩 Q5 — cfg.bin备份IP及端口

* **标准答案**：`121.43.187.92:8080`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**： cfg.bin经Q3/Q4流程解密后得到JSON配置文件，其中包含sdk\_internal.sdk\_backup\_server = "121.43.187.92:8080"。此为备份服务器IP地址及端口。
* **💡 关键证据**：

* 证据编号：FINDING-Q5-001, CMD-20260804-005/006
* cfg.bin解密后JSON内容：sdk\_backup\_server: "121.43.187.92:8080"

* **🛠️ 核心命令**：

```
ounter(line# 同Q4解密...