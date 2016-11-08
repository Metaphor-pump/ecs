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
(Class1.set)
//function Class1.set 0
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
A=M
D=M
@Class1.vm.0
M=D
//C_POP static 0
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
@Class1.vm.1
M=D
//C_POP static 1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 0
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
(Class1.get)
//function Class1.get 0
@Class1.vm.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH static 0
@Class1.vm.1
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH static 1
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
(Class2.set)
//function Class2.set 0
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
A=M
D=M
@Class2.vm.0
M=D
//C_POP static 0
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
@Class2.vm.1
M=D
//C_POP static 1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 0
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
(Class2.get)
//function Class2.get 0
@Class2.vm.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH static 0
@Class2.vm.1
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH static 1
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
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 6
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 8
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
@2
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class1.set
0;JMP

(return_address1)
//call Class1.set 2
@SP
M=M-1
A=M
D=M
@5
M=D
//C_POP temp 0
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 23
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 15
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
@2
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class2.set
0;JMP

(return_address2)
//call Class2.set 2
@SP
M=M-1
A=M
D=M
@5
M=D
//C_POP temp 0
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
@0
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class1.get
0;JMP

(return_address3)
//call Class1.get 0
@return_address4
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

@Class2.get
0;JMP

(return_address4)
//call Class2.get 0
(WHILE)
@WHILE
0;JMP
//goto WHILE

