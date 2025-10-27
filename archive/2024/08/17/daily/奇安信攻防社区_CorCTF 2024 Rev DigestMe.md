---
title: CorCTF 2024 Rev DigestMe
url: https://forum.butian.net/share/3662
source: 奇安信攻防社区
date: 2024-08-17
fetch_date: 2025-10-06T18:04:11.224020
---

# CorCTF 2024 Rev DigestMe

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### CorCTF 2024 Rev DigestMe

* [CTF](https://forum.butian.net/topic/52)

本题为一个CorCTF中的digestme题目的wp，这是一个自制的特殊VM逆向，整个逆向过程一波三折，最后还需要用到Cuda来完成最后的收尾，也还算有趣

题目的谜面如下
> FizzBuzz101 was innocently writing a new, top-secret compiler when his computer was Crowdstriked. Worse, the recovery key is behind a hasher that he wrote and compiled himself, and he can't remember how the bits work! Can you help him get his life's work back?
总的来说，题目\*\*本质上是一个hash算法\*\*（笔者做题的时候无视了这个提示，后面吃了大亏）。
把文件下载下来以后，粗略看一下，会发现题目是非常简单的C代码，但是如果尝试f5会发现提示函数过大
![func01.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-d31e6bfc30ee3d3246af95de631db9c202767a43.png)
观察了一下，代码范围从`0x1090`到`0xED97F`，足足九十万行汇编。这么多的汇编，一看就没办法正常的进行分析了，这种题目就要开始学会取巧，使用各种各样的技巧尝试简化这个分析过程。
### 读题：简化逻辑
我们会发现，程序分成两部分，一部分是大量的重复操作：
```php
.text:0000000000001758 mov cl, [rax+0FA7h]
.text:000000000000175E or cl, [rax+107h]
.text:0000000000001764 mov [rax+7], cl
.text:0000000000001767 mov cl, [rax+0FA8h]
.text:000000000000176D or cl, [rax+108h]
.text:0000000000001773 mov [rax+8], cl
.text:0000000000001776 mov cl, [rax+0FA9h]
.text:000000000000177C or cl, [rax+109h]
.text:0000000000001782 mov [rax+9], cl
.text:0000000000001785 mov cl, [rax+0FAAh]
.text:000000000000178B or cl, [rax+10Ah]
.text:0000000000001791 mov [rax+0Ah], cl
```
另一部分是在程序开头比较普通的处理逻辑：
```php
.text:0000000000001090
.text:0000000000001090 ; \_\_unwind {
.text:0000000000001090 push r15
.text:0000000000001092 lea rdi, s ; "Welcome!\nPlease enter the flag here: "
.text:0000000000001099 push r14
.text:000000000000109B lea r14, aCorctf ; "corctf{"
.text:00000000000010A2 push r13
.text:00000000000010A4 xor r13d, r13d
.text:00000000000010A7 push r12
.text:00000000000010A9 mov r12d, 80000000h
.text:00000000000010AF push rbp
.text:00000000000010B0 push rbx
.text:00000000000010B1 sub rsp, 498h
.text:00000000000010B8 call \_puts
.text:00000000000010BD mov esi, 186A0h ; size
.text:00000000000010C2 mov edi, 1 ; nmemb
.text:00000000000010C7 lea rbx, [rsp+4C8h+var\_418]
.text:00000000000010CF call \_calloc
.text:00000000000010D4 lea rbp, [rsp+4C8h+s]
.text:00000000000010DC mov r15, rax
.text:00000000000010DF call \_\_\_ctype\_b\_loc
.text:00000000000010E4 mov [rsp+4C8h+var\_4C8], rax
.text:00000000000010E8 lea rax, [rsp+4C8h+s+8]
.text:00000000000010F0 mov [rsp+4C8h+var\_4C0], rax
```
那么这里有一个技巧：可以试着将程序中间的某处patch 成`ret`，阻断ida对后续逻辑的分析，这样我们就能尝试用f5简单看看程序逻辑。当我们处理后，可以得到这样的逻辑:
```C
int main()
{
char s[1000];
char\* v17 = &s[16];
size\_t v4; // rax
puts("Welcome!\nPlease enter the flag here:");
char\* v3 = calloc(1, 0x186a0);
// while ( 1 )
// {
memset(v17, 0, sizeof(v17));
fgets(s, 999, stdin);
v4 = strcspn(s, "\n");
puts("Welcome!\nPlease enter the flag here: ");
v3 = calloc(1uLL, 0x186A0uLL);
v14 = \_\_ctype\_b\_loc();
while ( 1 )
{
memset(s, 0, sizeof(s));
fgets(s, 999, stdin);
v4 = strcspn(s, "\n");
s[v4] = 0;
if ( !memcmp("corctf{", s, 7uLL) && v4 > 1 && s[v4 - 1] == '}' && s[8] == s[17] && s[9] == s[11] )
{
v5 = s[7];
if ( s[7] == s[16] + 1 && s[14] == s[16] + 4 )
{
v6 = &s[8];
v7 = v3 + 0x940;
v8 = \*v14;
if ( ((\*v14)[s[7]] & 8) != 0 )
break;
}
}
LABEL\_14:
puts("Try again: ");
}
while ( 1 )
{
v9 = v7;
v10 = 7;
do
{
v11 = v5 >> v10--;
\*v9 = v11;
\*v9++ &= 1u;
}
while ( v10 != -1 );
v7 += 8;
if ( &s[18] == v6 )
break;
v5 = \*v6++;
if ( (v8[(char)v5] & 8) == 0 )
goto LABEL\_14;
}
v3[2456] = 1;
for ( i = 0LL; i != 64; ++i )
v3[i + 2816] = ((0x8000000000000000LL >> i) & 0x5800000000000000LL) != 0;
result = v3;
}
v3[319] = 1;
v3[318] = 1;
v3[317] = 1;
v3[316] = 1;
v3[315] = 1;
v3[314] = 1;
v3[313] = 1;
v3[312] = 1;
v3[311] = 1;
v3[310] = 1;
v3[309] = 1;
v3[308] = 1;
v3[307] = 1;
```
根据上述代码，首先可以总结出如下结论
- 初始化了一个巨大的内存空间，我们后文将会将其定义为`tmp`，在这里叫做`v3`
- 读入的字符串开头是`corctf{`，最后一个字符是`}`，这个题目中有直接体现
直接明文写在代码中，所以非常容易理解。然后，我们注意到有几个类似于字符串的约束关系
```C
s[8] == s[17]
s[9] == s[11]
s[7] == s[16] + 1
s[14] == s[16] + 4
```
而且我们会观察到，这个约束范围涉及的字符串从`s[7]~s[17]`，此时可以知道
- 输入\*\*至少有18个字符是有效字符\*\*
然后最后的循环中，我们还能看到一个循环边界
```cpp
if ( &s[18] == v6 )
break;
```
这个v6来自于`&s[8]`，并且在循环中不断自增，其本质上为指向输入的指针，那么此时可以得出结论
- 读入的字符串长度大概率是19个字节，因为程序的循环有一处`&s[18]`用于描述循环的中断，这种中断大概率就是表示\*\*字符串的处理结束\*\*
此时我们就知道了flag的长度，然后接下来的逻辑就有一点匪夷所思，因为它不断地尝试的进行01的赋值
```cpp
v3[317] = 1;
v3[316] = 1;
v3[315] = 1;
v3[314] = 1;
v3[313] = 1;
v3[312] = 1;
v3[311] = 1;
v3[310] = 1;
```
并且下文中包含大量的重复加法或者异或操作
```cpp
v3[4099] = 0;
v3[4098] = 0;
v3[4097] = 0;
v3[4096] = 0;
\*v3 = v3[256] | v3[4000];
v3[1] = v3[257] | v3[4001];
v3[2] = v3[258] | v3[4002];
```
根据前文内容，`v3`整段内存都被提前初始化成了0，而且`v3[4000]`也是0，那么理论上这个`\*v3 = v3[256] | v3[4000];`其实是无用的逻辑，这里笔者产生了一种想法
> 可能\*\*可以利用gcc对一些无用逻辑进行优化\*\*
具体做法就是：将当前反汇编的代码编写成有效的C代码，然后将当前的C代码进行编译，\*\*使用gcc的规则替我们进行无用代码的删除\*\*
然而这个想法其实有缺陷的，毕竟我们没有办法将所有逻辑都罗列出来，所以gcc的优化存在一定的不足。最后优化的结果也是果然不太行，优化后的结果如下
```cpp
\*((\_QWORD \*)v3 + 254) = 0x10100000000LL;
\*((\_QWORD \*)v3 + 258) = 0x101010100010101LL;
v17 = 16777473;
\*((\_QWORD \*)v3 + 260) = 0x100000001000101LL;
v3[1951] = 1;
\*((\_DWORD \*)v3 + 486) = 0x10001;
\*((\_WORD \*)v3 + 974) = 1;
v3[1950] = 1;
\*((\_QWORD \*)v3 + 245) = 65537LL;
```
将一些01进行合并后，逻辑变得更加混乱，感觉并没有办法进行逻辑分析，只能放弃这种简化策略。
如果优化不管用，就意味着程序有另一种分析策略，就是汇编存在一定的规律，毕竟出题人不可能自己手搓超长汇编，这就意味着汇编的逻辑\*\*存在某种循环\*\*。我们这里展示一段汇编
```php
.text:0000000000001290 mov byte ptr [rax+13Fh], 1
.text:0000000000001297 mov byte ptr [rax+13Eh], 1
.text:000000000000129E mov byte ptr [rax+13Dh], 1
.text:00000000000012A5 mov byte ptr [rax+13Ch], 1
.text:00000000000012AC mov byte ptr [rax+13Bh], 1
.text:00000000000012B3 mov byte ptr [rax+13Ah], 1
.text:00000000000012BA mov byte ptr [rax+139h], 1
.text:00000000000012C1 mov byte ptr [rax+138h], 1
.text:00000000000012C8 mov byte ptr [rax+137h], 1
.text:00000000000012CF mov byte ptr [rax+136h], 1
.text:00000000000012D6 mov byte ptr [rax+135h], 1
.text:00000000000012DD mov byte ptr [rax+134h], 1
.text:00000000000012E4 mov byte ptr [rax+133h], 1
.text:00000000000012EB mov byte ptr [rax+132h], 1
.text:00000000000012F2 mov byte ptr [rax+131h], 1
.text:00000000000012F9 mov byte ptr [rax+130h], 1
.text:0000000000001300 mov byte ptr [rax+12Fh], 1
.text:0000000000001307 mov byte ptr [rax+12Eh], 1
.text:000000000000130E mov byte ptr [rax+12Dh], 1
.text:0000000000001315 mov byte ptr [rax+12Ch], 1
.text:000000000000131C mov byte ptr [rax+12Bh], 1
.text:0000000000001323 mov byte ptr [rax+12Ah], 1
.text:000000000000132A mov byte ptr [rax+129h], 1
.text:0000000000001331 mov byte ptr [rax+128h], 1
.text:0000000000001338 mov byte ptr [rax+127h], 1
.text:000000000000133F mov byte ptr [rax+126h], 1
.text:0000000000001346 mov byte ptr [rax+125h], 1
.text:000000000000134D mov byte ptr [rax+124h], 1
.text:0000000000001354 mov byte ptr [rax+123h], 1
.text:000000000000135B mov byte ptr [rax+122h], 1
.text:0000000000001362 mov byte ptr [rax+121h], 1
.text:0000000000001369 mov byte ptr [rax+120h], 1
.text:0000000000001370 mov byte ptr [rax+0FBFh], 0
```
仔细观察，会发现一个规律：这个赋值的过程中，`rax+13F`到`rax+120`之间，\*\*正好进行了32个0的赋值\*\*。而我们观察后文后，发现\*\*至少也是按照8字节进行操作的循环\*\*，所以我们可以得出两种结论：
- 程序可能是以8 bit（一字节）为操作最小单元
- 程序可能是以32 bit（四字节）为操作最小单元
进一步读汇编后，会发现汇编存在三种类型
- 将两个32字节连续的内存空间进行或处理
- 将两个32字节连续的内存空间进行与处理
- 将两个32字节连续的内存空间进行异或处理
- 将两个32字节连续的内存空间进行或/与/异或处理，同时混入`0B40h`和`0B41h`进行操作
前几种可以理解，应该是对两段内存空间进行与/或/异或处理，最后一个是什么逻辑呢？我们取出一小段分析
```php
.text:0000000000005DE9 mov [rax+9Fh], cl
.text:0000000000005DEF mov cl, [rax+87h]
.text:0000000000005DF5 xor cl, [rax+7]
.text:0000000...