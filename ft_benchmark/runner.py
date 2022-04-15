import subprocess
from subprocess import CompletedProcess
from typing import List

from ft_benchmark.executable_type import ExecutableType


class RunnerConfig(list):
    pass


class RunMetrics(object):
    pass


class Result(CompletedProcess):
    pass


class Runner(object):

    def __init__(self, exec_type: ExecutableType = ExecutableType.DEFAULT) -> None:
        self.exec_type: ExecutableType = exec_type
        super().__init__()

    # args, *, stdin = None, input = None, stdout = None, stderr = None, capture_output = False, shell = False,
    # cwd = None, timeout = None, check = False, encoding = None, errors = None, text = None, env = None,
    # universal_newlines = None, ** other_popen_kwargs)

    def run(self, config: RunnerConfig) -> subprocess.CompletedProcess:
        args: List = config
        args.insert(0, self.exec_type.value)
        return subprocess.run(args=args, check=True, capture_output=True)
