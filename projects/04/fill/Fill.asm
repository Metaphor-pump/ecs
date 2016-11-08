// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here

@24576
D=A
@MXSCREEN
M=D

@SCREEN
D=A
@PTR
M=D

(LOOP)
    @KBD
    D=M
    @FILL
    D;JGT
    @UNFILL
    0;JMP

(UNFILL)
    @SCREEN // Do nothing if POINTER == SCREEN
    D=A    //因为SCREEN是常量，所以要用A表示而不能用M
    @PTR
    D=D-M
    @LOOP
    D;JEQ

    @PTR //UNFILL THE PIXEL
    A=M
    M=0  //0的二进制是0000 0000 0000 0000 ，这个动作填充了16个像素为白色

    @PTR //ITERATE THE PTR BY 1
    M=M-1

    @LOOP  // Jump back to main loop
    0;JMP

    
(FILL)
    @MXSCREEN // Do nothing if the screen is full
    D=M
    @PTR
    D=D-M
    @LOOP
    D;JEQ

    @PTR // Fill in the pixel
    A=M
    M=-1 //-1的二进制为1111 1111 1111 1111，这个动作填充16个像素为黑色，切勿写成M=1，否则填充的结果是每隔15像素一条竖线，而不是黑屏

    @PTR // Iterate pointer by 1
    M=M+1

    @LOOP  // jump back to main loop
    0;JMP