from enum import Enum


class ExecutableType(Enum):
    SCRAM = 'scram'
    XFTA = 'xfta'
    ECHO = 'echo'
    DEFAULT = ECHO
