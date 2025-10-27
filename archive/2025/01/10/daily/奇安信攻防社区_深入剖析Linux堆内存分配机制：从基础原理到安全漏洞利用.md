---
title: 深入剖析Linux堆内存分配机制：从基础原理到安全漏洞利用
url: https://forum.butian.net/share/4032
source: 奇安信攻防社区
date: 2025-01-10
fetch_date: 2025-10-06T20:05:56.884029
---

# 深入剖析Linux堆内存分配机制：从基础原理到安全漏洞利用

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

### 深入剖析Linux堆内存分配机制：从基础原理到安全漏洞利用

* [渗透测试](https://forum.butian.net/topic/47)

堆（Heap）是一个用于动态内存分配的数据结构，进程可以在运行时通过系统调用（如 malloc 和 free）向操作系统请求和释放内存。堆与栈不同，栈是用于自动变量的快速内存分配，而堆则用于需要灵活大小和生存期的动态数据

堆介绍
===
堆（Heap）是一个用于动态内存分配的数据结构，进程可以在运行时通过系统调用（如 malloc 和 free）向操作系统请求和释放内存。堆与栈不同，栈是用于自动变量的快速内存分配，而堆则用于需要灵活大小和生存期的动态数据
程序可以使用如malloc、calloc、realloc等函数在堆上动态分配内存。当内存不再需要时，使用free函数释放，如下面这个程序
```php
int main(int argc, char \*\*argv)
{
struct data \*d;
d = malloc(sizeof(struct data));
}
```
通过malloc函数分配的堆地址：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c12213dc7496727facf9fba62420c9e3d6511cdd.png)
堆的工作方式
======
用以下程序来展示堆的工作方式
```php
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>
struct data { #定义了一个名为data的结构体
char name[64]; #包含一个64字节大小的字符数组name
};
struct fp { #定义了一个名为fp的结构体
int (\*fp)(); #包含了一个函数指针fp
};
void winner() #自定义函数winner
{
printf("level passed\n"); #输出level passed
}
void nowinner() #自定义函数nowinner
{
printf("level has not been passed\n"); #输出level has not been passed
}
int main(int argc, char \*\*argv) #主函数，从命令行获取参数
{
struct data \*d; #声明了一个指向 struct data 类型结构体的指针 d
struct fp \*f; #声明了一个指向 struct fp 类型结构体的指针 f
d = malloc(sizeof(struct data)); #给data结构体分配内存
f = malloc(sizeof(struct fp)); #给fp结构体分配内存
f->fp = nowinner; #fp结构体中的函数指针初始化为指向nowinner函数
printf("data is at %p, fp is at %p\n", d, f); #输出data和fp结构体的内存地址
strcpy(d->name, argv[1]); #strcpy函数将命令行提供的第一个参数，复制到data结构体的name数组中
f->fp(); #调用函数指针指向的函数nowinner
}
```
在第一个malloc函数调用的地方下一个断点，然后执行到断点处，来看看堆是怎么运行的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-6ed5c4a55e9bc70f8649aa2f7fce2f1c49482a66.png)
现在停在了malloc函数处，还没有执行该指令，可以看到程序空间里是没有堆的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-ca88c2fff887ad55dde4898b0101080ae3f1758b.png)
输入n执行malloc函数，再次查看程序空间
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-601886c466fd502fcf1c5501af5b2abf7472def2.png)
可以看到，多出了一个heap空间，也就是堆，地址是0x804a000-0x806b000，查看这个堆空间里的数据
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4f80759c41ea22b07c9c93e3b41cd9f1321d3e7a.png)
现在堆里只有两个数据，0x49-1，0x48是第一个mallco函数给我们分配的空间大小，为什么要减一呢，因为在这个堆中保存数据是，为了区分是否是空闲区域，都会在表示大小的值后面加一个1，+1了就说明当前空间已经被存放了数据，那这里为什么后面存放的数据都是0呢，是因为这个程序是从命令行参数里获取值然后保存的，我们运行程序时没有输入参数，所以这里都是0
0x00020fd9是剩余可分配的堆空间大小
name函数大小设置的是64字节，为什么程序给我们分配了72字节的空间，其实是这样算的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-ff1b221d8e00fd813639580eef675649f6d20177.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a3555a74cb72cf3e97529a3786edff6cc8d49803.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-49351636f8c3c0c594505133d4b62e0bfba553ff.png)
程序还将前面保留的四个字节空闲空间和本身表示大小的空间算进去了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c2b5ac9884f4230732db172c880160f0a8c7c0d2.png)
在程序执行strcpy函数的地方下一个断点，这个地方是程序将输入的值存入堆里的地方
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-b354e8e3d0df4a7d66e60a573ccefb0c4a5ae41e.png)
重新运行程序，输入A，执行strcpy函数的指令，再在查看栈空间
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a185af27600b3ea9e7d9e739d3a1522749d6004a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-d87dce285dd2d47bb8d489a87b7437a4a845cab7.png)
程序已经将我们输入的8个A的十六进制值放入了堆
堆的常见漏洞及原理
=========
在堆管理过程中，误用堆可能会导致多种问题：
1.忘记释放内存（Memory Leak）
当程序分配内存后忘记释放，未被释放的内存将无法再被使用，导致内存泄漏（Memory Leak）。长时间运行的程序如果不断泄漏内存，最终会导致可用内存耗尽，程序崩溃或系统变慢。
2.使用已释放的内存（Use-After-Free）
在释放内存后，继续使用该内存区域。这通常会导致未定义行为，可能会读取到无效数据或导致程序崩溃。攻击者也可能利用此类漏洞进行恶意攻击。
3.释放已释放的内存（Double Free）
试图再次释放已经释放过的内存块。这可能会破坏堆的内部管理结构，导致内存分配器行为异常，甚至引发安全漏洞。
4.破坏堆元数据（Heap Metadata Corruption）
堆管理器使用元数据来跟踪内存块的分配和释放状态。如果程序不小心或恶意修改这些元数据，会导致堆管理器无法正确管理内存。例如，这可能会导致堆溢出或其他内存管理漏洞，进而被攻击者利用。
内存泄漏
----
堆内存泄漏是指程序运行过程中分配的内存没有被释放，导致这些内存块不能被重用。长时间运行的程序如果存在内存泄漏，会不断消耗系统内存资源，最终导致系统资源耗尽，影响程序和系统的正常运行
```php
#include <stdio.h>
#include <stdlib.h>
void memoryLeakExample() {
// 每次调用函数时分配1024字节的内存
char \*leak = (char \*)malloc(1024);
if (leak == NULL) {
fprintf(stderr, "Memory allocation failed\n");
return;
}
// 使用内存
snprintf(leak, 1024, "This is a memory leak example");
printf("%s\n", leak);
// 漏掉了释放内存的操作
}
int main() {
for (int i = 0; i < 10000; i++) {
memoryLeakExample();
}
return 0;
}
```
在这个例子中，函数 memoryLeakExample 中每次调用 malloc 分配了1024字节的内存，但没有相应的 free 调用来释放这些内存。每次调用该函数时，都会有一块内存无法被释放，导致内存泄漏
### 示例1：使用未初始化的内存
```php
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void uninitializedMemoryDisclosure() {
char \*password = malloc(16);
if (password == NULL) {
fprintf(stderr, "Memory allocation failed\n");
return;
}
char \*data = malloc(16);
if (data == NULL) {
fprintf(stderr, "Memory allocation failed\n");
free(password);
return;
}
strcpy(password, "secret1234");
printf("Enter some data: ");
scanf("%15s", data);
// 打印未初始化的内存，可能泄露密码
printf("You entered: %s\n", data);
free(password);
free(data);
}
int main() {
uninitializedMemoryDisclosure();
return 0;
}
```
在示例1中，分配了两块内存 password 和 data。虽然 data 被用户输入覆盖，但如果用户输入的长度不足以覆盖整个内存块，剩余部分可能包含之前存储在 password 中的敏感信息 secret1234。因此，输出 data 时可能会泄露密码
### 示例2：使用已释放的内存
```php
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void useAfterFreeDisclosure() {
char \*password = malloc(16);
if (password == NULL) {
fprintf(stderr, "Memory allocation failed\n");
return;
}
strcpy(password, "secret1234");
free(password);
// 重新分配内存块可能重用先前释放的内存
char \*data = malloc(16);
if (data == NULL) {
fprintf(stderr, "Memory allocation failed\n");
return;
}
printf("Enter some data: ");
scanf("%15s", data);
// 打印已释放的内存内容，可能泄露密码
printf("You entered: %s\n", data);
free(data);
}
int main() {
useAfterFreeDisclosure();
return 0;
}
```
在第二个示例中，先分配了一块内存给 password，并存储了密码 secret1234。释放 password 后，重新分配了一块内存给 data，这块内存可能重用之前 password 的内存区域。如果 data 的输入未覆盖整个内存块，打印 data 时可能会泄露之前的密码信息
释放后使用（Use After Free）
---------------------
在释放内存后，指向该内存的指针仍然有效，堆释放后使用（UAF）是指程序在释放内存后继续使用该内存的现象。这是一种严重的内存管理错误，可能导致未定义行为，程序崩溃，数据泄露，甚至被攻击者利用进行恶意攻击
```php
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void useAfterFree() {
char \*data = (char \*)malloc(100);
if (data == NULL) {
fprintf(stderr, "Memory allocation failed\n");
return;
}
strcpy(data, "Hello, World!");
printf("Data before free: %s\n", data);
free(data); // 释放内存
// 再次使用已释放的内存
printf("Data after free: %s\n", data);
// 重新分配内存
char \*newData = (char \*)malloc(100);
if (newData == NULL) {
fprintf(stderr, "Memory allocation failed\n");
return;
}
// 使用新分配的内存
strcpy(newData, "New Data");
printf("New Data: %s\n", newData);
free(newData);
}
int main() {
useAfterFree();
return 0;
}
```
在这个示例中，函数 useAfterFree 先分配了一块内存 data，然后在释放该内存后继续使用它。这可能导致未定义行为，程序可能会打印出垃圾数据或崩溃。之后重新分配了新内存 newData，这块内存可能会重用先前释放的内存区域，如果攻击者能够控制 data 的内容，可能会影响 newData 的内容
### UAF的实际攻击利用
```php
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void vulnerableFunction() {
char \*user\_input = (char \*)malloc(8);
if (user\_input == NULL) {
fprintf(stderr, "Memory allocation failed\n");
return;
}
printf("Enter name: ");
scanf("%7s", user\_input);
printf("Hello %s!\n", user\_input);
free(user\_input);
// 再次使用 user\_input
long \*authenticated = (long \*)malloc(8);
if (authenticated == NULL) {
fprintf(stderr, "Memory allocation failed\n");
return;
}
\*authenticated = 0;
print...