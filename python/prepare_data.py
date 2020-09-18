import pandas as pd
import random
import os
from shutil import copyfile
import numpy as np
import logging


def prepare_data(data, train):
    count = 0
    for i in range(data.shape[0]):
        try:
            png_file = data.filename[data.index[i]].split('.')[0] + '.png'
            src_path = os.path.join("images/", png_file)
            des_file = str(data.index[i]) + '_' + data.category[data.index[i]] + '.png'
            if train:
                dst_path = os.path.join("train/", des_file)
                copyfile(src_path, dst_path)
            else:
                dst_path = os.path.join("test/", des_file)
                copyfile(src_path, dst_path)
        except:
            count += 1
            continue
    logging.info('{} out of {} files does not exist their sepctrograms'.format(count, data.shape[0]))


def write_label(data):
    data = pd.read_csv(data_file)
    unique_labels = np.unique(data.category)
    f = open('labels.txt', 'a')
    f.writelines("{}\n".format(label for label in unique_labels))
    f.close()


def main(data_file):
    random.seed(20)
    data = pd.read_csv(data_file)
    write_label(data)
    msk = np.random.rand(len(data)) < 0.8
    train = data[msk]
    test = data[~msk]
    prepare_data(train, True)
    prepare_data(test, False)


if __name__ == "__main__":
    data_file = "meta/esc50.csv"
    main(data_file)
