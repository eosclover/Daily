"""
文件读写
1.打开文件一次，多次读写后，然后在关闭文件
2.写代码之前，先理清楚思路，每一步要实现的内容，将目标做
   拆分
3.文件读写要注意的地方：
（1）文件切记要关闭
（2）IO输入输出流，都是针对内存而言，
    输入 input  从硬盘到内存  是读的过程
    输出 output 从内存到硬盘   是写的过程

"""
with open('SaveFile.txt', 'w') as f:
    for i in range(0, 21):
        a = 'test' + str(i)+'@126.com     123456\n'
        f.write(a)
        print(a)
    f.close()
