


import sys, os
import caffe
import numpy as np
import cv2 as cv


def readfile2list(file_path):
    ret = []
    with open(file_path, 'r') as fp:
        ret = [b.strip().split(' ') for b in fp]
    return ret


def  test(img_path_list, caffe_model, deploy):
    GPU_ID = 0
    caffe.set_mode_gpu()
    caffe.set_device(GPU_ID)
    net = caffe.Net(deploy, caffe_model, caffe.TEST )
    f1 = open('pass.list', 'w')
    f2 = open('fail.list', 'w')
    f3 = open('low_prob.list', 'w')
    total, cor = 0, 0
    img_list = readfile2list(img_path_list)
    for line in img_list:
        imgpath = line[0]
        gt_label = line[1]
        img = cv.imread(imgpath, cv.IMREAD_GRAYSCALE)
        img = cv.resize(img, (32, 32))
        net.blobs['data'].data[...] = img
        out = net.forward()
        # print out['prob'].shape
        # print type(out['prob'].argmax())
        label = out['prob'].argmax()
        pp = out['prob'][0][label]
        if  pp < 0.9 :
            f3_w_str = imgpath + ' ' + str(label) + ' ' + str(pp) + '\n'
            f3.write(f3_w_str)
        total += 1
        if int(label) == int(gt_label):
            cor += 1
            f1.write(imgpath)
            f1.write('\n')
        else:
            f2.write(imgpath)
            f2.write('\n')
    print cor  / float(total)
    f1.close()
    f2.close()
    f3.close()

if __name__  == '__main__':
    img_path = 'bin_cls_test.list'
    test( img_path, sys.argv[1] , sys.argv[2] )



