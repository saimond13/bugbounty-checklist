# bugbounty_nuclei_ffuf_whatweb.py

import os
import subprocess
from datetime import datetime

def run_command(command, output_file):
    with open(output_file, 'w') as f:
        subprocess.run(command, shell=True, stdout=f, stderr=subprocess.DEVNULL)

def setup_dirs(target):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f"bugbounty_{target}_{timestamp}"
    os.makedirs(base_dir, exist_ok=True)
    return base_dir

def run_nuclei(urls_file, output_dir):
    print("[+] Running nuclei...")
    run_command(f"nuclei -l {urls_file} -o {output_dir}/nuclei.txt", f"{output_dir}/nuclei_output.log")

def run_ffuf(domain, output_dir):
    print("[+] Running ffuf...")
    wordlist = "/usr/share/wordlists/dirb/common.txt"
    run_command(f"ffuf -u https://{domain}/FUZZ -w {wordlist} -o {output_dir}/ffuf.json -of json", f"{output_dir}/ffuf_output.log")

def run_whatweb(domain, output_dir):
    print("[+] Running WhatWeb...")
    run_command(f"whatweb {domain}", f"{output_dir}/whatweb.txt")

def main():
    target = input("Enter target domain (e.g. example.com): ")
    urls_file = input("Enter path to alive URLs list (e.g. alive.txt): ")

    output_dir = setup_dirs(target)

    run_nuclei(urls_file, output_dir)
    run_ffuf(target, output_dir)
    run_whatweb(target, output_dir)

    print(f"[+] All scans saved in {output_dir}")

if __name__ == "__main__":
    main()
