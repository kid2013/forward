#!/bin/bash

prefix=/home/username/ocr8100/model/snap_shot
deploy_prefix=/home/username/forward/deploy/ocr8100/deploy
img_list=img_file/180709_alnum_test.list
for  i in $(seq 7 1 8)
do
    modelfolder=$prefix$i
    for model in $(ls $modelfolder/*.caffemodel)
    do
        if [ $i -ge 7  ] && [ $i -le 8 ]
        then
            deploy=${deploy_prefix}62.prototxt
        else
            deploy=${deploy_prefix}8100.prototxt
        fi
        python forward_test_ocr8100.py  $img_list  tmp $model  $deploy    1  $i.list  
    done
done





