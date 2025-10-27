---
title: Appshark - Static Taint Analysis Platform To Scan Vulnerabilities In An Android App
url: https://buaq.net/go-134233.html
source: unSafe.sh - 不安全
date: 2022-11-05
fetch_date: 2025-10-03T21:42:42.839371
---

# Appshark - Static Taint Analysis Platform To Scan Vulnerabilities In An Android App

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

![](https://8aqnet.cdn.bcebos.com/5fe907c1ec6e3cbd1071a3a553b69aef.jpg)

Appshark - Static Taint Analysis Platform To Scan Vulnerabilities In An Android App

Appshark is a static taint analysis platform to scan vulnerabilities in an Android app. Pre
*2022-11-4 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-134233.htm)
阅读量:32
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW6IXPDSxJE5pTeCn31iaD9JpdptV8OVGIMeVtTPjDsQMBzlKA69cnPamBS2vs5bmb396gFOE3G_ozLAi2_S24qIwwWNf9SZFUALazs5F7c6t0Xe9gq1fgxWIvUi0yc5hDo03j4Gko6hBgBcz7qJTKLbKj0axOn57Ml4rWIgRE4c-VZG_FFQHLtrIkgg/w640-h334/hack-android.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW6IXPDSxJE5pTeCn31iaD9JpdptV8OVGIMeVtTPjDsQMBzlKA69cnPamBS2vs5bmb396gFOE3G_ozLAi2_S24qIwwWNf9SZFUALazs5F7c6t0Xe9gq1fgxWIvUi0yc5hDo03j4Gko6hBgBcz7qJTKLbKj0axOn57Ml4rWIgRE4c-VZG_FFQHLtrIkgg/s728/hack-android.jpg)

Appshark is a static [taint analysis](https://www.kitploit.com/search/label/Taint%20Analysis "taint analysis") platform to scan [vulnerabilities](https://www.kitploit.com/search/label/vulnerabilities "vulnerabilities") in an Android app.

## Prerequisites

Appshark requires a specific version of JDK -- [JDK 11](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html "JDK 11"). After testing, it does not work on other LTS versions, JDK 8 and JDK 16, due to the dependency compatibility issue.

## Building/Compiling AppShark

We assume that you are working in the root [directory](https://www.kitploit.com/search/label/Directory "directory") of the project repo. You can build the whole project with the [gradle](https://gradle.org/ "gradle") tool.

```
$ ./gradlew build  -x test
```

After executing the above command, you will see an artifact file `AppShark-0.1.1-all.jar` in the directory `build/libs`.

## Running AppShark

Like the previous step, we assume that you are still in the root folder of the project. You can run the tool with

```
$ java -jar build/libs/AppShark-0.1.1-all.jar  config/config.json5
```

The `config.json5` has the following configuration contents.

```
{
```

Each JSON field is explained below.

* apkPath: the path of the apk file to analyze
* out: the path of the output directory
* rules: the path(s) of the rule file(s), can be more than 1 rules
* maxPointerAnalyzeTime: the timeout duration in seconds set for the analysis started from an entry point
* debugRule: specify the rule name that enables logging for debugging

If you provide a configuration JSON file which sets the output path as `out` in the project root directory, you will find the result file `out/results.json` after running the analysis.

## Interpreting the Results

Below is an example of the `results.json`.

```
{
  "AppInfo": {
    "AppName": "test",
    "PackageName": "net.bytedance.security.app",
    "min_sdk": 17,
    "target_sdk": 28,
    "versionCode": 1000,
    "versionName": "1.0.0"
  },
  "SecurityInfo": {
    "FileRisk": {
      "unZipSlip": {
        "category": "FileRisk",
        "detail": "",
        "model": "2",
        "name": "unZipSlip",
        "possibility": "4",
        "vulners": [
          {
            "details": {
              "position": "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolderFix1(java.lang.String,java.lang.String)>",
              "Sink": "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolderFix1(java.lang.String,java.lang.String)>->$r31",
              "entryMethod": "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void f()>",
              "Source": "<net.byte   dance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolderFix1(java.lang.String,java.lang.String)>->$r3",
              "url": "/Volumes/dev/zijie/appshark-opensource/out/vuln/1-unZipSlip.html",
              "target": [
                "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolderFix1(java.lang.String,java.lang.String)>->$r3",
                "pf{obj{<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolderFix1(java.lang.String,java.lang.String)>:35=>java.lang.StringBuilder}(unknown)->@data}",
                "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolderFix1(java.lang.String,java.lang.String)>->$r11",
                "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolderFix1(java.lang.String,java.lang.String)>->$r31"
              ]
            },
            "hash": "ec57a2a3190677ffe78a0c8aaf58ba5aee4d   2247",
            "possibility": "4"
          },
          {
            "details": {
              "position": "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolder(java.lang.String,java.lang.String)>",
              "Sink": "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolder(java.lang.String,java.lang.String)>->$r34",
              "entryMethod": "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void f()>",
              "Source": "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolder(java.lang.String,java.lang.String)>->$r3",
              "url": "/Volumes/dev/zijie/appshark-opensource/out/vuln/2-unZipSlip.html",
              "target": [
                "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolder(java.lang.String,java.lang.String)>->$r3",
                "pf{obj{<net.bytedance.security.a   pp.pathfinder.testdata.ZipSlip: void UnZipFolder(java.lang.String,java.lang.String)>:33=>java.lang.StringBuilder}(unknown)->@data}",
                "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolder(java.lang.String,java.lang.String)>->$r14",
                "<net.bytedance.security.app.pathfinder.testdata.ZipSlip: void UnZipFolder(java.lang.String,java.lang.String)>->$r34"
              ]
            },
            "hash": "26c6d6ee704c59949cfef78350a1d9aef04c29ad",
            "possibility": "4"
          }
        ],
        "wiki": "",
        "deobfApk": "/Volumes/dev/zijie/appshark-opensource/app.apk"
      }
    }
  },
  "DeepLinkInfo": {
  },
  "HTTP_API": [
  ],
  "JsBridgeInfo": [
  ],
  "BasicInfo": {
    "ComponentsInfo": {
    },
    "JSNativeInterface": [
    ]
  },
  "UsePermissions": [
  ],
  "DefinePermis   sions": {
  },
  "Profile": "/Volumes/dev/zijie/appshark-opensource/out/vuln/3-profiler.json"
}
```

Appshark - Static Taint Analysis Platform To Scan Vulnerabilities In An Android App
![Appshark - Static Taint Analysis Platform To Scan Vulnerabilities In An Android App](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW6IXPDSxJE5pTeCn31iaD9JpdptV8OVGIMeVtTPjDsQMBzlKA69cnPamBS2vs5bmb396gFOE3G_ozLAi2_S24qIwwWNf9SZFUALazs5F7c6t0Xe9gq1fgxWIvUi0yc5hDo03j4Gko6hBgBcz7qJTKLbKj0axOn57Ml4rWIgRE4c-VZG_FFQHLtrIkgg/s72-w640-c-h334/hack-android.jpg)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/11/appshark-static-taint-analysis-platform.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)