import os
import gdown
import shutil

dir_now = os.getcwd()
urls = ['https://drive.google.com/open?id=1EEQI50BoCvGy0ZE4ufNrS7CRj7FqXzL_&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1qDAkk5UEKzRPSBeePVmtKQDtsCqpXBYh&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1nNVj-Af_miAKvNpxVn6Dw8gLsS-5HD7q&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1mXWiD_1m9RW-9AMOVujjSBq8Zfi22r0k&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1KgzkK3JDPA4r0TMRi5h0YI9QAMcfETUy&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1605Nda5nW3AGzkpiiu5Pp6Tlft4K62h-&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1HCuvLBKdBMKm0h1DV0Tnil739UgUfr9Z&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=19W6ujJQNwqtfA8t1ur_VDI_Fbih8YnV1&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1cMwD4at8LJhri6aBH8trh7EQVgXV0J4e&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1_8k75kHH3FakiubJOhpa8g_a2F8ogAi3&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1avIG1jX69xqgjypnFtWcwInYfxVJDJ3_&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1Ha7plhzhYjVhY0COHlUuLQA3gZRLnAsr&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1cMwEgLm86VTV-9OQD_giikIs9b-rmVrb&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1iC5dyIpZXR9KH3yNonGvNU_4mb20OReD&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1EadR2vKDWPCjNLM0REKBYoceYaCtGR7T&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1pkT96E1WF9bwHSB1mMHPEEqggfx5qA0L&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1hF783AHMaOS7A-IbkYctDq-kKGRXH2sx&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1wxBA7G8El0Je6sK1e9B65uU8PL2jHNPG&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1W74EQd9dZmlYHuEuUIIFPtQAEBwEGhfK&authuser=0&usp=drive_link',
       'https://drive.google.com/open?id=1y1sJ8AQdgsV1tSRa51fcn_xniUbGaApJ&authuser=0&usp=drive_link']

outputs = ['01_x_Train.h5', '02_x_Train.h5', '03_x_Train.h5', '04_x_Train.h5', '05_x_Train.h5',
          '06_x_Train.h5', '07_x_Train.h5', '08_x_Train.h5', '09_x_Train.h5', '10_x_Train.h5',
          '01_x_Test.h5', '02_x_Test.h5', '03_x_Test.h5', '04_x_Test.h5', '05_x_Test.h5',
          '06_x_Test.h5', '07_x_Test.h5', '08_x_Test.h5', '09_x_Test.h5', '10_x_Test.h5']


def Download_wo_tex_ptb(file_list):
    """
    file_list : python list 
    list of 0-19
    0-9    : Texture-free perturbed Training dataset h5 files [01-10]
    10-19  : Texture-free perturbed Test dataset h5 files [01-10]
    
    ex)
    Download_wo_tex_ptb([10])
    Texture_free_perturbed Test dataset 01 downloaded
    
    Download_wo_tex_ptb(range(0,20))
    
    """
    
    if "datasets" not in os.listdir(dir_now):
        os.mkdirs(dir_now + "/datasets")

    if "wo_tex_ptb" not in os.listdir(dir_now+ "/datasets"):
        os.mkdir(dir_now + "/datasets/wo_tex_ptb")
    
    for i in file_list:
        url = urls[i]
        output = outputs[i]
        if output not in os.listdir(dir_now + "/datasets/wo_tex_ptb"):
            gdown.download(url, output, quiet=True, fuzzy =True)
            shutil.move(dir_now + "/" + output, dir_now + "/datasets/wo_tex_ptb")
            
def Download_Ex_dataset_2():
    url = "https://drive.google.com/file/d/1esaWNtf0tZoak7qbhAQMDpZi7u8qo4d2/view?usp=sharing"
    output = "Ex_dataset_2.csv"
    if "datasets" not in os.listdir(dir_now):
        os.mkdirs(dir_now + "/datasets") 
        
    if "Ex_dataset_2" not in os.listdir(dir_now+ "/datasets"):
        os.mkdir(dir_now + "/datasets/Ex_dataset_2")
        
    if output not in os.listdir(dir_now + "/datasets/Ex_dataset_2"):
        gdown.download(url, output, quiet=True, fuzzy =True)
        shutil.move(dir_now + "/" + output, dir_now + "/datasets/Ex_dataset_2")
    