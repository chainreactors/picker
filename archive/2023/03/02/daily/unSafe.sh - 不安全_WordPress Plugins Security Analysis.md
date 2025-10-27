---
title: WordPress Plugins Security Analysis
url: https://buaq.net/go-151579.html
source: unSafe.sh - 不安全
date: 2023-03-02
fetch_date: 2025-10-04T08:25:23.829707
---

# WordPress Plugins Security Analysis

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

WordPress Plugins Security Analysis

We are excited to announce the launch of our 40 Vulnerabilities in 40 Days Campaign! Our goal is to
*2023-3-1 22:18:45
Author: [infosecwriteups.com(查看原文)](/jump-151579.htm)
阅读量:78
收藏*

---

We are excited to announce the launch of our 40 Vulnerabilities in 40 Days Campaign! Our goal is to raise awareness about the importance of proactive vulnerability management and to encourage everyone to take action to secure their systems.

Starting from March 1st, we will be showcasing one vulnerability every day for 40 days, along with details on how to detect and remediate it. Our team of experts will be available to provide insights and best practices, so you can learn from real-world scenarios and understand the impact of these vulnerabilities.

We believe that knowledge is power, and by educating ourselves and others, we can help make the world a safer place. Join us and become a part of the 40 Vulnerabilities in 40 Days Campaign today!

A zero-day vulnerability is a security weakness in software or hardware that is unknown to the party responsible for patching or otherwise protecting the system. This vulnerability can be exploited by attackers to conduct malicious activities such as unauthorized access to sensitive data, spreading malware, or disrupting normal operations.

Zero-day vulnerabilities are particularly dangerous because they can be used by attackers before the vendor has had a chance to release a patch or a fix for the issue. Attackers can take advantage of these vulnerabilities to launch targeted attacks, which can have serious consequences, such as data theft, financial loss, or reputational damage.

CVE-2022–45834

CVE-2022–4367

CVE-2022–4011

CVE-2022–3941

CVE-2022–4412

CVE-2022–4411

CVE-2022–4406

CVE-2022–4405

CVE-2022–4404

CVE-2022–4528

CVE-2022–4529

CVE-2022–4530

CVE-2022–4531

CVE-2022–4532

CVE-2022–4533

CVE-2022–4534

CVE-2022–4535

CVE-2022–4536

CVE-2022–4537

CVE-2022–4538

CVE-2022–4539

CVE-2022–4540

CVE-2022–4541

CVE-2022–4550

CVE-2022–46847

CVE-2022–4423

CVE-2022–4424

CVE-2022–4425

CVE-2022–4443

CVE-2022–47171

CVE-2022–47163

CVE-2022–47162

CVE-2022–47159

CVE-2022–47155

CVE-2022–47154

CVE-2022–47152

CVE-2022–47147

CVE-2022–47138

CVE-2022–47141

CVE-2022–47143

CVE-2022–47139

CVE-2022–47135

CVE-2022–47448

CVE-2022–47447

CVE-2022–47440

CVE-2022–47446

CVE-2022–47443

CVE-2022–47422

CVE-2022–4549

CVE-2022–4548

CVE-2022–47427

Example Request:

```
POST /wp-admin/options-general.php?page=wp_csv_to_db_menu_page HTTP/1.1
```

Example Vulnerable Code:

The displayed code snippet is used in WordPress and can save the information in the CSV file to the WordPress database. After filling the WordPress form with the required information, the code connects to the WordPress database and stores the information in the CSV file in the desired table of the WordPress database. This code also has a special value “update\_db” which, if checked, will update the data in the CSV file instead of creating a new record. If no records have been updated, a success message is displayed. But if there is a problem connecting with the database, an error message will be displayed.

```
if ( isset( $_POST[ 'execute_button' ] ) ) {
// If "Update DB Rows" was checked
if ( isset( $_POST[ 'update_db' ] ) )
// Setup sql 'on duplicate update' loop
$updateOnDuplicate = ' ON DUPLICATE KEY UPDATE ';
foreach ( $db_cols as $db_col ) {
$updateOnDuplicate .= "$db_col=VALUES($db_col),";}
$updateOnDuplicate = rtrim( $updateOnDuplicate, ',' );
$sql = 'INSERT INTO ' . $_POST[ 'table_select' ] . ' (' . $db_cols_implode . ') ' . 'VALUES ' . $values_implode . $updateOnDuplicate;
$db_query_update = $wpdb->query( $sql );} else {
$sql = 'INSERT INTO ' . $_POST[ 'table_select' ] . ' (' . $db_cols_implode . ') ' . 'VALUES ' . $values_implode;
$db_query_insert = $wpdb->query( $sql );}
// If db db_query_update is successful
if ( $db_query_update ) {
$success_message = __( 'Congratulations!  The database has been updated successfully.', 'wp_csv_to_db' );}
// If db db_query_insert is successful
elseif ( $db_query_insert ) {
$success_message = __( 'Congratulations!  The database has been updated successfully.', 'wp_csv_to_db' );
$success_message .= '<br /><strong>' . count( $values ) . '</strong> ' . __( 'record(s) were inserted into the', 'wp_csv_to_db' ) . ' <strong>' . $_POST[ 'table_select' ] . '</strong> ' . __( 'database table.', 'wp_csv_to_db' ); }
// If db db_query_insert is successful AND there were no rows to udpate
elseif ( ($db_query_update === 0) && ($db_query_insert === '') ) {
$message_info_style .= '* ' . __( 'There were no rows to update. All .csv values already exist in the database.', 'wp_csv_to_db' ) . '<br />';} else {
$error_message   .= '* ' . __( 'There was a problem with the database query.', 'wp_csv_to_db' ) . '<br />';
$error_message   .= '* ' . __( 'A duplicate entry was found in the database for a .csv file entry.', 'wp_csv_to_db' ) . '<br />';
$error_message   .= '* ' . __( 'If necessary; please use the option below to "Update Database Rows".', 'wp_csv_to_db' ) . '<br />';}
```

## CSRF Protection Parameter

One of the useful methods to prevent CSRF vulnerability in the development of WordPress plugins is to use unique tokens. To use this method, you need to use tokens in your plugin development code that are uniquely added to the form. For example, you can use the form author token.

For example, in the code below, the form author token is added as a variable containing a random value in the form:

```
function add_csrf_nonce_field() {wp_nonce_field( 'csrf_nonce_action', 'csrf_nonce_name' );}add_action( 'form_name_form_tag', 'add_csrf_nonce_field'
```

In the code below, the token of the form author is checked after submitting the form, and if the token is not correct, the form is considered invalid:

```
function verify_csrf_nonce_field() {
if ( !isset( $_POST['csrf_nonce_name'] ) || !wp_verify_nonce( $_POST['csrf_nonce_name'], 'csrf_nonce_action' ) ) {wp_die(
```

You can also use change tokens like time token. For example, you can add a time token like this:

```
function add_csrf_nonce_field() {$nonce_value = time();echo '<input type="hidden" name="csrf_nonce_name" value="' . $nonce_value . '" />';}add_action( 'form_name_form_tag', 'add_csrf_nonce_field' );
```

In the following code, the time token is checked after submitting the form and if the token is older than one minute, it considers the form invalid:

```
function verify_csrf_nonce_field() {$submitted_nonce = isset( $_POST['csrf_nonce_name'] ) ? intval( $_POST['csrf_nonce_name'] ) : 0;if ( time() - $submitted_nonce > 60 ) {wp_die( 'Invalid CSRF nonce. Please tryagain.');}}add_action('form_name_process_action', 'verify_csrf_nonce_field');
```

You can also use WordPress framework features, such as the wp\_verify\_nonce class, to prevent CSRF. Using the wp\_verify\_nonce class in the WordPress framework is a useful and advanced method to prevent CSRF attacks.

The wp\_verify\_nonce class uses a random token that is generated on each new request and after the form is submitted, the token is compared with the token submitted in the form.

To use the wp\_verify\_nonce class in the development of WordPress plugins, you can use the following code:

```
function add_csrf_nonce_field() {wp_nonce_field( 'csrf_nonce_action', 'csrf_nonce_name' );}add_action( 'form_name_form_tag', 'add_csrf_nonce_field' );
function verify_csrf_nonce_field() {if ( !isset( $_POST['csrf_nonce_name'] ) || !wp_verify_nonce( $_POST['csrf_nonce_name'], 'csrf_nonce_action' ) ) {wp_die('Invalid CSRF nonce. Please...