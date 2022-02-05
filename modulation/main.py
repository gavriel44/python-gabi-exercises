
from operator import le
from matplotlib import pyplot as plt
from numpy import sin
from math import pi

def modulate(message: str):
    """
    message - a message to be modulated to AM
    """
    y_final = []

    bit_x = [i* pi/180 for i in range(361)]

    encoded_message = message.encode("ascii")


    f = 3
    cycles = 0

    for byte in encoded_message:
        byte = bin(byte)[2:]
        if len(byte)<7:
            byte = "0" + byte
        for bit in byte:
            cycles += 1
            amplitude = 6
            # print(type(bit))
            if bit == "1":
                amplitude = 2
            
            bit_y = [amplitude * sin(f*i) for i in bit_x]
            y_final.extend(bit_y)

    x_final = [i * pi/180 for i in range(361 * cycles)]
    return x_final, y_final


def demodulate(wave_y):

    bit_string = get_bit_str_from_wave_y(wave_y)
    return bit_str_to_str(bit_string)
    

def get_bit_str_from_wave_y(wave_y):
    bit_string = ''
    for i in range(90, len(wave_y), 361):
        if wave_y[i] > -3:
            bit_string = bit_string + "1"
        else:
            bit_string = bit_string + "0"
    return bit_string


def bit_str_to_str(bit_str):
    final_str =''
    
    # slicing the input and converting it
    # in decimal and then converting it in string
    for i in range(0, len(bit_str), 7):
        
        temp_data = bit_str[i:i + 7]
        
        decimal_data = int(temp_data, 2)
    
        final_str = final_str + chr(decimal_data)

    return final_str


if __name__ == "__main__":
    # modulate("hello asda")
    # # print(modulate("hello"))
    plt.plot(*modulate("helLo to yOu my"))
    plt.show()

    wave_x, wave_y = modulate("helLo to yOu my")
    print(demodulate(wave_y))