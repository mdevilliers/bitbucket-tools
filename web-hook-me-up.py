#!/usr/bin/env python

from __future__ import print_function

import os

from argparse import ArgumentParser
from argparse import Action

from pybitbucket.bitbucket import Client
from pybitbucket.auth import BasicAuthenticator
from pybitbucket.repository import Repository,RepositoryRole
from pybitbucket.hook import Hook

def main():

  # secrets from ENV
  parser = ArgumentParser(
        'web_hook_me_up.py',
        description="Tool to copy add a WebHook to all of your bitbucket repos."
  )

  parser.add_argument(
        '-username', required=True,
        action=EnvDefault, envvar='BITBUCKET_USERNAME',
        help='Bitbucket username (or BITBUCKET_USERNAME environment variable)'
  )

  parser.add_argument(
        '-password', required=True,
        action=EnvDefault, envvar='BITBUCKET_PASSWORD',
        help='Bitbucket password (or BITBUCKET_PASSWORD environment variable)'
  )

  parser.add_argument(
        '-email', required=True,
        action=EnvDefault, envvar='BITBUCKET_EMAIL',
        help='Bitbucket email (or BITBUCKET_EMAIL environment variable)'
  )

  opts = parser.parse_args()

  bitbucket = Client(
            BasicAuthenticator( opts.username, opts.password, opts.email))

  # things to change
  description='Hook for slack'
  url="https://hooks.slack.com/services/XXXXXXXXXXXXXX"
  ownner="XXXXXXX"
  events=['issue:created','issue:updated', 'pullrequest:created', 'pullrequest:approved']

  repositories = Repository.find_repositoris_by_owner_and_role(client=bitbucket, role=RepositoryRole.ADMIN, owner=owner)

  for repo in repositories:
    print (repo.name)

    allhooks = Hook.find_hooks_in_repository(
      owner=owner,
      repository_name=repo.name.lower(),
      client=bitbucket
      )

    for hook in allhooks:
      if 'description' in hook and hook.description == description:
        print("existing hook deleted!")
        hook.delete()

    # print(allhooks)
    Hook.create_hook(
        repository_name=repo.name.lower(),
        description=description,
        callback_url=url,
        active=events,
        username=owner,
        client=bitbucket
    )


# http://stackoverflow.com/questions/10551117/setting-options-from-environment-variables-when-using-argparse
class EnvDefault(Action):
    """Inspects the environment for a variable
    before looking for a command line value"""
    def __init__(self, envvar, required=True, default=None, **kwargs):
        if not default and envvar:
            if envvar in os.environ:
                default = os.environ[envvar]
        if required and default:
            required = False
        super(EnvDefault, self).__init__(default=default, required=required,
                                         **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


if __name__ == '__main__':
    main()
