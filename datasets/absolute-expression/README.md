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

### Tissues

- PXD000561: LFQ experiment, tissue proteomes, 2212 raw files
- PXD000865: LFQ experiment, tissue proteomes, 1055 raw files
- PXD010154: LFQ experiment, tissue proteomes, 1800 raw files
- PXD020192: LFQ experiment, tissue proteomes, 92 raw files
- PXD010271: LFQ experiment, tissue proteomes, 220 raw files

- brain:
  - PXD000547 & PXD000548: LFQ experiment, brain, 80 raw files
  - PXD012755: LFQ experiment, brain, 32 raw files

- skin:
  - PXD019909: LFQ experiment, skin, 152 raw files

- heart:
  - PXD008934: LFQ experiment, heart, 34 raw files
  - PXD006675: LFQ experiment, heart, 594 raw files
  - PXD005736: LFQ experiment, heart, 30 raw files

- stomach:
  - PXD008840: LFQ experiment, stomach, 504 raw files

- lung:
  - PXD004700: LFQ experiment, lung, 46 raw files

- Ovarian Tissue Proteome (https://www.ebi.ac.uk/pride/archive/projects/PXD008183) (To be annotated)
- Choroid tissue (https://www.ebi.ac.uk/pride/archive/projects/PXD002273) (To be annotated)
- Brain Proteome (https://www.ebi.ac.uk/pride/archive/projects/PXD005445) (Annotated wronly)
- Pancreas (https://www.iprox.org/page/project.html?id=IPX0001745000) (To be annotated)
- Eccrine sweat glands (https://www.ebi.ac.uk/pride/archive/projects/PXD010637) (To be annotated)


### Plasma

- PXD011839
- PXD004242

### Tumor datasets

- PXD012431 (High-throughput mass spectrometry and bioinformatics analysis of breast cancer proteomic data):
    - SDRF: https://github.com/bigbio/proteomics-metadata-standard/blob/4905da47fbbbdd9879333b76687028e4b88f5459/annotated-projects/PXD012431/sdrf.tsv
    - PRIDE: https://www.ebi.ac.uk/pride/archive/projects/PXD012431
    - Publication: http://europepmc.org/article/MED/31294064
    - biology: breast cancer, label-free
