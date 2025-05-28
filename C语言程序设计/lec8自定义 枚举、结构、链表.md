# 一、枚举
## 1.常量符号化
```c
const int red = 0;
const int yellow = 1;
const int green = 2;
```
## 2.枚举
`enum COLOR{RED,YELLOW,GREEN};`
枚举是一种用户定义的数据类型，它用关键字 enum 以如下语法来声明
`enum 枚举类型名字 {名字0,…, 名字n} ;`
枚举类型名字通常并不真的使用，要用的是在大括号里的名字，因为它们就是就是常量符号，它们的类型是int，值则依次从0到n。
名字0的值是0，名字1的值是1，名字2的值是2.......
**当需要一些可以排列起来的常量值时，定义枚举的意义就是给了这些常量值符号化**

### 2.1 套路：自动计数模型
[[lec7 字符串#^eb1b23]]
```c
#include <stdio.h>
enum COLOR{RED,YELLOW,GREEN,NumCOLORS};//NumCOLORS代表一共有几个常量
int main(){
int color = -1;
char * ColorNames[NumCOLORS]={"red","yellow","green"};//建立一个用枚举量做下标的字符串数组，后面遍历或者调用容易很多
char *colorName =NULL;//初始化字符指针，在下面的程序中作为字符变量

printf("请输入你喜欢的颜色代码：");
scanf("%d",&color);
if (color>=0 && color<NumCOLORS){
colorName = ColorNames[colors];
}
else{
colorName = "unknown";
}
printf("你喜欢的颜色是%s\n"，colorName)；//%s，输出字符串
}
```

# 二、结构
## 1.引入：声明结构类型
```c
int main(){
struct data{
   int month;
   int day;
   int year;
};//！！！注意分号！！!最容易漏
struct data today;//！！！注意分号！！!最容易漏

today.month = 07;
today.day = 31;
today.year = 2023;
}
```

```c
int main(){
struct data{
   int month;
   int day;
   int year;
};//！！！注意分号！！!最容易漏

struct data today={07，31，2014};//这个暂时不考
}
```
## 2.声明结构的形式

![[Pasted image 20240523093232.png]]
对于第一和第三种形式，都声明了结构point。但是第二种形式没有声明point，只是定义了两个变量
**注意：声明结构体时，在函数内部声明的只能在函数内部使用，所以通常在函数外部声明结构类型，这样可以被所以函数所使用**

point指的是结构struct的**标签**，
p1，p2表示用point这个结构体的**结构体变量**
x,y为结构体的**成员**

## 使用typedef与结构体
在编程中使用typedef目的一般有两个，一个是给变量提供一个易记且意义明确的新名字（类型有新别名，方便变量的定义），另一个是简化一些比较复杂的类型声明。

typedef是类型定义的意思。typedef struct 是为了使用这个结构体方便。
具体区别在于:
若`struct node {}`这样来定义结构体的话。在申请node的变量时，需要这样写，`struct node n;`
若用typedef，可以这样写，`typedef struct node{}NODE`; 定义结构体时。在申请变量时就可以这样写，`NODE n;`
区别就在于使用时，是否可以省去struct这个关键字。

## 3.结构成员
结构与数组有点像
数组用[]运算符和下标访问成员
结构体用.运算符和名字访问其成员
today.day   student.firstName  p1.x  p1.y
**注意！数组名字是指针（地址），结构体名字不是指针（地址），必须用&运算符**
```c
int main(){
struct data{
   int month;
   int day;
   int year;
};//！！！注意分号！！!最容易漏
struct data today;//！！！注意分号！！!最容易漏

today.month = 07;
today.day = 31;
today.year = 2023;

struct date *pData = &today
}
```
指针的类型是struct date，是一个结构体指针，然后把一个结构体的地址赋给该指针

## 4.结构与函数
#### 4.1 结构作为函数参数
`int number0fDays(struct date d)`
整个结构可以作为参数的值传入函数
这时候是在函数内**新建一个结构变量，并复制调用者的结构的值**
也可以返回一个结构
#### 4.2 输入结构
看下面的程序
```c
#include <stdio.h>

struct point {
int x;
int y; 
};

void getStruct(struct point p){
scanf("%d", &p.x);
scanf("%d",&p.y);
}

int main(){
struct point y ={0,0};
getStruct(y);
printf("%d %d",&y.x,&y.y);//输出 y.x=0,y.y=0,并没有改变值
}
```
因为在c语言中调用是传值的，函数中的p与main中的y是不同的

**解决方法**
因为函数可以返回一个结构体，因此可以在函数中建立一个临时的结构变量改变结构体成员，然后直接把结构体return回去
```c
struct point inputPoint(){//返回的是point类型结构体，因此函数类型为struct point
struct point temp;
scanf("%d", &temp.x);
scanf("%d",&temp.y);
return temp;
}
void main(){
struct point y={0,0};
y = inputPoint();//直接return回y
printf("%d %d",&y.x,&y.y);
}
```

#### 4.3 结构指针作为参数(重要，后面构造链表要用到)
##### 4.3.1 指向结构的指针
```c
struct date{
int month;
int day;
int year;
};
struct date myday;
struct date *p= &myday;

(*p).month = 12;
p->month = 12;//用->表示指针所指的结构变量中的成员
```
注意！！！
1.这里为什么没有给**结构体变量初始化**，也能直接传递给指针？
指针 `p` 被初始化为 `&myday`，即 `myday` 的地址。由于 `myday` 已经**被隐式地初始化了**，所以 `p` 指向了一个有效的内存地址，它指向的内存包含了**已经初始化的值**（在这个例子中，所有成员都是0）。
其他变量，如字符串，一定要初始化后再传递给指针变量。[[lec7 字符串#5.2.3常见错误：使用指针时必须先初始化！！！]]

2.p->month表示`(*p).month`,成员的值
```c
struct point *inputPoint(struct point*p){
scanf("%d", &(p->x));
scanf("%d",&(p->y))
}
void main(){
struct point y={0,0};
inputPoint(&y);//传入y的地址给函数
printf("%d %d",&y.x,&y.y);
}


```

# 三、链表（数据结构）考试必考！
## 3.1 初始了解
我们至少有两种方法来存储数据
1.数组：
	优点：存储速度快，访问快`a[3]=*(a+3)`，
	缺点：需要一个连续很大的内存 插入和删除元素很麻烦
2.链表：
	 优点：插入和删除元素的效率高，不需要一个很大的内存
	 缺点：查找某个元素的效率很低
![[Pasted image 20240523173144.png]]
头结点：
	头结点存储的数据类型和首节点的类型是一模一样
	头结点是首节点前面的那个节点
	头结点并不存放有效数据，存放头指针head
	头结点的目的是方便对链表进行操作
头指针head
	存放头结点地址的指针变量
首结点：
	存放第一个有效数据的节点
尾结点：
	存放最后一个有效数据的节点，它的指针指向一个“NULL”
每个结点包含两个部分：1.用户需要的实际数据 2.下一个结点的地址

## 3.2什么是链表
```c
struct Student{
int num;
float score;
struct Student*next;//next是指针变量，指向下一个结构体的变量，链表的核心
}
```
成员num和score用来存放结点中的有用值（用户需要用到的数据）。
next是指针类型的成员，它指向**下一个**struct Student类型数据（就是next所在的结构体类型）
**假设第一个结构体a，第二个结构体b，a.next指向b的值**
`a.next->num`
![[Pasted image 20240523233755.png]]

## 3.3 建立简单的静态链表
建立一个简单链表，它由3个学生数据的结点组成，要求输出各结点中的数据
![[Pasted image 20240523233847.png]]
```c
#include <stdio.h>
struct Student//声明结构体类型struct Student
{
int num;
float score;
struct Student*next;//指向下一个结构体
};
int main(){
struct Student a,b,c,*head,*p;
//定义3个结构体变量a,b,c作为链表的结点,head为头指针，p为移动的指针
a.num=10101;a.score=89.5;
b.num=10103;b.score=90;
c.num=10107;c.score=85;
head=&a;
a.next=&b;
b.next=&c;
c.next=NULL;
p=head;//p刚开始为head指针，head指向a
do{
printf("%ld %5.ld\n",p->num,p->score);
p=p->next;//使p指向下一个结点，好好理解
}while(p! =NULL);
return 0;
}
```
head指向a的结点，a.next指向b结点，b,next指向c结点，c.next指向NULL
输出链表要借助p，p=head先指向a结点，p->next的值是b的地址，p=p->next后p就指向b的地址
## 3.4 建立简单的动态链表(双向的，循环的)
写一函数建立一个有3名学生数据的单向动态链表
![[Pasted image 20240523235235.png]]![[Pasted image 20240524003630.png]]
核心代码
```c
p1 先指向新输入的结构体的值
p2 此时指的是后一个结构体的值
p2 —>next = p1;
p2 = p1;
p2 ->next = NULL;
```
 **所以要给出if else的判断**
	当n=1时，表示输入的是第一个学生的数据，那么头结点指针head指向这个第一个结点
	当n>1时，表示输入的是后面学生的数据，（p1始终指向最新数据，p2尾指针此时指向上一个结点），把上一个结点的next指针指向p1（`p2->next = p1`），然后将p2=p1（因为当输入下一个数据，p1又会更新为新结点的地址，p2必须指向老p1的地址，才表示的是上一个结点的地址）


```c
#include <stdio.h>
#include<stdlib.h>// 包含标准库，用于动态内存分配等
#define LEN sizeof(struct Student)// 定义一个宏LEN，它的值是结构体Student的大小。这样在代码中就可以用LEN代替计算大小的表达式，使代码更清晰。
struct Student{//定义链表结构体
int num;
float score;
struct Student*next;
};
int n;//定义一个整型变量n，用于计数输入的学生数量。

struct Student*creat(void)//定义函数。此函数返回一个指向链表头的指针
{
struct Student*head;
struct Student*p1,*p2;//定义三个指向Student结构体的指针：head用于指向链表的头结点，p1用于指向当前正在处理的结点，p2用于指向前一个结点。
n=0;//初始化学生计数器n为0。
p1=p2=(struct Student*)malloc(LEN);
//开辟新单元，动态分配一个Student结构体大小的内存块,并将其地址赋给p1和p2。
scanf("%d,%f",&p1->num,&p1->score);//从标准输入读取一个长整型和一个浮点型数据，分别存储到p1指向的结构体的num和score成员中。
head=NULL;// 将head指针初始化为NULL,表示刚开始链表为空。

while(p1->num! =0)//进入一个循环,直到用户输入学号为0。
{
n=n+1;//每读取一个学生的信息，学生计数器n加1。
if(n==1) head=p1;//如果是第一个学生,将head指针指p1。head指针指向p1后就不会再变化
else p2->next=p1;//否则,将上一个学生结点的next指针(p2->next)指向当前学生结点。
p2=p1;//更新p2指针，使其指向当前结点，为下一次循环做准备。

p1=(struct Student*)malloc(LEN);//为下一个学生结点分配内存，并更新p1指针。
每要输入新的数据，p1就得动态分配一个Student结构体大小的内存，而p2因为一直动，所以不需要

scanf("%d,%f",&p1->num,&p1->score);//提提示用户输入下一个学生的学号和成绩，并将这些信息存储到新分配的结点中。

}
//循环结束
p2->next=NULL;//将最后一个学生结点的next指针设置为NULL,表示链表结束。
return(head);//返回链表的头结点指针head
}

int main()
{
struct Student *pt;
pt=creat();
//函数返回链表第一个结点的地址（head指针）
printf("\nnum:%d\nscore:%5.1f\n",pt->num,pt->score);
//输出第1个结点的成员值
return 0;
}
```
在这个程序中head指针、p1指针、p2指针分别的作用
1. **head指针**：
    
    - `head`指针用于指向链表的头结点。在链表中，头结点是链表的第一个元素，它通常包含链表的第一个数据项。
    - 在这个程序中，`head`指针最初被初始化为`NULL`，表示链表为空。**当第一个学生的信息被输入时**，`head`指针被设置为指向这个新创建的节点。
    -
    - 最终，`head`指针指向链表的开始，可以通过它来遍历整个链表。
2. **p1指针**：
    
    - `p1`指针用于动态创建新的结点，并接收用户输入的学生信息（学号和成绩）。
    - 在循环中，`p1`指针首先被用来分配内存以创建一个新的学生结点，然后接收输入的学生信息。
    - 每次循环，`p1`指针都会被更新，指向最新创建的结点。
3. **p2指针**：
    
    - `p2`指针用于在链表中维护前一个结点的引用。它帮助在创建新结点时正确地链接链表。
    - 在循环的开始，`p2`指针被设置为指向`p1`（当前结点），这样在下一次循环时，就可以将`p1`（新的当前结点）链接到`p2->next`（前一个结点的`next`指针）。
    - 在循环结束时，`p2->next`被设置为`NULL`，这表示链表的结束。

### 3.4.1 输出链表（查）
**核心思想**
新建立一个指针p，为struct Student类型，用于移动输出
然后那个head指针开始，每输出一个，p就用（p=p->next）语句，指向下一个结点，直到指针p指向NULL
```c
void print(struct Student*head)//定义print函数

{

	struct Student*p;//在函数中定义struct Student类型的变量p
	printf("\nNow,These %d records are:\n",n);
	p=head;//使p指向第1个结点

	if(head!=NULL)//若不是空表
		do
		{
			printf("%ld %5.1f\n",p->num,p->score); 
			//输出一个结点中的学号与成绩
			p=p->next;//p指向下一个结点，相当于数组中p++的操作
		}while(p!=NULL);//当p不是"空地址"
}
```
### 3.4.2 删除链表某个结点，学号为6（删）
**核心思想**
![[Pasted image 20240528190614.png]]
 现在p一直在运动，直到检测到p->num=6，此时要把p敲除
 p1是p前一个结点，p2是p后一个结点
 建立p1->next=p2
 而p2又恰好为p->next
 那么式子变为p1->next=p->next,此时要解决的就是求出p1
 通过遍历来解决这个问题,，加上一个一直移动的指针
```c
struct Student*p1;
while(p->next ! = 6){
p1=p;
}
```



### 3.4.3 增加某个结点，学号为6（增）
**假设学号是从小到大排**

![[Pasted image 20240528191443.png]]


现在先开辟一处结构体地址p1，输入要增加的数据p1->num=6;
再开辟一个结构体指针p，开始从head指针开始移动
前面的p->num都<6,不管。**当p->num > 6**时，遍历停止
我们要做的就是
```
p3->next = p1;
p1->next = p;
```
p,p1我们都知道，主要是怎么求出p的前一个结构体的地址p3
同样[[#^34995f]]
```c
struct Student*p3;
while(p->next < 6){
p3=p;
```

### 3.4.4 修改某个结点的数据（改）
**核心思想**
直接找到那个点，然后改p->num和p->score

# 链表总程序
```c
#include <stdio.h>
#include<stdlib.h>

struct Student{
	int num;
	float score;
	struct Student*next ;
}; 
int n;//external变量，全局变量

struct Student* creat(){
	struct Student* head,*p1,*p2;
	n = 0;
	p1=p2=(struct Student*)malloc(sizeof(struct Student));
	scanf("%d %f",&p1->num,&p1->score);
	head=NULL;
	while(p1->num!=0){
		n = n+1;
		if(n==1){
			head=p1;
		} 
		else{
			p2->next=p1;
		}
		p2=p1;
		p1=(struct Student*)malloc(sizeof(struct Student));
		scanf("%d %f",&p1->num,&p1->score);
	}
	p2->next=NULL;
	return head;
} 
void print(struct Student*head){
	struct Stduent*p;
	p=head;
	if(p!=NULL){
		do{
			printf("%d %f",p->num,p->score);
			p=p->next;
		}while(p!=NULL);
	}
} 
int main(){
	struct Student*p;
	p=creat();
	print(p);
	return 0;
} 
```

# 四、自定义数据类型的名字(typedef)
C 语言提供了一个叫做 typedef 的功能来声明一个已有的数据类型的
比如：
typedef int Length;
使得 Length 成为 int 类型的别名。
这样 Length 这个名字就可以代替int出现在变量定义和参数声明的地方了
```c
typedef int Length; // Length就等价于int类型
typedef char*[10] Strings; // Strings 是10个字符串的数组的类型

typedef struct node{
int data;
struct node *next;
} aNode;
或
typedef struct node aNode; // 这样用aNode 就可以代替struct node

```

# 五、联合（union）
```c
union AnElt {
int i;
char c;
} elt1, elt2;
elt1.i = 4;
elt2.c =’a’;
```
成员是int i或者char c，两者不能同时存在
**sizeof(union ...) = sizeof(每个成员的最大值)**

存储：
•所有的成员共享一个空间
• 同一时间只有一个成员是有效的
• union的大小是其最大的成员
