# -*- coding: UTF-8 -*-

import sys, getopt
# task
from task import output_weekly_report
# model
from lattice_model import forbidden,exclamation,smile

task_map = {
    "output_weekly_report": output_weekly_report.output_weekly_report
}

model_map = {
    "forbidden": forbidden.forbidden,
    "exclamation": exclamation.exclamation,
    "smile": smile.smile
}

def main(argv):
    task_name = ''
    model_name = ''
    whether_voice = False
    try:
        opts, args = getopt.getopt(argv,"ht:m:v:",["task=","model=","voice="])
    except getopt.GetoptError:
        print("test.py -t <taskName> -m <modelName> -v <voice>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("test.py -t <taskName> -m <modelName> -v <voice>")
            sys.exit()
        elif opt in ("-t", "--task"):
            task_name = arg
        elif opt in ("-m", "--model"):
            model_name = arg
        elif opt in ("-v", "--voice"):
            if arg == "true":
                whether_voice = True
    print("use task:", task_name)
    print("use model:", model_name)
    print("voice status:", whether_voice)
    from task import strip_instance
    strip = strip_instance.getStripInstance()
    task_map[task_name](model_map[model_name](strip),strip,whether_voice)


if __name__ == "__main__":
    main(sys.argv[1:])