from core.library.Utils import Singleton
import datetime


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    MAIN = '\033[0;30;43m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger(Singleton):
    __enable_from = False

    def __init__(self):
        super().__init__()

    @classmethod
    def info(cls, msg, from_module=None):
        t = datetime.datetime.now()
        from_t = f'{Colors.GREEN}[From] {from_module}{Colors.END}' if cls.__enable_from else ''
        print(
            f"{Colors.CYAN} [Info] {t.strftime('%H:%M:%S')}{Colors.END} {from_t} {msg}")

    @classmethod
    def output(cls, msg, from_module=None):
        t = datetime.datetime.now()
        from_t = f'{Colors.GREEN}[From] {from_module}{Colors.END}' if cls.__enable_from else ''
        print(
            f"{Colors.BLUE} [Output] {t.strftime('%H:%M:%S')}{Colors.END} {from_t} {msg}")

    @classmethod
    def warn(cls, msg, from_module=None):
        t = datetime.datetime.now()
        from_t = f'{Colors.GREEN}[From] {from_module}{Colors.END}' if cls.__enable_from else ''
        print(
            f"{Colors.WARNING} [Warning] {t.strftime('%H:%M:%S')}{Colors.END} {from_t} {msg}")

    @classmethod
    def danger(cls, msg, from_module=None):
        t = datetime.datetime.now()
        from_t = f'{Colors.GREEN}[From] {from_module}{Colors.END}' if cls.__enable_from else ''
        print(
            f"{Colors.FAIL} [Failed] {t.strftime('%H:%M:%S')}{Colors.END} {from_t} {msg}")

    @classmethod
    def main(cls, msg):
        t = datetime.datetime.now()
        from_t = f'{Colors.GREEN}[From] {Colors.END}' if cls.__enable_from else ''
        print(
            f"{Colors.MAIN} [MainThread] {t.strftime('%H:%M:%S')} {from_t} {msg}{Colors.END}")

    @classmethod
    def enable_from(cls):
        cls.__enable_from = True
