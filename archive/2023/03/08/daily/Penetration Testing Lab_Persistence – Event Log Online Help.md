---
title: Persistence – Event Log Online Help
url: https://pentestlab.blog/2023/03/07/persistence-event-log-online-help/
source: Penetration Testing Lab
date: 2023-03-08
fetch_date: 2025-10-04T08:54:24.170300
---

# Persistence – Event Log Online Help

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

Posted on [March 7, 2023](https://pentestlab.blog/2023/03/07/persistence-event-log-online-help/)

# Persistence – Event Log Online Help

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[Leave a Comment on Persistence – Event Log Online Help](https://pentestlab.blog/2023/03/07/persistence-event-log-online-help/#respond)

Event viewer is a component of Microsoft Windows that displays information related to application, security, system and setup events. Even though that Event Viewer is used mainly for troubleshooting windows errors by administrators could be also used as a form a persistence during red team operations. Microsoft in order to assist administrators to retrieve direct information for a particular event ID over the web has embedded a functionality which is called Event Log Online Help.

The Event Log Online Help redirects the users to a Microsoft URL and is controlled from the following registry location.

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Event Viewer
```

Three registry keys could be modified if local administrator access has been achieved in order to execute arbitrary payloads once the Event Log Online Help is clicked by the user. These keys can be found below:

* MicrosoftRedirectionProgram
* MicrosoftRedirectionProgramCommandLineParameters
* MicrosoftRedirectionURL

A very trivial proof of concept is to trigger a message box.

```
#include <windows.h>
#pragma comment (lib, "user32.lib")

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
  MessageBox(NULL, "pentestlab.blog", "Pentestlab", MB_OK);
  return 0;
}
```

The code above could be compiled using MinGW in order to generate an executable.

```
x86_64-w64-mingw32-g++ -O2 messagebox.cpp -o messagebox.exe -I/usr/share/mingw-w64/include/ -s -ffunction-sections -fdata-sections -Wno-write-strings
-fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -fpermissive
```

The registry key “*MicrosoftRedirectionProgram”* could be modified to contain the location of the compiled executable. Clicking the Event Log Online Help will display the message box indicating that code has been executed.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-messagebox.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-messagebox.png)

Event Log Online Help – MessageBox

In similar manner “*msfvenom*” could be used to generated a payload.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-msfvenom.png?w=636)](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-msfvenom.png)

msfvenom – Payload Generation

Modification of the registry key below to map to the location on the disk of the previously generated payload will execute the payload.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-microsoft-redirection-program.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-microsoft-redirection-program.png)

Microsoft Redirection Program – Registry Key

When the Event Log Online Help is clicked a connection will be established.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-meterpreter.png?w=636)](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-meterpreter.png)

Event Log Online Help – Meterpreter

The second registry key “*MicrosoftRedirectionProgramCommandLineParameters*” allows the user modify the data value in order to execute commands. A very common living off the land binary such as “regsvr32” can be utilized to execute a fileless payload.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-microsoft-redirection-program-command-line-regsvr32.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-microsoft-redirection-program-command-line-regsvr32.png)

Microsoft Redirection Program Command Line Parameters

Once the Event Log Online Help is clicked the command will be executed and a communication channel will established.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-meterpreter-regsvr32.png?w=636)](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-meterpreter-regsvr32.png)

Meterpreter – regsvr32

The last registry key is the “*MicrosoftRedirectionURL*” which by default it points out to a Microsoft location. The registry value could be changed to point either to a malicious URL or to a payload which is dropped on the disk.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-microsoft-redirection-url.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-microsoft-redirection-url.png)

Microsoft Redirection URL

In all of the above scenarios the following condition will be created:

* Parent Process (mmc.exe) –> Child Process (Payload)

[![](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-mmc-parent-process.png?w=854)](https://pentestlab.blog/wp-content/uploads/2023/03/event-log-online-help-mmc-parent-process.png)

MMC – Parent Process

EDR’s should flag when mmc tries to spawn non trusted processes. Furthermore, monitoring of the above registry keys for changes could create a detection opportunity. As access to Windows graphical interface is required and considering the fact that the average user would not typically open event viewer and click on the Windows Event Log Online Help it is unlikely that this technique will gain popularity. However, in an assumed breach or malicious insider scenarios it could be used as a trivial method to maintain an active connection over a C2 channel.

## References

* <https://www.hexacorn.com/blog/2019/02/15/beyond-good-ol-run-key-part-103/>

### Rate this:

### Share this:

* [Click to share on X (Opens in new window)
  X](https://pentestlab.blog/2023/03/07/persistence-event-log-online-help/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://pentestlab.blog/2023/03/07/persistence-event-log-online-help/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://pentestlab.blog/2023/03/07/persistence-event-log-online-help/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://pentestlab.blog/2023/03/07/pe...