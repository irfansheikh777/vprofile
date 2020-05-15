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

print  (master.commit.message) 
print (git_commitid)
print str(timestamp)
 

