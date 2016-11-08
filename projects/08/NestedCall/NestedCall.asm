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
(Sys.init)
//function Sys.init 0
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
@0
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Sys.main
0;JMP

(return_address1)
//call Sys.main 0
@SP
M=M-1
A=M
D=M
@6
M=D
//C_POP temp 1
(LOOP)
@LOOP
0;JMP
//goto LOOP

(Sys.main)
//function Sys.main 0
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 123
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

@Sys.add12
0;JMP

(return_address2)
//call Sys.add12 1
@SP
M=M-1
A=M
D=M
@5
M=D
//C_POP temp 0
@246
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 246
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
(Sys.add12)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
//function Sys.add12 3
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
@12
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 12
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
