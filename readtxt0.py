print("marc 처리기")
print("\nNAM JUNG DUCK.2020-01-07")
add = input("\n 파일의 이름을 써주세요(파일은 sample폴더안에 들어 있어야 합니다.) : ")
add = "./sample/"+add
marc = open(add,'r', encoding='UTF-8')
data=marc.read() #텍스트 파일 불러오기
print("\n","=="*40, "\n")
#==============================================================
text=data

reader = text[0:24] #리더부분

finddir = text.index("")
dir = text[24:int(finddir)] #디렉토리 부분

length=12
cutdir=[''.join(x) for x in zip(*[list(dir[z::length]) for z in range(length)])]
#디렉토리 부분 12자리씩 끊어 리스트로 저장

varfie=text[int(finddir):] #가변필드 부분

varfie=varfie.replace("", "\n").replace("", "$")
#print(varfie)
varfie=varfie.split("\n") #가변필드의 특수문자를 치환하고 리스트로 저장

#===============================================================
#디렉토리를 3,4,5 자리로 나눠서 각각 다른 변수로 저장.
#===============================================================
print("TAG.....12F.................................")
taglist=[]
i=0
while i < len(cutdir):
    cutdir2 = cutdir[i]
    tag2=cutdir2[0:3]
    #fielen=int(cutdir2[3:7])
    #fiesta=int(cutdir2[7:12])
    taglist.append(tag2)
    i+=1

i=0
outdata='' #텍스트 따로 출력 할때 텍스트를 저장할 변수
for i, name in enumerate(taglist):
    if int(taglist[i])<=8:
        print(taglist[i]+"\t  "+varfie[i+1]) #태그가 008이하일 경우 띄어쓰기 7칸(지시기호 없음)
        outdata = outdata+(taglist[i]+"\t  "+varfie[i+1]+"\n")
    else:
        print(taglist[i]+"\t"+varfie[i+1]) # 그 외에 경우 4칸 (지시기호 있음)
        outdata = outdata+(taglist[i]+'\t'+varfie[i+1]+"\n")
    i += 1
print("\n","=="*40, "\n")

output = input("\n파일을 출력하시겠습니까? (y/n) : ")
if output==("y" or "Y"):
    import sys
    sys.stdout = open('./marc_data/output.txt','w', encoding='UTF-8')
    print(outdata)
    print("Thanks")
else:
    print("bye")
