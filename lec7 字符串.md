# 1.字符数组

^8114ab

`char word[]={‘H’, ‘e’, ‘l’, ‘l’, ‘o’,‘!’};
这不是c语言的字符串，因为不能用字符串的方式计算，结尾不是'\0'
![[Pasted image 20240508210448.png]]
# 2.字符串
`char word[] = {‘H’, ‘e’, ‘l’, ‘l’, ‘o’,‘!’,’\0’}`
`char word[]="Hello!"`
`char* word="Hello!"`//word指向一个字符串
![[Pasted image 20240508210435.png]]
* 以0（整数0）结尾的一串字符
	0或`’\0’`是一样的，但是和’0’不同 
* 0标志字符串的结束，但它不是字符串的一部分
* 计算字符串长度的时候不包含这个0[[lec7 字符串#7.1 strlen]]
* 字符串以**数组**的形式存在，以**数组或指针**的形式访问（指针是指向数组）
* string.h 里有很多处理字符串的函数

# 3.字符串变量
### 3.1 一些输出的区别
`char *ps="C Language"`的顺序是：
1.分配内存给字符指针；
2.分配内存给字符串；
3.将字符串首地址赋值给字符指针；
**ps是一个字符串指针，是一个字符串变量**，代表的是**字符串首字母”C“的地址**
并且`*ps`只是指向一个字符（首字母）
```c
int main(){
char *a = "bcd";
printf("%c",*a); //输出：b
printf("%c",*(a+1)); //输出：c
printf("%s",a);//s输出：bcd
}
```
^198993

### 3.2 字符指针和字符数组
`char* s="Hello";`
`char* s2="Hello";`
"Hello"是一个字符串常量
s是一个字符串指针，初始化指向一个字符串常量
然而，用这种指针形式，”Hello“常量是只读模式，**指针只能指向它，无法改变它**（即只能读，不能写入）`const char* s="Hello"只能改变s，无法改变*s`
并且，s和s2是指向同一个”Hello“常量 
**不能进行s[0]='K'、s[1]='B'的操作，但可以进行s=“nihao”！（直接改变指针的指向）**

如果要修改（写入）字符，应该用字符数组
`char s[]="Hello";`表示**这个常量就在这，而不是指向的关系**
**可以进行s[0]='K'、s[1]='B'，但无法进行s=“Hello”（数组只能在初始化时一次性赋多个值，后面要修改只能一个一个赋值，因为后面s指的是第一个字符的地址，不能赋一整个字符串的地址上去！）**[[lec5 数组#^6488a9]]
![[Pasted image 20240522005320.png]]

### 3.3 char* 是不是就是代表字符串？

^2b4b8d

字符串可以表示为`char*`的形式
但`char*`不一定是字符串
`char*`本意是指向字符数组，只有当字符数组最后面有结尾的0时，才能说它指的是字符串
# 4.字符串常量
”Hello“：这样的形式称为字符串常量
这个字符数组的长度为**5+1**
但用strlen函数计算字符串长度时，不包括结尾的0
# 5.字符串运算
### 5.1 字符串赋值(这个用字符数组无法操作)

^42109c

```cpp
char *t="title";
char *s;
s=t;
```
并没有产生新的字符串，只是让指针s指向了t所指的字符串，对s的任何操作就是对t做的
注意，如果是这样操作的话，s与t指向同一个东西，你对`*t`的所有操作也会使得`*s`改变，因此这样并不能称为复制
```cpp
//复制字符串
char* copy(const char* s) {
    int length = strlen(s);
    char* copy = new char[length + 1]; // +1 for null terminator
    
    // Copy each character using pointers
    const char* src = s;
    char* dest = copy;
    while (*src != '\0') {
        *dest = *src;
        src++;
        dest++;
    }
    
    *dest = '\0'; // Add null terminator to the copied string
    
    return copy;
}
```



```c
char t[]="title";
char s[];
s=t;//必然报错，因为t是指针常量，指向字符数组第一个字符的地址，无法进行字符串的整体赋值
t = "hello";//也会报错，因为t代表的是第一个字符的指针常量
```
### 5.2 字符串输入输出
##### 5.2.1 scanf不安全的输入
```c
char string[8];
scanf("%s",string);//string名本身代表的就是地址
printf("%s",string);//用%s，输出的就是字符串，用*string输出的是第一个字符

```
scanf读入一个单词（到空格、tab四个空格或回车为止）
scanf是不安全的，因为不知道要读入的数据为多长 ，如果超过7个字符超过字符数组的限制会报错
##### 5.2.2scanf安全的输入
`scanf("%7s",string);`
在%和s之间的数字表示最多允许读入的字符的数量，这个数字应该比数组的大小小一
##### 5.2.3常见错误：使用指针时必须先初始化！！！

^33bfaa

```c
char *string;//这样一定会报错！因为指针没有初始化
scanf("%s",string);

改成：
char *string = "Hello";
scanf("%s",string);
```
```c
char string[8];//使用数组可以不初始化
scanf("%s",string);
```
### 5.3 空字符串
```c
char buffer[100]="";
buffer[0]='\0'这是一个空字符串

char buffer[]=""
这个字符数组的长度只有1
```
## 5.4 字符串数组 考试会考

^4b6275

1. `char **a`
	a是一个指针，指向char*（一个字符指针：指向字符数组【当字符数组结尾有\0时指向字符串】）[[lec7 字符串#3.3 char* 是不是就是代表字符串？]]
2. `char a[][]`
	a是一个二维数组，第二个维度的大小不知道，不能编译
3. `char a[][10]`（字符串数组）
	a是一个二维数组，a[x]是一个char*(可以往里面储存字符串)，然后一个字符串长度为9个字符
4. `char *a[]`
	a是一个一维数组，a[x]是一个char*.本质为一个**指针数组** [[lec6 指针#3.2.2 数组指针和指针数组]]，数组里存储着`char*`指针，每一个`char*`指向一个字符串 ^eb1b23

![[Pasted image 20240604221827.png]]
辨析：字符串数组和字符数组
字符数组是`char a[]`，里面存放着字符[[#^8114ab]]
然后字符串数组是`char a[][10]`里面存放着字符数组char*，一个字符数组最大是10个字符

# 6.字符输入输出
## 6.1 scanf
`scanf读到\n停止，不会读入\n`
## 6.2 %s
%s的作用是通过*地址*定位到字符或字符串
```c
#include<stdio.h>
int main(){
	char a[6]="hello";
	printf("%s",&a[0]);=printf("%s",a);
	return 0; 
} 
```
# 7.标准库中的字符串函数(重要)

^1eb9e1

##  string.h库
• strlen
• strcmp
• strcpy要先`char*a=(char*)malloc(strlen(b)+1)`
• strcat
• strchr
• strstr
### 7.1 strlen
原型：`size_t strlen(const char *s);`
返回s的字符串长度（不包括结尾的0）
使用：`int a = strlen(字符串)`
### 7.2 strcmp
原型：`int strcmp(const char *s1, const char *s2);`(返回整形)
比较两个字符串，返回：
```
0:s1==s2
>0:s1>s2
<0:s1<s2
```
使用：`int a = strcmp(字符串1，字符串2)`
在比较字符串时,设置一个计数器,从零开始,一直循环到最短的那个字符结束,一位一位进行比较,
如果 字符串1是字符串2的前m位,例如 abcd 与abcdef 比较, 则 字符串1<字符串2. 原因是,到第5位时,字符串1的ASCII值是0,而字符串2的ASCII值为'e',即十进制的101,当然是字符串2大了. 具体到 cds和aesoqd 从第一位开始,'c'和'l'比较,当然是'c' < 'a'了,所以,"cds" > "lesoqd"

### 7.3复制一个字符串strcpy
使用：
```c
char *dst = (char*)malloc(strlen(src)+1);//因为要包括\n所以要+1
strcpy(dst, src);
```
### 7.4 连接两个字符串strcat
原型：`char * strcat(char *restrict s1, const char *restrict s2);`
把s2拷贝到s1的后面，接成一个长的字符串
返回s1
s1必须具有足够的空间
(strcpy和strcat的安全问题考试不考)
### 7.5 字符串中找字符
原型：
```
char * strchr(const char *s, int c);//正向
char * strrchr(const char *s, int c);//逆向
```
返回一个指针`char*`指向**你想要的那个字符及后面内容的地址**
```c
char s[]="Hello";
char *p = strchr(s,'l');
printf("%s\n",p);//输出llo
p = strchr(s,'l');//寻找第二个
printf("%s\n",p);//输出lo
```