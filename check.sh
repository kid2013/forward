#!/bin/bash

# echo $1
python forward_test.py $1 $2

sed -n '/_1.jpg/p' fail.list > false_neg.list
sed -n '/_0.jpg/p' fail.list > false_pos.list
sed -n '/_1.jpg/p' pass.list > true_pos.list
sed -n '/_0.jpg/p' pass.list > true_neg.list

rm -fr false_neg false_pos true_pos true_neg
mkdir false_neg false_pos true_pos true_neg

cat false_neg.list | xargs cp -t false_neg
cat false_pos.list | xargs cp -t false_pos
cat true_pos.list | xargs cp -t true_pos
cat true_neg.list | xargs cp -t true_neg

cat pass.list | xargs eog --name="pass" &
cat fail.list | xargs eog --name="fail" &
awk '{print $1}' low_prob.list | xargs eog --name="low_prob" &
cat low_prob.list
wait

