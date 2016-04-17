bitbucket-tools
---------------

Collection of tools to manage bitbucket repositories

installation
------------

```
pip install -r requirements.txt
```

web-hook-me-up.py
-----------------

Will add a webhook for every bitbucket repositiory for an organisation.


```
python web-hook-me-up.py -h
usage: web_hook_me_up.py [-h] -username USERNAME -password PASSWORD -email
                         EMAIL

Tool to copy add a WebHook to all of your bitbucket repos.

optional arguments:
  -h, --help          show this help message and exit
  -username USERNAME  Bitbucket username (or BITBUCKET_USERNAME environment
                      variable)
  -password PASSWORD  Bitbucket password (or BITBUCKET_PASSWORD environment
                      variable)
  -email EMAIL        Bitbucket email (or BITBUCKET_EMAIL environment
                      variable)
```

Change the following variables in the file as appropriate -

```
  description='Hook for slack'
  url="https://hooks.slack.com/services/XXXXXXXXXXXXXX"
  owner="XXXXXXX"
  events=['issue:created','issue:updated', 'pullrequest:created', 'pullrequest:approved']

```

