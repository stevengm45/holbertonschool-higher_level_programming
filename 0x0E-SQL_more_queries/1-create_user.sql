-- create the MySQL server user user_0d_1

CREATE USER IF NOT EXISTS "user_0d_1"@"localhost" IDENTIFY BY "user_0d_1pwd";
GRANT ALL PRIVILEGES ON *.* TO "user_0d_1"@"localhost";
