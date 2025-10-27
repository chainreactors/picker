---
title: 学习PE文件后的第一次实践项目之DLL反射型注入
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588763&idx=1&sn=3f8a5ac4ea9d15820cc2cd6d5692963e&chksm=b18c26d186fbafc70f3e7c1673c15273d3202d1ec5d43301132c3a6e91aee46636b5ff4d87a8&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-21
fetch_date: 2025-10-06T20:11:13.773579
---

# 学习PE文件后的第一次实践项目之DLL反射型注入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GhB2YhPKZEztqohjYnMYVpcs2EwibvHbmpGGqwrfjtW8SEIFLxOdIx2gbmkQKMZMwg0Bqe8CNXIsw/0?wx_fmt=jpeg)

# 学习PE文件后的第一次实践项目之DLL反射型注入

l1pmoluy

看雪学苑

```
一

原理
```

##

普通注入

先看普通型的注入，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GhB2YhPKZEztqohjYnMYVpDWzlZMrHQkegFQ3uSEIprZDK7pdufLI8gz7oR4RnmokxmOcEQ2iamEw/640?wx_fmt=other&from=appmsg)

普通的dll注入是在目标进程中开辟一处空间，在空间中写入dll文件的名称，再用`LoadLibraryA`函数通过查找名称来加载dll，而想在程序里调用`LoadLibraryA`的话就得用到`CreateRemoteThread`函数，这个函数传递的参数之一就有函数指针，等到`CreateRemoteThread`创建新线程之后，就会在新线程中调用这个过度函数，其二的参数就是传给指针的参数。

这里插一句，在我多次用x64dbg调试得到的感悟，`CreateRemoteThread`这个函数，相当于开辟了一个不知道在哪的空间，在这个地方引用你要传入的函数。

## 反射型注入

反射型dll注入则是将整个DLL文件传到目标进程的空间中，然后通过`CreateRemoteThread`调用一段shellcode，将DLL展开，并运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GhB2YhPKZEztqohjYnMYVpmzemVAcaflX7ibolsAtenjeod6Hr6ic8NsicE8VklQkjSQ7pnfxfx7JJA/640?wx_fmt=png&from=appmsg)

##

```
二

源码1
```

##

Injectmain

```
#include <stdio.h>
#include <windows.h>
#include <tlhelp32.h>

DWORD RVAtoFileOffset(DWORD rva, PIMAGE_NT_HEADERS pNtHeaders, PIMAGE_SECTION_HEADER pSec);
LPVOID GetRemoteReflectLoad(LPVOID pDll, const char* funcName, unsigned char* pBuf);
DWORD ProcesstoPid(wchar_t* Processname);
BOOL WINAPI MainInject(DWORD dwTargetPid, char* Dllname);

int main() {
    //先定义需要注入的dll与目标进程的名字
    //wchar_t szProcName[MAX_PATH] = L"cs2.exe";
    wchar_t szProcName[MAX_PATH] = L"pta.exe";
    char Dllname[MAX_PATH] = "D:\\study\\VStudio\\ReflectDll\\x64\\Debug\\DLLIN.dll";

    //查找获得目标进程的id
    DWORD dwPid = ProcesstoPid(szProcName);
    //写入dll文件,这里思考一下，传入的参数都是什么呢？
    //因为在这个函数里，我们要做的是将dll文件写入，并且用其中的函数
    //dll中的API将会作为参数出现，所以传入的是进程id和dll函数目录
    DWORD result = MainInject(dwPid, Dllname);

}

DWORD ProcesstoPid(wchar_t* Processname) //查找指定进程的PID(Process ID)
{
    HANDLE hProcessSnap = NULL;
    DWORD ProcessId = 0;
    PROCESSENTRY32 pe32 = { 0 };
    hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0); //打开进程快照
    if (hProcessSnap == (HANDLE)-1)
    {
        printf("\n[-] CreateToolhelp32Snapshot() Error: %d", GetLastError());
        return 0;
    }
    pe32.dwSize = sizeof(PROCESSENTRY32);
    if (Process32First(hProcessSnap, &pe32)) //开始枚举进程
    {
        do
        {
            if (!wcscmp(Processname, pe32.szExeFile)) //判断是否和提供的进程名相等，是，返回进程的ID
            {
                ProcessId = pe32.th32ProcessID;
                break;
            }
        } while (Process32Next(hProcessSnap, &pe32)); //继续枚举进程
    }
    else
    {
        printf("\n[-] Process32First() Error: %d", GetLastError());
        return 0;
    }
    if (!ProcessId) printf("no find");
    else printf("[+] target id is %d", ProcessId);
    CloseHandle(hProcessSnap); //关闭系统进程快照的句柄
    return ProcessId;
}
//用于转换RVA->文件偏移地址
//传参说明：第一个是要转换的相对虚拟地址，第二个是Nt头的位置，第三个是节区表头的位置
DWORD RVAtoFileOffset(DWORD rva, PIMAGE_NT_HEADERS pNtHeaders, PIMAGE_SECTION_HEADER pSec) {
    // 遍历节区表
    for (int i = 0; i < pNtHeaders->FileHeader.NumberOfSections; i++) {
        // 检查RVA是否在当前节区的范围内
        if (rva >= pSec[i].VirtualAddress && rva < pSec[i].VirtualAddress + pSec[i].SizeOfRawData) {
            // 转换RVA到文件偏移地址
            return pSec[i].PointerToRawData + (rva - pSec[i].VirtualAddress);
        }
    }
    // 如果未找到对应的节区，返回无效值
    return 0xFFFFFFFF;
}

//该函数通过分析PE文件头来尝试获取句柄
LPVOID GetRemoteReflectLoad(LPVOID pDll, const char* funcName, unsigned char* pBuf) {
    //这里因为dll在别的进程里，所以想要看到可以利用前面的pBuf

    //定位一些相关文件头
    PIMAGE_DOS_HEADER pDosHeader = (PIMAGE_DOS_HEADER)pBuf;
    PIMAGE_NT_HEADERS pNtHeaders = (PIMAGE_NT_HEADERS)((BYTE*)pBuf + pDosHeader->e_lfanew);
    PIMAGE_SECTION_HEADER pSec = (PIMAGE_SECTION_HEADER)((LPBYTE)pNtHeaders + sizeof(IMAGE_NT_HEADERS));

    //获取导出表地址及大小，注意这里是RVA
    DWORD exportDirRVA = pNtHeaders->OptionalHeader.DataDirectory[0].VirtualAddress;
    DWORD exportDirSize = pNtHeaders->OptionalHeader.DataDirectory[0].Size;

    //定位导出表
    //这里遇到一个小问题，得到的偏移地址是RVA，但是咱们的文件现在只是磁盘文件,所以需要转换
    DWORD exportDirFileOffset = RVAtoFileOffset((DWORD)exportDirRVA, pNtHeaders, pSec);

    //转换之后RVA就变成了文件偏移，然后再定位
    PIMAGE_EXPORT_DIRECTORY pExportDir = (PIMAGE_EXPORT_DIRECTORY)((BYTE*)pBuf + exportDirFileOffset);

    //解析导出表，这里同理都是RVA
    DWORD pRNames = pExportDir->AddressOfNames;
    DWORD pFNames = RVAtoFileOffset(pRNames, pNtHeaders, pSec);
    DWORD* pNames = (DWORD*)((BYTE*)pBuf + pFNames);

    DWORD pRFunctions = pExportDir->AddressOfFunctions;
    DWORD pFFunctions = RVAtoFileOffset(pRFunctions, pNtHeaders, pSec);
    DWORD* pFunctions = (DWORD*)((BYTE*)pBuf + pFFunctions);

    WORD pRNameOrdinals = pExportDir->AddressOfNameOrdinals;
    WORD pFNameOrdinals = RVAtoFileOffset(pRNameOrdinals, pNtHeaders, pSec);
    WORD* pNameOrdinals = (WORD*)((BYTE*)pBuf + pFFunctions);

    // 遍历查找目标函数
    DWORD funcRVA = 0;
    for (DWORD i = 0; i < pExportDir->NumberOfNames; i++) {
        DWORD functionNameRVA = pNames[i];
        DWORD functionNameFileOffset = RVAtoFileOffset(functionNameRVA, pNtHeaders, pSec);
        const char* pName = (char*)((BYTE*)pBuf + functionNameFileOffset);
        if (strcmp(pName, funcName) == 0) {
            funcRVA = pFunctions[i];
            break;
        }
    }
    if (funcRVA == 0) {
        printf("\n[-] Function %s not found.", funcName);
        return NULL;
    }

    DWORD fileOffset = RVAtoFileOffset(funcRVA, pNtHeaders, pSec);;
    DWORD* pfileOffset = (DWORD*)((BYTE*)pBuf + fileOffset);
    if (fileOffset == 0) {
        printf("\n[-] Failed to convert RVA to file offset.");
        return NULL;
    }

    LPVOID remoteFuncAddr = (LPBYTE)pDll + fileOffset;
    return remoteFuncAddr;
}

BOOL WINAPI MainInject(DWORD dwTargetPid, char* Dllname)
{
    //与普通dll注入一样，首先要做的是获取句柄
    HANDLE hProc = NULL;

    hProc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwTargetPid);
    if (!hProc)
    {
        printf("\n[-] OpenProcess Failed.");
        DWORD dwError = GetLastError();
        printf("\n[-] OpenProcess failed. Error code: %d\n", dwError);
        return FALSE;
    }

    //有了句柄就可以创建空间然后写入了，这里的写入我参考的是PE加载器中
    //ReadFileA与创建空间的方法，其中相当于是在目标进程空间中创造一个"类磁盘"空间

    HANDLE hFile = CreateFileA(Dllname,
        GENERIC_READ, 						    //读取权限
        FILE_SHARE_READ | FILE_SHARE_WRITE,     //允许其他进程读取文件|允许其他进程写入文件
        NULL,								    //不需要特定的安全性
        OPEN_EXISTING, 						    //不需要特定的安全性
        FILE_ATTRIBUTE_NORMAL,				    //如果文件存在，则打开文件。如果文件不存在，操作会失败
        NULL								    //普通文件，没有特殊属性。
    );
    if (hFile == INVALID_HANDLE_VALUE) {
        printf("\n[-] CreateFileA failed.");
        return FALSE;
    }

    DWORD FileSize = GetFileSize(hFile, NULL);
    LPDWORD SizeToRead = 0;
    //本地暂存
    unsigned char* pBuf = new unsigned char[FileSize];
    ZeroMemory(pBuf, FileSize);
    int result = ReadFile(hFile, pBuf, FileSize, SizeToRead, NULL);  //读取文件放在开辟的空间里，pBuf为空间句柄
    if (result == 0)
    {
        printf("\n[-] 文件读取失败");
        return FALSE;
    }
    //对接下来开辟的空间进行计算大小
    PIMAGE_DOS_HEADER pDos = (PIMAGE_DOS_HEADER)pBuf;
    PIMAGE_NT_HEADERS pNt = (PIMAGE_NT_HEADERS)((BYTE*)pBuf + pDos->e_lfanew);
    PIMAGE_SECTION_HEADER pSection = (PIMAGE_SECTION_HEADER)((LPBYTE)pNt + sizeof(IMAGE_NT_HEADERS));
    DWORD ImageSize = pNt->OptionalHeader.SizeOfImage;

    //开辟目标进程中的"类磁盘"空间，大小为前文的FileSize
    //这里注意申请的地址权限要是可执行的（PAGE_EXECUTE_READWRITE）
    //这里创建的时候一下子创两个
    //刚开始没发现，才发现，pAlloc应该+的是FileSize哎呀麻烦了我想想
    ULONG_PTR TotalSize = ImageSize + ImageSize;
    printf("\n[+] FileSize : %p", FileSize);
    printf("\n[+] ImageSize: %p", ImageSize);
    printf("\n[+] TotalSize: %p", TotalSize);
    //这里遇到一个问题是，传入的TotaSize大小不够后面节区表的第一个表，好奇怪所以需要修正TotalSize大小
    LPVOID pDll = VirtualAllocEx(hProc, NULL, TotalSize + 1, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    if (pDll == NULL) {
        printf("\n[-] 内存分配失败, 错误代码: %d", GetLastError());
        return FALSE;
    }

    // 清零目标进程内存
    SIZE_T sizeToZero = TotalSize; // 需要清零的字节数
    BYTE* zeroBuffer = (BYTE*)calloc(sizeToZero, 1); // 创建一个全零的缓冲区
    i...