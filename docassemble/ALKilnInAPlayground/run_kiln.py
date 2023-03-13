from docassemble.base.functions import log
import subprocess
# https://stackoverflow.com/a/89243/14144258
# https://docs.python.org/3/library/subprocess.html#subprocess.run

__all__ = ['do_shell']

'''
tests can run locally and on GitHub
The Computer has a docker container with node
want tests to run, user to see the result, download generated files
want not on GitHub, not do something on their local machine, I want to do it on The Computer
'''

def do_shell():
  #command = ['npm', 'install', '@suffolklitlab/alkiln', '/tmp']
  #tmp = ''
  #with subprocess.Popen(command, stdout=subprocess.PIPE) as proc:
  #  while True:
  #    line = proc.stdout.readline()
  #    if not line: break
  #    tmp += line
  #    output = tmp
  #output = tmp
  #return output
  
  ## Working
  #try:
  #  foo = subprocess.run(["node", "console.log('foo');"], check=True, capture_output=True, text=True);
  #  return foo
  #except BaseException as error:
  #  # subprocess.CalledProcessError?
  #  log(str(error), 'console')
  #  if hasattr(error, 'message'):
  #      log(error.message, 'console')
  #      return error.message
  #  else:
  #      return error
  
  ## Trying next
  command = ['npm', 'install', '@suffolklitlab/alkiln']
  outcome = subprocess.run(command, check=False, capture_output=True)
  log(f'returncode = {outcome.returncode}', 'console')
  if outcome.returncode != 0:
    # there was an error, we assume the traceback was printed to stderr
    log('there was an error :\n', 'console')
    log(outcome.stderr.decode('utf-8'), 'console')
    return(outcome.stderr.decode('utf-8'))
  else:
    log(outcome, 'console')
    return outcome
  
  return 'foo'
