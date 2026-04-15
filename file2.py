#!/bin/bash

echo "Running Python program..."

python3 <<EOF
name = input("Enter your name: ")
print(f"Hello, {name}! This is Python running inside Bash.")
EOF
