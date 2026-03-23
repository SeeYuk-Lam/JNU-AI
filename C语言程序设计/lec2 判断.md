# 关系运算符relational opeartor
<img width="643" height="344" alt="Pasted image 20240616170636" src="https://github.com/user-attachments/assets/85a24205-0a82-4dfd-a2c6-d814f55dc028" />
^dd45b8
在c语言中，只有0值为假，其余非0值都为真
# 逻辑运算符logical operator
&&代表and，也就是与
||代表or，也就是或
!代表非，作用是反转布尔值，而不是在原来的数字上加负号
```
11. (b)The result of the following program is  
main()  
{  int a = -2, b;  
   do  
   {  b = ++a; b=-1  
      if (!b) printf(“#”);  
      else printf(“*”);  
    }while(a<1)  
}  
A}#*# B} *#*  
C)### D) ***
```
# 条件运算符conditional operator
三目运算符`a>5?1:0`
# 赋值运算符assignment operator
a=1；
# 算术运算符arithmetic operator
# 顺序：算术>赋值>

# 一、else的匹配
<img width="905" height="237" alt="download" src="https://github.com/user-attachments/assets/8a6280e5-ca36-4a5b-aa00-2cbaa7c269c2" />


else是与第一个if匹配
缩进不能暗示else的匹配（与python不同）
<img width="576" height="236" alt="download" src="https://github.com/user-attachments/assets/b649895f-9188-4237-95ab-e07139da176a" />


else与第二个if匹配
else总是与最近的if匹配（无括号的情况）
# 二、if

1.**if的作用范围为后面的第一条语句**或复合语句（用花括号括起来）
2.嵌套的if
```c
if ( gameover == 0 )
	if ( player2move == 2 )
printf("Your turn\n")；
```

^0cd1a6

1. 如果 gameover 的值为 0，表示游戏尚未结束。
	- 如果 player2move 的值为 2，表示轮到玩家2进行操作。
	- 在这种情况下，代码会执行 printf("Your turn\n")，输出 "Your turn"，提示玩家2轮到他操作了。
2. 如果 gameover 的值为 0，表示游戏尚未结束。
	- 如果 player2move 的值不为 2，表示当前不是玩家2的轮次。
	- 在这种情况下，代码不会执行 printf("Your turn\n")，没有输出。
3. 如果 gameover 的值不为 0，表示游戏已经结束。
	- 不管 player2move 的值是什么，都不会执行 printf("Your turn\n")，没有输出。

3.在写if else时尽量使用单一出口原则
<img width="888" height="488" alt="download" src="https://github.com/user-attachments/assets/76f76da2-0246-4d79-aa86-309356387c4e" />


4.if如果后面加：或者；会出现什么结果
执行，会输出空语句

# 三、多路分支，switch-case

^319d59

1.switch与if的对比
<img width="958" height="698" alt="download" src="https://github.com/user-attachments/assets/26ca4ff7-74ae-4427-8620-f41998f97f94" />


2.基本格式
<img width="523" height="579" alt="download" src="https://github.com/user-attachments/assets/6416728d-030c-4d83-8084-cedc800133e1" />


控制表达式只能是整数型的结果
• 常量可以是常数，也可以是常数计算的表达式
• 根据表达式的结果，寻找匹配的case，并执行case后面的语句，一直到break为止 （后面的语句不会再判断case） 没有break会直接执行到default
• 如果所有的case都不匹配，那 么就执行default后面的语句 ；如果没有default，那么就什么都不做
• case后面不需要{}，需要用冒号：
(a) switch结构不是循环体，continue没有用处
<img width="416" height="529" alt="download" src="https://github.com/user-attachments/assets/73f97816-d130-459e-850b-5535b56ea064" />

没有break，输出结果为<img width="116" height="97" alt="download" src="https://github.com/user-attachments/assets/b706feaf-80fd-471c-bb2f-2ec7e5c58edf" />

