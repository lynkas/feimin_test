import json,os
answer_str = "answer"
fileList = os.listdir(answer_str)

for filename in fileList:
    with open(os.path.join(answer_str,filename)) as answerFile:
        with open(filename) as resultFile:
            answer = json.loads(answerFile.read())
            result = json.loads(resultFile.read())
            print(filename)
            assert answer==result
            print("OK")
