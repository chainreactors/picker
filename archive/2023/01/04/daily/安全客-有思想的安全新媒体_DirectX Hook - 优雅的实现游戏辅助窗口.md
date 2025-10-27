---
title: DirectX Hook - 优雅的实现游戏辅助窗口
url: https://www.anquanke.com/post/id/284747
source: 安全客-有思想的安全新媒体
date: 2023-01-04
fetch_date: 2025-10-04T02:56:50.402569
---

# DirectX Hook - 优雅的实现游戏辅助窗口

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# DirectX Hook - 优雅的实现游戏辅助窗口

阅读量**408007**

发布时间 : 2023-01-03 10:30:51

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**作者：The\_Itach1@知道创宇404实验室
日期：2022年12月27日**

前言：最近看到了一个github的项目，分析过后觉得里面无论是代码还是界面都很好看，然后开始研究其代码。

这篇文章主要分析其如何实现的辅助窗口的实现，其用到的东西有minihook+DirectX11(9) Hook+imgui。

## Minihook

项目地址：[TsudaKageyu/minhook: The Minimalistic x86/x64 API Hooking Library for Windows (github.com)](https://github.com/TsudaKageyu/minhook)

先来了解下Minihook，Minihook是适用于 Windows 的简约 x86/x64 API 挂钩库。

一般来说，我们Hook windwos API的步骤是

* 编写DLL，确定Hook 的API函数。
* 编写自己的函数。
* 根据PE结构的知识点，遍历IAT函数表，根据函数名找到函数地址，进行修改，修改为我们的函数地址。

常见Hook IAT代码如下。

```
// hook_iat
BOOL hook_iat(LPCSTR szDllName, PROC pfnOrg, PROC pfnNew)
{
    HMODULE hMod;
    LPCSTR szLibName;
    PIMAGE_IMPORT_DESCRIPTOR pImportDesc;
    PIMAGE_THUNK_DATA pThunk;
    DWORD dwOldProtect, dwRVA;
    PBYTE pAddr;

    // hMod, pAddr = ImageBase of calc.exe
    //             = VA to MZ signature (IMAGE_DOS_HEADER)
    hMod = GetModuleHandle(NULL);
    pAddr = (PBYTE)hMod;

    // pAddr = VA to PE signature (IMAGE_NT_HEADERS)
    pAddr += *((DWORD*)&pAddr[0x3C]);

    // dwRVA = RVA to IMAGE_IMPORT_DESCRIPTOR Table
    dwRVA = *((DWORD*)&pAddr[0x80]);

    // pImportDesc = VA to IMAGE_IMPORT_DESCRIPTOR Table
    pImportDesc = (PIMAGE_IMPORT_DESCRIPTOR)((DWORD)hMod+dwRVA);

    for( ; pImportDesc->Name; pImportDesc++ )
    {
        // szLibName = VA to IMAGE_IMPORT_DESCRIPTOR.Name
        szLibName = (LPCSTR)((DWORD)hMod + pImportDesc->Name);
        if( !_stricmp(szLibName, szDllName) )
        {
            // pThunk = IMAGE_IMPORT_DESCRIPTOR.FirstThunk
            //        = VA to IAT(Import Address Table)
            pThunk = (PIMAGE_THUNK_DATA)((DWORD)hMod +
                                         pImportDesc->FirstThunk);

            // pThunk->u1.Function = VA to API
            for( ; pThunk->u1.Function; pThunk++ )
            {
                if( pThunk->u1.Function == (DWORD)pfnOrg )
                {
                    VirtualProtect((LPVOID)&pThunk->u1.Function,
                                   4,
                                   PAGE_EXECUTE_READWRITE,
                                   &dwOldProtect);

                    pThunk->u1.Function = (DWORD)pfnNew;

                    VirtualProtect((LPVOID)&pThunk->u1.Function,
                                   4,
                                   dwOldProtect,
                                   &dwOldProtect);

                    return TRUE;
                }
            }
        }
    }

    return FALSE;
}
```

可以看到过程还是比较繁琐，Minihook就很好的帮我们简化这个过程。

写一个hook弹窗的样例吧，将minihook对应的lib导入到项目后，就可以直接使用了，很方便。

```
#include <Windows.h>
#include <iostream>
#include "minhook/minhook.h"
#pragma comment (lib, "minhook/minhook.lib")

//typedef int (WINAPI* fMessageBoxA)(HWND, LPCSTR, LPCSTR, UINT);
using fMessageBoxA = int(WINAPI*)(HWND , LPCSTR , LPCSTR , UINT );
fMessageBoxA pMessageBoxA = NULL;

PVOID pMessageBoxAAddress;

int WINAPI MessageBoxAHooked(HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType)
{
    LPCSTR lpMyText = "Hacked by The_Itach1";
    return pMessageBoxA(hWnd, lpMyText, lpCaption, uType);
}

void SetupMessageBoxAHook()
{
    pMessageBoxAAddress = (LPVOID)MessageBoxA;

    if (MH_CreateHook(pMessageBoxAAddress, &MessageBoxAHooked, (PVOID*)&pMessageBoxA) != MH_OK)
        return;

    if (MH_EnableHook(pMessageBoxAAddress) != MH_OK)
        return;

    std::cout << "MessageBoxA Hook start!\n";
}

void initHook()
{
    if (MH_Initialize() != MH_OK)
    {
        MessageBoxA(NULL, "Error initialize minhook", "alternative hack", MB_OK | MB_ICONERROR);
    }
}

void UnHook()
{
    MH_DisableHook((PVOID)MessageBoxA);
    MH_RemoveHook((PVOID)MessageBoxA);
    MH_Uninitialize();

}

int main()
{
    //minhook的初始化
    initHook();

    //MessageBoxAHook
    SetupMessageBoxAHook();
    //测试是否hook成功
    MessageBoxA(NULL, "box1", "box1", MB_OK);

    //卸载hook
    UnHook();
    MessageBoxA(NULL, "box2", "box2", MB_OK);

    system("pause");
}
```

效果如下，可以看出当hook时，弹窗的内容被修改了，不hook时，就是正常的弹窗了。

![]()

而且minihook相比于IAT hook，或者Detours，感觉操作上更加的简便。

## DirectX11

### DirectX 简介

DirectX 是 Windows 中的一组组件，允许软件（主要且尤其是游戏）直接与视频和音频硬件结合使用。 使用 DirectX 的游戏可以更有效地使用内置于硬件的多媒体加速器功能，从而改善你的整体多媒体体验。

### 为什么要挂钩DirectX

在为游戏创建作弊时，渲染额外的内容或修改模型在游戏中的渲染方式迟早可能需要。有多种技术可以实现这一点，但最常见的技术之一是挂钩 DirectX API 的 3D 图形组件。

比如说D3D HOOK实现骨骼透视，实际上就是hookD3D绘制3D模型都需要调用的DrawIndexedPrimitive()函数，然后判断模型，修改其Z轴深度缓存，从而实现模型透视，还有就是这篇文章要讲到的，通过Hook DirectX11中呈现渲染图像的函数，来达到在游戏窗口上多添加一个imgui的辅助窗口。

### Direct3D11初始化

[Direct3D11学习：（三）Direct3D11初始化 – 郭小雷 – 博客园 (cnblogs.com)](https://www.cnblogs.com/Ray1024/p/6084609.html)
可以先看上面这篇文章，初步了解下Direct3D11初始化的过程，我们需要注意的是其中的创建一个渲染目标视图。

```
ID3D11RenderTargetView* mRenderTargetView;
ID3D11Texture2D* backBuffer;
// 获取一个交换链的后台缓冲区指针
mSwapChain->GetBuffer(0,__uuidof(ID3D11Texture2D), reinterpret_cast<void**>(&backBuffer));
// 创建渲染目标视图
md3dDevice->CreateRenderTargetView(backBuffer, 0, &mRenderTargetView);
// 每调用一次GetBuffer方法，后台缓冲区的COM引用计数就会递增一次。我们需要在使用完之后释放它
ReleaseCOM(backBuffer);
```

而什么是渲染呢
在Direct3D中，一个设备对象至少包含两个显示缓存区：当前缓存区（Front Buffer）和后备缓存区（Back Buffer），前者可以看成Direct3D窗口的映射。当我们渲染图形时，实际上并不是直接在窗口上输出，而是在后备缓存区上绘图。渲染完毕后，交换两个缓存区，使原来的后备缓存区变成当前缓存区，从而实现窗口刷新。快速重复此过程，就会在屏幕上形成连续的动画。

所以想要在游戏窗口，再加一个imgui的窗口，我们就需要在其执行绘制函数前，多创建一个渲染目标视图到其后备缓存区，这样后面绘制的时候，就也会绘制我们新添的imgui窗口。

### Imgui

[Dear Imgui](https://github.com/ocornut/imgui) 是一个**用于 C++ 的无膨胀图形用户界面库**。它输出优化的顶点缓冲区，您可以在启用 3D 管道的应用程序中随时渲染这些缓冲区。它快速、可移植、与渲染器无关且自包含（无外部依赖项）。

Imgui的example很多，其中就有[example\_win32\_directx11](https://github.com/ocornut/imgui/tree/master/examples/example_win32_directx11)的例子，只不过是开发的角度，不像游戏是已经开发出来的exe，所以对于游戏，是需要对关键函数进行hook的。

下面来分析这个example\_win32\_directx11。

```
// Dear ImGui: standalone example application for DirectX 11
// If you are new to Dear ImGui, read documentation from the docs/ folder + read the top of imgui.cpp.
// Read online: https://github.com/ocornut/imgui/tree/master/docs

#include "imgui.h"
#include "imgui_impl_win32.h"
#include "imgui_impl_dx11.h"
#include <d3d11.h>
#include <tchar.h>

// Data
static ID3D11Device*            g_pd3dDevice = NULL;
static ID3D11DeviceContext*     g_pd3dDeviceContext = NULL;
static IDXGISwapChain*          g_pSwapChain = NULL;
static ID3D11RenderTargetView*  g_mainRenderTargetView = NULL;

// Forward declarations of helper functions
bool CreateDeviceD3D(HWND hWnd);
void CleanupDeviceD3D();
void CreateRenderTarget();
void CleanupRenderTarget();
LRESULT WINAPI WndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam);

// Main code
int main(int, char**)
{
    // Create application window
    //ImGui_ImplWin32_EnableDpiAwareness();
    WNDCLASSEXW wc = { sizeof(wc), CS_CLASSDC, WndProc, 0L, 0L, GetModuleHandle(NULL), NULL, NULL, NULL, NULL, L"ImGui Example", NULL };
    ::RegisterClassExW(&wc);
    HWND hwnd = ::CreateWindowW(wc.lpszClassName, L"Dear ImGui DirectX11 Example", WS_OVERLAPPEDWINDOW, 100, 100, 1280, 800, NULL, NULL, wc.hInstance, NULL);

    // Initialize Direct3D
    if (!CreateDeviceD3D(hwnd))
    {
        CleanupDeviceD3D();
        ::UnregisterClassW(wc.lpszClassName, wc.hInstance);
        return 1;
    }

    // Show the window
    ::ShowWindow(hwnd, SW_SHOWDEFAULT);
    ::UpdateWindow(hwnd);

    // Setup Dear ImGui context
    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGuiIO& io = ImGui::GetIO(); (void)io;
    //io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
    //io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls

    // Setup Dear ImGui style
    ImGui::StyleColorsDark();
    //ImGui::StyleColorsLight();

    ...