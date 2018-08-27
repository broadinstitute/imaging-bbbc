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

IMAGE_SETS = {'BBBC001': u'Human HT29 colon-cancer cells',
              'BBBC002': u'<i>Drosophila</i> Kc167 cells',
              'BBBC003': u'Mouse embryos',
              'BBBC004': u'Synthetic cells',
              'BBBC005': u'Synthetic cells',
              'BBBC006': u'Human U2OS cells (out of focus)',
              'BBBC007': u'<i>Drosophila</i> Kc167 cells',
              'BBBC008': u'Human HT29 colon-cancer cells',
              'BBBC009': u'Human red blood cells',
              'BBBC010': u'<i>C. elegans</i> live/dead assay',
              'BBBC011': u'<i>C. elegans</i> metabolism assay',
              'BBBC012': u'<i>C. elegans</i> infection marker',
              'BBBC013': u'Human U2OS cells cytoplasm–nucleus translocation',
              'BBBC014': u'Human U2OS cells cytoplasm–nucleus translocation',
              'BBBC015': u'Human U2OS cells transfluor',
              'BBBC016': u'Human U2OS cells transfluor',
              'BBBC017': u'Human HT29 colon-cancer cells shRNAi screen',
              'BBBC018': u'Human HT29 colon-cancer cells (diverse phenotypes)',
              'BBBC019': u'Collective cell migration',
              'BBBC020': u'Murine bone-marrow derived macrophages',
              'BBBC021': u'Human MCF7 cells &ndash; compound-profiling experiment',
              'BBBC022': u'Human U2OS cells &ndash; compound-profiling Cell Painting experiment',
              'BBBC024': u'3D HL60 Cell Line (synthetic data)',
              'BBBC025': u'Human U2OS cells &ndash; RNAi Cell Painting experiment',
              'BBBC026': u'Human Hepatocyte and Murine Fibroblast cells &ndash; Co-culture experiment',
              'BBBC027': u'3D Colon Tissue (synthetic data)',
              'BBBC028': u'Polymerized structures',
              'BBBC029': u'Synthetic DIC Images',
              'BBBC030': u'Chinese Hamster Ovary Cells',
              'BBBC031': u'Simulated 24-well plate with synthetic cells',
              'BBBC032': u'Mouse embryo blastocyst cells',
              'BBBC033': u'Mouse trophoblast stem cells',
              'BBBC034': u'Induced pluripotent human stem cells',
              'BBBC035': u'Simulated HL60 cells (from the Cell Tracking Challenge)',
              'BBBC036': u'Human U2OS Cells – profiling bioactive compounds using Cell Painting',
              'BBBC037': u'Human U2OS cells - Gene overexpression profiling experiment',
              'BBBC038': u'Kaggle 2018 Data Science Bowl',
              'BBBC039': u'Nuclei of U2OS cells in a chemical screen',
              'BBBC040': u'Human U2OS cells – Small molecule Cell Painting experiment',
              'BBBC041': u'P. vivax (malaria) infected human blood smears',
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
