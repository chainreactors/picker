---
title: Analyzing nested, obfuscated PHP files…
url: https://www.hexacorn.com/blog/2023/06/03/analyzing-nested-obfuscated-php-files/
source: Hexacorn
date: 2023-06-04
fetch_date: 2025-10-04T11:45:08.477709
---

# Analyzing nested, obfuscated PHP files…

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2023/06/01/analysing-ps2exe-executables/)
[Next →](https://www.hexacorn.com/blog/2023/06/07/this-lolbin-doesnt-exist/)

# Analyzing nested, obfuscated PHP files…

Posted on [2023-06-03](https://www.hexacorn.com/blog/2023/06/03/analyzing-nested-obfuscated-php-files/ "10:07 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Many PHP webshells are encrypted, encoded, obfuscated in many different ways, but most use a rudimentary approach relying on engaging the same sequence of code ‘hiding’ routines repetitively, sequences that rely on calls to *eval* that are then applied to various combos of *gzinflated*, *base64*–*decoded* and sometimes *rot13-decoded* data blobs. In some cases it can go on and on for as many as 10+ iterations…

Deobfuscating such scripts is a tedious, and quite frankly, a boring job to do – you have to go through all these layers manually, one by one. BOOOOOORING!

Luckily, we can use some automation to help the process…

The following perl script does the magic on a Windows box, provided you have installed Php in c:\php.

```
use strict;
use warnings;

my $f=shift || die ("Gimme a file name!\n");
my $cnt=0;
my $nf=$f;

while (1)
 {
    print "$cnt\n";
    open F,"<$nf";
    binmode F;
    read F,my $data,-s $f;
    close F;

    last if $data !~ /[\s\@]eval/s;

    $data=~s/([\s\@])eval/$1echo/sg;
    $data=~s/X-Powered-By: .*?><\?//sg;

    $nf = sprintf("$f.%04d.php",$cnt);

   if ($data !~/<\?/)
    {
       $data = "<?php\n$data\n";
    }

    open F,">$nf";
    binmode F;
    print F $data;
    close F;

    system ("c:\php\php.exe $nf > $nf.txt");
    $nf=$nf.".txt";

    $cnt++;
 }
```

What happens is this: the script takes an input PHP file, reads it, finds *eval* expressions in it, and replaces them with *echo*, and then writes the modified script into a new file, and then it executes this new file as a script under *php.exe* binary. The resulting decoded/decrypted script is saved to a new text file. Then this new text file becomes an input to the same procedure, and the process is repeated until there is no more *eval* references in the final file…

If you are lucky, the last file will hold the decoded script.

There are caveats, of course.

More advanced cases rely on sneaking in some non-evaled variables that are introduced in consecutive layers, to be then used/referenced later, sometimes even by the final layer. The script above doesn’t take care of cases like this, but still, you can solve such cases by browsing the resulting .txt files — you will quickly discover where the information was lost, and adjust for it, and finally – repeat the whole automation process after manually editing one of the intermediate text files.

If it doesn’t make any sense: just review the text files one by one and look for loose code or initialized variables that you may want to manually copy to the next layer, and restart from there.

The other caveat case are scripts that rely on [*preg\_replace(“/.\*/e”* trick](https://stackoverflow.com/questions/16986331/can-someone-explain-the-e-regex-modifier). It’s not taken care of, but why should it? It’s been deprecated since php 5.5 and removed in php 7.0. If you see a script obfuscated using this function, it’s most likely a very old code. You can still de-obfuscate it manually or semi-automatically (with parts deobfuscated by the above scripts), but let’s be honest – very unlikely it’s your smoking gun…. If anyone is still using such old PHP version, there is probably a bigger fish to fry…

In my experience, the code works on majority of poorly encoded php webshells, and if sometimes it doesn’t – it just needs a tweak or two to account for some random/unexpected cosmetic issues.

And sometimes, you can just run the script on all already somehow deobfuscated scripts:

```
for %k in (.php*) do (perl __decode.pl "%k")
```

Example results for a *test.php* script:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/06/php_deobf.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/06/php_deobf.png)

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [De-everything, Un-everything](https://www.hexacorn.com/blog/category/de-everything-un-everything/), [webshell](https://www.hexacorn.com/blog/category/webshell/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/06/03/analyzing-nested-obfuscated-php-files/ "Permalink to Analyzing nested, obfuscated PHP files…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")