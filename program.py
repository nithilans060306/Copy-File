with open("text1.txt","r") as fp:
    msg1=fp.read()
    with open("copytxt","w") as fp1:
        fp1.write(msg1)