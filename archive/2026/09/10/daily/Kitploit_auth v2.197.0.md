---
title: auth v2.197.0
url: https://kitploit.com/en/posts/github-supabase-auth-v21970
source: Kitploit
date: 2026-09-10
fetch_date: 2026-09-11T06:51:39.231491
---

# auth v2.197.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50887/7b01820da0adbf9a46a2abc29309837b8029aea2650b81b03509f720c3534db2-display-v1.webp)

New releaseSep 10, 2026

# auth v2.197.0

A JWT based API for managing users and issuing JWT tokens

Share

# Auth - Authentication and User Management by Supabase

[![Coverage Status](https://coveralls.io/repos/github/supabase/auth/badge.svg?branch=master)](https://coveralls.io/github/supabase/auth?branch=master)

Auth is a user management and authentication server written in Go that powers
[Supabase](https://supabase.com)'s features such as:

* Issuing JWTs
* Row Level Security with PostgREST
* User management
* Sign in with email, password, magic link, phone number
* Sign in with external providers (Google, Apple, Facebook, Discord, ...)

It is originally based on the excellent
[GoTrue codebase by Netlify](https://github.com/netlify/gotrue), however both have diverged significantly in features and capabilities.

If you wish to contribute to the project, please refer to the [contributing guide](https://github.com/supabase/auth/blob/master/CONTRIBUTING.md).

## Table of Contents

* [Quick Start](#quick-start)
* [Running in Production](#running-in-production)
* [Configuration](#configuration)
* [Endpoints](#endpoints)

## Quick Start

Create a `.env` file to store your own custom environment variables. See [`example.env`](https://github.com/supabase/auth/blob/master/example.env)

1. Start the local Postgres database in a Postgres container: `docker-compose -f docker-compose-dev.yml up postgres`
2. Build the auth binary: `make build` . You should see an output like this:

root@kitploit:~

```
go build -ldflags "-X github.com/supabase/auth/cmd.Version=`git rev-parse HEAD`"
GOOS=linux GOARCH=arm64 go build -ldflags "-X github.com/supabase/auth/cmd.Version=`git rev-parse HEAD`" -o gotrue-arm64
```

3. Execute the auth binary: `./auth`

### If you have Docker installed

Create a `.env.docker` file to store your own custom env vars. See [`example.docker.env`](https://github.com/supabase/auth/blob/master/example.docker.env)

1. `make build`
2. `make dev`
3. `docker ps` should show two Docker containers (`auth-auth-1` and `auth-postgres-1`)
4. That's it! Visit the [health check endpoint](http://localhost:9999/health) to confirm that auth is running.

## Running in production

Running an authentication server in production is not an easy feat. We
recommend using [Supabase Auth](https://supabase.com/auth) which gets regular
security updates.

Otherwise, please make sure you set up a process to promptly update to the
latest version. You can do that by following this repository, specifically the
[Releases](https://github.com/supabase/auth/releases) and [Security
Advisories](https://github.com/supabase/auth/security/advisories) sections.

### Backward compatibility

Auth uses the [Semantic Versioning](https://semver.org) scheme. Here are some
further clarifications on backward compatibility guarantees:

**Go API compatibility**

Auth is not meant to be used as a Go library. There are no guarantees on
backward API compatibility when used this way regardless of which version
number changes.

**Patch**

Changes to the patch version guarantees backward compatibility with:

* Database objects (tables, columns, indexes, functions).
* REST API
* JWT structure
* Configuration

Guaranteed examples:

* A column won't change its type.
* A table won't change its primary key.
* An index will not be removed.
* A uniqueness constraint will not be removed.
* A REST API will not be removed.
* Parameters to REST APIs will work equivalently as before (or better, if a bug
  has been fixed).
* Configuration will not change.

Not guaranteed examples:

* A table may add new columns.
* Columns in a table may be reordered.
* Non-unique constraints may be removed (database level checks, null, default
  values).
* JWT may add new properties.

**Minor**

Changes to minor version guarantees backward compatibility with:

* REST API
* JWT structure
* Configuration

Exceptions to these guarantees will be made only when serious security issues
are found that can't be remedied in any other way.

Guaranteed examples:

* Existing APIs may be deprecated but continue working for the next few minor
  version releases.
* Configuration changes may become deprecated but continue working for the next
  few minor version releases.
* Already issued JWTs will be accepted, but new JWTs may be with a different
  structure (but usually similar).

Not guaranteed examples:

* Removal of JWT fields after a deprecation notice.
* Removal of certain APIs after a deprecation notice.
* Removal of sign-in with external providers, after a deprecation notice.
* Deletion, truncation, significant schema changes to tables, indexes, views,
  functions.

We aim to provide a deprecation notice in execution logs for at least two major
version releases or two weeks if multiple releases go out. Compatibility will
be guaranteed while the notice is live.

**Major**

Changes to the major version do not guarantee any backward compatibility with
previous versions.

### Inherited features

Certain inherited features from the Netlify codebase are not supported by
Supabase and they may be removed without prior notice in the future. This is a
comprehensive list of those features:

1. Multi-tenancy via the `instances` table i.e. `GOTRUE_MULTI_INSTANCE_MODE`
   configuration parameter.
2. System user (zero UUID user).
3. Super admin via the `is_super_admin` column.
4. Group information in JWTs via `GOTRUE_JWT_ADMIN_GROUP_NAME` and other
   configuration fields.
5. JWT signing. Supabase Auth supports asymmetric keys (RS256 by default;
   ECC/Ed25519 optional). HS256 is still supported for compatibility, but
   migrating to asymmetric keys is recommended for easier validation and
   rotation. Future deprecations will be announced in the changelog. See the
   [JWT Signing Keys](https://supabase.com/docs/guides/auth/signing-keys) and
   [JWTs guide](https://supabase.com/docs/guides/auth/jwts) for details.

Note that this is not an exhaustive list and it may change.

### Best practices when self-hosting

These are some best practices to follow when self-hosting to ensure backward
compatibility with Auth:

1. Do not modify the schema managed by Auth. You can see all of the
   migrations in the `migrations` directory.
2. Do not rely on the schema and the structure of data in the database. Always use
   Auth APIs and JWTs to infer information about users.
3. Always run Auth behind a TLS-capable proxy such as a load balancer, CDN,
   nginx or other similar software.

## Configuration

You may configure Auth using either a configuration file named `.env`,
environment variables, or a combination of both. Environment variables are prefixed with `GOTRUE_`, and will always have precedence over values provided via file.

### Top-Level

root@kitploit:~

```
GOTRUE_SITE_URL=https://example.netlify.com/
```

`SITE_URL` - `string` **required**

The base URL your site is located at. Currently used in combination with other settings to construct URLs used in emails. Any URI that shares a host with `SITE_URL` is a permitted value for `redirect_to` params (see `/authorize` etc.).

`URI_ALLOW_LIST` - `string`

A comma-separated list of URIs (e.g. `"https://foo.example.com,https://*.foo.example.com,https://bar.example.com"`) which are permitted as valid `redirect_to` destinations. Defaults to []. Supports wildcard matching through globbing. e.g. `https://*.foo.example.com` will allow `https://a.foo.example.com` and `https://b.foo.example.com` to be accepted. Globbing is also support...