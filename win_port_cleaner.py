import os
import re

'''
功能：python实现杀掉指定端口
win10系统环境下
python版本：3.6
'''


def kill_port(port):
    # 查找端口的pid
    find_port = 'netstat -aon | findstr %s' % port
    result = os.popen(find_port)
    text = result.read()
    pid = re.findall("LISTENING\s+([\s\S+]*?)\s+", text)
    if pid:
        # 占用端口的pid
        find_kill = 'taskkill -f -pid %s' % pid[0]
        print(find_kill)
        result = os.popen(find_kill)
        print(result.read())


if __name__ == "__main__":
    for i in range(10000, 10021):
        kill_port(i)