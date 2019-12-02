#!/usr/bin/python3

import subprocess
import sys
sys.path.append('/home/pi/WUPHF')
import text


def main():

    ifconfig = subprocess.check_output(['ifconfig', 'eth0']) 

    start = ifconfig.find('inet addr:') + len('inet addr:')
    end = ifconfig.find('Bcast') - 1

    ip = ifconfig[start:end]

    text.send_text('Pi running with IP: ' + ip)


if __name__ == '__main__':
    main()
