from time import sleep

from src._config import Site


def verify_username(username: str) -> bool:
    """NOT DONE"""
    content = Site.Env['data']

    def filter_content(content: str) -> str:
        # TODO regex -> with {username} in data
        return content

    content = filter_content(content=content)

    r = Site.Client.post(
        content=content,
        url='',
    )

    if r.status_code == 200:
        return True

    if r.status_code == 429:
        print(
            """hit rate limit, waiting for 15 seconds.
            All verified names are avaiable in ~/.config/data/verified_names.log"""
        )
        sleep(secs=15)
        r = Site.Client.post(
            content=content,
            url='',
        )

    return False
