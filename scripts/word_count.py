#!/usr/bin/env python3
"""
@author: Arthur

Counts words in each chapter, and total,
 toward user given overall desired total.

Exports to html file
"""
import subprocess
import os
import glob
import pandas as pd
import numpy as np

TOTAL_NUM_WRDS = 10000

print('Performing word count in Python!')
list_of_files = glob.glob(os.path.join('chapters',
                                       '*.tex'),
                          recursive=False)
list_of_files.sort()

f_names = [x.split('/')[-1].split('.')[0] for x in list_of_files]
counts = []
no_chapters = len(f_names)
for tex_file in list_of_files:
    process = subprocess.Popen(
        ['texcount', '-1', tex_file], stdout=subprocess.PIPE)
    out, err = process.communicate()
    counts.append(eval(out.split()[0]))
counts.append(np.sum(counts))
f_names.append('Total')
df = (pd.DataFrame((zip(f_names, counts)))
      .rename(columns={0: 'Chapter', 1: 'Count'}))
wrds_per_chap = TOTAL_NUM_WRDS/no_chapters
df['Percent'] = 100.0*df['Count'].divide(wrds_per_chap)
df['Diff'] = df['Count']-wrds_per_chap
df = df.set_index('Chapter')
df.loc['Total', 'Percent'] = 1.0E2*df.loc['Total', 'Count']/TOTAL_NUM_WRDS
df.loc['Total', 'Diff'] = df.loc['Total', 'Count']-TOTAL_NUM_WRDS
df = df.astype(np.float)
df.to_html('book_word_stats.html',
           justify='center',
           float_format='{:1.0f}'.format)
