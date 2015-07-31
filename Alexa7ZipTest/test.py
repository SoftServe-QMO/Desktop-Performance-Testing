# -*- coding: UTF-8 -*-

import os
import sys
import time
from datetime import datetime
import ctypes


import subprocess
from Alexa import *

ProjectPath = os.path.dirname(os.path.realpath(__file__))
RunStartString = time.strftime("%d_%b_%Y__%H_%M_%S", time.localtime())
ExitOnError = True


def Main():
    try:
        #Insert here your test case code
        subprocess.Popen(["C:\\Program Files\\7-Zip\\7zFM.exe"])

        proxy = ctypes.cdll.LoadLibrary("c:\\PerfMonitorProxy.dll")

            #AppImage: Tools
        Tools = AppImage()
        Tools.Name = "Tools"
        Tools.Path = ProjectPath + "\\images\\Tools.png"
        Tools.Threshold = 0.003

        proxy.perfmon("ALEXA", "open_window", 50)
        performanceTools = Tools.Bind(15)
        if Tools.TimeOut is False:
            Mouse.Click(Tools.x + (Tools.Width / 2), Tools.y + (Tools.Height / 2))
        elif Tools.TimeOut is True and ExitOnError is True:
            Finish()
        #end...
            #AppImage: Benchmark
        Benchmark = AppImage()
        Benchmark.Name = "Benchmark"
        Benchmark.Path = ProjectPath + "\\images\\Benchmark.png"
        Benchmark.Threshold = 0.003
        performanceBenchmark = Benchmark.Bind(15)
        proxy.perfmon("ALEXA", "open_window", 0)

        if Benchmark.TimeOut is False:
            Mouse.Click(Benchmark.x + (Benchmark.Width / 2), Benchmark.y + (Benchmark.Height / 2))
            proxy.perfmon("ALEXA", "benchmark", 50)
        elif Benchmark.TimeOut is True and ExitOnError is True:
            Finish()
        #end...

        time.sleep(10)

            #AppImage: Stop
        Stop = AppImage()
        Stop.Name = "Stop"
        Stop.Path = ProjectPath + "\\images\\Stop.png"
        Stop.Threshold = 0.003
        proxy.perfmon("ALEXA", "benchmark", 0)
        proxy.perfmon("ALEXA", "stop_benchmark", 50)
        performanceStop = Stop.Bind(15)
        if Stop.TimeOut is False:
            Mouse.Click(Stop.x + (Stop.Width / 2), Stop.y + (Stop.Height / 2))
            proxy.perfmon("ALEXA", "stop_benchmark", 0)
        elif Stop.TimeOut is True and ExitOnError is True:
            Finish()
        #end...

            #AppImage: Cancel
        Cancel = AppImage()
        Cancel.Name = "Cancel"
        Cancel.Path = ProjectPath + "\\images\\Cancel.png"
        Cancel.Threshold = 0.003
        Cancel.Bind(15)
        if Cancel.TimeOut is False:
            Mouse.Click(Cancel.x + (Cancel.Width / 2), Cancel.y + (Cancel.Height / 2))
        elif Cancel.TimeOut is True and ExitOnError is True:
            Finish()
        #end...

        NagiosUtils.AddPerformanceData("Open Tools", performanceTools, 15, 20)
        NagiosUtils.AddPerformanceData("Open Benchmark", performanceBenchmark, 150, 200)
        NagiosUtils.AddPerformanceData("Stop Benchmark", performanceStop, 150, 200)


    except Exception, error:
        errorLine = str(sys.exc_traceback.tb_lineno)
        Finish("UNKNOWN: an exception has occurred at line " + errorLine +
        ": " + str(error), 3)


def Setup():

    Ocr.Data = "C:\\Alexa\\OcrData\\tessdata"
        #Alexa Log
    Log.DisableConsoleOutput()
    Log.Enable = True
    Log.DebugImages = True
    Log.Level = "error"
    Log.Path = "C:\\Alexa\\TestCases\\Spider\\log\\" + RunStartString
    #end...

    #Init here your Nagios Data Source


def Finish(message=None, exitcode=None):

    Log.EnableConsoleOutput()

    if message is None:
        NagiosUtils.PrintOutput()
    else:
        NagiosUtils.PrintOutput(message)

    if exitcode is None:
        sys.exit(NagiosUtils.GetExitCode())
    else:
        sys.exit(exitcode)


if __name__ == '__main__':
    try:
        Setup()
        Main()
        Finish()
    except Exception, error:
        errorLine = str(sys.exc_traceback.tb_lineno)
        Finish("UNKNOWN: an exception has occurred at line " + errorLine +
        ": " + str(error), 3)
