---
title: Puckungfu: A NETGEAR WAN Command Injection
url: https://buaq.net/go-141034.html
source: unSafe.sh - 不安全
date: 2022-12-23
fetch_date: 2025-10-04T02:18:08.480619
---

# Puckungfu: A NETGEAR WAN Command Injection

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

![](https://8aqnet.cdn.bcebos.com/6f815fa4663edf13fc868f951b6c26c7.jpg)

Puckungfu: A NETGEAR WAN Command Injection

SummaryVulnerability DetailsOverviewExecution Flow/bin/pucfu/usr/lib/libfwcheck.soget
*2022-12-22 19:18:10
Author: [research.nccgroup.com(查看原文)](/jump-141034.htm)
阅读量:41
收藏*

---

* [Summary](#summary)
* [Vulnerability Details](#vulnerability-details)
  + [Overview](#overview)
  + [Execution Flow](#execution-flow)
    - [/bin/pucfu](#binpucfu)
    - [/usr/lib/libfwcheck.so](#usrliblibfwcheck.so)
      * [get\_check\_fw](#get_check_fw)
      * [fw\_check\_api](#fw_check_api)
      * [curl\_post](#curl_post)
    - [/lib/libpu\_util.so](#liblibpu_util.so)
      * [SetFileValue](#setfilevalue)
      * [pegaPopen](#pegapopen)
* [Check Firmware HTTPS](#check-firmware-https)
  + [Normal Request & Response](#normal-request-response)
* [Exploitation](#exploitation)
  + [Command Injection
    Response](#command-injection-response)
  + [Root Shell](#root-shell)
* [Final Notes](#final-notes)
  + [Patch](#patch)
  + [Pwn2Own Note](#pwn2own-note)

This blog post describes a command injection vulnerability found and
exploited in November 2022 by NCC Group in the [Netgear
RAX30](https://www.netgear.com/uk/home/wifi/routers/rax30/) router’s WAN interface. It was running firmware version [1.0.7.78](https://kb.netgear.com/000064989/RAX30-Firmware-Version-1-0-7-78)
at the time of exploitation. The vulnerability was patched on the 1st of
December 2022 with hotfix firmware version 1.0.9.90. Hotfix 1.0.9.90 is
no longer publicly accessible on the Netgear website as the latest
hotfix firmware version is [1.0.9.92](https://kb.netgear.com/000065427/RAX30-Firmware-Version-1-0-9-92).

The firmware files are accessible via the following links:

* [RAX30-V1.0.7.78.zip](https://www.downloads.netgear.com/files/GDC/RAX30/RAX30-V1.0.7.78.zip)
* [RAX30-V1.0.9.92.zip](https://www.downloads.netgear.com/files/GDC/RAX30/RAX30-V1.0.9.92.zip)

## Overview

The [Netgear
RAX30](https://www.netgear.com/uk/home/wifi/routers/rax30/) `/bin/pucfu` binary executes during boot and will
attempt to connect to a Netgear domain
(`<https://devcom.up.netgear.com/>`) and retrieve a JSON
response. We use a DHCP server to control the DNS server that is
assigned to the router’s WAN interface. By controlling the response of
the DNS lookup we can cause the router to perform HTTP(S) requests to an
attacker-controlled web server. Our web server will then respond with a
specially crafted JSON response that triggers a command injection in
`/bin/pucfu`.

The command injection vulnerability occurs in the
`SetFileValue()` function defined in
`/lib/libpu_util.so` which is imported by
`/bin/pucfu`. This function will be passed a user-controlled
value, which will be appended to an executed `execve` shell
command.

## Execution Flow

The vulnerability flow consists of functions from the libraries
`/usr/lib/libfwcheck.so` and `/lib/libpu_util.so`
as shown in the following call graph:

![Puckungfu Command Injection Call Graph](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2022/12/netgear-wan-call-graph.jpg)

### /bin/pucfu

The `/bin/pucfu`’s `main` [1] function calls
the `get_check_fw` [2] function from the
`/usr/lib/libfwcheck.so` library. This function retrieves the
`url` JSON parameter from
`<https://devcom.up.netgear.com/UpBackend/checkFirmware/>` and
stores it into the `bufferLargeA` variable.
`bufferLargeA` is then copied to `bufferLargeB`
[3] and passed to the `SetFileValue` function as the value
parameter [4].

```
int main(int argc,char **argv) // [1]
{
    ...
    // Perform API call to retrieve data
    status = get_check_fw(callMode, 0, bufferLargeA, 0x800); // [2] - Retrieve attacker controlled data into bufferLargeA
    ...
    strcpy(bufferLargeB, bufferLargeA); // [3]
    SetFileValue("/tmp/fw/cfu_url_cache", "lastURL", bufferLargeB); // [4] - Attacker controlled data passed as value parameter
    ...
}
```

### /usr/lib/libfwcheck.so

#### get\_check\_fw

The `get_check_fw` function prepares request parameters by
retrieving data from the D2 database including the base URL of
`<https://devcom.up.netgear.com/UpBackend/>` [5]. Next,
`fw_check_api` is called passing through the
`urlBuffer` buffer [6] which will contain the received URL
from the JSON response.

```
int get_check_fw(int mode, byte betaAcceptance, char *urlBuffer, size_t urlBufferSize)
{
    ...
    char upBaseUrl [136];
    char deviceModel [64];
    char fwRevision [64];
    char fsn [16];
    uint region;

    // Retrieve data from D2
    d2_get_ascii(DAT_00029264,"UpCfg",0,"UpBaseURL",upBaseUrl,0x81); // [5]
    d2_get_string(DAT_00029264,"General",0,"DeviceModel",deviceModel,0x40);
    d2_get_ascii(DAT_00029264,"General",0,"FwRevision",fwRevision,0x40);
    d2_get_ascii(DAT_00029264,"General",0,&DAT_000182ac,fsn,0x10);
    d2_get_uint(DAT_00029264,"General",0,"Region",&region);

    // Call Netgear API and store response URL into urlBuffer
    ret = fw_check_api(upBaseUrl, deviceModel, fwRevision, fsn, region, mode, betaAcceptance, urlBuffer, urlBufferSize); // [6]
    ...
}
```

#### fw\_check\_api

`fw_check_api` performs a POST request to the
`baseUrl` endpoint with the data parameters as a JSON body
[7]. The JSON response is then parsed [8] and the `url` data
value is copied to the `urlBuffer` parameter [9] which is
returned to the `main` function.

```
uint fw_check_api(char *baseUrl,char *modelNumber,char *currentFwVersion,char *serialNumber, uint regionCode,int reasonToCall,byte betaAcceptance,char *urlBuffer, size_t urlBufferSize)
{
    ...
    // Build JSON request
    char json [516];
    snprintf(json,
        0x200,
        "{\"token\":\"%s\",\"ePOCHTimeStamp\":\"%s\",\"modelNumber\":\"%s\",\"serialNumber\":\"%s \",\"regionCode\":\"%u\",\"reasonToCall\":\"%d\",\"betaAcceptance\":%d,\"currentFWVersion \":\"%s\"}",
        token,
        epochTimestamp,
        modelNumber,
        serialNumber,
        regionCode,
        reasonToCall,
        (uint)betaAcceptance,
        currentFwVersion
    );

    snprintf(checkFwUrl, 0x80, "%s%s", baseUrl, "checkFirmware/");

    // Perform HTTPS request
    int status = curl_post(checkFwUrl, json, &response); // [7]
    char* _response = response;

    ...

    // Parse JSON response
    cJSON *jsonObject = cJSON_Parse(_response); // [8]

    // Get status item
    cJSON *jsonObjectItem = cJSON_GetObjectItem(jsonObject, "status");
    if ((jsonObjectItem != (cJSON *)0x0) && (jsonObjectItem->type == cJSON_Number))
    {
        state = 0;
        (*(code *)fw_debug)(1,"\nStatus 1 received\n");

        // Get URL item
        cJSON *jsonObjectItemUrl = cJSON_GetObjectItem(jsonObject,"url");

        // Copy url into url buffer
        int snprintfSize = snprintf(urlBuffer, urlBufferSize, "%s", jsonObjectItemUrl->valuestring); // [9]
        ...
        return state;
    }
    ...
}
```

#### curl\_post

The `curl_post` function performs a HTTPS post request
using the `curl_easy` library. Although HTTPS is used, the
`CURLOPT_SSL_VERIFYHOST` [10] and
`CURLOPT_SSL_VERIFYPEER` [11] curl options are set to
disabled therefore an attacker-controlled HTTPS web server will not be
verified by the library.

```
size_t curl_post(char *url, char *json, char **response)
{
    ...
    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, curlSList);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json);
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0); // [10] - SSL Verification Disabled
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0); // [11] - SSL Verification Disabled
    ...
}
```

##...