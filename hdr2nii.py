# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:21:35 2019

@author: Jun Ma
"""

import SimpleITK as sitk
import os
join = os.path.join

#%% training set: convert hdr to nii
hdrpath = r'E:\Data\iSeg2019\iSeg-2019-Training'
niipath = r'E:\Data\iSeg2019\Task07_iSeg\imagesTr'
labelpath = r'E:\Data\iSeg2019\Task07_iSeg\labelsTr'

for i in range(1,11):
    label_name = 'subject-'+str(i)+'-label.hdr'
    t1_name = 'subject-'+str(i)+'-t1.hdr'
    t2_name = 'subject-'+str(i)+'-t2.hdr'
    t1_img = sitk.ReadImage(join(hdrpath, t1_name))
    t2_img = sitk.ReadImage(join(hdrpath, t2_name))
    label_img = sitk.ReadImage(join(hdrpath, label_name))
    t1_savename = 'iseg_' + str(i) + '_0000.nii.gz'
    t2_savename = 'iseg_' + str(i) + '_0001.nii.gz'
    label_savename = 'iseg_' + str(i) + '.nii.gz'
    sitk.WriteImage(t1_img, join(niipath, t1_savename))
    sitk.WriteImage(t2_img, join(niipath, t2_savename))
    sitk.WriteImage(label_img, join(labelpath, label_savename))


#%% validation set: convert hdr to nii
hdrpath = r'E:\Data\iSeg2019\iSeg-2019-Validation'
niipath = r'E:\Data\iSeg2019\Task07_iSeg\imagesTs'

for i in range(11, 24):
    t1_name = 'subject-'+str(i)+'-t1.hdr'
    t2_name = 'subject-'+str(i)+'-t2.hdr'
    t1_img = sitk.ReadImage(join(hdrpath, t1_name))
    t2_img = sitk.ReadImage(join(hdrpath, t2_name))

    t1_savename = 'iseg_' + str(i) + '_0000.nii.gz'
    t2_savename = 'iseg_' + str(i) + '_0001.nii.gz'

    sitk.WriteImage(t1_img, join(niipath, t1_savename))
    sitk.WriteImage(t2_img, join(niipath, t2_savename))

#%% testing set: convert hdr to nii
hdrpath = r'E:\Data\iSeg2019\iSeg-2019-Testing'
niipath = r'E:\Data\iSeg2019\iSeg-2019-Testnii'

for i in range(24, 40):
    t1_name = 'subject-'+str(i)+'-t1.hdr'
    t2_name = 'subject-'+str(i)+'-t2.hdr'
    t1_img = sitk.ReadImage(join(hdrpath, t1_name))
    t2_img = sitk.ReadImage(join(hdrpath, t2_name))

    t1_savename = 'iseg_' + str(i) + '_0000.nii.gz'
    t2_savename = 'iseg_' + str(i) + '_0001.nii.gz'

    sitk.WriteImage(t1_img, join(niipath, t1_savename))
    sitk.WriteImage(t2_img, join(niipath, t2_savename))


#%% convert nii to hdr
niipath = r'E:\Data\iSeg2019\Infer\TestHist'
hdrpath = r'E:\Data\iSeg2019\Infer\TestHisthdr'

for i in range(24, 40):
    seg_name = 'iseg_' + str(i) + '.nii.gz'
    save_name = 'subject-'+str(i)+'-label.hdr'

    seg_img = sitk.ReadImage(join(niipath, seg_name))
    sitk.WriteImage(seg_img, join(hdrpath, save_name))

