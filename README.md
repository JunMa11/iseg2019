# iSeg2019 [Homepage](http://iseg2019.web.unc.edu/) & [Leaderboard](http://iseg2019.web.unc.edu/evaluation-results/)
3D U-net Baseline for iseg-2019 and An Attempt at Dealing With Multiple Sites Data via Histogram Matching

The 3D U-Net baseline is based on [nnU-Net](https://github.com/MIC-DKFZ/nnUNet).

## Requirement
- [Pytorch](https://pytorch.org/get-started/locally/) version >=1.0.1
- [nnU-Net](https://github.com/MIC-DKFZ/nnUNet)
  - `git clone https://github.com/MIC-DKFZ/nnUNet.git`
  - `cd nnUNet`
  - Install with `pip install -r requirements.txt` followed by `pip install -e .`
- Set `paths.py`
  - mkdir `mydata_folder` (mydata_folder should be located in the same path with `paths.py`) 
  - [line 35](https://github.com/MIC-DKFZ/nnUNet/blob/f0276df1786a9b4f8e7722152e601dfa542df07f/nnunet/paths.py#L35): `base = "path to/mydata_folder"`
  - [line 51](https://github.com/MIC-DKFZ/nnUNet/blob/f0276df1786a9b4f8e7722152e601dfa542df07f/nnunet/paths.py#L51): `preprocessing_output_dir = "path to/mydata_folder/pre_data"`
  - [line 60](https://github.com/MIC-DKFZ/nnUNet/blob/f0276df1786a9b4f8e7722152e601dfa542df07f/nnunet/paths.py#L60): `network_training_output_dir = os.path.join(base, my_output_identifier)`

> Please strictly follow this path setting guidance unless you know what you are changing!

## Preprocessing: convert and rename hdr files to nii files by hdr2nii 
The finally folder structure should be 
- `Task07_iSeg`
  - imagesTr (file names shoud be `iseg_1_0000.nii.gz`, `iseg_1_0001.nii.gz`, ..., `iseg_10_0000.nii.gz`, `iseg_10_0001.nii.gz`)
  - labelsTr (file names shoud be `iseg_1.nii.gz`, ..., `iseg_10.nii.gz`)
  - imagesVal (file names shoud be `iseg_11_0000.nii.gz`, `iseg_11_0001.nii.gz`, ..., `iseg_23_0000.nii.gz`, `iseg_23_0001.nii.gz`)
  - imagesTs (file names shoud be `iseg_24_0000.nii.gz`, `iseg_24_0001.nii.gz`, ..., `iseg_39_0000.nii.gz`, `iseg_39_0001.nii.gz`)

Then, Put the above `Task07_iSeg` folder into `path to/mydata_folder/nnUNet_raw_splitted`

## Testing
- Downloda the pre-trained model and put it in the nnU-Net's model folder `mydata_folder/nnUNet/3d_fullres/Task07_iSeg`. Download: [BaiduNetDisk](https://pan.baidu.com/s/1Km0vqM3sDrA4z71Z7zs2HQ) pw:xyhu
- Inference validation set: Run `python inference/predict_simple.py -i path to/imagesVal -o OUTPUT_FOLDER -t Task07_iSeg -tr nnUNetTrainer -m 3d_fullres -f all`
- Inference testing set: Run `python inference/predict_simple.py -i path to/imagesTs -o OUTPUT_FOLDER -t Task07_iSeg -tr nnUNetTrainer -m 3d_fullres -f all`


## Histogram matching
- Generate histogram matching results by running `HistogramMatch.py`
- Inference histogram matching results: Run `python inference/predict_simple.py -i path to/imagesTsHist -o OUTPUT_FOLDER -t Task07_iSeg -tr nnUNetTrainer -m 3d_fullres -f all`

## Results
- 3D U-Net is a strong baseline!
- The performance has significantly drop on new sites dataset.

![Results on Leardboard](https://github.com/JunMa11/iseg2019/blob/master/iSegResults/Rank.PNG)

## Re-train the model on TitanXP GPU
I use all the training cases during training. 
- Put the `dataset.json` into `path to/mydata_folder/nnUNet_raw_splitted/Task07_iSeg`
- Run `python experiment_planning/plan_and_preprocess_task.py -t Task07_iSeg -pf 10`
- Run `python run/run_training.py 3d_fullres nnUNetTrainer Task07_iSeg all --ndet`.

> All the `python` command should be run in `path to nnUNet/nnunet` (the same path to `paths.py` file).
