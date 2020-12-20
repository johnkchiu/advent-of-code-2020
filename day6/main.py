#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import click

def read_file(input):
  lines = open(input,'r').read().splitlines()
  print(lines)

  # with open(input, 'r') as file:
  #     for line in file:
  #       print(line)
  return lines

@click.command()
@click.argument('input')
def main(input):
    click.echo(f'Using input file: {input}')
    part1(input)
    part2(input)

def part1(input):
  sum = 0
  answers = set()

  lines = read_file(input)
  for i, line in enumerate(lines):
    for v in line.strip():
        answers.add(v)

    if line == '' or i == len(lines)-1:  # empty or last line
      sum += len(answers)
      print(f'answers: {answers}')
      answers = set()

  print(f'sum: {sum}')


def part2(input):
  pass

if __name__ == '__main__':
    main()
