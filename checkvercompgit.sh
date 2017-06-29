rm git_status.out
rm git_diff.out
rm vercomment.txt
rm version.txt

git log -1 --pretty=format:"%h: %s%n" > vercomment.txt
git log -1 --pretty=format:"%H%n" > version.txt
# MYVAR=$(git log -1 --pretty=format:"%h: %s%n")
# echo $MYVAR

MYTEST=$(hg status)
# echo $MYTEST
if [ -n "$MYTEST" ]; then git status > git_status.out; fi
if [ -n "$MYTEST" ]; then git diff > git_diff.out; fi

nrnivmodl
