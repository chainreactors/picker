---
title: Extraction, Processing, & Querying Apple Unified Logs from an iOS Device
url: https://abrignoni.blogspot.com/2025/05/extraction-processing-querying-apple.html
source: Instapaper: Unread
date: 2025-05-24
fetch_date: 2025-10-06T22:29:55.913012
---

# Extraction, Processing, & Querying Apple Unified Logs from an iOS Device

# [Initialization vectors](https://abrignoni.blogspot.com/)

Digital Forensics and Incident Response. All things InfoSec.

## Sunday, May 18, 2025

### Extraction, Processing, & Querying Apple Unified Logs from an iOS Device

What are Apple Unified Logs and why are they important in my digital forensics examinations?

Introduction

Unified logs keep pattern of life information with a high level of granularity in all Apple devices. Per [Apple's documentation](https://developer.apple.com/documentation/os/logging):

The unified logging system provides a comprehensive and performant API
to capture telemetry across all levels of the system. This system
centralizes the storage of log data in memory and on disk, rather than
writing that data to a text-based log file. You view log messages using
the Console app, `log` command-line tool, or Xcode debug console.

For example these logs, in iOS, keep information on:

* Device orientation (face up, face down.)
* Screen locks and unlocks with biometrics.
* Navigation start with destination address.
* Power on, power off device.
* Horizontal scrolling.
* App opening.
* Apps in focus.

There are many more artifacts of immense forensic value in these logs. Lionel Notari has been aggregating these artifacts at his [ios-unifiedlogs.com](https://www.ios-unifiedlogs.com) webpage. His page is currently the best source for research based unified logs artifact aggregation.

In order to access these artifacts the logs need to be extracted and preserved. The end product of the extraction process will be a .logarchive archive.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4kK_eQmtsvTOIT1-qRyOJC1ET9FiLhyphenhyphen2fItuNrvAtFqCiTUnXwcX7yVcPQkUbvF3YwCGdQ6ZYpa7hj1Q3gsB88POAMYTdum2POQvWuf4UolYLm5Pcswqq3-WicK7z-ROv_VOwSc9ROTu_06rWuTHEeKnCIPID7dcUBZ_RD7aYNFBWCofmGxESYcloVWE/w320-h303/Screenshot%202025-05-18%20at%2010.28.09%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4kK_eQmtsvTOIT1-qRyOJC1ET9FiLhyphenhyphen2fItuNrvAtFqCiTUnXwcX7yVcPQkUbvF3YwCGdQ6ZYpa7hj1Q3gsB88POAMYTdum2POQvWuf4UolYLm5Pcswqq3-WicK7z-ROv_VOwSc9ROTu_06rWuTHEeKnCIPID7dcUBZ_RD7aYNFBWCofmGxESYcloVWE/s354/Screenshot%202025-05-18%20at%2010.28.09%E2%80%AFAM.png) |
| Exemplar .logarchive |

In macOS systems the graphical user interface presents the .logarchive as a single entity. In reality it is a directory that aggregate a number of directories and files.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTMXwjLDYVoxcr0eLGB9Dg5gfjcxrdLCmhk5oOHlnVqH3vp4Blh8-TnBJKvNL8L3sf9NwF2y5lE_-h8y4Uw02xZyonTPqKpwzs09Zd28-cEMTfFZ5buLDDQLFata9hfqr2I5WyGKyKbMgKciKO-i8KfKaQKSF7NSebcTTPolJtkqCVMkVU9eL09BA0MQY/w264-h320/Screenshot%202025-05-18%20at%2010.33.18%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTMXwjLDYVoxcr0eLGB9Dg5gfjcxrdLCmhk5oOHlnVqH3vp4Blh8-TnBJKvNL8L3sf9NwF2y5lE_-h8y4Uw02xZyonTPqKpwzs09Zd28-cEMTfFZ5buLDDQLFata9hfqr2I5WyGKyKbMgKciKO-i8KfKaQKSF7NSebcTTPolJtkqCVMkVU9eL09BA0MQY/s894/Screenshot%202025-05-18%20at%2010.33.18%E2%80%AFAM.png) |
| Contents of a .logarchive |

 These directories and files are aggregated from the **/private/var/db/diagnostics** and **/private/var/db/uuidtext** directories in an iOS device. It is of note that the uuidtext directory contains support files while the diagnostic directory contains .tracev3 files.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjThotnMBITKWeXNx_Wl7_ShxMQpLq0_LXnaJAvToKmszSd5sk8-9RgP0p66qi6ZtK68nLfR-Cdbl21afofaKvJOr-tGHM3POo0ujaXhJjhj2ASYWrQCD-a70FWjXqD9N9NQs7v7xORXCLrqAhXwr01FpX0RviKFK_LhFMQg199ju1W0SXFFtzRAW7i2hE/w303-h400/Screenshot%202025-05-18%20at%2010.40.51%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjThotnMBITKWeXNx_Wl7_ShxMQpLq0_LXnaJAvToKmszSd5sk8-9RgP0p66qi6ZtK68nLfR-Cdbl21afofaKvJOr-tGHM3POo0ujaXhJjhj2ASYWrQCD-a70FWjXqD9N9NQs7v7xORXCLrqAhXwr01FpX0RviKFK_LhFMQg199ju1W0SXFFtzRAW7i2hE/s822/Screenshot%202025-05-18%20at%2010.40.51%E2%80%AFAM.png) |
| Exemplar .tracev3 files |

There are different extraction methods we can use.

Extraction

In order to extract the logs we can do one of the following:

* Connect an iOS device to a macOS computer and use the log collect command at the terminal.

+ Open a terminal and execute "sudo log collect --device --output /path/to/filename.logarchive"
+ A useful flowchart for this process has been provide by Tim Korver and can be found at [github.com/Ankan-42/Apple-Unified-Log](https://github.com/Ankan-42/Apple-Unified-Log)

* Use third-party tools like UFADE or the iOS Logs Acquisition Tool.

+ UFADE (Universal Forensics Apple Device Extractor) by Christian Peter can be downloaded at [github.com/prosch88/UFADE](https://github.com/prosch88/UFADE)
+ iOS Logs Acquisition Tool by Lionel Notari can be downloaded at [www.ios-unifiedlogs.com/iosunifiedlogtool](https://www.ios-unifiedlogs.com/iosunifiedlogtool)

* Extracting the log files from a full file system extraction.

There are a few steps to follow in order to generate a .logarchive from files directly pulled from an iOS full file system extraction. This information in this section was kindly provided by Resarcher [Johann Polewczyk](https://www.linkedin.com/in/johann-polewczyk-6a905425%20) of the Université de Lausanne.

1. Extract contents (all subdirectories and files) of diagnostics and uuidtext folders and place them in the root of a directory.
2. Create an Info.plist file and put it in the root of the directory.
   Exemplar plist:

   <?xml version="1.0" encoding="UTF-8"?>

   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST
   1.0//EN"

      "<http://www.apple.com/DTDs/PropertyList-1.0.dtd>">

   <plist version="1.0">

   <dict>

       <key>OSArchiveVersion</key>

       <integer>4</integer>

   </dict>

   </plist>
3. Must include Info.plist with OSArchiveVersion for compatibility.
   The integer under the OSArchiveVersion must align with the iOS or OS version from source.

   [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-7ShnDIym7ZqvsHKfEB5SSSIMHbAcPezUcV5R2sh8RMM5GW2O2hcgbVbNkgC61mXT5ed0JyLoPc3rTLGZLYE_fzuBlXOJno0jLv73OlWnF6zxX5EqVaXZTdSKkSyU0iHij69SW1xKBkRq0X7QOblXwqrVXSTNCktlSghW3VZMm6XPgVR_h1IVlIlAmr4/s320/Screenshot%202025-05-18%20at%2011.01.13%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-7ShnDIym7ZqvsHKfEB5SSSIMHbAcPezUcV5R2sh8RMM5GW2O2hcgbVbNkgC61mXT5ed0JyLoPc3rTLGZLYE_fzuBlXOJno0jLv73OlWnF6zxX5EqVaXZTdSKkSyU0iHij69SW1xKBkRq0X7QOblXwqrVXSTNCktlSghW3VZMm6XPgVR_h1IVlIlAmr4/s1054/Screenshot%202025-05-18%20at%2011.01.13%E2%80%AFAM.png)
4. Add .logarchive to the end of the directoy name.

On macOS, with the .logarchive extension, the target folder is seen as a bundle you can open with the Console App or parse from the Terminal with the log show command. I have yet found a way to effectively produce reports from the Console app and working with the log show command is not as productive as I would need it to be. In order to query the data more effectively the data had to be converted into another format. It is also important to note that most examiners work in Windows based environments and having to use macOS devices for the querying and reporting might not be practical. In response we developed a way to query the logs outside macOS using [iLEAPP](https://github.com/abrignoni/iLEAPP).

Querying Apple Unified Logs

In this process the macOS device will be used only to convert the .logarchive to a JSON file. This would mean the examiner can use a single macOS device to do the conversions while querying and reporting on Windows based systems. Even though there are third-party scripts that provide a .logarchive to JSON conversion, we have decided that conversion via a macOS device itself is the more suitable and traceable way to make a conversion. Unlike third-party conversion tooling the macOS based process keeps the Apple key names intact and since it is an Apple device using Apple conver...