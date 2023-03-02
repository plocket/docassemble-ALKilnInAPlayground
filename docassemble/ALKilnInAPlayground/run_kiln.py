from docassemble.base.functions import log
import subprocess
# https://stackoverflow.com/a/89243/14144258
# https://docs.python.org/3/library/subprocess.html#subprocess.run

__all__ = ['do_shell']

def do_shell():
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
  command = ['node', 'console.log(\'foo\');']
  outcome = subprocess.run(command, check=False, capture_output=True)
  log(f'returncode = {outcome.returncode}', 'console')
  if outcome.returncode != 0:
    # there was an error, we assume the traceback was printed to stderr
    log('there was an error :\n', 'console')
    return(outcome.stderr.decode('utf-8'), 'console')
  else:
    return outcome
  return 'foo'
