# Run a directory brute force
from src.recon import dir_bruteforce

results = dir_bruteforce.scan("http://example.com", wordlist="common.txt")
print("Discovered directories:", results)