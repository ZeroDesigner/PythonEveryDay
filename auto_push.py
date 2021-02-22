import os,time
def job(dir):
    curtime = time.ctime()
    os.chdir(dir)
    os.system('git add .')
    com_line='git commit -m \'%s\''%(curtime)
    os.system(com_line)
    os.system('git push -u origin master')
    return
while True:
    job('./')
    time.sleep(600)
