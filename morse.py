import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT)
dot=0.3
def short():
    GPIO.output(20, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(20, GPIO.LOW)
def long():
    GPIO.output(20, GPIO.HIGH)
    time.sleep(dot*3)
    GPIO.output(20, GPIO.LOW)
def sos():
    for x in range(0,3):
        short()
        time.sleep(dot)
    time.sleep(dot)
    for x in range(0,3):
        long()
        time.sleep(dot)
    time.sleep(dot)
    for x in range(0,3):
        short()
        time.sleep(dot)
characters=[
    '1','2','3','4','5','6','7','8','9','0',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '.',',','\'','\"','_',':',';','?','!','-','+','/','(',')','=','@'
    ]
code=[
    '01111',#1
    '00111',#2
    '00011',#3
    '00001',#4
    '00000',#5
    '10000',#6
    '11000',#7
    '11100',#8
    '11110',#9
    '11111',#0
    '01',#A
    '1000',#B
    '1010',#C
    '100',#D
    '0',#E
    '0010',#F
    '110',#G
    '0000',#H
    '00',#I
    '0111',#J
    '101',#K
    '0100',#L
    '11',#M
    '10',#N
    '111',#O
    '0110',#P
    '1101',#Q
    '010',#R
    '000',#S
    '1',#T
    '001',#U
    '0001',#V
    '011',#W
    '1001',#X
    '1011',#Y
    '1100',#Z
    '01',#A
    '1000',#B
    '1010',#C
    '100',#D
    '0',#E
    '0010',#F
    '110',#G
    '0000',#H
    '00',#I
    '0111',#J
    '101',#K
    '0100',#L
    '11',#M
    '10',#N
    '111',#O
    '0110',#P
    '1101',#Q
    '010',#R
    '000',#S
    '1',#T
    '001',#U
    '0001',#V
    '011',#W
    '1001',#X
    '1011',#Y
    '1100',#Z
    '010101',#.
    '110011',#,
    '011110',#'
    '010010',#"
    '001101',#_
    '111000',#:
    '101010',#;
    '001100',#?
    '101011',#!
    '100001',#-
    '01010',#+
    '10010',#/
    '10110',#(
    '101101',#)
    '10001',#=
    '011010'#@
    ]
message=input("Write a message: ")
for i in range (0, len(message)):
    if message[i]==' ':
        time.sleep(dot*7)
    elif message[i] in characters:
        for j in range (0,len(code[characters.index(message[i])])):
            if code[characters.index(message[i])][j]=='0':
                short()
                print(0)
                time.sleep(dot)
            elif code[characters.index(message[i])][j]=='1':
                long()
                time.sleep(dot)
                print(1)
            else:
                print(code[j])
                sys.exit("wrong character in code")
        time.sleep(dot*3)
    else:
        print(message[i])
        sys.exit("wrong character in message")
    print("\n")
