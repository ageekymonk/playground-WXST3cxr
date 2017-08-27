# Eval, Exec and Compile
## Eval
Eval is used to evaulate dynamically generated python `expression`. It cannot evaluate statements. For example `eval('10+5')` is valid but `eval('a=5')` is not valid. This means it cannot be used to evaluate function definition, loops etc. It returns last executed expression.

## Exec
Exec is used to execute dynamically generated python code. It always returns None. It can execute any python code like loop, function, class etc.

## Compile
This might seem odd for a interpreted language. But this is used to compile code into python bytecode. It is used to speed up the repeated execution of a code.

@[Eval Exec Compile]({"stubs": ["eval_exec_compile.py"], "command": "python3 eval_exec_compile.py"})
