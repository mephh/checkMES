import re
#This function looks through tokenlog.dat file and saves serial numbers into array
def check_serial_number():
    with open ('TOKENLOG.DAT', 'r') as tokenlog:
        snum = []
        for line in tokenlog:
            if 'Serial No=' in line:  #jak linia dluzsza niz dlugosc sn to blad i zeskanuj ponownie - DO NAPISANIA
                line = line[10:29]
                snum.append(line)
    print(snum)
    print(len(snum))
    if (len(snum)>2):
        check_batch()


def check_batch(): #checks start.bat for SN coding
    with open ('start.bat', 'r') as batch:
        coding = []
        for line in batch:
            if 'CODE=' in line:
                line = re.search('\[(.*)\]', line)
                coding = line.group(1)
                print(coding)

def check_config(): #checks config file for SN coding
    with open ('config.dat', 'r') as batch:
        coding = []
        for line in batch:
            if 'CODE=' in line:
                line = re.search('\[(.*)\]', line)
                coding = line.group(1)
# def check_mes():
#
#     url = 'http://plkwim0app07/jrwebservices/mes.asmx/GetBoardHistory?CustomerName=HoneyWell&pstrSerialNo=100024581812000036&pSep='
#     response = urllib2.urlopen(url)
#     the_page = response.read()
#     the_page = re.search('<string>(.*)</string>', the_page)
#     print(the_page.group(1))
#     print subprocess.Popen("@echo udalo sie", shell=True, stdout=subprocess.PIPE).stdout.read()
#     print subprocess.Popen("pause", shell=True, stdout=subprocess.PIPE).stdout.read()
#
#     if "ICT ICT" in the_page:
#             if "Fail" in the_page:
#                  ncr = True #placeholder
#             if "Repair Repair" in the_page:
#                 if "Present" in the_page:
#                  ncr = True #placeholder


check_serial_number()
#check_batch()

