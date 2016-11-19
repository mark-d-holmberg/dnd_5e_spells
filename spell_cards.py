#!/usr/bin/env python

import argparse
import csv
import json

from pprint import pprint

__author__ = 'austen0'

SPELLS = 'dnd_5e_spells.csv'

def new_spell_list(out, classes):
  spell_names = get_spell_index(SPELLS, 3)
  spell_classes = get_spell_index(SPELLS, 16)
  spell_dict = dict(zip(spell_names, spell_classes))

  spells = []
  for name, spell_c in spell_dict.iteritems():
    if any(c in spell_c for c in classes.split(',')):
      spells.append(name)

  with open(out, 'wb') as out:
    writer = csv.writer(out)
    for spell in sorted(spells):
      writer.writerow(['#%s' % spell])

def get_spell_index(src_file, index):
  spell_index = []
  with open(src_file, 'rb') as src:
    reader = csv.reader(src)
    reader.next()
    for row in reader:
      if not row[index].startswith('#'):
        spell_index.append(row[index])
  return spell_index

def fmt_spell_text(text):
  font_size = 11
  if len(text) > 250:
    font_size = 10
  if len(text) > 300:
    font_size = 9
  if len(text) > 400:
    font_size = 8
  if len(text) > 550:
    text = text[0:550]
    text += '... (see ref for full text)'
    font_size = 7

  full_text = []
  lines = text.split('<br> ')
  for line in lines:
    full_text.append('text | <span style="font-size:%spx">%s' % (
      font_size, line))
  return full_text

def fmt_spell_title(title):
  font_size = 17
  if len(title) > 20:
    font_size = 15
  if len(title) > 26:
    font_size = 13
  if len(title) > 29:
    font_size = 11

  return '<span style="font-size:%spx">%s' % (font_size, title)

def gen_spell_json(src_file, json_tmpl):
  desired_spells = get_spell_index(src_file, 0)
  found_spells = []
  with open(SPELLS, 'rb') as src:
    spells = []
    reader = csv.reader(src)
    reader.next()
    for row in reader:
      if row[3] in desired_spells:
        found_spells.append(row[3])

        spell = json_tmpl.copy()
        contents = []
        contents.append('subtitle | %s' % row[6])
        contents.append('rule')
        contents.append('property | Casting time | %s' % row[7])
        contents.append('property | Range | %s' % row[8])
        contents.append('property | Duration | %s' % row[9])
        contents.append('property | Components | %s' % row[10])
        contents.append('rule')
        contents.extend(fmt_spell_text(row[14]))
        contents.append('fill')
        contents.append('subtitle | <span style="font-size:8px">[%s]' % row[19])

        spell['title'] = fmt_spell_title(row[3])
        spell['tags'] = ['spell_level_%s' % row[4], row[0]]
        spell['icon'] = 'white-book-%s' % row[4]
        spell['contents'] = contents

        spells.append(spell)

  if len(spells) > 0:
    out = json.dumps(spells)
    out_name = src_file.replace('.csv', '.json')
    with open(out_name, 'wb') as out_file:
      out_file.write(out)

    print 'Generated %s spells to \'%s\':' % (len(found_spells), out_name)
    for s in found_spells:
      print s
    #pprint(spells)
  else:
    print 'No spells in list.'

def arg_parser():
  parser = argparse.ArgumentParser(description='D&D Spell JSON Generator')
  parser.add_argument(
    '--new_spell_list',
    dest='new_spell_list',
    type=str,
    help='generate new spell list to filepath'
  )
  parser.add_argument(
    '--classes',
    dest='classes',
    type=str,
    default='B,C,D,M,P,R,S,W,Z',
    help='specify classes for new spell list'
  )
  parser.add_argument(
    '--gen_spell_json',
    dest='gen_spell_json',
    type=str,
    help='generate spell json from filepath'
  )
  parser.add_argument(
    '--color',
    dest='color',
    type=str,
    help='specify card color'
  )
  parser.add_argument(
    '--icon_back',
    dest='icon_back',
    type=str,
    help='specify card back icon'
  )
  return parser.parse_args()

def main():
  args = arg_parser()

  json_tmpl = { 'count': 1 }
  if args.color:
    json_tmpl['color'] = args.color
  if args.icon_back:
    json_tmpl['icon_back'] = args.icon_back

  if args.new_spell_list:
    new_spell_list(args.new_spell_list, args.classes)
  if args.gen_spell_json:
    gen_spell_json(args.gen_spell_json, json_tmpl)

if __name__ == '__main__':
  main()
