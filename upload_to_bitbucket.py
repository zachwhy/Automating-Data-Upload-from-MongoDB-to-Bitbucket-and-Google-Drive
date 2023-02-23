from git import Repo
from datetime import date


PATH_OF_GIT_REPO = "/home/yncalab/curate_data/plonline_data"   # make sure .git folder is properly configured
COMMIT_MESSAGE = 'sent from pythonanywhere'

current = str(date.today())

name = "pldata_" + current + ".csv"

repo = Repo(PATH_OF_GIT_REPO)

# repo.git.pull()

repo.index.add([name])

repo.index.commit(COMMIT_MESSAGE)

print("sending from online python anywhere")

origin = repo.remote('origin')
origin.push()

# origin.pull()

print ("done")

