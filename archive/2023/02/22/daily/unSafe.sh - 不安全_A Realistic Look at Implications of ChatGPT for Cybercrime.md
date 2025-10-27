---
title: A Realistic Look at Implications of ChatGPT for Cybercrime
url: https://buaq.net/go-150404.html
source: unSafe.sh - 不安全
date: 2023-02-22
fetch_date: 2025-10-04T07:41:05.097118
---

# A Realistic Look at Implications of ChatGPT for Cybercrime

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

![](https://8aqnet.cdn.bcebos.com/d2ba42414b5be848a2c6287bc5f1b249.jpg)

A Realistic Look at Implications of ChatGPT for Cybercrime

Recently there’s been a lot of bold claims about how ChatGPT is going to revolutionize the cybercri
*2023-2-21 21:15:0
Author: [malwaretech.com(查看原文)](/jump-150404.htm)
阅读量:24
收藏*

---

Recently there’s been a lot of bold claims about how ChatGPT is going to revolutionize the cybercrime landscape, but
it can be hard to distinguish the facts from the fiction. In this article I’m going to dive into some claims, as well
as share some of my thoughts on where things might be heading.

## AI will allow low skilled hackers to develop advanced malware

This is one of the claims that seems to be everywhere. I can’t even scroll down three posts on LinkedIn without someone talking about AI malware.

The first problem with this claim is that ChatGPT is simply not good at coding.
If you ask it to generate a Python snippet to load a webpage, it can do that. If you ask it to generate a file encryptor, it can probably do that too.
But when it comes to building any kind of complex code, it sucks. The more parameters you add, the more confused it gets.

Whilst you can sometimes get ChatGPT to generate a very rudimentary example of an individual malware component, it’s far from capable of building a fully functional piece of malware.
The second you start trying to assemble multiple components together, it loses track of what it’s doing and fails. In fact, even if ChatGPT did have the capability to work
well with code, the prompt character/token limit would prevent inputting enough data to generate anything beyond snippets you could find on Google.

As an example, I tried to get ChatGPT to generate a cookie stealer for Chrome. Below is the code ChatGPT output.

```
#include <stdio.h>

#include <string.h>

#include <windows.h>

#define COOKIE_FILE "C:\\Users\\<username>\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"

int main() {
    FILE *cookie_file;
    COOKIE_HEADER header;
    char name[256];
    char value[4096];
    char encrypted_value[4096];

    cookie_file = fopen(COOKIE_FILE, "rb");
    if (cookie_file == NULL) {
        printf("Failed to open cookie file.\n");
        return 1;
    }

    while (fread(&header, sizeof(header), 1, cookie_file) == 1) {
        if (header.name_length >= sizeof(name) || header.value_length >= sizeof(value) || header.encrypted_value_length >= sizeof(encrypted_value)) {
            printf("Cookie size is too large.\n");
            continue;
        }

        fread(name, header.name_length, 1, cookie_file);
        name[header.name_length] = '\0';

        fread(value, header.value_length, 1, cookie_file);
        value[header.value_length] = '\0';

        fread(encrypted_value, header.encrypted_value_length, 1, cookie_file);
        encrypted_value[header.encrypted_value_length] = '\0';

        printf("Name: %s\nValue: %s\nEncrypted Value: %s\n\n", name, value, encrypted_value);
    }

    fclose(cookie_file);

    return 0;
}
```

Already very early on, we’ve hit multiple problems.

Consider the following line `#define COOKIE_FILE "C:\\Users\\<username>\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"`

Here the user’s username is set to a placeholder value of , so we'd need to come up with code to get the actual username.
The cookie path also depends on using the right Windows version, Chrome version, and drive letter. In the case of my own system,
the cookie file was actually in a completely different folder. The code also doesn't handle Cookie decryption, which has been used since Chrome version 80.
Cookies are simply output to the console, so we'd still need to build another component to upload them. And on top of all this, that isn't even the right file format. Chrome uses
SQLite3 for cookie storage, whereas this code is just trying to read the raw file in a way that won't ever work.

All of these errors I noticed because I can read code, I’m familiar with programming, I understand the internal workings of the relevant systems & software, and I know how malware works on a functional level.
If I were coming in as someone who cannot code, I’m unlikely to have any of the above skills, therefore no idea why my code doesn’t work.
In my experimentation with ChatGPT, not only did I find I was heavily relying on my skills as an experience malware developer,
but also my skills as a communicator. Having to translate abstract malware concepts into plain English instructions for a chatbot to understand was definitely a new experience for me.

Something also worth noting is that ChatGPT generates different responses to the same prompts.
I think this is due the fact that Large Language Models as statistic models that work on probabilities of one word following the next.
So when using ChatGPT to generate code, it will generate different code each time we ask. This makes it a nightmare to generate, debug, and assemble multiple
piece of code.

I believe a lot of the misinformation stems from people’s belief that programming consists of simply writing code. Therefore, because the AI can output code, it can replace programmers.
But the AI cannot replace programmers, because programming is not just writing code.
Programming requires that you research and understand what it is you want to do, how you want to do it, and are familiar with the limitations of your design choices.
Only then can you begin translating ideas into code.
We don’t think a C programmer doesn’t understand code because they don’t write ASM,
and we don’t believe a Python programmer doesn’t understand code because they don’t write C.
So why do we expect that someone who has no coding experience can just pick up an AI and churn out complex software?
AI is simply the next level of abstraction from machine code, not a replacement for the coder.

But ultimately everything we’ve said here is avoiding the elephant in the room: ChatGPT being able to generate code examples is due to it being trained on publicly available code.
If someone with zero coding ability wants malware, there’s are thousands of ready-to-go examples available on Google. There’s even custom malware development services for sale on various open hacking forums.
I think we need not worry about cybersecurity being turned on its head by Schrodinger’s hacker, who is simultaneously highly proficient in malware design despite knowing no coding at all, but also too dense to perform simple Google searchs.

### Antivirus bypassing polymorphic malware

In [this article](https://www.cyberark.com/resources/threat-research-blog/chatting-our-way-into-creating-a-polymorphic-malware), CyberArk makes the claim that ChatGPT can not only generate malware,
but polymorphic malware which easily bypasses security products. Such claims are either misleading or false.

*What is polymorphic malware?*
Polymorphism is an old, pretty much obsolete virus technique. Back when antivirus relied exclusively on code signatures, you could avoid detection via altering (mutating) their code.
For example, let’s say we wanted to get the number 2 in Assembly.

```
; Method 1

mov eax, 2

; Method 2

mov eax, 1
add eax, 1

; Method 3

xor eax, eax
inc eax
inc eax

; Method 4

mov eax, 3
dec eax
```

These are just 4 examples of the nearly infinite ways to do the same thing in programming.
Polymorphic malware exploits this.
The malware regenerates its own code on each deployment or every time its run, so that no two instances of the same malware are identical.
This is very similar to how biological viruses are sometimes able to evade the immune syste...