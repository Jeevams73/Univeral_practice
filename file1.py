#!/bin/bash

echo "System Information:"
echo "-------------------"

python3 <<EOF
import platform

print("System:", platform.system())
print("Node Name:", platform.node())
print("Release:", platform.release())
print("Processor:", platform.processor())
EOF
