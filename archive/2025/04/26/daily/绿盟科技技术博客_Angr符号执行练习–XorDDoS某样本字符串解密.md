---
title: Angr符号执行练习–XorDDoS某样本字符串解密
url: https://blog.nsfocus.net/angr-3/
source: 绿盟科技技术博客
date: 2025-04-26
fetch_date: 2025-10-06T22:06:29.204149
---

# Angr符号执行练习–XorDDoS某样本字符串解密

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Angr符号执行练习–XorDDoS某样本字符串解密

### Angr符号执行练习–XorDDoS某样本字符串解密

[2025-04-25](https://blog.nsfocus.net/angr-3/ "Angr符号执行练习–XorDDoS某样本字符串解密")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 3,085

目录:

☆ XorDDoS某样本
☆ 用r2pipe模块静态分析
1) 获取函数入口/出口地址
2) 获取到指定函数的交叉引用
3) 析取dec\_conf()的参数
4) static\_analyses()
☆ 用angr模拟调用dec\_conf()
1) proj.factory.call\_state
2) proj.factory.callable
☆ r2pipe+angr
☆ 用angr模拟调用encrypt\_code()
☆ 后记

————————————————————————–

☆ XorDDoS某样本

参看

————————————————————————–
XorDDoS僵尸网络家族的某样本
https://www.virustotal.com/gui/file/0e9e859d22b009e869322a509c11e342
https://www.virustotal.com/gui/file/cad80071b9af3fa742ec7fbbeae0e2ffe2566742b20bfdf436b8138da3fd20e9
————————————————————————–

有VirusTotal企业账号的，可下载该ELF样本，也可尝试从微步在线下载。

$ file -b 0e9e859d22b009e869322a509c11e342
ELF 32-bit LSB executable, Intel 80386, …, statically linked, …, not stripped

用IDA32反汇编，样本没有strip，留有调试符号。

————————————————————————–
0804CFA3 C7 44 24 08 0B 00 00 00 mov dword ptr [esp+8], 0Bh
0804CFAB C7 44 24 04 B1 2F 0B 08 mov dword ptr [esp+4], offset aM7a4nqNa\_0 ; “m7A4nQ\_/nA”
0804CFB3 8D 85 B3 EA FF FF lea eax, [ebp+var\_154D]
0804CFB9 89 04 24 mov [esp], eax
0804CFBC E8 67 B2 FF FF call dec\_conf
0804CFC1 C7 44 24 08 07 00 00 00 mov dword ptr [esp+8], 7
0804CFC9 C7 44 24 04 BC 2F 0B 08 mov dword ptr [esp+4], offset aMN3\_0 ; “m [(n3”
0804CFD1 8D 85 B3 E9 FF FF lea eax, [ebp+var\_164D]
0804CFD7 89 04 24 mov [esp], eax
0804CFDA E8 49 B2 FF FF call dec\_conf
————————————————————————–
dec\_conf(v23, “m7A4nQ\_/nA”, 11);
dec\_conf(v22, “m [(n3”, 7);
dec\_conf(v21, “m6\_6n3”, 7);
dec\_conf(v19, aM4s4nacNZv, 18);
dec\_conf(v18, aMN4C, 17);
dec\_conf(v17, “m.[$n3”, 7);
dec\_conf(v16, a6f6, 512);
dec\_conf(v20, “m4S4nAC/nA”, 11);
————————————————————————–

样本含有一些加密字符串，dec\_conf()用于解密字符串。

————————————————————————–
08048228 dec\_conf proc
08048228 55 push ebp
08048229 89 E5 mov ebp, esp
0804822B 83 EC 18 sub esp, 18h
0804822E 8B 45 10 mov eax, [ebp+arg\_8]
08048231 89 44 24 08 mov [esp+8], eax
08048235 8B 45 0C mov eax, [ebp+arg\_4]
08048238 89 44 24 04 mov [esp+4], eax
0804823C 8B 45 08 mov eax, [ebp+arg\_0]
0804823F 89 04 24 mov [esp], eax
08048242 E8 09 E6 01 00 call memmove
08048247 8B 45 10 mov eax, [ebp+arg\_8]
0804824A 89 44 24 04 mov [esp+4], eax
0804824E 8B 45 08 mov eax, [ebp+arg\_0]
08048251 89 04 24 mov [esp], eax
08048254 E8 9B 11 00 00 call encrypt\_code
08048259 B8 00 00 00 00 mov eax, 0
0804825E C9 leave
0804825F C3 retn
0804825F dec\_conf endp
————————————————————————–
int dec\_conf(char \*dst, char \*src, int size )
{
memmove( dst, src, size );
/\*
\* 就地修改dst，而非返回什么
\*/
encrypt\_code( dst, size );
return 0;
}
————————————————————————–

dst用于保存解密结果，src是固化在.rodata中的加密数据，size对应src的长度。
dec\_conf()实际调用encrypt\_code()完成解密。

————————————————————————–
/\*
\* 就地修改buf
\*/
char \*\_\_cdecl encrypt\_code(char \*buf, int size)
{
char \*p;
int i;

p = buf;
for ( i = 0; i < size; ++i )
\*p++ ^= xorkeys[i % 16];
return buf;
}
————————————————————————–
080CF3E8 42 42 32 46 41 33 36 41…xorkeys db ‘BB2FA36AAA9541F0’
————————————————————————–

encrypt\_code()并不复杂，就是简单异或，xorkeys内置在ELF中，固定。但我们假设
encrypt\_code()很复杂，比如被控制流平坦化过，不想静态分析其逻辑，准备用angr
模拟调用dec\_conf()或encrypt\_code()，黑盒调用，只关心in/out。

样本不只调用dec\_conf()解密字符串，也会直接调用encrypt\_code()解密字符串。下
面是几处直接调用encrypt\_code()解密字符串的地方:

————————————————————————–
08048C08 C7 44 24 08 0A 00 00 00 mov dword ptr [esp+8], 0Ah
08048C10 C7 44 24 04 07 2D 0B 08 mov dword ptr [esp+4], offset aM7a4nqNa ; “m7A4nQ\_/nA”
08048C18 8D 85 F1 FA FF FF lea eax, [ebp+var\_50F]
08048C1E 89 04 24 mov [esp], eax
08048C21 E8 2A DC 01 00 call memmove
08048C26 C7 44 24 04 0A 00 00 00 mov dword ptr [esp+4], 0Ah ; int
08048C2E 8D 85 F1 FA FF FF lea eax, [ebp+var\_50F]
08048C34 89 04 24 mov [esp], eax ; char \*
08048C37 E8 B8 07 00 00 call encrypt\_code
————————————————————————–
0804F12F C7 44 24 08 00 02 00 00 mov dword ptr [esp+8], 200h
0804F137 C7 44 24 04 4C 32 0B 08 mov dword ptr [esp+4], offset unk\_80B324C
0804F13F C7 04 24 C0 1C 0D 08 mov dword ptr [esp], offset remotestr
0804F146 E8 05 77 01 00 call memmove
0804F14B C7 44 24 04 00 02 00 00 mov dword ptr [esp+4], 200h ; int
0804F153 C7 04 24 C0 1C 0D 08 mov dword ptr [esp], offset remotestr ; char \*
0804F15A E8 95 A2 FF FF call encrypt\_code
————————————————————————–
memmove(remotestr, &unk\_80B324C, 512);
encrypt\_code(remotestr, 512);
————————————————————————–
0804D093 C7 45 CC 00 00 00 00 mov [ebp+var\_34], 0
0804D09A EB 26 jmp short loc\_804D0C2
0804D09C
0804D09C loc\_804D09C:
0804D09C 8B 55 CC mov edx, [ebp+var\_34]
0804D09F 89 D0 mov eax, edx
0804D0A1 C1 E0 02 shl eax, 2
0804D0A4 01 D0 add eax, edx
0804D0A6 C1 E0 02 shl eax, 2
/\*
\* daemonname位于.data，而非.rodata
\*/
0804D0A9 05 20 F1 0C 08 add eax, offset daemonname ; “!#Ff3VE.-7″
0804D0AE C7 44 24 04 14 00 00 00 mov dword ptr [esp+4], 14h ; int
0804D0B6 89 04 24 mov [esp], eax ; char \*
0804D0B9 E8 36 C3 FF FF call encrypt\_code
0804D0BE 83 45 CC 01 add [ebp+var\_34], 1
0804D0C2
0804D0C2 loc\_804D0C2:
0804D0C2 83 7D CC 16 cmp [ebp+var\_34], 16h
0804D0C6 76 D4 jbe short loc\_804D09C
————————————————————————–
for ( i = 0; i <= 22; ++i )
encrypt\_code(&daemonname[20 \* i], 20);
————————————————————————–

还有其他调用encrypt\_code()解密字符串的地方，但那些地方都是动态提供输入，不
是固定串，此处略过。

☆ 用r2pipe模块静态分析

关于r2pipe模块，参看

《Angr符号执行练习–SecuInside 2016 mbrainfuzz》
https://scz.617.cn/unix/202503311347.txt

1) 获取函数入口/出口地址

将来angr模拟调用dec\_conf()，至少有两种方案。一种需要知道函数入口/出口地址，
另一种只需知道函数入口地址。

————————————————————————–
def get\_func\_info ( r2, func ) :
cmd = f”afij sym.{func}”
info = r2.cmd( cmd )
info = json.loads( info )
info = info[0]
func\_entry = info[‘offset’]
func\_exit = info[‘offset’] + info[‘size’] – 1
return ( func\_entry, func\_exit )
————————————————————————–

假设已打开r2句柄，此处简化处理，假设ret是最后一条指令。

2) 获取到指定函数的交叉引用

样本调用dec\_conf()的模式是固定的，只要找到”call dec\_conf”指令所在地址，可
从附近的汇编指令析取dec\_conf()的参数，比如加密字符串的地址、长度。通过交叉
引用找出所有”call dec\_conf”指令所在地址。

————————————————————————–
def find\_xrefs\_to\_func ( r2, func ) :
xrefs = []
cmd = f”axtj sym.{func}”
#
# 返回str
#
info = r2.cmd( cmd )
#
# 返回list
#
info = json.loads( info )
for item in info :
xrefs.append( item[‘from’] )
return xrefs
————————————————————————–

3) 析取dec\_conf()的参数

————————————————————————–
def get\_call\_params ( r2, calladdr ) :
cmd = f”pdj -4 @ {calladdr}”
info = r2.cmd( cmd )
info = json.loads( info )
return ( info[1][‘val’], info[0][‘val’] )
————————————————————————–

此实现只针对调用dec\_conf()的情形，意思是，从”call dec\_conf”向低址方向移动
四条指令，反汇编这四条指令，分别析取第二条、第一条指令的立即数。

————————————————————————–
0804CFA3 C7 44 24 08 0B 00 00 00 mov dword ptr [esp+8], 0Bh
0804CFAB C7 44 24 04 B1 2F 0B 08 mov dword ptr [esp+4], offset aM7a4nqNa\_0 ; “m7A4nQ\_/nA”
0804CFB3 8D 85 B3 EA FF FF lea eax, [ebp+var\_154D]
0804CFB9 89 04 24 mov [esp], eax
0804CFBC E8 67 B2 FF FF ca...