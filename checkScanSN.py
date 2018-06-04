import subprocess

def check_serial_number():
    with open ('TOKENLOG.DAT', 'r') as tokenlog:
        x=1
        for line in tokenlog:
            if 'Serial No=' in line:
                if (len(line))!=30:
                    x = str(x)
                    print""
                    print""
                    print""
                    print subprocess.Popen("@echo Zeskanowano bledna liczbe znakow na DUT"+x, shell=True, stdout=subprocess.PIPE).stdout.read()
                    print subprocess.Popen("@echo Wcisnij anuluj i zeskanuj produkty ponownie", shell=True, stdout=subprocess.PIPE).stdout.read()
                    print""
                    print""
                    print""
                    x = int(x)
                x=x+1

check_serial_number()