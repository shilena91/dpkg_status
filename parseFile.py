def validateLine(line, row):
    index = line.find(':')
    if index <= 0:
        return False
    if ' ' in line[:index]:
        return False
    return True

def splitValues(pkgContainer, key, delimeter):
    if key not in pkgContainer: return

    if delimeter == ', ':
        array = pkgContainer[key].split(delimeter)
        pkgContainer[key] = array
    elif delimeter == ' | ':
        result = []
        for e in pkgContainer[key]:
            result.append(e.split(delimeter))
        pkgContainer[key] = result

def getReverseDepends(pkgArray):
    for pkg in pkgArray:
        revDepends = []
        for otherPkg in pkgArray:
            if 'Depends' not in otherPkg: continue
            for depends in otherPkg['Depends']:
                for dependItem in depends:
                    length = dependItem.find(' (')
                    if length == -1:
                        length = len(dependItem)
                    if pkg['Package'] == dependItem[:length]:
                        revDepends.append(otherPkg['Package'])
        pkg['Reverse_Depends'] = revDepends if len(revDepends) > 0 else None

def parseFile(file):
    row = 0
    value = ''
    key = ''
    pkgJson = []

    for pkg in file.split('\n\n'):
        if pkg == '':
            continue
        pkgContainer = {}
        for line in pkg.split('\n'):
            row += 1
            if not validateLine(line, row):
                if key == '': continue
                value = value + '\n' + line
                pkgContainer[key] = value
            else:
                key = line[:line.find(':')]
                value = line[line.find(':') + 1:len(line)].strip()
                pkgContainer[key] = value
        
        splitValues(pkgContainer, 'Depends', ', ')
        splitValues(pkgContainer, 'Depends', ' | ')
        pkgJson.append(pkgContainer)
        row += 1
    return pkgJson
