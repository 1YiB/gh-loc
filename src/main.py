import logging

import fire
from rich.logging import RichHandler

from src import _gen, _rest, _site
from src._config import ConfigPaths, config


def rest_api(n: int) -> None:

    # log file
    log_file = (

        f"{ConfigPaths.data_dir}\\{config['api', 'rest', 'log_file']}"
    )  
    # logger
    logger = logging
    logger.basicConfig(
        handlers=[
            RichHandler(),
            logging.FileHandler(log_file),
        ],
        level=logging.INFO,
        format='%(message)s',
    )
    # generate n usernames
    for _ in range(n):
        usr = _gen.gen_username()
        if _rest.rest_verify(usr):
            logging.info(usr)


def site_api() -> None:
    # log file
    log_file = f"{ConfigPaths.data_dir}\\{config['api', 'site', 'log_file']}"
    # logger
    logger = logging
    logger.basicConfig(
        handlers=[
            RichHandler(),
            logging.FileHandler(log_file),
        ],
        level=logging.INFO,
        format='%(message)s',
    )
    # data file
    data_file = f"{ConfigPaths.data_dir}\\{config['api', 'rest', 'log_file']}"
    # read data from data file and verify data
    with open(file=data_file, encoding='utf-8', mode='a+') as f:

        usernames = f.readlines()
        for username in usernames:
            if _site.verify_username(username=username):
                logger.info(username)


def app() -> None:
    fire.Fire(
        {
            'rest': rest_api,
            'site': site_api,
        }
    )
