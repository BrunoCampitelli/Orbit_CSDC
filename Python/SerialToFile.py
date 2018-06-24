#w=label
# b=binary/hex (writes both)
# d=done

import serial

memfile="serout.txt" #change the file being used here
#st = serial.Serial('COM3',115200, timeout=None,parity=serial.PARITY_NONE, rtscts=0)
st = serial.Serial('COM3',115200, timeout=None,parity=serial.PARITY_NONE, rtscts=0)
open(memfile, 'w').close()
txtmem=open(memfile,"w")
# print("preparing to read file")
# open(memfile, 'r').close()
# rom=open(memfile,"r")
# memory=list(rom.read())
# rom.close()
# print("file read")

hexout=[]
binout=[]


while 1:
    print("waiting for command")
    st.reset_input_buffer()
<<<<<<< HEAD
    size=ord(st.read(1))#wait for command
    print(size)
    ser=st.read(size)
    ser=list(ser)

    for n in range(0,size):
        ser[n]=ord(ser[n])
        hexout[n]=hex(ser[n])
        binout[n]='{0:08b}'.format(ser[n])
    
    hexoutf=' '.join(hexout)#hex out
    binoutf=' '.join(binout)#binary out
    binoutns=''.join(binout)#binary no space
    open(memfile, 'w').close()
    txtmem=open(memfile,"w")
    txtmem.write(hexoutf)
    txtmem.write('\n')
    txtmem.write(binoutf)
    txtmem.write('\n')
    txtmem.write(binoutns)
    txtmem.close()
=======
    cmd=st.read(1)

    if(cmd=='w'):
        print("write received")
        size=st.read(2)
        size=ord(size[0])*256+ord(size[1])
        print(size)
        cmd=st.read(size)
        print(cmd)
        
        txtmem.write(cmd)
        txtmem.write('\n')

    elif(cmd=='b'):
        print("binary received")
        size=st.read(2)#wait for command
        size=ord(size[0])*256+ord(size[1])
        print(size)
        ser=st.read(size)
        ser=list(ser)
        for n in range(0,size):
            hexout.append('')
            binout.append('')

        for n in range(0,size):
            ser[n]=ord(ser[n])
            hexout[n]=hex(ser[n])
            binout[n]='{0:08b}'.format(ser[n])
        
        hexoutf=' '.join(hexout)
        binoutf=' '.join(binout)
        txtmem.write(hexoutf)
        txtmem.write('\n')
        txtmem.write(binoutf)
        txtmem.write('\n')
        hexoutf=None
        binoutf=None
        hexout=[]
        binout=[]


    elif(cmd=='d'):
        print("exiting")
        txtmem.close()
        exit()
>>>>>>> 1f8a856b2c785c96b181663465d5824e84011c3e

    # if (cmd[0]=='r'):
    #     print("read received")
    #     cmd=st.read(3)
    #     address=ord(cmd[0])*256+ord(cmd[1])
    #     size=ord(cmd[2])
    #     if (size==0): size = 256

    #     #setup pkt to be sent    
    #     pkt=memory[address]
    #     for n in range(1,size):
    #         pkt=pkt+memory[address+n]
        
    #     #send pkt
    #     st.write(pkt)


    # elif(cmd[0]=='w'):
    #     print("write received")
    #     cmd=st.read(3)
    #     address=ord(cmd[0])*256+ord(cmd[1])
    #     size=ord(cmd[2])
    #     if (size==0): size = 256
    #     cmd=st.read(size)
        
    #     for n in range(0,len(cmd)-1):
    #         memory[address+n]=cmd[n]#modify instantiated memory
        

    #     upstr=''.join(memory)
    #     open(memfile, 'r+').close()#update physical memory
    #     txtmem=open(memfile,"r+")
    #     txtmem.write(upstr)
    #     txtmem.close()

    # elif(cmd[0]=='p'):#use this command to print to console directly, for debud purposes
    #     print("print received")
    #     cmd=st.read(1)
    #     size=ord(cmd[0])
    #     if (size==0): size = 256
    #     cmd=st.read(size)
    #     print(cmd)
        
    # else:
    #     print("invalid command\n")

