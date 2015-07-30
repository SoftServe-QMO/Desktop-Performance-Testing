using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length <= 1)
            {
                System.Console.WriteLine("Please enter CounterGroup and Counters");
                System.Console.WriteLine("Usage: executable <CounterGroup> <Counter1> <CounterN>");
                return;
            }

            if (args.Length == 2) {
                if (args[0].Equals("delete")) {
                    if (PerformanceCounterCategory.Exists(args[1]))
                    {
                        PerformanceCounterCategory.Delete(args[1]);
                        Console.Out.WriteLine("Deleting perfGroup: " + args[1]);                       
                    }
                    return;
                }
            }

            CounterCreationDataCollection col = new CounterCreationDataCollection();

            String metrics_name = args[0];

            for (int i = 1; i < args.Length; i++) {

                Console.Out.WriteLine("Adding counters: " + args[i]);
                CounterCreationData counter = new CounterCreationData();
                counter.CounterName = args[i];
                counter.CounterHelp = args[i];
                counter.CounterType = PerformanceCounterType.NumberOfItems32;
                col.Add(counter);
            }
            
            if (PerformanceCounterCategory.Exists(metrics_name))
            {
                PerformanceCounterCategory.Delete(metrics_name);
                Console.Out.WriteLine("Deleting perfGroup:" + metrics_name);
            }
            
            PerformanceCounterCategory category = PerformanceCounterCategory.Create(metrics_name,
            "Perf Category Description ", col);
            Console.Out.WriteLine("Creating perfGroup:" + metrics_name);
            

        }
    }
