// Test file for NestedCall test.

load Sys.vm,
output-file NestedCall.out,
compare-to NestedCall.cmp,
output-list RAM[0]%D1.6.1 RAM[1]%D1.6.1 RAM[2]%D1.6.1 RAM[5]%D1.6.1 RAM[6]%D1.6.1;



set sp 261,
set local 261,
set argument 256,
set this 3000,
set that 4000;

repeat 50 {
  vmstep;
}
output;
