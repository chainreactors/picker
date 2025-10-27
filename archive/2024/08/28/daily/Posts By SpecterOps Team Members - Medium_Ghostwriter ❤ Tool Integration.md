---
title: Ghostwriter ❤ Tool Integration
url: https://posts.specterops.io/ghostwriter-tool-integration-2dfbb952eb8a?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-08-28
fetch_date: 2025-10-06T18:07:10.521505
---

# Ghostwriter ❤ Tool Integration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2dfbb952eb8a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fghostwriter-tool-integration-2dfbb952eb8a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fghostwriter-tool-integration-2dfbb952eb8a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-2dfbb952eb8a---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-2dfbb952eb8a---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Ghostwriter ❤ Tool Integration

[![Alexander Sou](https://miro.medium.com/v2/resize:fill:64:64/1*05-twOFKf1u-oGOnok5nOw.jpeg)](https://medium.com/%40sou_predictable?source=post_page---byline--2dfbb952eb8a---------------------------------------)

[Alexander Sou](https://medium.com/%40sou_predictable?source=post_page---byline--2dfbb952eb8a---------------------------------------)

4 min read

·

Aug 27, 2024

--

Listen

Share

Incorporating new components into existing systems is such a pain, this process has been labeled “Integration Hell”. To ease tool integration, Ghostwriter v3.0.0 shipped with a GraphQL API. This API allows outside entities to easily query and manipulate Ghostwriter’s data. In this blogpost, we’ll use our [Operation Log Generator](https://github.com/SpecterOps/ghostwriter-oplog-populate) to demonstrate the capabilities of this API.

Press enter or click to view image in full size

![]()

Talking to Ghostwriter Has Never Been Easier

## Ghostwriter & GraphQL

Ghostwriter’s GraphQL API is driven by the [Hasura GraphQL Engine](https://hasura.io/). This engine provides three broad GraphQL operations:

**Queries** - [Query operations](https://hasura.io/docs/latest/queries/quickstart/) fetch data from Ghostwriter

```
query domainQueryID {
  domain(where: {name: {eq: "mydomain.com"}}) {
    id
  }
}
```

**Mutations** - [Mutation operations](https://hasura.io/docs/latest/mutations/quickstart/) manipulate Ghostwriter data

```
  mutation createSampleClient {
    insert_client_one(object: {name: "SpecterPops", codename: "SAMPLE CLIENT", timezone: "America/Los_Angeles"}) {
      id
    }
  }
```

**Subscriptions** - [Subscription operations](https://hasura.io/docs/latest/subscriptions/quickstart/) allow applications to receive data in real-time

```
subscription domainHealthMonitoring {
  domain(where: {healthStatus: {healthStatus: {_neq: "Healthy"}}}) {
    id
    name
  }
}
```

### Schema Exploration

Ghostwriter’s GraphQL schema can be explored in two different ways:

1. **Hasura Console** — The Hasura console allows direct interaction with the Ghostwriter’s PostgreSQL database. Changes made [via the console](https://www.ghostwriter.wiki/features/graphql-api/using-the-hasura-console) could irreversibly break Ghostwriter, so this option is disabled by default
2. **Ghostwriter’s GraphQL SDL** — Ghostwriter’s GraphQL schema is available [on Github](https://github.com/GhostManager/Ghostwriter/blob/master/DOCS/schema.graphql), and can be safely [explored with Postman](https://www.ghostwriter.wiki/features/graphql-api/common-api-actions#getting-to-know-the-api-schema)

The GraphQL operations defined by the schema provide powerful methods for Ghostwriter data management and the API allows external tools to easily leverage these operations. For example, our Python Operation Log Generator script leverages GraphQL mutation operations to create and fill a Ghostwriter operation log with entries we commonly see on our operations.

## Sample Example

Press enter or click to view image in full size

![]()

The Operation Log Generator uses a serries of Ghostwriter GraphQL mutations to create and populate an operation log. These mutations include:

* `login`- This mutation obtains a JSON Web Token (JWT) as part of the [Ghostwriter API authentication process](https://www.ghostwriter.wiki/features/graphql-api/authentication)
* `insert_client_one`- Our script uses this operation to create a single sample Ghostwriter client: `Specter Pops`
* `insert_project_one`- The script uses this mutation to a single new project, `SAMPLE PROJECT`, to the newly-created sample client
* `insert_oplog_one`- We use this operation to generate a single operation log under the project: `SAMPLE PROJECT`
* `insert_oplogEntry` - This final mutation aggregates all operation log entries from the file: `config/oplog.csv`, before issuing a single GQL query to populate the newly-created sample operation log. If this file does not exist, the program creates an operation log with 5,000 procedurally-generated entries

These five API calls are all it takes to link our operation log generator to Ghostwriter! Let’s take a closer look at how our script actually implements these calls.

### Authentication

The script first sets up token-based authentication with Ghostwriter. The steps to authenticate are outlined in [Ghostwriter’s documentation](https://www.ghostwriter.wiki/features/graphql-api/authentication), but at a high level, the program first use a username and password obtain a JWT with a `login` GraphQL API call.

```
def get_logon_token(credentials):
    # Prepare our initial unauthenticated GraphQL client
    transport = AIOHTTPTransport(credentials.url)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define our gql query
    get_logon_token_query = gql(
        """
        mutation login_mutation($password: String!, $username: String!) {
            login(password: $password, username: $username) {
                token expires
            }
        }
        """
    )
    get_logon_token_query_params = {
        "password": credentials.password,
        "username": credentials.username
    }

    # Login and get our token
    login_result = client.execute(
        get_logon_token_query,
        variable_values=get_logon_token_query_params
    )
    return login_result["login"]["token"] # pylint: disable=unsubscriptable-object...
```

The script then creates a GQL `Client` object and uses the obtained JWT as the bearer token in an HTTP `Authroization` header.

```
...
from gql import Client, gql
...
# Use credential configs to get a Ghostwriter token
gw_auth_token = get_logon_token(credentials)

# Set up token-based authentication
headers = {"Authorization": f"Bearer {gw_auth_token}"}
transport = AIOHTTPTransport(credentials.url, headers=headers)
authenticated_client = Client(transport=transport, fetch_schema_from_transport=True)
...
```

This GQL `Client` object is then used to execute all other GQL operations.

### API Usage

Once a GQL `Client` object has been created, executing operations is a simple three step process.

1. Create a `gql` object b...