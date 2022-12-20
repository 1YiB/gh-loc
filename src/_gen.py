import random
import string

from src._config import config


def gen_username() -> str:


    strg_len:int = config['gen', 'length'] # type:ignore
    strg = random.choices(string.ascii_lowercase + string.digits, k=strg_len)

    res: str = ''.join(strg)

    return res
