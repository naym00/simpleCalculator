# 0 means float
# 1 means int

def checkIntOrFloat(x):
    if int(float(x)) == float(x):
        return 1
    else:
        return 0
