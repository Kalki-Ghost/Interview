# An e-commerce site has a series of advertisement to display. Links to the ads are stores in a data structure and they are displayed or not is based on the value at bit position in a number. The sequence of ads being displayed at this time can be represented as a binary value. Where 1 means the ad is displayed and 0 means ad is not displayed. The ads should rotate. So,when the next page loads, ads that are displayed now hidden and vice versa


def ads(number):
    binary = bin(number)
    binary = binary[2:]
    binary1 = ""
    for i in binary:
        if i == "1":
            binary1 += "0"
        else:
            binary1 += "1"
    number = 0
    for i in range(len(binary1)):
        if binary1[i] == '1':
            number += pow(2, len(binary1) - i - 1)
    return number


print(bin(50))
print(ads(50))
