import sqlite3
import base64
import argparse
parser = argparse.ArgumentParser(description="Convert Gitea password hashes to hashcat format")
parser.add_argument (
    "-u", "--username",
    action="store_true",
    help="Include Username in the output"
)
parser.add_argument(
    "filename",
    type=str,
    help="Gitea database file"
)

try:
    args = parser.parse_args()
    conn = sqlite3.connect(args.filename)
    cursor = conn.cursor()
    cursor.execute("SELECT name, passwd_hash_algo, salt, passwd FROM user")
    for row in cursor.fetchall():
        name = row[0]
        if "pbkdf2" in row[1]:
            algo, iterations, keylen = row[1].split("$")
            algo = "sha256"
        else:
            raise Exception("Unknown Algorithm: " + row[1])
        salt = bytes.fromhex(row[2])
        passwd = bytes.fromhex(row[3])
        salt_b64 = base64.b64encode(salt).decode("utf-8")
        passwd_b64 = base64.b64encode(passwd).decode("utf-8")
        if args.username:
            print(f"{name}:",end="")
        print(f"{algo}:{iterations}:{salt_b64}:{passwd_b64}")
except Exception as e:
    print(f"Error: {e}")
    exit(1)






