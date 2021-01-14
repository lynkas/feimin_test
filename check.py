import json
import os

answer_str = "answer"
fileList = os.listdir(answer_str)
ok = True
for filename in fileList:
    # fuck you, apple
    if filename==".DS_store": continue
    with open(os.path.join(answer_str,filename)) as answerFile:
        with open(filename) as resultFile:
            answer = json.loads(answerFile.read())
            result = json.loads(resultFile.read())
            if answer!=result:
                print(filename+" is not same as provided.")
                ok=False

if ok: print("ok, all the same")