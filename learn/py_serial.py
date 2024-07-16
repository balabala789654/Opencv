import serial
import serial.tools.list_ports

ports_list = list(serial.tools.list_ports.comports())
for comport in ports_list:
    print(list(comport)[0], list(comport)[1])

count = 100
ser = serial.Serial(port='COM3', baudrate=115200, timeout=1) # 打开串口
ser.write(f'the number is {count}') # 对串口发送数据
data = ser.read(10) # 读取10个字节
ser.close() # 关闭串口


