#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import click

def read_file(input):
  # lines = open(input,'r').read().splitlines()
  # print(lines)

  # with open(input, 'r') as file:
  #     for line in file:
  #       print(line)

@click.command()
@click.argument('input')
def main(input):
    click.echo(f'Using input file: {input}')
    read_file(input)

if __name__ == '__main__':
    main()
