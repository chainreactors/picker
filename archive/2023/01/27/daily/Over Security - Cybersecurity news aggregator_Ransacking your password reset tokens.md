---
title: Ransacking your password reset tokens
url: https://positive.security/blog/ransack-data-exfiltration
source: Over Security - Cybersecurity news aggregator
date: 2023-01-27
fetch_date: 2025-10-04T04:59:43.365878
---

# Ransacking your password reset tokens

![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436cf0ef16e7ad_menu_icon_flipped.png)

[HOME](/)[About](/about)[Services](/services)[Blog](/blog)[Contact](/contact)

[![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c270016e798_purple.png)](/)

# Ransacking your password reset tokens

January 26, 2023

ByÂ

Lukas Euler

![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/63ceda8f7b5b98d68365bdee_ransack_bruteforce_overview.png)

-- MARKDOWN --
- Integrating the ["Ransack" library](https://github.com/activerecord-hackery/ransack) in its default configuration into your Ruby on Rails project poses a major security risk that can likely be exploited to extract sensitive information or fully compromise the application
- The issue arises because the recommended way to use the library exposes powerful conditional parameters to end users which allow character by character brute-force of arbitrary attributes on associated database objects
- Other technologies such as Hasura (GraphQL Engine) or older versions of Sequelize (Node.js ORM) are vulnerable to similar attacks when query filters with arbitrary conditional operators are configured
- We have reported internet-exploitable critical and high severity security issues based on this in six different applications. Our research identified several hundred more applications that are potentially affected

\*\*Update 2022-02-10:\*\* [Ransack 4.0.0 has been released](https://github.com/activerecord-hackery/ransack/releases/tag/v4.0.0) which addresses this issue by changing the default behavior of the library to enforce the use of explicit allow lists for searchable attributes and associations.

# Table of Contents
- [Exploiting Ransack](#exploiting-ransack)
Â Â Â Â - [Vulnerable example application](#vulnerable-example-application)
Â Â Â Â - [Character by character brute-force](#character-by-character-brute-force)
Â Â Â Â - [Mitigation](#mitigation)
- [Case Study: Becoming superadmin on fablabs.io](#case-study-becoming-superadmin-on-fablabsio)
- [Searching for vulnerable applications](#searching-for-vulnerable-applications)
Â Â Â Â - [GitHub/searchcode](#githubsearchcode)
Â Â Â Â - [Common Crawl](#common-crawl)
- [Other technologies](#other-technologies)
Â Â Â Â - [Hasura (GraphQL)](#hasura-graphql)
Â Â Â Â - [Sequelize (Node.js)](#sequelize-nodejs)
- [Responsible disclosure overview](#responsible-disclosure-overview)

# Exploiting Ransack
The popular Ransack Ruby library provides a very powerful feature set around object-based database searching in Rails applications. One of its main appeals is the ease with which it can be utilized to implement public facing search functionality on a website. As is often the case when using a very powerful and complex tool for a rather simple use case, this can lead to problems.

![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/63c075a2482ce1c64d9cc8ac_01_ransack_documentation.png)

Official Ransack documentation suggests processing query parameters from unrestricted user input. The warning was [added to the documentation on 2022-11-03](https://github.com/activerecord-hackery/ransack/commit/4d234c89ca69f6aa7b5a992a4e69e3f658302362), possibly in reaction to [our suggestion in an open GitHub issue](https://github.com/activerecord-hackery/ransack/issues/1273#issuecomment-1298273454)

In its default configuration, Ransack will allow for [query conditions based on properties of associated database objects](https://activerecord-hackery.github.io/ransack/going-further/associations/). An application is potentially vulnerable if it exposes a search/filtering function which processes an unrestricted query object, usually represented by a Ruby hash constructed via the `q` GET parameter.
[Search matchers](https://activerecord-hackery.github.io/ransack/getting-started/search-matches/) are Ransack's syntax to specify how user provided query values are compared to real records from the database. A straight-forward and less problematic search matcher is `\*\_eq` (exactly equals), whereas other search matchers like `\*\_start` (starts with), `\*\_cont` (contains) or `\*\_gt` (is greater than) can be abused to exfiltrate potentially sensitive attribute values of associated database objects via character by character brute-force or binary search for numbers.
An attacker can perform character by character brute-force by repeatedly guessing a prefix of the value they want to extract using the `\*\_start` search matcher, starting with a prefix length of just one character, and extending that prefix by an additional character whenever their previous guess was successful. The attacker can tell that a guess was successful whenever their Ransack search returns at least one result. With a case sensitive database collation a single bcrypt password hash for example can be extracted with fewer than 2000 requests on average, all within a few minutes.

## Vulnerable example application

Consider a blogging platform implemented in Rails:

It can have different users which authenticate themselves via passwords and have access to an email based account recovery feature:

```
class User < ActiveRecord::Base
 validates :email, :username, presence: true
 attr_accessor :password_hash, :reset_password_token

 has_many posts
end
```

These users can publish posts on the platform (Note how the `User` and `Post` classes are associated via the `has\_many` and `belongs\_to` keywords, which instruct the framework to set up database relationships in the background):

```
class Post < ActiveRecord::Base
  validates :title, :content, presence: true

  belongs_to :user
end
```

The platform offers a search feature to help look for posts containing specific keywords, conveniently implemented with the `Ransack` library on the backend side:

```
def index
  @q = Post.ransack(params[:q])
  @posts = @q.result(distinct: true)
end
```

The search feature is accessible via a simple HTML form from the frontend, intended to allow finding posts based on their title:
```html
<form id="post\_search" action="/posts" method="get">

Â  Â <label>Search by title:</label>
 Â  Â <input name="q[title\_cont]" type="text" value="">

Â  Â <input type="submit" name="submit" value="Search">

</form>
```

Intended usage of the search feature via the HTML form causes the browser to issue a GET request to `/posts?q[title\_cont]=hacking`, which is met with an HTML response containing a list of matching posts.

## Character by character brute-force
The technique used here is similar to known exploitation techniques for (boolean-based) blind SQL injections.
In the fictional example, an attacker can determine the first character of the password reset token of a post's author by submitting a series of search queries until the application returns a non-empty list of posts. Note the use of the `Post` ->Â `User` association and the `\*\_start` search matcher.

```http
GET /posts?q[user\_reset\_password\_token\_start]=0 -> Empty results page
GET /posts?q[user\_reset\_password\_token\_start]=1 -> Empty results page
GET /posts?q[user\_reset\_password\_token\_start]=2 -> Results in page
```

Once the first character has been recovered, we can start guessing the next character by extending the prefix given in the query filter:
```http
GET /posts?q[user\_reset\_password\_token\_start]=20 -> Empty results page
GET /posts?q[user\_reset\_password\_token\_start]=21 -> Empty results page
GET /posts?q[user\_reset\_password\_token\_start]=22 -> Empty results page

[...]
â
GET /posts?q[user\_reset\_password\_token\_start]=2c -> Empty results page
GET /posts?q[user\_reset\_password\_token\_start]=2f -> Results in page
```

And so on and so forth until the entire token has been recovered.

Automating this process yields excellent entertainment value, as it is a rare example of an exploit that can sensibly be visualized in true Hollywood hacking fashion:

[![

](https://cdn.prod.website-files.com/5f6...