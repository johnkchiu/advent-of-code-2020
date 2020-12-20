#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import click


@click.command()
@click.argument('day')
def main(day):
    click.echo(f'Creating new day: {day}')
    cmds = f'''
      mkdir -p {day}
      cp -rf _template.py {day}/main.py
    '''
    os.system(cmds)

if __name__ == '__main__':
    main()
