---
title: GLiNet Router Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2024030009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-03-07
fetch_date: 2025-10-06T17:08:08.796134
---

# GLiNet Router Authentication Bypass

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
|  |  | |  | | --- | | **GLiNet Router Authentication Bypass** **2024.03.06**  Credit:  **[Daniele 'dzonerzy' Linguaglossa](https://cxsecurity.com/author/Daniele%2B%26%23039%3Bdzonerzy%26%23039%3B%2BLinguaglossa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-46453](https://cxsecurity.com/cveshow/CVE-2023-46453/ "Click to see CVE-2023-46453")**  CWE: **N/A** | |

DZONERZY Security Research
GLiNet: Router Authentication Bypass
========================================================================
Contents
========================================================================
1. Overview
2. Detailed Description
3. Exploit
4. Timeline
========================================================================
1. Overview
========================================================================
CVE-2023-46453 is a remote authentication bypass vulnerability in the web
interface of GLiNet routers running firmware versions 4.x and up. The
vulnerability allows an attacker to bypass authentication and gain access
to the router's web interface.
========================================================================
2. Detailed Description
========================================================================
The vulnerability is caused by a lack of proper authentication checks in
/usr/sbin/gl-ngx-session file. The file is responsible for authenticating
users to the web interface. The authentication is in different stages.
Stage 1:
During the first stage the user send a request to the challenge rcp
endpoint. The endpoint returns a random nonce value used later in the
authentication process.
Stage 2:
During the second stage the user sends a request to the login rcp endpoint
with the username and the encrypted password. The encrypted password is
calculated by the following formula:
md5(username + crypt(password) + nonce)
The crypt function is the standard unix crypt function.
The vulnerability lies in the fact that the username is not sanitized
properly before being passed to the login\_test function in the lua script.
------------------------------------------------------------------------
local function login\_test(username, hash)
if not username or username == "" then return false end
for l in io.lines("/etc/shadow") do
local pw = l:match('^' .. username .. ':([^:]+)')
if pw then
for nonce in pairs(nonces) do
if utils.md5(table.concat({username, pw, nonce}, ":")) ==
hash then
nonces[nonce] = nil
nonce\_cnt = nonce\_cnt - 1
return true
end
end
return false
end
end
return false
end
------------------------------------------------------------------------
This script check the username against the /etc/shadow file. If the username
is found in the file the script will extract the password hash and compare
it to the hash sent by the user. If the hashes match the user is
authenticated.
The issue is that the username is not sanitized properly before being
concatenated with the regex. This allows an attacker to inject a regex into
the username field and modify the final behavior of the regex.
for instance, the following username will match the userid of the root user:
root:[^:]+:[^:]+ will become root:[^:]+:[^:]+:([^:]+)
This will match the "root:" string and then any character until the next ":"
character. This will cause the script skip the password and return the
user id instead.
Since the user id of the root user is always 0, the script will always
return:
md5("root:[^:]+:[^:]+" + "0" + nonce)
Since this value is always the same, the attacker can simply send the known
hash value to the login rcp endpoint and gain access to the web interface.
Anyway this approach won't work as expected since later in the code inside
the
this check appear:
------------------------------------------------------------------------
local aclgroup = db.get\_acl\_by\_username(username)
local sid = utils.generate\_id(32)
sessions[sid] = {
username = username,
aclgroup = aclgroup,
timeout = time\_now() + session\_timeout
}
------------------------------------------------------------------------
The username which is now our custom regex will be passed to the
get\_acl\_by\_username
function. This function will check the username against a database and
return the aclgroup associated with the username.
If the username is not found in the database the function will return nil,
thus causing attack to fail.
By checking the code we can see that the get\_acl\_by\_username function is
actually appending our raw string to a query and then executing it.
This means that we can inject a sql query into the username field and
make it return a valid aclgroup.
------------------------------------------------------------------------
M.get\_acl\_by\_username = function(username)
if username == "root" then return "root" end
local db = sqlite3.open(DB)
local sql = string.format("SELECT acl FROM account WHERE username =
'%s'", username)
local aclgroup = ""
for a in db:rows(sql) do
aclgroup = a[1]
end
db:close()
return aclgroup
end
------------------------------------------------------------------------
Using this payload we were able to craft a username which is both a valid
regex and a valid sql query:
roo[^'union selecT char(114,111,111,116)--]:[^:]+:[^:]+
this will make the sql query become:
SELECT acl FROM account WHERE username = 'roo[^'union selecT
char(114,111,111,116)--]:[^:]+:[^:]+'
which will return the aclgroup of the root user (root).
========================================================================
3. Exploit
========================================================================
------------------------------------------------------------------------
# Exploit Title: [CVE-2023-46453] GL.iNet - Authentication Bypass
# Date: 18/10/2023
# Exploit Author: Daniele 'dzonerzy' Linguaglossa
# Vendor Homepage: https://www.gl-inet.com/
# Vulnerable Devices:
# GL.iNet GL-MT3000 (4.3.7)
# GL.iNet GL-AR300M(4.3.7)
# GL.iNet GL-B1300 (4.3.7)
# GL.iNet GL-AX1800 (4.3.7)
# GL.iNet GL-AR750S (4.3.7)
# GL.iNet GL-MT2500 (4.3.7)
# GL.iNet GL-AXT1800 (4.3.7)
# GL.iNet GL-X3000 (4.3.7)
# GL.iNet GL-SFT1200 (4.3.7)
# And many more...
#...