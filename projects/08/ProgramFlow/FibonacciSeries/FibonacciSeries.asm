@ARG
D=M
@1
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH argument 1
@SP
M=M-1
A=M
D=M
@4
M=D
//C_POP pointer 1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 0
@SP
M=M-1
A=M
D=M
@THAT
A=M
M=D
//C_POP that 0
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 1
@SP
M=M-1
A=M
D=M
@THAT
A=M
A=A+1
M=D
//C_POP that 1
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH argument 0
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 2
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
//sub
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
//C_POP argument 0
(MAIN_LOOP_START)
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH argument 0
@SP
M=M-1
@SP
A=M
D=M
@COMPUTE_ELEMENT
D;JGT
D;JLT
//if-goto COMPUTE_ELEMENT 
@END_PROGRAM
0;JMP
//goto END_PROGRAM        
(COMPUTE_ELEMENT)
@THAT
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH that 0
@THAT
D=M
@1
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH that 1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
//add
@SP
M=M-1
A=M
D=M
@THAT
A=M
A=A+1
A=A+1
M=D
//C_POP that 2
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH pointer 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
//add
@SP
M=M-1
A=M
D=M
@4
M=D
//C_POP pointer 1
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH argument 0
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
//sub
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
//C_POP argument 0
@MAIN_LOOP_START
0;JMP
//goto MAIN_LOOP_START

(END_PROGRAM)
