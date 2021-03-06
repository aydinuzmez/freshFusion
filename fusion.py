#is being programmed by Aydin Uzmez

import subprocess
import os
import time


FUSION7PATH = r"T:\DEV\cgru\cgru_windows\software_setup\start_fusion.cmd"
RENDERNODEPATH= r"T:\DEV\fusion\DEV\Deployments\freshFusion\rendernode\FusionRenderNode.exe"

class Task(object):
    def __init__(self):
        self.color()
        self.pid = None
        self.__appname = "FusionRenderNode.exe"
        self.sp= None

    def __List(self):
        tempCmd = "tasklist /nh /fi \"imagename eq "+ self.__appname+"\""
        try:
            return subprocess.Popen(tempCmd,stdout=subprocess.PIPE,shell=True).communicate()
        except:
            return None

    def Kill(self):
        pid = self.GetPid()
        if pid is None:
            return None
        else:
            print(str(pid) +" PID was Terminated.")
            tempCmd = "taskkill /PID "+str(pid)+" /F"
            return subprocess.Popen(tempCmd,stdout=subprocess.PIPE,shell=True)

    def GetPid(self):
        try:
            pid = self.__List()[0].split()[1]
            return int(pid)
        except:
            return None

    def run(self,appname):
        if(appname == "FUSION7"):
            return subprocess.Popen([FUSION7PATH])
        if(appname =="RENDERNODE"):
            return subprocess.Popen("start /AFFINITY 0xFFA "+RENDERNODEPATH,stdout=subprocess.PIPE,shell=True) #10 Core


    def title(self,title):
        return subprocess.Popen("title "+title,shell=True)
    def color(self):
        return subprocess.Popen("color A",shell=True)

task1 = Task()
task1.title("Fresh Fusion is being started... Let's Party")
task1.Kill()
task1.run("FUSION7")
time.sleep(15)
task1.run("RENDERNODE")
task1.title("Fresh Fusion was started.")