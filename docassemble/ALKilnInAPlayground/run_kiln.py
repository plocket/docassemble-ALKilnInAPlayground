import subprocess
from docassemble.base.functions import log
# https://stackoverflow.com/a/89243/14144258

__all__ = ['do_shell']

def do_shell():
  foo = subprocess.run("echo bar", shell=True, check=True, capture_output=True, text=True);
  #log('console', foo);
  log(foo.stdout, 'console');
  return foo
