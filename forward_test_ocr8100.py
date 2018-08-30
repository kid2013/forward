


import sys, os
import caffe
import numpy as np
import cv2 as cv
import pdb


def readfile2list(file_path):
    ret = []
    with open(file_path, 'r') as fp:
        ret = [b.strip().split(' ') for b in fp]
    return ret


def  test(img_file, res_file, caffe_model, deploy_file, flag, save_file):
    GPU_ID = 1
    caffe.set_mode_gpu()
    caffe.set_device(GPU_ID)
    net = caffe.Net(deploy_file, caffe_model, caffe.TEST )
    img_path_list = readfile2list(img_file)
    total = len(img_path_list)
    resf = open(res_file, 'w')
    # pdb.set_trace()
    fa = open(save_file, 'w')
    corr = 0
    for idx, ipath in enumerate(img_path_list):
            img = cv.imread(ipath[0], cv.IMREAD_GRAYSCALE)
            label_t = int(ipath[1])
            if flag == 0 :
                [x1, y1, x2, y2] = [int(cood) for cood in ipath[2:]]
                img = img[y1:y2, x1:x2]
            img = cv.resize(img, (32, 32))
            net.blobs['data'].data[...] = img
            out = net.forward()
            label = out['prob'].argmax()
            if label == label_t :
                corr += 1
            #else :
            #    print ipath[0]
            write_str = ipath[0] + ' ' + str(label_t) + ' '  + str(label) + '\n'
            resf.write(write_str)
    # print float(corr) / total
    acc = float(corr) / total
    print acc
    write_str = caffe_model + ' ' + str(acc) + '\n'
    fa.write(write_str)
    fa.close()
    resf.close()


if __name__  == '__main__':
    test(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])



