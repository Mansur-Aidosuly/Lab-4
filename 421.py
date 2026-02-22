import sys

q = int(sys.stdin.readline())

for _ in range(q):
    module_path, attr = sys.stdin.readline().split()
    
    try:
        module = __import__(module_path, fromlist=["*"])
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    
    if not hasattr(module, attr):
        print("ATTRIBUTE_NOT_FOUND")
    else:
        obj = getattr(module, attr)
        if callable(obj):
            print("CALLABLE")
        else:
            print("VALUE")