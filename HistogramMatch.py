#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:26:41 2019

@author: Jun
"""

import os
import nibabel as nb
from skimage.transform import match_histograms
join = os.path.join

img_path = 'path_to/nnUNet/nnunet/mydata_folder/nnUNet_raw_splitted/Task07_iSeg/imagesTs'
ref_img = 'path_to/nnUNet/nnunet/mydata_folder/nnUNet_raw_splitted/Task07_iSeg/imagesVal/iseg_13_0001.nii.gz'
save_path = 'path_to/nnUNet/nnunet/mydata_folder/nnUNet_raw_splitted/Task07_iSeg/imagesTsHist'

filenames = os.listdir(img_path)
filenames.sort()

for img_name in filenames: 
    img_nii = nb.load(join(img_path, img_name))
    img_data = img_nii.get_data()
    ref_data = nb.load(ref_img).get_data()
    
    img_histmatch = match_histograms(img_data[img_data!=0], ref_data[ref_data!=0], multichannel=False)
    save_img = img_data.copy()
    save_img[img_data!=0] = img_histmatch
    img_hist_nii = nb.Nifti1Image(save_img, img_nii.affine, img_nii.header)
    nb.save(img_hist_nii, join(save_path, img_name))
