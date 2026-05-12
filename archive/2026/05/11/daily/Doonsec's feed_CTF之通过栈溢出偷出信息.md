---
title: CTF之通过栈溢出偷出信息
url: https://mp.weixin.qq.com/s/ViZnGRYTJX1pVWSuFehKhQ
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:33:42.019985
---

# CTF之通过栈溢出偷出信息

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIyXibGLTfgAtY3lAIWLb6RpYOc45HQzN0ND5HWSqLSv1CVxKbWT0mEWnRjuvnS1z6BWZXN5KgbiaLEeIgicuEKIqibdjp0GCGwx0Z4/0?wx_fmt=jpeg)

# CTF之通过栈溢出偷出信息

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、技术原理

栈溢出是二进制安全中最基础也是最经典的漏洞类型，其本质在于程序在向栈上的缓冲区写入数据时，未对输入数据的长度进行边界检查。当攻击者输入的数据量超过了缓冲区预分配的大小（例如向一个64字节的数组写入100字节），多余的数据就会像水漫过堤坝一样，覆盖栈帧中紧邻缓冲区的“高地址”数据。这些数据通常包括保存的基址指针和最为关键的函数返回地址。一旦返回地址被恶意篡改，当函数执行完毕尝试通过`ret`指令返回时，CPU的指令指针寄存器就会被指向攻击者预设的地址，从而导致程序的控制流被劫持，执行非预期的代码逻辑。

```
#include <stdio.h>
#include <string.h>

voidvulnerable_function() {
    char buffer[64]; // 定义一个64字节的缓冲区
    printf("请输入数据: ");
    // 使用gets函数，它不检查输入长度，极易导致栈溢出
    gets(buffer);
    printf("输入结束。\n");
}

intmain() {
    vulnerable_function();
    return0;
}
```

```
# 关闭所有保护，方便进行栈溢出练习
gcc -fno-stack-protector -no-pie -z execstack -o vuln vuln.c
```

编译指令参数表

| 保护机制 | 开启指令 (默认/推荐) | 关闭指令 (用于练习) | 作用描述 |
| --- | --- | --- | --- |
| **Stack Canary** | `-fstack-protector-strong` | `-fno-stack-protector` | 在返回地址前插入随机值，检测溢出。 |
| **PIE (地址随机化)** | `-pie -fPIE` | `-no-pie` | 随机化程序基址，使返回地址难以预测。 |
| **NX (栈不可执行)** | `-z noexecstack` | `-z execstack` | 标记栈内存为不可执行，防止运行Shellcode。 |

# 二、NX保护机制

NX（No-eXecute，禁止执行）是操作系统与CPU协同工作的一种安全机制。它的核心原理是将内存页划分为“可读/可写”和“可执行”两类。通常，栈和堆内存被标记为“不可执行”。这意味着，即使攻击者通过栈溢出成功将恶意代码写入了栈内存中，CPU在尝试执行这些指令时也会抛出异常并强制终止程序。NX保护极大地增加了直接在栈上运行代码的难度，是现代操作系统默认开启的基础防线。

```
#include <stdio.h>
#include <string.h>

voidvulnerable_echo() {
    char buffer[128];
    // 假设攻击者输入包含了一段 Shellcode
    read(0, buffer, 512); // 明显的栈溢出，允许写入超长数据
}

intmain() {
    vulnerable_echo();
    return0;
}
```

```
# 开启NX保护（现代Linux默认开启）
gcc -z noexecstack -o vuln vuln.c
```

编译指令参数表

| 场景 | 编译指令组合 | 结果 |
| --- | --- | --- |
| **开启NX (安全)** | `gcc -z noexecstack -o vuln vuln.c` | 栈内存不可执行，Shellcode无法运行。 |
| **关闭NX (危险)** | `gcc -z execstack -fno-stack-protector -no-pie -o vuln vuln.c` | 栈内存可执行，允许直接运行注入的Shellcode。 |

## Ret2Shellcode

Shellcode注入是早期栈溢出攻击的主要手段，攻击者将一段精心构造的机器码直接写入栈上的缓冲区，然后覆盖返回地址指向这段代码的起始位置。然而，现代操作系统引入了NX或DEP机制来防御此类攻击。NX机制将内存页分为“可读/可写”和“可执行”两类，栈和堆通常被标记为不可执行。这意味着即使攻击者成功将Shellcode写入栈中并跳转过去，CPU在尝试执行这些指令时也会抛出异常并终止程序。因此，ret2shellcode技术通常仅在NX保护被关闭（如使用`-z execstack`）的老旧系统或特定配置环境下才有效。

```
#include <stdio.h>
#include <string.h>

voidvulnerable_function() {
    char buffer[64];
    // 明显的栈溢出，且假设环境关闭了NX保护
    gets(buffer);
}

intmain() {
    vulnerable_function();
    return0;
}
```

```
# 必须关闭NX保护，Ret2Shellcode才能生效
gcc -fno-stack-protector -no-pie -z execstack -o ret2shellcode vuln.c
```

## Ret2Text

当NX保护开启，无法在栈上执行Shellcode时，攻击者会将目光转向程序自身的代码段。因为代码段天生就是“可执行”的。Ret2Text的核心逻辑是“程序里自带后门，我直接跳过去用”。如果程序内部恰好包含了一些有用的函数或代码片段（例如题目故意留下的 `system("/bin/sh")` 后门函数），攻击者就可以通过栈溢出，将返回地址直接覆盖为这个后门函数的内存地址。当函数返回时，控制流就会顺理成章地跳转到这个后门函数中执行，从而获取权限。这种方法简单有效，但局限性在于现实中的程序通常不会把这种危险的代码直接写在二进制文件里。

```
#include <stdio.h>
#include <stdlib.h>

// 程序里自带的后门函数 (Ret2Text 的目标)
voidsecret_backdoor() {
    system("/bin/sh");
}

voidnormal_function() {
    char buffer[64];
    gets(buffer); // 漏洞点
}

intmain() {
    normal_function();
    return0;
}
```

```
# 关闭PIE保护，确保后门函数的地址是固定的，方便直接跳转
gcc -fno-stack-protector -no-pie -o ret2text vuln.c
```

## Ret2Libc

如果程序里找不到现成的后门函数，攻击者就会把目光投向系统自带的C标准库（libc）。Ret2Libc的核心逻辑是“程序里没有，我去借用系统库里的强大函数”。几乎所有的程序都会动态链接libc，而libc中包含了 `system`、`execve` 等极其强大的函数。攻击者通过栈溢出，将返回地址覆盖为libc中 `system` 函数的入口地址，并精心构造栈上的数据，将 `"/bin/sh"` 字符串的地址作为参数传递给 `system`。这样一来，程序就会借用系统库的权限执行 `system("/bin/sh")`，从而打开一个Shell。这是现代Linux程序中最常见的利用方式，但通常需要配合泄露内存地址来绕过ASLR。

```
#include <stdio.h>
#include <stdlib.h>

voidnormal_function() {
    char buffer[64];
    // 程序里没有后门，但链接了libc，里面有system函数
    gets(buffer);
}

intmain() {
    normal_function();
    return0;
}
```

```
# 正常编译，开启NX保护，迫使攻击者必须使用Ret2Libc等高级技巧
gcc -fno-stack-protector -no-pie -o ret2libc vuln.c
```

## Ret2CSU

Ret2CSU是Ret2Libc在64位程序下的一种高级辅助技术。它的核心逻辑是“没有传参工具，我自己造一个”。在64位系统中，函数参数是通过寄存器传递的，而不是像32位那样压在栈上。如果程序里找不到像 `pop rdi; ret` 这样能把栈上的数据弹到寄存器里的指令片段，攻击者就无法给 `system` 函数传递 `/bin/sh` 参数。但是，GCC编译器在编译程序时，几乎总是会生成一个名为 `__libc_csu_init` 的初始化函数。这个函数内部包含一段特殊的指令序列，可以依次将特定寄存器的值“弹出”并移动到参数寄存器中。攻击者利用这段代码作为“万能传参跳板”，凑齐参数后，再跳转去执行 `system` 函数。

```
#include <stdio.h>
#include <unistd.h>

voidvuln() {
    char buf[100];
    // 64位程序，如果找不到 pop rdi; ret 等gadgets
    read(0, buf, 200); // 溢出
}

intmain() {
    // __libc_csu_init 依然会被编译器自动生成
    vuln();
    return0;
}
```

```
# 标准编译，Ret2CSU利用的是编译器自动生成的代码片段
gcc -fno-stack-protector -no-pie -o ret2csu vuln.c
```

# 三、格式化字符串漏洞

格式化字符串漏洞源于用户输入被直接作为格式化函数（如`printf`）的格式化字符串参数。当程序执行`printf(user_input)`而非`printf("%s", user_input)`时，攻击者可以通过输入特定的格式化占位符（如`%x`, `%s`, `%n`）来操纵函数的行为。`%x`和`%p`允许攻击者读取栈上的数据，从而泄露Canary值或内存地址，绕过ASLR保护；而最危险的`%n`占位符则允许将“已输出字符的个数”写入到指定内存地址。利用这一特性，攻击者可以修改全局偏移表中的函数指针，将`printf`等函数的地址替换为`system`的地址，或者修改栈上的返回地址，从而在不开启NX的情况下也能实现任意代码执行，其灵活性和危害性往往超过普通的栈溢出。

```
#include <stdio.h>
#include <string.h>

int main() {
    char buffer[100];
    printf("请输入格式化字符串: ");
    fgets(buffer, sizeof(buffer), stdin);
    // 漏洞点：用户输入直接作为格式化字符串
    printf(buffer);
    return 0;
}
```

编译指令参数表

| 保护机制 | 开启指令 | 关闭指令 | 作用描述 |
| --- | --- | --- | --- |
| **FORTIFY\_SOURCE** | `-D_FORTIFY_SOURCE=2` | `-U_FORTIFY_SOURCE` | 检查格式化字符串安全性，阻止向只读段写入（如%n）。 |
| **RELRO** | `-z relro -z now` | `-z norelro` | 将GOT表设为只读，防止利用`%n`修改GOT表。 |

# 四、Fortify 机制

Fortify机制是一种由编译器和C库共同实现的轻量级运行时保护机制，旨在防御常见的缓冲区溢出和格式化字符串攻击。当开启`_FORTIFY_SOURCE`宏时，编译器会将不安全的标准库函数调用（如`strcpy`, `sprintf`, `printf`）替换为带有安全检查的`_chk`版本（如`__strcpy_chk`）。这些增强版函数在运行时会利用编译器内置的对象大小检测功能，计算目标缓冲区的实际容量。如果检测到写入操作即将越界，或者在格式化字符串中检测到试图向只读内存段写入（如使用`%n`），程序会立即调用`__chk_fail`终止运行并报错。虽然它不能完全阻止溢出，但能极大地增加利用难度，是现代Linux发行版默认开启的重要防线。

```
#include <stdio.h>
#include <string.h>

int main() {
    char dest[10];
    // 如果开启FORTIFY，编译器会检查src长度是否超过dest大小
    // 如果溢出，程序会崩溃并提示 "buffer overflow detected"
    strcpy(dest, "This string is definitely too long");
    return 0;
}
```

编译指令参数表

| 级别 | 编译指令 | 效果 |
| --- | --- | --- |
| **Level 2 (推荐)** | `gcc -O2 -D_FORTIFY_SOURCE=2 ...` | 增强检查，包括格式化字符串和更多内存操作检查。 |
| **Level 0 (关闭)** | `gcc -U_FORTIFY_SOURCE ...` | 禁用Fortify保护，允许未检查的函数行为。 |

# 五、总结

构建安全的二进制程序需要采用“纵深防御”策略，全方位筑牢安全防线。在编译环节，应开启全保护选项：使用 `-fstack-protector-strong` 启用Canary保护以对抗栈溢出，配合 `-z noexecstack` 开启NX保护防止Shellcode执行，利用 `-pie -fPIE` 实现ASLR增加攻击难度，并通过 `-z relro -z now` 开启完全RELRO将GOT表设为只读以抵御格式化字符串攻击，同时结合 `-O2 -D_FORTIFY_SOURCE=2` 启用Fortify机制智能拦截危险的缓冲区溢出。在代码编写层面，必须杜绝使用 `gets`、`strcpy` 等不安全函数，改用带有长度限制的 `fgets`、`snprintf`，并严格规范 `printf` 的调用格式。此外，还需保持操作系统与编译器的及时更新，并开启系统级的ASLR防护，从而在编译、编码和运行环境三个维度上最大程度地消除潜在的安全隐患。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

书中自有代码来

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

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