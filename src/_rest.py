from ratelimiter import RateLimiter

from src._config import Rest


@RateLimiter(max_calls=5000, period=3600)
def rest_verify(username: str) -> bool:
    res = Rest.Client.get(url=f'/{username}')

    if res.status_code == 404:
        return True
    return False
