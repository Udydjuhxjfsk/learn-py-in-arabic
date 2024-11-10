import marshal
myfile = input('write path file : ')
open_file = open(myfile, 'r') .read()
compile_file = compile(open_file, '', 'exec')
encrypt = marshal.dumps(compile_file)
code = open('New_'+str(myfile),'w')
code.write('import marshal\n')
code.write('exec(marshal.loads('+repr(encrypt)+'))\n')
print("the file encrypted : " + str(myfile))