import smbus
import sys
sys.path.insert(0, '')

from pcf8575 import PCF8575
#bus = smbus.SMBus(1)

i2c_port_num = 1
pcf_address = 0x20

#address=0x40
#address=0x20

pcf = PCF8575(i2c_port_num, pcf_address)

#bus.read
#bus.write_i2c_block_data(address, reg_write_dac, msg)
#bus.write_byte(

print('it worked: ')
print(pcf.port)
