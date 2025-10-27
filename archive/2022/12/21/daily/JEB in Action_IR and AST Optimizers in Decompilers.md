---
title: IR and AST Optimizers in Decompilers
url: https://www.pnfsoftware.com/blog/ir-and-ast-optimizers-in-decompilers/
source: JEB in Action
date: 2022-12-21
fetch_date: 2025-10-04T02:04:07.664203
---

# IR and AST Optimizers in Decompilers

[Skip to content](#content)

[![JEB in Action](https://www.pnfsoftware.com/blog/wp-content/uploads/2018/12/icon-jeb-128-newlogo-transparent.png)](https://www.pnfsoftware.com/blog/)

[JEB in Action](https://www.pnfsoftware.com/blog/)

JEB Decompiler Blog

Menu and widgets

* [PNF Software (Main)](https://www.pnfsoftware.com)

Search for:

## Last Posts

* [Reversing with VIBRE AI Assistant](https://www.pnfsoftware.com/blog/vibe-reversing-with-vibre-ai-assistant/)
* [Reversing Nvidia GPU’s SASS code](https://www.pnfsoftware.com/blog/reversing-nvidia-cuda-sass-code/)
* [Deobfuscation ratings, inlining “fat” functions, and breaking opaque predicates](https://www.pnfsoftware.com/blog/deobfuscation-ratings-inlining-fat-functions-and-breaking-opaque-predicates/)
* [Generic Unpacking for APK](https://www.pnfsoftware.com/blog/generic-unpacking-for-apk/)
* [How To Use JEB – Auto-decrypt strings in protected binary code](https://www.pnfsoftware.com/blog/how-to-use-jeb-auto-decrypt-strings-in-protected-binary-code/)
* [How To Use JEB – Analyze an obfuscated win32 crypto clipper](https://www.pnfsoftware.com/blog/how-to-use-jeb-to-analyze-an-obfuscated-win32-crypto-clipper/)
* [JEB Assistant (legacy)](https://www.pnfsoftware.com/blog/jeb-assistant/)
* [Control-flow unflattening in the wild](https://www.pnfsoftware.com/blog/control-flow-unflattening-in-the-wild/)
* [Recovering JNI registered natives, recovering protected string constants](https://www.pnfsoftware.com/blog/recovering-jni-registered-natives/)
* [Android JNI and Native Code Emulation](https://www.pnfsoftware.com/blog/android-jni-and-native-code-emulation/)

## Categories

* [Android](https://www.pnfsoftware.com/blog/category/android/)
* [API (JEB1)](https://www.pnfsoftware.com/blog/category/api-jeb1/)
* [API (JEB2)](https://www.pnfsoftware.com/blog/category/api-jeb2/)
* [API (JEB3)](https://www.pnfsoftware.com/blog/category/api-jeb3/)
* [Assistant](https://www.pnfsoftware.com/blog/category/assistant/)
* [Collaboration](https://www.pnfsoftware.com/blog/category/collaboration/)
* [CUDA](https://www.pnfsoftware.com/blog/category/cuda/)
* [Dart](https://www.pnfsoftware.com/blog/category/dart/)
* [Debugging](https://www.pnfsoftware.com/blog/category/debugging/)
* [Decompilation](https://www.pnfsoftware.com/blog/category/decompilation/)
* [Ethereum](https://www.pnfsoftware.com/blog/category/ethereum/)
* [Flutter](https://www.pnfsoftware.com/blog/category/dart/flutter/)
* [JEB2](https://www.pnfsoftware.com/blog/category/jeb2/)
* [JEB3](https://www.pnfsoftware.com/blog/category/jeb3/)
* [JEB4](https://www.pnfsoftware.com/blog/category/jeb4/)
* [JEB5](https://www.pnfsoftware.com/blog/category/jeb5/)
* [Malware](https://www.pnfsoftware.com/blog/category/malware/)
* [Native Code](https://www.pnfsoftware.com/blog/category/native-code/)
* [Obfuscation](https://www.pnfsoftware.com/blog/category/obfuscation/)
* [PDF](https://www.pnfsoftware.com/blog/category/pdf/)
* [PLC](https://www.pnfsoftware.com/blog/category/plc/)
* [Tutorial](https://www.pnfsoftware.com/blog/category/tutorial/)
* [WebAssembly](https://www.pnfsoftware.com/blog/category/webassembly/)

## Archives

* [September 2025](https://www.pnfsoftware.com/blog/2025/09/)
* [August 2025](https://www.pnfsoftware.com/blog/2025/08/)
* [October 2024](https://www.pnfsoftware.com/blog/2024/10/)
* [February 2024](https://www.pnfsoftware.com/blog/2024/02/)
* [January 2024](https://www.pnfsoftware.com/blog/2024/01/)
* [December 2023](https://www.pnfsoftware.com/blog/2023/12/)
* [August 2023](https://www.pnfsoftware.com/blog/2023/08/)
* [April 2023](https://www.pnfsoftware.com/blog/2023/04/)
* [December 2022](https://www.pnfsoftware.com/blog/2022/12/)
* [November 2022](https://www.pnfsoftware.com/blog/2022/11/)
* [June 2022](https://www.pnfsoftware.com/blog/2022/06/)
* [May 2022](https://www.pnfsoftware.com/blog/2022/05/)
* [June 2021](https://www.pnfsoftware.com/blog/2021/06/)
* [March 2021](https://www.pnfsoftware.com/blog/2021/03/)
* [February 2021](https://www.pnfsoftware.com/blog/2021/02/)
* [July 2020](https://www.pnfsoftware.com/blog/2020/07/)
* [June 2020](https://www.pnfsoftware.com/blog/2020/06/)
* [April 2020](https://www.pnfsoftware.com/blog/2020/04/)
* [February 2020](https://www.pnfsoftware.com/blog/2020/02/)
* [October 2019](https://www.pnfsoftware.com/blog/2019/10/)
* [July 2019](https://www.pnfsoftware.com/blog/2019/07/)
* [May 2019](https://www.pnfsoftware.com/blog/2019/05/)
* [April 2019](https://www.pnfsoftware.com/blog/2019/04/)
* [March 2019](https://www.pnfsoftware.com/blog/2019/03/)
* [January 2019](https://www.pnfsoftware.com/blog/2019/01/)
* [November 2018](https://www.pnfsoftware.com/blog/2018/11/)
* [October 2018](https://www.pnfsoftware.com/blog/2018/10/)
* [September 2018](https://www.pnfsoftware.com/blog/2018/09/)
* [July 2018](https://www.pnfsoftware.com/blog/2018/07/)
* [May 2018](https://www.pnfsoftware.com/blog/2018/05/)
* [February 2018](https://www.pnfsoftware.com/blog/2018/02/)
* [November 2017](https://www.pnfsoftware.com/blog/2017/11/)
* [October 2017](https://www.pnfsoftware.com/blog/2017/10/)
* [August 2017](https://www.pnfsoftware.com/blog/2017/08/)
* [June 2017](https://www.pnfsoftware.com/blog/2017/06/)
* [May 2017](https://www.pnfsoftware.com/blog/2017/05/)
* [April 2017](https://www.pnfsoftware.com/blog/2017/04/)
* [October 2016](https://www.pnfsoftware.com/blog/2016/10/)
* [September 2016](https://www.pnfsoftware.com/blog/2016/09/)
* [June 2016](https://www.pnfsoftware.com/blog/2016/06/)
* [April 2016](https://www.pnfsoftware.com/blog/2016/04/)
* [March 2016](https://www.pnfsoftware.com/blog/2016/03/)
* [February 2016](https://www.pnfsoftware.com/blog/2016/02/)
* [December 2015](https://www.pnfsoftware.com/blog/2015/12/)
* [November 2015](https://www.pnfsoftware.com/blog/2015/11/)
* [October 2015](https://www.pnfsoftware.com/blog/2015/10/)
* [September 2015](https://www.pnfsoftware.com/blog/2015/09/)
* [August 2015](https://www.pnfsoftware.com/blog/2015/08/)
* [July 2015](https://www.pnfsoftware.com/blog/2015/07/)
* [June 2015](https://www.pnfsoftware.com/blog/2015/06/)
* [December 2014](https://www.pnfsoftware.com/blog/2014/12/)
* [August 2014](https://www.pnfsoftware.com/blog/2014/08/)
* [April 2014](https://www.pnfsoftware.com/blog/2014/04/)
* [March 2014](https://www.pnfsoftware.com/blog/2014/03/)
* [December 2013](https://www.pnfsoftware.com/blog/2013/12/)
* [September 2013](https://www.pnfsoftware.com/blog/2013/09/)
* [August 2013](https://www.pnfsoftware.com/blog/2013/08/)
* [July 2013](https://www.pnfsoftware.com/blog/2013/07/)
* [June 2013](https://www.pnfsoftware.com/blog/2013/06/)
* [May 2013](https://www.pnfsoftware.com/blog/2013/05/)
* [April 2013](https://www.pnfsoftware.com/blog/2013/04/)
* [March 2013](https://www.pnfsoftware.com/blog/2013/03/)

## [Main Website](https://www.pnfsoftware.com)

# IR and AST Optimizers in Decompilers

The following is a small guide that will help users writing decompiler plugins decide whether they need to work at the **IR** (Intermediate Representation) level or at the **AST** (Abstract Syntax Tree) level. The recommendations apply to both JEB decompiler engines, *dexdec* (for Android Dex/Dalvik) and *gendec* (generic decompiler engine.

## Decompilation Pipeline

A method undergoing decompilation goes through the following simplified pipeline:

1. The low-level native code (machine code or bytecode) is converted to low-level IR
2. Some augmentation take place, including SSA transformation and typing
3. IR processors lift and clean the low-level IR
4. The final high-level IR is converted to an AST
5. AST processors clean and beautify the code
6. The final AST is rendered as pseudo-code

The steps 3 (IR processing) and 5 (AST processing) are customizable by the user through JEB’s API. Indeed, custom plugins are sometimes necessary to perform work not done by JEB’s built-in optimizers.

## IR vs AST

The following comparison between IR and AST will help you decide which plugi...