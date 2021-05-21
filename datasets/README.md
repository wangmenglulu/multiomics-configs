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

- [ ] PMID25238572: This dataset needs to be annotated across multiple datasets in PRIDE as described in the manuscript: **Running**
   - [cell-lines]
   - [tumor]
   - [total]
- [ ] PXD001048
- [ ] PXD002137: To be annotated
- [ ] PXD002395: **Running**
- [x] [PXD004682](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD004682.1-organism-part/)
- [ ] PXD008440: To be annotated
- [x] [PXD015270](https://www.ebi.ac.uk/pride/archive/projects/PXD015270): This project is divided in two different SDRFs
    - [cell-lines](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD015270.1-cell-lines/)
    - [organism-part](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD015270.2-organism-part/)
- [ ] PXD012431: **Running**
- [ ] PXD014458: **Failing**
- [ ] PXD003351: To be annotated
- [ ] PXD005571: To be annotated
- [ ] PXD009630: **Running**
- [ ] PXD012923: To be annotated
- [ ] PXD012998: To be annotated
    - [cell-lines]
    - [phenotype]
- [ ] PXD015744: To be annotated
- [ ] PXD019123: To be annotated
- [ ] PXD025864: To be annotated
- [ ] PXD023272
- [ ] PXD022268
- [ ] PXD020224
- [ ] PXD021865
- [ ] PXD020426
- [ ] PXD001724 and PXD001725:

#### Others

- [ ] PXD008722: Running
- [ ] PXD008934: To be Run
- [ ] PXD012755: To be Run


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

## Absolute Expression analysis:

### Tissues Proteomes

- [ ] PXD020192: (Running HX)
- [ ] **PXD000561**: (Running HH)
- [ ] PXD010154: (Running HH)
- [x] PXD012755: (Running HH)
- [ ] PXD008934: (Running HH)
- [x] PXD008722: (Running HH)
- [ ] PXD006675: (Running HH)

- Ovarian Tissue Proteome (https://www.ebi.ac.uk/pride/archive/projects/PXD008183) (To be annotated)
- Hart Tissue proteome (https://www.ebi.ac.uk/pride/archive/projects/PXD005736) (To be annotated)
- Choroid tissue (https://www.ebi.ac.uk/pride/archive/projects/PXD002273) (To be annotated)
- Brain Proteome (https://www.ebi.ac.uk/pride/archive/projects/PXD005445) (Annotated wronly)
- Pancreas (https://www.iprox.org/page/project.html?id=IPX0001745000) (To be annotated)
- Eccrine sweat glands (https://www.ebi.ac.uk/pride/archive/projects/PXD010637) (To be annotated)

### Fluid Proteomes (Plasma, Urine)

- [ ] PXD023650 (To be annotated)

### Cancer cell-lines


### Tumor data

- PXD012431 (High-throughput mass spectrometry and bioinformatics analysis of breast cancer proteomic data):
    - SDRF: https://github.com/bigbio/proteomics-metadata-standard/blob/4905da47fbbbdd9879333b76687028e4b88f5459/annotated-projects/PXD012431/sdrf.tsv
    - PRIDE: https://www.ebi.ac.uk/pride/archive/projects/PXD012431
    - Publication: http://europepmc.org/article/MED/31294064
    - biology: breast cancer, label-free

### Synthectic Projects

- PXD000759


