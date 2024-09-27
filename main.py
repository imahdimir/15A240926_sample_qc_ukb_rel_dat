"""

Alex email on Sep 24, 2024, 11:18AM PST

Also, you will need to filter based on sample QC. Have you been able to locate the sample qc file on the RAP? It may be with the phenotype data.

The sample QC file is described here: https://biobank.ctsu.ox.ac.uk/crystal/refer.cgi?id=531

You will need to filter out samples that are not in the White British ancestry subset, have excess relatives, are flagged as having outlying heterozygosity/missingness (het.missing.outliers), and are flagged as having a sex chromosome aneuploidy.

Also, I found an answer to the sample ID within files/filenames: https://dnanexus.gitbook.io/uk-biobank-rap/frequently-asked-questions#are-the-headers-of-gvcf-or-cram-files-pseudonymized


columns in the sampel qc:

https://biobank.ctsu.ox.ac.uk/crystal/ukb/docs/ukb_genetic_data_description.txt

in.white.British.ancestry.subset (0/1)	(no/yes) Indicates samples who self-reported 'White British' and have very similar genetic ancestry based on a principal components analysis of the genotypes. See genotype QC documentation for details.
excess.relatives		      (0/1)	(no/yes) Indicates samples which have more than 10 putative third-degree relatives in the kinship table.
het.missing.outliers		      (0/1)	(no/yes) Indicates samples identified as outliers in heterozygosity and missing rates, which indicates poor-quality genotypes for these samples.
putative.sex.chromosome.aneuploidy    (0/1)	(no/yes) Indicates samples identified as putatively carrying sex chromosome configurations that are not either XX or XY. These were identified by looking at average log2Ratios for Y and X chromosomes. See genotype QC documentation for details.

"""

from pathlib import Path

import pandas as pd


class Directory :
    proj_data = '/Users/mmir/Library/CloudStorage/Dropbox/git/15A240926_sample_qc_ukb_rel_dat_CSF'
    proj_data = Path(proj_data)
    p = proj_data



DIR = Directory()
D = DIR


class FilePath :
    d = Directory()

    # file id on RAP: file-Fy3V3G8JkF6199F34yJ8K14F
    # /Bulk/Genotype Results/Genotype calls/ukb_sqc_v2.txt
    ukb_sqc_v2 = '/ukb_sqc_v2.txt'

    filtered_ids = d.p / 'filtered_ids.txt'


FILE_PATH = FilePath()
FP = FILE_PATH


class Var :
    pass


VAR = Var()
V = VAR


def read_and_add_col_names_to_ukb_sqc_v2() :
    pass

    ##

    # this column names are from: https://github.com/kenhanscombe/ukbtools/blob/master/R/genetics_qc.R   03edd9f

    cols = ["x1" , "x2" , "genotyping.array" , "Batch" , "Plate.Name" , "Well" ,
            "Cluster.CR" , "dQC" , "Internal.Pico..ng.uL." ,
            "Submitted.Gender" , "Inferred.Gender" , "X.intensity" ,
            "Y.intensity" , "Submitted.Plate.Name" , "Submitted.Well" ,
            "sample.qc.missing.rate" , "heterozygosity" ,
            "heterozygosity.pc.corrected" , "het.missing.outliers" ,
            "putative.sex.chromosome.aneuploidy" , "in.kinship.table" ,
            "excluded.from.kinship.inference" , "excess.relatives" ,
            "in.white.British.ancestry.subset" , "used.in.pca.calculation" , ]

    # print it a dictionary format with keys start from zero
    for i , col in enumerate(cols) :
        print(f'{i} : "{col}",')

    ##
    col_names = {
            0  : "x1" ,
            1  : "x2" ,
            2  : "genotyping.array" ,
            3  : "Batch" ,
            4  : "Plate.Name" ,
            5  : "Well" ,
            6  : "Cluster.CR" ,
            7  : "dQC" ,
            8  : "Internal.Pico..ng.uL." ,
            9  : "Submitted.Gender" ,
            10 : "Inferred.Gender" ,
            11 : "X.intensity" ,
            12 : "Y.intensity" ,
            13 : "Submitted.Plate.Name" ,
            14 : "Submitted.Well" ,
            15 : "sample.qc.missing.rate" ,
            16 : "heterozygosity" ,
            17 : "heterozygosity.pc.corrected" ,
            18 : "het.missing.outliers" ,
            19 : "putative.sex.chromosome.aneuploidy" ,
            20 : "in.kinship.table" ,
            21 : "excluded.from.kinship.inference" ,
            22 : "excess.relatives" ,
            23 : "in.white.British.ancestry.subset" ,
            24 : "used.in.pca.calculation" ,
            }
    ##
    _dtype = pd.StringDtype()
    _sep = ' '  # single space
    _fp = FP.ukb_sqc_v2
    df_sqc = pd.read_csv(_fp , sep = _sep , header = None , dtype = _dtype)

    ##
    df_sqc = df_sqc.rename(columns = col_names)
    df_sqc = df_sqc[col_names.values()]

    ##
    return df_sqc

    ##


def filter_sample_qc() :
    pass

    ##
    df_sqc = read_and_add_col_names_to_ukb_sqc_v2()

    ##
    cols_value = {
            'in.white.British.ancestry.subset'   : '1' ,
            'excess.relatives'                   : '0' ,
            'het.missing.outliers'               : '0' ,
            'putative.sex.chromosome.aneuploidy' : '0' ,
            }

    ##
    for col , value in cols_value.items() :
        df_sqc = df_sqc[df_sqc[col] == value]

    ##
    df_filtered_ids = df_sqc[['x2']]

    ##
    df_filtered_ids.to_csv(FP.filtered_ids , index = False , header = None)

    ##


def main() :
    pass

    ##
    filter_sample_qc()

    ##


##
if __name__ == '__main__' :
    main()
