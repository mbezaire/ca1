rm hg_status.out
rm hg_diff.out
rm vercomment.txt
rm version.txt

hg parent --template '{rev}: {desc}\n' > vercomment.txt
hg parent --template '{node}\n' > version.txt
# MYVAR=$(hg parent --template '{rev}: {desc}\n')
# echo $MYVAR

MYTEST=$(hg status)
# echo $MYTEST
if [ -n "$MYTEST" ]; then hg status > hg_status.out; fi
if [ -n "$MYTEST" ]; then hg diff > hg_diff.out; fi

nrnivmodl
