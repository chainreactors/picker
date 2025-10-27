---
title: A Race to the Bottom - Database Transactions Undermining Your AppSec
url: https://blog.doyensec.com/2024/07/11/database-race-conditions.html
source: Over Security - Cybersecurity news aggregator
date: 2024-07-12
fetch_date: 2025-10-06T17:45:59.006396
---

# A Race to the Bottom - Database Transactions Undermining Your AppSec

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# A Race to the Bottom - Database Transactions Undermining Your AppSec

11 Jul 2024 - Posted by Viktor Chuchurski

## Introduction

Databases are a crucial part of any modern application. Like any external dependency, they introduce additional complexity for the developers building an application. In the real world, however, they are usually considered and used as a black box which provides storage functionality.

This post aims shed light on a particular aspect of the complexity databases introduce which is often overlooked by developers, namely **concurrency control**. The best way to do that is to start off by looking at a fairly common code pattern we at Doyensec see in our day-to-day work:

```
func (db *Db) Transfer(source int, destination int, amount int) error {
  ctx := context.Background()

  conn, err := pgx.Connect(ctx, db.databaseUrl)
  defer conn.Close(ctx)

  // (1)
  tx, err := conn.BeginTx(ctx)

  var user User
  // (2)
  err = conn.
    QueryRow(ctx, "SELECT id, name, balance FROM users WHERE id = $1", source).
    Scan(&user.Id, &user.Name, &user.Balance)

  // (3)
  if amount <= 0 || amount > user.Balance {
    tx.Rollback(ctx)
    return fmt.Errorf("invalid transfer")
  }

  // (4)
  _, err = conn.Exec(ctx, "UPDATE users SET balance = balance - $2 WHERE id = $1", source, amount)
  _, err = conn.Exec(ctx, "UPDATE users SET balance = balance + $2 WHERE id = $1", destination, amount)

  // (5)
  err = tx.Commit(ctx)
  return nil
}
```

*Note: All error checking has been removed for clarity.*

For the readers not familiar with Go, hereâs a short summary of what the code is doing. We can assume that the application will initially perform authentication and authorization on the incoming HTTP request. When all required checks have passed, the `db.Transfer` function handling the database logic will be called. At this point the application will:

1. 1. Establish a new database transactions
2. 2. Read the source accountâs balance
3. 3. Verify that the transfer amount is valid with regard to the source accountâs balance and the applicationâs business rules
4. 4. Update the source and destination accountsâ balances appropriately
5. 5. Commit the database transaction

A transfer can be made by making a request to the `/transfer` endpoint, like so:

```
POST /transfer HTTP/1.1
Host: localhost:9009
Content-Type: application/json
Content-Length: 31

{
    "source":1,
    "destination":2,
    "amount":50
}
```

We specify the source and destination account IDs, and the amount to be transferred between them. The full source code, and other sample apps developed for this research can be found in our [playground](https://github.com/doyensec/db-race-conditions-playground) repo.

Before continuing reading, take a minute and review the code to see if you can spot any issues.

Notice anything? At first look, the implementation seems correct. Sufficient input validation, bounds and balance checks are performed, no possibility of SQL injection, etc. We can also verify this by running the application and making a few requests. Weâll see that transfers are being accepted until the source accountâs balance reaches zero, at which point the application will start returning errors for all subsequent requests.

Fair enough. Now, letâs try some more dynamic testing. Using the following Go script, let us try and make 10 concurrent requests to the `/transfer` endpoint. Weâd expect that two request will be accepted (two transfers of 50 with an initial balance of 100) and the rest will be rejected.

```
func transfer() {
	client := &http.Client{}

	body := transferReq{
		From:   1,
		To:     2,
		Amount: 50,
	}
	bodyBuffer := new(bytes.Buffer)
	json.NewEncoder(bodyBuffer).Encode(body)

	req, err := http.NewRequest("POST", "http://localhost:9009/transfer", bodyBuffer)
	if err != nil {
		panic(err)
	}
	req.Header.Add("Content-Type", `application/json`)
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	} else if _, err := io.Copy(os.Stdout, resp.Body); err != nil {
		panic(err)
	}
	fmt.Printf(" / status code => %v\n", resp.StatusCode)
}

func main() {
	for i := 0; i < 10; i++ {
		// run transfer as a goroutine
		go transfer()
	}
	time.Sleep(time.Second * 2)
	fmt.Printf("done.\n")
}
```

However, running the script we see something different. We see that almost all, if not all, of the request were accepted and successfully processed by the application server. Viewing the balance of both accounts with the `/dump` endpoint will show that the source account has a negative balance.

We have managed to overdraw our account, effectively making money out of thin air! At this point, any person would be asking âwhy?â and âhow?â. To answer them, we first need to take a detour and talk about databases.

## Database Transactions and Isolation Levels

Transactions are a way to define a logical unit of work within a database context. Transactions consist of multiple database operations which need to be successfully executed, for the unit to be considered complete. Any failure would result in the transaction being reverted, at which point the developer needs to decide whether to accept the failure or retry the operation. Transactions are a way to ensure [ACID](https://en.wikipedia.org/wiki/ACID) properties for database operations. While all properties are important to ensure data correctness and safety, for this post weâre only interested in the âIâ or Isolation.

In short, Isolation defines the level to which concurrent transactions will be isolated from each other. This ensures they always operate on correct data and donât leave the database in an inconsistent state. Isolation is a property which is directly controllable by developers. The [ANSI SQL-92](https://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt) standard defines four isolation levels, which we will take a look at in more detail later onm, but first we need to understand why we need them.

### Why Do We Need Isolation?

The isolation levels are introduced to eliminate read phenomena or unexpected behaviors, which can be observed when concurrent transactions are being performed on the set of data. The best way to understand them is with a short example, graciously borrowed from [Wikipedia](https://en.wikipedia.org/wiki/Isolation_%28database_systems%29#Read_phenomena).

#### Dirty Reads

Dirty reads allow transactions to read uncommitted changes made by concurrent transactions.

```
-- tx1
BEGIN;
SELECT age FROM users WHERE id = 1; -- age = 20
-- tx2
BEGIN;
UPDATE users SET age = 21 WHERE id = 1;
-- tx1
SELECT age FROM users WHERE id = 1; -- age = 21
-- tx2
ROLLBACK; -- the second read by tx1 is reverted
```

#### Non-Repeatable Reads

Non-repeatable reads allow sequential `SELECT` operations to return different results as a result of concurrent transactions modifying the same table entry.

```
-- tx1
BEGIN;
SELECT age FROM users WHERE id = 1; -- age = 20
-- tx2
UPDATE users SET age = 21 WHERE id = 1;
COMMIT;
-- tx2
SELECT age FROM users WHERE id = 1; -- age = 21
```

#### Phantom Reads

Phantom reads allow sequential `SELECT` operations on a set of entries to return different results due to modifications done by concurrent transactions.

```
-- tx1
BEGIN;
SELECT name FROM users WHERE age > 17; -- returns [Alice, Bob]
-- tx2
BEGIN;
INSERT INTO users VALUES (3, 'Eve', 26);
COMMIT;
-- tx1
SELECT name FROM users WHERE age > 17; -- retu...