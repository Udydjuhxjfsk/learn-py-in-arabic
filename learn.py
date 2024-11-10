# w r a => write - read - append
#  write => ينشأ ملف ويقوم بالكتابه فيه
#  read => يقوم بقرائة الملفات
# append => يضيف نص جديد للنص القديم
# variable = open('file' , '')
f = open('learn.txt','a')
f.write("\nhiiiiiii")
f.close()