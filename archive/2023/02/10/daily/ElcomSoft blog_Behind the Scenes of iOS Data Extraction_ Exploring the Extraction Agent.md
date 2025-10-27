---
title: Behind the Scenes of iOS Data Extraction: Exploring the Extraction Agent
url: https://blog.elcomsoft.com/2023/02/behind-the-scenes-of-ios-data-extraction-exploring-the-extraction-agent/
source: ElcomSoft blog
date: 2023-02-10
fetch_date: 2025-10-04T06:12:24.888814
---

# Behind the Scenes of iOS Data Extraction: Exploring the Extraction Agent

«…Everything you wanted to know about password recovery, data decryption, mobile & cloud forensics…»

[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/icons/facebook.png)](https://www.facebook.com/elcomsoft)
[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/icons/twitter.png)](https://twitter.com/elcomsoft)
[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/icons/telegram.png)](https://telegram.me/elcomsoft)
[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/icons/linkedin.png)](https://www.linkedin.com/company/152541/)
[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/icons/reddit.png)](https://www.reddit.com/user/Elcomsoft/)
[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/icons/instagram.png)](https://www.instagram.com/elcomsoft/)
[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/icons/youtube.png)](https://www.youtube.com/elcomsoftcompany)

* [Home](/)
* [Categories](/products.html)
  + [General](https://blog.elcomsoft.com/category/general/)
  + [Elcomsoft News](https://blog.elcomsoft.com/category/elcom-news/ "Elcomsoft news")
  + [Security](https://blog.elcomsoft.com/category/old/security/)
  + [Mobile](https://blog.elcomsoft.com/category/mobile-devices/ "All about mobile devices and technologies")
  + [Software](https://blog.elcomsoft.com/category/old/software/)
* [Tags](/events.html)
  + [EIFT](https://blog.elcomsoft.com/tag/eift/ "EIFT")
  + [iOS](https://blog.elcomsoft.com/tag/ios/ "iOS")
  + [Elcomsoft iOS Forensic Toolkit](https://blog.elcomsoft.com/tag/elcomsoft-ios-forensic-toolkit/ "Elcomsoft iOS Forensic Toolkit")
  + [iCloud](https://blog.elcomsoft.com/tag/icloud/ "iCloud")
  + [Elcomsoft Phone Breaker](https://blog.elcomsoft.com/tag/elcomsoft-phone-breaker/ "Elcomsoft Phone Breaker")
  + [EDPR](https://blog.elcomsoft.com/tag/edpr/ "EDPR")
  + [EPB](https://blog.elcomsoft.com/tag/epb/ "EPB")
  + [Apple](https://blog.elcomsoft.com/tag/apple/ "Apple")
  + [password recovery](https://blog.elcomsoft.com/tag/password-recovery/ "password recovery")
  + [Elcomsoft Phone Viewer](https://blog.elcomsoft.com/tag/elcomsoft-phone-viewer/ "Elcomsoft Phone Viewer")
* [Tips & Tricks](/partners/index.html)
  + [Apple Face ID: Security Implications and Potential Vulnerabilities](https://blog.elcomsoft.com/2025/09/apple-face-id-security-implications-and-potential-vulnerabilities/ "Apple Face ID: Security Implications and Potential Vulnerabilities")
  + [Installing and Troubleshooting the Extraction Agent (2025)](https://blog.elcomsoft.com/2025/07/installing-and-troubleshooting-the-extraction-agent-2025/ "Installing and Troubleshooting the Extraction Agent (2025)")
  + [Extracting and Analyzing Apple sysdiagnose Logs](https://blog.elcomsoft.com/2025/06/extracting-and-analyzing-apple-unified-logs/ "Extracting and Analyzing Apple sysdiagnose Logs")
  + [Apple Ecosystem: Overlooked Devices](https://blog.elcomsoft.com/2025/06/apple-ecosystem-overlooked-devices/ "Apple Ecosystem: Overlooked Devices")
  + [What TRIM, DRAT, and DZAT Really Mean for SSD Forensics](https://blog.elcomsoft.com/2025/06/what-trim-drat-and-dzat-really-mean-for-ssd-forensics/ "What TRIM, DRAT, and DZAT Really Mean for SSD Forensics")
  + [iOS Extraction Tip: Why Start with Recovery Mode?](https://blog.elcomsoft.com/2025/05/ios-extraction-tip-why-start-with-recovery-mode/ "iOS Extraction Tip: Why Start with Recovery Mode?")
  + [Why Every Digital Forensics Lab Needs a Good USB Hub](https://blog.elcomsoft.com/2025/05/why-every-digital-forensics-lab-needs-a-good-usb-hub/ "Why Every Digital Forensics Lab Needs a Good USB Hub")
  + [Installing iOS Forensic Toolkit on Linux](https://blog.elcomsoft.com/2025/05/installing-ios-forensic-toolkit-on-linux/ "Installing iOS Forensic Toolkit on Linux")
  + [iOS Forensic Toolkit Now Supports All Models of Apple Watch](https://blog.elcomsoft.com/2025/05/ios-forensic-toolkit-now-supports-all-models-of-apple-watch/ "iOS Forensic Toolkit Now Supports All Models of Apple Watch")
  + [Extraction Agent: Offline Extraction with All Developer Accounts](https://blog.elcomsoft.com/2025/05/extraction-agent-offline-extraction-with-all-developer-accounts/ "Extraction Agent: Offline Extraction with All Developer Accounts")
  + [More...](https://blog.elcomsoft.com/category/tips-tricks/ "More...")
* [Events](/events/)

* [Official site](https://www.elcomsoft.com)
* [About us](https://www.elcomsoft.com/company.html)

[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/avatars/elcomsoft.png)](/)

* [Home](/)
* [Categories](/products.html)
  + [General](https://blog.elcomsoft.com/category/general/)
  + [Elcomsoft News](https://blog.elcomsoft.com/category/elcom-news/ "Elcomsoft news")
  + [Security](https://blog.elcomsoft.com/category/old/security/)
  + [Mobile](https://blog.elcomsoft.com/category/mobile-devices/ "All about mobile devices and technologies")
  + [Software](https://blog.elcomsoft.com/category/old/software/)
* [Tags](/events.html)
  + [EIFT](https://blog.elcomsoft.com/tag/eift/ "EIFT")
  + [iOS](https://blog.elcomsoft.com/tag/ios/ "iOS")
  + [Elcomsoft iOS Forensic Toolkit](https://blog.elcomsoft.com/tag/elcomsoft-ios-forensic-toolkit/ "Elcomsoft iOS Forensic Toolkit")
  + [iCloud](https://blog.elcomsoft.com/tag/icloud/ "iCloud")
  + [Elcomsoft Phone Breaker](https://blog.elcomsoft.com/tag/elcomsoft-phone-breaker/ "Elcomsoft Phone Breaker")
  + [EDPR](https://blog.elcomsoft.com/tag/edpr/ "EDPR")
  + [EPB](https://blog.elcomsoft.com/tag/epb/ "EPB")
  + [Apple](https://blog.elcomsoft.com/tag/apple/ "Apple")
  + [password recovery](https://blog.elcomsoft.com/tag/password-recovery/ "password recovery")
  + [Elcomsoft Phone Viewer](https://blog.elcomsoft.com/tag/elcomsoft-phone-viewer/ "Elcomsoft Phone Viewer")
* [Tips & Tricks](/partners/index.html)
  + [Apple Face ID: Security Implications and Potential Vulnerabilities](https://blog.elcomsoft.com/2025/09/apple-face-id-security-implications-and-potential-vulnerabilities/ "Apple Face ID: Security Implications and Potential Vulnerabilities")
  + [Installing and Troubleshooting the Extraction Agent (2025)](https://blog.elcomsoft.com/2025/07/installing-and-troubleshooting-the-extraction-agent-2025/ "Installing and Troubleshooting the Extraction Agent (2025)")
  + [Extracting and Analyzing Apple sysdiagnose Logs](https://blog.elcomsoft.com/2025/06/extracting-and-analyzing-apple-unified-logs/ "Extracting and Analyzing Apple sysdiagnose Logs")
  + [Apple Ecosystem: Overlooked Devices](https://blog.elcomsoft.com/2025/06/apple-ecosystem-overlooked-devices/ "Apple Ecosystem: Overlooked Devices")
  + [What TRIM, DRAT, and DZAT Really Mean for SSD Forensics](https://blog.elcomsoft.com/2025/06/what-trim-drat-and-dzat-really-mean-for-ssd-forensics/ "What TRIM, DRAT, and DZAT Really Mean for SSD Forensics")
  + [iOS Extraction Tip: Why Start with Recovery Mode?](https://blog.elcomsoft.com/2025/05/ios-extraction-tip-why-start-with-recovery-mode/ "iOS Extraction Tip: Why Start with Recovery Mode?")
  + [Why Every Digital Forensics Lab Needs a Good USB Hub](https://blog.elcomsoft.com/2025/05/why-every-digital-forensics-lab-needs-a-good-usb-hub/ "Why Every Digital Forensics Lab Needs a Good USB Hub")
  + [Installing iOS Forensic Toolkit on Linux](https://blog.elcomsoft.com/2025/05/installing-ios-forensic-toolkit-on-linux/ "Installing iOS Forensic Toolkit on Linux")
  + [iOS Forensic Toolkit Now Supports All Models of Apple Watch](https://blog.elcomsoft.com/2025/05/ios-forensic-toolkit-now-supports-all-models-of-apple-watch/ "iOS Forensic Toolkit Now Supports All Models of Apple Watch")
  + [Extraction Agent: Offline Extraction with All Developer Accounts](https://blog.elcomsoft.com/2025/05/extraction-agent-offline-extraction-with-all-developer-accounts/ "Extraction Agent: Offline Extraction with All Developer Accounts")
  + [More...](https://blog.elcomsoft.c...