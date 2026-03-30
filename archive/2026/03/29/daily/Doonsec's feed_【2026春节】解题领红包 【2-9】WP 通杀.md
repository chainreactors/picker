---
title: 【2026春节】解题领红包 【2-9】WP 通杀
url: https://mp.weixin.qq.com/s/YkgeclEp_9NwLisSUpC5sw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:45:19.332133
---

# 【2026春节】解题领红包 【2-9】WP 通杀

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aV8UF5rUbweSdybZroF6F5KnWVPCy7lnK2huI6wKWAJllqsUOhOKjbNliao3JmicdzkibVjcO0OmibdsBibiaCjrbl3sR2bCE5kTCjs6Y4gM5pt0A/0?wx_fmt=jpeg)

# 【2026春节】解题领红包 【2-9】WP 通杀

原创

吾爱pojie
吾爱pojie

吾爱破解论坛

![]()

在小说阅读器中沉浸阅读

作者**论****坛账号：jingtai123**

## 书接上回

> 【2026春节】解题领红包10.Windows 高级题 11.MCP 中级题
> https://www.52pojie.cn/thread-2094516-1-1.html

## 继续感慨 难得通杀 借了AI的大势了

> AI的发展太离谱了。不学习AI 就像发明了汽车马夫不学开车一样。
>
> 本篇内容大部分由AI生成。

## 2026春节解题领红包之二 - Windows初级题

### 题目概述

这是一道逆向分析题目，需要分析给定的汇编代码，找到并解密flag。

> 一开始走了爆破路线，后来AI分析直接秒了- -！

---

### 方法一：直接分析汇编解密

#### 分析过程

1. **定位解密函数**

   在汇编代码的 **00521620 - 00521681** 地址处找到了关键的解密函数。
2. **分析加密数据初始化**

   该函数首先在堆栈上初始化加密数据：

   ```
    复制代码 隐藏代码
   0052162C | C702 7770322D            | mov dword ptr ds:[edx],2D327077
   00521635 | C742 04 282B2763         | mov dword ptr ds:[edx+4],63272B28
   0052163C | C742 08 63631D70         | mov dword ptr ds:[edx+8],701D6363
   ...
   ```
3. **分析解密算法**

   核心解密逻辑使用异或操作：

   ```
    复制代码 隐藏代码
   00521670 | 8030 42                  | xor byte ptr ds:[eax],42    ; 密钥是 0x42
   00521673 | 83C0 01                  | add eax,1
   00521676 | 39C8                     | cmp eax,ecx
   00521678 | 75 F6                    | jne 00521670
   ```

   **解密算法**：对每个字节执行 `byte ^ 0x42`
4. **提取加密数据**

   从汇编代码中提取完整的加密数据：

   ```
    复制代码 隐藏代码
   encrypted = [
      0x77, 0x70, 0x32, 0x2D,
      0x28, 0x2B, 0x27, 0x63,
      0x63, 0x63, 0x1D, 0x70,
      0x72, 0x70, 0x74, 0x1D,
      0x0A, 0x23, 0x32, 0x32,
      0x3B, 0x1D, 0x2C, 0x27,
      0x35, 0x1D, 0x3B, 0x27,
      0x23, 0x30, 0x63
   ]
   ```

#### 解密结果

```
 复制代码 隐藏代码
52pojie!!!_2026_Happy_new_year!
```

---

### 方法二：Checksum 约束 + 多线程爆破验证

#### 分析过程

在逆向分析过程中，我们发现了程序使用了 Checksum 验证机制：

```
 复制代码 隐藏代码
defget_checksum(text):
    returnsum(ord(c) * (i + 1) for i, c inenumerate(text))
```

已知条件：

* 目标长度：31
* 目标 Checksum：44709
* 关键词列表：`["52pojie", "2026", "Happy_new_year", "_", "!"]`

#### 核心算法

采用 **DFS（深度优先搜索）** 配合 **多线程验证** 的策略：

1. **DFS 遍历**

   ：使用关键词进行深度优先搜索，生成所有可能的组合
2. **Checksum 剪枝**

   ：在 DFS 过程中实时计算 Checksum，如果超过目标值则立即剪枝
3. **数学优化**

   ：利用公式 `add_checksum = block.base_weight + (current_len * block.char_sum)` 进行 O(1) 级别的快速计算

```
 复制代码 隐藏代码
# 预处理每个关键词的基础信息
blocks_info = []
for b in WORD_BLOCKS:
    base_weight = sum(ord(c) * (i + 1) for i, c inenumerate(b))
    char_sum = sum(ord(c) for c in b)
    blocks_info.append({
        "str": b,
        "len": len(b),
        "base_weight": base_weight,
        "char_sum": char_sum
    })

defdfs(current_str, current_len, current_checksum):
    # 剪枝：Checksum 超标
    if current_checksum > TARGET_CHECKSUM:
        return
    # 剪枝：长度达标
    if current_len == TARGET_TOTAL_LENGTH:
        if current_checksum == TARGET_CHECKSUM:
            task_queue.put(current_str)
        return
    # 剪枝：长度超标
    if current_len > TARGET_TOTAL_LENGTH:
        return
    for block in blocks_info:
        add_checksum = block["base_weight"] + (current_len * block["char_sum"])
        dfs(current_str + block["str"], current_len + block["len"], current_checksum + add_checksum)
```

4. **多线程验证**

   ：开启多个线程，从队列中获取候选 flag 并调用 EXE 程序进行验证，一旦找到正确答案立即通知所有线程停止

```
 复制代码 隐藏代码
NUM_THREADS = 8
defworker_thread(thread_id):
    whilenot found_event.is_set():
        try:
            flag = task_queue.get(timeout=0.5)
        except queue.Empty:
            if dfs_done_event.is_set():
                break
            continue

        output = test_flag(flag)
        if"SUCCESS"in output or"Congratulations"in output:
            found_event.set()
```

#### 验证结果

对解密结果进行验证：

* 字符串：`52pojie!!!_2026_Happy_new_year!`
* 长度：31
* 计算出的 Checksum：44709

**验证通过！** 完全匹配目标值。

---

### 最终 Flag

```
 复制代码 隐藏代码
52pojie!!!_2026_Happy_new_year!
```

---

### 解题脚本

#### 1. 汇编解密脚本 (solve.py)

```
 复制代码 隐藏代码
# 从汇编代码中提取加密数据
encrypted = [
    0x77, 0x70, 0x32, 0x2D,
    0x28, 0x2B, 0x27, 0x63,
    0x63, 0x63, 0x1D, 0x70,
    0x72, 0x70, 0x74, 0x1D,
    0x0A, 0x23, 0x32, 0x32,
    0x3B, 0x1D, 0x2C, 0x27,
    0x35, 0x1D, 0x3B, 0x27,
    0x23, 0x30, 0x63
]

# 密钥是 0x42
key = 0x42

# 解密
decrypted = bytes([b ^ key for b in encrypted])

print("解密结果：")
print(decrypted.decode('utf-8', errors='ignore'))
```

#### 2. Checksum 验证脚本 (myz3.py)

```
 复制代码 隐藏代码
import subprocess
import time
import threading
import queue

WORD_BLOCKS = [
    "52pojie",
    "2026",
    "Happy_new_year",
    "_",
    "!"
]

TARGET_TOTAL_LENGTH = 31
TARGET_CHECKSUM = 44709
NUM_THREADS = 8

task_queue = queue.Queue()
found_event = threading.Event()
dfs_done_event = threading.Event()
print_lock = threading.Lock()

deftest_flag(flag):
    exe_path = r'【2026春节 解题领红包之二 {Windows 初级题} 出题老师：云在天.exe'
    p = subprocess.Popen(
        [exe_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=r'C:\Users\jingt\Desktop\52pojie\第一题'
    )
    output, _ = p.communicate(input=flag + '\n', timeout=3)
    return output

defworker_thread(thread_id):
    whilenot found_event.is_set():
        try:
            flag = task_queue.get(timeout=0.5)
        except queue.Empty:
            if dfs_done_event.is_set():
                break
            continue

        output = test_flag(flag)

        if"SUCCESS"in output or"Congratulations"in output:
            with print_lock:
                print(f"\n[+] 线程 {thread_id} 破案了！真正的 Flag 是：{flag}")
            found_event.set()
        else:
            with print_lock:
                print(f"    [-] 线程 {thread_id} 验证失败: {flag}")

        task_queue.task_done()

# 预处理关键词信息
blocks_info = []
for b in WORD_BLOCKS:
    base_weight = sum(ord(c) * (i + 1) for i, c inenumerate(b))
    char_sum = sum(ord(c) for c in b)
    blocks_info.append({
        "str": b,
        "len": len(b),
        "base_weight": base_weight,
        "char_sum": char_sum
    })

defdfs(current_str, current_len, current_checksum):
    if found_event.is_set():
        return
    if current_checksum > TARGET_CHECKSUM:
        return
    if current_len == TARGET_TOTAL_LENGTH:
        if current_checksum == TARGET_CHECKSUM:
            task_queue.put(current_str)
        return
    if current_len > TARGET_TOTAL_LENGTH:
        return
    for block in blocks_info:
        add_checksum = block["base_weight"] + (current_len * block["char_sum"])
        dfs(current_str + block["str"], current_len + block["len"], current_checksum + add_checksum)

# 启动多线程
threads = []
for i inrange(NUM_THREADS):
    t = threading.Thread(target=worker_thread, args=(i+1,))
    t.daemon = True
    t.start()
    threads.append(t)

dfs("", 0, 0)
dfs_done_event.set()

for t in threads:
    t.join()
```

---

### 解题思路总结

1. **快速定位解密函数**

   ：在汇编中寻找典型的解密特征（XOR操作、循环处理、字符串操作）
2. **分析算法细节**

   ：确定加密数据、密钥和算法
3. **复现解密过程**

   ：用脚本实现相同的算法
4. **辅助验证**

   ：通过Checksum等约束条件验证结果正确性
5. **多线程加速**

   ：使用多线程配合EXE验证，快速定位正确答案

---

## 2026春节*解题领红包之三*{Android\_初级题}\_出题老师\_正己

### 直接拼图

一开始分析半天，实在不想装APK，然后除了jntm 啥也没分析出来，于是虚拟机安装拼图直接答案了！白浪费时间 - -！

---

## 【2026春节】解题领红包之四 {Windows 初级题} 出题老师：云在天

### 解题思路

这是一个使用 PyInstaller 打包的 Python CrackMe 程序。与其从汇编代码层面进行分析，更高效的方法是直接提取和分析 PyInstaller 打包的 pyc 文件。

### 解题步骤

#### 1. 识别程序结构

首先观察到程序是一个典型的 PyInstaller 打包的 Windows 可执行文件，其特征包括：

* 包含解压缩和库加载的启动代码
* 使用 Python 解释器动态加载模块
* 有清晰的 PyInstaller 特征（如 PYZ.pyz 文件）

#### 2. 提取打包文件

使用 PyInstaller 自带的提取工具或 pyinstxtractor.py 提取程序内容，可以获得：

* `crackme_easy.pyc`

  - 主要程序逻辑的编译文件
* `PYZ.pyz`

  - Python 归档文件
* 各种系统库和 Python 依赖库

#### 3. 分析 pyc 文件

虽然 uncompyle6 不支持 Python 3.14，但我们可以使用 Python 内置的 `dis` 模块直接分析字节码：

```
 复制代码 隐藏代码
import marshal
import dis

pyc_path = "crackme_easy.pyc"
withopen(pyc_path, 'rb') as f:
    f.read(16)  # 跳过 pyc 头部
    code_obj = marshal.load(f)

dis.dis(code_obj)
```

#### 4. 关键函数详细分析

##### 4.1 `get_encrypted_flag()` - 获取加密数据

```
 复制代码 隐藏代码
defget_encrypted_flag():
    enc_data = 'e3w+fiRvfW18fnx4ZAZ6Pj43YwB9OWMXfXo8Dg4O'
    return base64.b64decode(enc_data)
```

**分析**: 这个函数简单地返回一个 base64 编码的加密字符串，没有任何复杂逻辑。

---

##### 4....