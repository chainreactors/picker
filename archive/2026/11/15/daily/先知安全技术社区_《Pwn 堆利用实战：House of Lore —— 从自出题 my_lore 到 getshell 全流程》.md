---
title: 《Pwn 堆利用实战：House of Lore —— 从自出题 my_lore 到 getshell 全流程》
url: https://xz.aliyun.com/news/93334
source: 先知安全技术社区
date: 2026-11-15
fetch_date: 2026-11-16T08:47:55.566098
---

# 《Pwn 堆利用实战：House of Lore —— 从自出题 my_lore 到 getshell 全流程》

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# 《Pwn 堆利用实战：House of Lore —— 从自出题 my\_lore 到 getshell 全流程》

[![](https://xzfile.aliyuncs.com/2026/11/06/1256/fbe74378-5ff.jpg)SogwCat](/users/176804)·2026-11-15 15:20·12 分钟·14·河南·二进制安全

📎my\_ lore.zip how2heap 里的 house\_of\_lore demo 只打印一句 Nice jump d00d，fake chunk 还摆在栈上 —— 学完依然不知道真实题目里这套技巧怎么落地。为此我自己写了一道题 my\_lore（No PIE / glibc 2.23-0ubuntu10），把&#34;BSS 上的函数指针 hook&#34;和&#34;可控缓冲区 name[…

[📎my\_](https://www.yuque.com/attachments/yuque/0/2026/zip/63608051/1794491191855-2f35b097-abe2-4ef6-84ca-a27d1569f850.zip)[lore.zip](http://lore.zip)

how2heap 里的 house\_of\_lore demo 只打印一句 Nice jump d00d，fake chunk 还摆在栈上 —— 学完依然不知道真实题目里这套技巧怎么落地。为此我自己写了一道题 my\_lore（No PIE / glibc 2.23-0ubuntu10），把"BSS 上的函数指针 hook"和"可控缓冲区 name[0x100]"故意摆成相邻布局，然后用一条完整的利用链把它打穿。

全文按"漏洞 → 原理 → 布局 → 动态验证 → getshell"推进：先用 free 不清空指针拿到 UAF、用不限长的 edit 改 A->bk；再回到 glibc 源码，看清 smallbin 是从尾部取块、且只校验一条回链（bck->fd == victim）；接着在 name 尾部伪造 chunk、用两次 malloc(0x100) 让第二次的返回值精确落在 hook - 0x10，写入 system 后由 run 触发 system("/bin/sh")。

除了 exp，文中还拆开了几个容易含糊的点：为什么 setname 刚好差 1 个字节写不到 hook、为什么 free 之后 rdi 会变成 main\_arena、fake->bk 为什么不能指向自己、以及每一步在 gdb 里的检查点（bins / x/2gx / p/x $rax）。最终实测拿到 uid=1000(bgl1)。

# 0.知识点的补充

### 1.释放的堆块距离链表头的远近

只有unsorted bin和small bin满足fifo这条规律，所以这两个bin满足，最先进来的距离表头最远；

我们这里只是口头说一下，大家可能记忆不是那么深刻，我们直接用上一个例题，my\_force进行演示一下；

unsorted bin

```
c
1
1280
1
32                //挡板，防止，我们释放堆块0和堆块2的时候合并
1
1280
1
32               //挡板，防止释放的堆块和top chunk合并
heap
```

【你应该看到】

```
Addr: 0x405000
Size: 0x510 (with flag bits: 0x511)

Allocated chunk | PREV_INUSE
Addr: 0x405510
Size: 0x30 (with flag bits: 0x31)

Allocated chunk | PREV_INUSE
Addr: 0x405540
Size: 0x510 (with flag bits: 0x511)

Allocated chunk | PREV_INUSE
Addr: 0x405a50
Size: 0x30 (with flag bits: 0x31)
```

【释放】

```
c
4
0
4
2
heap
```

【你应该看到】

```
Free chunk (unsortedbin) | PREV_INUSE
Addr: 0x405000
Size: 0x510 (with flag bits: 0x511)
fd: 0x7ffff7bc4b78
bk: 0x405540

Allocated chunk
Addr: 0x405510
Size: 0x30 (with flag bits: 0x30)

Free chunk (unsortedbin) | PREV_INUSE
Addr: 0x405540
Size: 0x510 (with flag bits: 0x511)
fd: 0x405000
bk: 0x7ffff7bc4b78

Allocated chunk
Addr: 0x405a50
Size: 0x30 (with flag bits: 0x30)

Top chunk | PREV_INUSE
Addr: 0x405a80
Size: 0x20580 (with flag bits: 0x20581)
```

此时我们查看一下bins

【bins】

```
fastbins
empty
unsortedbin
all: 0x405540 —▸ 0x405000 —▸ 0x7ffff7bc4b78 ◂— 0x405540 /* '@U@' */
smallbins
empty
largebins
empty
```

看到没，我们最先释放的那个堆块0距离链表头最远；

### 2.释放的堆块进入top chunk的情况：

前提条件：被释放的堆块紧邻top；

块大小>0x80（也就是不在fastbin范围）

2.26以及以上，tcache已满，或该大小没有tcache栈；

### 3.malloc的时候在本漏洞中做了什么

```
victim = last(bin);              /* ① victim = bin->bk = A */
bck    = victim->bk;             /* ② bck = A->bk = fake */

if (bck->fd != victim)           /* ③ 检查 fake->fd 是否等于 A */
    malloc_printerr("corrupted");

set_inuse_bit_at_offset(victim, nb);   /* ④ 标记 A 已使用 */

bin->bk = bck;                   /* ⑤ bin->bk = fake    尾部变了！ */
bck->fd = bin;                   /* ⑥ fake->fd = bin    fake 的 fd 被改写！ */

return chunk2mem(victim);        /* ⑦ 返回 A + 0x10 = A 的用户指针 */
```

# 2.静态分析

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  __int64 size; // [rsp+8h] [rbp-28h]
  int v5; // [rsp+14h] [rbp-1Ch]
  __int64 nbytes; // [rsp+18h] [rbp-18h]
  unsigned int v7; // [rsp+20h] [rbp-10h]
  unsigned int v8; // [rsp+24h] [rbp-Ch]
  unsigned int v9; // [rsp+28h] [rbp-8h]
  int v10; // [rsp+2Ch] [rbp-4h]

  setvbuf(_bss_start, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  puts("=====================================");
  puts("  my_lore : House of Lore lab");
  puts("=====================================");
  printf("[*] name = %p\n", &blob);
  printf("[*] hook = %p\n", &qword_4042A0);
  printf("[*] cmd  = %p\n", &cmd);
  while ( 1 )
  {
    while ( 1 )
    {
      while ( 1 )
      {
        while ( 1 )
        {
          while ( 1 )
          {
            while ( 1 )
            {
              while ( 1 )
              {
                printf("1. alloc\n2. edit\n3. show\n4. free\n5. setname\n6. setcmd\n7. run\n8. quit\n> ");
                v10 = read_int(0);
                if ( v10 != 1 )
                  break;
                v5 = slot_alloc();
                if ( v5 >= 0 )
                {
                  size = read_size("size: ");
                  if ( size )
                  {
                    ptrs[v5] = malloc(size);
                    sizes[v5] = size;
                    printf("[%d] = %p (size=%zu)\n", v5, (const void *)ptrs[v5], size);
                    printf("data: ");
                    read(0, (void *)ptrs[v5], size);
                  }
                  else
                  {
                    puts("[-] bad size");
                  }
                }
                else
                {
                  puts("[-] full");
                }
              }
              if ( v10 != 2 )
                break;
              v7 = read_int("idx: ");
              nbytes = read_size("len: ");
              if ( v7 >= 0x10 || !ptrs[v7] )
                goto LABEL_21;
              printf("data: ");
              read(0, (void *)ptrs[v7], nbytes);
              puts(&byte_402122);
            }
            if ( v10 != 3 )
              break;
            v8 = read_int("idx: ");
            if ( v8 >= 0x10 || !ptrs[v8] )
              goto LABEL_21;
            write(1, (const void *)ptrs[v8], sizes[v8]);
            puts(&byte_402122);
          }
          if ( v10 != 4 )
            break;
          v9 = read_int("idx: ");
          if ( v9 < 0x10 && ptrs[v9] )
            free((void *)ptrs[v9]);
          else
LABEL_21:
            puts("[-] bad idx");
        }
        if ( v10 != 5 )
          break;
        printf("name: ");
        read(0, &blob, 0x100u);
        puts(&byte_402122);
      }
      if ( v10 != 6 )
        break;
      printf("cmd: ");
      read(0, &cmd, 0x3Fu);
      byte_4042FF = 0;
      puts(&byte_402122);
    }
    if ( v10 != 7 )
      return 0;
    if ( qword_4042A0 )
      qword_4042A0(&cmd);
    else
      puts("[*] hook is NULL");
  }
}
```

这个函数也是相对简单，里面存在两个漏洞；

漏洞一：在43到48行这里，这里的是一个堆溢出的漏洞

漏洞二：80到81行，这里存在uaf；

### 题目漏洞利用思路：

其实，这道题我们可以看出来，和之前的自命题不同的是多了一些不同的选项：书名，cmd，run；其实这是为了，专门进行练习这道题目写的；我们来详细看看

```
.bss:0000000000404120                                         ; main+327↑o
.bss:00000000004041A0 blob            db    ? ;               ; DATA XREF: main+75↑o
.bss:00000000004041A0                                         ; main+404↑o
.bss:00000000004041A1                 db    ? ;
.bss:00000000004041A2                 db    ? ;
.bss:00000000004041A3                 db    ? ;

......

.bss:0000000000404296                 db    ? ;
.bss:0000000000404297                 db    ? ;
.bss:0000000000404298                 db    ? ;
.bss:0000000000404299                 db    ? ;
.bss:000000000040429A                 db    ? ;
.bss:000000000040429B                 db    ? ;
.bss:000000000040429C                 db    ? ;
.bss:000000000040429D                 db    ? ;
.bss:000000000040429E                 db    ? ;
.bss:000000000040429F                 db    ? ;
.bss:00000000004042A0 ; __int64 (__fastcall *qword_4042A0)(_QWORD)
.bss:00000000004042A0 qword_4042A0    dq ?                    ; DATA XREF: main+93↑o
.bss:00000000004042A0                                         ; main+480↑r ...
.bss:00000000004042A8                 align 20h
.bss:00000000004042C0 cmd             db    ? ;               ; DATA XREF: main+B1↑o
.bss:00000000004042C0                                         ; main+44B↑o ...
.bss:00000000004042C1                 db    ? ;
.bss:00000000004042C2                 db    ? ;
.bss:00000000004042C3                 db    ? ;
.bss:00000000004042C4                 db    ? ;
.bss:00000000004042C5                 db    ? ;
.bss:00000000004042C6                 db    ? ;
.bss:00000000004042C7...