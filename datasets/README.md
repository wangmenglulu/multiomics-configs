# Datasets under study:

Datasets under study are divided into two different categories:

- differential-expression: label-free, or TMT. In differential expression datasets are analyzed completely.
- absolute-expression: Absolute expression is divided into cell-lines dataets, tissues and datasets are analyzed by Sample.

Some datasets are reuse between the two categories (differential-expression or absolute-expression) depending on the type of analysis performed.

## Differential Expression analysis:

- Differential expression datasets are Label-free or TMT datasets public in PRIDE.
- They can be run using multiple sdrf files depending on the variable under study (factor value).
- The analyses are run against the Human Swiss-Prot including isoforms (Homo-sapiens-uniprot-reviewed-isoforms-contaminants-decoy-202105.fasta). This is important because in other projects like the proteogenomics, we run against a bigger databases including variants etc. Using UNIPROT/Isoforms we aim to identified and quantified only canonical reviewed proteins.

- All the data is deposited in: https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/

### Differential Expression Label-Free

The datasets are run using the pipeline [proteomicsLFQ](https://github.com/nf-core/proteomicslfq).

- The parameters used for proteomicsLFQ are:

```bash
nextflow run /hps/nobackup2/proteomics/yperez_temp/proteomicslfq/main.nf -c /hps/nobackup2/proteomics/yperez_temp/proteomicslfq/nextflow.config -profile conda,lsf --root_folder **RAW_FILES** --database Homo-sapiens-uniprot-reviewed-isoforms-contaminants-decoy-202105.fasta --input SDRF --search_engines comet,msgf --protein_level_fdr_cutoff 0.01 --psm_pep_fdr_cutoff 0.05 --targeted_only false --outdir SDRF_OUTPUT --protein_inference bayesian --protein_quant shared_peptides --add_triqler_output -resume
```


#### Cancer datasets:

**Already Done***
- [x] [PXD002395](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD002395.1-cell-line/)
- [x] [PXD004682](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD004682.1-organism-part/)
- [x] [PXD005571](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD005571.2-phenotype-subtype/)
    - [phenotype](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD005571.1-phenotype/)
    - [subtype](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD005571.3-subtype/)
- [x] [PXD008440](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD008440.1-disease-response/)
- [x] [PXD008722](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD008722.1-organism-part/)
- [x] [PXD012431](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD012431.1-organism-part/)
- [ ] [PXD012998](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD012998.1-histologic-subtype/)
- [x] PXD015270:
    - [cell-lines](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD015270.1-cell-lines/)
    - [organism-part](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD015270.2-organism-part/)
- [x] PMID25238572: This dataset needs to be annotated across multiple datasets in PRIDE as described in the manuscript:
    - [cell-lines](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPMID25238572.1-cell-lines/)
    - [tumor](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPMID25238572.2-organism-part/)

**Running**

- [ ] PXD002137

**Under annotation**

- [ ] PXD001048
- [x] PXD002137
- [x] PXD015744
- [x] PXD019123
- [ ] PXD025864: To be annotated
- [x] PXD002395
- [x] PXD003351
- [x] PXD005571
- [x] PXD009630
- [x] PXD012923
- [x] PXD023272
- [ ] PXD022268
- [ ] PXD020224
- [ ] PXD021865
- [ ] PXD020426
- [ ] PXD001724 and PXD001725:

**Failing**
- [x] PMID25238572: This dataset needs to be annotated across multiple datasets in PRIDE as described in the manuscript: **Failing**
    - total(**Failing because the number of fractions is different across samples, still not supported by ProteomicsLFQ**)
- [x] PXD014458 (**Failing because the TRFP do not convert all the scans to mzML**)

#### Others

- [ ] PXD008934: To be Run
- [ ] PXD012755: To be Run

## Absolute Expression analysis:

Absolute expression analysis is run using different datasets split by Sample accession. For every dataset, the multiple Samples are included in the results' folder.

### Tissues Proteomes

- [ ] PXD000561: **Running**
- [X] [PXD020192](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/absolute-expression/proteomes/RPXD020192.1-organism-part/)
- [ ] PXD010154: **Running**
- [ ] PXD006675: **Running**

Plasma Datasets:

- [ ] PXD004242: **Running**

**To be annotated**
- [ ] PXD000865
- [ ] PXD009261
- [ ] PXD009737
- [ ] PXD009021
- [ ] PXD002854

**Pending**

- [ ] PXD012755
- [ ] PXD008934
- [ ] PXD008722
- [ ] PXD006675
- [ ] PXD023650

- Ovarian Tissue Proteome (https://www.ebi.ac.uk/pride/archive/projects/PXD008183) (To be annotated)
- Hart Tissue proteome (https://www.ebi.ac.uk/pride/archive/projects/PXD005736) (To be annotated)
- Choroid tissue (https://www.ebi.ac.uk/pride/archive/projects/PXD002273) (To be annotated)
- Brain Proteome (https://www.ebi.ac.uk/pride/archive/projects/PXD005445) (Annotated wronly)
- Pancreas (https://www.iprox.org/page/project.html?id=IPX0001745000) (To be annotated)
- Eccrine sweat glands (https://www.ebi.ac.uk/pride/archive/projects/PXD010637) (To be annotated)


### Tumor data

- PXD012431 (High-throughput mass spectrometry and bioinformatics analysis of breast cancer proteomic data):
    - SDRF: https://github.com/bigbio/proteomics-metadata-standard/blob/4905da47fbbbdd9879333b76687028e4b88f5459/annotated-projects/PXD012431/sdrf.tsv
    - PRIDE: https://www.ebi.ac.uk/pride/archive/projects/PXD012431
    - Publication: http://europepmc.org/article/MED/31294064
    - biology: breast cancer, label-free

### Synthectic Projects

- PXD000759

## Cancer Cell-lines datasets

These datasets are use for IBAQ-based absolute quantification. Some of then can be also seen in the Differential expression section.

#### Label-free experiments
- [ ] PXD000396: (This dataset is analytical)
- [ ] PXD002395
- [ ] PXD003209
- [ ] PXD004452 (Running - DecoyPyrat)
- [ ] PXD005366
- [ ] PXD005698
- [ ] PXD005940
- [ ] PXD005942
- [x] PXD005946 (small errors in some Samples)
- [x] PXD012255
- [x] PXD015270
- [x] PXD019263 (Running - DecoyPyrat)

#### TMT experiments analyzed as Label-free
- [x] PXD014145 (Finish - http://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/pgdb-manuscript/PXD014145-Sample-1/)


Number of Samples: 246
Number of Raw Files: 2360

Comments:

The following samples are not in CBioPortal or Cosmic: (PXD002395-Sample-17, PXD002395-Sample-2, PXD002395-Sample-32, PXD004452-Sample-15, PXD004452-Sample-18, PXD005946-Sample-11)


