    @2
    M=0
(LOOP)
    @1
    D=M
    D=D-1
    M=D
    @END
    D;JLT
    @0
    D=M
    @2
    M=M+D
    @LOOP
    0;JMP
(END)
    @END
    0;JMP