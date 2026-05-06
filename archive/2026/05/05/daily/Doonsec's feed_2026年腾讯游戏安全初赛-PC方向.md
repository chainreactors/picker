---
title: 2026年腾讯游戏安全初赛-PC方向
url: https://mp.weixin.qq.com/s/qHuLHvkBoYhOF2rkNRciaw
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:08:37.907627
---

# 2026年腾讯游戏安全初赛-PC方向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0WvRxWmG7ibff16ibfwJoIYicQnDBzVibguB3KmCTcibz4AW25SsZY8WHX4uQfBhy8KwL2Iic69ZwSzEibHfBkib3NzKfGPYRMSr9GndU/0?wx_fmt=jpeg)

# 2026年腾讯游戏安全初赛-PC方向

江树
江树

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 仅为本人题解，并非参考答案不能保证正确，请参照官方公布题解。

## 〇、得分点

### 如何加载驱动

关掉**ACE**预启动，随便签一个泄露签名，即可加载驱动，稳定性极高，就蓝屏了两次。

### Flag

```
flag{SHAD0WNT_HYPERVMX}
```

### 最短路径

```
DDDDDDSSDDDDWWDDSSSSSSSSAASSSSDD
//格式化为
RRRRRRDDRRRRUURRDDDDDDDDLLDDDDRR
```

### 地图

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2eiccIoVoy5TU4CSNHmhj2CL4VoicIZ0KAPp44Mq4ia2xArEIS7DzRzf6cjsamMqvCvL3EsLc6bc4ibRQbLc7uIXjibNqEeRG9rWLc/640?wx_fmt=other&from=appmsg)

```
###########################
#S . . . . . .#.#. . . . .#
############# ####### ### #
#.#.#.#.#.#.#.#.#.#.#.#.#.#
############# ####### ### #
#. . . . .#.#. . . . .#.#.#
# ####### ############### #
#.#.#.#.#.#.#.#.#.#.#.#.#.#
# ####### ############### #
#.#.#. . . . . . . . .#.#.#
# ### ### ########### ### #
#.#.#.#.#.#.#.#.#.#.#.#.#.#
# ### ### ########### ### #
#.#.#.#.#.#.#. . .#.#.#.#.#
# ### ####### ### ####### #
#.#.#.#.#.#.#.#.#.#.#.#.#.#
# ### ####### ### ####### #
#.#.#. . . . .#.#.#.#. . .#
# ############### ### #####
#.#.#.#.#.#.#.#.#.#.#.#.#.#
# ############### ### #####
#. . .#.#. . .#.#.#.#.#.#.#
##### ### ### ### ### ### #
#.#.#.#.#.#.#.#.#.#.#.#.#.#
##### ### ### ### ### ### #
#. . . . .#.#.#.#. . . . E#
###########################
```

### 五个泄漏点（最后一个可能有误）

#### 1. 两个对象名

#### ①MazeMoveOK 事件

* 类型：命名事件
* 对象名：**Global\MazeMoveOK**
* 驱动侧实现：**ZwOpenEvent + ZwSetEvent**
* 含义：成功相关反馈槽位

#### ②MazeMoveWall 事件

* 类型：命名事件
* 对象名：Global\MazeMoveWall
* 驱动侧实现：**ZwOpenEvent + ZwSetEvent**
* 含义：失败/撞墙相关反馈槽位

#### 2. 两个 GUID

#### ①GUID1 命名信号量

* 类型：命名信号量
* 对象名：

+ **Global{A7F3B2C1-9E4D-4C8A-B5D6-1F2E3A4B5C6D}**

* 驱动侧实现：

+ 解码对象名
+ **ObReferenceObjectByName**
+ **KeReleaseSemaphore**

* 含义：成功相关反馈槽位

#### ②GUID2 命名信号量

* 类型：命名信号量
* 对象名：

+ **Global{B8E2C3D0-0F5A-5D9B-C6E7-2A3F4B5C6D7E}**

* 驱动侧实现同上
* 含义：失败/撞墙相关反馈槽位

#### 3. LastError

* 类型：线程用户态上下文回写
* 驱动侧关键函数：**sub\_140316ADF**
* 关键行为：

+ 写**+0x68 （TEB -> LastErrorValue）**

* 写入值包括：

+ **0xC0DE0001 -> ok**
+ **0xC0DE0000 -> wall**

#### 4. ZwSetInformationObject

每次**move**前先调用`SetHandleInformation(h, HANDLE_FLAG_PROTECT_FROM_CLOSE, 0)`进行清零，在**move**后调用`GetHandleInformation(h, &flags)`

```
if( flags & HANDLE_FLAG_PROTECT_FROM_CLOSE !=0)
   handle_ok =true
else
   handle_ok =False
```

* handle\_ok = True

+ 表示：成功

* handle\_ok = False

+ 表示：失败/撞墙

#### 5. KeDelayExecutionThread

函数会通过**KUSER\_SHARED\_DATA**访问**TickCountLowDeprecated**，并且在异或后被编码进入返回缓冲，可以在用户层恢复被驱动使用的这个**Tick**值。

```
tick_xor = struct.unpack_from("<I", raw, 0)[0]
tick = tick_xor ^ 0xBAADF00D
```

然后计算

```
predicted_ms = (tick % 50) + 10
```

就是理论上这个线路被延时的毫秒数，然后我们可以计算一个**IO**请求的耗时

```
 t0 = time.perf_counter()
 DeviceIoControl(...)
 time_ms = (time.perf_counter() - t0) * 1000.0
```

如果**predicted\_ms**和**time\_ms**很接近，就能说明本次触发到了该泄漏点，但是无法判断具体的结果。

* 很接近

+ 表示：命中该泄漏点，应重试，直到命中前几个可明确结果泄漏点

* 不接近

+ 表示：应观测其他泄漏点获取本次**move**的结果

### 总结

在二进制文件中放了大量的小混淆，导致不管是正向分析还是逆向分析，都不舒服，比如发现了某一个函数，发现**xref**不可用，因为上游的调用点有花指令，混淆等，导致了**IDA**不能正确分析，在驱动分析中尤其明显，但是由于驱动导入表暴露了大量的信息，所以都可以通过导入表入手，不完整的分析全流程，也能得到相关结论，如果赛题在导入函数上做手脚，比如动态解析，难度会更大。

很好本来都要提交了，感觉这个寻路脚本咋会这么慢，时间还不稳定，又重新用IDA看了一眼驱动，发现有随机的**Sleep**感觉大概率是没找齐全，然后就找到了之前没找到的两个泄漏点（但是他们没有影响我得到flag....）

## 一、赛题文件

## 文档：2026游戏安全技术竞赛-PC客户端安全-初赛.docx

```
#「宫殿」的验证机制并不寻常：系统由用户态控制台和内核驱动组成，驱动内部隐藏着一个加密迷阵，所有操作指令必须由控制台通过驱动接口下
# 发。表面上，系统不会对你的任何操作给出反馈——你无法直接判断每一步操作是成功推进，还是被防线拦截。
```

从上述文本能够判断是迷宫题目，但是应该不是简单的迷宫，应该无法通过传统的迷宫分析方法分析，需要完整的逆向，至少要找到文档中提到的：

```
# 某些异常现象暗示着隐藏的信息泄露。找到这些线索，你就能感知每一步的结果；发现得越多，破解效率越高。
```

## 二、应用层：ShadowGateApp.exe

并未发现有保护壳，直接运行得到：

```
C:\Users\Euarno\Desktop\2026游戏安全技术竞赛-PC客户端安全-初赛>ShadowGateApp.exe

==============================================
    Shadow Palace Gate  -  ACCESS DENIED
==============================================

  ACE has intercepted Shadow's palace gate
  system. A kernel driver hides an encrypted
  maze inside. Navigate through it to extract
  the credential for Shadow's internal network.

  The palace gives NO feedback on whether
  your moves succeed or hit a wall.

Or does it? The system is not as silent
as it seems. Five hidden flaws betray
  the result of every move 鈥?but each move
  exposes only one of them.

  Hint: after each reset, the first five
  successful moves reveal each flaw exactly
  once, in a fixed order.

[*] Connecting to Shadow gate driver...
[+] Gate module online.

[*] Maze grid: 13x13, Entry=(0,0), Exit=(12,12)
Commands:
  W/A/S/D    - Navigate Up/Left/Down/Right
  I/J/K/L    - Navigate Up/Left/Down/Right (alt)
  R          - Reset to entry point
  T          -Show operation log (position hidden)
  H          -Show this help
  Q / ESC    - Abort mission
```

可以有一个基本的了解**13\*13**的迷宫，**“The palace gives NO feedback on whether your moves succeed or hit a wall.”**表面不会有反馈，**“Five hidden flaws betray the result of every move ”**要通过五个侧信道得到迷宫的反馈，\*\*“after each reset, the first five successful moves reveal each flaw exactly once, in a fixed order. ”\*\*每次你按**R**重置后，前**5**次成功移动会依次触发五种不同的泄露机制，顺序是固定的。(这里其实还是有一点疑惑的，最终只找到了三类泄露方式，但也可以算作五个泄漏点)

字符串没有做混淆，在字符串表暴露了很多信息。结合字符串的交叉引用，有如下分析：

```
__int64 OpenShadowGateDevice()
{
  __int64 result; // rax
DWORDLastError; // edi

//设备路径
  result = (__int64)CreateFileW(L"\\\\.\\ShadowGate", 0xC0000000, 0, 0, 3u, 0x80u, 0);
if ( result ==-1 )
  {
LastError=GetLastError();
    sub_140001010("[ERROR] Failed to open device '%ws'\n", L"\\\\.\\ShadowGate");
    sub_140001010("[ERROR] Error code: %lu (0x%08lX)\n", LastError, LastError);
if ( LastError==2 )
    {
//要求我们应该提前加载好驱动 驱动没有签名 我的解决方案是找一个泄露签名 退出ACE预启动 即可加载
      sub_140001010("[HINT] Driver not loaded. Use: sc create ShadowGate type=kernel binPath=<path>\\ShadowGateSys.sys\n");
      sub_140001010("[HINT] Then: sc start ShadowGate\n");
return -1;
    }
else
    {
if ( LastError==5 )
        sub_140001010("[HINT] Run as Administrator.\n");
return -1;
    }
  }
return result;
}
```

虽然还没有分析驱动，但是应用创建了两个全局命名事件，名称强烈暗示它们分别对应移动成功和撞墙，即失败。

```
HANDLE CreateLeakEvents()
{
  HANDLE result; // rax

  hObject = CreateEventW(0, 1, 0, L"Global\\MazeMoveOK");
result = CreateEventW(0, 1, 0, L"Global\\MazeMoveWall");
  qword_140005688 = result;
return result;
}
```

通信方面使用了最基本的**IO**通讯，分析**DeviceIoControl**的交叉引用可以得到所有的**IO**码。

```
if ( QueryMaza(v6, &v9) )
printf(
"[*] Maze grid: %ux%u, Entry=(%u,%u), Exit=(%u,%u)\n",
        (_DWORD)v9,
        DWORD1(v9),
        DWORD2(v9),
        HIDWORD(v9),
        v10,
        HIDWORD(v10));

BOOL __fastcall QueryMaza(__int64 a1, void *lpOutBuffer)
{
  DWORD BytesReturned; // [rsp+40h] [rbp-18h] BYREF

  BytesReturned = 0;
return DeviceIoControl(hDevice, 0x8001200C, 0, 0, lpOutBuffer, 0x18u, &BytesReturned, 0);
}
```

显然**0x8001200C**用于查询迷宫信息，接下来就能发现**main**函数有大量的花指令了，因为正常的**R**等逻辑的处理代码都不存在。

只需要把：

```
push rcx
ret
```

改为：

```
jmp rcx
```

伪代码就重建好了，然后依旧是出题人的小礼物啊：

```
v8 -= 27;
switch ( v8 )
```

这里会有垂落，处理的是大小写**R**的情况：

```
case '7':
case 'W':
ResetMaze(_RCX);
     v6 = 0;
     dword_140005668 = 0;
     v22[0] = 0;
     v7 = 0;
printf("[*] Reset to entry point.\n");
continue;

BOOL ResetMaze(){
  DWORD BytesReturned; // [rsp+40h] [rbp-18h] BYREF

  BytesReturned = 0;
return DeviceIoControl(hDevice, 0x80012008, 0, 0, 0, 0, &BytesReturned, 0);
}
```

显然**0x80012008**用于重新开始，那剩下的操作码肯定是操作迷宫了的。

| IOCTL | 作用 |
| --- | --- |
| 0x80012004 | 移动/核心交互 |
| 0x80012008 | 重置到起点 |
| 0x8001200C | 查询迷宫信息 |

紧接着还要详细分析，相关的按键被映射为了十六进制整数，如下：

```
case '&':
case '/':
case 'F':
case 'O':
        LOBYTE(direct) = 0x30; //A  J
        v12 = 76;
goto LABEL_11;
case ')':
case '1':
case 'I':
case 'Q':
        LOBYTE(direct) = 0x40;// D  L
        __asm { rcl     al, cl }
        v12 = 82;
goto LABEL_11;
case '.':
case '<':
case 'N':
case '\\':
        LOBYTE(direct) = 0x10; //W  I
        v12 = 85;
goto LABEL_11;
case '0':
case '8':
case 'P':
case 'X':
        LOBYTE(direct) = 0x20; // S   K
        v1...