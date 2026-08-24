# SQL

T-SQL (Microsoft SQL Server) tutorials plus HackerRank SQL exercise
solutions.

## mssql_tutorial/

T-SQL scripts from a SQL Server tutorial series, Parts 2–9 (Part 8 is
split into two files). Each file is a self-contained script meant to be
run top-to-bottom in a SQL Server session.

| File | Topic |
|---|---|
| `Part2.sql` | Creating, altering & dropping a database |
| `Part3.sql` | Creating and working with tables |
| `Part4.sql` | Adding a DEFAULT constraint |
| `Part5.sql` | Cascading referential integrity constraint |
| `Part6.sql` | Adding a CHECK constraint |
| `Part7.sql` | Identity column in SQL Server |
| `Part8-1.sql`, `Part8-2.sql` | Getting the last generated identity value |
| `Part9.sql` | UNIQUE key constraint |

### How to run it

Requires a SQL Server instance (e.g.
[SQL Server 2022 Express](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
or the free [Azure SQL Edge](https://learn.microsoft.com/en-us/sql/sql-edge/))
and a client — [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
on Windows/macOS, or `sqlcmd`.

Open each script in its own query window and run the batches in order
(the scripts use the T-SQL `GO` batch separator). **Part 2 first** — it
creates `myDatabase`, which Parts 3–9 all `USE`. If you re-run a script,
drop the objects it creates first, or the statements will error.

## hackerrank/

Solutions to HackerRank SQL problems (Basic Select, Advanced Select,
Basic Join, Aggregation tracks). Standard SQL against HackerRank's
sandbox databases (`CITY`, `EMPLOYEE`, etc.).

### How to work through it

Each file contains several problems — the problem title is the `#`
comment above its query. Re-create the problem's table on
[sqlbasics](https://sqlbasics.org/) or in any SQL client, then verify
your query against the expected output on the HackerRank problem page.
