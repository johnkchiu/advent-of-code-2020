#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from collections import defaultdict

import click

def read_file(input):
  lines = open(input,'r').read().splitlines()
  # print(lines)

  # with open(input, 'r') as file:
  #     for line in file:
  #       print(line)
  return lines

def find_rule(rules, cur_color, find_color):
  if (cur_color not in rules): return False

  if (find_color in rules[cur_color]):
    return True
  else:
    for color, _ in rules[cur_color].items():
      if find_rule(rules, color, find_color): return True


def part1(input):
  # construct graph (with weights)
  rules = defaultdict(dict)
  print(rules)

  # build dict rules
  for line in read_file(input):
    line = line.replace('.','').replace('bags','').replace('bag','') # remove some words
    key, vals = line.split(' contain ')
    for val in vals.split(', '):
      weight, val = val.split(' ', 1)
      print(f'key: {key.strip()}, weight: {weight}, val: {val.strip()}')
      if (weight != 'no'):
        rules[key.strip()][val.strip()] = weight
  print(f'rules: {rules}')

  count = 0
  for color, rule in rules.items():
    print(f'color: {color}, rule: {rule}')
    if find_rule(rules, color, 'shiny gold'):
      print(f'found color: {color}')
      count += 1

  print(f'count: {count}')

def part2(input):
  pass

@click.command()
@click.argument('input')
def main(input):
    click.echo(f'Using input file: {input}')
    part1(input)
    part2(input)

if __name__ == '__main__':
    main()
