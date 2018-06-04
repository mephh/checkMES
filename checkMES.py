#import urllib.request
import re
import urllib2
import subprocess
#This function looks through tokenlog.dat file and saves serial numbers into array
def check_serial_number():
    with open ('TOKENLOG.DAT', 'r') as tokenlog:
        snum = []
        for line in tokenlog:
            if 'Serial No=' in line:
                line = line[10:29]
                snum.append(line)
    print(snum)


def check_mes():

    url = 'http://plkwim0app07/jrwebservices/mes.asmx/GetBoardHistory?CustomerName=HoneyWell&pstrSerialNo=100024581812000036&pSep='
    response = urllib2.urlopen(url)
    the_page = response.read()
    the_page = re.search('<string>(.*)</string>', the_page)
    print(the_page.group(1))
    print subprocess.Popen("@echo udalo sie", shell=True, stdout=subprocess.PIPE).stdout.read()
    print subprocess.Popen("pause", shell=True, stdout=subprocess.PIPE).stdout.read()

    if "ICT ICT" in the_page:
            if "Fail" in the_page:
                 ncr = True #placeholder
            if "Repair Repair" in the_page:
                if "Present" in the_page:
                 ncr = True #placeholder


try:
    check_serial_number()
except:
    print("Blad barkodu. Prosze ponownie zeskanowac produkty")
try:
    check_mes()
except:
    print("Blad komunikacji z MES")
print('Done.')
