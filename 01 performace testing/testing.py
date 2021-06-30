# a = ['1' , '6789']
# b = []
# for i in a:
#     for t in range(1,11):
#         b.append(i[0])
#         c = len(b)
#         for tt in range(1,6791):
#             if(c == 10):
#                 d = tt
#                 for t2 in range(1,11):
#                     b.append(d)
#                     print(b)
import codecs
out_path = "Dataset/"


a = ['1' , '6789']
b = []
for i in a:
    for t in range(1,11):
        b.append(i[0])
        c = len(b)
        if(c == 10):
            for tt in range(2,6792):
                d = tt
                for t2 in range(1,11):
                    b.append(d)
    print(b)
    file_name = out_path + "format_00" +".gt.txt"
    file = codecs.open(file_name, "w", "utf-8") 
    file.write("{}".format(b)) 
    file.close() 