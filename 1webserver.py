def HostCount(fnm):
    requestCount = {}
    data = open(fnm, "r").readlines()
    #Check for IP and increment its value
    for line in data:
        lineParts = line.split(" ")
        ip = lineParts[0].strip("\"")
        if ip not in requestCount:
            requestCount[ip] = 0
        requestCount[ip] += 1
    print("Print (host, request-count) tuples for the top-10 frequent hosts :",sorted(requestCount.items(), key=lambda x: x[1], reverse=True)[0:10])
def StatusCount(fnm):
    requestCount = {}
    data = open(fnm, "r").readlines()
    # Check for Status and increment its value
    for line in data:
        lineParts = line.split(" ")
        ip = lineParts[8]
        if ip not in requestCount:
            requestCount[ip] = 0
        requestCount[ip] += 1
    print("Print (HTTP-status-code, count) tuples, sorted by count in desc :",sorted(requestCount.items(), key=lambda x: x[1], reverse=True))
def HighestReqCount(fnm):
    requestCount = {}
    data = open(fnm, "r").readlines()
    # Check for timestamp based on hour and find the Count of requests.
    for line in data:
        lineParts = line.split(" ")
        date = lineParts[3].split(":")[0].strip("'[")
        hour = lineParts[3].split(":")[1]
        datetime = date + ":" + hour
        if datetime not in requestCount:
            requestCount[datetime] = 0
        requestCount[datetime] += 1
    print("Print the hour with the highest request count, along with the count: ",sorted(requestCount.items(), key=lambda x: x[1], reverse=True)[0])
def HighestBytesTime(fnm):
    datasent = 0
    requestCount = {}
    # Check for Status "200" (successfully served) for a timestamp, increment its bytes value
    data = open(fnm, "r").readlines()
    for line in data:
        lineParts = line.split(" ")
        status = lineParts[8]
        date = lineParts[3].split(":")[0].strip("'[")
        hour = lineParts[3].split(":")[1]
        datetime = date + ":" + hour
        if datetime not in requestCount:
            requestCount[datetime] = 0
            if status == "200":
                datasent = int(lineParts[9])
        requestCount[datetime] += datasent
    print("Print the hour with the highest total number of bytes served : ",
          sorted(requestCount.items(), key=lambda x: x[1], reverse=True)[0])
def FirstLastpath(fnm):
    firstpathcount = {}
    lastpathcount = {}
    lastpathcount["NA"] = 0
    data = open(fnm, "r").readlines()
    # Check for firstpath ignoring "?"
    # Check for lastpath , replace with NA if not found
    for line in data:
        lineParts = line.split(" ")
        path = lineParts[6].split("/")
        if path[-1] == '' and len(path) == 2:
            pass
        else:
            firstpath = path[1].split("?")[0]
            lastpath = path[-1].split("?")[0]
            if firstpath not in firstpathcount:
                firstpathcount[firstpath] = 0
            firstpathcount[firstpath] += 1
            if lastpath == '':
                lastpathcount["NA"] += 1
            if firstpath != lastpath:
                if lastpath not in lastpathcount:
                    lastpathcount[lastpath] = 0
                lastpathcount[lastpath] += 1
            else:
                lastpathcount["NA"] += 1
    print("Print firstpath in frequent count:", sorted(firstpathcount.items(), key=lambda x: x[1], reverse=True)[0:10])
    print("Print lastpath in frequent count:", sorted(lastpathcount.items(), key=lambda x: x[1], reverse=True)[0:10])
def MeanMode(fnm):
    from statistics import mode
    dataset = []
    data = open(fnm, "r").readlines()
    #Mean based on timestamp
    for line in data:
        lineParts = line.split(" ")
        Header = lineParts[5].strip("\"")
        if Header == "GET":
            dataset.append(lineParts[3].strip("["))
    print("Print the mean of the distribution of number of GET params is around Timestamp: ", mode(dataset))
if __name__ == "__main__":
    fnm = "D:\Test\\apache-http-logs\w3af.txt"
    HostCount(fnm)
    StatusCount(fnm)
    HighestReqCount(fnm)
    HighestBytesTime(fnm)
    FirstLastpath(fnm)
    MeanMode(fnm)

