---
title: Bashfuscator - A Fully Configurable And Extendable Bash Obfuscation Framework
url: https://buaq.net/go-172999.html
source: unSafe.sh - 不安全
date: 2023-07-27
fetch_date: 2025-10-04T11:52:51.641427
---

# Bashfuscator - A Fully Configurable And Extendable Bash Obfuscation Framework

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

![](https://8aqnet.cdn.bcebos.com/4fbeb70f1d6b74942630f23bb2201211.jpg)

Bashfuscator - A Fully Configurable And Extendable Bash Obfuscation Framework

Documentation What is Bashfuscator? Bashfuscator is a modular and extendable Bash obfuscat
*2023-7-26 21:41:0
Author: [www.kitploit.com(查看原文)](/jump-172999.htm)
阅读量:45
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjMEBNVJCDy38EF1sI9SYqTG1-Tr08gwus315k8MRKnrghvat2RWQyVKP9MPCyX9gDxVvDZiVKNVl6nEmdzbnFNFi541YEPbzZAFm44SPFQLFbyuedDB2U2NcAGxCHtXSZ0njRImTPLCR-Mng-ee2cnCpEU5o2RpMHuvOCrRFhKAv4iZZcL49MwwkE4f_mj=w640-h128)](https://blogger.googleusercontent.com/img/a/AVvXsEjMEBNVJCDy38EF1sI9SYqTG1-Tr08gwus315k8MRKnrghvat2RWQyVKP9MPCyX9gDxVvDZiVKNVl6nEmdzbnFNFi541YEPbzZAFm44SPFQLFbyuedDB2U2NcAGxCHtXSZ0njRImTPLCR-Mng-ee2cnCpEU5o2RpMHuvOCrRFhKAv4iZZcL49MwwkE4f_mj)

[Documentation](https://bashfuscator.readthedocs.io/en/latest/index.html "Documentation")

## What is Bashfuscator?

Bashfuscator is a modular and extendable Bash [obfuscation](https://www.kitploit.com/search/label/Obfuscation "obfuscation") framework written in Python 3. It provides numerous different ways of making Bash one-liners or scripts much more difficult to understand. It accomplishes this by generating convoluted, randomized Bash code that at runtime evaluates to the original input and executes it. Bashfuscator makes generating highly obfuscated Bash commands and scripts easy, both from the [command line](https://www.kitploit.com/search/label/Command%20Line "command line") and as a Python library.

The purpose of this project is to give [Red Team](https://www.kitploit.com/search/label/Red%20Team "Red Team") the ability to bypass static detections on a Linux system, and the knowledge and tools to write better Bash obfuscation techniques.

This framework was also developed with [Blue Team](https://www.kitploit.com/search/label/Blue%20Team "Blue Team") in mind. With this framework, Blue Team can easily generate thousands of unique obfuscated scripts or commands to help create and test detections of Bash obfuscation.

### Media/slides

This is a list of all the media (i.e. youtube videos) or links to slides about Bashfuscator.

* [Bsides Charm](https://www.youtube.com/watch?v=zef422NDmpo "Bsides Charm")

### Payload support

Though Bashfuscator does work on UNIX systems, many of the payloads it generates will not. This is because most UNIX systems use BSD style utilities, and Bashfuscator was built to work with GNU style utilities. In the future BSD payload support may be added, but for now payloads generated with Bashfuscator should work on GNU Linux systems with Bash 4.0 or newer.

## Installation & Requirements

Bashfuscator requires Python 3.6+.

On a Debian-based distro, run this command to install dependencies:

`sudo apt-get update && sudo apt-get install python3 python3-pip python3-argcomplete xclip`

On a RHEL-based distro, run this command to install dependencies:

`sudo dnf update && sudo dnf install python3 python3-pip python3-argcomplete xclip`

Then, run these commands to clone and install Bashfuscator:

```
git clone https://github.com/Bashfuscator/Bashfuscator
```

Only Debian and RHEL based distros are supported. Bashfuscator has been tested working on some UNIX systems, but is not supported on those systems.

## Example Usage

For simple usage, just pass the command you want to obfuscate with `-c`, or the script you want to obfuscate with `-f`.

```
$ bashfuscator -c "cat /etc/passwd"
[+] Mutators used: Token/ForCode -> Command/Reverse
[+] Payload:

${@/l+Jau/+<b=k } p''"r"i""n$'t\u0066'  %s  "$(      ${*%%Frf\[4?T2   }  ${*##0\!j.G }   "r"'e'v <<< '   "} ~@{$"   ")  }  [email protected]`\7=-k#*{$   "}   ,@{$"  ; }  ;   } ,,*{$  "}]  }   ,*{$  "}   f9deh`\>6/J-F{\,vy//@{$" niOrw$   } QhwV#@{$ [NMpHySZ{$"  s%  "f"'"'"'4700u\n9600u\r'"'"'$p  {   ;  }  ~*{$  "}  48T`\PJc}\#@{$"   1#31  "}  ,@{$"   }  D$y?U%%*{$ 0#84  *$   }   Lv:sjb/@{$   2#05   }   ~@{$   2#4   }*!{$  }   OGdx7=um/[email protected]{\eA/*{$ 1001#2   }   Scnw:i/@{$  } ~~*{$  11#4   "} O#uG{\HB%@{$"   11#7 "} ^^@{$"  011#2   "}   ~~@{$" 11#3 }  L[\h3m/@{$  "}   ~@{$" 11#2 }  6u1N.b!\b%%*{$   }   YCMI##@{$   31#5 "} ,@{$" 01#7  }  (\}\;]\//*{$ }   %#6j/?pg%m/*{$   001#2  "}  6IW]\p*n%@{$"   }  ^^@{$ 21#7  } !\=jy#@{$  }   tz}\k{\v1/?o:[email protected]/*{$  11#5   ni   niOrw  rof ;   "}   ,,@{$"  } MD`\!\]\P%%*{$      )  }@{$   a   }  ogt=y%*{$ "@$" /\   }   {\nZ2^##*{$    \   *$  c  }@{$  }   h;|Yeen{\/.8oAl-RY//@{$   p  *$  "}@{$"  t   }  zB(\R//*{$  } mX=XAFz_/9QKu//*{$  e   *$  s  } ~~*{$  d   }  ,*{$   }  2tgh%X-/L=a_r#f{\//*{$   w }  {\L8h=@*##@{$   "}   W9Zw##@{$"  (=NMpHySZ    ($"  la'"'"''"'"'"v"'"'"''"'"''"'"'541\'"'"'$  } &;@0#*{$ '   "${@}" "${@%%Ij\[N   }"    ${@~~  }   )"  ${!*} |   $@  $'b\u0061'''sh   ${*//J7\{=.QH   }

[+] Payload size: 1232 characters
```

You can copy the obfuscated payload to your clipboard with `--clip`, or write it to a file with `-o`.

For more advanced usage, use the `--choose-mutators` flag, and specify exactly what obfuscation modules, or Mutators, you want to use in what order. Use also the `-s` argument to control the level of obfuscation used.

```
bashfuscator -c "cat /etc/passwd" --choose-mutators token/special_char_only compress/bzip2 string/file_glob -s 1
[+] Payload:

"${@#b }"  "e"$'\166'"a""${@}"l "$(  ${!@}m''$'k\144'''ir -p '/tmp/wW'${*~~} ;$'\x70'"${@/AZ }"rin""tf  %s  'MxJDa0zkXG4CsclDKLmg9KW6vgcLDaMiJNkavKPNMxU0SJqlJfz5uqG4rOSimWr2A7L5pyqLPp5kGQZRdUE3xZNxAD4EN7HHDb44XmRpN2rHjdwxjotov9teuE8dAGxUAL'>  '/tmp/wW/?
??';  prin${@#K. }tf %s  'wYg0iUjRoaGhoNMgYgAJNKSp+lMGkx6pgCGRhDDRGMNDTQA0ABoAAZDQIkhCkyPNIm1DTQeppjRDTTQ8D9oqA/1A9DjGhOu1W7/t4J4Tt4fE5+isX29eKzeMb8pJsPya93'  >  '/tmp/wW/???
' "${@,, }"  &&${*}pri''\n${*,}tf %s 'RELKWCoKqqFP5VElVS5qmdRJQelAziQTBBM99bliyhIQN8VyrjiIrkd2LFQIrwLY2E9ZmiSYqay6JNmzeWAklyhFuph1mXQry8maqHmtSAKnNr17wQlIXl/ioKq4hMlx76' >'/tmp/wW/??

';"${@,  }" $'\x70'rintf  %s 'clDkczJBNsB1gAOsW2tAFoIhpWtL3K/n68vYs4Pt+tD6+2X4FILnaFw4xaWlbbaJBKjbGLouOj30tcP4cQ6vVTp0H697aeleLe4ebnG95jynuNZvbd1qiTBDwAPVLT   tCLx' >'/tmp/wW/?

?' ;  ${*/~} p""${@##vl  }ri""n''tf %s  '  pr'"'"'i'"'"'$'"'"'n\x74'"'"'f %s  "$( prin${*//N/H  }tf  '"'"'QlpoOTFBWSZTWVyUng4AA3R/gH7z/+Bd/4AfwAAAD8AAAA9QA/7rm7NzircbE1wlCTBEamT1PKekxqYIA9TNQ' >'/tmp/wW/????'  "${@%\`  }"  ;p''r""i$'\x6e'''$'\164'"f" %s 'puxuZjSK09iokSwsERuYmYxzhEOARc1UjcKZy3zsiCqG5AdYHeQACRPKqVPIqkxaQnt/RMmoLKqCiypS0FLaFtirJFqQtbJLUVFoB/qUmEWVKxVFBYjHZcIAYlVRbkgWjh'  >'/tmp/wW/?

'  ${*};"p"rin''$'\x74f' %s  'Gs02t3sw+yFjnPjcXLJSI5XTnNzNMjJnSm0ChZQfSiFbxj6xzTfngZC4YbPvaCS3jMXvYinGLUWVfmuXtJXX3dpu379mvDn917Pg7PaoCJm2877OGzLn0y3FtndddpDohg'>'/tmp/wW/?
?
' && "${@^^ }"  pr""intf  %s  'Q+kXS+VgQ9OklAYb+q+GYQQzi4xQDlAGRJBCQbaTSi1cpkRmZlhSkDjcknJUADEBeXJAIFIyESJmDEwQExXjV4+vkDaHY/iGnNFBTYfo7kDJIucUES5mATqrAJ/KIyv1UV'> '/tmp/wW/
???'  ${*^}; ${!@}  "${@%%I  }"pri""n$'\x74f' %s '1w6xQDwURXSpvdUvYXckU4UJBclJ4OA'"'"'  |""b${*/t/\(  }a\se$'"'"'6\x34'"'"' -d| bu${*/\]%}nzi'"'"'p'"'"'${!@}2  -c)"  $@  |$   {@//Y^  } \ba\s"h"  ' >  '/tmp/wW/
??
' ${@%b  } ;  pr"i"\ntf  %s  'g8oZ91rJxesUWCIaWikkYQDim3Zw341vrli0kuGMuiZ2Q5IkkgyAAJFzgqiRWXergULhLMNTjchAQSXpRWQUgklCEQLxOyAMq71cGgKMzrWWKlrlllq1SXFNRqsRBZsKUE' >  '/tmp/wW/??
?'"${@//Y  }" ;$'c\141t' '/tmp/wW'/????  ${*/m};"${@,,  }"  $'\162'\m '/tmp/wW'/????  &&${@^ }rmd\ir  '/tmp/wW'; ${@^^  }   )"  "${@}"

[+] Payload size: 2062 characters
```

For more detailed usage and examples, please refer to the [documentation](https://bashfuscator.readthedocs.io/en/latest/Usage.html "documentation").

## Extending the Framework

Adding new obfuscation methods to the framework...