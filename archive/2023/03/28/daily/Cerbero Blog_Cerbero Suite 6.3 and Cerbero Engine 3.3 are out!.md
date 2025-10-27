---
title: Cerbero Suite 6.3 and Cerbero Engine 3.3 are out!
url: https://blog.cerbero.io/?p=2630
source: Cerbero Blog
date: 2023-03-28
fetch_date: 2025-10-04T10:50:45.802351
---

# Cerbero Suite 6.3 and Cerbero Engine 3.3 are out!

[Skip to content](#content)

[Cerbero Blog](https://blog.cerbero.io/)

Menu

* [Home](https://cerbero.io)
* Products
  + [Cerbero Suite](https://cerbero.io/suite/)
  + [Cerbero Engine](https://cerbero.io/engine/)
* [Packages](https://cerbero.io/packages/)
* [E-Zine](https://cerbero.io/e-zine/)
* [Blog](/)
* Support
  + [User Manual](https://cerbero.io/manual/)
  + [SDK Documentation](https://sdk.cerbero.io/)
  + [FAQ](https://cerbero.io/faq/)
  + [Resources](https://cerbero.io/resources/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

# Cerbero Suite 6.3 and Cerbero Engine 3.3 are out!

We have released Cerbero Suite 6.3 and Cerbero Engine 3.3. What follows is a list of the most important new features.

### Support for 7z and XZ archives

We have released the [7z Format](https://cerbero.io/packages/7zformat/) package which provides support for both 7z and XZ archives.

[![](/wp-content/uploads/2023/03/63/7z.png)](/wp-content/uploads/2023/03/63/7z.png)

The support includes encrypted archives and all common compression methods.

The package is available to all licenses of Cerbero Suite.

### Support for TAR archives

TAR archives are now supported thanks to the [TAR Format](https://cerbero.io/packages/tarformat/) package.

[![](/wp-content/uploads/2023/03/63/tar.png)](/wp-content/uploads/2023/03/63/tar.png)

The package is available to all licenses of Cerbero Suite.

### PowerShell Beautifier 2.0

We have released version 2.0 of our commercial [PowerShell Beautifier](https://cerbero.io/packages/powershellbeautifier/) package. The new release adds the option to remove unused variables.

[![](/wp-content/uploads/2023/03/psb2/1.png)](/wp-content/uploads/2023/03/psb2/1.png)

For example, this is a snippet of a malicious script:

```
$T = 'Get'
$M = $T + 'Method'
$I = 'Invoke'
$T = $T + 'Type'
$L = 'Load'
$Q0 = [Reflection.Assembly]
$B = $Q0::$L($MyS)
$B = $B.$T('NewPE2.PE')
$B = $B.$M('Execute')

$Ub = 'C:\Windows\Microsoft'
$z = $Ub + '.NET\Framewor'
$VT = $z + 'k\v4.0.30'
$XQ = $VT + '319\RegSvcs.exe'
$B = $B.$I($null,[object[]] ($XQ,$serv))
```

With both variable replacement and removal of unused variables enabled it becomes:

```
$load_result = [Reflection.Assembly]::Load($x_result)
$get_type_result = $load_result.GetType('NewPE2.PE')
$get_method_result = $get_type_result.GetMethod('Execute')
$invoke_result = $get_method_result.Invoke($null, [object[]]('C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegSvcs.exe', $x_result_2))
```

### OneNote Format for all licenses

The [OneNote Format](https://cerbero.io/packages/onenoteformat/) package is now available to all licenses of Cerbero Suite. The package was previously released for commercial licenses only.

Once the package is installed, you can directly open OneNote documents in Cerbero Suite and all embedded files are automatically extracted and ready to be inspected.

[![](/wp-content/uploads/2023/02/onenote/extract.png)](/wp-content/uploads/2023/02/onenote/extract.png)

### Crypto Module

We have exposed the Crypto module to the SDK and [documented it](https://sdk.cerbero.io/latest/Pro.Crypto.html).

The module provides classes for hashing and encryption/decryption.

Hashing data, for example, can be as simple as the following code snippet:

```
from Pro.Crypto import *

print(NTCryptoSHA1(b"Hello, World!").finalHexString())
```

### GZ module documentation

We have documented the [GZ module](https://sdk.cerbero.io/latest/Pro.GZ.html) which provides the API for parsing GZip archives.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [March 27, 2023March 27, 2023](https://blog.cerbero.io/cerbero-suite-6-3-and-cerbero-engine-3-3-are-out/)Categories [Engine](https://blog.cerbero.io/category/engine/), [Suite Advanced](https://blog.cerbero.io/category/suite-advanced/), [Suite Standard](https://blog.cerbero.io/category/suite-standard/)Tags [News](https://blog.cerbero.io/tag/news/)

## Leave a Reply [Cancel reply](/cerbero-suite-6-3-and-cerbero-engine-3-3-are-out/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: OneNote Format Package: All Licenses](https://blog.cerbero.io/onenote-format-package-all-licenses/)

[Next Next post: Reversing Complex PowerShell Malware](https://blog.cerbero.io/reversing-complex-powershell-malware/)

Search for:

Search

## Recent Posts

* [Memory Challenge 1: Reveal](https://blog.cerbero.io/memory-challenge-1-reveal/)
* [NSIS Format Package](https://blog.cerbero.io/nsis-format-package/)
* [ASAR Format Package](https://blog.cerbero.io/asar-format-package/)
* [InnoSetup Format Package 2.0](https://blog.cerbero.io/innosetup-format-package-2-0/)
* [Cerbero Journal Issue 6](https://blog.cerbero.io/cerbero-journal-issue-6/)
* [Memory Analysis Package 0.5](https://blog.cerbero.io/memory-analysis-package-0-5/)
* [Cerbero Suite 8.5](https://blog.cerbero.io/cerbero-suite-8-5/)
* [Memory Analysis Package 0.4](https://blog.cerbero.io/memory-analysis-package-0-4/)
* [Cerbero Suite 8.4](https://blog.cerbero.io/cerbero-suite-8-4/)
* [WIM Format Package](https://blog.cerbero.io/wim-format-package/)

## Archives

Archives

Select Month
 October 2025  (1)
 September 2025  (2)
 August 2025  (2)
 July 2025  (2)
 June 2025  (3)
 May 2025  (7)
 April 2025  (4)
 March 2025  (2)
 October 2024  (3)
 September 2024  (1)
 August 2024  (3)
 July 2024  (5)
 June 2024  (2)
 April 2024  (4)
 March 2024  (1)
 February 2024  (1)
 January 2024  (4)
 December 2023  (3)
 November 2023  (7)
 October 2023  (3)
 September 2023  (1)
 July 2023  (1)
 May 2023  (11)
 March 2023  (9)
 February 2023  (3)
 January 2023  (1)
 November 2022  (1)
 September 2022  (2)
 August 2022  (2)
 July 2022  (3)
 June 2022  (2)
 May 2022  (5)
 April 2022  (3)
 March 2022  (4)
 February 2022  (6)
 January 2022  (1)
 November 2021  (4)
 October 2021  (5)
 September 2021  (7)
 June 2021  (1)
 April 2021  (1)
 March 2021  (4)
 February 2021  (1)
 December 2020  (1)
 November 2020  (1)
 October 2020  (1)
 September 2020  (2)
 July 2020  (2)
 January 2020  (1)
 September 2019  (1)
 August 2019  (2)
 July 2019  (1)
 June 2019  (1)
 May 2019  (3)
 April 2019  (2)
 June 2018  (1)
 April 2018  (1)
 March 2018  (1)
 January 2018  (1)
 November 2017  (2)
 March 2017  (5)
 July 2016  (2)
 May 2016  (2)
 April 2016  (1)
 October 2015  (2)
 September 2015  (2)
 June 2015  (2)
 December 2014  (2)
 October 2014  (1)
 September 2014  (3)
 August 2014  (1)
 July 2014  (1)
 December 2013  (2)
 November 2013  (5)
 October 2013  (5)
 September 2013  (6)
 August 2013  (6)
 July 2013  (1)
 June 2013  (4)
 May 2013  (7)
 April 2013  (5)
 March 2013  (3)
 February 2013  (4)
 January 2013  (3)
 December 2012  (3)
 November 2012  (5)
 October 2012  (3)
 September 2012  (1)
 August 2012  (2)
 July 2012  (2)
 June 2012  (2)
 May 2012  (2)
 April 2012  (1)
 March 2012  (6)
 February 2012  (5)
 January 2012  (8)
 November 2011  (1)
 August 2011  (1)

* [Home](https://cerbero.io)
* Products
  + [Cerbero Suite](https://cerbero.io/suite/)
  + [Cerbero Engine](https://cerbero.io/engine/)
* [Packages](https://cerbero.io/packages/)
* [E-Zine](https://cerbero.io/e-zine/)
* [Blog](/)
* Support
  + [User Manual](https://cerbero.io/manual/)
  + [SDK Documentation](https://sdk.cerbero.io/)
  + [FAQ](https://cerbero.io/faq/)
  + [Resources](https://cerbero.io/resources/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

[Cerbero Blog](https://blog.cerbero.io/)  [Proudly powered by WordPress](https://wordpress.o...