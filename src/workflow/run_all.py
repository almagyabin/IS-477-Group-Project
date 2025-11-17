import subprocess

if __name__ == "__main__":
    subprocess.run(["snakemake", "-j", "1"], check=True)
