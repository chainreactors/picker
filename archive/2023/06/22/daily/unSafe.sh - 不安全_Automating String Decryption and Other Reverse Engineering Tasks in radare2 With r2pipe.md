---
title: Automating String Decryption and Other Reverse Engineering Tasks in radare2 With r2pipe
url: https://buaq.net/go-169773.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:31.174997
---

# Automating String Decryption and Other Reverse Engineering Tasks in radare2 With r2pipe

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

![](https://8aqnet.cdn.bcebos.com/04cd7f4952f934bd13315292a41b0628.jpg)

Automating String Decryption and Other Reverse Engineering Tasks in radare2 With r2pipe

In the previous post in this series, we looked at powering up radare2 with aliases and macros to ma
*2023-6-21 21:52:53
Author: [www.sentinelone.com(查看原文)](/jump-169773.htm)
阅读量:24
收藏*

---

In the [previous post](https://www.sentinelone.com/labs/radare2-power-ups-delivering-faster-macos-malware-analysis-with-r2-customization/) in this series, we looked at powering up radare2 with aliases and macros to make our work more productive, but sometimes we need the ability to automate more complex tasks, extend our analyses by bringing in other tools, or process files in batches. Most reverse engineering platforms have some kind of scripting engine to help achieve this kind of heavy lifting and radare2 does, too. In this post, we’ll learn how to drive radare2 with r2pipe and tackle three different challenges that are common to RE automation: decrypting strings, applying comments, and processing files in batches.

## Scripting radare2 with C, Go, Swift, Perl, Python, Ruby…

No matter what language you’re most comfortable working in, there’s a good chance that r2pipe supports it. There are 22 supported languages, though they are not all supported equally.

![Programming languages supported by radare2’s r2pipe](https://www.sentinelone.com/wp-content/uploads/2023/06/r2pipe_5.jpg)

C, NodeJS, Python and Swift are the most well-supported languages, but I tend to use Go for speed and brevity, and it lets me hack scripts together rather haphazardly to achieve what I need. When scripting your own reversing sessions, there’s little need to worry about the niceties of programming style or convention as we would do when shipping code for production or other purposes. Although performance can be improved by doing things in one language rather than another, that’s something I rarely need to worry about in practice in my reversing work.

All that’s a preamble to saying that you can – and probably should! – write better scripts than those I’ll show here, but these examples will serve as a good introduction to how you can easily hack your way around problems thanks to r2’s shell integration to get a working solution without worrying too much about “the right” or “the best” way to do it.

## Automated String Decryption in OSX.Fairytale

We’ll use a sample of [OSX.Fairytale](https://malshare.com/sample.php?action=detail&hash=a9a7a1c48cd1232249336749f4252c845ce68fd9e7da85b6da6ccbcdc21bcf66) to illustrate automated string decryption. Though I’ll be using Go, you can easily apply the same techniques in whatever other language you prefer.

Like many simple malware families, Fairytale encrypts strings with a combination of base64 and a hard coded XOR key. In this case, the XOR key is 0x30.

![OSX.Fairytale uses 0x30 as a hard coded key for XOR decryption](https://www.sentinelone.com/wp-content/uploads/2023/06/r2pipe_2.jpg)

OSX.Fairytale uses 0x30 as a hard coded key for XOR decryption

Once we have determined the XOR key, there’s various simple ways to decrypt a given string or even the whole binary (e.g., [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR(%7B'option':'Hex','string':''%7D,'Standard',false)), or writing your own [decryption function](https://www.sentinelone.com/labs/techniques-for-string-decryption-in-macos-malware-with-radare2/)), but our eventual aim is to add comments to the disassembly (as well as learn a few useful tricks), so we’ll take a different approach.

Note that radare2 comes with a useful little tool called `rahash2` , which among other things, can decrypt strings. Here’s an example you can run on the command line:

```
% rahash2 -D base64 -s 'H1JZXh9cUUVeU1hTRFw=' | rahash2 -D xor -S 0x30 -
/bin/launchctl%
```

As we discussed in the previous post, we could easily make this into a [function](https://www.sentinelone.com/labs/radare2-power-ups-delivering-faster-macos-malware-analysis-with-r2-customization/) in our `.zshrc` file. However, one drawback with that approach is r2 won’t let us call such functions from the r2 prompt. We can solve that by creating a standalone executable and saving it in our path, like so:

```
#!/bin/zsh
if [ "$#" -eq 2 ]; then
	echo $(rahash2 -D xor -S $1 -s $2)
elif [ "$#" -eq 3 ]; then
	echo $(rahash2 -D base64 -s $3 | rahash2 -D xor -S $2 -)
elif [ "$#" -eq 1 ]; then
	echo "
		  # USAGE:
			# rxorb
			# rxorb 0x30 "\|YRBQBI"
			# Use '-b' to base64 decode the string before the xor
			# rxorb -b 0x30 FXAffFlSQlFCSR98UUVeU1hxV1VeREMfFXAeQFxZQ0Q=
		"
else
	echo "INPUT ERROR, type 'rxorb help' for help."
fi
```

Saving this as `/usr/local/bin/rxorb` and giving it executable permissions (e.g., via `chmod +X`) will now make this available to us both on the command line and from within r2, once we open a new shell and new r2 session.

![Calling rxorb from within r2 to decrypt individual strings](https://www.sentinelone.com/wp-content/uploads/2023/06/r2pipe_4-1024x273.jpg)

Calling *rxorb* from within r2 to decrypt individual strings

Great, we now have a general string decryption tool that we can feed a string, a key and cipher text and we are able to specify whether the cipher needs to be base64 decoded before being XOR’d with the given key. This alone will take care of a lot of use cases!

However, while this works well for manual decryption, it becomes tedious for anything more than a few strings. What would be much better is if we could simply type one command that would iterate over encrypted strings in the binary and either print out all the decrypted text or comment the code where the string is referenced. Ideally, our solution should give us the option to do both.

Let’s see how we can implement that by leveraging radare2’s scripting engine, r2pipe (*aka* `r2p`).

## Building the Script

We’ll call the Go program “decode.go”, and the first part of it requires importing the r2pipe package from github.

```
package main
import (
  "fmt"
  "github.com/radareorg/r2pipe-go"
)

var r2p, _ = r2pipe.NewPipe("") 	// Declare r2p as a global

func check(err error) {
     if err != nil {
	panic(err)
     }
}
```

After the imports, we declare a global variable `r2p`, which provides a pipe to the r2 instance when we call it from within an r2 session. This global will allow us to send and receive commands to the r2 session. We also implement a generic error function for use throughout the code.

Next, we’ll implement a decrypt function. We could (and probably should) write a native version of this, but since we already have a decrypt function using `rahash2` above, we’ll reuse that. This will also allow us to see and solve some other common challenges we might face in other scenarios.

```
func decryptStrAtLoc(loc string, key string) {
     bytes := fmt.Sprintf("ps @ %s", loc) 		// [1]
     str, err := r2p.Cmd(bytes)
     check(err)
     decodeCmd := fmt.Sprintf("!rxorb -b %s %s > /tmp/rxorb", key, str) // [2]
     r2p.Cmd(decodeCmd)
}
```

The `decryptStrAtLoc()` function does most of the work in our program. As parameters, it takes an address and the XOR key. We’ve chosen not to return the decrypted string to the caller but instead consume it within the function. We’ll see why shortly.

For each command we want to pass to the r2 session, we first format the command as a string, then pass the command to `r2p`. Thus, [1] formats a command that returns the bytes at the current address as a string. At [2], we format a command that decodes the string by passing it to the `rxorb` util...