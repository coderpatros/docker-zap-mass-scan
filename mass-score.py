#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import traceback

def parse_results (site, date, is_summary_file, file):
  last_line = ''
  rra = ''

  with open('wiki/scan-results/' + site + '/' + date, 'rt') as f:
    for line in f:
      if line.startswith('LINK: '):
        rra = line[5:].rstrip('\n')
      else:
        last_line = line.rstrip('\n')

    if len(last_line) > 0:
      scores = last_line.split('\t')
      if last_line.startswith('FAIL-NEW:'):
        # format is: FAIL-NEW: x    FAIL-INPROG: x    WARN-NEW: x    WARN-INPROG: x    INFO: x    IGNORE: x    PASS: x
        fail_new = scores[0].split(': ')[1]
        fail_ip = scores[1].split(': ')[1]
        warn_new = scores[2].split(': ')[1]
        warn_ip = scores[3].split(': ')[1]
        info = scores[4].split(': ')[1]
        ignore = scores[5].split(': ')[1]
        passes = scores[6].split(': ')[1]
        # Just add the new and in progress scores for now..
        fail = str(int(fail_new) + int(fail_ip))
        warn = str(int(warn_new) + int(warn_ip))
      else:
        # Stable format is: FAIL: x    WARN: x    INFO: x    IGNORE: x    PASS: x
        fail = scores[0].split(': ')[1]
        warn = scores[1].split(': ')[1]
        info = scores[2].split(': ')[1]
        ignore = scores[3].split(': ')[1]
        passes = scores[4].split(': ')[1]

      if len(rra) > 0:
        file.write ('| [' + site + '](' + rra + ')')
      else:
        file.write ('| ' + site)
      
      file.write(' | ')
      if int(fail) > 0:
        file.write ('![fail: ' + fail + '](https://img.shields.io/badge/scan-fail%20' + fail + '-critical.svg)')
      if int(warn) > 0:
        file.write ('![warn: ' + warn + '](https://img.shields.io/badge/scan-warn%20' + warn + '-important.svg)')
      if int(info) > 0:
        file.write ('![info: ' + info + '](https://img.shields.io/badge/scan-info%20' + info + '-informational.svg)')
      if int(ignore) > 0:
        file.write ('![ignore: ' + ignore + '](https://img.shields.io/badge/scan-ignore%20' + ignore + '-inactive.svg)')
      if int(passes) > 0:
        file.write ('![pass: ' + passes + '](https://img.shields.io/badge/scan-pass%20' + passes + '-success.svg)')

      if is_summary_file:
        file.write (' | [' + date + '](scan-' + site + '-history.md) |')
      else:
        file.write (' | [' + date + '](scan-results/' + site + '/' + date +') |')
      file.write ('\n')

def handle_site (name, summary_file):
  f = open('wiki/scan-' + name + '-history.md','w')
  f.write('## ' + name + '\n\n')
  f.write('| Site | Status | Date | \n')
  f.write('| --- | --- | --- |\n')

  all_files = sorted(os.listdir('wiki/scan-results/' + name), reverse=True)
  if len(all_files) > 0:
    parse_results(name, all_files[0], True, summary_file)
    for file in all_files:
      parse_results(name, file, False, f)

  f.write ('\n [Back to summary page](summary)\n')
  f.close()

if __name__ == '__main__':
  summary_file = open('wiki/summary.md','w')
  # Header
  summary_file.write('| Site | Status | History | \n')
  summary_file.write('| --- | --- | --- |\n')

  last_file = ''
  last_site = ''
  for file in sorted(os.listdir('wiki/scan-results')):
    if os.path.isdir('wiki/scan-results/' + file):
      handle_site(file, summary_file)

  summary_file.close()

