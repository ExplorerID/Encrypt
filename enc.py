#Facebook Farhan Tanzim Sagor
# Python Bytecode : 3.8
# Time Succses Parser : Sat June  11 13:53:32 2022
# Auto Parser Dis Version : 1.2.1
# Source : https://www.github.com/Sagor-BCZ

import marshal, os, time
h = '\x1b[1;92m'
bi = '\x1b[1;96m'
k = '\x1b[1;93m'
u = '\x1b[1;95m'
pu = '\x1b[1;97m'
b = '\x1b[1;94m'
m = '\x1b[1;91m'
hi = '\x1b[1;30m'
hg = '\x1b[4;92m'
p = '\x1b[0m'

def logo():
    os.system('clear')
    print( """\n
  \033[1;91m       ____  ___ _    __________
\033[1;92m        / __ \/   | |  / /  _/ __ \\
\033[1;91m       / / / / /| | | / // // / / /
\033[1;92m      / /_/ / ___ | |/ // // /_/ /
\033[1;91m     /_____/_/  |_|___/___/_____/
------------------------------------------
 \33[1;92m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
\33[1;92m█  \33[mGithub: https://github.com/\33[1;92mSagor-BCZ
\33[1;92m█  \33[mFacebook: \33[1;92mMd. Sagor Monsi
   Facebook: Farhan Tanzim Sagor
   Fb Group: BD CYBER ZONE (BCZ)
\33[1;92m█  \33[mFb Page: \33[1;92m+MRZ
\33[1;92m█  \33[mTools : \33[1;92mFREE
\33[1;92m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""" )
    print(hi + '------------------------------------------')


def main():
    try:
        logo()
        print(p + '[' + h + '+' + p + '] ' + k + 'Ex ' + m + ': ' + p + '/sdcard/filename.py')
        a = input(p + '[' + h + '+' + p + '] ' + pu + 'File ' + m + ': ' + h)
        x = open(a).read()
        b = compile(x, '<BCZ>', 'exec')
        c = a.replace('.py', '_enc.py')
        d = marshal.dumps(b)
        e = open(c, 'w')
        e.write('# Compile by BCZ\n#Facebook : Farhan Tanzim Sagor\n#Facebook : Md.Sagor Monsi\n# Github  : https://github.com/Sagor-BCZ\n#Facebook Group : Bd Cyber Zone (BCZ)\n')
        e.write('import marshal\n')
        e.write('exec(marshal.loads(' + repr(d) + '))')
        e.close()
        time.sleep(2)
        print(p + '[' + h + '+' + p + '] ' + pu + 'Files Encrypted ' + m + ': ' + h + c)
        os.system('xdg-open https://www.facebook.com/sagor.official.0')
        time.sleep(0.1)
    except IOError:
        print(p + '[' + m + 'x' + p + '] ' + pu + 'File Not Found')
        time.sleep(1)
        main()
    except KeyboardInterrupt:
        out()


def out():
    time.sleep(0.1)
    print(p + '[' + h + '+' + p + '] ' + p + 'Thanks For Using This My Tools')
    os.system('xdg-open https://www.facebook.com/sagor.official.0')
    time.sleep(1)
    exit(p + '[' + m + '!' + p + '] ' + p + 'Exit')


try:
    main()
except KeyboardInterrupt:
    out()
