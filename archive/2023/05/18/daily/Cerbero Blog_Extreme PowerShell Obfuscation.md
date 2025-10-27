---
title: Extreme PowerShell Obfuscation
url: https://blog.cerbero.io/?p=2709
source: Cerbero Blog
date: 2023-05-18
fetch_date: 2025-10-04T11:39:14.088194
---

# Extreme PowerShell Obfuscation

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

# Extreme PowerShell Obfuscation

We recently stumbled upon [an old article](https://perl-users.jp/articles/advent-calendar/2010/sym/11) by [Daisuke Mutaguchi](https://twitter.com/mutaguchi/) explaining an extreme technique for PowerShell obfuscation. The article is in Japanese, so you may have to use [Google translate](https://perl--users-jp.translate.goog/articles/advent-calendar/2010/sym/11?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp).

Here’s the final example provided by the author of the article:

```
${;}=+$();${=}=${;};${+}=++${;};${@}=++${;};${.}=++${;};${[}=++${;};
${]}=++${;};${(}=++${;};${)}=++${;};${&}=++${;};${|}=++${;};
${"}="["+"$(@{})"[${)}]+"$(@{})"["${+}${|}"]+"$(@{})"["${@}${=}"]+"$?"[${+}]+"]";
${;}="".("$(@{})"["${+}${[}"]+"$(@{})"["${+}${(}"]+"$(@{})"[${=}]+"$(@{})"[${[}]+"$?"[${+}]+"$(@{})"[${.}]);
${;}="$(@{})"["${+}${[}"]+"$(@{})"[${[}]+"${;}"["${@}${)}"];
"${"}${.}${[}+${"}${)}${@}+${"}${+}${=}${+}+${"}${+}${=}${&}+${"}${+}${=}${&}+${"}${+}${+}${+}+${"}${[}${[}+${"}${.}${@}+${"}${+}${+}${|}+${"}${+}${+}${+}+${"}${+}${+}${[}+${"}${+}${=}${&}+${"}${+}${=}${=}+${"}${.}${.}+${"}${.}${[}|${;}"|&${;};
```

Yes, this is valid PowerShell.

Although there are limits to static deobfuscation, we decided to see what can be done about this with the new release of our [PowerShell Beautifier package](https://cerbero.io/packages/powershellbeautifier/).

Before beginning, make sure you have the latest version of the package installed and let’s deobfuscate the code with all parameters set.

[![](/wp-content/uploads/2023/05/extpsobf.png)](/wp-content/uploads/2023/05/extpsobf.png)

Ant this is the result:

```
$var_13 = "".inSert;
$var_14 = 'ie' + "$var_13"[27];
"[CHar]34+[CHar]72+[CHar]101+[CHar]108+[CHar]108+[CHar]111+[CHar]44+[CHar]32+[CHar]119+[CHar]111+[CHar]114+[CHar]108+[CHar]100+[CHar]33+[CHar]34|$var_14" | & $var_14;
```

Incredible! It’s already much easier to read!

We can see that this line has not been fully resolved:

```
$var_14 = 'ie' + "$var_13"[27];
```

The reason is that the code relies on something which is known only at execution time: namely the signature of the “insert” method. Of course, given what is already present, we can guess the result, but let’s not.

If we try to execute the following lines:

```
$var_13 = "".inSert;
Write-Host "$var_13"
```

PowerShell will output the aforementioned method signature:

```
string Insert(int startIndex, string value)
```

Let’s print only the index used by the code:

```
Write-Host "$var_13"[27]
```

As expected, it prints out the character “x” and thus making the string “iex”.

So let’s replace the unresolved string with the resolved one:

```
$var_13 = "".inSert;
$var_14 = 'iex';
"[CHar]34+[CHar]72+[CHar]101+[CHar]108+[CHar]108+[CHar]111+[CHar]44+[CHar]32+[CHar]119+[CHar]111+[CHar]114+[CHar]108+[CHar]100+[CHar]33+[CHar]34|$var_14" | & $var_14;
```

And now we deobfuscate again.

```
$var_1 = "".inSert;
"[CHar]34+[CHar]72+[CHar]101+[CHar]108+[CHar]108+[CHar]111+[CHar]44+[CHar]32+[CHar]119+[CHar]111+[CHar]114+[CHar]108+[CHar]100+[CHar]33+[CHar]34|iex" | & 'iex';
```

It is clear that the code uses “iex” (aka Invoke-Expression) to execute the code in the string. If we wish to know what the code in the string contains, we can isolate the contents of the string and execute the deobfuscator only on this portion:

```
[CHar]34+[CHar]72+[CHar]101+[CHar]108+[CHar]108+[CHar]111+[CHar]44+[CHar]32+[CHar]119+[CHar]111+[CHar]114+[CHar]108+[CHar]100+[CHar]33+[CHar]34|iex
```

The result:

```
'"Hello, world!"' | Invoke-Expression
```

The code prints out the string “Hello, world!”.

牟田口さん、ありがとうございました！

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [May 17, 2023](https://blog.cerbero.io/extreme-powershell-obfuscation/)Categories [Package](https://blog.cerbero.io/category/package/), [Reversing](https://blog.cerbero.io/category/reversing/)Tags [Deobfuscation](https://blog.cerbero.io/tag/deobfuscation/), [Powershell](https://blog.cerbero.io/tag/powershell/)

## Leave a Reply [Cancel reply](/extreme-powershell-obfuscation/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: CRX Format Package](https://blog.cerbero.io/crx-format-package/)

[Next Next post: Obfuscated Batch Scripts in OneNote Document](https://blog.cerbero.io/obfuscated-batch-scripts-in-onenote-document/)

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
  + [Cerbero Suite](https://ce...