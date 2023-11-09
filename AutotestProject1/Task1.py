import subprocess

def command_file(directory:str, specified_text: str):
    result = subprocess.run(directory, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        lst = out.split("\n")
        if specified_text in lst:
            return True
        return False
    return False

if __name__ == '__main__':
    print(command_file('cat /etc/os-release', 'SUPPORT_URL="https://help.ubuntu.com/"'))