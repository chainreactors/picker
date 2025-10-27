---
title: dotnet host startup hook
url: https://y4er.com/posts/dotnet-host-startup-hook/
source: Y4er的博客
date: 2023-01-04
fetch_date: 2025-10-04T02:58:58.417786
---

# dotnet host startup hook

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [DOTNET\_STARTUP\_HOOKS](#dotnet_startup_hooks)
* [思考](#思考)
* [参考](#参考)

## 目录

* [DOTNET\_STARTUP\_HOOKS](#dotnet_startup_hooks)
* [思考](#思考)
* [参考](#参考)

# dotnet host startup hook

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [代码审计](/categories/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)

2023-01-03  2023-01-03  约 1331 字
 预计阅读 6 分钟

目录

* [DOTNET\_STARTUP\_HOOKS](#dotnet_startup_hooks)
* [思考](#思考)
* [参考](#参考)

警告

本文最后更新于 2023-01-03，文中内容可能已过时。

# # DOTNET\_STARTUP\_HOOKS

dotnet core提供了一个底层的hook钩子，通过环境变量设置`DOTNET_STARTUP_HOOKS=aaa.dll`就可以在Main函数之前运行一些自定义代码

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/984eb38c-8506-a2f3-74f0-a31f26121040.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/984eb38c-8506-a2f3-74f0-a31f26121040.png "image.png")

image.png

`System.Private.CoreLib.dll!System.StartupHookProvider`类中

csharp

```
// Licensed to the .NET Foundation under one or more agreements.
// The .NET Foundation licenses this file to you under the MIT license.

using System;
using System.Diagnostics;
using System.Diagnostics.Tracing;
using System.Diagnostics.CodeAnalysis;
using System.IO;
using System.Reflection;
using System.Runtime.Loader;

namespace System
{
    internal static class StartupHookProvider
    {
        private const string StartupHookTypeName = "StartupHook";
        private const string InitializeMethodName = "Initialize";
        private const string DisallowedSimpleAssemblyNameSuffix = ".dll";

        private static bool IsSupported => AppContext.TryGetSwitch("System.StartupHookProvider.IsSupported", out bool isSupported) ? isSupported : true;

        private struct StartupHookNameOrPath
        {
            public AssemblyName AssemblyName;
            public string Path;
        }

        // Parse a string specifying a list of assemblies and types
        // containing a startup hook, and call each hook in turn.
        private static void ProcessStartupHooks()
        {
            string? startupHooksVariable = AppContext.GetData("STARTUP_HOOKS") as string;
            ...
            // Parse startup hooks variable
            string[] startupHookParts = startupHooksVariable.Split(Path.PathSeparator);
            StartupHookNameOrPath[] startupHooks = new StartupHookNameOrPath[startupHookParts.Length];
            for (int i = 0; i < startupHookParts.Length; i++)
            {
                string startupHookPart = startupHookParts[i];
                ...
                if (Path.IsPathFullyQualified(startupHookPart))
                {
                    startupHooks[i].Path = startupHookPart;
                }
                else
                {
                    // The intent here is to only support simple assembly names, but AssemblyName .ctor accepts
                    // lot of other forms (fully qualified assembly name, strings which look like relative paths and so on).
                    // So add a check on top which will disallow any directory separator, space or comma in the assembly name.
                    for (int j = 0; j < disallowedSimpleAssemblyNameChars.Length; j++)
                    {
                        if (startupHookPart.Contains(disallowedSimpleAssemblyNameChars[j]))
                        {
                            throw new ArgumentException(SR.Format(SR.Argument_InvalidStartupHookSimpleAssemblyName, startupHookPart));
                        }
                    }

                    if (startupHookPart.EndsWith(DisallowedSimpleAssemblyNameSuffix, StringComparison.OrdinalIgnoreCase))
                    {
                        throw new ArgumentException(SR.Format(SR.Argument_InvalidStartupHookSimpleAssemblyName, startupHookPart));
                    }

                    try
                    {
                        // This will throw if the string is not a valid assembly name.
                        startupHooks[i].AssemblyName = new AssemblyName(startupHookPart);
                    }
                    catch (Exception assemblyNameException)
                    {
                        throw new ArgumentException(SR.Format(SR.Argument_InvalidStartupHookSimpleAssemblyName, startupHookPart), assemblyNameException);
                    }
                }
            }

            // Call each hook in turn
            foreach (StartupHookNameOrPath startupHook in startupHooks)
            {
                CallStartupHook(startupHook);
            }
        }

        // Load the specified assembly, and call the specified type's
        // "static void Initialize()" method.
        [RequiresUnreferencedCode("The StartupHookSupport feature switch has been enabled for this app which is being trimmed. " +
            "Startup hook code is not observable by the trimmer and so required assemblies, types and members may be removed")]
        private static void CallStartupHook(StartupHookNameOrPath startupHook)
        {
            Assembly assembly;
            try
            {
                if (startupHook.Path != null)
                {
                    Debug.Assert(Path.IsPathFullyQualified(startupHook.Path));
                    assembly = AssemblyLoadContext.Default.LoadFromAssemblyPath(startupHook.Path);
                }
                else if (startupHook.AssemblyName != null)
                {
                    Debug.Assert(startupHook.AssemblyName != null);
                    assembly = AssemblyLoadContext.Default.LoadFromAssemblyName(startupHook.AssemblyName);
                }
                ...
            Type type = assembly.GetType(StartupHookTypeName, throwOnError: true)!;

            // Look for a static method without any parameters
            MethodInfo? initializeMethod = type.GetMethod(InitializeMethodName,
                                                         BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static,
                                                         null, // use default binder
                                                         Type.EmptyTypes, // parameters
                                                         null); // no parameter modifiers
            ...
            initializeMethod.Invoke(null, null);
        }
    }
}
```

截取了部分代码，其实就是在这个StartupHookProvider类中进行加载程序集，然后反射调用`Initialize`函数，堆栈如下

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/d6a07957-c160-97ee-bcca-673747fee68d.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/d6a07957-c160-97ee-bcca-673747fee68d.png "image.png")

image.png

如果你跟不到这个地方，那么需要勾掉这个选项：工具-选项-启用“仅我的代码”

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/37e70a36-0a94-44cd-dde8-fa4b4b189e73.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/37e70a36-0a94-44cd-dde8-fa4b4b189e73.png "image.png")

image.png

然后回溯栈帧的时候会让你选择符号服务器，勾上之后就可以跟进来了。

`src\coreclr\vm\assembly.cpp`在这个cpp文件中

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/7bb77cac-9fc7-0e5a-5014-f7c5e9ad4a6d.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/7bb77cac-9fc7-0e5a-5014-f7c5e9ad4a6d.png "image.png")

image.png

调用了钩子

在`https://github.com/dotnet/runtime/blob/2619d1c8eeef4a881c3910c87c1a8903ed742c24/src/coreclr/vm/assembly.cpp#L1494`

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/3c1a7b65-ff34-9e86-426b-31faea115fe4.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/3c1a7b65-ff34-9e86-426b-31faea115fe4.png "image.png")

image.png

RunStartupHooks在RunMain函数之前运行。

# # 思考

这个环境变量该如何使用？和java agent有什么区别？

想了...