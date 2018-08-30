
rm -fr  pos_img
mkdir  pos_img
flag="test"

for  i in `seq  1000`
do
    cp /ssd/wanwuming/narrow/$flag/$i/$flag_*_1_*.jpg pos_img
done
# cp /ssd/wanwuming/narrow/neg/$flag/$flag_0_0_*0*.jpg  neg_img

ls -l neg_img | awk '{print $9}' > neg.list
ls -l pos_img | awk '{print $9}' > pos.list

sed -i '1,2d' *.list
sed -i "s!$flag!$HOME/forward/neg_img/$flag!" neg.list
sed -i "s!$flag!$HOME/forward/pos_img/$flag!" pos.list
