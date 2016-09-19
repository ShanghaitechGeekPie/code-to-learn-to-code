// C/C++的注释以井号开头

// 也可以用/* */对

/* 比如这样
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          佛祖保佑       永无BUG
*/


/////////////////////////////////////////////////
//// 1. 数据类型
//// 变量接受字母数字下划线，但是不允许数字开头
/////////////////////////////////////////////////

// 整型
int a;
unsigned ua;
long long b;
unsigned long long ub;

a = 10;     // 十进制10
a = 010;    // 八进制10，即十进制8
a = 0x10;   // 十六进制10，即十进制16

a = -1;     // 默认为signed类型，可以接受负数
ua = 1;     // unsigned类型只能是整数

b = -9223372036854775800;  // long long 类型可以有更大的数据范围

// 实型
float c;
double d;

c = 1.0;
c = 1.f;        // 对于一个整数可以用.f表示这是一个实型
c = 1e2;        // 科学计数法
c = -1.22e-12;  // 可以有符号

d = 1.6E+300;    // double 范围更大

// 字符型
char e;
e = 97;         // ASCII编码，char本身也是一种范围很小的整数
e = 'a';        // 单引号括起来的字符可以转化为ASCII编码，与上句等价
e = e - 32;     // ASCII码表可查，e此时为'A'
e = e + ' ';    // ' ' space为32号，e此时为'a'
e = '\n';       // 常见\转义的特殊字符\t \n \r等也可以表示

// 运算
a = 1 + 1;      // 加法
b = 10 - 2;     // 减法
ua = 10 * 10;   // 乘法
ub = 11 % 5;    // 取余 ub = 1

a = 123 / 12;    // 整姓之间的除法会变成取整运算 a = 10
c = 123 / 12;    // 即便是float也是如此 c = 10.f
c = 123.0 / 12;  // 只要有除数或者被除数是实型就可以了 c = 10.25
c = (float)123 / 12; // 也可以用强制转换

c = a + 1.3;     // 这时则不必强制转换 c = 11.3

// 位运算 比较运算 逻辑运算 与Python相同


/////////////////////////////////////////////////
//// 2. 流程控制
/////////////////////////////////////////////////

a = 1002;
ua = 1003;
b = 1002;
ua = 1003;

if (a == b) {
  // 相等
} else {
  // 不相等
}

if (a != ua) {
  // 不相等
} // else 可省略

switch (a) {
  case 1:
    b = 1;
    break;
  case 2:
    b = 2;
    break;
  case 1002:
    b = 3;
    break;
  default:
    b = 4;
    break;
}
// b = 4

switch (a - 1) {
  case 1001:
    b = 1;
  case 1002:
    b = 2;
  case 1003:
    b = 3;
  // default可省略
}
// b = 3， 因为没有break

a = 3;
b = 100;
for (int i = a; i < b; i++) {
  // will be called 97 times. i will be 3,4,5...,97,98,99
}

for (int i = a + 1; i < b; i += 2) {
  // will be called 48 times. i will be 4,6,8...,96,98
}

int i = a + 1;
while (i < b) {
  // will be called 48 times. i will be 4,6,8...,96,98
  // 与上第二个for循环等价

  i += 2; // 不要忘了加变量修改
}

i = a + 1;
do{
 // will be called 48 times. i will be 4,6,8...,96,98
 // 与上第二个for循环等价

 i += 2; // 不要忘了加变量修改
} while (i < b);


for (;;) { // for 参数可以为空，也可部分为空，产生死循环
  break;    // break跳出循环
  continue; // continue跳出当次循环
}


/////////////////////////////////////////////////
//// 3.scanf printf
/////////////////////////////////////////////////

// scanf

scanf("%d", &a);
// 输入1<回车>
// a = 1

scanf("%x", &a);
// 输入F<回车>
// a = 16

scanf("%d %d %d", &a, &ua, &b);
// 输入1 2 3<回车>
// a = 1; ua = 2; b = 3;

// 输入1<回车>
// 输入 2 3<回车>
// a = 1; ua = 2; b = 3;

scanf("%f", &c);
// 输入97<回车>
// c = 97.0

// 输入1.2E2<回车>>
// c = 120.0

scanf("%c", e);
// 输入9<回车>
// e = 57 = '9'

scanf("%c", e);
scanf("%c", e);
// 输入97<回车>
// 第一句 e = 57 = '9' 此时7尚未被读入
// 第二句 e = 55 = '7'

scanf("%d", e);
// 输入97<回车>
// e = 97 = 'a'

// printf

a = 1;
printf("%d\n", a);
// 打印1<换行>

a = 1;
printf("%d", a);
printf("%d\n", a);
// 打印11<换行>
// 第一句没有换行符，所以第二句紧接着输出

a = 9;
printf("%o\n", a);
// 打印11<换行>

a = 15;
printf("%x\n", a);
// 打印F<换行>

c = 3.1415926;
printf("%f\n", c);
// 打印3.141593
// 默认最大小数6位，四舍五入

c = 3.1415926;
printf("%.2f\n", c);
// 打印3.14

c = 3.1415926;
printf("%6.2f\n", c);
// 打印  3.14

c = 3.1415926;
printf("%-6.2f\n", c);
// 打印3.14  <两个空格>

e = 97;
printf("%d\n", e);
// 打印97

e = 97;
printf("%c\n", e);
// 打印a
