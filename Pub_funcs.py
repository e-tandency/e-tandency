# *.* coding: utf-8 *.*
import collections
import subprocess

ExecutionResult = collections.namedtuple(
    'ExecutionResult',
    'status, stdout, stderr'
)

def execute(cmd, **kwargs):
    splitted_cmd = cmd.split()
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    try:
        process = subprocess.Popen(splitted_cmd, **kwargs)
        stdout, stderr = process.communicate()
        status = process.poll()
        return ExecutionResult(status, stdout, stderr)
    except OSError as e:
        print("Command exec error: '%s' %s" % (cmd, e))
        return ExecutionResult(1, '', '')


def Char_Rep(str,o_char,n_char):
    """
    Replace character
    """
    if o_char in str.replace(o_char, n_char):
        Char_Rep(str.replace(o_char, n_char),o_char,n_char)
    else:
        return str.replace(o_char, n_char)