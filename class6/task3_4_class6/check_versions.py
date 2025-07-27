import requests
import numpy
import sys
import pkg_resources 

print("Tasks - Virtual Environments - Task 3:")
print("--- Installed Package Versions ---")

try:
    print(f"requests version: {requests.__version__}")
except AttributeError:
    print(f"requests version (pkg_resources): {pkg_resources.get_distribution('requests').version}")

try:
    print(f"numpy version: {numpy.__version__}")
except AttributeError:
    print(f"numpy version (pkg_resources): {pkg_resources.get_distribution('numpy').version}")

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version.split(' ')[0]}\n") # Get just the version number