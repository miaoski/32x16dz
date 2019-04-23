#!/bin/env python2
# coding: utf8
# 將文字轉換成跑馬燈可以用的 HEX 格式，每個字 16x15 一行。
# 倚天中文字型檔格式

import sys

SCREEN = True

std15  = open('STDFONT.15', 'rb')
sup15 = open('SPCFSUPP.15', 'rb')
spc15  = open('SPCFONT.15', 'rb')
asc15  = open('ASCFONT.15', 'rb')

if len(sys.argv) < 2:
    print '用法:', sys.argv[0], 'UTF-8中文字串'
    print '* 不在 Big5 字集內的字會被自動忽略，目前也不支援半形英數'
    sys.exit(1)

s = sys.argv[1].decode('utf-8').encode('big5', 'ignore')
words = []

for i in range(0, len(s), 2):
    hb, lb = ord(s[i]), ord(s[i+1])
    big5 = hb * 256 + lb                    # 用 << 8 會有奇怪的結果
    ladd = (lb - 64) if (lb < 127) else (lb - 161 + 63)
    if big5 >= 0xa140 and big5 <= 0xa3bf:   # spcfont 特殊符號
        hadd = (hb - 161) * 157
        loc = hadd + ladd;
        words.append((spc15, loc))
    elif big5 >= 0xc6a1 and big5 <= 0xc8d3: # spcfsupp 日文
        hadd = (hb - 198) * 157 - 63
        loc = hadd + ladd + 66;             # 修正 Python 的日文 bug
        words.append((sup15, loc))
    elif (0x7e >= lb >= 0x40 or 0xfe >= lb >= 0xa1) and (0xc67e >= big5 >= 0xa440 or 0xf9fe >= big5 >=0xc940):
        hadd = (hb - 164) * 157             # Big5 字元集 stdfont
        loc = hadd + ladd;
        if big5 >= 0xc940:
            loc -= 408
        words.append((std15, loc))
    else:
        print '不支援的字: %02x%02x' % (hb, lb)

canvas = [[] for _ in range(16)]

for fp,loc in words:
    fp.seek(loc * 30, 0)
    shape = fp.read(30)
    #if SCREEN:
    #    for i in range(0, 30, 2):
    #        print '{0:08b}{1:08b}'.format(ord(shape[i]), ord(shape[i+1])).replace('0', ' ')       # 輸出到螢幕
    #else:
    #    for i in range(0, 30, 2):
    #        print '{0:#04x}, {1:#04x},'.format(ord(shape[i]), ord(shape[i+1])),                   # 輸出成 hex
    #    print '0x00, 0x00'
    #    print ','
    canvas[0].append(0x00)              # 最上面留白
    canvas[0].append(0x00)
    for i in range(0, 15):
        canvas[i+1].append(ord(shape[i * 2]))
        canvas[i+1].append(ord(shape[i * 2 + 1]))

for i in range(16):
    for x in canvas[i]:
        sys.stdout.write('{0:08b}'.format(x).replace('0', ' '))
    print
print
for i in range(16):
    print ''.join(['{0:#04x}, '.format(x) for x in canvas[i]])
