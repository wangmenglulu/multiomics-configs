# Differential expression analysis

- Differential expression datasets are Label-free, TMT or DIA datasets public in PRIDE.
- They can be run using multiple sdrf files depending on the variable under study (factor value).
- The analyses are run against the Human Swiss-Prot including isoforms (Homo-sapiens-uniprot-reviewed-isoforms-contaminants-decoy-202105.fasta). This is important because in other projects like the proteogenomics, we run against a bigger databases including variants etc. Using UNIPROT/Isoforms we aim to identified and quantified only canonical reviewed proteins.

- All the data is deposited in: https://ftp.pride.ebi.ac.uk/pride/data/proteomes/differential-expression/

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
- [x] [PXD012998](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD012998.1-histologic-subtype/)
- [x] PXD015270:
    - [cell-lines](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD015270.1-cell-lines/)
    - [organism-part](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD015270.2-organism-part/)
- [x] PMID25238572: This dataset needs to be annotated across multiple datasets in PRIDE as described in the manuscript:
    - [cell-lines](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPMID25238572.1-cell-lines/)
    - [tumor](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPMID25238572.2-organism-part/)
- [x] [PXD019123](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD019123.1-disease/)
- [x] [PXD025864](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD025864.1-disease/)
- [x][PXD023508]
    - [mutation-carrier](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD023508.1-mutation-carrier/)
    - [disease](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD023508.2-disease/)
    - [phenotype](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD023508.3-phenotype/)
- [x][PXD023272](https://ftp.pride.ebi.ac.uk/pride/data/proteomes/proteogenomics/differential-expression/RPXD023272.1-organism-part/)


**Failing**
- [x] PMID25238572: This dataset needs to be annotated across multiple datasets in PRIDE as described in the manuscript: **Failing**
    - total(**Failing because the number of fractions is different across samples, still not supported by ProteomicsLFQ**)
- [x] PXD014458 (**Failing because the TRFP do not convert all the scans to mzML**)
