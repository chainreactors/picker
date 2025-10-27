---
title: Stripe CTF 2.0 (Web Edition)
url: https://blog.g0tmi1k.com/2012/09/stripe-ctf-20-web-edition/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:47.185514
---

# Stripe CTF 2.0 (Web Edition)

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Stripe CTF 2.0 (Web Edition)

[Stripe](https://stripe.com/) hosted another 'Capture the Flag' (CTF) [event](https://blog.g0tmi1k.com/categories/boot2root/). They [previously](https://stripe.com/blog/capture-the-flag) did one back in February 2012 which contained 6 flags - however they were back with the 'web edition' going from level 0 to level 8 covering a range of web attacks. *This is how I did it.*

**Please note**: The event **is now over**. If you wish to do this yourself, **you will have to [download](https://github.com/stripe-ctf/stripe-ctf-2.0) the code** **and do it offline**.

![Strip CTF Logo](/images/stripectf2.png "Strip CTF v2")

Table of Contents

* + [Links](#Links)
  + [Brief](#Brief)
  + [Level 0 - Secret Safe](#Level.0.-.Secret.Safe)
  + [Level 1 - Guessing Game](#Level.1.-.Guessing.Game)
  + [Level 2 - Social Network](#Level.2.-.Social.Network)
  + [Level 3 - Secret Vault](#Level.3.-.Secret.Vault)
  + [Level 4 - Karma Trader](#Level.4.-.Karma.Trader)
  + [Level 5 - Domain Authenticator](#Level.5.-.Domain.Authenticator)
  + [Level 6 - Steamer](#Level.6.-.Steamer)
  + [Level 7 - WaffleCopter](#Level.7.-.WaffleCopter)
  + [Level 8 - PasswordDB](#Level.8.-.PasswordDB)
  + [Summary](#Summary)
  + [Code](#Code)
    - [level7.py](#level7.py)
  + [level8.py](#level8.py)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/StripeCTF2.0.mp4)

Download video: <http://download.g0tmi1k.com/videos_archive/StripeCTF2.0.mp4>

## Brief

The game is to complete various challenges/puzzles by using different techniques. For example:

* Level 0 - Secret Safe *(SQL injection. See video at: 00:31)*
* Level 1 - Guessing Game *(PHP functions/User Input - 01:19)*
* Level 2 - Social Network *(Local file inclusion - 01:59)*
* Level 3 - Secret Vault *(SQL injection - 03:26)*
* Level 4 - Karma Trader *(Cross-site scripting/Cross-site request forgery - 05:04)*
* Level 5 - Domain Authenticator *(Chained requests- 07:55)*
* Level 6 - Streamer *(Cross-site scripting - 10:07)*
* Level 7 - WaffleCopter *(Weak cryptography - 14:47)*
* Level 8 - PasswordDB *(Network side attack - 18:45)*

Upon completion, the user is given a key (aka a 'flag'), which they can then enter into the control panel, that unlocks the next stage/level. The source code for each level is available if requested, therefore we are able to go about in a [white-box testing](http://en.wikipedia.org/wiki/White-box_testing) manner. *When signing up to Stripe, for each stage the contestant was generated a random username for that puzzle, and they were spread over multiple servers.*

## Level 0 - Secret Safe

*'We'll start you out with Level 0, the Secret Safe. The Secret Safe is designed as a secure place to store all of your secrets. It turns out that the password to access Level 1 is stored within the Secret Safe. If only you knew how to crack safes...'*

After looking at the source code, the attacker spots a few key lines in the code, for example:

*File: level00.js, Line: 06*

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sqlite3 = require ('sqlite3'); // SQLite (database) driver ``` |

*File: level00.js, Line: 34*

|  |  |
| --- | --- |
| ``` 1 ``` | ``` var query = 'SELECT * FROM secrets WHERE key LIKE ? || ".%"'; ``` |

The attacker knows which database is powering the project ([SQLite](http://www.sqlite.org/)), and the query command that is being used. The query command is using '[LIKE](http://dev.mysql.com/doc/refman/5.0/en/string-comparison-functions.html#operator_like)', followed by the user's input, then the use of '[%](http://dev.mysql.com/doc/refman/5.6/en/pattern-matching.html)' in the query is wildcard in SQLite, causing it to select everything after the full stop.

The expected input was meant to be a username, and then the project selects everything related to that user. However, if the attacker uses the same wild card '%' as the username *(as the user input isn't sanitised)*, it causes the database to select everything from all the users. This reveals the flag for the next level *(contained in secretstash-.level01.password)*.

---

**In short**: The use of % acts as a wild card to select all the values in the database.

**Input**: `%`

## Level 1 - Guessing Game

*'Excellent, you are now on Level 1, the Guessing Game. All you have to do is guess the combination correctly, and you'll be given the password to access Level 2! We've been assured that this level has no security vulnerabilities in it (and the machine running the Guessing Game has no outbound network connectivity, meaning you wouldn't be able to extract the password anyway), so you'll probably just have to try all the possible combinations. Or will you...?'*

When analysing the given source code, the attacker notices:

*File: index.php, Line: 12-16*

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` $filename = 'secret-combination.txt'; extract($_GET); if (isset($attempt)) {   $combination = trim(file_get_contents($filename));   if ($attempt === $combination) { ``` |

The first line is loading in the file which is the combination *(aka the password)* to reveal the key. However, due to the next line containing the '[extract](http://www.php.net/manual/en/function.extract.php)' function; the attacker can use this to their advantage. They can do this as 'extract' takes the requested inputs variables *(e.g. from $*GET, $*POST etc.)*, and at the same time overwrites the current values, therefore, the attacker can alter the variable for '$filename' *(which contains the combination)*.

After checking to see if the variable '$attempt' has been set *(which the attacker can do due to the use of extract)*, it tries to [read a file](http://www.php.net/manual/en/function.file-get-contents.php) which has the name set to the value of '$filename'. However, if the attacker has altered the value to a file which doesn't exist *(e.g. 'blank' - no file)*, the function will fail with a value of 'false'.

This value is [compared](http://php.net/manual/en/language.operators.comparison.php) to the value of '$attempt'. If it matches then the key will be displayed.

The attacker has already had to define the '$attempt', but if they don't set a value to it *(e.g. 'blank)*, it will match the return result *(false)* of the failed request for a file *($filename)*, thus displaying the key.

---

**In short**: by using PHP's extract function, the attacker can set/overwrite values which will match by returning false to show the key.

**Input**: `?attempt=&filename=`

## Level 2 - Social Network

*'You are now on Level 2, the Social Network. Excellent work so far! Social Networks are all the rage these days, so we decided to build one for CTF. Please fill out your profile at `https://level02-3.stripe-ctf.com/user-xtpnikecaz`. You may even be able to find the password for Level 3 by doing so.'*

As soon as the attacker inspected the project, the attacker saw that the social network allows for pictures to be uploaded. Looking at the code the attacker spots a few things:

*File: index.php, Line: 09*

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $dest_dir = "uploads/"; ``` |

*File: index.php, Line: 44*

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <input type="submit" value="Upload!"> ``` |

*File: index.php, Line: 49*

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <a href="password.txt">password.txt</a> ``` |

The attacker is aware that the code which is in-place doesn't check what is being uploaded to it, and will also attempt to upload any file regardless of the type. They are also able to identify the local path for the upload location, as well as where the key is being stored.

By using the inbuilt form to upload a PHP file which '[file\_get\_contents](http://www.php.net/manual/en/function.file-get-contents.php)' *(same function from level 2)*, the attacker is able to go back from the upload folder *([directory traversal](http://en.wikipedia.org/wiki/Direc...