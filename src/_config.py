from dataclasses import dataclass
from pathlib import Path

import httpx
import tomli
from ndicts.ndicts import NestedDict


@dataclass()
class ConfigPaths:
    # config paths dataclass

    HOME: Path = Path.expanduser(Path('~'))

    config_dir=Path(f'{HOME}\\.config\\gh-loc\\')
    config_file=Path(f'{HOME}\\.config\\gh-loc\\config.toml')
    data_dir=Path(f'{HOME}\\.config\\gh-loc\\data')

    __dirs__ = [config_dir,data_dir]
    __files__ = [config_file]

# create config files
for x,y in zip(ConfigPaths.__dirs__,ConfigPaths.__files__):
    x.mkdir(parents=True,exist_ok=True)
    open(file=y,mode='a+')

# read config.toml
with open(ConfigPaths.config_file, 'r+b') as f:
    config = NestedDict(tomli.load(f))


# for official gh rest api
class Rest:

    Env = config['api', 'rest']

    Client = httpx.Client(
        base_url=Env['base_url'],
        auth=(
            Env['gh_username'],
            Env['gh_token'],
        ),
    )


# for unofficial gh api , experimental
class Site:
    Env = config['api', 'site']
    Client = httpx.Client(
        base_url=Env['base_url'],
        cookies=Env['cookies'],
        headers=Env['headers'],
    )
