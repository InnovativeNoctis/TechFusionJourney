import argparse
import hashlib
import sys
from pathlib import Path


def hash_password(password: str, salt: str, algorithm: str) -> str:
    """Hash a password with an optional salt using the specified algorithm."""
    algorithm = algorithm.lower()

    salted_password = (salt + password).encode("utf-8")

    try:
        return hashlib.new(algorithm, salted_password).hexdigest()
    except ValueError:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}")


def generate_rainbow_table(password_file: str, output_file: str, salt: str, algorithm: str):
    """Generate a rainbow table from the given password file."""

    input_path = Path(password_file)
    output_path = Path(output_file)

    if not input_path.exists():
        print(f"[ERROR] Password file not found: {password_file}")
        sys.exit(1)

    try:
        with input_path.open("r", encoding="utf-8") as infile, \
             output_path.open("w", encoding="utf-8") as outfile:

            for line in infile:
                password = line.strip()
                if not password:
                    continue

                hashed = hash_password(password, salt, algorithm)
                outfile.write(f"{password}:{hashed}\n")

        print(f"[+] Rainbow table saved to {output_file}")

    except PermissionError:
        print("[ERROR] Permission denied while accessing files.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Rainbow Table Generator")

    parser.add_argument(
        "passwords",
        type=str,
        help="File containing passwords to hash"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="rainbow_table.txt",
        help="Output file for the rainbow table"
    )

    parser.add_argument(
        "-s", "--salt",
        type=str,
        default="",
        help="Optional salt to prepend to passwords"
    )

    parser.add_argument(
        "-a", "--algorithm",
        type=str,
        default="sha256",
        help="Hash algorithm (md5, sha1, sha256, etc.)"
    )

    args = parser.parse_args()

    generate_rainbow_table(
        args.passwords,
        args.output,
        args.salt,
        args.algorithm
    )


if __name__ == "__main__":
    main()