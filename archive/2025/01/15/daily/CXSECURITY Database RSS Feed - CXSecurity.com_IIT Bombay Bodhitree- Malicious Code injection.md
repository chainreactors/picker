---
title: IIT Bombay Bodhitree- Malicious Code injection
url: https://cxsecurity.com/issue/WLB-2025010016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-15
fetch_date: 2025-10-06T20:04:46.244459
---

# IIT Bombay Bodhitree- Malicious Code injection

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
|  |  | |  | | --- | | **IIT Bombay Bodhitree- Malicious Code injection** **2025.01.14**  Credit:  **[Koushal S Kedar](https://cxsecurity.com/author/Koushal%2BS%2BKedar/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **[CVE-2024-48818](https://cxsecurity.com/cveshow/CVE-2024-48818/ "Click to see CVE-2024-48818")**  CWE: **N/A** | |

# Exploit Title: IIT Bombay Bodhitree- Malicious Code Injection
# Date: 30-12-2024
# Exploit Author: Koushal S Kedari
# Vendor Homepage: https://cs101.bodhi.cse.iitb.ac.in/
# Version: cs101
# CVE: CVE-2024-48818
# Tested on: Ubuntu, Windows
-------------------------------------------------------------------------------------------------------------------------------------------
This vulnerability exists in the IIT Bombay Bodhitree platform, allowing attackers to inject malicious code in the online code compiler. The exploit can lead to Remote Code Execution (RCE), system takeover, privilege escalation, and sensitive data exposure. The vulnerability arises from improper input validation and a lack of restrictions on user processes, enabling attackers to traverse directories and escalate privileges.
---> Affected Component: Code editor and compiler at `http://cs101.bodhi.cse.iitb.ac.in/assignments/editor/4`
Steps to reproduce:
1) Login into cs101 account under Bodhitree.
2) Head to your course.
3) Once you have entered your course page, Navigate to Assignments.
4) Click on programing labs.
5) Choose your lab based on the language.
6) Go to live editor button.
7) Tailor a code that leads to directory traversal or RCE.
8) Execute the code and check the output below in the output box.
"Suggested Mitigation strategy":
To mitigate the risk of malicious code injection and system compromise, implement the following:
- Use safe execution environments such as `chroot` or Docker containers to sandbox code execution.
- Enforce strong input sanitization to ensure user-provided inputs are safe.
- Use the principle of least privilege to restrict access to critical system resources.
Suggested Implementation (Using `chroot`):
- Set up a `chroot` jail to restrict code execution.
- Copy only required executables and libraries into the jail.
- Use `sudo chroot` to isolate the execution process from the rest of the system.
```python
import os
import shutil
import subprocess
def setup\_chroot(jail\_dir, executable\_path):
try:
# Create chroot directory
if not os.path.exists(jail\_dir):
os.makedirs(jail\_dir)
# Copy executable into jail
executable\_name = os.path.basename(executable\_path)
chroot\_executable\_path = os.path.join(jail\_dir, executable\_name)
shutil.copy(executable\_path, chroot\_executable\_path)
# Set executable permissions
os.chmod(chroot\_executable\_path, 0o755)
except Exception as e:
print(f"Error during setup: {e}")
def execute\_in\_chroot(jail\_dir, executable\_name):
try:
subprocess.run(['sudo', 'chroot', jail\_dir, f'./{executable\_name}'], check=True)
except subprocess.CalledProcessError as e:
print(f"Execution failed: {e}")
except Exception as e:
print(f"Unexpected error: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
jail\_directory = "/tmp/chroot\_jail"
executable = "/bin/ls"
setup\_chroot(jail\_directory, executable)
execute\_in\_chroot(jail\_directory, "ls")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010016)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top