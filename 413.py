import json
import sys
import re

def resolve_query(data, query):
    tokens = re.findall(r'[a-zA-Z_]\w*|\[\d+\]', query)
    current = data

    for token in tokens:
        if token.startswith('['):
            index = int(token[1:-1])
            if isinstance(current, list) and 0 <= index < len(current):
                current = current[index]
            else:
                return "NOT_FOUND"
        else:
            if isinstance(current, dict) and token in current:
                current = current[token]
            else:
                return "NOT_FOUND"

    return json.dumps(current, separators=(',', ':'))

data = json.loads(sys.stdin.readline())
q = int(sys.stdin.readline())

for _ in range(q):
    query = sys.stdin.readline().strip()
    result = resolve_query(data, query)
    print(result)