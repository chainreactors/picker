---
title: 还原iot设备中魔改的luac
url: https://forum.butian.net/share/3744
source: 奇安信攻防社区
date: 2024-09-21
fetch_date: 2025-10-06T18:21:23.824488
---

# 还原iot设备中魔改的luac

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

### 还原iot设备中魔改的luac

* [硬件与物联网](https://forum.butian.net/topic/51)

之前在分析tplink的设备时发现lua文件时编译完的，而且lua解释器是魔改过的。github上的[luadec-tplink](https://github.com/viruscamp/luadec)虽然可以还原成字节码，但是有些时候还原的结果不完整。所以决定研究下luac的还原，之后遇到其他设备时也许能用上。

本次研究的固件是[tplink archer c7 V5.80](https://www.tp-link.com/us/support/download/archer-c7/#Firmware)。
tplink archer c7的lua版本是5.1.4，下载对应版本[lua源码](https://www.lua.org/ftp/lua-5.1.4.tar.gz)。
lua加载执行chunk流程
--------------
main函数中，首先`lua\_open`打开文件，调用`luaL\_dofile`。`luaL\_dofile`是一个宏实际调用`luaL\_loadfile`和`lua\_pcall`。
```c
#define luaL\_dofile(L, fn) \
(luaL\_loadfile(L, fn) || lua\_pcall(L, 0, LUA\_MULTRET, 0))
int main(void)
{
lua\_State \*L=lua\_open();
lua\_register(L,"print",print);
if (luaL\_dofile(L,NULL)!=0) fprintf(stderr,"%s\n",lua\_tostring(L,-1));
lua\_close(L);
return 0;
}
```
#### luaL\\_loadfile
从调试时的调用栈可以看到，`luaL\_loadfile`最终调用`f\_parser`。
`f\_parser`中，首先读取第一个字节，判断是不是0x1B，是则认为是lua字节码文件，调用`luaU\_undump`，否则解析lua源码。
```c
static void f\_parser (lua\_State \*L, void \*ud) {
int i;
Proto \*tf;
Closure \*cl;
struct SParser \*p = cast(struct SParser \*, ud);
// 预读入第一个字符
int c = luaZ\_lookahead(p->z);
luaC\_checkGC(L);
// 根据之前预读的数据来决定下面的分析采用哪个函数
tf = ((c == LUA\_SIGNATURE[0]) ? luaU\_undump : luaY\_parser)(L, p->z,
&p->buff, p->name);
cl = luaF\_newLclosure(L, tf->nups, hvalue(gt(L)));
cl->l.p = tf;
for (i = 0; i < tf->nups; i++) /\* initialize eventual upvalues \*/
cl->l.upvals[i] = luaF\_newupval(L);
setclvalue(L, L->top, cl);
incr\_top(L);
}
```
`luaU\_undump`，`LoadHeader`获取文件头，`LoadFunction`获取函数体。
```c
Proto\* luaU\_undump (lua\_State\* L, ZIO\* Z, Mbuffer\* buff, const char\* name)
{
LoadState S;
if (\*name=='@' || \*name=='=')
S.name=name+1;
else if (\*name==LUA\_SIGNATURE[0])
S.name="binary string";
else
S.name=name;
S.L=L;
S.Z=Z;
S.b=buff;
LoadHeader(&S); // 文件头
return LoadFunction(&S,luaS\_newliteral(L,"=?")); //函数体
}
```
#### LoadHeader
文件头格式如下，这里只介绍后续会用到的字段。
第一个字段是luac文件的magic number，用于标识luac文件。
`version`字段表示lua版本，这里使用的是lua5.1，所以值是0x51。
`format`字段为0表示是官方定义的文件格式，不为0则为其他格式。但是实际上有些luac文件即使修改了官方的格式，该字段还是为0。
`endian`表示字节序。
`size\_size\_t`字段表示size\\_t类型所占的字节数。32位为4，64位为8。
`size\_lua\_Number`表示`lua\_Number`类型的数据大小。lua中的number使用浮点数表示，float为32位，double为64位。
```c
typedef struct {
char signature[4]; // #define LUA\_SIGNATURE "\033Lua"
uchar version; // 0x51,0x52，0x53
uchar format;
uchar endian;
uchar size\_int;
uchar size\_size\_t;
uchar size\_Instruction;
uchar size\_lua\_Number;
uchar lua\_num\_valid;
uchar luac\_tail[0x6];
} GlobalHeader;
```
使用101 editor模板可以很清楚地看到header结构的各个字段。
![image-20240821111556927.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-673bc506b9f10f5802b6ec2a6d377dbc6d91c859.png)
#### LoadFunction
`LoadFunction`首先初始化Proto结构体（存放函数原型的数据结构），之后是加载`protoheader`、`code`、`constants`和`debug`部分。
`protoheader`包含source（函数名或文件名）、linedefined（源码第一行行号）、lastlinedefined（源码最后一行行号）、is\\_vararg（是否可变参数）等字段，描述函数相关信息。
```c
static Proto\* LoadFunction(LoadState\* S, TString\* p)
{
Proto\* f;
if (++S->L->nCcalls > LUAI\_MAXCCALLS) error(S,"code too deep");
f=luaF\_newproto(S->L);
setptvalue2s(S->L,S->L->top,f); incr\_top(S->L);
f->source=LoadString(S); if (f->source==NULL) f->source=p; // protoheader
f->linedefined=LoadInt(S);
f->lastlinedefined=LoadInt(S);
f->nups=LoadByte(S);
f->numparams=LoadByte(S);
f->is\_vararg=LoadByte(S);
f->maxstacksize=LoadByte(S);
LoadCode(S,f); // code
LoadConstants(S,f); // constants
LoadDebug(S,f); // debug
IF (!luaG\_checkcode(f), "bad code");
S->L->top--;
S->L->nCcalls--;
return f;
}
```
#### LoadCode
`LoadCode`获取指令个数n，之后获取n条指令，每个指令是32位。
```c
static void LoadCode(LoadState\* S, Proto\* f)
{
int n=LoadInt(S);
f->code=luaM\_newvector(S->L,n,Instruction);
f->sizecode=n;
LoadVector(S,f->code,n,sizeof(Instruction));
}
```
#### LoadConstants
`LoadConstants`获取常量，同样先获取常量个数，再根据常量类型分别设置常量数据。
常量类型分为LUA\\_TNIL（空）、LUA\\_TBOOLEAN（布尔）、LUA\\_TNUMBER（数字）、LUA\\_TSTRING（字符串），其中数字使用浮点数表示。
之后获取该函数中的函数原型个数，嵌套调用`LoadFunction`。一个luac文件可以认为是一整个最大的proto，文件中定义的每个函数是最大proto的子函数。通过这种方式就把所有的function都加载进来。（这应该就是luadec的反编译结果中第一个函数是所有函数的定义的原因）
```c
static void LoadConstants(LoadState\* S, Proto\* f)
{
int i,n;
n=LoadInt(S);
f->k=luaM\_newvector(S->L,n,TValue);
f->sizek=n;
for (i=0; i<n; i++) setnilvalue(&f->k[i]);
for (i=0; i<n; i++)
{
TValue\* o=&f->k[i];
int t=LoadChar(S);
switch (t)
{
case LUA\_TNIL:
setnilvalue(o);
break;
case LUA\_TBOOLEAN:
setbvalue(o,LoadChar(S)!=0);
break;
case LUA\_TNUMBER:
setnvalue(o,LoadNumber(S));
break;
case LUA\_TSTRING:
setsvalue2n(S->L,o,LoadString(S));
break;
default:
error(S,"bad constant");
break;
}
}
n=LoadInt(S);
f->p=luaM\_newvector(S->L,n,Proto\*);
f->sizep=n;
for (i=0; i<n; i++) f->p[i]=NULL;
for (i=0; i<n; i++) f->p[i]=LoadFunction(S,f->source);
}
```
#### LoadDebug
获取行号信息，局部变量，和upvalue。当函数A中包含子函数B，并且函数B访问了函数A的参数或局部变量时，就会产生upvalue。实际iot固件中大多upvalue是函数访问全局变量时产生的。
```c
static void LoadDebug(LoadState\* S, Proto\* f)
{
int i,n;
n=LoadInt(S);
f->lineinfo=luaM\_newvector(S->L,n,int);
f->sizelineinfo=n;
LoadVector(S,f->lineinfo,n,sizeof(int));
n=LoadInt(S);
f->locvars=luaM\_newvector(S->L,n,LocVar);
f->sizelocvars=n;
for (i=0; i<n; i++) f->locvars[i].varname=NULL;
for (i=0; i<n; i++)
{
f->locvars[i].varname=LoadString(S);
f->locvars[i].startpc=LoadInt(S);
f->locvars[i].endpc=LoadInt(S);
}
n=LoadInt(S);
f->upvalues=luaM\_newvector(S->L,n,TString\*);
f->sizeupvalues=n;
for (i=0; i<n; i++) f->upvalues[i]=NULL;
for (i=0; i<n; i++) f->upvalues[i]=LoadString(S);
}
```
总之，整个luac文件可分为`header`和`function`两部分，`function`又分为`protoheader`，`code`，`constants`，`subproto`，`debug`部分。
首先加载解析`protoheader`部分，之后`LoadFunction`解析`proto`部分。
`LoadFunction`中，解析`protoheader`（函数头），`code`（代码），`subproto`（子函数），`debug`（行号信息、局部变量、upvalue）部分。
`subproto`中，同样按照`LoadFunction`流程解析。通过层层嵌套的方式，整个luac解析完成。
![image-20240822155546582.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-600a61c91379f6baa04112c7c96dcc5fd49e5977.png)
#### lua\\_pcall
加载完luac文件后，调用`docall`执行指令，最终调用`luaV\_execute`执行，根据不同opcode执行对应操作。
```c
void luaV\_execute (lua\_State \*L, int nexeccalls) {
...
switch (GET\_OPCODE(i)) {
case OP\_MOVE: {
setobjs2s(L, ra, RB(i));
continue;
}
case OP\_LOADK: {
setobj2s(L, ra, KBx(i));
continue;
}
case OP\_LOADBOOL: {
setbvalue(ra, GETARG\_B(i));
if (GETARG\_C(i)) pc++; /\* skip next instruction (if C) \*/
continue;
}
case OP\_LOADNIL: {
TValue \*rb = RB(i);
do {
setnilvalue(rb--);
} while (rb >= ra);
continue;
}
...
```
对比官方和tplink lua的不同
------------------
在了解了标准的luac的加载执行流程后，为了还原tplink luac，我们需要对比tplink luac的加载执行过程和标准的luac不同的地方。
下面列出一些可能的不同点。
1.header中的magic number、format。
例如小米luac的magic number不是`\x1BLua`而是`\x1BFate/Z`
![image-20240826154653091.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-17ff2497229823468c2026f022215110ac5b250e.png)
2.一些结构体中各个字段的顺序。
例如修改`protoheader`中的`source`、`linedefined`、`lastlinedefined`等字段顺序，导致标准反编译器无法识别luac的格式
3.contants和opcode可能修改ENUM的值，或者添加原本没有的类型。
例如`LUA\_T`开头的宏是从0开始，有的lua不是从0开始而是从3开始。
```c
#define LUA\_TNIL 0
#define LUA\_TBOOLEAN 1
#define LUA\_TLIGHTUSERDATA 2
#define LUA\_TNUMBER 3
#define LUA\_TSTRING 4
#define LUA\_TTABLE 5
#define LUA\_TFUNCTION 6
#define LUA\_TUSERDATA 7
#define LUA\_TTHREAD 8
```
4.打乱opcode原本的顺序
5.自定义contants类型格式
#### tplink lua的不同
在不断逆向分析以及调试验证后，发现tplink的lua做出了以下修改（逻辑在liblua.so.5.1.4）：
1.修改opcode
对比`luaV\_execute`中的opcode的值和执行的操作，发现相同...