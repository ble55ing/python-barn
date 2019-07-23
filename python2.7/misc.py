#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import binascii
import zlib
import Image
def _crc32(v):
  """
  Generates the crc32 hash of the v.
  @return: str, the str value for the crc32 of the v
  """
  return '0x%x' % (binascii.crc32(v) & 0xffffffff) #取crc32的八位数据 %x返回16进制

#将01字符串生成二维码
def Toqrcode(str,xlen,ylen):
    MAX = xlen;
    if MAX<ylen:
        MAX = ylen
    pic = Image.new("RGB", (MAX, MAX))

    #str = "000000000011010010000111101110101001110110010010011110110010111001010011000010011110100100110000101100100111011000010100101001100001101000111011000101110100001011001001110110010000100110101100100001111010010011000111010110000000000"

    i = 0
    for y in range(0, ylen):
        for x in range(0, xlen):
            if (str[i] == '1'):
                pic.putpixel([x, y], (0, 0, 0))
            else:
                pic.putpixel([x, y], (255, 255, 255))
            i = i + 1
    pic.show()
    pic.save("qrcode.png")

#将01字符串生成一维码
def Tobarcode(str,xlen,ylen):
    MAX = xlen;
    if MAX < ylen:
        MAX = ylen
    pic = Image.new("RGB", (MAX, MAX))

    str = "000000000011010010000111101110101001110110010010011110110010111001010011000010011110100100110000101100100111011000010100101001100001101000111011000101110100001011001001110110010000100110101100100001111010010011000111010110000000000"

    i = 0
    for x in range(0, 231):
        for y in range(0, 31):
            if (str[i] == '1'):
                pic.putpixel([x, y], (0, 0, 0))
            else:
                pic.putpixel([x, y], (255, 255, 255))
        i = i + 1
    pic.show()
    pic.save("barcode.png")

# 摩斯密码表(自己可定义加密方式...)
CODE = {
    # 26个字母
    'A': '.-',  'B': '-...',    'C': '-.-.',
    'D': '-..', 'E': '.',    'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',    'K': '-.-', 'L': '.-..',
    'M': '--',  'N': '-.',  'O': '---',
    'P': '.--.',    'Q': '--.-',    'R': '.-.',
    'S': '...', 'T': '-',   'U': '..-',
    'V': '...-',    'W': '.--', 'X': '-..-',
    'Y': '-.--',    'Z': '--..',

    # 10个数字
    '0': '-----',   '1': '.----',   '2': '..---',
    '3': '...--',   '4': '....-',   '5': '.....',
    '6': '-....',   '7': '--...',   '8': '---..',
    '9': '----.',

    # 16个标点符号
    ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
    '?': '..--..', '=': '-...-',    "'": '.----.', '/': '-..-.',
    '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
    ')': '-.--.-', '$': '...-..-','&': '. . . .','@': '.--.-.'

# 下面还可自行添加密码字典
}
# 反转字典(作为解密摩斯密码的字典)
UNCODE = dict(map(lambda t:(t[1],t[0]),CODE.items()))

#将字符串转换为摩斯码，用空格分离
def stringToMorseAlphabet(msg):
    # message用于保存加密结果
    message = ''
    # msg = raw_input('Message:')
    # msg = 'this is test'
    for c in msg:
        if c == ' ':
            message += ' '
        else:
            # upper():将所有小写字母转换成大写字母
            message += CODE[c.upper()] + ' '
    return message
#将没有空格的摩斯码按长度优先原则翻译
def morseAlphabetToStringnonull(morseCode):
    morseres = ""
    while len(morseCode)>0:
        try:
            morseres+=UNCODE[morseCode[:5]]
            morseCode = morseCode[5:]
        except:
            try:

                morseres+=UNCODE[morseCode[:4]]
                morseCode = morseCode[4:]
            except:
                try:

                    morseres += UNCODE[morseCode[:3]]
                    morseCode = morseCode[3:]
                except:
                    try:
                        morseres += UNCODE[morseCode[:2]]
                        morseCode = morseCode[2:]
                    except:
                        try:

                            morseres += UNCODE[morseCode[:1]]
                            morseCode = morseCode[1:]
                        except:
                            print 'error in morseAlphabetToStringnonull:not find Morse'
                            break;

    return morseres
# 将有空格的摩斯码进行翻译，返回结果字符串
def morseAlphabetToString(morseCode):
    # message用于保存解密结果
    message = ''
    list = morseCode.split(' ')
    if morseCode.find("_")>=0:
        morseCode.replace("_","-")
    # print list
    for s in list:
        if s == '':
            message += ' '
        else:
            message += morseAlphabetToStringnonull(s)
    return message
# 将没有空格的摩斯码进行翻译，返回所有可能结果的list （没做）