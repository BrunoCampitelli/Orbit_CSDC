import serial
#st = serial.Serial('COM3',115200, timeout=None,parity=serial.PARITY_NONE, rtscts=0)
st = serial.Serial('/dev/ttyACM0',115200, timeout=None,parity=serial.PARITY_NONE, rtscts=0)

payload="boi"
payload=list(payload)
size=len(payload)
print(size)

out=chr(size)
for n in range(1,size+1):
    out=out+payload[n-1]
print(out)
st.write(out.encode('utf-8'))
# st.write(chr(1).encode('utf-8'))
# size=st.read(1)
back=st.read(size)
print(back)