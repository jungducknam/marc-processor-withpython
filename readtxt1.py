print("marc 처리기")
print("\nNAM JUNG DUCK.2020-01-08")

add = input("파일의 이름을 써주세요(파일은 sample폴더안에 들어 있어야 합니다.) : ")

add = "./sample/"+add

marc = open(add,'r', encoding='UTF-8')
data=marc.read()
print("\n","=="*40, "\n")
#==============================================================
text=data

reader = text[0:24] #리더

finddir = text.index("")

dir = text[24:int(finddir)] #디렉토리 전반

length=12
cutdir=[''.join(x) for x in zip(*[list(dir[z::length]) for z in range(length)])] #디렉토리 부분 12자리씩 끊어 리스트로 저장

varfie=text[int(finddir):].encode('UTF-8') #가변필드. UTF-8형식으로 한글이 인코딩되어있어서, 필드 주소가 안맞았던 거임. 그래서 UTF-8로 인코딩하고 다시 디코딩 하는 과정이 필요!

#===============================================================

taglist=[] #태그 함수를 저장할 리스트 선언
lenlist=[] #필드 길이부분을 저장할 리스트
stalist=[] #필드 시작부분을 저장할 리스트
outdata='' #출력을 대비한 변수 선언

i=0
while i < len(cutdir):
    cutdir2 = cutdir[i] #자른 디렉터리 리스트를 차례대로 출

    tag1=cutdir2[:3]            #리스트에서 태그자른거
    fielen=int(cutdir2[3:7])    #길이부분1.text
    fiesta=int(cutdir2[7:12])   #시작부분

    taglist.append(tag1)        #리스트에 따로저장
    lenlist.append(int(fielen))
    stalist.append(int(fiesta))
    i+=1
#===============================================================
choice=input("해당 marc데이터 전체를 보시겠습니까?(숫자 1 입력)\n특정한 TAG의 데이터를 보시겠습니까?(숫자 2 입력)\n번호를 선택해주세요 : ")
print("\n","=="*40, "\n")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%분기시작
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if choice == '1':
    i=0
    A=taglist
    B=stalist
    C=lenlist
    while i < len(A):
        if int(A[i])<=8:
            print(A[i]+'\t   '+varfie[int(B[i]):int(C[i])+int(B[i])].decode('UTF-8'))#태그+필드내용 츨력문(008이하태그 적용)
            outdata=outdata+A[i]+'\t   '+varfie[int(B[i]):int(C[i])+int(B[i])].decode('UTF-8')+'\n'
        else:
            print(A[i]+'\t'+varfie[int(B[i]):int(C[i])+int(B[i])].decode('UTF-8'))#태그+지시기호+필드내용 츨력문
            outdata=outdata+A[i]+'\t'+varfie[int(B[i]):int(C[i])+int(stalist[i])].decode('UTF-8')+'\n'
        i+=1

    print("\n","=="*40, "\n")
    #===============================================================

    output = input("\n파일을 출력하시겠습니까? (y/n) : ")
    if output=="y":
        print("Thanks")
        print("\n","=="*40, "\n")
        import sys
        sys.stdout = open('./marc_data/output.txt','w', encoding='UTF-8')
        print(outdata)
    else:
        print("bye")
        print("\n","=="*40, "\n")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
else:
    while True:
        print("\n","=="*40, "\n")
        print("TAG")
        i=0
        while i < len(taglist):
            print(taglist[i])
            i+=1

        print("\n","=="*40, "\n")
        choicetag=input("위의 리스트를 참조하시고, 보시고 싶은 TAG의 번호를 입력해주세요 : ")
        if choicetag in taglist:
            findtag = taglist.index(choicetag)
            print("\n","=="*40, "\n")
            a=(taglist[findtag]+'\t'+varfie[int(stalist[findtag]):int(lenlist[findtag])+int(stalist[findtag])].decode('UTF-8'))
            b=a[7:]
            b=b.split("")
            print(b)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            if choicetag == '020':
                if b
                print(taglist[findtag])
                print('ISBN : ' + b[1])
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            print("\n","=="*40, "\n")
        else:
            print("해당태그는 이 파일에 존재하지 않습니다. 다른 태그를 입력해주세요")

        con = input("다른 태그도 찾아보실건가요??(y=계속탐색, n=종료) : ")
        if con == "y":
            continue
        else:
            break
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
