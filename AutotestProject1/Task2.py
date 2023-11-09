import subprocess
import string

def command_file(directory:str, specified_text: str, word = 'Yes'):
    result = subprocess.run(directory, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        lst = out.split("\n")
        if specified_text in lst:
            output = specified_text.translate(str.maketrans('', '', string.punctuation))
            print(output)
            return True

        if word in specified_text:
            print('Yes')
        else:
            print('No')
        return False
    return False







if __name__ == '__main__':
    print(command_file('cat /etc/os-release', 'VERSION="22.04.1 LTS (Jammy Jellyfish)"'))