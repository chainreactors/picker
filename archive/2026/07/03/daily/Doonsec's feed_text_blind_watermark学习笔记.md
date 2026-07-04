---
title: text_blind_watermark学习笔记
url: https://mp.weixin.qq.com/s/N81i4C4vurBOhneU6KxFLg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:45:43.529066
---

# text_blind_watermark学习笔记

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/teQhPZBEOpN0mrib3ou6rwE8wic2T5LnKic4y2ic1uibHWJEnmIeaxZNr4KicRLTZuNJ8ZRUwicxNcdMnxHyMptPaQea8ToA41WegqPibkFD16CBydE/0?wx_fmt=jpeg)

# text\_blind\_watermark学习笔记

原创

泷羽Sec静安
泷羽Sec静安

泷羽Sec-静安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# text\_blind\_watermark 文本盲水印

> 关注**泷羽Sec**和**泷羽Sec-静安**公众号，这里会定期更新与 OSCP、渗透测试等相关的最新文章，帮助你理解网络安全领域的最新动态。后台回复"OSCP配套工具"获取相关的工具

## 一、原理

> 项目地址：https://github.com/guofei9987/text\_blind\_watermark

文本盲水印将信息隐匿到文本中，不改变文本外观和可读性。

### 核心思路

```
嵌入: 水印字符串 → 加密 → 二进制 bit 流 → 在载体文本的字符间插入不可见字符
提取: 扫描文本 → 识别不可见字符 → 还原 bit 流 → 解密 → 原始字符串
```

* bit `1` → 在载体文本的字符后插入一个不可见字符（如 `chr(0x7F)` 或零宽字符）
* bit `0` → 不做操作，只移动到下一个字符

---

## 二、v0.4.2 用法（最新版，推荐）

### 安装

```
pip install text_blind_watermark
```

### 嵌入

```
from text_blind_watermark import TextBlindWatermark

password = b"p@ssw0rd"
watermark = b"This is watermark"

with open('original.txt', 'r') as f:
    text = f.read()

twm = TextBlindWatermark(pwd=password)
text_with_wm = twm.add_wm_rnd(text=text, wm=watermark)

with open('output.txt', 'w') as f:
    f.write(text_with_wm)
```

### 提取

```
from text_blind_watermark import TextBlindWatermark

password = b"p@ssw0rd"

with open('output.txt', 'r') as f:
    text_with_wm = f.read()

twm = TextBlindWatermark(pwd=password)
result = twm.extract(text_with_wm)
print(result)  # b'This is watermark'
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpOxJHGcmkMOhxqPXPleLc1MQxrvCiapibIQF0sUb8NqiaYVfAsy9KJOP1Mr4yKiaIgicLlIW8vuVaJODmhicmUeuvHOXesADqkibOsyq0/640?wx_fmt=png&from=appmsg)

### 技术细节

* 水印字符：`chr(0x2060)` (Word Joiner) 表示 bit=0，`chr(0xFEFF)` (BOM) 表示 bit=1
* 加密方式：XOR（通过 `CryptConverter`）
* 密码格式：**bytes 类型**，如 `b"password"`
* 水印字符是真正的零宽字符，**终端/浏览器中完全不可见**
* 嵌入位置随机（`add_wm_rnd`），也可以指定位置（`add_wm_at_idx`）

### 其他嵌入方式

```
twm.add_wm_at_idx(text=text, wm=watermark, byte_idx=10)  # 指定位置嵌入
twm.add_wm_at_last(text=text, wm=watermark)                # 末尾嵌入
```

---

## 三、v0.0.2 用法（AES-ECB 加密，CTF 常考）

### 安装

```
pip install text_blind_watermark==0.0.2 pycryptodome
```

> **注意：** v0.0.2 源码中 `import crypto` 与 `pycryptodome` 的 `Crypto` 模块冲突。 安装 `crypto` 包后还需手动修复源码中的 import。**CTF 建议直接用下方的独立脚本，不依赖库版本。**

### 嵌入

```
from text_blind_watermark import embed

sentence = "这是一段很长的载体文本..." * 100  # 载体文本必须足够长
watermark = "secret_message"
password = "my_password"

result = embed(sentence, watermark, password)

with open('output.txt', 'w') as f:
    f.write(result)
```

### 提取

```
from text_blind_watermark import extract

with open('output.txt', 'r') as f:
    data = f.read()

password = "my_password"
flag = extract(data, password)
print(flag)  # secret_message
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpOQ6Ykd96gniaNYZDC0OcZDoyvQy2C2XMvKGloAfuibo0Y1cibx7EjDwF0IqVyZ4ZE5csKzymcyghtcr6yGPudDTBwAM42icTA9LAc/640?wx_fmt=png&from=appmsg)

### 技术细节

* 水印字符：`chr(127)` 即 `0x7F` (DEL)
* 加密方式：**AES-ECB**
* 密码格式：**字符串类型**，右补 `0` 至 16 字节作为 AES 密钥

+ 如 `"my_password"` → `"my_password00000"`

* 嵌入流程：`水印 → UTF-8 编码 → AES-ECB 加密 → 十六进制 → 二进制 → 插入 chr(0x7F)`
* 提取流程：`扫描 chr(0x7F) → 二进制 → 对齐 128 位 → 十六进制 → AES-ECB 解密`

---

## 四、版本对比

| 版本 | 安装 | 水印字符 | 加密 | 密码类型 | API |
| --- | --- | --- | --- | --- | --- |
| v0.0.2 | `pip install text_blind_watermark==0.0.2 crypto pycryptodome` | `chr(127)` 0x7F | AES-ECB | str | `embed()` / `extract()` |
| v0.4.2 | `pip install text_blind_watermark` | `0x2060` / `0xFEFF` | XOR | bytes | `TextBlindWatermark` 类 |

---

## 五、CTF 解题

### 典型套路

1. 题目给出一个嵌入水印的文件（.txt 或通过隐写工具提取的 .txt）
2. 密码可能藏在文件尾部、文件名、题目描述中
3. 识别出 `text_blind_watermark` 库，判断版本，用对应算法解密
4. 输出可能是 hex 编码，需要再做一次 hex decode

### 万能解题脚本（不依赖库版本）

适用于 v0.0.2 的 AES-ECB 算法，不需要安装 `text_blind_watermark`：

```
from Crypto.Cipher import AES

with open('text_blind_watermark.txt', 'r') as f:
    data = f.read()

password = '!@#$123456'  # 根据题目修改

# 1. 提取二进制：chr(0x7F) = bit 1，其余 = bit 0
bin_wm = ""
prev = False
for ch in data:
    if prev:
        if ord(ch) == 127:
            bin_wm += "1"
            prev = False
        else:
            bin_wm += "0"
            prev = True
    else:
        prev = True

# 2. 去尾部零，对齐到 128 位边界（AES 块大小）
last = len(bin_wm) - bin_wm[::-1].find("1")
last = ((last - 1) // 128 + 1) * 128
bin_wm = bin_wm[:last]

# 3. AES-ECB 解密
hex_str = hex(int(bin_wm, 2))
key = '{:0<16}'.format(password).encode('utf-8')
result = AES.new(key=key, mode=AES.MODE_ECB).decrypt(
    bytes.fromhex(hex_str[2:])
).decode('utf-8')

print("提取结果:", result)

# 4. 如果结果是 hex 编码的 flag，再解一次
flag_hex = result.split()[-1]
print("Flag:", bytes.fromhex(flag_hex).decode())
```

### 快速判断版本

```
# 检查文件中有哪些特殊字节
python3 -c "
data = open('text_blind_watermark.txt', 'rb').read()
print('0x7F (DEL):', data.count(0x7F))
print('0xE280A0 (0xFEFF UTF-8):', data.count(b'\xef\xbb\xbf'))
print('0xE281A0 (0x2060 UTF-8):', data.count(b'\xe2\x81\xa0'))
print('唯一字节:', sorted(set(data)))
"
```

* 含 `0x7F` → v0.0.2 ~ v0.3.1，用上面的万能脚本
* 含零宽字符 → v0.4.2，用 `TextBlindWatermark` 类

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpM0ukfLyibClF5pvM4GrTK9VcUnyVO4CPTfiaqIIW2fr8Bo047nPVGtpBiacibGmOwgAJhr2zlDxPRaMss8ibImFvTEDZPhk2EI9g6I/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpNHXtxURl1nLicNc12yALz7nAUOSEr795U1091ib0RYup45IkgnU0aZIe124AosHMMKmbRASV9iauzuWjBe9Avo7xeMb8BCNGic7E0/640?wx_fmt=png&from=appmsg)

---

## 六、踩坑记录

### 1. v0.0.2 的 `import crypto` 冲突（最常见）

v0.0.2 源码第一行是 `import crypto`（小写），但实际需要的是 `pycryptodome` 提供的 `Crypto`（大写）。

**修复方法**：安装后手动改源码：

```
pip install text_blind_watermark==0.0.2 pycryptodome
# 找到源码位置
vi $(python -c "import text_blind_watermark; print(text_blind_watermark.__file__)")
# 第1行: import crypto → import Crypto
# 注释掉第4行: # sys.modules['Crypto'] = crypto
```

### 2. v0.0.2 的 `bin()` 丢前导零 bug

`embed()` 函数中 `bin(int(hex, 16))` 会丢掉前导零。当 AES 密文首字节 < 0x10 时，二进制少一位，提取结果错位，解密出乱码。

**修复方法**：在源码中将：

```
# embed 中:
bin_text = bin(int(ciphertext_hex, base=16))[2:]
# 改为:
bin_text = bin(int(ciphertext_hex, base=16))[2:].zfill(len(ciphertext_tmp) * 8)

# extract 中:
hex_wm_extract = hex(int(bin_wm_extract, base=2))
AES...decrypt(bytes.fromhex(hex_wm_extract[2:]))
# 改为:
hex_wm_extract = hex(int(bin_wm_extract, base=2))[2:].zfill(len(bin_wm_extract) // 4)
AES...decrypt(bytes.fromhex(hex_wm_extract))
```

### 3. 密码类型不同

* v0.0.2 用 **字符串**：`password = "my_password"`
* v0.4.2 用 **bytes**：`password = b"p@ssw0rd"`

### 4. 不可见字符在复制粘贴时丢失

* `chr(0x7F)` 在终端中不可见但存在
* 零宽字符（0x2060/0xFEFF）复制粘贴可能丢失
* **始终直接传文件，不要复制粘贴内容**

## 七、实际应用场景

### 1. 文档泄露溯源（最核心用途）

给不同人发同一份文档，每个人嵌入不同的水印（如工号、邮箱）。一旦泄露，提取水印就知道是谁泄的。

* 公司内部敏感报告、商业计划书
* 上市公司财报发给不同分析师
* 政府机密文件分发

### 2. AI / LLM 输出追踪

给 AI 生成的文本嵌入水印，后续可验证某段文本是否由该模型生成。DeepMind、OpenAI 都在研究这个方向。

### 3. 社交平台防搬运

在知乎、公众号文章里嵌入隐形水印，被人复制搬运后可举证是你的内容。

### 4. 企业通讯取证

在钉钉、飞书等企业通讯中，给每条消息嵌入用户标识，截图泄露后可溯源。

### 为什么选"盲"水印

"盲"指**提取时不需要原始文本**，只需密码。普通水印提取需要对比原文，盲水印只要有密码就能从被篡改过的文本里提取出来。

## 八、v0.4.2 复制粘贴兼容性

v0.4.2 使用零宽 Unicode 字符（`U+2060` Word Joiner / `U+FEFF` BOM），**可以跨平台复制粘贴传播**。

### 测试通过的场景

经作者测试，以下场景水印信息隐藏比较完美：

* **Chrome 浏览器**（Mac），包括知乎网页版、微博网页版等
* **微信、钉钉**（Mac / iPhone 均可）
* **苹果备忘录**
* **Chrome 打开 github.com** 上的代码文件和文本文件（md 文件不行）
* 用 **Ctrl+C/V** 在上述平台之间复制粘贴

![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpPIRuyBZwIeKfYHNVRBIKFVLkNJSB5uATxMyiaHLJyo4NLhgZ2zLtzga0dEUgjic9672HTvOqMRwxwbDJleFRRicXKZYWwS1ywBD0/640?wx_fmt=png&from=appmsg)

使用收集复制再发这个也是可以的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpO4lkwaicoZu9z0Rv1K5vgn2B9W5aIqooTxdb3W7lm1zJO9FKLnLo2gXmx4Z09P0s15XwMknT1ATdib3Aeeicsx7aUw6VTRb5lDoA/640?wx_fmt=png&from=appmsg)

### 不太行的场景

* **Safari 浏览器**

### 为什么 v0.4.2 比 v0.0.2 强在传播

|  | v0.0.2 | v0.4.2 |
| --- | --- | --- |
| 水印字符 | `chr(0x7F)` DEL | `U+2060` / `U+FEFF` 零宽字符 |
| 是否可见 | 终端中显示为乱码 | 完全不可见 |
| 复制粘贴 | 大概率丢失 | 多数平台保留 |
| 适用场景 | 本地文件隐写 | **跨平台传播溯源** |

v0.4.2 的设计目标就是**让水印跟着文字走**——复制到微信、钉钉、知乎，水印都在。这才是实际生产环境该用的版本。

## 九、抗篡改能力分析

作者说"经过一定范围的修改仍能提取"，实际上**没那么强**。具体看怎么改、改哪里。

### v0.0.2 的抗篡改能力（基本没有）

水印是逐字符插在载体文本里的，每个 bit 对应一个载体字符位置。**任何改变字符数量的操作都会导致错位**：

| 篡改类型 | 能否提取 | 原因 |
| --- | --- | --- |
| 末尾增删文字 | ✅ ...