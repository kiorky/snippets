#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

import csv
class csv_dialect(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_ALL

def runcsv(self, output):
    rows = []
    titles = []
    output_filename = '%s.csv' % output
    fic = open(output_filename, "w")
    csvwriter = csv.DictWriter(fic,
                               fieldnames=titles,
                               extrasaction='ignore',
                               dialect = csv_dialect)
    titles_row = dict([(title, title) for title in titles])
    csvwriter.writerows([titles_row])
    for i, row in enumerate(rows):
        for cell in row:
            if isinstance(row[cell], unicode):
                row[cell] = row[cell].encode('utf-8')
    csvwriter.writerows(rows)
    fic.flush()
    fic.close()


# vim:set et sts=4 ts=4 tw=80:
