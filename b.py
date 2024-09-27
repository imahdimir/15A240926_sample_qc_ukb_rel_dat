"""


    """

# Import packages
# dxpy allows python to interact with the platform storage
import dxpy
import numpy as np
import pandas as pd
import re
import subprocess
import glob
import os


##
# Automatically discover dispensed dataset ID
dispensed_dataset = dxpy.find_one_data_object(
    typename='Dataset', name='app*.dataset', folder='/', name_mode='glob'
)
dispensed_dataset_id = dispensed_dataset['id']

##
# Get project ID
project_id = dxpy.find_one_project()['id']

##
dataset = (':').join([project_id, dispensed_dataset_id])

##
# Note: This cell can only be run once. Otherwise, you'll need to delete the existing data tables in order to re-run
cmd = ['dx', 'extract_dataset', dataset, '-ddd', '--delimiter', ',']
subprocess.check_call(cmd)


##
# Discover cohort data
dispensed_control_id = list(
    dxpy.find_data_objects(
        typename='CohortBrowser',
        folder='/Cohorts',
        name_mode='exact',
        name='ischemic_controls',
    )
)[0]['id']

##

dispensed_case_id = list(
    dxpy.find_data_objects(
        typename='CohortBrowser',
        folder='/Cohorts',
        name_mode='exact',
        name='ischemic_cases',
    )
)[0]['id']

##
field_ids = [
    '31',
    '2966',
    '22001',
    '22006',
    '22019',
    '22021',
    '21022',
    '23104',
    '20160',
    '30760',
    '30780',
    '22020',
    '22009'
]

##
data_dict_df = pd.read_csv('/Users/mmir/Library/CloudStorage/Dropbox/git/15A240926_sample_qc_ukb_rel_dat/app11425_20240515222223.dataset.data_dictionary.csv')
data_dict_df.head()

##
def fields_for_id(field_id):
    '''Collect all field names (e.g. 'p<field_id>_iYYY_aZZZ') given a list of field IDs and return string to pass into extract_dataset'''
    field_names = ['eid']
    for _id in field_id:
        select_field_names = list(
            data_dict_df[
                data_dict_df.name.str.match(r'^p{}(_i\d+)?(_a\d+)?$'.format(_id))
            ].name.values
        )
        # Note: This conditional is used to select only the first instance for all fields except '2966'
        # This conditional is not needed otherwise
        # For PCA field, select the first ten PCs
        if _id == '22009':
            field_names += select_field_names[:10]
        # Select only the first instance for all fields except '2966'
        elif _id != '2966' and len(select_field_names) > 1:
            field_names.append(select_field_names[0])
        else:
            field_names += select_field_names

    field_names = [f'participant.{f}' for f in field_names]
    return ','.join(field_names)

##
field_names = fields_for_id(field_ids)
field_names

##


##
