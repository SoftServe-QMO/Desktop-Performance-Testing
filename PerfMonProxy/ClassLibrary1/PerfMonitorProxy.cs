using RGiesecke.DllExport;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;



class PerfMonitorProxy
{
    [DllExport("perfmon", CallingConvention = CallingConvention.Cdecl)]
    public static int TestExport(String counterGroup, String counterSet, int value)
    {
        System.Console.Out.WriteLine(String.Format("Setting counter {0} for group {1} with value {2}", counterSet, counterGroup, value));


        // get an instance of our perf counter
        PerformanceCounter counter = new PerformanceCounter();
        counter.CategoryName = counterGroup;
        counter.CounterName = counterSet;
        counter.ReadOnly = false;
        counter.RawValue = value;            
        
        counter.Close();
        return 0;
    }
}