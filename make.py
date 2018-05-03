#!/usr/bin/env python
# -*- Encoding: utf-8 -*-
# -*- coding: utf-8 -*-

import jinja2
import datetime
import re
from os import stat
from sys import argv
import os
import glob

def icons(base):
    return dict(
        C='<a href="{0}benchmarking.html#cellCounting" class="badge" rel="tooltip" title="Counts">C</a>'.format(base),
        FB='<a href="{0}benchmarking.html#foregroundBackground" class="badge" rel="tooltip" title="Foreground/background">F</a>'.format(base),
        H='<a href="{0}benchmarking.html#humanLabel" class="badge" rel="tooltip" title="Outlines of objects">O</a>'.format(base),
        B='<a href="{0}benchmarking.html#bioLabel" class="badge" rel="tooltip" title="Biological labels">B</a>'.format(base))

IMAGE_SETS = {'BBBC001': 'Human HT29 colon-cancer cells',
              'BBBC002': '<i>Drosophila</i> Kc167 cells',
              'BBBC003': 'Mouse embryos',
              'BBBC004': 'Synthetic cells',
              'BBBC005': 'Synthetic cells',
              'BBBC006': 'Human U2OS cells (out of focus)',
              'BBBC007': '<i>Drosophila</i> Kc167 cells',
              'BBBC008': 'Human HT29 colon-cancer cells',
              'BBBC009': 'Human red blood cells',
              'BBBC010': '<i>C. elegans</i> live/dead assay',
              'BBBC011': '<i>C. elegans</i> metabolism assay',
              'BBBC012': '<i>C. elegans</i> infection marker',
              'BBBC013': u'Human U2OS cells cytoplasm–nucleus translocation',
              'BBBC014': u'Human U2OS cells cytoplasm–nucleus translocation',
              'BBBC015': 'Human U2OS cells transfluor',
              'BBBC016': 'Human U2OS cells transfluor',
              'BBBC017': 'Human HT29 colon-cancer cells shRNAi screen',
              'BBBC018': 'Human HT29 colon-cancer cells (diverse phenotypes)',
              'BBBC019': 'Collective cell migration',
              'BBBC020': 'Murine bone-marrow derived macrophages',
              'BBBC021': 'Human MCF7 cells &ndash; compound-profiling experiment',
              'BBBC022': 'Human U2OS cells &ndash; compound-profiling Cell Painting experiment',
              'BBBC024': '3D HL60 Cell Line (synthetic data)',
              'BBBC025': 'Human U2OS cells &ndash; RNAi Cell Painting experiment',
              'BBBC026': 'Human Hepatocyte and Murine Fibroblast cells &ndash; Co-culture experiment',
              'BBBC027': '3D Colon Tissue (synthetic data)',
              'BBBC028': 'Polymerized structures',
              'BBBC029': 'Synthetic DIC Images',
              'BBBC030': 'Chinese Hamster Ovary Cells',
              'BBBC031': 'Simulated 24-well plate with synthetic cells',
              'BBBC032': 'Mouse embryo blastocyst cells',
              'BBBC033': 'Mouse trophoblast stem cells',
              'BBBC034': 'Induced pluripotent human stem cells',
              'BBBC035': 'Simulated HL60 cells (from the Cell Tracking Challenge)',
              'BBBC036': u'Human U2OS Cells – profiling bioactive compounds using Cell Painting',
              'BBBC037': u'Human U2OS cells - Gene overexpression profiling experiment',
              'BBBC038': 'Kaggle 2018 Data Science Bowl',
}

PAGES = [('index', 'Introduction', ''),
         ('image_sets', 'Image sets', 'Image sets'),
         ('benchmarking', 'Benchmarking', 'Benchmarking methodology'),
         #('software', 'Software', 'Software'),
         ('contribute', 'Contribute', 'Contribute to the BBBC')]

def proper_path(relative):
    d = os.path.dirname(argv[0])
    if d:
        return os.path.join(d, relative)
    else:
        return relative

def make_page(page, title=None, gt=None, tab=None, subdir=False, acc=None):
    input_filename = proper_path('templates/' + page + '.html')

    mtime = datetime.datetime.fromtimestamp(stat(input_filename)[8])

    if ((page == 'image_sets') or (tab == 'image_sets')):
        mtime = None
    if title is None:
        plain_title = None
    else:
        plain_title = re.sub("<[^>]*>", "", title)
    if acc:
        plain_title = acc + ': ' + plain_title
    loader = jinja2.FileSystemLoader('templates')
    env = jinja2.Environment(loader=loader)
    template = env.get_template(page + '.html')
    output_filename = proper_path(('htdocs/%s/index.html' if subdir else 'htdocs/%s.html') % page)
    output_dir = os.path.dirname(output_filename)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    f = open(output_filename, 'w')
    base = '../' if subdir else ''
    f.write(template.render(page=page,
                            tab=tab or page,
                            title=title, acc=acc,
                            plain_title=plain_title,
                            pages=PAGES,
                            image_sets=IMAGE_SETS,
                            base=base,
                            mdate=None if mtime is None else mtime.strftime("%Y-%m-%d"),
                            **icons(base)).encode('utf-8'))
    f.close()

for page, short_title, long_title in PAGES:
    make_page(page, long_title)

#for (section, pages) in IMAGE_SETS:
#    for (page, title, symbols) in pages:
#        make_page(page, title, gt=symbols, tab='image_sets')

for acc, title in IMAGE_SETS.items():
    make_page(acc, title, acc=acc, tab='image_sets', subdir=True)
