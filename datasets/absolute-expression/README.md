# Absolute Expression datasets

Absolute datasets are specific datasets that can be used to compute for each protein an absolute expression value (e.g. IBAQ). Absolute expression datasets are mainly two types of datasets DIA-LFQ and DDA-LFQ.

We have divided the datasets in four main categories:

- cell-lines: experiments from cancer cell-lines
- tissues: experiments from healthy/normal human tissues
- platelet: experiments from platelet / serum / plasma
- tumor: experiments from different tumor

Each category contains a set of folders representing the different projects annotated, in each project samples are divided as follows:

- If more than one sample are available for the same factor value (e.g. tissue, cell-line, etc) they are aggregated into one sdrf.tsv using biological or technical replicates. With this approach, we can enable in the analysis Match-Between runs for better performance o the identification results.
- If no replication is available in the project (biological or technical), the full project can be divided by samples.

## How to select datasets

For absolute expression projects, we have a set of rules to select the project to be annotated:

- Samples MUST be from healthy/normal tissues.
- For absolute quantification we will use only Trypsin-derived samples. We have decided that because, if we add more enzymes, more variability is found across experiments making difficult the final comparisons.

## Factor values

For each category the factor value is different:

- cell-lines: the factor value is the cell-line code `characteristics[cell line]`
- tissues: experiments from healthy/normal human tissues `characteristics[organism part]`
- platelet: experiments from platelet / serum / plasma `characteristics[organism part]`
- tumor: experiments from different tumor  `characteristics[disease]`

## Datasets

- PXD000561: LFQ experiment, tissue proteomes, 2212 raw files
- PXD000865: LFQ experiment, tissue proteomes, 1055 raw files
- PXD010154: LFQ experiment, tissue proteomes, 1800 raw files
- PXD020192: LFQ experiment, tissue proteomes, 92 raw files

- brain:
  - PXD000547 & PXD000548: LFQ experiment, brain, 80 raw files
  - PXD012755: LFQ experiment, brain, 32 raw files

- skin:
  - PXD019909: LFQ experiment, tissue proteomes, 152 raw files

