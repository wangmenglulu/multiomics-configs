import csv

import pandas as pd
import click

@click.command()
@click.option('--input', help='sdrf')
@click.option('--property', help='property to split')
def main(input, property):
    """Simple program that greets NAME for a total of COUNT times."""
    df = pd.read_csv(input, sep='\t', skip_blank_lines=False)
    d = dict(tuple(df.groupby(property)))
    for key in d:
      dataframe = d[key]
      name_file = 'sdrf-' + key.replace(" ", "-")+ '.tsv'
      dataframe.to_csv(name_file ,sep='\t', quoting=csv.QUOTE_NONE, index=False)
    print(d)

if __name__ == '__main__':
    main()
