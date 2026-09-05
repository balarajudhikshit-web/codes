words=input().split()
maxwidth=int(input())
current_line=[]
current_width=0
lines=[]

for word in words:
    if current_width+len(word)+len(current_line)> maxwidth:
        lines+=[current_line]
        current_line=[]
        current_width=0
    current_line+=[word]
    current_width+=len(word)
if len(current_line)>0:
    lines+=[current_line]
result=[]

for i in range(len(lines)):
    line=lines[i]
    total_length=0
    for word in line:
        total_length+=len(word)
    spaces_needed=maxwidth-total_length
    
    if i==len(lines)-1:
        formatted_line=""
        for j in range(len(line)):
            if j>0:
                formatted_line+=" "
            formatted_line+=line[j]
        while len(formatted_line)<maxwidth:
            formatted_line+=" "
        result+=[formatted_line]
    else:
        if len(line)==1:
            formatted_line=line[0]
            while len(formatted_line)<maxwidth:
                formatted_line+=" "
            result+=[formatted_line]
        else:
            spaces_between_words=spaces_needed//(len(line)-1)
            extra_spaces=spaces_needed%(len(line)-1)
            formatted_line=""
            for j in range(len(line)-1):
                formatted_line+=line[j]
                if j<extra_spaces:
                    formatted_line+=" "*(spaces_between_words+1)
                else:
                    formatted_line+=" "*spaces_between_words
            formatted_line+=line[-1]
            result+=[formatted_line]
for formatted_line in result:
    print(formatted_line)