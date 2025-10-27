---
title: WordPress Profile Builder 3.9.0 Missing Authorization
url: https://cxsecurity.com/issue/WLB-2023030039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-16
fetch_date: 2025-10-04T09:43:50.828173
---

# WordPress Profile Builder 3.9.0 Missing Authorization

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
|  |  | |  | | --- | | **WordPress Profile Builder 3.9.0 Missing Authorization** **2023.03.15**  Credit:  **[Lana Codes](https://cxsecurity.com/author/Lana%2BCodes/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0814](https://cxsecurity.com/cveshow/CVE-2023-0814/ "Click to see CVE-2023-0814")**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "CWE-200")** | |

Description: Profile Builder – User Profile & User Registration Forms <= 3.9.0 – Sensitive Information Disclosure via Shortcode
Affected Plugin: Profile Builder – User Profile & User Registration Forms
Plugin Slug: profile-builder
Affected Versions: <= 3.9.0
CVE ID: CVE-2023-0814
CVSS Score: 6.4 (Medium)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
Researcher/s: Lana Codes
Fully Patched Version: 3.9.1
Vulnerability Analysis
The vulnerability, assigned CVE-2023-0814, exists due to missing authorization within the wppb\_toolbox\_usermeta\_handler() function. The affected function is defined as a callback function to the ‘user\_meta’ shortcode, which is registered via the WordPress add\_shortcode() function in usermeta.php.
As with all shortcode callback functions, wppb\_toolbox\_usermeta\_handler() takes an array of attributes. In particular, the ‘user\_id’ attribute is used to create a new user object. Then, the ‘key’ attribute is used in a call to ‘$user->get()’. Finally, the function returns the value of the retrieved ‘key’ for the given ‘user\_id’. During this process, capability checks are not properly implemented to ensure that the user executing the function is authorized to retrieve the given ‘key’ value.
Profile Builder wppb\_toolbox\_usermeta\_handler function
The wppb\_toolbox\_usermeta\_handler() function creates a user object and performs a $user->get() with threat actor-supplied values.
Prerequisites
Vulnerable instances of Profile Builder need the ‘Enable Usermeta shortcode’ setting enabled within the ‘Shortcodes’ section of the ‘Advanced Settings’ tab of the plugin’s ‘Settings’ page.
Profile Builder Advanced Settings Page
‘Enable Usermeta shortcode’ setting activated
Exploitation
Information Disclosure
Any authenticated user, with subscriber-level permissions or greater, can send a specially-crafted HTTP POST request to the ‘wp-admin/admin-ajax.php’ endpoint with the ‘action’ parameter set to ‘parse-media-shortcode’ and the ‘shortcode’ parameter containing the ‘user\_meta’ shortcode with the ‘user\_id’ and ‘key’ attributes set.
Profile Builder POST to admin-ajax.php to retrieve the username of the user with a user ID of 1
POST to admin-ajax.php to retrieve the username of the user with a user ID of 1
As explained earlier, the value of the ‘key’ attribute is passed to a $user->get() call. Since the get() method of the WP\_User class is designed to retrieve user information, any column of the ‘wp\_users’ table can be passed via this attribute, including:
- ID
- user\_login
- user\_pass
- user\_nicename
- user\_email
- user\_url
- user\_registered
- user\_activation\_key
- user\_status
- display\_name
Password Reset to Privilege Escalation
The Profile Builder plugin provides the shortcode ‘[wppb-recover-password]’ to embed a password recovery form into a page on a WordPress site. The form allows users to submit their username or email address to receive an email with a password reset link containing a user activation key. When generated, this key is stored in the ‘user\_activation\_key’ column in the ‘wp\_users’ table of the WordPress database. Using CVE-2023-0814, this key can be retrieved for any user.
First, the threat actor must generate the user activation key by entering the username or email address of the targeted user in the password recovery form and clicking the ‘Get New Password’ button.
Profile Builder password recovery form
Next, the threat actor will make a similar POST request to our previous user enumeration proof-of-concept, but this time ensuring the ‘user\_id’ is set to the user ID of the username or email address entered into the password recovery form and setting the ‘key’ attribute to ‘user\_activation\_key’.
POST to admin-ajax.php to retrieve the user activation key for the admin account
Once the threat actor has retrieved the user activation key, they can navigate back to the password recovery form page, but this time with the ‘key’ query parameter set to the retrieved user activation key.
Password Recovery page with ‘key’ query parameter set to retrieved value
At this point, the threat actor simply needs to enter a new password and click the ‘Reset Password’ button. The threat actor will then be able to login using the targeted username and new password.
Timeline
February 7th, 2023 – Lana Codes responsibly discloses the vulnerability to the plugin vendor and our Vulnerability Disclosure program.
February 13th, 2023 – The vendor releases a patch in version 3.9.1 and Wordfence releases a firewall rule to address the vulnerability. Wordfence Premium, Care, and Response users receive this rule.
February 14th, 2023 – Wordfence releases an additional firewall rule to provide extended protection against exploitation. Wordfence Premium, Care, and Response users receive this rule.
March 14th, 2023 – Wordfence free users receive the first firewall rule.
March 15th, 2023 – Wordfence free users receive the second firewall rule.
Conclusion
In today’s post, we covered an Information Disclosure vulnerability that could lead to the takeover of an administrative account in Cozmolabs Profile Builder, a plugin used by over 60,000 WordPress installations. The Wordfence Threat Intelligence team issued a firewall rule providing protection against the vulnerability on February 13th and 14th, 2023. This rule has been protecting our Wordfence Premium, Wordfence Care, and Wordfence Response users since that date, while those still using our free version will receive this rule on March 14 and March 15, 2023.
If you believe your site has been compromised as a result of this vulnerability or any other vulnerability, we offer Incident Response services via Wordfence Care. If you need your site cl...