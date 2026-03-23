# 一.变量的名字
关键字keyword：int、float、void不可改变的名字
标识符identifier，symbolic name：变量名、函数名
标识符的原则：标识符只能由**字母、数字和下划线**组成，**数字不可以出现在第一个位置上** ，C语言的关键字不可以用做标识符

# 二.初始化

int a = 0
问：如果不进行初始化，也没有scanf输入进行初始化？
	程序会正常运行，但结果会错误
就是单纯声明是垃圾值。
# 三.表达式expression

1.定义：有运算符的式子就叫做表达式（“=”也是运算符，是赋值运算符）
price = 0;
change=100-price

2.表达式的值：当表达式被计算时得到的结果。
N = 2+3 表达式的值为5
n == 5 如果n=5表达式的值为true,n≠5表达式的值为false ^41e00e

# 四.常量constant

1.整形常量intergar constant：42, -10, 0xFF
2..浮点常量：3.14
3.字符常量character constant：用单引号括起来的单个字符。例如：'A', '7', '\n'。
4.字符串常量string constant：字符串常量是用双引号括起来的字符序列。例如："Hello, World!"。
5.符号常量：通过预处理指令#define定义的常量
宏定义[[lec10预处理器#^fda6dc]]
```
#define PI 3.14159

#define MAX_SIZE 100
```
6.. Array数组、Pointer指针、Structure结构体、Union联合体、Enum枚举……
# 五、四则运算(运算符)

^2c1e51
<img width="649" height="370" alt="Pasted image 20240616160715" src="https://github.com/user-attachments/assets/17b3a42d-56dd-43c3-a1a6-77c8dab307ba" />

运算后结果自动转换[[lec11 类型进阶#]]


# 六、数据类型的输入输出
整数
int
printf("%d",…)
scanf("%d",…)

 带小数点的数[[lec11 类型进阶#^255546]]
double
printf("%f",…)
scanf("%lf",…)

# 七、运算符的优先级（同级按照从左往右谁先）
<img width="1006" height="431" alt="download" src="https://github.com/user-attachments/assets/9f7e3c3a-f955-48bc-aadd-5fd94aeb2cd3" />


加减乘除是从左往右，正负号/赋值是从右往左
延申：如何交换a、b两个数的值(a=5，b=6)

1.令一个新变量为c c=a，a=b，b=c

2.a=a + b 11
   b=a - b 5
   a=a - b 6 ^e60535

# 八、递增递减运算符（考试）

i++ ^246d80
运算结果：给i加1
表达式的值：没加1之前的值

++i
运算结果：给i加1
表达式的值：加上1之后的值

技巧：a在前表示a不变，a在后表示a变
例：a=1 则b=1+(++a)=3
b=1+(a++)=2
++a=a++=2
<img width="677" height="288" alt="Pasted image 20240616161530" src="https://github.com/user-attachments/assets/d599eea7-0e2a-404e-a97e-bf1501826d64" />


# 九、关系运算的结果

当两个值的关系符合关系运算符的预期时， 关系运算的结果为整数1，否则为整数0

# 十、计算时间差的程序

题目：输入两个时间，每个时间分别输入小时和分钟的值，然后输出两个时间之间的差，也以几小时几分表示 （如果直接相减，会出现分钟错位的情况，1点40分和2点10分）
<img width="866" height="607" alt="download" src="https://github.com/user-attachments/assets/a894e130-1c23-4f08-924f-f868feb0bf13" />
