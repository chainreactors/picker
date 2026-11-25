---
title: 攻防世界 GFSJ0508「黑客精神」- 逆向分析
url: https://mp.weixin.qq.com/s/T7f66dAGhJzqze0nRk_eoA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:40:49.420074
---

# 攻防世界 GFSJ0508「黑客精神」- 逆向分析

# 攻防世界 GFSJ0508「黑客精神」- 逆向分析

西贝Legion
西贝Legion

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**环境与工具准备**

**00**

## 分析机为 macOS（自带 `objdump` 对 ARM Thumb-2 支持不完善，后面会踩坑），因此准备了一套 Python 逆向环境：

```
# 1. 建立隔离 venv（managed python）
VENV=~/.workbuddy/binaries/python/envs/default
python3 -m venv "$VENV"
"$VENV/bin/pip" install capstone pyelftools

# 2. 关键命令
jadx xman.apk            # Java 层反编译
file / strings / nm / objdump   # 原生库静态信息
python (capstone + pyelftools)  # 精确的 Thumb-2 反汇编
```

需要用到的核心 Python 库：

* **capstone**

  把 `.text` 机器码按 **Thumb-2** 正确反汇编（macOS 自带 objdump 会误判为 ARM）。
* **pyelftools**

  解析 ELF 段/节/符号表，做虚拟地址↔文件偏移换算。

##

**识别文件类型**

**01**

```
$ file libmyjni.so xman.apk
libmyjni.so: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, stripped
xman.apk:     Zip archive data (Android package)
```

结论：

* `xman.apk`

  是 Android 安装包，用 `jadx` 直接反编译 Java 层。
* `libmyjni.so`

  是 **32 位 ARM 动态库**，符号被 strip（只保留 `initSN/saveSN/n1/n2/n3/callWork/JNI_OnLoad` 等少数符号），核心逻辑在原生代码里。

###

**原生库静态侦察（strings / 动态符号）**

**02**

### 2.1 提取可读字符串

```
$ strings -n 4 libmyjni.so
...
JNI_OnLoad
g_env
native_class
getValue / setValue / callWork
fopen / fread / fputs / strcmp / strlen
/sdcard/reg.dat
W3_arE_whO_we_ARE
EoPAoY62@ElRD
com.gdufs.xman
输入即是flag,格式为xman{……}！
打开文件失败
```

关键线索已经浮现：

* 程序会在 `/sdcard/reg.dat` 读写文件（`fopen/fread/fputs`）。
* 存在两个可疑字符串：`W3_arE_whO_we_ARE`（很像密钥）和 `EoPAoY62@ElRD`（很像密文/目标）。
* `输入即是flag,格式为xman{……}！`

  明确告诉我们：用户输入即 flag 内容，包装格式为 `xman{...}`。

### 2.2 动态符号表（函数入口地址）

```
$ nm -D libmyjni.so
00001320 T getValue
00001364 T setValue
000013b0 T n1
000011f8 T n2
00001444 T callWork
000014cc T n3
00001508 T JNI_OnLoad
```

这些就是原生函数的真实入口地址，后面反汇编就按这些地址切分函数。

##

**Java 层分析（jadx）**

**03**

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2iahWDAPrwEHIA2a11siaDDaFhQY1u0CRJXULWBlB4SSb8sQdxdGts3cnt9H9AOvSnJLlVmK1YJ8f2ibw2z9yw8tWQ2rptfliat1U/640?wx_fmt=other&from=appmsg)

### 3.1 反编译

```
$ jadx -d jadx_out -j 4 xman.apk
```

### 3.2 包结构与调用关系

包名 `com.gdufs.xman`，三个关键类：

**MyApp（Application 子类）**

```
public class MyApp extends Application {
public static int m;                  // 0=未注册 1=已注册 其他=状态异常
public static native void initSN();
public static native void saveSN(String sn);
public static native void work();

@Override
public void onCreate() {
super.onCreate();
        initSN();                         // 启动时读取并校验注册状态
    }
}
```

**MainActivity**

```
// 按钮点击逻辑（整理后）
if (MyApp.m == 0) {
// 未注册 → 跳转到输入注册码界面
startActivity(new Intent(this, RegActivity.class));
} else {
work();   // 已注册 → 调用原生 work()，结果通过 MainActivity.work(String) 回调显示
}
// 原生 work() 内部会回调 MainActivity.work(String result)
```

**RegActivity**

```
// 用户在编辑框输入 sn，点确定：
MyApp.saveSN(et.getText().toString());   // 交给原生 saveSN 加密保存
// 然后杀掉进程（下次启动由 initSN 重新判定）
```

### 3.3 Java 层结论

* 注册码由用户从 `RegActivity` 输入，经 `saveSN` 写进 `/sdcard/reg.dat`（加密后的数据）。
* 下次 App 启动，`MyApp.onCreate()` 调 `initSN()` 读回 `reg.dat`，与内置目标比对，决定 `m` 的值。
* `work()`

  在 `m==1` 时把 flag 通过 `MainActivity.work(String)` 回调显示出来。
* **java 层本身不含任何密钥/校验逻辑**

  ，真正算法全在 `libmyjni.so`。因此下一步必须啃原生代码。

##

**原生层反汇编（踩坑：Thumb-2 vs ARM）**

**04**

## 4.1 第一次尝试失败

```
$ objdump -d libmyjni.so | head
000011f8 <n2>:
    e92d 6803   push    {r0, r1, r11, lr}   # 这条在 ARM 模式下是错的
```

`push {r0, r1, ...}` 在 ARM 指令集里根本不合法 → 说明这些函数是用 **Thumb-2** 编译的，但 `objdump` 当成 ARM 解码，整段错位。

### 4.2 改用 Capstone 按 Thumb-2 精确反汇编

由于 macOS 的 `objdump` 不支持 `force-thumb`，写 Python 脚本用 Capstone 解码：

```
from elftools.elf.elffile import ELFFile
from capstone import Cs, CS_ARCH_ARM, CS_MODE_THUMB

elf = ELFFile(open("libmyjni.so", "rb"))
text = elf.get_section_by_name(".text")
code = text.data()
base = text["sh_addr"]
md = Cs(CS_ARCH_ARM, CS_MODE_THUMB)

# 按符号表给出的函数边界逐函数反汇编（避免整段错位）
for name, addr, end in [("n2",0x11f8,0x13b0), ("n1",0x13b0,0x1444),
                         ("n3",0x14cc,0x1508), ("JNI_OnLoad",0x1508,0x1600)]:
    print(f"===== {name} =====")
for insn in md.disasm(code[addr-base:end-base], addr):
        print(f"{insn.address:#08x}: {insn.mnemonic} {insn.op_str}")
```

反汇编结果片段（`n2` 开头）：

```
000011f8: push.w  {r4, r5, r6, r7, r8, sb, sl, lr}
000011fc: mov     r6, r0
000011fe: ldr     r4, [pc, #0x108]
00001200: sub     sp, #0x18
00001202: ldr     r0, [pc, #0x108]
...
0000125e: mov.w   r4, #0x7e0          # ← 关键：运行计数器 r4 初值 0x7e0
...
0000127e: movs    r1, #3
00001280: blx     #0x16c8            # 调用一个取模运算 (i % 3)
00001284: cmp     r1, #1
00001286: bne     #0x12a8
...                              # i%3 == 1 分支
0000128a: adds    r4, #5
0000128c: ands    r3, r4
...
000012a8: cmp     r1, #2
000012aa: bne     #0x12c0
...                              # i%3 == 2 分支
000012ac: adds    r0, r4, #7
...
000012c0: adds    r0, r4, #3          # i%3 == 0 分支
...
000012d2: ldrb    r3, [r5]           # 取出明文第 i 字节
000012d6: adds    r5, #1
000012d8: eors    r3, r2             # ← 与密钥字节 XOR
000012da: strb    r3, [r5, #-0x1]    # 存回（密文）
```

至此确认 `n2` 就是一个 **逐字节 XOR 加密函数**：

* `fopen("/sdcard/reg.dat", "w+")`

  打开文件；
* 把 18 字节密钥结构从 rodata 拷到栈上；
* 对输入字符串逐字节，用由 `r4`（初值 `0x7e0`）派生出的密钥索引取密钥字节，做 XOR；
* `fputs`

  把结果写入 `reg.dat`。

##

**确认 Java 方法 ↔ 原生函数 的映射**

**05**

静态区 `.data` 中保存了 `JNINativeMethod` 结构体数组（三要素：`{方法名指针, 签名指针, 函数指针}`）。

该数组在文件偏移 `0x4004` 处，用 Python 解析：

```
from elftools.elf.elffile import ELFFile
elf = ELFFile(open("libmyjni.so", "rb"))
data = open("libmyjni.so", "rb").read()

# JNINativeMethod 数组（3 项，每项 12 字节）
base = 0x4004
arr = data[base:base+3*12]
for k in range(3):
    e = arr[k*12:k*12+12]
    name_p = int.from_bytes(e[0:4], "little")   # 方法名 vaddr
    sig_p  = int.from_bytes(e[4:8], "little")   # 签名 vaddr
    fn     = int.from_bytes(e[8:12], "little")  # 原生函数 vaddr (+1 表示 Thumb)
# 通过 PT_LOAD 把 vaddr 换算成文件偏移，读出字符串
    ...
print(name, fn)
```

解析结果：

| Java 方法 | 签名 | 原生函数（Thumb 地址） | 真实地址 | 对应符号 |
| --- | --- | --- | --- | --- |
| `initSN` | `()V` | `0x13b1` | `0x13b0` | **n1** |
| `saveSN` | `(Ljava/lang/String;)V` | `0x11f9` | `0x11f8` | **n2** |
| `work` | `()V` | `0x14cd` | `0x14cc` | **n3** |

> 函数指针 (`0x13b1/0x11f9/0x14cd`) 末尾的 `+1` 是 ARM/Thumb 调用约定（bit0=1 表示 Thumb 代码）。

##

**逐个函数分析算法**

**06**

## 6.1 `n2`（= `saveSN`，地址 0x11f8）—— 加密写入

逻辑梳理（结合反汇编 + 字面池）：

* `fopen("/sdcard/reg.dat", "w+")`

  （路径来自 rodata `0x2da8`，模式 `w+` 来自 `0x2db8`）。
* 把 18 字节密钥结构从 rodata `0x2ddd` 拷到栈（通过 `ldr r0,[pc,...]` + `stm` 批量拷贝）：`0x2ddd: 'W3_arE_whO_we_ARE\0'`（17 字符 + 1 个 0x00 = 18 字节）。
* 取输入字符串长度 `strlen`，循环：

+ 计算 `rem = i % 3`（调用一个 `__modsi3` 之类的辅助函数，地址 `0x16c8`）；
+ 根据 `rem` 用不同步长推进计数器 `r4`（初值 `0x7e0`）并算出密钥下标 `idx`：

  | `rem = i%3` | `r4` 更新 | 密钥下标 `idx` |
  | --- | --- | --- |
  | 0 | `r4 = (r4 + 3) % 13` | `idx = r4 + 3` |
  | 1 | `r4 = (r4 + 5) & 0xF` | `idx = r4 + 1` |
  | 2 | `r4 = (r4 + 7) % 15` | `idx = r4 + 2` |
+ `cipher[i] = plain[i] ^ key_struct[idx]`

* `fputs(cipher, fp)`

  写入 `reg.dat`，`fclose`。

### 6.2 `n1`（= `initSN`，地址 0x13b0）—— 校验注册状态

反汇编尾部（从 `strcmp` 开始，地址 `0x1410` 起）：

```
00001410: ldr   r1, [pc, #0x2c]   ; 字面池 → 目标字符串指针
00001412: strb.w r8, [r5, r7]     ; 在缓冲区末尾补 '\0'
00001416: mov   r0, r5
00001418: add   r1, pc
0000141a: blx   #0x1168           ; ← 调用 strcmp(content, TARGET)
0000141e: cbnz  r0, #0x1426       ; 不相等 → 跳 1426
00001420: mov   r0, r6
00001422: movs  r1, #1            ; 相等 → setValue(obj, 1)  ← 注册成功
00001424: b     #0x142a
00001426: mov   r0, r6
00001428: mov   r1, r8            ; 不相等 → setValue(obj, 0)
0000142a: bl    #0x1364           ; setValue
```

字符串指针解析（PC 相对 + 字面池）：

* `fopen`

  路径 `0x2da8`(`/sdcard/reg.dat`)，模式 `0x2e08`(`r+`)。
* `strcmp`

  的 **目标字符串**位于 rodata `0x2e0b`：`0x2e0b: 'EoPAoY62@ElRD'`（13 字节）。

**核心结论**：`initSN` 把 `reg.dat` 读出来后，只要 `strcmp(content, "EoPAoY62@ElRD") == 0`，就把状态置为 `m=1`（注册成功）。也就是说，写进 `reg.dat` 的内容必须等于密文 `EoPAoY62@ElRD`。

### 6.3 `n3`（= `work`，地址 0x14cc）—— 回显提示

```
000014cc: bl #0x13b0        ; 先调 initSN 刷新 m
000014d4: bl #0x1320        ; getValue(obj) 读取 m
000014da: cbnz r0, #0x14e4  ; m != 0
000014dc: ... string '还不行呢！'        (m==0：未注册)
000014e4: cmp r0, #1
...