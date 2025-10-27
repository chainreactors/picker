---
title: Testing Databend Applications Using Testcontainers - Multi-Language Implementation Guide
url: https://cloudsjhan.github.io/2024/11/26/Testing-Databend-Applications-Using-Testcontainers-Multi-Language-Implementation-Guide/
source: cloud world
date: 2024-11-27
fetch_date: 2025-10-06T19:17:12.691816
---

# Testing Databend Applications Using Testcontainers - Multi-Language Implementation Guide

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## Testing Databend Applications Using Testcontainers - Multi-Language Implementation Guide

posted

2024-11-26

|

visitors:

|

|

wordcount:

913
|

min2read ≈

6

Testing Databend Applications Using Testcontainers - Multi-Language Implementation Guide

![](https://)

### Introduction to Testcontainers

[Testcontainers](https://testcontainers.com/ "Testcontainer website") is an open-source library that provides lightweight, disposable instances of databases, message brokers, web browsers, or any service that can run in a Docker container.

#### Core Features:

* Disposable: Can be discarded after testing
* Lightweight: Quick to start with minimal resource usage
* Docker-based: Leverages container technology for isolation

  #### Main Use Cases:
* Database testing: MySQL, PostgreSQL, MongoDB, Databend etc.
* Message queue testing: RabbitMQ, Kafka, etc.
* Browser automation testing
* Testing any containerizable service
  Using TestContainers for test cases helps avoid test environment pollution, ensures test environment consistency, simplifies test configuration, and improves test reliability.

This tool is particularly suitable for testing scenarios that depend on external services, enabling quick creation of isolated test environments.

### Support Databend for Testcontainers

![](https://p.ipic.vip/9bbqbg.png)

The Databend team has completed support for Databend data source in three major programming languages through PRs in [testcontainer-java](https://github.com/testcontainers/testcontainers-java/pull/9148 "PR for support databend in testcontainer-java"), [testcontainers-go](https://github.com/testcontainers/testcontainers-go/pull/2779 "PR for support databend in testcontainers-go"), and [testcontainers-rs](https://github.com/testcontainers/testcontainers-rs-modules-community/pull/207 "PR for support databend in testcontains-rs"). This means developers can easily integrate Databend test environments in projects using these languages.

### Prerequisites

* Docker installed in the operating environment
* Development environments for Java, Go, and Rust installed

#### Java Dependency Configuration

First, create a new Java Demo project. Here’s an example using Maven, adding databend testcontainers and databend-jdbc dependencies in pom.xml:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` <dependencies>     <dependency>         <groupId>org.testcontainers</groupId>         <artifactId>databend</artifactId>         <version>1.20.4</version>         <scope>test</scope>     </dependency>      <dependency>         <groupId>com.databend</groupId>         <artifactId>databend-jdbc</artifactId>         <version>0.2.8</version>     </dependency> </dependencies> ``` |

For Gradle, use:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ```  testImplementation "org.testcontainers:databend:1.20.4" ``` |

#### Creating Test Class

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` Create a `TestContainerDatabend` test class with its constructor: public class TestContainerDatabend {     private final DatabendContainer dockerContainer;      public TestContainerDatabend() {         dockerContainer = new DatabendContainer("datafuselabs/databend:v1.2.615");         dockerContainer.withUsername("databend").withPassword("databend").withUrlParam("ssl", "false");         dockerContainer.start();     } } ``` |

We specified `datafuselabs/databend:v1.2.615` as the Docker image for starting Databend, other databend versions available at [databend docker hub](https://hub.docker.com/r/datafuselabs/databend), then set the username and password, and started the container service.

Here’s the test case:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` @Test public void testSimple() {     try (Connection connection = DriverManager.getConnection(getJdbcUrl())) {         DatabendStatement statement = (DatabendStatement) connection.createStatement();         statement.execute("SELECT 1");         ResultSet r = statement.getResultSet();         while (r.next()) {             int resultSetInt = r.getInt(1);             System.out.println(resultSetInt);             assert resultSetInt == 1;         }     } catch (Exception e) {         throw new RuntimeException("Failed to execute statement: ", e);     } }  public String getJdbcUrl() {     return format("jdbc:databend://%s:%s@%s:%s/",             dockerContainer.getUsername(),             dockerContainer.getPassword(),             dockerContainer.getHost(),             dockerContainer.getMappedPort(8000)); } ``` |

While running the test, we can see that testcontainers has started a databend container service in our system:

![](https://p.ipic.vip/xy6aci.png)

After the test completes, the container is immediately destroyed and resources are released.

Besides Databend, Testcontainers supports most databases and message queues available in the market, making it easy to build test suites that depend on these resources.

#### Go

Similarly, for Golang projects requiring Databend services, you can use `testcontainers-go`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` | ``` package main  import (     "context"     "database/sql"     "testing"      _ "github.com/datafuselabs/databend-go"     "github.com/stretchr/testify/require"      "github.com/testcontainers/testcontainers-go"     "github.com/testcontainers/testcontainers-go/modules/databend" )  func TestDatabend(t *testing.T) {     ctx := context.Background()      ctr, err := databend.Run(ctx, "datafuselabs/databend:v1.2.615")     testcontainers.CleanupContainer(t, ctr)     require.NoError(t, err)      connectionString, err := ctr.ConnectionString(ctx, "sslmode=disable")     require.NoError(t, err)      mustConnectionString := ctr.MustConnectionString(ctx, "sslmode=disable")     require.Equal(t, connectionString, mustConnectionString)      db, err := sql.Open("databend", connectionString)     require.NoError(t, err)     defer db.Close()      err = db.Ping()     require.NoError(t, err)      _, err = db.Exec("CREATE TABLE IF NOT EXISTS a_table ( \n" +         " `col_1` VARCHAR(128) NOT NULL, \n" +         " `col_2` VARCHAR(128) NOT NULL \n" +         ")")     require.NoError(t, err) } ``` |

#### Rust

Since Databend is written in Rust, you can naturally use testcontainer-rs to quickly start a Databend container service in Rust projects:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` | ``` #[cfg(test)] mod tests {     use databend_driver::Client;      use crate::{databend::Databend as DatabendImage, testcontainers::runners::AsyncRunner};      #[tokio::test]     async fn test_databend() {         let databend = DatabendImage::default().start().await.unwrap();         let http_port = databend.get_host_port_ipv4(8000).await.unwrap();         let dsn = format!(             "databend://databend:databend@localhost:{}/default?sslmode=disable",             http_port         );         let client = Client::new(dsn.to_string());         let conn = client.get_conn().await.unwrap();         let row = conn.query_row("select 'hello'").await.unwrap();         assert!(row.is_some());         let row = row.unwrap();         let (val,): (String,) = row.try_into().unwrap();         assert_eq!(val, "hello");          let conn2 = conn.clone();         let row = conn2.query_row("select 'world'").await.unwrap();         assert!(row.is_some());         let row = row.unwrap();         let (val,): (String,) = row.try_into().unwrap();         assert_eq!(val, "world");     } } ``` |

### Conclusion

For modern software development, reliable testing frameworks and toolchains are crucial foundations for ensuring code quality. W...