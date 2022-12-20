<h3 align="center">
    gh-loc
</h3>
<h6 align="center">
    <a href="#install">Install</a>
    ·
    <a href="#config">Config</a>
    ·
    <a href="#usage">Usage</a>
</h6>

### Install

<br />

> pre-requisite: `python=^3.10` `pip` `conda(optional)` `gh-account` `git`

- clone git repo

```
$ git clone https://github.com/1YiB/gh-loc.git
```

- install `*.whl` file

```
$ cd gh-loc/dist
$ pip install <name of file>
```

- check if installed

```

$ which gh-loc # bash
$ where gh-loc # cmd
$ gcm gh-loc   # pwsh
```

### Config

- gh-loc must first be configured before being used.

- it can be configured using the `~/.config/gh-loc/config.toml` file

- the format is given below:

```toml
# ~/.config/gh-loc/config.toml

[gen]
# length of generate user names
length = 3

[api]


[api.rest]

# api url 
base_url = "https://api.github.com/users/"
# your username
gh_username = ""
# your github token (github.com/settings/tokens)
gh_token = ""

# file where available names are written
log_file = "names.log"

[api.site]

# advanced feature , does not work as of now
base_url = "https://github.com/signup_check/username"
cookies = {}
headers = {}
content = ""

data_file = "names.log" 
log_file = "verified_names.log"
```

### Usage

- Rest
    - official github api which requires token

``` 
$ gh-loc rest <number of usernames to generate>
```

- Site
    - unofficial github api which requires auth_token from website 
    -  does not work as of now
```
$ gh-loc site 
```

- Help Page

```
$ gh-loc --help
```