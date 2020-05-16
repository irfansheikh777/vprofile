#!/usr/bin/env python

from git import *
import git
import subprocess
import datetime
import sys

repo = git.Repo("/opt/vprofile")
o = repo.remotes.origin
o.pull()
master = repo.head.reference
#####Variables############
timestamp = datetime.datetime.fromtimestamp(master.commit.committed_date)
git_commitid = str(master.commit.hexsha)

file = open("file.txt", "w")
file.write(git_commitid)
file.close()


f1 = open("file.txt")
f2 = open("constant.txt")
# Read the first line from the files
f1_line = f1.readline()
f2_line = f2.readline()

if f1_line != f2_line:
    print("MISMATCHED!  Hey There seems to be new commit")
    file = open("constant.txt", "w")
    file.write(git_commitid)
    file.close()
    print(git_commitid)
else:
    print("There  is no new commit")






