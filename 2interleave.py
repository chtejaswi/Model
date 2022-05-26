# Please enter the files dynamically
filenames = ['D:\Test\\apache-http-logs\\a.txt', 'D:\Test\\apache-http-logs\\b.txt', 'D:\Test\\apache-http-logs\\c.txt']
#Final output list contents
Output = []
g = globals()
#Number of interleaveline required
NumberofConsecutiveLines = 3
#Reading dynamically content in all files and generating dummy lists with no blank lines
for item in range(len(filenames)):
    with open(filenames[item]) as f_in:
        g['depth_{0}'.format(item)] = (line.rstrip() for line in f_in)
        g['depth_{0}'.format(item)] = list(line for line in g['depth_{0}'.format(item)] if line)
minlen = []
Count =0
# Checking the Contents length in a file
for i in range(len(filenames)):
    minlen.append(len(g['depth_{0}'.format(i)]))
Repeat = sorted(minlen)[0]
#Create Output list from the input lists based on interleave
while(Count != Repeat):
    for _ in range(len(filenames)):
            Output.extend(g['depth_{0}'.format(_)][Count: Count + NumberofConsecutiveLines])
    Count += NumberofConsecutiveLines
#Writing to Output text file
with open('D:\Test\\apache-http-logs\\Output.txt', 'w') as f:
    for item in Output:
        f.write("%s\n" % item)
