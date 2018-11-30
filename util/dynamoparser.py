

# Parse Dynamodb Return
def parse(items):
    ret = {}
    for key in items:
        if('BOOL' in items[key]):
            ret[key] = items[key]['BOOL']
            continue
        if('S' in items[key]):
            ret[key] = items[key]['S']
            continue
        if('N' in items[key]):
            ret[key] = items[key]['N']
            continue
        if('B' in items[key]):
            ret[key] = items[key]['B']
            continue
       
    return ret




