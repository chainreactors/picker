---
title: Sidekick in Action: Analyzing LockBit 3.0
url: https://binary.ninja/2025/02/26/sidekick-in-action-analyzing-lockbit.html
source: Binary Ninja
date: 2025-02-27
fetch_date: 2025-10-06T20:35:39.789578
---

# Sidekick in Action: Analyzing LockBit 3.0

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Sidekick in Action: Analyzing LockBit 3.0

* [Tim Bryant](https://github.com/iamausertoo)
* 2025-02-26
* [sidekick](/tag/sidekick)

In this post, weâll explore how we used Sidekick to analyze complex malware samples. Weâll use LockBit 3.0 as our target, walking through the process of identifying and understanding key functions, deobfuscating strings, and mapping the sampleâs behavior.

## The Challenge

LockBit 3.0 exemplifies the complexity of modern malware analysis. Like many sophisticated samples, it employs various obfuscation techniques to hinder analysis. Using traditional reverse engineering tools, tasks like locating string decryption routines or mapping key functionality can take a considerable time. However, with AI assistance, we were able to reduce these tasks to minutes while maintaining accuracy.

## Stage 1: Quickly Identifying Important Functions

Our first step was to get a high-level understanding of the binaryâs structure. Using the Automation Workbench interface (shown in Figure 1), we started by running the utility functions analysis tool, which scanned the binary for functions with high in-degree. In malware, string decryption routines and hashing routines typically have high in-degree.

![Automation Workbench](/blog/images/sidekick-3.0-lockbit/01_workbench.png)
*Figure 1: Binary Ninjaâs Automation Workbench interface showing the utility functions tool*

Because this post was intended to highlight the new Analysis Console, we didnât run the script directly. Instead, we asked Sidekick to run it on our behalf (Figure 2). In response, Sidekick:

1. Searched the scripts in the Automation Workbench
2. Chose the most appropriate script
3. Registered the script as a tool that it can call
4. Ran the tool and reported the results

This demonstrates that Sidekick can readily use scripts (created by users or by itself) to answer analysis questions. We will see more of that later.

![Assistant Tools](/blog/images/sidekick-3.0-lockbit/02_run-utility-tool.png)
*Figure 2: Analysis Console and Indexes showing the identified utility functions*

At this point, Sidekick asked if weâd like it to search through the functions in the newly created âUtility Functionsâ index, and we consented. Sidekick proceeded and examined the contents of the index:

```
index:Utility Functions
Metadata:
 Name: Utility Functions
 Total entries: 5
Type Distribution:
 function: 5
Entries by Type:
 function (5 entries):
   4011e4: sub_4011e4   | {In-Degree=27}
   401260: sub_401260   | {In-Degree=59}
   4086f8: sub_4086f8   | {In-Degree=82}
   408720: sub_408720   | {In-Degree=88}
   408c9c: sub_408c9c   | {In-Degree=28}
```

Next, we observed (in Figure 3) Sidekick retrieving several functions in the index before responding. Having accessed the function contents, it identified `sub_401260` as a likely string decryption function and gave a quick rundown of its operation. It was also helpful enough to suggest the purposes of the other functions.

![Identifying the Utility Functions](/blog/images/sidekick-3.0-lockbit/03_which-is-crypto.png)
*Figure 3: Examining the functions in the Utility Functions index*

Eventually, we needed to decrypt the strings by mimicking `sub_401260`. But, before doing that, we wanted to edit the binary to reflect our new understanding. So, we asked Sidekick to improve the decompilation accordingly. Sidekick made several updates based on its analysis and told us what edits it made (Figure 4). Among those edits, two were particularly interesting:

* `compute_string_hash` (formerly `sub_4011e4`): String case conversion/hashing
* `decrypt_data_block` (formerly `sub_401260`): Decrypts data using XOR with 0x450bdfca and bitwise NOT

![Edit the Binary](/blog/images/sidekick-3.0-lockbit/04_improve-decompilation.png)
*Figure 4: Sidekick fixes up the names and parameter types*

As an aside, all changes made by the assistant were recorded and viewable in the Sidekick Change Log sidebar. In Figure 5, we see that Sidekick named the functions, added comments, and fixed up the parameters. The Change Log provided transparency and allowed us to see each edit that was made. As always, if we felt Sidekick got something wrong, any such changes could be quickly reverted using Binary Ninjaâs undo system.

![Change Log](/blog/images/sidekick-3.0-lockbit/05_change-log.png)
*Figure 5: Sidekick Change Log showing the edits made*

## Stage 2: Decrypting Strings

With key functions identified, we focused on the `decrypt_data_block` function, which:

1. Takes two parameters:
   * A pointer to data (data)
   * A length parameter (length)
2. Implements a decryption routine that:
   * XORs each 32-bit value with the constant 0x450bdfca
   * Performs a bitwise NOT operation on the result
   * Moves to the next 32-bit value
   * Continues until all data is processed

This is a rather straightforward string decryption routine, so we proceeded with the next steps.

### Building the Decryption Tool

We created a matching decryption tool simply by asking Sidekick to create a decryption tool for `decrypt_data_block`. As shown in Figure 6, Sidekick described what we needed more precisely: the inputs, outputs, and processing required.

![Tool Creation](/blog/images/sidekick-3.0-lockbit/06_make-decrypt-tool.png)
*Figure 6: Asking the assistant to create a decryption tool*

We wanted to copy and paste the bytes from the `__builtin_memcpy` call in the linear view to verify that the tool worked correctly. However, the bytes were escaped hex strings, not plain hex strings. So we used the Automation Workbench directly to make that change (Figure 7). The script was also stripping the final zero byte, which messed up the final character, so we manually removed that line. After running the script, it was obvious that the decrypted strings were actually 16-bit little-endian. We quickly fixed this issue.

![Updating the Tool](/blog/images/sidekick-3.0-lockbit/07_edit-decrypt-tool.png)
*Figure 7: Editing the decryption tool*

![Script Arguments](/blog/images/sidekick-3.0-lockbit/08_manual-use.png)
*Figure 8: Running the script prompts for input*

When we ran the script, we were prompted for the input sequence (Figure 8). Running the script after these minor edits produced the output:

`Decoded String: ROOT\CIMV2`

This confirmed that our approach was working. We were ready to decrypt all the strings.

Note: We could have asked the assistant to use the tool directly to verify for us. For example, âGo pick a few of the call sites for `decrypt_data_block` and see what kinds of strings there are.â We skipped that step and proceeded to decrypt all the strings.

### Decrypting All the Strings

For extracting all encrypted strings, we considered three approaches:

1. Look for `__builtin_memcpy` calls before each `decrypt_data_block` call
   * Pros: Straightforward approach
   * Cons: Misses short strings and may require additional code for edge cases
2. Write a script to reconstruct the arrays
   * Pros: Comprehensive
   * Cons: Time-consuming and duplicates Binary Ninjaâs functionality
3. Use an LLM to extract memory contents at each call site
   * Pros: Low effort and flexible anal...