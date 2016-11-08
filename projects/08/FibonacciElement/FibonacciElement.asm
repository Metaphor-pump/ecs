@256
D=A
@SP
M=D
//SP initialize
@return_address0
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Sys.init
0;JMP

(return_address0)
//call Sys.init 0
(Main.fibonacci)
//function Main.fibonacci 0
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
D=M-D
@RET_TRUE0
D;JLT
D=0
@CONTINUE0
0;JMP
(RET_TRUE0)
D=-1
(CONTINUE0)
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
M=M-1
A=M
D=M
@IF_TRUE
D;JNE
//if-goto IF_TRUE

@IF_FALSE
0;JMP
//goto IF_FALSE

(IF_TRUE)
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
@LCL
D=M
@R13
M=D

@R13
D=M
@5
D=D-A
A=D
D=M
@R14
M=D

@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D

@ARG
D=M+1
@SP
M=D

@R13
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D

@R13
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D

@R13
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D

@R13
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D

@R14
A=M
0;JMP
//return
(IF_FALSE)
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
@return_address1
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(return_address1)
//call Main.fibonacci 1
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
@return_address2
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(return_address2)
//call Main.fibonacci 1
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
@LCL
D=M
@R13
M=D

@R13
D=M
@5
D=D-A
A=D
D=M
@R14
M=D

@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D

@ARG
D=M+1
@SP
M=D

@R13
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D

@R13
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D

@R13
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D

@R13
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D

@R14
A=M
0;JMP
//return
(Sys.init)
//function Sys.init 0
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 4
@return_address3
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(return_address3)
//call Main.fibonacci 1
(WHILE)
@WHILE
0;JMP
//goto WHILE              
