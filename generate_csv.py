from re import compile
from imaplib import IMAP4_SSL
from smtplib import SMTP_SSL
from time import sleep

### USER PARAMETERS ###
jpl_email = "horizons@ssd.jpl.nasa.gov"
username = "sample_address@email"
password = 'xxxx'  # can also hardcode the pwd
site_coord = "'116.383300,39.9166000, 0.0'" 
start_time = "'2019-10-21'"
stop_time = "'2020-10-20'"
output_name = 'filename'

bodies = "'301'"
step_size = "'1 d'"
### USER PARAMETERS ###

message = f"""Subject: JOB

!$$SOF
COMMAND = {bodies}
CENTER= 'coord@399'
COORD_TYPE= 'GEODETIC'
SITE_COORD= {site_coord}
MAKE_EPHEM= 'YES'
TABLE_TYPE= 'OBSERVER'
START_TIME= {start_time}
STOP_TIME= {stop_time}
STEP_SIZE= {step_size}
CAL_FORMAT= 'CAL'
TIME_DIGITS= 'MINUTES'
ANG_FORMAT= 'DEG'
OUT_UNITS= 'KM-S'
RANGE_UNITS= 'AU'
APPARENT= 'AIRLESS'
SUPPRESS_RANGE_RATE= 'NO'
SKIP_DAYLT= 'NO'
EXTRA_PREC= 'NO'
R_T_S_ONLY= 'NO'
REF_SYSTEM= 'J2000'
CSV_FORMAT= 'YES'
OBJ_DATA= 'NO'
TIME_ZONE = '+00:00'
QUANTITIES= '1' 
!$$EOF
"""

# https://realpython.com/python-send-email/
smtp_server = "smtp.gmail.com"
smtp_ssl_port = 465
try:
    server = SMTP_SSL(smtp_server, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(username, jpl_email, message)
except Exception as e:
    print(e)
finally:
    server.quit()
sleep(240)

# login to read email
imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
try:
    server = IMAP4_SSL(imap_ssl_host, imap_ssl_port)
    server.login(username, password)
    server.select('INBOX')
except Exception as e:
    print(e)

# parse the inbox and read emails
limiter = compile(r'[*]{5,}')
reg = compile(r'\A\d+')
typ, data = server.search(None, '(FROM "Horizons Ephemeris System")')
assert len(data[0].split()) != 0, "no ephemeris emails found"
for num in data[0].split():
    typ, data = server.fetch(num, '(UID BODY[HEADER])')
    subject = [x for x in data[0][1].splitlines() if x.startswith(b'Subject: ')][0][9:].decode()
    if subject.startswith("[Horizons] BATCH Submittal"):
        print("Horizons could not process one or more requests." +
            " Check BATCH Submittal Results email for my info.")
        continue
    if subject.endswith('(2/2)') or subject.startswith('[Horizons] SRCH3'):
        continue

    typ, data = server.fetch(num, '(UID BODY[TEXT])')
    text = data[0][1].decode().splitlines()[2:-1]
    f_name = ''
    top = 5
    while top:
        while limiter.fullmatch(text[0]) is None:
            if top == 3 and text[0].startswith('Target body name:'):
                # first line: {Horizons Name} {(id #)}]
                f_name = reg.sub('', text[0][18:text[0].find('{')].strip())
                f_name = f_name.split()[0].lower()
            text = text[1:]
        text = text[1:]
        top -= 1

    if subject.endswith('(1/2)'):
        data = server.search(None, f'(SUBJECT "{subject[:-5]}(2/2)")')[1]
        typ, data = server.fetch(data[0], '(UID BODY[TEXT])')
        additional = data[0][1].decode().splitlines()[2:-1]
        text += additional

    while limiter.fullmatch(text[-1]) is None:
        text = text[:-1]
    text = [text[0]] + text[3:-2]

    with open(f'{output_name}.csv', 'w') as f:
        for x in text:
            f.write(x + '\n')
server.close()
server.logout()
