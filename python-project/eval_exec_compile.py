# eval
a = eval('100*200')
print(f'Value of a is {a}')

b = exec('a = 100*200')
print(f'Value of a is {a} b is {b}')

# compiling the code
eval_compiled_code = compile('100*200', '<string>', 'eval')
exec_compiled_code = compile('a = 100*200', '<string>', 'exec')

a = eval(eval_compiled_code)

b = exec(exec_compiled_code)

# This is the quirky part. Eval can run exec compiled code and returns value
eval(exec_compiled_code)
