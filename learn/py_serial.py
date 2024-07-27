import serial
import serial.tools.list_ports
import time

# write函数只支持传输bytes类型数据
# 用b""表示bytes类型
# 也可以使用encode()函数将字符串类型转换成bytes类型
# 使用decode()函数将bytes类型转换成字符串类型
if __name__ == "__main__":
    ser = serial.Serial(port='COM10', 
                        baudrate=115200, 
                        bytesize=serial.EIGHTBITS, 
                        parity=serial.PARITY_NONE, 
                        stopbits=serial.STOPBITS_ONE, 
                        timeout=1) # 打开串口
    count = 1
    while True:
        result = ser.write(f"{count}".encode('utf-8')) # 对串口发送数据
        # print("send data len: ", result)
        count += 1
        time.sleep(0.5)
        
    # data = ser.read(10) # 读取10个字节
    # ser.close() # 关闭串口


