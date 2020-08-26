# JavaSE知识
[TOC]
## 第一章
### 输出java语句
```java
public class HelloJava {
    public static void main(String[] args) {
       // 输出HelloWorld
       System.out.println("Hello  World");
    }
}
```
### 交换数值
```java
public class OperateDemo {
    public static void main(String[] args) {//如果少了 String[] args，程序则不能执行
       OperateDemo od=new OperateDemo();
       od.changeValue_1(1,2);
       od.changeValue_2(1,2);
    }
    //交换两数的值
    public  void changeValue_1(int a,int b){
       int temp;
       temp=a;
       a=b;
       b=temp;
       sop(a,b);
    }
    //交换两数的值
    public  void changeValue_2(int a,int b){
       a=a^b;
       b=a^b;// (a^b)^b;
       a=a^b;// a^(a^b);
       sop(a,b);
    }
    public void sop(int a,int b){
       System.out.println("交换后：a=="+a+"   b=="+b);
    }
}
```
### 获取数字的十六进制变现形式:
```java
public class OperationDemo_2 {
    public static void main(String[] args) {
       //System.out.println(Integer.toBinaryString(60));//111100
       int num =60;
       //获取60的最低4位，通过&15的方式；
       int n1 =num & 15;
       System.out.println(n1>9 ? (char)(n1-10+'A'):n1);
       //右移4位
       int temp=60>>>4;
       //获取temp的最低4位，通过&15的方式；
       int n2=temp & 15;
       System.out.println(n2>9?(char)(n2-10+65):n2);
       System.out.println((char)(n1-10+'A'));
    }
}
public class VarDemo_1 {
    public static void main(String[] arg){
    //定义变量的格式：
    //数据类型  变量名=初始化值;
    /*  int x=2;
       sop(x);
       short s=12;
       sop(s);
       long l=12243;*/
    /*  * 什么时候定义变量？
        * 当数据不确定的时候，需要对数据进行存储时
        * 就定义一个变量来完成存储动作。 */
    //类型转换
       byte b=3;
       b = (byte) (b + 2);
       sop(b+1+'A');//答案为 71   因为‘A’是65 , 字符在ASCll中都有对应的数字
      
       //转义字符，通过\ 来转变后面的字母或者符号的含义
      /*  \n:换行
          \b:退格，相当于backspace
          \r:回车window系统中，回车符是由两个字符来表示的\r\n
          \t:制表符，相当于tab键
          注意： char 里面可以装汉字 */
       short s=4;
       //s=s+5;  这句话编译失败，这个s会做一个强制转换动作，（四位赋值给五位），导致精度缺失
       s+=5;//这句话编译通过，内部会做一个转换动作
      /*  运算符； ^:相同为假，不同为真。  
          &和&&：&：无论左边是真是假，右边都要运算
                &&：当左边是假时，右边不运算，效率高。
          >>:最高位是什么有原有数据的最高位而定，是0补0，是1补1；
          >>>:无论最高为是什么，右移后，都用0补   */
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
## 第二章：语句
### 一：if语句
```java
public class IfDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       int x=3;
       if(x>2){//如果if后面只有一条语句，可以省略大括号；
           System.out.println("yes");
       }else{
           System.out.println("over");
       }
       // x=(x>2)?100:200;
    /* if else 语句 简写格式 ：变量 = （条件表达式）？表达式1：表达式2；
    三元运算符：
        好处：可以简化if else语句
        弊端：因为是一个运算符，所以运算完必须有一个结果
        int a=3;
       if(a>1)
           System.out.println("A");
       else if(a>2)
           System.out.println("B");
       else if (a>3)
           System.out.println("C");
       else
           System.out.println("D");
       System.out.println("over");//结果是  A  over
       if(a>1)
           System.out.println("A");
       if(a>2)
           System.out.println("B");
       if(a>3)
           System.out.println("C");
       else
           System.out.println("D");
       System.out.println("over"); // 结果是A B D over   */
    }
}
public class IfText {
    public static void main(String[] args) {
       //需求1：根据用户定义的树枝不同。打印对应的星期英文。
       int num = 1;
       if(num==1)
           System.out.println("monday");
       else if (num==2)
           System.out.println("tuesday");
       //需求2：根据用于指定的月份，打印该月份所属的季节；春  夏  秋  冬
       int x = 6;
    /*  if (x==3|| x==4||x==5)
           System.out.println(x+"月    是   春季");
       else if (x==6||x==7||x==8)
           System.out.println(x+"月   是  夏季");
       else if (x==9||x==10||x==11)
           System.out.println(x+"月   是  秋季");
       else if (x==12||x==1||x==2)
           System.out.println(x+"月   是  冬季");
       else
           System.out.println(x+"月  是错误的");  */ 
       //  代码 简化：
       if (x>12||x<1)
           System.out.println(x+"月  是错误的");
       else if(x>=3&&x<=5)
           System.out.println(x+"月   是  春季");
       else if (x>=6&&x<=8)
           System.out.println(x+"月  是   夏季");
       else if(x>=9&&x<=11)
           System.out.println(x+"月  是  秋季");
       else
           System.out.println(x+"月  是  冬季");
    }
}
```
### 二：Switch语句
```java
import java.util.Scanner;
public class SwitchDemo {
    public static void main(String[] args) {
/* 特点:1，被选择的表达式类型只有四种  byte short  int char 
        2,case语句没有顺序
        3，switch结束方式   break 、 ｝结束
    如果值不多的情况下，而且是上面四种类型，用switch，其他情况用if
    需求2：根据用于指定的月份，打印该月份所属的季节；春  夏  秋  冬
       //输入一个数字  */
       System.out.println("请输入一个月份，并按回车键结束");
       Scanner s=new Scanner(System.in);
       int num =  s.nextInt();
       switch (num){
       case 12:
       case 1:
       case 2:
           System.out.println("冬季");break;
       case 3:
       case 4:
       case 5:
           System.out.println("春季");break;
       case 6:
       case 7:
       case 8 :
           System.out.println("夏季");break;
       case 9:
       case 10:
       case 11:
           System.out.println("秋季");break;
       default:
           System.out.println("您输入的月份是错误的");
       }  
    }
}
```
### 三：while语句
```java
public class WhileDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       /* 
       while（条件表达式）｛
           循环体（执行语句）；
       ｝
       //先判断条件在执行循环体
       int x=1;
       while(x<=10){
           System.out.println("x="+x);
           // x++;
           x+=2;
       }  */
       //先执行循环体在判断条件
       int x=1;
       do{
           System.out.println("x="+x);
           x++;
       }while(x<3);  
    }
}
```
### 四：for语句
```java
public class ForDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
/*  for(初始化表达式;循环条件表达式;循环后的操作表达式)｛
        执行语句;
    ｝
    执行顺序：
        先执行  初始化表达式（才开始在内存中开辟空间） 
        再执行  循环条件表达式  
        再执行  执行语句 
        在执行  循环后的操作表达式
        再执行  循环条件表达式  
        再执行  执行语句 
        在执行  循环后的操作表达式
         */
       for (int x=0;x<3;x++){
           System.out.println("x =  "+x);
       }
       // System.out.println("x="+x);
       int y=0;
       while(y<3){
           System.out.println("y =  "+y);
           y++;
       }
       System.out.println("y  =  "+y);
/*  1，变量有自己的作用域。对于for来讲：如果用于控制循环的增量定义在for语句中，
           那么该变量只在for语句内有效；for语句执行完毕，该变量在内存中被释放。
    2，for和while可以互换。如果要定义循环增量。用for更为合适
    总结：什么时候用循环结构？
         当对某些语句执行很多次是，就用循环结构。 */
    }
}
public class ForText {
    public static void main(String[] args) {
       int x=1;
       for(System.out.println("A");x<3;System.out.println("C")){
           System.out.println("D");
           x++;
       }
/*  无限循环形式:一 ： for(;;){}
              二 ：  while(true){}   */
    }
}
public class ForText_2 {
    public static void main(String[] args) {
       //要求： 获取1~10的和，并打印
       int sum=0;
       for(int x = 1; x<=10;x++){
           sum+=x;
       }
       System.out.println(sum);
       //需求2：1~100之间7的倍数的个数并打印
       int sum1=0;
       for(int a=1;a<=100;a++){
           if(a%7==0){
              sum1++;
              System.out.println("a  ="+a);
           }
       }
       System.out.println(sum1);
    }
}
public class ForForText {
    public static void main(String[] args) {
       /*
       for(int x=0;x<3;x++){
           for(int y=0;y<4;y++){ 
              System.out.print("*");
           }
           System.out.println();
       }
     对于嵌套循环， 外循环控制行数，内循环控制每一行的列数 
打印如图
    *****
    ****
    ***
    **
    *  
       for(int x = 0;x<5;x++){
           for(int y=0;y<5-x;y++){
              System.out.print("*");
           }
           System.out.println();//给每次的内循环换行
       }
 打印九九乘法表
        1*1=1
        1*2=2  2*2=4
        1*3=3  2*3=6  3*3=9   */
       for(int x=1;x<=9;x++){
           for(int y=1;y<=x;y++){
              System.out.print(y+"*"+x+"="+x*y+"\t");//加上制表符对齐每一列 
           }
           System.out.println();
       }
    }
}
public class ForForText_2 {
    public static void main(String[] args) {
/*  练习:
 ----*
 ---* *
 --* * *
 -* * * *
 * * * * *            */    
       for(int x=0;x<5;x++){
           for(int y=0;y<4-x;y++){
               System.out.print("-");//控制左边的“-”
           }
           for(int z=0;z<=x;z++){
              System.out.print("* ");//控制右边的“* ”，发现“*”之间带有空格所以要加一个空格
           }
           System.out.println();//换行   
       }
    }
}
```
### 五：其他类
```java
public class OtherDemo {
    public static void main(String[] args) {
       for(int x=0;x<3;x++){
           break;//break语句跳出当前循环，并且不执行break下面的语句
       }
       //continue：只能作用于循环结构   特点：结束本次循环，继续下一次循环
       for(int x=0;x<3;x++){
           if(x%2==1)
              continue;
           System.out.println(x);
       }
/*  记住：1，break和continue语句作用范围
        2，break和continue单独存在时，下面可以有任何语句，因为执行不到 */
    }
}
```
## 第三章：函数
### 函数的定义
```java
import java.util.Scanner;
public class FunctionDemo {
    public static void main(String[] args) {
       //需求：任何一个数乘以三加五的结果
       System.out.println("请输入一个数：");
       Scanner s =new Scanner(System.in);
       int x=s.nextInt();
       System.out.println("这个数乘以三加五的结果是："+(x*3+5));
       // getResult(x);如果这样写的话，程序运行了，但是你没有对其进行任何操作，
       // 可以用输出语句把程序运行的 结果打印在控制台上
       System.out.println(getResult(x));    
    }
/*  发现，以上代码可以定义成一个独立的功能代码块，方便以后使用。
     java中对功能的定义是通过函数的行驶来体现的。
需要定义功能。完成一个整数的*3+5的运算，并打印结果
     1，先明确函数定义的格式
           修饰符  返回值类型 函数名（参数类型 形式参数1，参数类型 形式参数2）｛
               执行语句；
               return 返回值；
           ｝
           返回值类型：函数运行后的结果的数据类型。
           参数类型：是一个形式参数类型。
           形式参数：是一个变量，用于存储调用韩寒苏是传递给函数的实际参数
           实际参数：传递给形式参数的具体数值
           return：用于结束函数.
           返回值：该返回值给调用者用
     2，特点1，函数可以将功能代码块进行封装
           2，便于对该功能进行复用
           3，函数只有被调用才会执行
           4，函数的出现提高的代码的复用性
           5，对于函数没有家具体的返回值的情况，返回值类型用关键字void 表示
        那么该函数中的return 语句如果在最后一行可以省略不写
     注意：函数中只能调用函数，不可以在函数内部定义函数，定义函数时，函数的结果应该返回给调用者，交由调用者处理*/
    public static int getResult(int num){
       return num*3+5;
    }
}
import java.util.Scanner;
public class FunctionDemo2 {
  
    public static void main(String[] args) {
       System.out.println("运算后的结果是："+getSum());
       System.out.println("请输入两个数，用空分开");
       Scanner s=new Scanner(System.in);
       int x=s.nextInt();
       int y=s.nextInt();
       System.out.println("您输入的两个数的和是："+getSum2(x,y));
       System.out.println("这两个数是否相等?   "+compare(x,y));
       System.out.println("这两个数较大者是?   "+getMax(x,y));
    }
/* 如何定义一个函数呢？
     1，既然函数是一个独立的功能，那么该功能的运算结果是什么先明确;因为是在明确函数的返回值类型
     2，在明确该定义功能的过程中是否需要未知的内容参与运算，因为是在明确函数的参数列表（参数的类型个和个数）
    需求1：定义一个功能，完成3+4的运算，并将结果返还给调用者
    思路：运算结果：是一个整数   （明确函数的返回值类型）
         运算过程中不需未知参数参与运算 （明确参数的类型，和个数）
         需要将运算结果返还给调用者 */
     public static int getSum(){
        return 3+4;
     }
/*  需求 2：定义一个函数，完成调用者指定的数的和；
     思路：运算的结果是一个和；（明确返回值类型）
           运算过程中   需要两个未知参数参与运算（明确参数的类型和个数）
           需要将运算的结果返回给调用者      */       
     public static int getSum2(int a,int b){
        return a+b;
     }
 /* 需求判断两个数是否相同
    思路：运算的结果是一个boolean值，运算过程中需要未知参数参与运算，需要将运算的结果返回给调用者   */
     public static boolean compare(int a,int b){
       /* 
         if(a==b)
            return true;
         else  //else可以省略不写
            return false;
       或者可以用三运算符写代码
         return  (a==b)?true:false;*/
         return a==b;//或者直接这样写，a==b运算的结果本来就是true，false
     }
/*  需求：定义一个功能，对两个数进行比较，获取最大的数
    思路：运算的结果是 一个数；运算过程中需要 两个参数参与运算；运算的结果返还给调用者*/
  
     public static int getMax(int a,int b){
     /*  方法一：先用if代码
        if(a>b)
            return a;
        return b;
        方法二：   */
        return (a>b)?a:b;
     }
     //注意：没有返回值类型的函数，不能直接打印
}
public class FunctionText {
    public static void main(String[] args) {
       daYinJuXing(5,6);
       chengFaBiao(9);
    }
/* 需求：1，定义一个功能，用于打印矩形
         2，定一个打印99乘法表功能的函数
1，定义一个功能，用于打印矩形
思路： 运算的结果是 打印一个矩形
       运算过程中需要两个未知参数参与运算    */
    public static void daYinJuXing(int a,int b){
       for(int x=0;x<a;x++){
           for(int y=0;y<b;y++){
              System.out.print("*");
           }
           System.out.println();
       }
    }
/* 2，定一个打印99乘法表功能的函数
    思路：函数的运算结果是打印一个99乘法表，运算过程中不需要未知参数参与运算       */
    public static void chengFaBiao(int a){
       for(int x=1;x<=a;x++){
           for(int y=1;y<=x;y++){
              System.out.print(y+"*"+x+"="+x*y+"\t");//不要忘加"\t"
           }
           System.out.println();
       }
    }
}
```
### 函数的重载
```java
public class FunctionOverload {
/* 什么时候用重载？
当月定义的功能相同，但参与运算的未知内容不同那么，这是就定义一个相同的函数名称以表示功能，方便阅读，而通过列表参数的的不同来区分多个同名函数
    注意：1，重载和返回值类型没有关系，
          2，参数列表是有顺序的，参数的顺序不同也属于重载
          3，重载的时候，是不允许函数的其他条件相同，只有返回值类型不同的函数存在的 */
    public static void main(String[] args) {
       int x=sum(4,6);
       System.out.println(x);
       int y=sum(4,6,8);
       System.out.println(y);
       chengFaBiao(9);
    }
    //定义一个加法，获取两个数的和
    public static int sum(int a, int b){
       return a+b;
    }
    //定义一个加法，获取三个数的和
    public static int sum(int a, int b,int c){
       return a+b+c;
    }
    //定义一个乘法表，指定几就打到几
    public static void chengFaBiao(int a){
       for(int x=1;x<=a;x++){
           for(int y=1;y<=x;y++){
              System.out.print(y+"*"+x+"="+x*y+"\t");//不要忘加"\t"
           }
           System.out.println();
       }
    }
}
```
## 第四章：数组
### 一维数组
```java
public class ArrayDemo {
/* 数组的概念：同 一种数据 类型的集合。其实数组就是一个容器。
好处:可以自动给数组中的元素从0开始百年好，方便操作这些元素
格式：元素类型[] 数组名=new 元素类型[元素个数或数组长度]
     int[] x=new int[3];
    x存放在栈内存中，new出来的实体是在堆内存中的，每个元素都有对应的地址值   
数组的几个特点： 地址值   初始化值  垃圾回收机制  */
     public static void main(String[] args) {
       //定义一个长度为3的数组，元素初始化值为0
       int[] x=new int[3];
       //定义一个长度为3 的数组，并给元素赋初始化值,并不指定数组的长度。
       int[] y=new int[]{1,3,4,5};//数组的长度为4，数组角标最大值是3
       System.out.println("x="+x[1]);
       System.out.println("y="+y[6]);//出现ArrayIndexOutOfBoundsException 
    }
}
public class ArrayDemo2 {
    public static void main(String[] args) {
    /*  对数组的操作：获取数组中的元素    */
       int[] arr= new int[]{1,2,3,4};
       int sum=0;
       for(int x=0;x<arr.length;x++){
           if(x==arr.length-1){
               System.out.println("arr["+x+"]="+arr[x]);
           }else{
               System.out.print("arr["+x+"]="+arr[x]+",");
           }
           sum+=arr[x];//求和
       }
       System.out.println(arr);//[I@2a139a55   分解后；[数组  I数组类型   @  2a139a55数组地址值
       System.out.println("sum="+sum);
    }
}
/*  练习：求数组中的最大值
思路:1,获取最大值需要进行比较，每一次比较都会有一个较大的值。因为该值不确定，通过一个变量进行临时存储。
     2，让数组中的每一个元素都和这个变量记录的较大值进行比较。如果大于了变量中的值，就用该变量值记录较大值
     3，当所有元素都比较完成那，那么该变量中存储的的就是数组中的最大值了。
步骤:1，定义变量。初始化为数组中任意一个元素即可。
     2，通过循环语句对数组进行遍历。
     3，在变量过程中定义判断条件，如果遍历到的元素比变量中的元素大，就赋值给该变量。
需要定义一个功能来完成。以便提高复用性。
    1，明确结果，数组中的最大元素 int 。
    2，未知内容：一个数组。int[]    */
public class ArrayText {
    public static void main(String[] args) {
       int[] arr=new int[]{1,2,3,41,5,6};
       int x=getMax(arr);
       System.out.println("数组中的最大值是："+x);
    }
    //获取最大值
    public static int getMax(int[] a){
       int max=a[0];
       for(int x=1;x<a.length;x++){
           if(max<a[x]){
              max=a[x];
           }
       }
       return max;
    }
/* 获取最大值的另一种方式。
   可不可一将临时变量初始化为0？是可以的，将0作为角标来看待就可以 */
    public static int getMax_2(int[] a){
       int max=0;
       for(int x=1;x<a.length;x++){
           if(a[max]<a[x]){  //获取最小值，只要把<改成>就可以
              max=x;
           }
       }
       return a[max];
    }
/*  获取double类型的数组的最大值。因为功能一致，所以定义相同的函数名称，以重载的形式存在
    public static double getMax_3(double[] a){
       double max=0.00;
       for(double x=1;x<a.length;x++){
           if(a[max]<a[x]){  //获取最小值，只要把<改成>就可以
              max=x;
           }
       }
       return a[max];
    }*/
}
```
### 数组的排序
```java
import java.util.Arrays;
/* 排序: 选择排序，冒泡排序，（希尔排序是效率最高的排序方法（三层循环加位运算进行排序））
 需求：对给定的数组进行排序 int[]{1,3,5,2,6,8}; */
public class ArrayText_2 {
    public static void main(String[] args) {
       int[] arr=new int[]{1,3,5,2,4,6,8,7};
       sop(arr);
       //selectedSort(arr);
       //bubbleSort(arr);
       Arrays.sort(arr);//这是java给我们提供的排序方法
       sop(arr);
    }
/*  选择排序：内循环一次，最值出现在头角表位置上
    方法构造思路：明确返回值类型。 因为对数组进行直接操作，所以不需要返回值类型
                是否需要参数。 需要一个数组 */
    public static void selectedSort(int[] arr){
       for(int x=0; x<arr.length-1;x++){
          for(int y=x+1;y<arr.length;y++){
             int temp=0;
             if(arr[x]>arr[y]){//角标为x的元素依次与后面的元素相比较,>是按照升序排序,<是按照降序排序
                 change(arr[x],arr[y]);
             //  temp=arr[x];
             //  arr[x]=arr[y];
             //  arr[y]=temp;
             }
          }
       }
    }
    // 冒泡排序：相邻的两个元素进行比较，如果符合条件则换位
    public static void bubbleSort(int[] arr){
       for(int  x=0;x<arr.length;x++){
          //因为随着循环次数的增加，每循环一次数组中要比较的元素就减少一个,且数组最后一位不用作比较。同时还可以避免角标越界
          for(int y=0;y<arr.length-x-1;y++){
             int temp=0;                    
             if(arr[y]>arr[y+1]){//相邻两个元素进行比较  >是按照升序排序，<是按照降序排序
                 change(arr[y],arr[y+1]);
             //  temp=arr[y];
             //  arr[y]=arr[y+1];
             //  arr[y+1]=temp;
             }
          }
       }
    }
    //交换两个元素的位置
    public static void change(int a,int b){
       int temp=0;
       temp=a;
       a=b;
       b=temp;
    }
    //打印数组
    public static void sop(int[] arr){
       System.out.print("数组是：");
       for(int x=0;x<arr.length;x++){
           System.out.print(arr[x]+" ");
       }
       System.out.println();
    }
}
```
### 数组的查找操作
```java
public class ArrayText3 {
    public static void main(String[] args) {
       int[] arr={1,2,3,4,5,6,7};
       //int index=getIndex(arr,5);
       //int index=halfSearch(arr,1);
       int index=insertIndex(arr,8);
       System.out.println("要查找的值的角标是:"+index);
    }
    //方法构思: 返回值类型是 角标，int  。参数是一个数组，与要查找的值
    //定义功能，或区域key值   第一次   出现在数组中的位置。如果返回值是-1，那么代表该key在数组中不存在
    public static int getIndex(int[] arr,int key){
       for(int x=0;x<arr.length;x++){
           if(arr[x]==key)
              return x;
       }
       return -1;
    }
    //折半查找，提高效率，但那是数组必须是有序的
    public static int halfSearch(int [] arr,int key){
       int min ,max ,mid;
       min=0;
       max=arr.length-1;
       mid=(min+max)/2;
       while(arr[mid]!=key){//while条件不满足就表示，找到了相应的数组角标，直接返回 mid
           if(key>arr[mid])
              min=mid+1;
           else if(key<arr[mid])
              max=mid-1;
           if(min>max)//如果min>max则程序执行结束
              return -1;
           mid=(min+max)/2;
       }
       return mid;//程序执行到这一步，代表找到了key值对应的角标
    }
    //折半查找的第二种方法
    public static int halfSearch2(int [] arr,int key){
       int min=0,max=arr.length-1,mid=(min+max)/2;
       while(min<=max){//如果，min不是<=max则，数组头尾的数值不能够查到其角标
           if(key>arr[mid])
              min=mid+1;
           else if(key<arr[mid])
              max=mid-1;
           else
              return mid;//以上两个判断如果都不满足那么代表已找到相应的角标
           mid=(min+max)/2;
       }
       return -1;//while条件不满足那么就表示没有查找到相应的角标
    }
/*  练习：有一个有序的数组，将要将一个元素插入到该数组中，还要保证数组是有序的
        如何获取该元素在数组中的位置? */
    public static int insertIndex(int [] arr , int key){
       int min=0,max=arr.length,mid=(min+max)/2;
       while(min<max){
           if(key>arr[mid])
              min=mid+1;
           else if(key<arr[mid])
              max=max-1;
           else
              return mid;
           mid=(min+max)/2;
       }
       return min;
    }
}
public class ArrayText4 {
    public static void main(String[] args) {
       //  toBin3(6);
       toHex2(60);
    }
/*  十进制--->二进制
方法思路：明确函数的返回值类型，将十进制数转化成二进制数并直接打印，所以函数返回值类型是:void
明确参数:一个十进制数 */
    public static void toBin(int a){
       while(a!=0){
           System.out.println(a%2);
           a=a>>1;
       }
    }
    //调用StringBuffer的append（） 和reverse（）方法将临时的数据存储起来，并反转打印
    public static void toBin2(int a){
       StringBuffer sb=new StringBuffer();
       while(a>0){
           sb.append(a%2);
           a=a/2;
       }
       System.out.println(sb.reverse());
    }
    //利用数组将临时数据存储起来，并倒叙打印
    public static void toBin3(int a){
       int [] x=new int [3];//数组的长度掘洞二进制数的长度
       int b=0;
       while(a>0){
           x[b]=a%2;
           a=a/2;
           b++;
       }
       for(int y=x.length-1;y>=0;y--){
           System.out.print(x[y]);
       }
    }
    // 十进制-->十六进制
    public static void toHex(int  num){
       for(int x=0;x<8;x++){
           int temp=num&15;
           if(temp>9)
              System.out.println((char)(temp-10+'A'));
           else
              System.out.println(temp);
           num=num>>4;
       }
    }
    public static void toHex2(int num){
       StringBuffer sb=new StringBuffer();
       for(int x=0;x<8;x++){
           int temp =num&15;
           if(temp>9)
              sb.append((char)(temp-10+'A'));
           else
              sb.append(temp);
           num=num>>>4;
       }
       System.out.println(sb.reverse());
    }
}
public class ArrayText5 {
    public static void main(String[] args) {
       // toHex3(60);
       //toBin(9);
       trans(60,15,4);
    }
/*  0 1 2 3 4 5 6 7 8 9 A B C D E F   十六进制中的元素
    将十六进制中的元素存入一个表中，然后那运算后的值到表中去查找表中的十六进制元素
查表法：1,将所有元素临时存储起来，建立对应关系。
        2,每一次  &15  后的值作为索引去查找建立好的表。就可以找到对应的元素。这样比  -10+'A'简单
怎样建立表？可以通过数据的形式来定义  */
  
    //建立表格打印十六进制数
    public static void toHex(int num){
       char [] chs={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E'};
       for(int x=0;x<8;x++){
           int temp =num&15;
           System.out.print(chs[temp]);
           num=num>>>4;
       }
    }
    //代码优化
    public static void toHex2(int num){
       char [] chs={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E'};
       char [] ch=new char[8];//定义一个临时存储容器。
       for(int x=0;x<8;x++){
           int temp =num&15;
           ch[x]=chs[temp];
           //System.out.println(chs[temp]);
           num=num>>>4;
       }
       //for(int x=0;x<ch.length;x++){
       for(int x=ch.length-1;x>=0;x--){
           System.out.print(ch[x]);
       }
       //运行结果   0000003C
    }
    //代码进一步优化  当所转化的值不为0作为条件进行计算
    public static void toHex3(int num){
       char [] chs={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E'};
       char [] ch=new char[8];
       int pos=0;
       //int pos=8;
       while(num!=0){
           int temp=num&15;
           ch[pos++]=chs[temp];
           //ch[--pos]=chs[temp];
           num=num>>>4;
       }
       System.out.println(pos);
       for(int x=pos-1;x>=0;x--){
       //for(int x=pos;x<ch.length;x++){
           System.out.print(ch[x]+",");
       }
    }      //运行结果   3,C,
/*   定义一个十进制转化换二进制的方法
     定义一个临时字符数组，并按倒序进行存储，*/
    public static void toBin(int num){
       char [] chs={'0','1'};
       char [] arr=new char [32];
       int pos =arr.length;//最后一个
       while(num!=0){
           int temp=num&1;
           arr[--pos]=chs[temp];
           num =num>>>1;
       }
       for(int x=pos;x<arr.length;x++)
           System.out.print(arr[x]);
    }
    //共性抽取   num 要转换的数，base &上的数，offset 右移的位数
    public static void trans(int num ,int base,int offset){
       char [] chs={'0','1','2','3','4','5','6',
               '7','8','9','A','B','C','D','E'};
       char [] arr=new char [32];
       int pos=arr.length;
       while(num!=0){
           int temp=num&base;
           arr[--pos]=chs[temp];
           num=num>>>offset;
       }
       for(int x=pos;x<arr.length;x++){
           System.out.print(arr[x]);
       }
    }
}
```
### 二维数组
```java
/*  二维数组：例 int [][] arr=new int [2][3];
       定义一个名称为arr的二维数组。二维数组中有两个一维数组。每个一维数组，有三个元素   */
public class Array2Demo {
    public static void main(String[] args) {
       //int [] arr=new int [3];
       //int [][] arr=new int [3][4];
       //System.out.println(arr[0][1]);
       int [][] arr=new int [3][];
       arr[0]=new int[3];
       arr[1]=new int[1];
       arr[2]=new int[2];
       System.out.println(arr.length);//打印的是二维数组的长度  是3
       System.out.println(arr[0].length);//打印的是二维数组中第一个数组的长度
    }
}
```
## 第五章：面向对象
```java
/*  面向对象：三个特征：封装，继承，多态
以后开发：其实就是找对象使用。没有对象，就创建一个对象。
 找对象，建立对象，使用对象。维护对象的关系
类和对象的关系：
    类就是：对生活中的事物的描述.
    对象：就是这类事物，试试存在的个体。
例：现实生活中的对象：张三，李四；
 想要描述：提取对象的共性类容。对具体的抽象
 描述时:这些对象的共性有：姓名，性别，年龄  
 映射到java中，描述的就是class定义的类
 具体的对象就是对应java在堆内存中用new建立的实体
 
需求：描述汽车(颜色，轮胎数）描述事物就是在描述事物的属性和行为。
    属性对应是类中的变量，行为对应的是类中的函数（方法).
    其实定义类就是在描述事物，就是在定义属性和行为。属性和行为共同称为类中的成员（成员变量和成员方法）
成员变量和局部变量：
    作用范围：成员变量作用整个类中
              局部变量作用与函数中
    在内存中的位置：成员变量：在堆内存中，因为对象的存在，才在内存中存在
                    局部变量：在栈内存中 */
class Car{
    //描述颜色
    String color ="red";
    //描述轮胎数
    int num =4;
    void run(){
       System.out.println(color+".."+num);
    }  
}
public class Demo {
    public static void main(String[] args) {
       //其实汽车，在java中通过new 操作符来完成。就是在堆内存中
       Car c=new Car();
       c.run();
       c.color="blue";
       c.run();
/*  匿名对象：
使用方式一:当对象的方法只调用一次时，可以使用匿名来完成，这样写比较简单如果一个对象进行多个成员调用时，必须给这个对象起个名字
使用方式二：可以将匿名对象作为实际参数进行传递
new Car().color="yellow";  */ 
       show(c);
    }
    //需求：汽车修配厂，对汽车进行改装，将汽车的改成黑色，将汽车的轮胎改成三轮胎
    public static void show(Car c){
       c.num=3;
       c.color="black";
       c.run();
    }
}
```
### 封装
```java
/*  封装：是指隐藏对象的属性和实现细节，仅对外提供公共的访问方式
    好处：1,将变化隔离
         2,便于使用
         3,提高重用性
         4,提高安全性
 封装的原则：1,将不需要对外提供的内容都隐藏起来。
            2,把属性都隐藏，提供公共方法对其访问 */
public class fengZhuangDemo {
    public static void main(String[] args) {
       Person p=new Person();
       p.setAge(-20);
    }
}
/* private ：私有，权限修饰符,用于修饰类中成员（成员变量，成员方法）私有只在本类中有效。
将age私有化以后，类以外即使建立了对象也不能直接访问但是人应该有年龄，就需要在Person类中提供对应的访问age   的方式
注意：私有（private）仅仅是封装的一种表现形式
之所以对外提供访问方式，就应为可以在访问方式中加入逻辑判断等语句，对访问的数据进行操作，提高代码的健壮性 */
class Person{
    private int age;
    public void setAge(int a){
       if(a>0&&a<130){
           age=a;
           speak();
       }else
           System.out.println("填的年龄不合法");
    }
    public int getAge(){
       return age;
    }
    void speak(){
       System.out.println(age);
    }
}
```
### 构造函数
```java
/*  构造函数：对象一建立就会调用与之对应的构造函数。
构造函数的作用:可以给对象进行初始化。
构造函数的小细节：
    当一个类中没有定义构造函数时，那么系统会默认给该类加入一个空参数的构造函数。
    当类中定义了构造函数后，默认的构造函数就没有了。
构造函数和一般函数的区别：
    1，在写法上不同
    2，构造函数是在对象一建立就运行（是给对象初始化），而一般方法是对象调用时才运行
    3，一个对象一建立，构造函数只运行一次，一般方法可以运行多次
 什么时候使用构造函数？
    当分析事物时，该事物存在具备一些特性或者行为，那么将这些类容定义在构造函数内 */
public class GouZaoHanShuDemo {
    public static void main(String[] args) {
       Person1 p=new Person1("zhangsan");
    }
}
class Person1{
    private String name;
    private int age;
/* 构造代码块：
  作用：给对象进行初始化；对象一建立就运行，而且 优先于  构造函数
什么时候用？
     定义不同对象的共性 初始化内容（cry();）
和构造函数的区别：
        构造 代码块 是给所有的对象进行统一的初始化
        而构造函数是给对应的对象进行初始化 */
    {
       cry();
    }
    Person1(){
       System.out.println("A:name="+name+",,age="+age);
       //cry();
    }
    Person1(String s){//重载
       name=s;
       System.out.println("B:name="+name+",,age="+age);
       //cry();
    }
    Person1(String s,int a){//重载
       name=s;
       age=a;
       System.out.println("C:name="+name+",,age="+age);
       //cry();
    }
    void cry(){
       System.out.println("cry.....");
    }
}
```
### This关键字
```java
/* this的用法：用于区分局部变量和成员变量  
this 代表哪一个？
    this就代表它所在函数所属对象的引用
简单说：哪个对象在调用this函数，this就代表哪个对象
this 的应用：当定义类中的功能时，该函数内部要用到调用该函数的对象时，这时就用this表示这个对象。但凡本类功         能使用了本类对象，都用this表示
this语句用于构造函数之间相互调用
this 语句只能放在构造函数的第一行，因为初始化要先执行。*/
public class ThisDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Person2 p=new Person2(20);
       Person2 p1=new Person2(20);
       System.out.println(p.compare(p1));
    }
}
class Person2{
    private String name;
    private int age;
    Person2(int age){
       this.age=age;
    }
    Person2(String name){//重载
       this.name=name;
       System.out.println("B:name="+name+",,age="+age);
    }
    Person2(String name,int age){//重载
       //this.name=name;这句话重复了，可以改成
       this(name);//相当于p(name); == new Person(name);
       this.age=age;
       System.out.println("C:name="+name+",,age="+age);
    }
    void speak(){
       System.out.println("name="+this.name+",,age="+this.age);
       this.show();//this可以不用写
    }
    void show(){
       System.out.println(this.name);
    }
/*  需求:给人定义一个用于比较年龄是否相同的功能。也就是是否是同龄人。
    方法思路：明确返回值类型  年龄是否相同  所以是boolean型
            明确参数   本类对象与相比较的人是否是同龄人*/
    public boolean compare(Person2 p){
       return this.age==p.age;
    }
}
```
### 静态 : static
```java
/* 静态 ：static
 用法：是一个静态修饰符，用于修饰成员（成员变量，成员方法）
    当成员被静态修饰后，就多了一个调用方法，除了可以被对象调用外，还可以直接被类名调用。 类名.静态成员。
 static的特点：
    1，随内存的加载而加载，也就是说，静态会随着类的消失而消失。生命周期较长。
    2，优先于对象存在(明确一点：静态是先存在的，对象是后存在的。)
    3，被所有对象共享
    4，可以直接被类名调用
实例变量和类变量的区别：
    1，存放位置:
       类变量随着累的加载而存在与方法区中
       实例变量随着对象的建立而存在
    2，生命周期:
       类变量的生命周期最长，随着类的消失而消失
       实例变量生命周期随着对象的消失而消失
静态的使用注意事项：
    1，静态方法只能访问静态成员（静态成员变量，静态成员方法）;非静态方法可以访问非静态方法，也可以访问静态
    2，静态方法中不可以定义this,super关键字,因为静态优先于对象存在，所以静态方法中不可以出现this
    3，主函数是静态的      
静态有利有弊：
    利：对对象的共享数据进行单独空间的存储，节省空间。没有必要每个空间中都存储一份,这样可以直接被类名调用
    弊：1,生命周期过长。
       2,访问出现局限性。（静态虽好，只能访问静态）*/
public class StaticDemo {
    public static void main(String[] args) {
       Person3 p=new Person3();
       p.name="zhangsan";
       //p.show();
       //System.out.println(Person3.country);
 
       System.out.println(args.length);
           //args   打印结果是： [Ljava.lang.String;@2a139a55
       //args.length 打印 结果是0，代表该数组中没有元素
    }
    public static void main(int a){//是可以存在的，方法重载了 
    }
}
class Person3{
    String name;//称之为：成员变量、实例变量
    static String country="CH";//静态成员变量，类变量
    public void show(){
       System.out.println(name+"..."+country);
    }
}
/* 什么时候使用静态？
    1，要从两方面下手： 因为静态修饰的内容有成员变量和函数
    2，什么时候定义静态变量（类变量）呢？
       当对象出现共享数据时，该数据被静态所修饰。
       对象中的特有数据要定义成非静态存在于堆内存中 
什么时候使用静态函数呢？
    当功能内部没有访问到非静态数据（对象特有的数据），那么该功能可以定义成静态的
静态的应用:
 
每一个应用程序都有共性的功能，可以将这些功能进行抽取，独立封装以便复用
虽然可以通过建立ArrayTool的对象使用这些工具方法，对数组进行操作。
发现问题：1，对象是用于封装数据的，可是ArrayTool对象并未封装特有数据
          2，操作数组的每一个方法都没有用到ArrayTool对象中的特有数据
这时就考虑，让程序更严谨，是不需要对象的。可以将ArrayTool中的方法都定义成static 的。直接通过类名调用即可;
将方法都静态后，可以方便于使用，但是该类还是可以被其他程序建立对象的。为了更严谨，强制让该类不能建立对象。可以通过构造函数私有化完成 */
public class StaticDemo2 {
    public static void main(String[] args) {
       int[] arr={2,4,1,3,5,7,23};
       int max=ArrayTool.getMax(arr);//如果本类中没有该类，jvm会在相同目录下找。
       int min=ArrayTool.getMin(arr);
       System.out.println(max);
       System.out.println(min);
       ArrayTool.printArray(arr);//下面的程序就是该工具类
       ArrayTool.selectedSort(arr);
       ArrayTool.printArray(arr);
       /*
       int  max=0;
       for(int x=1;x<arr.length;x++){
           if(arr[x]>arr[max])
              max=x;
       }   */
    }
}
/* 静态的应用。
    每一个应用程序都有共性的功能，可以将这些功能进行抽取，独立封装以便复用
将方法都静态后，可以方便于使用，但是该类还是可以被其他程序建立对象的。为了更严谨，强制让该类不能建立对象。可以通过构造函数私有化完成;
接下来，将ArrayTool.class文件发给其他人，其他人只要将该文件设置到calsspath路径下，就可以使用。但是很遗憾，该类中到底定义了多少方法，对方不清楚。因为并没有使用说明书,java 的说明数是通过文档注释来完成的*/
/**
 这是一个可以对数组进行操作的工具类，该类中提供了，获取最值、排序、打印等功能。
 @author 汤万才
 @version V1.8
 */
public class ArrayTool {
    /**
     空参数构造函数
     */
    private ArrayTool(){}//强制让该类不能建立对象。
    /**
     获取一个整型数组中的最大值
     @param arr 接受一个int类型的数组
     @return 会返回一个数组中的最大值
     */
    public static int getMax(int [] arr){
       int max=0;
       for(int x=1;x<arr.length;x++){
           if(arr[x]>arr[max])
              max=x;
       }
       return arr[max];
    }
    /**
     获取一个整型数组中的最小值
     @param arr 接受一个int类型的数组
     @return 会返回一个数组中的最小值
     */
    public static int getMin(int [] arr){
       int min=0;
       for(int x=1;x<arr.length;x++){
           if(arr[x]<arr[min])
              min=x;
       }
       return arr[min];
    }
    /**
     给int 数组进行选择排序
     @param arr 接受一个int类型的数组
     */
    public static void selectedSort(int []arr){
       for(int x=0;x<arr.length-1;x++){
           for(int y=x+1;y<arr.length;y++){
              if(arr[x]>arr[y]){
                  swap(arr,x,y);
                  /*
                  int temp=arr[x];
                  arr[x]=arr[y];
                  arr[y]=temp;
                  */
              }
           }
       }
    }
    /**
     给int 数组进行冒泡排序
     @param arr 接受一个int类型的数组
     */
    public static void bubbleSort(int [] arr){
       for(int x=0;x<arr.length-1;x++){
           for(int y=0;y<arr.length-x-1;y++){
              if(arr[y]>arr[y+1]){
                  swap(arr,y,y+1);
              }  
           }
       }
    }
    /**
     用于打印数组中的元素
     * @param arr 接受一个int类型的数组
     */
    public static void printArray(int [] arr){
       System.out.print("[");
       for(int x=0;x<arr.length;x++){
           if(x!=arr.length-1)
              System.out.print(arr[x]+",");
           else
              System.out.println(arr[x]+"]");
       }
    }
    /**
     给int 数组进行位置的置换
     @param arr 接受一个int类型的数组
     @param a 要进行置换的位置
     @param b 要进行置换的位置
     */
    //不想将该函数暴露出去
    private static void swap(int[] arr,int x,int y){
       int temp=arr[x];
       arr[x]=arr[y];
       arr[y]=temp;      
    }
}
/*  一个类中默认会有一个空参数的构造函数，这个默认的构造函数的权限和所属类一致。如果类被public修饰，那么默认的构造函数也带public修饰符。如果没有被public修饰，那么默认的构造函数也没有public修饰.  默认的构造函数的权限是随着类的变化而变化的 */
```
### 主函数 main
```java
/* 主函数是一个特殊的函数，作为程序的入口，可以被jvm调用
       主函数的定义：
           public:代表函数的访问权限最大
           static：代表主函数随着类的加载就已经存在了。
           void：主函数没有具体的返回值。
           main：不是关键字，但是是一个特殊的单词，可以被jvm识别
           (String[] args)：函数的参数，参数类型是一个数组，该数组中的元素是字符串。字符串类型的数组
       主函数是固定格式的：jvm识别。*/
public class MainDemo {
    public static void main(String[] args) {
       System.out.println(args.length);
       //args   打印结果是： [Ljava.lang.String;@2a139a55
       //args.length 打印 结果是0，代表该数组中没有元素
    }
}
```
### 静态代码块
```java
/*  静态代码块。
 格式： static{
       静态代码块中的执行语句;
        }
 特点：随着类的加载而执行，只执行一次,优先于主函数执行。用于给类进行初始化
执行优先级：   
  静态代码块（给类初始化）>构造代码块（给对象初始化）>构造函数（给指定对象初始化）*/
public class StaticCodeDemo {
    static{
       System.out.println("b");//先打印 b
    }
    public static void main(String[] args) {
       //new StaticCode();//后执行 a
       //new StaticCode();//这个就不会再执行了，因为只执行一次
       StaticCode.show();
       System.out.println("over");//最后执行 over
    }
    static{
       System.out.println("c");//再执行 c
    }
}
class StaticCode{
    static{
       System.out.println("a");
    }
    //创建一个show方法
    public static void show(){
       System.out.println("show run");
    }
}
```
### 程序执行的顺序
```java
public class DiaoYongDemo {
    public static void main(String[] args) {
       Person4 p=new Person4("zhangsan",20);
/*  Person p=new Person("zhangsan",20);
    这句话都做了什么事？
    1，因为new用到了Person.class。所以会先找到Person.class文件并加载到内存中
    2，执行该类中的static代码块（如果有的化），给Person.class类进行初始化。
    3，在堆内存中开辟空间，分配内存地址。
    4，在堆内存中建立对象特有的属性。并进行默认初始化。
    5，对属性进行显示初始化
    6，对对象进行构造代码块初始化。
    7，对对象进行对应的构造函数初始化
    8，将内存地址赋值给内存中的p变量  */
    }
}
class Person4{
    private String name;//第二
    private int age;//第二
    static{
       System.out.println("haha");//第一
    }
    {
       System.out.println("hehe");//第三
    }
    Person4(int age){
       this.age=age;
    }
    Person4(String name){//重载
       this.name=name;
       System.out.println("B:name="+name+",,age="+age);
    }
    Person4(String name,int age){//重载     //第四
       this(name);//相当于p(name); == new Person(name);
       this.age=age;
       System.out.println("C:name="+name+",,age="+age);
    }
    void speak(){
       System.out.println("name="+this.name+",,age="+this.age);
       this.show();//this可以不用写
    }
    void show(){
       System.out.println(this.name);
    }
}
```
### 设计模式：饿汉式，懒汉式。
```java
/*设计模式：解决莫一类问题最行之有效的方法
 java中有23中设计模式：
    单利设计模式：解决一个类在内存中只存在一个对象
 想要保证对象的唯一。
    1，为了避免其他程序过多的建立该类对象。先禁止其他程序建立该对象
    2，还为了让其他程序可以访问到该类对象，只好在本类中，自定义一个对象。
    3，为了方便其他程序对自定义对象的访问，可以提供一些访问方式
 这三部怎么用代码体现？
    1，将构造函数私有化
    2，在类中创建一个本类对象。
    3，提供一个方法可以获取到该对象
 对于事物该怎么描述，还怎么描述。当需要该事物对象保证在内存中唯一时，就将以上三步加上即可 */
public class DesignDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
    }
}
class Single{
    private int num;
    public void setNum(int num){
       this.num=num;
    }
    public int getNum(){
       return this.num;
    }
    private Single(){}
    private static Single s=new Single();
    public static Single getIncetance(){
       return s;
    }
}
class Student{
    private int age;
    //加上下面这三步，就可以保证对象的唯一性
    private static Student s=new Student();
    private Student(){}
    public static Student getStudent(){
       return s;
    }
    public void setAge(int age){
       this.age=age;
    }
}
//记住原则：定义单例，建议使用饿汉式
public class DesignDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
    }
}
/*  饿汉式：先初始化。Single类一进内存，就已经创建好了对象
class Single{
    private Single(){}
    private static Single s=new Single();
    public static Single getIncetance(){
       return s;
    }
}
方法二：懒汉式：对象是方法被调用时才初始化，也叫做对象的延迟加载。*/
class Single2{
    private Single2(){}
    private static Single2 s=null;
    public static Single2 getSingle(){
       if(s==null)
           s=new Single2();
       return s;
    }
}
```
### 继承
```java
/*  将学生和工人的共性内容提取出来，单独进行描述。只要让学生和工人与单独描述的这个类有关系就可了。
继承：1，提高了代码的复用性
      2，让类与类之间产生了关系。有了这个关系，才有了多态。
注意：千万不要为了获取其他类的功能，简化代码而选择继承。必须是类与类之间有所属关系才可以继承。所属关系 is a
 
java语言中：java 只支持单继承，不支持多继承。因为多继承容易带来安全隐患。
多个父类中定义了相同的功能，当功能内容不同时，子类对象不确定要运行哪一个
    但是java保留了这种机制。并用另一种体现形式来完成表示，就是  多实现
java支持多层继承，也就是一个继承体系。
 
如何使用一个继承体系 中的功能呢？
想要使用体系，先查阅体系中的父类描述，因为父类中定定义的是该体系中的共性功能通过了解共性功能，就可以知道 该体系中的基本功能, 那么这个体系已经可以基本使用了。
那么在具体调用时，要创建子类的对象，为什么呢？
    一是因为有可能父类不能创建对象，
    二是创建子类对象可以使用更多的功能，包括基本的  也包括特有的
简单一句话：查阅父类功能，创建子类对象使用功能 */
public class ExtendsDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
    }
}
class Person5{
    String name;
    int age;
}
class Student2 extends Person5{
    //String name;
    //int age;
    void study(){
       System.out.println("Student Study");
    }
}
class Worker extends Person5{
    //String name;
    //int age;
    void work(){
       System.out.println("Worker work");
    }
}
/* 子父类出现后，类成员的特点：
类中成员：
1，变量
 如果子父类中出现了非私有的同名成员变量时,子类要访问本类中的变量用this,子类要访问父类中的同名变量，用super;
 super的使用和this的用法几乎一致
    this代表的本类对象的引用。
    super代表的是父类对象的引用。
2，函数
 当子类中出现和父类中一模一样的函数时，当子类对象调用该函数，会运行子类中的函数。如同父类的函数被覆盖了一样;
 这种情况是函数的另一个特性:重写（覆盖）
    注意：1，子类覆盖父类，必须保证子类权限大于等于父类的权限，才可以覆盖，否则编译失败
         2，静态只能覆盖静态
3，构造函数
 在对子类对象进行初始化时，父类的构造函数也会运行。那是因为子类的构造函数默认第一行都有一条隐式的super();
 super会访问父类中空参数的构造函数。而且子类中所有的构造函数默认的第一行都是super();        
为什么子类一定要访问父类中的构造函数？
    因为父类中的数据子类可以直接获取，所以子类对象在建立时，需先查看父类是如何对这些数据进行初始化的,所以子  类在对象初始化时，先要访问一下父类中的构造函数
    如果要访问父类中指定的构造函数，可以手动的定义super语句的方式来指定。
注意：super语句一定定义在子类构造函数的第一行(因为初始化动作要先做)    子类的实例化过程
结论：
   1,子类中所有的构造函数，都默认会有父类空参数的构造函数，因为每一个构造函数的第一行都有一句隐式super();
   2,当父类中没有空参数的构造函数时，子类必须 手动 通过super语句形式来指定要访问父类中的构造函数
   3,当然，子类的构造函数第一行也可以手动指定this语句来访问本类中的构造函数。
   4,子类中至少会有一个构造函数会访问父类中的构造函数
记住：重载：只看同名函数的参数列表
      重写(覆盖)：子父类方法要一模一样 */
public class ExtendsDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Zi z=new Zi();
       System.out.println(z.num+"..."+z.num);
       z.show();
    }
}
class Fu{
    int num=1;
    Fu(){
       System.out.println("fu run");
    }
    void show(){
       System.out.println("fu  show");
    }
    void speak(){
       System.out.println("VB");
    }
}
class Zi extends Fu{
    //int num=2;
    Zi(){
       super();
       System.out.println("zi run");
    }
    Zi(int x){
       this();//访问的是Zi();
       System.out.println("zi..."+x);
    }
    void show(){
       System.out.println(super.num);//super可以省略
       System.out.println(this.num);//this和super指向的是同一个num
    }
    void speak(){
       System.out.println("JAVA");
    }
}
```
### Final 修饰符
```java
/* final：最终。
 作为一个修饰符：
    1，可以修饰类，函数，变量。
    2，被final修饰的类不可以被继承。为了避免被继承，被系类复写功能
    3，被final修饰的方法不可以被复写。
    4，被final修饰的变量是一个常量只能赋值一次，即可以修饰成员变量，也可以修饰局部变量
    （当在描述事物时，一些数据的出现是固定的，那么为了增强阅读性，都给这些值起个名字，方便阅读。而这个值不需要改变，所以加上final修饰。
    作为常量：常量的书写规范所有字母都大写，如果有多个单词组成，单词间通过 “ _ ”连接
    5，内部内定义在类中的局部位置上时，只能访问被final修饰的局部变量 */
class Demo3{
    final int x=3;
    public static final double PI =3.14;//全局常量
    final void show(){
    }
    void show2(){
       final int y=2;
       System.out.println(PI);
    }
}
public class FinalDemo {
    public static void main(String[] args) {
 
    }
}
```
### 抽象类
```java
/*
 当多个类中出现相同功能，但是功能主体不同，这时可以向上抽取。只抽取功能定义，而不抽取功能主体。
 抽象：看不懂。
 抽象的特点:
    1,抽象方法一定定义在抽象类中。
    2，抽象方法和抽象类都不许被abstract关键字修饰。
    3，抽象类不可以用new创建对象，因为调用抽象方法没有意义
    4，抽象类中的抽象方法要被使用，必须由子类复写起所有的抽象方法后，建立子类对象调用。
       如果子类只覆盖了部分抽象方法，那么子类还是一个抽象类
      
 抽象类与一般类没有太大的不同，该怎么描述事物就怎么描述事物。只不过事物中出现了一些看不懂的部分。这些不确定的部分，也是该事物的功能，需要明确出现。
 但是无法定义主体。通过抽象方法来表示。
 抽象类比一般类多了抽象函数。就是在类中可以定义抽象方法(抽象类中可以不定义抽象方法)
 抽象类可以不实例化 */
abstract class Student4{
    abstract void study();  //{System.out.println("study");}
    void sleep(){
       System.out.println("sleep");
    }
}
class BaseStudent extends Student4{
    void study(){
       System.out.println("base study");
    }
}
class AdvancedStudent extends Student4{
    void study(){
       System.out.println("advance study");
    }
}
class ChongCiStudent extends Student4{
    void study(){
       System.out.println("chongci study");
    }
}
public class AbstractDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //new Student().study();不能实例化类型 Student
       new BaseStudent().study();
    }
}
/*假如我们在开发系统是需要对员工进行建模，员工包含3个属性：姓名、工号以及工资。经理也是员工，除了含有员工的属性外，另外还有一个奖金属性。请使用继承的思想设计出员工类和经理类。要求类中提供必要的方法进行属性访问。
分析：
员工类：属性：name ID salary
经理类：继承了员工类，并有特有的奖金属性 bonus
经理和普通员工不同没有什么继承关系，所以不能把Employee当成普通员工，让经理去继承它，而要另创一个普通员工*/
abstract class Employee{
    private String  name;
    private String ID;
    private double salary;
    Employee(String  name,String ID,double salary){
       this.name=name;
       this.ID=ID;
       this.salary=salary;
    }
    public abstract void work();
}
class YiBanEmployee extends Employee{
    YiBanEmployee(String  name,String ID,double salary){
       super(name,ID,salary);
    }
    public void work(){
       System.out.println("YiBanEmployee work");
    }
}
class Manager extends Employee{
    private int bonus;
    Manager(String  name,String ID,double salary,int bonus){
       super(name,ID,salary);
       this.bonus=bonus;
    }
    public void work(){
       System.out.println("manager work");
    }
}
public class abstractDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
    }
}
```
### 模版方法设计模式
```java
/*
 需求：获取一段程序运行的时间。
 原理：获取程序开始和结束的时间相减即可。
 获取时间：System.currentTimeMillis();
 当代码完成修改后，就可以解决自己想要的执行的程序运行的时间
 这种方法称为 ：模版方法设计模式
 什么是模版方法设计模式呢？
    在定义功能时，功能的一部分是确定的，但是有一部分是不确定的，而确定的部分在使用不确定的部分，那么就将不确定的部分暴露出去。由该类的子类去完成
 */
public class TemplateDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new SubTime().getTime();
    }
}
abstract class GetTime{
    public final void getTime(){//禁止子类复写该方法
       long start=System.currentTimeMillis();
       //for(int x=0;x<1000;x++){ System.out.println(x);}
       runCode();
       long ends=System.currentTimeMillis();
       System.out.println("程序运行时间是："+(ends-start)+"毫秒");
    }
    //把想要的程序运行的代码抽象，让子类去重写该代码；
    abstract void runCode();
}
class SubTime extends GetTime{
    public void runCode(){
       for(int x=0;x<4000;x++){
           System.out.println(x);
       }
    }
}
```
###  接口
```java
/* 接口：初期理解，可以认为是一个特殊的抽象类
    当抽象类中的方法都是抽象的，那么该类可以通过接口的形式来表示
    class：用于定于类；
    interface ：用于定义接口
 接口定义时，格式特点：
    1，接口中常见的定义:常量，抽象方法；
    2，接口中的成员都有固定修饰符
       常量：public static final (这些关键字都可以省略，但是不建议省略)
       方法：public abstract   (这些关键字都可以省略，但是不建议省略)
        记住：接口中的成员都是public的
 接口是不可以创建对象的，因为有抽象方法，需要被子类实现，子类将接口中的抽象方法全部覆盖后，子类才可以实例化，否则子类是一个抽象类
 
 接口可以被类多实现，也是对多继承不支持的转换形式
 类与类：继承（单继承）
 类与接口：实现（一个或者多个）
 接口与接口：继承（单继承或者多继承） */
interface Inter{
    public static final int X=3;
    public abstract void show();
}
interface InterA{
    public static final int Y=3;
    public abstract void show();
}
class Demo4{
    public void function(){}
}
class Test extends Demo implements Inter,InterA{
    //实现接口中的方法
    public void show(){
       System.out.println("haha");
    }
}
public class InterfaceDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new Test().show();
    }
}
/* 接口的特点：
    1，接口是对外暴露的规则
    2，接口是程序的功能扩展
    3，接口可以用来多实现
    4，类与接口之间是实现关系，而且类可以继承一个类同时实现多个接口
    5，接口与接口之间可以有继承关系  */
 abstract class Student6{
    abstract void study();
    void sleep(){
       System.out.println("睡觉");
    }
}
interface Smoking{
    public abstract void smoke();
}
interface Drinking{
    public abstract void drink();
}
class Zhangsan extends Student6 implements Smoking,Drinking{
    public void study(){
       System.out.println("学习");
    }
    public void smoke(){
       System.out.println("抽烟");
    }
    public void drink(){
       System.out.println("喝酒");
    }
    //void sleep(){ System.out.println("睡觉"); }
}
class Lisi extends Student6 implements Smoking{
    public void study(){
       System.out.println("学习");
    }
    public void smoke(){
       System.out.println("抽烟");
    }
    void sleep(){
       System.out.println("睡觉");
    }
}
public class InterfaceDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new Zhangsan().drink();
    }
}
```
### 多态
```java
/* 多态：可以理解为事物存在的多种体现形态
 例：动物，猫狗
    猫 x=new 猫();
    动物  x=new 猫();
 1,多态的体现
    父类的引用指向了自己的子类对象
    父类的引用也可以接受自己的子类对象
 2,多态的前提
    必须是类与类之间有关系。要么是继承、要么是实现
    通常还有一个前提；就是存在覆盖
 3,多态的好处：多态的出现大大提高了程序的扩展性
 4,多态的应用
 5,多态的弊端：提高了扩展性，但是只能使用父类的引用访问父类中的成员
 6,多态的出现代码中的特点() */
abstract class Animal{
    abstract void eat();
}
class Cat extends Animal{
    public void eat(){
       System.out.println("吃鱼");
    }
    public void catchMouse(){
       System.out.println("抓老鼠");
    }
}
class Dog extends Animal{
    public void eat(){
       System.out.println("吃骨头");
    }
    public void kanJia(){
       System.out.println("看家");
    }
}
class Pig extends Animal{
    public void eat(){
       System.out.println("吃饲料");
    }
    public void gongDi(){
       System.out.println("拱地");
    }
}
public class DuoTaiDemo {
    public static void main(String[] args) {
    /*  Cat c=new Cat();
       function(c);//c.eat();
       Dog d=new Dog();
       function(d);//d.eat();*/
       function(new Cat());
       function(new Dog());
       Animal a=new Cat();//向上转型，类型提升。
       a.eat();
       //如果要调用猫的特有方法时，如何操作？
       //强制将父类的应用转换成子类类型，向下转型
       Cat c=(Cat)a;//向下转型，类型下降
       c.catchMouse();
    /*  千万不能出现这样的操作，就是将父类的对象转成子类类型
        Animal a=new Animal();(如果父类可以创建对象)
        Cat c =(Cat)a;
 我们不能转换的是父类应用指向了自己的子类对象时，应该可以被提升，也可以被强制转换多态自始至终都是  子类对象  在做着变化 */
    }
    public static void function(Animal a){
       a.eat();
       if(a instanceof Cat){
           Cat c=(Cat)a;
           c.catchMouse();
       }else if (a instanceof Dog){
           Dog c=(Dog)a;
           c.kanJia();
       }
    }
    /*
    public static void function(Cat c){
       c.eat();
    }
    public static void function(Dog d){
       d.eat();
    }   */
}
/* 基础班学生：学习，睡觉
  高级班学生：学习，睡觉
 可以将这两个事物进行抽取 */
abstract class Student7{
    public abstract void study();
    public void sleep(){
       System.out.println("躺着睡");
    }
}
class BaseStudent2 extends Student7{
    public void study(){
       System.out.println("base study");
    }
    public void sleep(){
       System.out.println("坐着睡");
    }
}
class AdvanceStudent extends Student7{
    public void study(){
       System.out.println("Advance study");
    }
}
public class DuoTaiDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       doSome(new BaseStudent2());
    }
    public static void doSome(Student7 s){
       s.study();
       s.sleep();
    }
}
/* 在多态中成员函数的特点：
    在编译时期：参阅引用型变量所属的类中是否有调用的方法。如果有，编译通过，没有则不通过
    在运行时期：参阅对象所属的类中是否有调用的方法
  简单的说就是：成员函数在多态时调用，编译时看左边，运行是看右边
在多态中，成员变量的特点(例：num)：无论编译和运行,都参考左边(引用型变量所属的类)
在多态中，静态成员函数的特点：无论编译和运行都参考左边 */
class Fu2{
    int num=1;
    void mothod1(){
       System.out.println("fu mothod_1");
    }
    void mothod2(){
       System.out.println("fu mothod_2");
    }
    static void mothod4(){
       System.out.println("fu mothod_4");
    }
}
class Zi2 extends Fu2{
    int num=2;
    void mothod1(){
       System.out.println("zi mothod_1");
    }
    void mothod3(){
       System.out.println("zi mothod_3");
    }
    static void mothod4(){
       System.out.println("zi mothod_4");
    }
}
public class DuoTaiDemo3 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Fu2 f=new Zi2();
       //运行时看右边
       //f.mothod1();//结果是：zi mothod_1
       //f.mothod2();//结果是：fu mothod_2
       //System.out.println(f.num);
       f.mothod4();
       Zi2 z=new Zi2();
       z.mothod4();
       //System.out.println(z.num);
       /*
       z.mothod1();//zi mothod_1
       z.mothod2();//fu mothod_2
       z.mothod3();//zi mothod_3
       */
    }
}
/* 需求：电脑运行实例
         电脑运行基于主板
class MainBoard{
    public void run(){
       System.out.println("mainboard run");
    }
    public void user(NetCard nc){
       nc.open();
       nc.close();
    }
}
class NetCard{
    public void open(){
       System.out.println("netcard open");
    }
    public void close(){
       System.out.println("netcard close");
    }
} */
class MainBoard{
    public void run(){
       System.out.println("mainboard run");
    }
                //多态
    public void use(PCI p){//PCI p=new NetCard();//接口型引用指向自己的子类对象
       if(p!=null){
           p.open();
           p.close();
       }
    }
}
interface PCI{
    public void open();
    public void close();
}
class NetCard implements PCI{
    public void open(){
       System.out.println("netcard open");
    }
    public void close(){
       System.out.println("netcard close");
    }
}
class SoundCard implements PCI{
    public void open(){
       System.out.println("SoundCard open");
    }
    public void close(){
       System.out.println("SoundCard close");
    }
}
public class DuoTaiDemo4 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       MainBoard mb=new MainBoard();
       mb.run();
       mb.use(new NetCard());
       mb.use(new SoundCard());
    }
}
/* 需求：数据库的操作。
 数据是用户信息：
    1，连接数据库。JDBC Hibernate
    2，操作数据库c create r read u update d delete
    3，关闭数据库连接 */
class UserInforByJDBC implements UserInforDao {
    public void add(User user){
       System.out.println("JDBC连接数据库");
       System.out.println("使用SQL添加数据");
       System.out.println("关闭数据库连接");
    }
    public void delete(User user){
       System.out.println("JDBC连接数据库");
       System.out.println("使用SQL删除数据");
       System.out.println("关闭数据库连接");
    }
}
class UserInforByHibernateC implements UserInforDao{
    public void add(User user){
       System.out.println("Hibernate连接数据库");
       System.out.println("使用SQL添加数据");
       System.out.println("关闭数据库连接");
    }
    public void delete(User user){
       System.out.println("Hibernate连接数据库");
       System.out.println("使用SQL删除数据");
       System.out.println("关闭数据库连接");
    }
}
class User{
   
}
interface UserInforDao{
    public void add(User user);
    public void delete(User user);
}
public class DuoTaiDemo5 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
//     UserInforByJDBC ui=new UserInforByJDBC();
//     ui.add(new User());
//     ui.delete(new User());
//     UserInforByHibernateC uh=new UserInforByHibernateC();
       UserInforDao ud=new UserInforByJDBC();
       ud.add(new User());
    }
}
```
### Object 类
```java
/*   Object:是所有对象的直接或者间接的父类，即传说中的上帝
 该类中定义的肯定是所有对象都具备的功能
 Object 类中已经提供了对对象是否相同的比较的方法,如果自定义的类中也有比较相同的功能，没有必要重新定义。只要沿袭父类中的功能，建立自己它特有的比较内容即可。这就是覆盖。 */
public class ObjectDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Demo5 d1=new Demo5(4);
       //Demo5 d2=new Demo5(4);
       //Demo5 d3=d1;
       //Person6 p1=new Person6();
       //System.out.println(d1.equals(p1));//equals比较的是地址值
       //System.out.println(d1.compare(d2));
       //System.out.println(d1==d2);
       //System.out.println(d1.toString());//Demo5@2a139a55
       //System.out.println(Integer.toHexString(d1.hashCode()));//2a139a55
       Class c=d1.getClass();
       //System.out.println(c.getName());//Demo5
       System.out.println(c.getName()+"@"+Integer.toHexString(d1.hashCode()));
       System.out.println(d1.toString());
       //Person6 p1=new Person6();
       //Person6 p2=new Person6();
       //System.out.println("Person:"+p1.equals(p2));
    }
}
class Demo5{//extends Object
    int num;
    Demo5(int num){
       this.num=num;
    }
    public boolean equals(Object obj){
       if(!(obj instanceof Demo5))
           return false;//throw Exception;
       Demo5 d=(Demo5)obj;
       return this.num==d.num;
    }
    /*
    public boolean compare(Demo5 d){
       return this.num==d.num;
    }
    */
    public String toString(){
       return "Demo5:"+num;
    }
}
class Person6{
   
}
```
### 内部类
```java
/* 内部类的访问规则：
    1，内部类可以直接访问外部类成员，包括私有，之所以可以直接访问外部类中的成员，是因为内部类中持有了一个外部类的引用，格式：类名.this
    2，外部类要访问内部类，必须键里内部类对象
 访问格式：
    1，当内部类定义在外部类的 成员位置上，而且非私有，可以在外部其他类中，直接建立内部类对象
        格式：外部类名.内部类   变量名 = new 外部类名().new 内部类名()
              Outer.Inner in=new Outer().new Inner();
    2，当内部类在成员位置上，就可以被成员修饰符所修饰。
       比如：private ：将内部类在外部类中进行封装
             static：内部类就具备静态特性
       当内部类被static修饰后，只能直接访问外部类中的static成员。出现了访问据局限
            在外部其他类中, 如何直接访问static内部类
              new Outer.Inner2().function();
           在外部其他类中，如何直接访问static内部类中的静态成员呢？
              Outer.Inner2.function2();
 注意：当内部类中定义了静态成员，该内部类必须是static的 
       当外部类中的静态方法访问内部类时，内部类也必须是static的            
 当描述事物时，事物的内部还有事物，该事物用内部类来描述。因为内部事物在使用外部事物的内容。
 class Body{
    private class XinZang{
       void tiaodong(){}
    }
    void show(){
       new XinZang().taiodong();
    }
 } */
class Outer{
    int x=3;
    class Inner{//内部类可以被 私有 修饰
       int x=4;
       void function(){
           int x=5;
           System.out.println("内部类方法:"+x);//内部类访问外部类成员
           System.out.println(x);//结果是  5
           System.out.println(this.x);//结果是  4
           System.out.println(Outer.this.x);//结果是  3
       }
    }
    static class Inner2{
       void function(){
           System.out.println("静态内部类方法");//静态内部类中的方法，不能调用非静态的成员
       }
       static void function2(){
           System.out.println("静态内部类静态方法");
       }
    }
    void method(){
       System.out.println("外部类方法");
       Inner in=new Inner();
       in.function();
    }
    static void show(){
       new Inner2().function();//建立对象调用内部类2中的非静态方法
       Inner2.function2();//直接用类名调用静态方法
    }
}
public class InnerClassDemo {
    public static void main(String[] args) {
//     Outer ou=new Outer();
//     ou.method();  
       //直接访问内部类的方式
//     Outer.Inner in=new Outer().new Inner();
//     in.function();
//     new Outer.Inner2().function();
//     Outer.Inner2.function2();
       Outer.show();
    }
}
/* 内部类定义在局部时：
    1，不可以被成员修饰符修饰
    2，可以直接访问外部类中的成员，因为还持有外部类中的引用。
       但是不可以访问它所在的局部中的变量。只能访问被final修饰的局部变量（与事实不相同有待考察）*/
class Outer2{
    int x=1;
    void method(final int a){
       final int y=2;
       class Inner{
           void show(){
              System.out.println("局部内部类方法::"+a);
           }
       }
       new Inner().show();
    }
}
public class InnerClassDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Outer2 out=new Outer2();
       out.method(3);//局部内部类方法::3
       out.method(4);//局部内部类方法::4
    }
}
/*
 匿名内部类：
    1，匿名内部类其实就是内部类的键写格式；
    2，定义匿名内部类的前提：内部类必须是继承一个类或者实现接口
    3，匿名内部类的格式： new 父类或者接口(){定义子类的内容};
    4，其实匿名内部类就是一个匿名子类对象，而且这个对象有点胖。可以理解为带内容的对象。
    5，匿名内部类中定义的方法最好不要超过3个。 */
abstract class Abstract{
    abstract void show();
}
class Outer3{
    int x=1;
    /*class Inner extends Abstract{
       void show(){
           System.out.println("");
       }
      }*/
    void method(){
       //new Inner().show();
       new Abstract(){//匿名内部类
           void show(){
              System.out.println("匿名内部类::"+x);
           }
           /*void abc(){
              System.out.println("匿名内部类::"+x);
           }*/
       }.show();//也可以调用abc();方法。但是同时只能调用一种方法
       /*
        Abstract a=new Abstract(){//匿名内部类     多态：父类引用指向子类对象
           void show(){
              System.out.println("匿名内部类::"+x);
           }
           void abc(){
              System.out.println("匿名内部类::"+x);
           }
       };
       a.show();可以
       a.abc();不可以，因为父类中没有该方法 */
    }
}
public class InnerClassDemo3 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new Outer3().method();
    }
}
interface Inter3{
    void method();
}
class Test3 {
    static Inter3 function(){
       return new Inter3(){
           public void method(){
              System.out.println("method run");
           }
       };
    }
}
public class InnerClassTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Test3.function().method();
       /*
        Test.function()：Test类中有一个静态方法function。
        .method()：function这个方法运算后结果是一个对象。而且是一个Inter3类型的对象。
        因为只有是Inter3类型的变量，才可以调用method方法。
        */
       InnerClassTest.show(new Inter3(){
           public void method(){
              System.out.println("method show run");
           }
       });
    }
    public static void show(Inter3 in){
       in.method();
    }
}
```
### 异常
```java
/* 异常：就是在程序运行时出现的不正常情况
 异常的由来：
    问题也是现实生活中具体的事物，也可以通过java的类的形式进行描述。并封装成对象。其实就是java对不正常情况进行描述后的对象体现
对于问题的划分：
    两种：一种是严重的问题，一种是非严重的问题。
       1，对于严重的，java通过Error类进行描述
           对于Error一般不编写针对性的代码对其进行处理
       2，对于非严重的，java通过Exception类进行描述
           对于Exception可以使用针对性的处理方式进行处理
 无论Error或者Exception都具有一些共性内容。
 比如：不正常的信息，引发原因等。
 Throwable
       |--Error
       |--Exception
 异常的处理
    java提供了特有的语句进行处理
       try{
           需要被检测的代码；
       }catch{
           处理异常的代码；
       }finnally{
           一定会执行的语句；
       }
 对捕获到的异常对象进行常见的方法操作
    String  getMessage()、toString()、printStackTrace() */
class De{
    int div(int  a,int b)throws Exception{//在功能上通过throws的关键字声明了可能会出现的问题
       return a/b;
    }
}
public class ExceptionDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       De d=new De();
       try{
           int x=d.div(4, 0);
           System.out.println("x="+x);//如果这句话出现异常，下面的代码则不会执行
       }catch(Exception e){
           System.out.println("除零了");
           System.out.println(e);//java.lang.ArithmeticException: / by zero
           System.out.println(e.getMessage());//    / by zero
           System.out.println(e.toString());//java.lang.ArithmeticException: / by zero
           e.printStackTrace();//异常名称，异常信息，异常出现的位置
                  //其实 jvm默认的异常处理机制，就是在调用printStackTrace方法打印异常的堆栈跟踪信息。
       }
       System.out.println("over");
    }
}
/*在函数上声明异常
    便于提高安全性，让调用者进行处理，不处理编译失败
对多异常的处理
    1，声明异常时，建议声明更为具体的异常。这样处理的可以更为具体
    2，对方声明几个异常，就对应有几个catch块，不要定义多余的catch块,如果多个catch块中异常出现继承关系，父类异常catch块放在最下面
 
建议在进行catch处理时，catch中一定要定义具体处理方式，不要简单定义一句 e.printStackTrace(),
也不要简单的就写一条输出语句 */
class Dem{
    int div(int  a,int b)throws ArithmeticException,ArrayIndexOutOfBoundsException{//在功能上通过throws的关键字声明了可能会出现的问题
       int [] arr=new int [a];
       System.out.println(arr[4]);
       return a/b;
    }
}
public class ExceptionDemo1 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Dem d=new Dem();
       try{
           int x=d.div(3, 1);
           System.out.println("x="+x);
       }catch(Exception e){
           System.out.println(e.toString());
       }
       /*catch(ArithmeticException e1){
           System.out.println("除零了");
       }catch(ArrayIndexOutOfBoundsException e2){
           System.out.println("角标越界了");
       }
       */
       System.out.println("over");
    }
}
/*
 Exception中有一个特殊的子类异常RuntimeException 运行时异常
 如果在函数中抛出该异常，函数上可以不用声明，编译一样通过。
 如果在函数上声明了该异常。调用者可以不用进行处理。编译一样通过。
 
 之所以不用在函数上声明，是因为不需要调用者处理。当该异常发生，希望程序停止。
 因为运行时，出现了无法继续运算的情况，希望停止程序后，对代码进行修正。
 
 自定义异常时:如果该异常的发生。无法在继续进行运算，就让自定义异常继承RuntimeException。
 对于异常分两种：
    1，编译时被检测的异常.
          如果在函数内抛出了 非 RuntimeException 则必须要在函数上声明该异常
    2，编译时不被检测的异常.(运行时 异常。RuntimeException以及其子类) */
class FuShuException2 extends RuntimeException{
    FuShuException2(String msg){
       super(msg);
    }
}
class Demo6{
    int div(int a,int b){//throws ArithmeticException 可以不用声明
       if(b==0)
           throw new ArithmeticException("除数为0了");//如果抛出Exception，则要声明
       else if(b<0||a<0)
           throw new FuShuException2("出现负数了");
       return a/b;
    }
}
public class ExceptionDemo3 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Demo6 d =new Demo6();
       int v=d.div(4, -1);
       System.out.println(v);
    }
 
}
 
/*
 需求：毕老师用电脑上课（使用名词提炼法）
 
 开始思考上课中遇到的问题：电脑蓝屏了
                        电脑冒烟了
 要对问题进行描述，以便封装成对象。
 可是当冒烟出发生后，出现了讲课进度无法进行的情况。这个就是老师的问题了 */
class Teacher{
    private String name;
    private Computer comp;
    Teacher(String name){
       this.name=name;
       comp=new Computer();
    }
    public void prelect() throws  NoPlanException{//throws  MaoYanException
       try {
           comp.run();
       } catch (LanPingException e) {
           comp.reset();
       } catch (MaoYanException e) {
           test();
           //throw e;//这个问题，老师也处理不了，所以要抛出去
           throw new NoPlanException("课时无法继续   "+e.getMessage());
       }
       System.out.println("老师讲课");
    }
    public void test(){
       System.out.println("做练习");
    }
}
class Computer{
    private int state=3;
    public void run() throws LanPingException, MaoYanException{
       if(state==2)
           throw new LanPingException("蓝屏了");
       else if(state==3)
           throw new MaoYanException("冒烟了");
       System.out.println("电脑运行");
    }
    public void reset(){
       System.out.println("电脑重启");
    }
}
class LanPingException extends Exception{
    LanPingException(String msg){
       super(msg);
    }
}
class MaoYanException extends Exception{
    MaoYanException(String msg){
       super(msg);
    }
}
class NoPlanException extends Exception{
    NoPlanException(String msg){
       super(msg);
    }
}
public class ExceptionTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Teacher te=new Teacher("毕老师");
       try {
           te.prelect();
       } catch (NoPlanException e) {
           System.out.println(e.toString());
           System.out.println("换老师或者放假 ");//+e.getMessage()
       }
    }
}
```
### 异常处理格式
```java
/*
 异常处理格式：
 格式一：
    try{
      
    }catch{
      
    }
 格式二：
    try{
      
    }catch{
      
    }finally{
   
    }
 格式三：
    try{
      
    }finally{
   
    }
记住：catch是用于处理异常的。如果没有catch，就代表异常没有被处理，如果该异常是检测时异常(即，不是RuntimeException异常)，那么就必须要声明。
异常在子父类覆盖中的体现：
    1，子类在覆盖父类时，如果父类的方法抛出异常，那么子类的覆盖方法，
       只能抛出父类的异常或者该异常的子类
    2，如果父类方法抛出多个  异常，那么子类在覆盖方法时，只能抛出父类异常的子集
    3，如果父类或者接口的方法中没有异常抛出，那么子类在覆盖方法时，也不可以抛出异常
       如果子类方法中发生了异常。就必须进行try处理，绝对不能抛。 */
/*
 因为项目中会出现特有的问题，而这些问题并未被java所描述并封装对象，所以对于这些特有的问题可以按照java的对问题封装的思想，将特有的问题。进行自定义的异常封装
 自定义异常
    需求：在本程序中，对于除数是-1，也视为是错误的是无法进行运算的
    那么就需要对这个问题及你想那个自定义的描述
 当函数内部出现了throw抛出的异常对象，那么就必须要给对应的处理动作，要么在内部 try catch处理，要么在函数上声明让调用者处理。
 一般情况下，函数内出现异常，函数上要声明
 
 发现打印的结果中只有异常的名称，却没有异常的信息，因为自定义的异常并未定义信息
 
 如何定义异常信息呢？
 因为父类中已经把异常信息的操作都完成了，所以子类中只要在构造时，将异常信息传递给 父类通过super语句。
 那么就可以直接通过getMassage方法获取自定义的异常信息
 
 自定义异常：必须是自定义类继承Exception。 
 继承Exception的原因:
    异常体系有一个特点：因为异常类和异常对象都被抛出。他们都具备可抛性，这个可抛性是Throwable这个体系中独有的特点。
    只有这个体系中的类和对象才可以被throws和throw操作。
    throws和throw的区别：
    throws使用在函数上。其后面跟的异常类可以跟多个。用，隔开。
    throw使用在函数内,其后面跟的是异常对象。 */
class FuShuException extends Exception{
    private int value;
    FuShuException(String message){
       super(message);
    }
    FuShuException(String message,int value){
       super(message);
       this.value=value;
    }
    int getValue(){
       return value;
    }
/*  private String message;
    FuShuException(String message){//如果单词拼写错误，自定义的异常信息将不能显示出来
       this.message=message;
    }
    public String getMessage(){
       return message;
    }*/
}
class ChuFa{
    int div(int  a,int b)throws ArithmeticException, FuShuException{//在功能上通过throws的关键字声明了可能会出现的问题
    if(b<0)
       throw new FuShuException("除数是负数::"+b);//手动通过throw关键字抛出一个自定义异常对象
    return a/b;
    }
}
public class ExceptionDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       ChuFa c=new ChuFa();
       try{
           int x=c.div(3, -1);
           System.out.println("x="+x);
       }catch(FuShuException e){
           //System.out.println("除数出现负数了");
           System.out.println(e.toString());
           return ;//如果有个return语句，则下面的over输出语句则不会执行
       }finally{
           System.out.println("finally");//finally 里面存放这一定会执行的语句
       }
       System.out.println("over");
    }
/*  finally代码块：定义一定执行的代码块，通常用于关闭资源。
 例：售货员向仓库管理员要货，而仓库漏水了没有或。这时仓库管理员,不仅要对仓库漏水的问题进行处理，还要给售货员一个答复 */
}
/* 例，有一个长方形和一个圆形,都可以获取面积。对于面积如果出现非法数值，视为获取面积出现问题。问题通过异常来表示。
 先要对这个程序进行基本的设计。 */
interface Shape{
    void getArea();
}
class ChangFangXing implements Shape{
    private int a,b;
    ChangFangXing(int a ,int b){ //throws IllegalException这个异常就不用抛出了
       if(a<0||b<0)
           throw new IllegalException("出现非法值");
       this.a=a;
       this.b=b;
    }
    public void getArea(){
       System.out.println("长方形的面积是："+a*b);
    }
}
class YuanXing implements Shape{
    private int a;
    public static final double PI=3.14;
    YuanXing(int a) {//throws IllegalException这个异常就不用抛出了
       if(a<0)
           throw new IllegalException("出现非法值");
       this.a=a;
    }
    public void getArea(){
       System.out.println("圆形的面积是："+(int)(PI*a*a));
    }
}
class IllegalException extends RuntimeException{//如果不继承Exception而继承
    private String msg;              //RuntimeException，就不用抛出异常了
    IllegalException(String msg){
       super(msg);
    }
}
public class ExceptionTest2 {
    public static void main(String[] args){//throws IllegalException这个异常就不用抛出了
       // TODO 自动生成的方法存根
       new YuanXing(3).getArea();
       new ChangFangXing(3,-4).getArea();
    }
}
/*
 异常的总结：
    异常是什么？是对问题的描述。将问题进行对象的封装。
 异常的体系：
    Throwable
       |--Error
       |--Exception
           |--
 异常体系的特点：
    异常体系中的所有类以及建立的对象都具备可抛性
    也就是说可以被throws和throw关键字操作
    也只有异常具备这个特点。
 throw和throws的用法：
    throw 定义在函数内，用于抛出对象。
    throws定义在函数上，用于抛出异常类，可以抛出多个，用逗号隔开。
 当函数内容有throw抛出异常对象，并未进行try处理。必须要在函数上声明。否则编译失败
 注意：RuntimeException及其子类除外，可以在抛出异常的情况下不用声明
 如果函数声明了以异常，调用者需要进行处理。处理方式可以throws可以try。
 异常有两种：
    编译时被检测异常
       该异常在编译时，如果没有处理（没有抛也没有try），编译失败。
       该异常被标识，代表可以被处理
    运行时异常（编译时不检测）
       在编译时，不需要处理，编译器不检测。
       该异常的发生，建议不处理，让程序停止。需要对代码进行修正能
 异常处理的语句：
 格式一：
    try{
       需要被检测的代码；
    }catch{
       处理异常的代码；
    }
 格式二：
    try{
       需要被检测的代码；
    }catch{
       处理异常的代码；
    }finally{
       一定会执行的代码；
    }
 格式三：
    try{
       需要被检测的代码；
    }finally{
       一定会执行的代码；
    }
 注意：finally中定义的通常是关闭资源的代码，因为资源必须要释放
    finally只有在一种情况下执行不到,就是当执行到  System.exit(0);
自定义异常：
    定义类继承Exception或者RuntimeException
       1，为了让该自定义类具备可抛性
       2，为了让该类具备操作异常的共性方法。
    当要定义自定义异常的信息时，可以使用父类已经定义好的功能,将异常信息传递给父类的构造函数
       class MyException extends Exception{
           MyException(String msg){
              Super(msg);
           }
       }
自定义异常：是按照java的面向对象的思想，将程序中出现的特有问题进行封装
异常的好处：1，将问题进行封装。
            2，将正常流程代码和问题代码相分离，方便于阅读
异常的处理原则：
    1，处理方式有两种:try或者throws。
    2，当用到抛出异常时，抛出几个，就处理几个。一个try对用多个catch
    3，多个catch，父类的catch放到最下面
    4，catch内，需要定义针对性的处理方式。不要简单的定义printStackTrace,输出语句，也不要不写。
       当捕获到的异常，本功能处理不了时，可以继续在catch中抛出
           try{
              throw new AException();
           }catch(AException e){
              throw e;
           }
       如果该异常处理不了，但并不属于功能出现的异常，可以将异常转换后，再抛出和该功能相关的异常,或者异常可以处理，需要将异常产生的和本功能相关的问题提供出去,让调用者知道。并处理。也可以将捕获的异常处理后，转换成新的异常。
           try{
              throw new AException();
           }catch(AException e){
              对AException进行处理;
              throw new BException();
           }
异常的注意事项：
    在子父类覆盖时：
       1，子类抛出的异常必须是父类异常的子类或者子集
       2，如果父类或者接口没有异常抛出时，子类覆盖出现异常，只能try不能抛
    参考 ExceptionTest.java老师用电脑上课   ExceptionTest2.java求图形面积 */
```
### 包
```java
/*包：1，对类文件进行分类管理
      2，给类提供多层命名空间
      3，写在程序文件的第一行
      4，类名的全称是  包名.类名
      5，包也是一种封装形式
为了简化类名的书写,使用一个关键字，import：导入的值包中的类
建议定义包名不要重复，可以使用url来完成定义，url是唯一的 */
package pack;//包名所有的字母都小写
//注意：导入的类文件，要加上   包名.
import packa.ADemo;//导入类名为packa.ADemo的文件，就可以建立ADemo的对象
public class PackageDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       ADemo a=new ADemo();//该类的权限也要够大
       a.show();//该方法权限要足够大
    }
}
```
另一个包中的代码：
```java
package packa;
public class ADemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
    }
    public void show(){
       System.out.println("ADemo show run");
    }
}
/*总结：
    1，包与包之间进行访问，被访问的包中的类以及类中的成员，需要被public修饰
    2，不同包中的子类还可以直接访问父类中被protected权限修饰的成员
    3，包与包之间可以使用的权限只有两种，public和protected
   
              public     protected      default    private
    同一个类中  ok         ok            ok         ok
    同一个包中  ok         ok            ok        
    子类       ok         ok
    不同包中     ok */
```
## 第六章:多线程
```java
/* 进程：是一个正在执行的程序。  每一个进程都有一个执行顺序。该顺序是一个执行路径，或者叫一个控制单元
   线程：就是进程中的一个独立的控制单元.   线程在控制着进程
   一个进程至少有一个线程
jvm 启动时会有一个进程java.exe。该进程至少有一个线程负责java程序执行,而且这个线程运行的代码存在于main方法中,该线程称之为主线程
 
 扩展：更细节说明java虚拟机，jvm启动不只一个线程，还有负责垃圾回收机制的线程。
 
 1，如何在自定义的代码中，自定义一线程呢？
    通过查找api，java已经提供了对线程这类事物的描述。就是Thread类
 创建线程的第一种方式：
 步骤：1，定义类继承Thread.
       2，复写Thread类中的run方法
       目的：将自定义的代码存储在run方法中。让线程运行
       3，调用线程的start方法，该方法有两个作用：启动线程，调用run方法
 
 发现运行结果每一次都不同。因为多个线程都获取cpu执行权。cpu执行到谁就运行谁。
 明确一点，在某个时刻只能有一个程序在运行（多核除外）。cpu在做着快速切换，以达到看上去是同时运行的效果。
 我们可以形象把多线程的运行行为在互相抢夺cpu执行权。这就是多线程的一个特性：  执行的随机性。
为什么要覆盖run方法？
 Thread类用于描述线程。该类就定义了一个功能，用于存储线程要运行的代码。该存储功能就是run方法。
 也就是说，Thread类中的run方法，用于存储线程要运行的代码。
 
      被创建
       |--->start
         运行
       |--->sleep(time)时间到线程就回来了
notify->|--->wait
       |--->stop
    冻结、消亡 */
class Demo extends Thread{
    public void run(){
       for(int x=0;x<60;x++)
           System.out.println("Demo run--"+x);
    }
}
public class ThreadDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Demo d=new Demo();
       d.start();//开启线程并执行线程中的run方法
       //d.run();仅仅是对象调用方法。而线程创建了，并没有运行
       for(int x=0;x<60;x++)
           System.out.println("hello run---"+x);
    }
}
/* 练习：创建两个线程，和主程序交替运行。
 原来线程都有自己的默认名称:Thread-编号  该编号从0开始
 
 static Thread currentThread():获取当前线程的对象
 getName():获取线程名称.
 设置线程名称:setName();或者构造函数 */
class Test extends Thread{
    //private String name;
    Test(String name){
       //this.name=name;
       super(name);//设置线程的名称,通过super()方法
    }
    public void run(){
       for(int x=0;x<60;x++)
           //System.out.println("Test"+name+" run--"+x);
           System.out.println("Test::"+this.getName()+" run--"+x);
    }                           //this==Thread.currentThread()
}
public class ThreadTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Test t1=new Test("1111---");
       Test t2=new Test("2222+++");
       t1.start();
       t2.start();
       for(int x=0;x<60;x++)
           System.out.println("main run---"+x);
    }
}
 
/* 需求:简单的卖票程序,多个窗口卖票
 创建线程的第二种方法:
    步骤;
       1,定义类实现Runnable接口
       2,覆盖Runnable接口中的run方法
           将线程要运行的代码存放在run方法中
       3,通过Thread类建立线程对象
       4,将Runnable接口的子类对象作为实际参数传递给Thread类的构造函数
           为什么要将Runnable接口的子类对象传递给Thread的构造函数.
           因为,自定义的run方法所属的对象是Runnable接口的子类对象
           所以要让线程去指定指定对象的run方法,就必须明确该run方法所属的对象
       5,调用Thread类的start方法开启线程并调用Runnable接口子类的run方法
 实现方式和继承方式有什么不同?
    实现方式好处:避免了单继承的局限性.
    在定义线程时,建议使用实现方式.
 两种方式的区别:
    继承Thread:线程代码存放在Thread子类的run方法中
    实现Runnable:线程代码存放在接口的子类的run方法中
 */
class Ticket implements Runnable{//extends Thread
    private static int ticket=100;//没有静态的时候,每个线程都有100张票,所以这个票要共享
    public void run(){
       while(true){
           if(ticket>0){
              System.out.println(Thread.currentThread().getName()+"::sale:"+ticket--);
           }  
       }
    }
}
public class TicketThread {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       /*
       Ticket t1=new Ticket();
       Ticket t2=new Ticket();
       Ticket t3=new Ticket();
       Ticket t4=new Ticket();
       t1.start();
       t2.start();
       t3.start();
       t4.start();
       */
       Ticket t1=new Ticket();
       Ticket t2=new Ticket();
       Ticket t3=new Ticket();
       Ticket t4=new Ticket();
       new Thread(t1).start();
       new Thread(t2).start();
       new Thread(t3).start();
       new Thread(t4).start();
       /*
        或者可以这么写
        Ticket t=new Ticket();
        Thread t1=new Thread(t);
        Thread t2=new Thread(t);
        Thread t3=new Thread(t);
        t1.start();
        t2.start();
        t3.start();
        */
    }
}
```
### 线程安全----同步
```java
/*
 通过分析发现,打印出了错票 Thread-2::sale:0,Thread-0::sale:-1
多线程的运行出现了安全问题
问题原因:
    当多条语句在操作同一个线程共享数据时,一个线程对多条语句只执行了一部分,还没有执行完,
    另一个程序参与进来执行.导致共享数据的错误
解决办法:
    对多条操作共享数据的语句,只能让一个线程都执行完.在执行过程中,其他线程不可以参与执行.
java对于多线程的安全问题提供了专业的解决办法.
就是同步代码块.
    synchronized(对象){
       需要被同步的代码
    }
 对象如同锁,持有所的线程可以在同步中执行.
 没有所得线程即使获取了cpu执行权,也进不去,因为没有获取锁
 
 例如:火车上的卫生间
 同步的前提:
    1,必须要有两个或者两个以上的线程
    2,必须是多个线程使用同一个锁
 必须保证同步中只能有一个线程在运行
 
 好处:解决线程的安全问题
 弊端:多个线程需要判断锁,较为消耗资源
 */
class Ticket1 implements Runnable{//extends Thread
    private static int ticket=100;
    public void run(){
       while(true){
           synchronized(" "){//同步代码块中的锁是任意一个 对象 
              if(ticket>0){
                  try { Thread.sleep(50);} catch (InterruptedException e) {}  
                  System.out.println(Thread.currentThread().getName()+"::sale:"+ticket--);
              }
           }
       }
    }
}
public class SafeThread {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Ticket1 t=new Ticket1();
      
       Thread t1=new Thread(t);
       Thread t2=new Thread(t);
       Thread t3=new Thread(t);
       t1.start();
       t2.start();
       t3.start();
    }
}
/*
 需求:银行有一个金库,有两个储户风别存放300元,每次村100,存三次
 目的:该程序是否有安全问题,如果有,如何解决?
 如何解决问题:
    1,明确那些代码是多线程运行代码
    2,明确共享数据.
    3,明确多线程运行代码中哪些语句是操作共享数据的.
同步函数用的是哪一个锁呢?
    函数需要被对象调用.那么函数都有一个所属对象引用,就是this
    所以同步函数使用的锁是this
 */
class Bank{
    private int sum;
    public synchronized void add(int n){
    //在public后面加synchronized,就可以将函数变成同步函数,省去下面的同步代码块内容
       //synchronized(""){
           sum+=n;
           try{Thread.sleep(100);}catch(Exception e){}
           System.out.println("sum="+sum);
       //}
    }
}
class Cus implements Runnable{
    Bank b=new Bank();
    public void run(){
       for(int x=0;x<3;x++)
           b.add(100);
    }
}
public class BankDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Cus c=new Cus();
       Thread a=new Thread(c);
       Thread b=new Thread(c);
       a.start();
       b.start();
    }
}
```
### 静态方法被多线程访问
```java
/*
 show方法被静态修饰后,运行出现了错票Thread-0::code:::0
 
 如果同步函数被静态修饰后,使用的是什么锁呢?
 通过验证发现不是this.因为静态方法中不可以定义this
 静态进内存时,内存中没有本类对象,但是一定有该类对应的字节码文件对象
 类名.class  该对象的类型是Class
 */
class Ticket2 implements Runnable{//extends Thread
    private static int ticket=100;
    boolean flag=true;
    public void run(){
       if(flag){
           while(true){
              //synchronized(this){//同步函数中的锁是this,所以这边的锁也是this
              synchronized(Ticket2.class){
                  if(ticket>0){
                     try { Thread.sleep(50);} catch (InterruptedException e) {}  
                     System.out.println(Thread.currentThread().getName()+"::code:::"+ticket--);
                  }
              }
           }
       }else
           while(true)
              show();
    }
    //public synchronized void show(){//同步函数中的锁是this
    public static synchronized void show(){//被静态修饰后使用的锁是Ticket2.class
       if(ticket>0){
           try { Thread.sleep(50);} catch (InterruptedException e) {}  
           System.out.println(Thread.currentThread().getName()+"::show:"+ticket--);
       }
    }
}
public class StaticMethodThread {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Ticket2 t=new Ticket2();
   
       Thread t1=new Thread(t);
       Thread t2=new Thread(t);
       t1.start();
       try{Thread.sleep(10);}catch(Exception e){}
       t.flag=false;
       t2.start();
    }
}
```
### 单例设计模式安全问题
```java
/*
 单例设计模式:
 饿汉式:
 class Single{
    private static final Single s=new Single();
    private Single(){}
    public static Single getInstance(){
       return s;
    }
 }
 懒汉式:
    当多线程并发进行访问时,会出现安全问题.这时就需要加同步来解决这个问题
    (静态函数中使用的锁是  字节码文件对象  即  类名.class)
    加同步,会导致程序的运行效率变低,为了提高效率,可以使用双重判断的方法进行优化
 */
class Single{
    private static Single s=null;
    private Single(){}
    public static Single getInstance(){
       if(s==null){
           synchronized(Single.class){
              if(s==null)
                  s= new Single();
           }
       }
       return s;
    }
}
public class SingleThread {
    public static void main(String[] args) {
 
    }
}
```
### 死锁
```java
// 死锁:同步中嵌套同步
class Test2 implements Runnable{
    boolean a;
    Test2(boolean a){
       this.a=a;
    }
    public void run(){
       if(a){
           synchronized(DeadLock.locka){
              System.out.println("if locka");
              synchronized(DeadLock.lockb){
                  System.out.println("if lockb");
              }
           }
       }else{
           synchronized(DeadLock.lockb){
              System.out.println("else lockb");
              synchronized(DeadLock.locka){
                  System.out.println("else locka");
              }
           }
       }
    }
}
class DeadLock{
    static Object locka=new Object();
    static Object lockb=new Object();
}
public class DeadLockThread {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Test2 t=new Test2(true);
       Test2 t0=new Test2(false);
       Thread t1=new Thread(t);
       Thread t2=new Thread(t0);
       t1.start();
       t2.start();
    }
}
```
### 线程间的通讯
```java
/*
 线程间的通讯:
    其实就是多个线程操作同一个资源
    但是操作的动作不同
等待唤醒机制:
    wait();使线程等待
    notify();唤醒线程池中的线程(等待中的线程就是在线程池中),按照等待的顺序进行唤醒
       notifyAll:唤醒线程池中的所有线程
    这两个方法基本上都用在同步里面,因为要对持有监视器(锁)的线程操作
    所以要使用在同步中,因为只有同步中才具备锁
   
    为什么这些操作线程的方法要定义在Object类中呢?
       因为这些方法在操作同步中线程时,都必须要标识它们所操作的线程持有的锁
       只有同一个锁上的被等待线程,可以被同一个锁上notify唤醒
       不可以对不同锁中的线程进行唤醒
      
       也就是说等待和唤醒必须是同一个锁
       而锁可以是任意对象,所以可以被任意对象调用的的方法定义在Object类中
   
    最后进行优化代码如下:
 */
class Res{
    private String name;
    private String sex;
    public synchronized void set(String name,String sex){
       this.notify();
       this.name=name;
       this.sex=sex;
       try{this.wait();}catch(Exception e){}
    }
    public synchronized void out(){
       this.notify();
       System.out.println(name+"..."+sex);
       try{this.wait();}catch(Exception e){}
    }  
}
class Intput implements Runnable{
    private Res r;
    Intput(Res r){
       this.r=r;
    }
    public void run(){
       int x=0;
       while(true){
           /*
           synchronized(r){
              r.notify();
              if(x==0){
                  r.name="mike";
                  r.sex="man";
              }else{
                  r.name="丽丽";
                  r.sex="女女女女";
              }
              x=(x+1)%2;
              try{r.wait();}catch(Exception e){}
           }
           */
           if(x==0){
              r.set("mike","man");
           }else{
              r.set("丽丽","女女女女");
           }
           x=(x+1)%2;
       }
    }
}
class Output implements Runnable{
    private Res r;
    Output(Res r){
       this.r=r;
    }
    public void run(){
       while(true){
           /*
           synchronized(r){
              r.notify();
              System.out.println(r.name+"...."+r.sex);
              try{r.wait();}catch(Exception e){}
           }*/
           r.out();
       }
    }
}
public class InputOutputThread {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Res r=new Res();
       Thread t1=new Thread(new Intput(r));
       Thread t2=new Thread(new Output(r));
       t1.start();
       t2.start();
    }
}
/*
 当有多个线程执行时;优化代码如下,添加while循环进行判断.并进行唤醒全部线程
 对于有多个生产者和消费者.
     为什么要定义while判断标记.
     原因:让被唤醒的线程再次判断标记
为什么定义notifyAll?
    因为需要唤醒对方线程.
    因为用notify,容易出现只唤醒本方线程的情况.导致程序中的所有线程都等待.
 */
class Resource{
    private Resource res;
    private int count;
    private String name;
    private boolean flag=false;
    public synchronized void set(String name){
       while(flag)//添加while循环,让每次线程等待的时候都进行判断flag标记
           try{this.wait();}catch(Exception e){}
      
       this.name=name+"..."+count++;
       System.out.println(Thread.currentThread().getName()+"..生产..."+this.name);
       flag=true;
       this.notifyAll();
    }
    public synchronized void out(){
       while(!flag)//添加while循环,让每次线程等待的时候都进行判断flag标记
           try{this.wait();}catch(Exception e){}
       System.out.println(Thread.currentThread().getName()+"消费..."+this.name);
       flag=false;
       this.notifyAll();
    }
}
class Producer implements Runnable{
    Resource res;
    Producer(Resource res){
       this.res=res;
    }
    public void run(){
       while(true){
           res.set("商品");
       }
    }
}
class Consumer implements Runnable{
    Resource res;
    Consumer(Resource res){
       this.res=res;
    }
    public void run(){
       while(true){
           res.out();
       }
    }
}
public class ProduceConsumerDemo {
    public static void main(String[] args) {
       Resource res=new Resource();
       Producer pro=new Producer(res);
       Consumer con=new Consumer(res);
       Thread t1=new Thread(pro);
       Thread t2=new Thread(pro);
       Thread t3=new Thread(con);
       Thread t4=new Thread(con);
       t1.start();
       t2.start();
       t3.start();
       t4.start();
    }
}
```
### Lock 锁
```java
import java.util.concurrent.locks.*;
/*
 JDK 1.5中提供了多线程升级的解决方案
 将同步synchronized替换成显示的Lock操作
 将Object中的wait,notify,notifyAll,替换成了Condition对象
 该对象可以Lock锁,进行获取
 该实例中实现了只唤醒随访的操作
 */
class Resource2{
    private int count;
    private String name;
    private boolean flag=false;
    //新建一个Lock锁对象,通过其子类 ReentrantLock类创建
    private Lock lock=new ReentrantLock();
    //通过Lock类的newCondition方法创建Condition对象
    private Condition condition_pro=lock.newCondition();
    private Condition condition_con=lock.newCondition();
    public  void set(String name){
       lock.lock();
       try{
           while(flag)
              condition_pro.await();
           this.name=name+"..."+count++;
           System.out.println(Thread.currentThread().getName()+"生产者"+this.name);
           condition_con.signal();//唤醒对方线程中等待的线程
           flag=true;
       }catch(Exception e){}
       finally{
           lock.unlock();//释放锁资源,finally里面放的是一定会被执行的语句
       }
    }
    public  void out(){
       lock.lock();
       try{
           while(!flag)
              condition_con.await();
           System.out.println(Thread.currentThread().getName()+"消费者...."+name);
           condition_pro.signal();//唤醒对方线程中的等待线程
           flag=false;
       }catch(Exception e){}
       finally{
           lock.unlock();
       }
    }
}
class Producer2 implements Runnable{
    Resource2 res;
    Producer2(Resource2 res){
       this.res=res;
    }
    public void run(){
       while(true){
           res.set("商品");
       }
    }
}
class Consumer2 implements Runnable{
    Resource2 res;
    Consumer2(Resource2 res){
       this.res=res;
    }
    public void run(){
       while(true){
           res.out();
       }
    }
}
public class ProduceConsumerDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Resource2 res=new Resource2();
       Producer2 pro=new Producer2(res);
       Consumer2 con=new Consumer2(res);
       Thread t1=new Thread(pro);
       Thread t2=new Thread(pro);
       Thread t3=new Thread(con);
       Thread t4=new Thread(con);
       t1.start();
       t2.start();
       t3.start();
       t4.start();
    }
}
```
### 停止线程
```java
/*
 stop方法已经过时了
 那么如何停止线程呢?
    只有一种方法,run方法结束.
    开启多线程运行,运行的代码通常是循环结构.
    只要控制住循环,就可以让run方法结束,也就是线程结束
 特殊情况:
    当线程处于了冻结状态
    就不会读取到标记,那么线程就不会结束
   
    当没有制定方式让冻结的线程回复到运行状态时,这时就需要对冻结进行清楚
    强制让线程回恢复到运行状态中来.这样就可以操作标记让线程结束
    Thread类提供了该方法 interrupted();
 */
import java.util.concurrent.locks.*;
class Stop implements Runnable{
    private boolean flag=true;
    Object obj=new Object();
    public synchronized void run(){
       while(flag){
           try{
//在没有加入同步的情况下,使用wait();方法,将抛出java.lang.IllegalMonitorStateException ,
//  Exception in thread "Thread-1" java.lang.IllegalMonitorStateException
//            at java.lang.Object.wait(Native Method)
//            at java.lang.Object.wait(Object.java:502)
//            at Stop.run(StopThread.java:26)
//            at java.lang.Thread.run(Thread.java:745)
              wait();
           }catch(InterruptedException e){
              System.out.println(Thread.currentThread().getName()+"...Exception");
              flag=false;
           }
           System.out.println("while...run");
       }
    }
    public void changeFlag(){
       flag=false;
    }
}
public class StopThread {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Stop s=new Stop();
       Thread t1=new Thread(s);
       Thread t2=new Thread(s);
       t1.setDaemon(true);//守护线程,在线程开始前调用,当运行程序都是守护线程时,jvm退出
       t2.setDaemon(true);
 
       t1.start();
       t2.start();
       int num=0;
       while(true){
           if(num++==20){
              //s.changeFlag();
              //t1.interrupt();//清除线程中断状态,让程序运行起来,如,线程wait,sleep等情况下
              //t2.interrupt();
              break;
           }
           System.out.println(Thread.currentThread().getName()+".."+num);
       }
       System.out.println("over");
    }
}
```
### 加入线程
```java
/*
 join:
    当A线程执行到B线程的join();方法时,A就会等待.等B线程执行完,A才会执行
 join可以用来临时加入线程执行
 */
class JoinDemo implements Runnable{
    public void run(){
       for(int x=0;x<60;x++)
       System.out.println(Thread.currentThread().getName()+".."+x);
    }
}
public class JoinThread {
    public static void main(String[] arg)throws Exception{
       JoinDemo join=new JoinDemo();
       Thread t1=new Thread(join);
       Thread t2=new Thread(join);
      
       t1.start();
       t2.start();
       t1.join();//当执行到这句话的时候,主线程会让出执行权,给t1执行完后,再执行
       for(int x=0;x<60;x++)
           System.out.println("main.."+x);
    }
}
```
## 第七章  String
```java
/*
 String s=new String();
 String s="";
 上面两句话是同一个意思,给s赋值一个空参数的对象
 String s="abc";s是一个类类型的变量,"abc"就是一个对象
           字符串最大的特点就是:一旦被初始化就不可以被改变.
 s="kk";不是s的值改变了,而是s的指向改变了."abc"的值并没有变;
 */
public class StringDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       String s="abc";
       String s1=new String("abc");
       /*
        s与s1的区别:
           s在内存中一个对象,"abc"
           s1在内存中有 两个对象,new 和  "abc"
        */
       String s2="abc";
   
       System.out.println(s==s1);//false
       System.out.println(s.equals(s1));//true
       //String类复写了Objcet类中的equals方法,该方法用于判断字符串是否相同
       System.out.println(s==s2);//true
       //因为"abc"已经存在,所以就不会在开辟新空间给s2,只要将它的指向改变就可以
    }
}
```
### String 中的方法
```java
/*
 String 类用于描述字符串事物.
 那么它就提供了多个方法对字符串进行操作
 那么常见的方法有哪些呢?
    "abcd"
    1,获取:
       1.1 字符串中的包含的字符数,也就是字符串的长度.
           int length();获取长度
       1.2 根据位置获取某一位置的字符
           char charAt(int index);
       1.3 根据字符获取该字符在字符串中的位置
           int indexOf(int ch);返回的是字符在字符串中第一次出现的位置
           int indexOf(int ch,int fromindex);返回的是从指定位置查找,字符在字符串中第一次出现的位置
           int indexOf(String str);返回指定子字符串在此字符串中第一次出现处的索引。
           int indexOf(String str,int fromIndex);返回指定子字符串在此字符串中第一次出现处的索引，
                                              从指定的索引开始。
           int lastIndexOf(int ch);返回指定字符在此字符串中最后一次出现处的索引。
    2,判断:
       2.1 字符串中是否包含某一个子串
           boolean contains(CharSequence s);当且仅当此字符串包含指定的 char 值序列时，返回 true。
       特殊之处:indexOf(String str);可以索引str第一次出现的位置,如果返回-1则表示该str在字符串中不存在
              所以,也可以用于指定判断是否包含某一字符串.
              if(str.indexOf("aa")!=-1)
              该方法既可以判断,又可以获取出现的位置
       2.2字符串是否有内容
           boolean isEmpty();当且仅当 length() 为 0 时返回 true。
       2.3 字符串是否是以指定的字符串开头或者结尾的
           boolean startsWith(String prefix); 测试此字符串是否以指定的前缀开始。
           boolean endsWith(String suffix); 测试此字符串是否以指定的后缀结束
       2.4 判断字符串内容是否相同,其复写了Object类中的equals方法
           boolean equals(Object anObject);
           判断字符串内容是否相同,并忽略大小写
           boolean equalsIgnoreCase(String anotherString)
    3,转换
       3.1 将字符数组转成字符串
           构造函数:String(char[])
                  String(char[],int offset,int count)
           静态方法:static String copyValueOf(char[]);
                  static String copyValueOf(char[] data,int offset,int count);
                  static String valueOf(char[] data); 返回 char 数组参数的字符串表示形式。
       3.2 将字符串转成字符数组
           char[] toCharArray();
       3.3 将字节数组转成字符串
           构造函数: String(byte[] bytes)
                   String(byte[] bytes,offset,count);将字节数组中的一部分转换字符串
       3.4 将字符串转成字节数组
           byte[] getBytes();
       3.5 将基本数据类型变成字符串
           static String valueOf(boolean);
           static String valueOf(char c);
           static String valueOf(double d) ;
           等等
           3+"";==String.valueOf(3);
       特殊:字符串和字节数组在转换过程中是可以指定编码表的
    4,替换
       String replace(oldchar,newchar);替换字符,所有的字符都替换
       String replace(String oldstr,String oldstr);替换字符串
    5,切割
       String[] split(regex);//按照某个字符串进行切割
    6,子串.获取字符串中的一部分
        String substring(beginIndex);
       String substring(beginIndex,endIndex);//包含头,不包含尾
    7,转换,去除空格,比较
       7.1 将字符串转化成大写或者小写
           String toUpperCase();
           String toLowerCase();
       7.2 将字符串两端的多余空格去除
           String trim();
       7.3 将两个字符串进行自然顺序的比较
           int compareTo();     
 */
public class StringMethodDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //method_get();
       //method_is();
       //method_trans();
       //method_replace();
       //method_split();
       //method_substring();
       method_();
    }
    public static void method_get(){
       String str="abcdefabcd";
       //字符串的长度
       sop(str.length());// 10
       //返回字符串中角标为3的字符
       sop(str.charAt(3));// d
       //返回字符为'b'在字符串中第一次出现的位置
       sop(str.indexOf('b'));// 1
       //返回从指定位置查找,字符为'b'在字符串中第一次出现的位置
       sop(str.indexOf('b',4));// 7
       //返回指定子字符串在此字符串中第一次出现处的索引。
       sop(str.indexOf("b"));// 1
       sop(str.lastIndexOf('a'));// 6
    }
    public static void method_is(){
       String str="ArrayDemo.java";
       //判断文件名称是否是以Array单词开头的
       sop(str.startsWith("Array"));//true
       //判断文件是够是以.java结尾的
       sop(str.endsWith(".java"));//true
       //判断文件中是否包含Demo
       sop(str.contains("Demo"));//true
    }
    public static void method_trans(){
       char[] ch={'a','b','c','d','e','f'};
       //String str=new String(ch);//str=abcdef
       String str=new String(ch,1,3);//str=bcd
      
       sop("str="+str);
      
       String ss="avnnvnrh";
       char[] chs=ss.toCharArray();
       for(int x=0;x<chs.length;x++){
           sop("chs="+chs[x]);
       }
    }
    public static void method_replace(){
       String s="hello java";
       String s1=s.replace('a', 'm');
       String s2=s.replace('b', 'm');//如果要替换的字符不存在,则返回的还是原来的字符串
       String s3=s.replace("java","world");
       sop("s="+s);//s=hello java  字符串一旦被初始化就不可以被改变
       sop("s1="+s1);//s1=hello jmvm  被替换后的字符串变成一个新的字符串赋值给s1
       sop("s3="+s3);
    }
    public static void method_split(){
       String s="zhangsan,lisi,wangwu";
       String[] arr=s.split(",");
       for(int x=0;x<arr.length;x++){
           sop("arr["+x+"]="+arr[x]);
       }
    }
    public static void method_substring(){
       String s="abcdefghi";
       String s1=s.substring(2);//从指定的位置开始到结尾处获取子串. 如果角标不存在,会出现字符角标越界异
       String s2=s.substring(2,5);//从指定位置开始(包含),到指定位置结束(不包含).
       sop(s1);
       sop(s2);
    }
    public static void method_(){
       String str="    ZHANGSAN lisi WANGWU  ";
       String str1="hello java";
       String str2="hello world";
      
       String s1=str.toUpperCase();
       String s2=str.toLowerCase();
       String s3=str.trim();
       int x=str1.compareTo(str2);//str2是参数.  运行结果是-13
       /*
        如果按字典顺序此 String 对象位于参数字符串之前，则比较结果为一个负整数。
        如果按字典顺序此 String 对象位于参数字符串之后，则比较结果为一个正整数。
        如果这两个字符串相等，则结果为 0；
        */
       sop(s1);//  ZHANGSAN LISI WANGWU 注意是有空格的
       sop(s2);//  zhangsan lisi wangwu
       sop(s3);//ZHANGSAN lisi WANGWU 没有空格了
       sop(x);
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
/*
 1,模拟一个trim方法,去除字符串两端的空格.
    思路:
    1,判断字符串第一个位置是否是空格,如果是则继续往下判断,直到不是空格为止.
    2,结尾处也是如此
    3,当开始和结尾都判断到不是空格时,就是要获取的字符串
 2,将一个字符串进行反转. 将字符串指定位置进行反转,"abcdefg";  "abfedcg"
    思路:
    1,曾经学过对数组元素进行反转
    2,将字符串变成数组,对数组进行反转
    3,将反转后的数组变成字符串
    4,只要将反转部分的开头和结尾位置作为参数传递即可
 3,获取一个字符串在另一个字符串中出现的次数,"abkkcdkkefkkgkk"
    思路:
    1,定义一个计数器.
    2,获取kk第一次出现的位置
    3,从第一次出现的位置后剩余的字符串中继续获取kk出现的位置
       每获取一次就计数一次
    4,当获取不到时,计数完成
 4,获取两个字符串中最大的相同子串. 第一个动作:将段的那个串进行长度依次递减的子串打印
    "abcwerthelloyuiodef"
    "cvhellobnm"
    思路:
    1,将短的那个子串按照长度递减的方式获取到
    2,将每获取到的子串去长串中判断是否包含,如果包含,已经找到
 */
public class StringTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //trim_();
       //reverse_();
       //getCount();
 
//     String s="abcdefg";
//     reverse_String(s);
//     reverse_String(s,2,5);
      
//     String s="abkkcdkkefkkgkk";
//     getCount2(s,"kk");
       sop(getMaxSubString());
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
    public static void sop_1(Object obj){
       System.out.print(obj);
    }
    //练习一:
    public static void trim_(){
       String s="    abcd efg   ";
       int pos=0;
       int x=s.length()-1;
       while(pos<=x&&s.charAt(pos)==' ')//代码优化,加上pos<=x&&
           pos++;
       while(pos<=x&&s.charAt(x)==' ')
           x--;
       sop(s.substring(pos,x+1));//因为substring方法,包含头不包含尾
    }
    //练习二:
    public static void reverse_(){
       String s="abcdefg";
       char[] chs=s.toCharArray();
       int x=2,y=5;
       while(x<y){
           char temp=chs[x];
           chs[x]=chs[y];
           chs[y]=temp;
           x++;
           y--;
       }
       String ss=String.copyValueOf(chs);//将数组变成字符串,还可以使用构造函数 String(char[]);
       sop(ss);
       /*
       for(int z=0;z<chs.length;z++)
           sop_1(chs[z]);//结果是  abfedcg
           */
    }
    //练习二的第二种做法
    //将功能主体抽取出来
    public static void reverse_String(String str){
       reverse_String(str,0,str.length()-1);
    }
    public static void reverse_String(String str,int begin,int end){
       char[] arr=str.toCharArray();//第一步将字符串变成字符数组
       reverse(arr,begin,end);//第二部按照指定的位置进行反转
       String s=new String(arr);//第三步就爱那个数组变成字符串
       sop(s);
    }
    public static void reverse(char[] arr,int x,int y){
       while(x<y){
           char temp=arr[x];
           arr[x]=arr[y];
           arr[y]=temp;
           x++;
           y--;
       }
    }
    //练习三:
    public static void getCount(){
       int count=0;
       String s="abkkcdkkefkkgkkhhkk";
       for(int x=0;x<s.length();x++){
           int index=s.indexOf("kk",x);
           x=index+2;
           count++;
       }
       sop(count);
    }
       //第二种做法:
    public static void getCount2(String s,String key){
       int count=0;
       int index=0;
//     while((index=s.indexOf(key))!=-1){
//         s=s.substring(index+key.length());
//         count++;
//     }
       while((index=s.indexOf(key,index))!=-1){
           index+=key.length();
           count++;
       }
       sop(count);
    }
    //练习四:
    public static String getMaxSubString(){
       String s1="abcwerthelloyuiodef";
       String s2="cvhellobnm";
       for(int x=0;x<s2.length();x++){
           for(int y=0,z=s2.length()-x;z!=s2.length()+1;y++,z++){
              String temp=s2.substring(y, z);
              if(s1.contains(temp))
                  return temp;
           }
       }
       return "";
    }
}
/*
 StringBuffer 是字符串缓冲区,
    1,是一个容器,而且长度是可变化的(数组的长度是固定的)
    2,可以直接操作多个类型
    3,最终会通过toString方法变成字符串
 功能:C create U update R read D delete
    1,存储
       StringBuffer append();将指定的数据作为参数添加到已有数据的结尾处
       StringBuffer insert(index,数据);可以将数据插入到指定的位置上去
    2,删除
       StringBuffer delete(start,end);
    3,获取
       char charAt(int index)
       int indexOf(String str)
       int lastIndexOf(String str)
       int length()
       String substring(int start, int end)
    4,修改
       StringBuffer replace(int start, int end, String str)
       void setCharAt(int index, char ch)
    5,反转
       StringBuffer reverse() ;
    6,
       void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)
       截取从指定位置开始到指定位置结束(不包含)的缓冲器中的字符,
       并把它存放到指定指定的数组中,并指定开始时位置
 在JDK 1.5 版本后出现了StringBuilder
    StringBuffer是线程同步的
    StringBuilder是线程不同步的
    以后开发建议使用StringBuilder,它与StringBuffer的用法基本相同
 升级的三要素;
    提高效率
    简化书写
    提高安全性
 */
public class StringBufferDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //add();
       //delete();
       //update();
       method_6();
    }
    public static void add(){
       StringBuffer sb=new StringBuffer();
       //StringBuffer sb1=sb.append("dd");
       sb.append(34).append("haha").append(true);
       sb.insert(4, "java");
       //到这一步的结果是:34hajavahatrue
       sop(sb);
       //sop(sb==sb1);//结果是 true
    }
    public static void delete(){
       StringBuffer sb=new StringBuffer("abcdefg");
       //sb.delete(1, 3);//adefg
       //sb.delete(0, sb.length());//清空缓冲区中的内容
      
       sb.deleteCharAt(2);//abdefg
        sop(sb);
    }  
    public static void update(){
       StringBuffer sb=new StringBuffer("abcdefg");
       sb.replace(1, 4, "java");
       sop(sb);//ajavaefg
    }
    public static void method_6(){
       StringBuffer sb=new StringBuffer("abcdefg");
       char[] chs=new char[4];
       sb.getChars(1, 4, chs, 1);
       for(int x=0;x<chs.length;x++)
           sop(chs[x]);//  结果是: bcd,第一位是空格
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
## 第八章:基本数据类型
```java
/*
 基本数据类型对象包装类:
 byte Byte
 short Short
 int Integer
 long Long
 float Float
 double Double
 char Character
 
 基本数据类型对象包装类的最长见作用,就是用于基本数据类型和字符串类型之间做转换
 
 基本数据类型转换成字符串
    基本数据类型+"";
    基本数据类型.toString(基本数据类型值);
       如:Integer.toString(34);//将34变成"34";
 字符串转换成基本数据类型
    xxx  a=Xxx.parseXxx(String str);
   
 如: int a=Integer.parseInt("123");
    long a=Long.parseLong("1234");
    double a=Double.parseDouble("12.34");
    boolean a=Boolean.parseBoolean("true");
 
 十进制转换成其他进制
    Integer.toBinaryString();
    Integer.toOctalString();
    Integer.toHexString();
 其他进制转换成十进制
    Integer.parseInt(String s, int radix)//radix是要转换成的进制
 */
public class IntegerDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //sop("int num="+Integer.MAX_VALUE);// 整数类型的最大值2147483647
       //将一个字符串转换成整数
       //int num=Integer.parseInt("123");
       //long lon=Long.parseLong("1155");
       //sop(num+4);
       //sop(lon+44);
    //十进制转成其他进制
       sop(Integer.toBinaryString(6));//110  二进制
       sop(Integer.toHexString(60));//3c   十六进制
       sop(Integer.toOctalString(12));//14     八进制
    //其他进制转换成十进制
       sop(Integer.parseInt("110", 2));//6
       sop(Integer.parseInt("3c",16));//60
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
 /*JDK 1.5 版本出现的新特性*/
public class IntegerDemo1 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       method();
       //Integer x=new Integer(4);
       Integer x=4;//自动装箱.==new Integer
       x=x+2;//相当于   x =x.intValue() + 2;
           //x,进行自动拆箱.变成了int类型的. 然后在和2相加
       Integer m=128;
       Integer n=128;
       sop("m==n:"+(m==n));//false
      
       Integer a=127;
       Integer b=127;
       sop("a==b:"+(a==b));//true 因为a和b指向了同一个Integer对象
                     //因为数值在byte范围内,对于新特性,如果该数值已经存在,则不会在开辟新空间
    }public static void method(){
       Integer x=new Integer("123");
       Integer y=new Integer(123);
       sop("x==y: "+(x==y));//false
       sop("x.equals(y): "+x.equals(y));//true  Integer复写了equals方法
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
## 第九章:集合框架
### Collection
```java
/*集合框架:
 Collection:
    List::元素是有序的,元素可以重复. 因为该集合体系有索引
       ArrayList
       LinkedList
       Vector
    Set::元素是无序的 ,元素不可以重复
       HashSet
       TreeSet
 为什么会出现这么多的容器呢?
 因为每一个容器对数据的存储方式都有不同,这个存储方式称之为:数据结构
    1,add方法的参数是Object
    2,集合中不可能存放对象实体,存放的是地址 
 什么是迭代器?
    其实就是集合中取出元素的方式
    形象比喻,就是抓娃娃机的夹子*/
 import java.util.*;
public class CollectionDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //base_method();
       //method_1();
       method_get();
    }
    public static void base_method(){
    //创建一个容器,使用Collection接口的子类.  ArrayList
           ArrayList al=new ArrayList();
       //1,添加元素
           al.add("java01");//add(Object obj);
           al.add("java02");
           al.add("java03");
           al.add("java04"); 
       //2,获取个数.获取是集合的长度
           //sop("size:"+al.size());
           //sop(al);//[java01, java02, java03, java04]           
       //3,删除元素
    //     al.remove("java03");
    //     sop(al);//[java01, java02, java04]
          
    //     al.clear();//清空集合
    //     sop(al);//[]  
       //4,判断元素
           sop("java03是否存在:"+al.contains("java03"));//true
           sop("集合是否为空呀? "+al.isEmpty());//false     
    }
    public static void method_get(){
       ArrayList al=new ArrayList();
           al.add("java01");//add(Object obj);
           al.add("java02");
           al.add("java03");
           al.add("java04");
       /*
       Iterator it=al.iterator();//获取迭代器,用于取出集合中的元素
       while(it.hasNext()){
           sop(it.next());
       }*/
       for(Iterator it=al.iterator();it.hasNext(); ){
           sop(it.next());
       }//这个更高效,因为迭代器一用完,it在内存中就释放了   
    }
    public static void method_1(){
       ArrayList al1=new ArrayList();
           al1.add("java01");//add(Object obj);
           al1.add("java02");
           al1.add("java03");
           al1.add("java04");
       ArrayList al2=new ArrayList();
           al2.add("java02");
           al2.add("java03");
       //al1.retainAll(al2);//取交集,al1中只会保留和al2中相同的元素
       //sop("al1:"+al1);//[java02, java03]
       //sop("al2:"+al2);
      
       al1.removeAll(al2);//去除al1中包含al2中的元素,保留剩下的元素
       sop("al1:"+al1);//al1:[java01, java04]
       sop("al2:"+al2);//al2:[java02, java03]
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
### List
```java
/*
 List:
    ArrayList:底层的数据结构使用的是数组结构.特点在于,查询速度很快,增删慢.线程是不同步的
    LinkedList:底层数据结构使用的链表结构. 特点在于,增删很快,查询速度慢
    Vector: 底层是数组数据结构.线程是同步的,被ArrayList取代了
 ArrayList,初始容量是10,超过长度会增加50%
 Vector,初始容量也是10,超过长度后增加100% 
   
 凡是可以操作角标的方法都是该体系特有的方法
    增:add(index,element);
       addAll(index,Collection);
    删:remove(index);
    改:set(index,element);
    查:get(index);
       subList(from,to);
       listIterator();
 List集合特有的迭代器. ListIterator是Iterator的子接口
 在迭代时,不可以通过集合对象的方法操作集合中的元素,因为会发生ConcurrentModificationException异常
 所以在迭代时,只能用迭代器的方法操作元素,可是Iterator方法是有限的,只能对元素进行判断,取出,删除的操作
 如果想要其他的操作如添加,修改等,就需要使用其子接口,ListIterator,该接口只能通过List集合的ListIterator方法获取
 */
import java.util.*;
public class ListDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //listMethod_();
       listIterator();
    }
    public static void listMethod_(){
       ArrayList al=new ArrayList();
       al.add("java01");//add(Object obj);
       al.add("java02");
       al.add("java03");
       sop("原集合是:"+al);
    //在制定位置添加元素
       //al.add(1,"java00");
    //在指定位置删除元素
       //al.remove(1);//[java01, java03]
    //修改元素
       //al.set(2,"java007");//[java01, java02, java007]
    //通过角标获取元素
       //sop(al.get(2));//java03
       sop(al);
    //获取所有元素
//     for(ListIterator it=al.listIterator();it.hasNext();)
//         sop("al:"+it.next());
    //通过indexOf获取元素的位置
       //sop("indexof="+al.indexOf("java02"));
    }
    public static void listIterator(){
       ArrayList al=new ArrayList();
       al.add("java01");//add(Object obj);
       al.add("java02");
       al.add("java03");
       ListIterator it=al.listIterator();
       sop("hasPrevious():"+it.hasPrevious());//这是迭代器还没有进行遍历,所以它前面是没有元素的
       while(it.hasNext()){
           Object obj=it.next();
           if(obj.equals("java02"))
              //it.add("java");//打印结果是:[java01, java02, java, java03]
              //it.remove();//将java02的引用从集合中移除
              it.set("java0000");//打印结果是[java01, java0000, java03]
           sop("obj="+obj);
       }
       sop("hasPrevious():"+it.hasPrevious());//迭代器已经遍历到最后一个元素,所以这时,是有前一个元素的
       sop(al);
       /*
       Iterator it=al.iterator();
       while(it.hasNext()){
           Object obj=it.next();
           if(obj.equals("java02"))
              //al.add("java");
              it.remove();//将java02的引用从集合中移除
           sop("obj="+obj);
       }
       sop(al);*/
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
### Vector
```java
import java.util.*;
/*
 枚举就是Vector特有的取出方式
 发现枚举与迭代器很相似,其实枚举和迭代是一样的
 为什么会出现迭代?
    因为枚举的名称以及方法名都很长,所以被迭代器取代了 */
public class VectorDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Vector v=new Vector();
       v.add("java01");//add(Object obj);
       v.add("java02");
       v.add("java03");
       Enumeration en=v.elements();
       while(en.hasMoreElements()){
           System.out.println(""+en.nextElement());
       }
    }
}
```
### LinkedList
```java
import java.util.*;
/*
 LinkedList特有方法:
addFirst();
    addLast();
    在集合的开头或者结尾添加元素.
    getFirst();
    getLast();
    获取元素,但是不删除元素. 如果集合中没有元素,会出现NoSuchElementException
    removeFirst();
    remoLast();
    获取元素并删除元素.  如果集合中没有元素,会出现NoSuchElementException
    offerFirst()
    offerLast()
    在集合的开头或者结尾添加元素.
    peekFirst()
    peekLast()
    获取元素,但是不删除元素.如果集合中没有元素,会返回null
    pollFirst()
    pollLast()
    获取元素并删除元素.  如果集合中没有元素,会返回null  */
public class LinkedListDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       LinkedList link=new LinkedList();
    //LinkedList特有方法
//     link.addFirst("java01");
//     link.addFirst("java02");
//     link.addFirst("java03");
//     sop(link);//[java03, java02, java01]
      
       link.addLast("java01");
       link.addLast("java02");
       link.addLast("java03");
//     sop(link);//[java01, java02, java03]
//     sop(link.getLast());//java03
//     sop(link);//[java03, java02, java01]
       sop(link.removeLast());//java03,取出并删除
       sop(link);//[java01, java02]
       sop("size"+link.size());
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
/*使用 LinkedList模拟一个堆栈或者队列数据结构
 堆栈:先进后出  如同一个被子
 队列:先进先出
 */
import java.util.*;
public class LinkedListTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       DuiLie d=new DuiLie();
       d.myAdd("java01");
       d.myAdd("java02");
       d.myAdd("java03");
       while(!(d.isNull()))
           sop(d.myGet());
       DuiZhan dz=new DuiZhan();
       dz.myAdd("java01");
       dz.myAdd("java02");
       dz.myAdd("java03");
       while(!(dz.isNull()))
           sop(dz.myGet());
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
class DuiLie{
    private LinkedList link;
    DuiLie(){ link=new LinkedList(); }
    public void myAdd(Object obj){ link.addLast(obj); }
    public Object myGet(){ return link.removeFirst(); }
    public boolean isNull(){ return link.isEmpty();}
}
class DuiZhan{
    private LinkedList link;
    DuiZhan(){ link=new LinkedList();}
    public void myAdd(Object obj){ link.addLast(obj);}
    public Object myGet(){ return link.removeLast();}
    public boolean isNull(){ return link.isEmpty();}
}
```
### ArrayList
```java
//去除Arraylist集合中的重复元素
import java.util.*;
public class ArrayListTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       ArrayList al=new ArrayList();
       al.add("java01");
       al.add("java02");
       al.add("java01");
       al.add("java02");
       al.add("java01");
       al.add("java03");
       sop(al);//[java01, java02, java01, java02, java01, java03]
       sop(singleElement(al));//[java01, java02, java03]
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
    public static ArrayList singleElement(ArrayList al){
       ArrayList newAl=new ArrayList();
       Object obj=new Object();
       Iterator it=al.iterator();
       while(it.hasNext()){
           obj=it.next();
           if(!(newAl.contains(obj)))
              newAl.add(obj);
       }
       return newAl;
    }
}
/* 将自定义对象作为元素存到Arraylist集合中,并除去重复元素
 比如:存入对象.同姓名同年龄视为同一个人. 作为重复元素
 思路:1,对人描述,将数据封装进人对象
      2,定义容器,将人
      3,取出
 List集合判断元素是否相同或者删除元素,依据的都是equals方法 */
import java.util.*;
class Person3{
    private String name;
    private int age;
    Person3(String name,int age){
       this.name=name;
       this.age=age;
    }
    public String getName(){ return name;}
    public int getAge(){ return age;}
    public boolean equals(Object obj){//这个equals是Person类中的
       if(obj instanceof Person3){
           Person3 p=(Person3)obj;
           return this.name.equals(p.name)&&this.age==p.age;
                  //这个equals是字符串类中的
       }
       return false;
    }
}
public class ArrayListTest2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       ArrayList al=new ArrayList();
       al.add(new Person3("java01",21));
       al.add(new Person3("java02",22));
       al.add(new Person3("java02",22));
       al.add(new Person3("java03",23));
       al.add(new Person3("java04",24));
       al.add(new Person3("java04",24));
       al=singleElement(al);
       Iterator it=al.iterator();
       while(it.hasNext()){
           //Object obj=it.next();
           Person3 p=(Person3)it.next();//当使用it.next();方法后,返回值是Object类型的,需要向下转型
           sop(p.getName()+"...."+p.getAge());
       }
    }
    public static ArrayList singleElement(ArrayList al){
       ArrayList newAl=new ArrayList();
       Object obj=new Object();
       Iterator it=al.iterator();
       while(it.hasNext()){
           obj=it.next();
           if(!(newAl.contains(obj)))
              newAl.add(obj);
       }
       return newAl;
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
### HashSet
```java
/*
 Set::元素是无序的 (存入和取出的顺序不一定相同),元素不可以重复
    HashSet:底层数据结构是哈希表
       HashSet是如何保证元素唯一性的呢?
       是通过元素的两个方法,hashCode和equals来完成的
       如果元素的hashCode值相同,才会判断equals是否为true,如果元素的hashCode值不同,则不会调用equals
    注意:对于判断元素是否存在,以及删除的操作,依赖的方法是元素的hashCode和equals方法
    TreeSet:
   
 Set集合的功能和Collection集合是一致的 */
import java.util.*;
class Demo{ }
public class HashSetDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       HashSet  hs= new HashSet();
       sop(hs.add("java01"));//true
       sop(hs.add("java01"));//false
       hs.add("java02");
       hs.add("java03");
       hs.add("java04");
       Iterator it=hs.iterator();
       while(it.hasNext()){
           sop(it.next());
       }
    }
    public  static void sop(Object obj){
       System.out.println(obj);
    }
}
import java.util.*;
//往hashSet集合中存入自定义对象,姓名和年龄相同为一个人,重复元素.
public class HashSetTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       HashSet hs=new HashSet();
       //hs.add(new Person2("java01",21));
       hs.add(new Person2("java01",21));
       hs.add(new Person2("java02",22));
       hs.add(new Person2("java03",23));
       //hs.add(new Person2("java04",24));
   
       sop(hs.contains(new Person2("java01",21)));
       Iterator it=hs.iterator();
       while(it.hasNext()){
           Person2 p=(Person2)it.next();
           sop(p.getName()+"..."+p.getAge());
       }
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
class Person2{
    private String name;
    private int age;
    Person2(String name,int age){
       this.name=name;
       this.age=age;
    }
    public String getName(){return name;}
    public int getAge(){return age;}
    public int hashCode(){//覆盖hashCode的方法,让HashSet集合中的元素有相同的地址值,
                     //然后在让其调用equals方法进行 自定义的内容的比较
       //return 1;改进;
        System.out.println(this.name+"..hashCode");
       return this.name.hashCode()+age*37;//*37是因为要尽量保证哈希值的唯一性
    }
    public boolean equals(Object obj){
       if(obj instanceof Person2){
           Person2 p=(Person2)obj;
           System.out.println(this.name+"..equals.."+this.age);
           return this.name.equals(p.name)&&this.age==p.age;
       }
       return false;
    }
}
```
### TreeSet
```java
import java.util.*;
import javax.management.RuntimeErrorException;
/*Set集合是无序的,不可以重复
    |--hashSet
    |--treeSet:treeSet可以对集合中的元素进行排序(与hashCode没有关系,至于compareTo方法有关
              底层数据结构是 :二叉树
              保证元素唯一性的依据是:compareTo方法return 0;来完成的
              如果return 1;则元素就是怎么存进去怎么取出来
              如果return -1;则元素是按照与存进去的相反的顺序取出来的
       treeSet排序的第一种方式:让元素自身具备比较性
           元素需要实现Comparable接口,覆盖compareTo方法
           这种方式也称为元素的自然排序,或者叫做默认顺序
       treeSet排序的第二种方式:元素自身不具备比较性,或者具备的比较性不是所需要的
           这时就需要让集合自身具备比较性,在集合初始化时就有了比较方式,就是新建一个比较器
 需求:往TreeSet集合中存储自定义的学生对象,想按照年龄进行排序
 记住:排序时,当主要条件相同时,一定要判断次要条件*/
public class TreeSetDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       TreeSet ts=new TreeSet();
       ts.add(new Student("java01",21));
       ts.add(new Student("java03",23));
       ts.add(new Student("java04",23));
       ts.add(new Student("java02",22));
       ts.add(new Student("java05",25));
       ts.add(new Student("java07",27));
       ts.add(new Student("java06",26));
       Iterator it=ts.iterator();
       while(it.hasNext()){
           Student s=(Student)it.next();
           sop(s.getName()+"..."+s.getAge());
       }
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
class Student implements Comparable{//该接口强制让学生具备比较性
    private String name;
    private int age;
    Student(String name,int age){
       this.name=name;
       this.age=age;
    }
    public String getName(){return this.name;}
    public int getAge(){return this.age;}
    public int compareTo(Object obj){
       /*  这是按照自定义的排序方法进行排序
       if(!(obj instanceof Student))
           throw new RuntimeException("不是学生对象");
       Student s=(Student)obj;
       System.out.println(this.name+"..compareTo.."+s.name);
       if(this.age==s.age)
           return this.name.compareTo(s.name);
       return (this.age-s.age);
       */
       //return 1;
       return -1;//倒序取出
    }
}
import java.util.*;
/*当元素自身不具备比较性,获取具备的比较性不是所需要的,这时就需要让集合(容器)自身具备比较性,定义一个比较器,将比较器对象作为参数传递给TreeSet集合的构造函数
 当两种排序都存在时,以比较器(Comparator)为主
    比较器的实现方法:定义一个类,实现Comparator 接口,覆盖compare方法
    某一类实现Comparable接口,覆盖compareTo(和equals,该方法可以不覆盖)方法 */
public class TreeSetDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       TreeSet ts=new TreeSet(new MyCompare());
       ts.add(new Student2("java01",21));
       ts.add(new Student2("java03",23));
       ts.add(new Student2("java03",21));
       ts.add(new Student2("java004",23));
       ts.add(new Student2("java02",22));
       Iterator it=ts.iterator();
       while(it.hasNext()){
           Student2 s=(Student2)it.next();
           sop(s.getName()+"..."+s.getAge());
       }
    }
    public static void sop(Object obj){ System.out.println(obj);}
}
class Student2{
    private String name;
    private int age;
    Student2(String name,int age){
       this.name=name;
       this.age=age;
    }
    public String getName(){return this.name;}
    public int getAge(){return this.age;}
}
class MyCompare implements Comparator{//定义一个比较器,是集合中的元素按照自定义的方式排序
    public int compare(Object o1, Object o2){
       Student2 s1=(Student2)o1;
       Student2 s2=(Student2)o2;
       int num= s1.getName().compareTo(s2.getName());
       if(num==0)
           return s1.getAge()-s2.getAge();
       return num;
    }
}
import java.util.*;
/*练习:按照字符串长度进行排序
 字符串本身具备比较性.但是它的比较方法不是所需要的,这时就只能用比较器 */
public class TreeSetTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       TreeSet ts=new TreeSet(new StringLengthComparator());
       ts.add("abcd");
       ts.add("bc");
       ts.add("ac");
       ts.add("abd");
       ts.add("c");
       ts.add("hahaha");
       Iterator it=ts.iterator();
       while(it.hasNext()){
           System.out.println(it.next());
       }
    }
}
class StringLengthComparator implements Comparator{
    public int compare(Object o1,Object o2){
       int num1 =o1.toString().length();
       int num2 =o2.toString().length();
       if(num1==num2)
           return o1.toString().compareTo(o2.toString());
       return num1-num2;
    }
}
```
### 泛型
```java
import java.util.*;
/* 泛型:JDK1.5版本后出现的新特性.用于解决安全问题,是一个类型安全机制
 好处:1,将运行时期出现的ClassCastException问题专一到了编译时期,方便程序员解决问题.让运行时期问题减少,安全
      2,避免了强制转换的麻烦
 泛型格式:通过<>来定义要操作的引用数据类型
 在使用java提供的对象时,什么时候使用泛型?
    通常在集合框架中很常见,只要定义<>就要使用泛型
 其实<>就是用来就收类型的
 当使用集合时,将集合中要存储的数据类型作为参数传递到<>中即可*/
public class GenericDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //ArrayList<String> al=new ArrayList<String>();
      
       TreeSet<String> al=new TreeSet<String>(new LenComparator());
       al.add("java00198");
       al.add("java098");
       al.add("java0019858");
       al.add("java013110198");
       al.add("java98");
       al.add("java97");
       //al.add(4);//相当于al.add(new Integer(4));//ClassCastException
       Iterator<String> it=al.iterator();//迭代器将元素取出来到迭代器中,所以迭代器也要定义泛型
       while(it.hasNext()){
           String s=it.next();
           System.out.println(s+"::"+s.length());
       }
    }
}
class LenComparator implements Comparator<String>{
    public int compare(String s1,String s2){
       int num =new Integer(s1.length()).compareTo( new Integer(s2.length()));
       if(num==0)
           return s1.compareTo(s2);
       return num;   
    }
}
import java.util.*;
class Student3{ }
class Worker{ }
//这是在泛型出来前的做法
class Tool{
    private Object obj;
    public void setObject(Object obj){ this.obj=obj;}
    public Object getObject(){return obj;}
}
/*
 泛型类:
 什么时候定义泛型类?
    当类中要操作的引用数据类型不确定的时候,早期定义Object来完成扩展,现在定义泛型来完成扩展*/
class Utils<Q>{
    private Q q;
    public void setObject(Q q){
       this.q=q;
    }
    public Q getObjcet(){
       return q;
    }
}
//泛型定义在方法上
/* 泛型类定义的泛型,在整个类中有效.如果被方法使用,那么泛型类的对象明确操作的具体类型后,所有要操作的类型就已经固定了,为了让不同的方法操作不同的类型,而且类型还不确定.那么可以将类型定义在方法上
 泛型定义在方法上,定义在返回值类型的前面
 特殊之处:静态方法不可以访问类上定义的泛型.
 如果静态方法操作的应用数据类型不确定,可以将泛型定义在方法上*/ /*
class Demo<T>{
    public void show(T t){
       System.out.println(t+"...show");
    }
    public void print(T t){
       System.out.println(t+"...print");
    }
}*/
class Demo<T>{//类型Demo后面也可以加上泛型,与下面的泛型方法不冲突
    public <T> void show(T t){
       System.out.println(t+"...show");
    }
    public <Q> void print(Q q){
       System.out.println(q+"...print");
    }
    public static<W> void method(W w){//泛型放在方法的返回值类型前面
       System.out.println(w+"...method");
    }
}
public class GenericDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
    /*  Tool t=new Tool();
       t.setObject(new Worker());
       Worker w=(Worker)t.getObject();
   
       Utils<Worker> u=new Utils<Worker>();
       u.setObject(new Worker());
       Worker w=u.getObjcet();*/
       Demo d=new Demo();
       d.show("haha");//haha...show
       d.print(4);//4...print
    }
}
import java.util.*;
//泛型定义在接口上
interface Inter<T>{
    void show(T t);
}
class MyInter implements Inter<String>{
    public void show(String s){
       System.out.println(s+"...show");
    }
}
class MyInterface<T> implements Inter<T>{
    public void show(T t){
       System.out.println(t+"...show..."+t);
    }
}
public class GenericDemo3 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       MyInter my=new MyInter();
       my.show("haha");
       MyInterface<Integer> m1=new MyInterface<Integer>();
       m1.show(5);
       MyInterface<String> m2=new MyInterface<String>();
       m2.show("hahahahaha");
    }
}
import java.util.*;
/*  ?  通配符.也可以理解为占位符
  泛型的限定:
    ? extends E :可以接受E类型或者E类型的子类  向上限定
    ? super E :可以接受E类型或者E类型的父类  向下限定 */
public class GenericDemo4 {
    public static void main(String[] args) {
    /*  ArrayList<String> al=new ArrayList<String>();
       al.add("java01");
       al.add("java02");
       al.add("java03");
       ArrayList<Integer> al1=new ArrayList<Integer>();
       al1.add(1);
       al1.add(2);
       al1.add(3);
       al1.add(4);
 
       print(al);
        print(al1);
    }
    public static void print(ArrayList<?> al){//占位符  ?
       Iterator<?> it=al.iterator();
       while(it.hasNext()){
           System.out.println(it.next());
       }*/
       ArrayList<Person4> al=new ArrayList<Person4>();
       al.add(new Person4("java01"));
       al.add(new Person4("java02"));
       al.add(new Person4("java03"));
      
       ArrayList<Student4> al1=new ArrayList<Student4>();
       al1.add(new Student4("ja1"));
       al1.add(new Student4("ja2"));
       al1.add(new Student4("ja3"));
       al1.add(new Student4("ja4"));
      
       print(al1);
    }
    public static void print(ArrayList<?extends Person4> al){//占位符  ?
       Iterator<? extends Person4> it=al.iterator();
       while(it.hasNext()){
           System.out.println(it.next().getName());
       }
    }
}
class Person4{
    private String name;
    Person4(String name){this.name=name;}
    public String getName(){return name;}
}
class Student4 extends Person4{
    Student4(String name){ super(name);}
}
```
### Map集合
```java
/* Map集合:该集合存储键值对. 一对一对的往里面存.而且要保证元素的唯一性
    |--HashTable:底层是哈希表结构,不可以存入null键bull值,集合线程是同步的.JDK1.0
    |--HashMap:底层是哈希表结构,可以存入null键bull值,集合线程是不同步的JDK1.2
    |--TreeMap:底层是二叉树数据结构.线程不同步.可以用于给Map集合中键进行排序
 和Set集合很像,其实Set底层就是使用了Map集合
    1,添加  V put(K key, V value) 返回:以前与 key 关联的值，如果没有针对 key 的映射关系，则返回 null
           void putAll(Map<? extends K,? extends V> m)
    2,删除  void clear()
    V remove(Object key)
    3,判断 boolean containsKey(Object key)
          boolean containsValue(Object value)
          boolean isEmpty()
    4,获取 V get(Object key)
          int size()
          Collection<V> values() //返回此映射中包含的值的 Collection 视图
      Set<Map.Entry<K,V>> entrySet()
      Set<K> keySet()   */
import java.util.*;
public class MapDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Map<String,String> map=new HashMap<String,String>();
       map.put("01", "java01");
       map.put("01", "java001");//如果,两个键是一样的,那么后一个键对应的值会覆盖前一个键值,并返回前一个键的值
       map.put("02", "java02");
       map.put("03", "java03");
       //sop("containsKey:"+map.containsKey("02"));//containsKey:true
       //sop("remove:"+map.remove("03"));//remove:java03
       //sop("get:"+map.get("02"));//get:java02
       map.put("04", null);
       sop(map.get("04"));//null 可以通过get方法返回值来判断一个键是否存在. 通过返回null来判断
       //获取Map集合中的所有值
       Collection<String> coll=map.values();
       sop(coll);//[java01, java02, java03, null]
       sop(map);//{01=java01, 02=java02, 03=java03, 04=null}
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
import java.util.*;
/* Map集合的两种取出方式:
    1,Set<K> keySet()
       将Map集合中所有的键存入到Set集合中. 因为Set具备迭代器.
       所以可以用迭代的方式取出所有的键,在根据get()方法.获取每一个键对应的值
       Map集合取出原理:将Map集合转成Set集合,在通过迭代器取出
    2,Set<Map.Entry<K,V>> entrySet()  :将Map集合中的映射关系存储到了Set集合中,
       而这个关系的数据类型是:Map.Entry  */
public class MapDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Map<String,String> map=new HashMap<String,String>();
       map.put("01", "java01");
       map.put("04", "java04");
       map.put("03", "java03");
       map.put("02", "java02");
    /* //先获取map集合的所有键的Set集合,keySet();
       Set<String> set=map.keySet();
       //有了Set集合就可以根据键获取对应的值
       Iterator<String> it=set.iterator();
       while(it.hasNext()){
           String key=it.next();
           sop(map.get(key));
       }  */
       //将Map集合中的映射关系取出,存入到Set集合中
       Set<Map.Entry<String, String>> entry=map.entrySet();
       Iterator<Map.Entry<String, String>> it=entry.iterator();
       while(it.hasNext()){
           Map.Entry<String, String> mapEntry=it.next();
           String key=mapEntry.getKey();
           String value=mapEntry.getValue();
           sop(key+"::"+value);
       }
       //Map.Entry 其实Entry也是一个接口,它是Map接口中的一个内部接口
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
import java.util.*;
/* 每一个学生都有对应的归属地.
   学生Student,地址String
   学生属性:姓名,年龄.
 注意姓名和年龄相同视为同一个学生. 保证学生的唯一性
 思路:   1,描述学生
       2,定义Map容器.将学生作为键,地址作为值,存入集合中
       3,获取Map集合中的元素  */
public class MapTest {
    public static void main(String[] args) {
       HashMap<XueSheng,String> map=new HashMap<XueSheng,String>();
       map.put(new XueSheng("java01",21), "shanghai");
       map.put(new XueSheng("java02",22), "beijing");
       map.put(new XueSheng("java04",24), "guangzhou");
       //map.put(new XueSheng("java04",24), "haha");
       map.put(new XueSheng("java03",23), "tianjing");
       //第一种取出方式:
       Set<XueSheng> set=map.keySet();
       Iterator<XueSheng> it=set.iterator();
       while(it.hasNext()){
           XueSheng xs=it.next();
           String ad=map.get(xs);
           String name=xs.getName();
           int age=xs.getAge();
           sop(name+"::"+age+"::"+ad);
       }
    /*  Map<XueSheng,String> map=new HashMap<XueSheng,String>(); 
           map.put(new XueSheng("java01",21), "shanghai");
           map.put(new XueSheng("java02",22), "beijing");
           map.put(new XueSheng("java04",24), "guangzhou");
           map.put(new XueSheng("java04",25), "guangzhou");
           map.put(new XueSheng("java03",23), "tianjing");
       //第二种取出方式
       Set<Map.Entry<XueSheng, String>> mapEntry=map.entrySet();
       Iterator<Map.Entry<XueSheng, String>> it=mapEntry.iterator();
       while(it.hasNext()){
           Map.Entry<XueSheng, String> mapElement=it.next();
           XueSheng xs=mapElement.getKey();
           String ad=mapElement.getValue();
           String name=xs.getName();
           int age=xs.getAge();
           sop(name+"::"+age+"::"+ad);
       } */
    }
    public static void sop(Object obj){System.out.println(obj);}
}
class XueSheng implements Comparable<XueSheng>{
    private String name;
    private int age;
    private String address;
    XueSheng(String name,int age){
       this.name=name;
       this.age=age;
    }
    public String getName(){return name;}
    public int getAge(){return age;}
    public int hashCode(){return name.hashCode()+age*17;}
    public boolean equals(Object obj){
       if(!(obj instanceof XueSheng2))
           throw new ClassCastException("类型不匹配");
       XueSheng xs=(XueSheng)obj;
       return this.name.equals(xs.name)&&this.age==xs.age;
    }
    public int compareTo(XueSheng xs){//如果没有指定泛型,则参数类型是Object类型
       int num=this.name.compareTo(xs.name);
       if(num==0)
           return new Integer(this.age).compareTo(new Integer(xs.age));
       return num;
    }
}
import java.util.*;
/* 需求:对学生对象的年龄进行升序排序
 因为数据是以键值对的形式存在的,所以要使用可以排序的集合:TreeMap */
public class MapTest2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       TreeMap<XueSheng2,String> tm=new TreeMap<XueSheng2,String>(new XueShengAgeComparator());
       tm.put(new XueSheng2("java01",21), "shanghai");
       tm.put(new XueSheng2("java03",22), "beijing");
       tm.put(new XueSheng2("java02",24), "guangzhou");
       tm.put(new XueSheng2("java04",24), "haha");
       tm.put(new XueSheng2("java04",23), "tianjing");
       Set<XueSheng2> set=tm.keySet();
       Iterator<XueSheng2> it=set.iterator();
       while(it.hasNext()){
           XueSheng2 xs=it.next();
           String ad=tm.get(xs);
           String name=xs.getName();
           int age=xs.getAge();
           sop(name+"::"+age+"::"+ad);
           /*运行结果
           java01::21::shanghai
           java03::22::beijing
           java04::23::tianjing
           java02::24::guangzhou
           java04::24::haha */
       }
    }  
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
//定义一个排序方法,按照学生的年龄进行排序
class XueShengAgeComparator implements Comparator<XueSheng2>{
    public int compare(XueSheng2 xs1,XueSheng2 xs2){
       int num=new Integer(xs1.getAge()).compareTo(new Integer(xs2.getAge()));
       if(num==0)
           return xs1.getName().compareTo(xs2.getName());
       return num;
    }
}
class XueSheng2 implements Comparable<XueSheng2>{
    private String name;
    private int age;
    private String address;
    XueSheng2(String name,int age){
       this.name=name;
       this.age=age;
    }
    public String getName(){return name;}
    public int getAge(){return age;}
    public int hashCode(){return name.hashCode()+age*17;}
    //判断学生是否相同
    public boolean equals(Object obj){
       if(!(obj instanceof XueSheng2))
           throw new ClassCastException("类型不匹配");
       XueSheng2 xs=(XueSheng2)obj;
       return this.name.equals(xs.name)&&this.age==xs.age;
    }
    //让学生具备比较性,并按照姓名进行排序
    public int compareTo(XueSheng2 xs){//如果没有指定泛型,则参数类型是Object类型
       int num=this.name.compareTo(xs.name);
       if(num==0)
           return new Integer(this.age).compareTo(new Integer(xs.age));
       return num;
    }
}
import java.util.*;
/* 练习:"kjdsbuvioniorbauyvyarvoi"获取字符串中字母出现的顺序
 希望打印结果:a(1)b(2)...
 通过结果发现,每一个字母都有对应的次数,说明字母和次数之间都有映射关系
 注意了,当发现有映射关系时,可以选择Map集合,因为Map集合中存放的就是映射关系
 什么时候使用Map集合呢?
    当数据之间存在映射关系,就要想到用Map集合
 思路:1,将字符串转换成字符数组.因为要对每一个字母进行操作.
      2,定义一个Map集合,因为打印的记过的字母有顺序.所以要使用TreeMap集合
      3,遍历字符数组
       将每一个字母作为键去查找Map集合
       如果返回null,就将该字母和1存入到Map集合中
       如果返回不是null,说明该字母在集合中已经存在并有对应的次数,那么就获取该次数,
       并进行自增.然后将该字母和自增后的次数存入到Map集合中.覆盖调用原来的键所队对应的值
    4,将Map中的数据变成指定的字符串形式返回 */
public class MapTest3 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       String s= "aabbccddee";
       char[] chs=s.toCharArray();
       TreeMap<Character,Integer> tm=new TreeMap<Character,Integer>();
       for(int x=0;x<chs.length;x++){
           if(!(tm.containsKey(chs[x]))){
              int num=1;
              tm.put(chs[x], num++);
           }else{
              int num=tm.get(chs[x]);
              tm.put(chs[x], num+1);
           }
       }
       Set<Character> set=tm.keySet();
       Iterator<Character> it=set.iterator();
       //定义一盒缓冲器,用云存储字符串
       StringBuilder sb=new StringBuilder();
       while(it.hasNext()){
           char ch=it.next();
           Integer num=tm.get(ch);
           //sop(ch+"("+num+")");
           sb.append(ch+"("+num+")");
       }
       sop(sb);//a(2)b(2)c(2)d(2)e(2)
    }
    public static void sop(Object obj){System.out.print(obj);}
}
/* Map集合扩展知识
  Map集合被应用是应为具备映射关系
 String    HashMap<String,String>
    班级      班级中的学生
 "yure"     "01"  "zhangsan"
 "yure"     "02"  "lisi"
 "jiuye"    "01"  "wangwu"
 "jiuye"    "02"  "zhaoliu"
           也可以将班级中的学生封装在Student类中  
 一个学校有多个教室.每个教室都有名称,每个教室都有学生*/
import java.util.*;
public class MapExpend {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       printInformation();
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
    public static void printInformation(){
       HashMap<String,HashMap<String,String>> czbk=new HashMap<String,HashMap<String,String>>();
       HashMap<String,String> yure=new HashMap<String,String>();
       HashMap<String,String> jiuye=new HashMap<String,String>();
      
       czbk.put("yure", yure);
       czbk.put("jiuye", jiuye);
      
       yure.put("01", "zhangsan");
       yure.put("02", "lisi");
      
       jiuye.put("01", "wangwu");
       jiuye.put("02", "zhaoliu");
      
       Set<String> set=czbk.keySet();
       Iterator<String> it=set.iterator();
       while(it.hasNext()){
           String banji=it.next();
           sop(banji);
           HashMap<String,String> jiaoshi =czbk.get(banji);
           Iterator<String> ite=jiaoshi.keySet().iterator();
           while(ite.hasNext()){
              String Id=ite.next();
              String name=jiaoshi.get(Id);
              sop(Id+"::"+name);
           }
       }
    }
}
```
### Collections
```java
//集合框架的工具类:Collections:
import java.util.*;
public class CollectionsDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //sortDemo();
       //maxDemo();
       binarySearchDemo();
    }
    public static void binarySearchDemo(){
       List<String> list=new ArrayList<String>();
       list.add("abcd");
       list.add("bcd");
       list.add("ac");
        list.add("cd");
       list.add("d");
       //Collections.sort(list);
       Collections.sort(list,new StrLenComparator());
       sop(list);
//     int num=Collections.binarySearch(list, "cdb");//结果是: 3
//     num的值是:如果搜索键包含在列表中，则返回搜索键的索引；否则返回 (-(插入点) - 1)。
//     sop(num);
//     int num1=halfSearch(list,"cdb");
//     sop(num1);
      
       int num=halfSearch2(list,"abc",new StrLenComparator());
       sop(num);//[d, ac, cd, bcd, abcd] -
    }
    public static int halfSearch(List<String> list,String key){
       int max,min,mid;
       max=list.size()-1;
       min=0;
       while(min<=max){
           mid=(min+max)>>1;
           String str=list.get(mid);
           int index=str.compareTo(key);
           if(index>0)
              max=mid-1;
           else if(index<0)
              min=mid+1;
           else
              return mid;
       }
       return -min-1;
    }
    public static int halfSearch2(List<String> list,String key,Comparator<String> com){
       int max,min,mid;
       max=list.size()-1;
       min=0;
       while(min<=max){
           mid=(min+max)>>1;
           String str=list.get(mid);
           int index=com.compare(str, key);
           if(index>0)
              max=mid-1;
           else if(index<0)
              min=mid+1;
           else
              return mid;
       }
       return -min-1;
    }
    public static void sortDemo(){
       List<String> list=new ArrayList<String>();
       list.add("abcd");
       list.add("bcd");
       list.add("acd");
       list.add("acd");
       list.add("cd");
       sop(list);
       //按照自然顺序进行排序
       //Collections.sort(list);//结果:[abcd, acd, acd, bcd, cd]
       //按照指定的比较器进行比较
       Collections.sort(list,new StrLenComparator());//结果:[cd, acd, acd, bcd, abcd]
       sop(list);
    }
    public static void maxDemo(){
       List<String> list=new ArrayList<String>();
       list.add("abcd");
       list.add("bcd");
       list.add("acd");
       list.add("acd");
       list.add("cd");
       sop(list);
       //String max=Collections.max(list);//结果是:cd
       String max=Collections.max(list,new StrLenComparator());
       //结果是:abcd  最长的那个
       sop(max);
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
class StrLenComparator implements Comparator<String>{
    public int compare(String s1,String s2){
       int num=s1.length()-s2.length();
       if(num==0)
           return s1.compareTo(s2);
       return num;
    }
}
/*
class Student{
}
list.add(new Student());
public static <T extends Comparator<? super T>>void sort(List<T> list){
} */
 
import java.util.*;
public class CollectionsDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //fillDemo();
       List<String> list=new ArrayList<String>();
       list.add("abcd");
       list.add("ac");
       list.add("bcd");
       list.add("cd");
       list.add("d");
//     sop(list);//[abcd, ac, bcd, cd, d]
//     fillDemo(list,1,3,"kk");
//     sop(list);//[abcd, kk, kk, cd, d]
        Collections.replaceAll(list, "ac", "qq");
        sop(list);//[abcd, qq, bcd, cd, d]
    }
    public static void fillDemo(){
       List<String> list=new ArrayList<String>();
       list.add("abcd");
       list.add("ac");
       list.add("bcd");
       list.add("cd");
       list.add("d");
       Collections.sort(list);
       sop(list);// [abcd, ac, bcd, cd, d]
       Collections.fill(list, "kk");
       sop(list);// [kk, kk, kk, kk, kk]
    }
// 练习:fill方法可以将List集合中的所有元素替换成制定元素,现在想将List集合中的部分元素替换成指定元素
    public static void fillDemo(List<String> list,int start,int end,String key){
       //代码改进
       for(;start<end;start++){
           list.set(start, key);
       }
    /*  List<String> li=new ArrayList<String>();
       int n=start;
       for(;start<end;start++){
           li.add(list.get(start));
       }
       //sop("临时集合前:"+li);
       Collections.fill(li, key);
       //sop("临时集合后:"+li);
       int num=end-n;
       for(int x=0;x<num;x++){
           list.remove(n+x);
           list.add(n+x,li.get(x));
       }  */
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
import java.util.*;
/* Collections.reverseOrder(),方法不仅可以逆转默认的排序方式(即相反的排序方式), 还可以逆转已经定义好的比较器的排序方式*/
public class CollectionsDemo3 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       orderDemo();
    }
    public static void orderDemo(){
//     TreeSet<String> ts=new TreeSet<String>(new StrComparator());
//     TreeSet<String> ts=new TreeSet<String>(Collections.reverseOrder());    
       TreeSet<String> ts=new TreeSet<String>(Collections.reverseOrder(new StrLenComparator1()));
       ts.add("abcd");
       ts.add("cd");
       ts.add("acd");
       ts.add("d");  
//     sop(ts);//  [d, cd, acd, abcd]
       sop(ts);//[abcd, acd, cd, d]
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
 
}
class StrComparator implements Comparator<String>{
    public int compare(String s1,String s2){
       return s2.compareTo(s1);
    }
    /*这个方法与  Collections.reverseOrder()效果是一样的*/
}
class StrLenComparator1 implements Comparator<String>{
    public int compare(String s1,String s2){
       int num=s1.length()-s2.length();
       if(num==0)
           return s1.compareTo(s2);
       return num;
    }
}
```
### Arrays
```java
// Arrays: 用于操作数组的工具类. 里面都是静态方法
import java.util.*;
public class ArraysDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
//     int[] arr={2,4,56,7};
//     String str=Arrays.toString(arr);
//     sop(str);
    /*把数组变成List集合有什么好处?
       可以使用集合的思想和方法来操作数组中的数据.
    注意:将数组变成集合,不可以使用集合中跟的增删方法,因为数组中的长度是固定的
    可以使用:
       contains
        get
       indexOf();
       subList();
     如果使用增删操作会发生UnsupportedOperationException,*/
//     String[] arr={"abc","bcd","cde"};
//     List<String> list=Arrays.asList(arr);
//     // list.add("haha");//UnsupportedOperationException
//     sop(list);//[abc, bcd, cde]
      
       int[] arrs={2,4,56,7};//如果将数组改成 Integer[] arrs={2,4,56,7};那么集合的泛型的类型就是Integer
       List<int[]> list=Arrays.asList(arrs);
       /*如果数组中的元素都是对象.那么变成集合时,数组中的元素就直接转成集合中的元素
        如果数组中的元素都是基本数据类型,那么会将该数组作为集合中的元素存在*/
       sop(list);
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
/* 集合变数组
 Collection接口中的toArray方法 */
import java.util.*;
public class ToArrayDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       ArrayList<String> al=new ArrayList<String>();
       al.add("abc1");
       al.add("abc2");
       al.add("abc3");
       /*1,指定类型的数组到底要定义多长呢?
           当指定类型的数组长度小于集合的size,那么该方法内部会创建一个新的数组.长度为集合的size.
           当指定类型的数组长度大于集合的size,就不会创建数组了,二是使用传递进来的数组
           所以创建一个刚刚好的数组最优
        2,为什么要将集合变成数组?
           为了限定对元素的操作.不需要进行增删了.*/
       String[] arr=al.toArray(new String[0]);
       System.out.println(Arrays.toString(arr));
    }
}
```
### 高级for 循环
```java
import java.util.*;
/* 高级for循环:
 格式: for(数据类型 变量名:被遍历的集合(Collection)或者数组){
       }
 对集合进行遍历,只能获取集合中的元素,但是不能对集合进行操作
 
 迭代器除了遍历,还可以对集合中的元素进行remove操作
 如使用了ListIterator,还可以在遍历过程中对集合进行增删改查的动作
 
 传统的for循环和高级for循环有什么区别?
    高级for循环有一个局限性,必须有被遍历的目标. */
public class ForEachDemo {
 
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       ArrayList<String> al=new ArrayList<String>();
       al.add("abc1");
       al.add("abc2");
       al.add("abc3");
       for(String s:al)
           System.out.println(s);//abc1,abc2,abc3
    /*  Iterator<String> it=al.iterator();
       while(it.hasNext()){
           System.out.println(it.next());
       }  */
       int[] arr={1,3,4,5};
       for(int i:arr)
           System.out.println("i:"+i);//i:1,i:3,i:4,i:5
       HashMap<Integer,String> hm=new HashMap<Integer,String>();
       hm.put(1, "a");
       hm.put(2, "b");
       hm.put(3, "c");
       Set<Integer> set=hm.keySet();
       for(Integer i:set)
           System.out.println(i+"::"+hm.get(i));
       Set<Map.Entry<Integer,String>> me=hm.entrySet();
       for(Map.Entry<Integer,String> mapentry:me)
           System.out.println(mapentry.getKey()+"---"+mapentry.getValue());
    }
}
```
### 方法的可变参数
```java
/* JDK1.5版本出现的新特性
    方法的可变参数:使用时注意:可变参数一定要定义在参数列表的最后面 */
public class ParamMethodDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       //show(3,4);
    /*  int[] arr={1,3,4,6,7};
        show(arr);
        int[] arr1={1,2,4,5,6,7};
        show(arr1);
        虽然少定义了多个方法,但是每次都要定义一个数组作为实际参数
        可变参数:
           其实就是上一种数组参数的简写形式,不用每次都手动的建立数组对象
           只要将要操作的元素作为参数传递即可,隐式将这些参数封装成了数组 */
       show(1,3,4,6,7,8,9);
       show("haha",2,3,4,5,8);//haha:5
    }
    public static void show(int... arr){
       System.out.println(arr.length);
    }
    public static void show(String s,int... arr){
       System.out.println(s+":"+arr.length);
    }
/*  public static void show(int a,int b){
       System.out.println(a+b);
    }
    public static void show(int a,int b,int c){
       System.out.println(a+b+c);
    }
    public static void show(int[] arr){
       System.out.println(arr.length);
    } */
}
```
### 静态导入
```java
/* StaticImport: 静态导入
 当类名重名时,需要指定具体的包名
 当方法重名时,需要指定具体的类名 */
import java.util.*;
import static java.util.Arrays.*;//导入了Arrays类中所有的静态成员
import static java.lang.System.*;//导入了System类中所有的静态成员
public class StaticImport {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       int[] arr={3,4,1,2,5};
       sort(arr);//Arrays.sort(arr);
       int index=binarySearch(arr,3);////Arrays.binarySearch(arr,3);
       out.println(index);//System.out.println(index);
       out.println(Arrays.toString(arr));//System.out.println(Arrays.toString(arr));
    }
}
```
## 第十章:其他类
### System
```java
/*System:类中的方法和属性都是静态的
    out:标准的输出流
    in:标准的输入流
 获取系统的一些信息
 获取系统属性信息:Properties getProperties() */
import java.util.*;
public class SystemDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Properties prop =System.getProperties();
       //应为Properties是HashMap集合的子类,也就是Map集合的子类
       //那么可以通过Map集合中的方法取出该元素
       //该集合中存储的都是字符串.没有泛型定义
//     如何在系统中自定义一些特有信息呢信息呢?
       System.setProperty("myKey", "myValue");
//     获取指定属性的信息
       String s=System.getProperty("os.name");//如果名字不存在则返回null
       sop(s);//Windows 7
//     可不可以在虚拟机启动时,动态的加载一些属性呢?
/*     for(Object obj:prop.keySet()){
           Object value=prop.get(obj);
           System.out.println(obj+"::"+value);
       }//结果是一大片信息 */ 
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
### Runtime
```java
/* Runtime:
    该类并没有提供构造函数,说明不可以创建对象,那么会直接想到该类中的方法都是静态的
    发现该类中还有非静态方法,说明该类肯定提供了方法获取本类对象.
    而且该方法是静态的,并且返回值类型是本类类型,由这一点可以看出该类使用了,单例设计模式,
    该方法是 static Runtime getRuntime(); */
public class RuntimeDemo {
    public static void main(String[] args) throws Exception{
       // TODO 自动生成的方法存根
       Runtime run=Runtime.getRuntime();
//     Process p=run.exec("D:\\QQ\\Bin\\QQScLauncher.exe");
//     Process p1=run.exec("notepad.exe");//打开记事本
       Process p2=run.exec("notepad.exe  SystemDemo.java");
//     Thread.sleep(400);
//     p.destroy();//杀掉子进程,QQ杀不掉
//     p1.destroy();//杀掉记事本的进程
    }
}
```
### Date
```java
import java.text.SimpleDateFormat;
import java.util.Date;
/*
 字母  日期或时间元素            
  G    Era标志符 
  y   年  Year 
  M   年中的月份  
  w   年中的周数 
  W   月份中的周数  
  D   年中的天数
  d   月份中的天数
  F   月份中的星期
  E   星期中的天数
  a   Am/pm 标记
  H   一天中的小时数（0-23）
  k   一天中的小时数（1-24）
  K   am/pm 中的小时数（0-11）
  h   am/pm 中的小时数（1-12）
  m   小时中的分钟数
  s   分钟中的秒数 
  S   毫秒数 */
public class DateDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Date d=new Date();
//     System.out.println(d);//Thu Mar 10 10:48:53 CST 2016
                            //打印的时间看不懂,有没有简单点的的呢?
       //将模式封装到SimpleDateFormat对象中
       SimpleDateFormat sdf=new SimpleDateFormat("yyyy年MM月dd日E  hh时mm分ss秒");
       //调用format方法让模式格式化指定Date对象
       String time=sdf.format(d);
       System.out.println(time);//2016年03月10日星期四  11时03分04秒
    }
}
```
### Calendar
```java
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
/*两个练习:
 1,获取任意年的二月有几天
    思路:根据指定的事件设置一个事件就是cal.set(year,2,1),这个是某一年的三月一号
    cal.add(Calendar.DAY_OF_MONTH,-1);向前减一天,就是二月的最后一天,也就是二月中有几天
 2,获取昨天出现的时刻
    调用cal.add(Calendar.DAY_OF_MONTH,-1);这个方法就可以 */
public class CalendarDemo {
    public static void main(String[] args) {
/*     如果只打印年怎么办呢?
       Date d=new Date();
       SimpleDateFormat sdf=new SimpleDateFormat("yyyy年");
       String s=sdf.format(d);
       sop(s);//2016年 */
//当前时间是:2016年三月10日星期四
       Calendar cal=Calendar.getInstance();
//     cal.set(2012, 02,23);//设置时间是:2012年三月23日星期五
//     cal.add(Calendar.MONTH, 4);//将月份向后推四个月    2016年七月10日星期日
       cal.add(Calendar.MONTH, -4);//将月份向前推四个月     2015年十一月10日星期二
       printCalendar(cal);
    }
    public static void printCalendar(Calendar cal){
       String[] months={"一月","二月","三月","四月","五月","六月","七月",
              "八月","九月","十月","十一月","十二月",""};
       String[] weeks={"","星期日","星期一","星期二","星期三","星期四","星期五","星期六"};
//     sop(cal);
//     sop(cal.get(Calendar.YEAR)+"年"+cal.get(Calendar.MONTH)+"月"+
//         cal.get(Calendar.DAY_OF_MONTH)+"星期"+cal.get(Calendar.DAY_OF_WEEK));//2016年2月10
       int month=cal.get(Calendar.MONTH);
       int week=cal.get(Calendar.DAY_OF_WEEK);
       sop(cal.get(Calendar.YEAR)+"年"+months[month]+
              cal.get(Calendar.DAY_OF_MONTH)+"日"
              +weeks[week]);
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
### Math
```java
import java.util.Random;
public class MathDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       save();
    }
//  练习:给定一个小数,并且保留小数的两位精度
    public static void save(){
       Random r=new Random();
       int i=(int)(r.nextDouble()*100);
       double d=i;
       double dou=i/100;
       sop(dou);
    }
    public static void randomDemo(){
       Random r=new Random();
       for(int x=0;x<10;x++){
//         double dou=Math.random();//返回带正号的 double值,该值大于等于 0.0 且小于 1.0。
//         sop(dou);
//         int i=(int)(Math.random()*10+1);//产生1-10之间的随机数
//         sop(i);
           int i1=r.nextInt(10)+1;//产生1-10之间的随机数
           sop(i1);
       }
    }
    public static void mathMethod(){
//     Math.ceil方法的返回的是大于指定数的最小整数
           double d=Math.ceil(12.123);
           sop("d="+d);//d=13.0
           double d1=Math.ceil(-12.123);
           sop("d1="+d1);//d1=-12.0
//     Math.floor(double a) 方法的返回的是小于指定数的最大整数
           double d2=Math.floor(12.123);
           sop("d2="+d2);//d2=12.0
//     Math.round 四舍五入
           double d3=Math.round(12.53);
           sop("d3="+d3);//d3=13.0
//     Math.pow(double a, double b)  返回第一个参数的第二个参数次幂的值。
           double d4=Math.pow(3,2);
           sop("d4="+d4);//d4=9.0
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
## 第十一章:IO流
### Io流
```java
/*  IO流用来处理设备之间的数据传输;java对数据的操作是通过流的方式;java用于操作流的对象都在IO包中;
 流按操作数据分为两种:字节流与字符流
 流按流向分为:输入流与输出流
 字节流的抽象基类:  ImputStream  OutputStream
 字符流的抽象基类:  Reader       Writer
 先学习一下字符流的特点既然IO流是用于操作数据的,那么数据的最常见体现形式是:文件
 需求:在硬盘上创建一个文件并写入一些文字
 找到一个专门用于操作文件的Writer子类对象,FileWriter,后缀名是父类名,前缀名是该流对对象的功能 */
import java.io.*;
public class IODemo {
    public static void main(String[] args) throws IOException{
       // TODO 自动生成的方法存根
//     创建一个FileWriter对象,该对象一被初始化就必须要明确被操作的文件
//     而且该文件会被创建到指定目录下,如果该目录下已有同名文件,则该文件会被覆盖
       FileWriter fw=new FileWriter("E:\\java练习\\Demo.txt");
//     调用Writer中的append方法向流中写入数据
       fw.append("abcdef");
       fw.flush();//刷新流对象中的缓冲的数据,将数据刷到目的地中去
       fw.append("abcdef");
       fw.close();//关闭流资源,但是关闭之前会刷新一次缓冲中的数据.将数据刷到目的地中
//  close和flush的区别:flush刷新以后还可以继续使用该流,close刷新后,会将流关闭
    }
}
```
### Io 异常的处理
```java
import java.io.FileWriter;
import java.io.IOException;
public class FileWriterDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       FileWriter fw = null;//在外部创建对象,在内部初始化
       try{
           fw=new FileWriter("E:\\java练习\\Demo1.txt");
           fw.append("abcdef");
           fw.flush();
       }catch(IOException e){
           System.out.println("catch1"+e.toString());
       }finally{
           try{
              if(fw!=null)//这个判断动作一定要做
                  fw.close();
           }catch(IOException e){
              System.out.println("catch2"+e.toString());
           }  
       }
    }
}
```
### 向已有的文件中读写数据
```java
import java.io.FileReader;
import java.io.IOException;
public class FileReaderDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       FileReader fr=null;
       try{
           fr=new FileReader("E:\\java练习\\Demo.txt");
//     第一种方式读取数据
       /*  int ch=0;
           while((ch=fr.read())!=-1)
              System.out.println((char)ch);*/
//     第二种方式读取数据:通过字符数组进行读取
//         char[] buf=new char[3];
//         int num =fr.read(buf);
//  fr.read(buf)该方法的返回值是往字符数组里面读进去的元素个数,如果读取完毕则返回-1;
//         System.out.println("num="+num+"..."+new String(buf));//num=3...abc
//         int num1 =fr.read(buf);
//         System.out.println("num1="+num1+"..."+new String(buf));//num1=3...def
//         int num2 =fr.read(buf);
//         System.out.println("num2="+num2+"..."+new String(buf));//num2=-1...def
           char[] buf=new char[1024];//一般定义数组的长度是1024的整数倍,即 2K的整数倍
           int num=0;
           while((num=fr.read(buf))!=-1)
              System.out.println(new String(buf,0,num));      
       }catch(IOException e){
           System.out.println("catch1:"+e.toString());
       }finally{
           try{
              if(fr!=null)
                  fr.close();
           }catch(IOException e){
              System.out.println("catch2:"+e.toString());
           }
       }  
    }
}
import java.io.*;
public class FileWriterDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       FileWriter fw=null;
       try{
           fw=new FileWriter("E:\\java练习\\Demo1.txt",true);
              //传递一个true参数,代表不覆盖已有文件.并在已有文件末尾处进行数据续写
           fw.append("hahhahahha\r\nhehehhehehehe");
              //java里面的回车符是由两个转义字符组成的:\r\n
       }catch(IOException e){
           System.out.println("");
       }finally{
           try{
              if(fw!=null)
                  fw.close();
           }catch(IOException e){
              System.out.println("");
           }
       }
    }
}
```
### 读取数据
```java
import java.io.FileReader;
import java.io.IOException;
//读取一个.java文件,并打印在控制台上
public class FileReaderTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       FileReader fr=null;
       try{
           fr=new FileReader("E:\\java练习\\IO流\\src\\FileWriterDemo.java");
           char[] chs=new char[1024];
           int num=0;
           while((num=fr.read(chs))!=-1){
              System.out.print(new String(chs,0,num));//打印语句不能带有换行
           }
       }catch(IOException e){
           System.out.println(e.toString());
       }finally{
           try{
              if(fr!=null)
                  fr.close();
           }catch(IOException e){
              System.out.println(e.toString());
           }
       }
    }
}
```
### 缓冲区
```java
import java.io.*;
/* 缓冲区的出现是为了提高流的操作效率而出现的,所以在创建缓冲区前必须要有流对象
 该缓冲区中提供了跨平台的换行符: newLine(); */
public class BufferedWriterDemo {
    public static void main(String[] args)throws IOException{
       // TODO 自动生成的方法存根
//     创建一个字符流写入对象
       FileWriter fw=new FileWriter("C:\\Users\\ENZ\\Desktop\\文本.txt");
//     为了提高字符写入流效率,加入了缓冲技术,只要将需要被提高效率的流对象作为参数
//     传递给缓冲区的构造函数即可
       BufferedWriter bufw=new BufferedWriter(fw);
       bufw.write("hahhahahha");
//     记住,只要用到缓冲区,就要记得刷新
       bufw.flush();
       bufw.newLine();//缓冲区特有的换行方法
       bufw.write("呵呵呵呵");
       bufw.flush();
       bufw.close();//只需要关闭缓冲区就可以了,不用关闭缓冲区中的流对象
    }
}
import java.io.*;
/* 字符读取流缓冲区
 该缓冲区提供了一个一次读取一行的方法readLine,方便于对文本数据的获取,当返回值是null时,表示读到文件末尾 */
public class BufferedReaderDemo {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
//     创建一个读取流对象和文件相关联
       FileReader fr=new FileReader("C:\\Users\\ENZ\\Desktop\\文本.txt");
//     为了提高效率,加入缓冲技术. 将字符读取流对象作为参数传递给缓冲对象的构造函数
       BufferedReader bufr =new BufferedReader(fr);
       String s=null;
       while((s=bufr.readLine())!=null){
           System.out.println(s);
       }
       bufr.close();
    }
}
import java.io.*;
/* 练习:通过缓冲区复制一个.java文件
 readLine方法的原理:无论是读一行,获取多个字符,其实最终都是在硬盘上一个一个读取.所以还是read方法一次读一个     的方法.读取一个文本行。
 通过下列字符之一即可认为某行已终止：换行 ('\n')、回车 ('\r') 或回车后直接跟着换行。*/
public class BufferedCopyDemo {
    public static void main(String[] args){//throws IOException,下面对这个问题进行了处理
       // TODO 自动生成的方法存根
       FileWriter fw=null;
       FileReader fr=null;
       BufferedWriter bufw=null;
       BufferedReader bufr=null;
       try{
           fw=new FileWriter("C:\\Users\\ENZ\\Desktop\\java文本.txt");
           fr=new FileReader("E:\\java练习\\IO流\\src\\CopyDemo.java");
           bufw=new BufferedWriter(fw);
//还可以这样写:bufw=new BufferedWriter(new FileWriter("文件路径"));
           bufr=new BufferedReader(fr);
           String line=null;
           while((line=bufr.readLine())!=null){
              bufw.write(line);
              bufw.newLine();//因为readLine并没有返回回车符,所以要进行换行
              bufw.flush();//一定记得要刷新缓冲区
           }
       }catch(IOException e){
           System.out.println("文件复制失败");
       }finally{
           try{
              if(bufw!=null)
                  bufw.close();
           }catch(IOException e){
              System.out.println("字符写入流关闭失败");
           }
           try{
              if(bufr!=null)
                  bufr.close();
           }catch(IOException e){
              System.out.println("字符写入流关闭失败");
           }
       }
    }
}
import java.io.*;
/* 将C盘一个文件复制到D盘中
 原理:其实就是将C盘下的文件数据存储到D盘的一个文件中
 步骤:1,在D盘创建一个文件,用于存储C盘文件中的数据
      2,定义读取流和C盘文件进行关联
      3,通过不断的读写完成数据的存储
      4,关闭资源
 C:\\Users\\ENZ\\Desktop\\文本文件.txt */
public class CopyDemo {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
//     copy_1();
       copy_2();
    }
    public static void copy_1()throws IOException{
       FileWriter fw=new FileWriter("C:\\Users\\ENZ\\Desktop\\文本文档_copy_1.txt");
       FileReader fr=new FileReader("C:\\Users\\ENZ\\Desktop\\文本文档.txt");
       int num=0;
       while((num=fr.read())!=-1){
           fw.write(num);
       }
       fw.close();
       fr.close();
    }
//  复制文件的第二种方法,一定要掌握
    public static void copy_2()throws IOException{
       FileWriter fw=null;
       FileReader fr=null;
       try{
           fw=new FileWriter("C:\\Users\\ENZ\\Desktop\\文本文档_copy_2.txt");
           fr=new FileReader("C:\\Users\\ENZ\\Desktop\\文本文档.txt");
           char[] chs=new char[1024];
           int num=0;
           while((num=fr.read(chs))!=-1){
              fw.write(chs,0,num);
           }
       }catch(IOException e){
           System.out.println("文件复制失败");
       }finally{
           try{
              if(fw!=null)
                  fw.close();
           }catch(IOException e){
              System.out.println("写入流关闭失败");
           }
           try{
              if(fr!=null)
                  fr.close();
           }catch(IOException e){
              System.out.println("读取流关闭失败");
           }
       }
    }
}
```
### 添加行号:
```java
import java.io.*;
public class LineNumberReaderDemo {
    public static void main(String[] args) throws IOException{
       // TODO 自动生成的方法存根
       FileReader fr=new FileReader("E:\\java练习\\IO流\\src\\CopyDemo.java");
       LineNumberReader lin=new LineNumberReader(fr);
       String line=null;
       lin.setLineNumber(0);//行号从1开始;即是:设置的行号+1,为初始行号
       while((line=lin.readLine())!=null){
           System.out.println(lin.getLineNumber()+"::"+line);
       }  
    }
}
```
### 模拟一个readLine方法:
```java
import java.io.*;
/* 模拟一个readLine方法(这个模拟就是一个:装饰设计模式)
 装饰设计模式:   当想要对已有的对象进行功能增强时,可以定义一个类,将已有的对象传入,基于原有的功能,并提供加强            功能,那么自定义的类成为装饰类
 装饰类通常会通过构造方法接收被装饰的对象,并基于被装饰的对象的功能,提供更强的功能
 
 装饰模式比继承要灵活,避免了继承体系的臃肿,而且大大降低了类与类之间的关系
 装饰类因为增强已有对象,具备的功能和已有对象是相同的,只不过提供了更强的功能
 所以装饰类和被装饰类通常都是属于一个体系中的  */
public class MyBufferedReader {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
       FileReader fr=new FileReader("E:\\java练习\\IO流\\src\\CopyDemo.java");
       MyBuffered mb=new MyBuffered(fr);
       String s=null;
       while((s=mb.myreadLine())!=null){
           System.out.println(s);
       }
       mb.myClose();
    }
}
//装饰设计模式
class MyBuffered{
    private FileReader fr;
    MyBuffered(FileReader fr){
       this.fr=fr;
    }
//可以一次读一行的方法
    public String myreadLine()throws IOException{
       int ch=0;
// 定义一个临时容器,原BufferedReader封装的是字符数组,为了演示的方便
// 定义一个StringBuilder容器,因为还要将数据转成字符串形式返回
       StringBuilder s=new StringBuilder();
       while((ch=fr.read())!=-1){
           if(ch=='\r')
              continue;
           if(ch=='\n')
              return s.toString();
           else
              s.append((char)ch);
       }
       if(s.length()!=0)
           return s.toString();
       return null;
    }
    public void myClose()throws IOException{
       fr.close();
    }
}
```
### 模拟一个setLineNumber()方法
```java
import java.io.*;
class MyLineNumber extends MyBuffered {
//简化下面的代码,让该类继承MyBuffered类,然后简化代码书写
    private int lineNumber;       //
    MyLineNumber(FileReader r){
       super(r);
    }
    public void setLineNumber(int lineNumber){
       this.lineNumber=lineNumber;
    }
    public int getLineNumber(){
       return lineNumber;
    }
    public String myReadLine() throws IOException{
       lineNumber++;
       return super.myreadLine();
    }
/*  这是没有继承MyBuffer类,的全部代码;当代码很臃肿
    private int lineNumber ;
    private FileReader fr;
    MyLineNumber(FileReader fr){
       this.fr=fr;
    }
    public void setLineNumber(int lineNumber){
       this.lineNumber=lineNumber;
    }
    public int getLineNumber(){
       return this.lineNumber;
    }
    public String myreadLine()throws IOException{
       lineNumber++;
       StringBuilder buf=new StringBuilder();
       int num=0;
       while((num=fr.read())!=-1){
           if(num=='\r')
              continue;
           else if(num=='\n')
              return buf.toString();
           else
              buf.append((char)num);
        }
        if(buf.length()!=0)
           return buf.toString();
        return null;
     }
     public void myClose() throws IOException{
        fr.close();
     }*/
}
public class MyLineNumberReader {
    public static void main(String[] args) throws IOException {
       // TODO 自动生成的方法存根
       FileReader fr=new FileReader("E:\\java练习\\IO流\\src\\CopyDemo.java");
       MyLineNumber ml=new MyLineNumber(fr);
       String s=null;
       ml.setLineNumber(0);
       while((s=ml.myreadLine())!=null){
           System.out.println(ml.getLineNumber()+"::"+ s);
       }
       ml.myClose();
    }
}
```
### 字节流
```java
import java.io.*;
/* 字符流:FileReader    FileWriter
          BufferedReader   BufferedWriter
 字节流:OutputStream  InputStream
 需求想要操作图片数据.这时就要用到字节流  */
public class FileStream {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
       writerFile();
//     readFile_1();
//     readFile_2();
       readFile_3();
    }
    public static void writerFile()throws IOException{
       FileOutputStream fo=new FileOutputStream("C:\\Users\\ENZ\\Desktop\\nihao.txt");
       fo.write("abcdef".getBytes());
       fo.close();
    }
    public static void readFile_1()throws IOException{
       FileInputStream fi=new FileInputStream("C:\\Users\\ENZ\\Desktop\\nihao.txt");
       int num=0;
       while((num=fi.read())!=-1){
           System.out.print((char)num);//abcdef
       }
       System.out.println();
       fi.close();
    }
    public static void readFile_2()throws IOException{
       FileInputStream fi=new FileInputStream("C:\\Users\\ENZ\\Desktop\\nihao.txt");
       int num=0;
       byte[] b=new byte[1024];
      
       while((num=fi.read(b))!=-1){
           System.out.println(new String(b,0,num));//abcdef
       }
       fi.close();
    }
    public static void readFile_3()throws IOException{
       FileInputStream fi=new FileInputStream("C:\\Users\\ENZ\\Desktop\\nihao.txt");
       int len=fi.available();//返回文件的字节个数
       byte[] b=new byte[len];//定义一个大小刚刚好的数组缓冲区.不用在循环了.
       fi.read(b);
       System.out.println(new String(b));//abcdef
       fi.close();
    }
}
import java.io.*;
/*  复制一个图片
 思路:  1,用字节读取流对象和图片关联
       2,用字节写入流创建一个图片文件,用于存储获取到的图片数据
       3,通过循环读写,完成数据的存储
       4,关闭资源 */
public class CopyPicture {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       FileInputStream in = null;
       FileOutputStream out=null;
       try{
           in=new FileInputStream("C:\\Users\\ENZ\\Desktop\\图片.jpg");
           out=new FileOutputStream("C:\\Users\\ENZ\\Desktop\\图片copy.jpg");
           byte[] b=new byte[1024];
           int len=0;
           while((len=in.read(b))!=-1){
//            out.write(b);
              out.write(b, 0, len);//应该写入有效数据
           }
       }catch(IOException e){
           System.out.print("图片复制失败");
       }finally{
           try{
              if(in!=null)
                  in.close();
           }catch(IOException e){
              System.out.print(e.toString());
           }
           try{
              if(out!=null)
                  out.close();
           }catch(IOException e){
              System.out.print(e.toString());
           }
       }
    }
}
import java.io.*;
public class CopyMusic {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       long start=System.currentTimeMillis();
       CopyMusic();
       long end=System.currentTimeMillis();
       System.out.println("复制所用时间是:"+(end-start));
    }
    public static void CopyMusic(){
//     FileInputStream in = null;
//     FileOutputStream out=null;
 
       BufferedInputStream bufin = null;
       BufferedOutputStream bufout = null;
       try{
//         in=new FileInputStream("C:\\Users\\ENZ\\Desktop\\一千个伤心的理由.mp3");
//         out=new FileOutputStream("C:\\Users\\ENZ\\Desktop\\一千个伤心的理由-1.mp3");
//  优化代码,加入缓冲区
           bufin=new BufferedInputStream(new FileInputStream("C:\\Users\\ENZ\\Desktop\\一千个伤心的理由.mp3"));
           bufout=new BufferedOutputStream(new FileOutputStream("C:\\Users\\ENZ\\Desktop\\一千个伤心的理由-1.mp3"));
           byte[] b=new byte[1024*1024];
           int len=0;
           while((len=bufin.read(b))!=-1){
//            out.write(b);
              bufout.write(b, 0, len);//应该写入有效数据
           }
       }catch(IOException e){
           System.out.print("图片复制失败");
       }finally{
           try{
              if(bufin!=null)
                  bufin.close();
           }catch(IOException e){
              System.out.print(e.toString());
           }
           try{
              if(bufout!=null)
                  bufout.close();
           }catch(IOException e){
              System.out.print(e.toString());
           }
       }
    }
}
import java.io.*;
public class CopyMusic2 {
    public static void main(String[] args) throws IOException{
       // TODO 自动生成的方法存根
       long start=System.currentTimeMillis();
       CopyMusic();
       long end=System.currentTimeMillis();
       System.out.println("复制所用时间是:"+(end-start)+"毫秒");
    }
    public static void CopyMusic()throws IOException{
       MyBufferedInputStream bufin=new MyBufferedInputStream(new                             FileInputStream("C:\\Users\\ENZ\\Desktop\\一千个伤心的理由.mp3"));
       BufferedOutputStream bufout=new BufferedOutputStream(new FileOutputStream("C:\\Users\\ENZ\\Desktop\\一千个伤心的理由-2.mp3"));
       int len=0;
       while((len=bufin.myRead())!=-1){
           bufout.write(len);
       }
       bufin.myClose();
       bufout.close();
    }
}
class MyBufferedInputStream {
    private InputStream in;
    private int pos=0,count=0;
    private byte[] buf=new byte[1024*1024];
    MyBufferedInputStream(InputStream in){
       this.in=in;
    }
    public int myRead()throws IOException{
//  通过in对象读取硬盘上的数据.
//     先调用InputStream中的read方法把一组数据存放到缓冲区中
//     然后缓冲区在一次一次的调用read方法读取数组中的数据,直到把数组中的数据去完为止.
//     然后缓冲区再调用InputStream中的read方法把一组数据存放到缓冲区中
//     然后在一次一次的取出数据
       if(count==0){
           count=in.read(buf);
           if(count<0)
              return -1;
           pos=0;//将pos置0,否则文件将会变得很大
           byte b=buf[pos];
           count--;
           pos++;
           return b&255;
       }else if(count>0){
           byte b=buf[pos];
           count--;
           pos++;
           return b&0xff;
       }
       return -1;
    }
    public void myClose()throws IOException{
       in.close();
    }
}
import java.io.*;
/*  读取键盘录入
 System.out :对应的是标准的输出设备---控制台
 System.in :对应的是标准的输入设备---键盘
 需求:通过键盘录入数据,当录入一行数据后,就将该数据进行打印,如果录入的是over,那么就停止录入
 
 通过刚才的键盘录入一行数据并打印其大写,发现原理其实就是读一行数据的原理,也就是readLine方法
 能不能直接使用readLine方法来完成键盘录入的一行数据的读取呢?
 readLine方法是字符流BufferedReader类中的方法,而键盘录入的read方法是字节流InputStream的方法,那么能不能将字节流转换成字符流,再使用字符流缓冲区中的readLine方法呢 */
public class TransStreamDemo {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
//     readKeyBoard();
       transStream();
/*  如果只输入一个a,那么敲击回车之后,打印出来三个数 97  13  10 后面两个数对应的是回车符'\r','\n'
       int x=in.read();
       sop(x);//97
       int x1=in.read();
       sop(x1);//13
       int x2=in.read();
       sop(x2);//10*/
    }
//  读取键盘录入的一行数据并转换成大写输出到控制台上
    public static void readKeyBoard()throws IOException{
       InputStream in=System.in;
       StringBuilder sb=new StringBuilder();
       while(true){
           int a=in.read();
           if(a=='\r')
              continue;
           else if(a=='\n'){
              String s=sb.toString();
              if("over".equals(s))
                  break;
              sop(s.toUpperCase());
              sb.delete(0, sb.length());
           }else
              sb.append((char)a);
       }
       in.close();
    }
//     将字节流对象转换成字符流对象
    public static void transStream()throws IOException{
//  获取键盘录入对象
//     InputStream in=System.in;
//  将字节流对象转换成字符流对象,使用转换流 InputStreamReader
//     InputStreamReader isr=new InputStreamReader(in);
//  为了提高效率,将字符串进行缓冲区技术高效操作.使用 BufferedReader     
//     BufferedReader br=new BufferedReader(isr);
//将上面的三句话转换成一句话
       BufferedReader bufr=
              new BufferedReader(new InputStreamReader(System.in));
//-------------------------------------------------     
//     OutputStream out=System.out;
//     OutputStreamWriter osw=new OutputStreamWriter(out);
//      BufferedWriter bufw=new BufferedWriter(osw);
//将上面的三句话转换成一句话
       BufferedWriter bufw=
              new BufferedWriter(new OutputStreamWriter(System.out));
       String line=null;
       while((line=bufr.readLine())!=null){
           if("over".equals(line))
              break;
//         sop(line.toUpperCase());可以将这句话转换成下面的话
           bufw.write(line);
           bufw.newLine();
           bufw.flush();
       }
       bufr.close(); 
       bufw.close();
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
### 流操作的基本规律
```java
import java.io.*;
/*
 1,需求:想把键盘录入的数据存打印到控制台上
    源:键盘录入    System.in
    目的:控制台 System.out
 2,需求:想把键盘录入的数据存储到一个文件中
    源:键盘 System.in
    目的:文件   new FileOutputStream("C:\\Users\\ENZ\\Desktop\\文本文档.txt")
 3,需求:想要将一个文件的数据打印到控制台上
    源:文件   new FileInputStream("C:\\Users\\ENZ\\Desktop\\文本文档.txt")
    目的:控制台   System.out
 流操作的基本规律:
    最痛苦的是流对象有很多,不知道改用那一个
 通过三个明确来完成
    1,明确源和目的
       源:输入流  InputStream  Reader
       目的:输出流  OutputStream  Writer
    2,操作的数据是不是纯文本?
       是: 用字符流
       不是: 用字节流
    3,当体系明确后在明确要使用哪个具体的对象
       通过设备来区分
           源设备:内存,硬盘,键盘
           目的设备:内存,硬盘,控制台
 例:1,将一个文本文件中的数据存储到另一个文件中---复制文件
      该题中要操作的对象是文本文件 所以要用名字开头是File的流对象
       1,源:硬盘上的文本文件. 所以应该使用输入流中的操作字符流的对象   FileReader
       2,目的:存储到硬盘上. 所以应该使用输出流中的操作字符流的对象    FileWriter
        3,是否需要提高效率? 如果要则要使用  字符流   缓冲区
    2,将键盘录入的数据保存到一个文件中
      该题中要操作的对象是文本文件,因为从键盘录入的都是字节流,所以需要将字节流转换成字符流,以方便操作.
        源:键盘录入   System.in这是字节流,要转换成字符流所以,new InputStreamReader(System.in);
        目的:硬盘上的文本   FileWriter(文件路径);  
        需要提高效率吗?需要则加入 BufferedReader  BufferedWriter
    扩展  --------------------------------
        在该例中FileWriter使用的默认的编码表utf-8,如果想按照指定的编码表来操作流,则要使用的对象是OutputStreamWriter
        而该转换流对象要接收一个字节输出流(OutputStream),而且还是一个可以操作文件的字节输出流,所以要使用 FileOutputStream
           如果需要高效,则要使用缓冲区BufferedWriter
      代码体现就是:
      BufferedWriter bufw=new BufferedWriter(new OutputStreamWriter(new FileOutputStream("c:\\d.txt"),"UTF-8")); */
public class TransStreamDemo2 {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
       transStream();
    }
    public static void transStream()throws IOException{
//     可以将System类中默认的输入输出改变成想要的 
//  改变源:     System.setIn( InputStream in);
//  改变目的:   System.setOut( PrintStream p);
       System.setIn(new FileInputStream("C:\\Users\\ENZ\\Desktop\\文本文档.txt"));
       System.setOut(new PrintStream("hahahah哈哈.txt"));//文件出现在了E:\java练习\IO流
//     源:
       BufferedReader bufr=new BufferedReader(new InputStreamReader(System.in));
//     目的:
       BufferedWriter bufw=new BufferedWriter(new OutputStreamWriter(System.out));
       String line=null;
       while((line=bufr.readLine())!=null){
           if("over".equals(line))
              break;
           bufw.write(line);
           bufw.newLine();
           bufw.flush();
       }
       bufr.close();
       bufw.close();
    }
}
```
### 获取系统信息
```java
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Properties;
public class SystemInfo {
    public static void main(String[] args) throws FileNotFoundException {
       // TODO 自动生成的方法存根
       Properties p=System.getProperties();
       System.setOut(new PrintStream("system-information.txt"));
       p.list(System.out);
    }
}
import java.io.*;
import java.text.*;
import java.util.*;
//异常的日志信息
public class ExceptionInfo {
    public static void main(String[] args){
       // TODO 自动生成的方法存根
       try {
           PrintStream p=new PrintStream("");
       } catch (FileNotFoundException e2) {
           // TODO 自动生成的 catch 块
           try{
              Date d=new Date();
              SimpleDateFormat sdf=new SimpleDateFormat("yyyy年MM月dd日  HH:mm:ss");
              String s=sdf.format(d);
              PrintStream ps=new PrintStream("exception.log");
              ps.println(s);
              System.setOut(ps);
           }catch(Exception e1){
                  throw new RuntimeException("日志创建失败");
           }
           e2.printStackTrace(System.out);
       }
    }
}
```
### File 类
```java
import java.io.*;
/* File类的常见方法:
    1,创建
       boolean createNewFile() :在指定位置创建文件,如果已存在则不创建返回false
    2,删除
       boolean delete() 文件删除, 失败返回假
       void deleteOnExit() //在程序退出时删除指定文件
    3,判断
       boolean canExecute() 文件是否可执行
       boolean canRead()
       boolean canWrite()
       *boolean exists() 文件是否存在
       *boolean mkdir() 创建此抽象路径名指定的目录。 只能创建一级目录
       *boolean mkdirs() 创建此抽象路径名指定的目录。 创建多级目录
        *boolean isFile() 判断是否是文件
        *boolean isDirectory() 判断是否是目录
        *boolean isHidden() 文件是否是一个隐藏文件。
        boolean isAbsolute() 判断文件路径是否是绝对路径
    4,获取信息
       String getName() 返回由此抽象路径名表示的文件或目录的名称。
       String getParent() 返回此抽象路径名父目录的路径名字符串,如果没有则返回null
       String getPath()
       File getAbsoluteFile()  返回此抽象路径名的绝对路径名形式。
       String getAbsolutePath() 返回此抽象路径名的绝对路径名字符串。
      
       long length() 返回由此抽象路径名表示的文件的长度。
       long lastModified() 返回此抽象路径名表示的文件最后一次被修改的时间。
      
       boolean renameTo(File dest) 重新命名此抽象路径名表示的文件。 */
public class FileDemo {
    public static void main(String[] args) throws IOException {
       // TODO 自动生成的方法存根
//     createFile();
       fileMethod();
    }
//创建File对象
    public static void createFile(){
//     将a.txt封装成对象.可以将已有的或者未出现的文件或者文件夹封装成对象
       File f1=new File("a.txt");
//     将父路径和子路径分开封装
       File f2=new File("C:\\abc","a.txt");
       File d=new File("C:\\abc");
       File f3=new File(d,"a.txt");
       sop(f1);//a.txt
       sop(f2);//C:\abc\a.txt
       sop(f3);//C:\abc\a.txt
    }
    public static void fileMethod() throws IOException{
//     File d=new File("file.txt");//创建一个新 File 实例。
//     sop("create:"+d.createNewFile());//文件不存在则返回true,文件存在则返回false
//     d.deleteOnExit();
//     sop(d.delete());
//     sop(d.canExecute());//true
//     sop(d.exists());//true
//创建目录
//     File f=new File("D:\\haha\\hehe\\heihei");
//     sop(f.mkdir());//true  "D:\\haha"
//     sop(f.mkdirs());//true "D:\\haha\\hehe\\heihei"
//判断是否是文件或者目录
//     File d1=new File("file.txt");
//  记住:判断是否是文件或者目录时,必须先要判断该文件对象封装的内容是否存在,通过exists判断
//     sop(d1.exists());
//     sop("dir:"+d1.isDirectory());//dir:false
//     sop("file:"+d1.isFile());//如果文件存在则 file:true
//获取文件路径
//     File f1=new File("D:\\abc\\file.txt");
//    
//     sop(f1.getName());//file.txt
//     sop(f1.getParent());//c:\abc
//     sop(f1.getAbsolutePath());//c:\abc\file.txt
//     sop(f1.getPath());//c:\abc\file.txt  文件设置是什么就返回什么
//     sop(f1.length());//返回由此抽象路径名表示的文件的长度。
//重新命名此抽象路径名表示的文件。
       File f3=new File("E:\\哈哈.txt");
       File f4=new File("D:\\嘿嘿.txt");
//     sop(f3.renameTo(f4));//这是在E:\\下的操作  哈哈.txt--->嘿嘿 .txt
       sop(f3.renameTo(f4));//这是在 E:\\ 哈哈.txt--->D:\\嘿嘿 .txt            
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
//(如果设置了断点,会让程序暂挂,导致程序不能运行,解决办法就是禁用断点)
}
import java.io.*;
public class FileDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
//     listRootDemo();
//     listDemo();
//     listDemo2();
       listFileDemo();
    }
//查看系统目录
    public static void listRootDemo(){
       File[] files=File.listRoots();
       for(File f:files)
           System.out.println(f);
    }
//查看指定目录下的所有文件
    public static void listDemo(){
       File f=new File("D:\\");
//  调用list方法的File对象必须是封装了一个目录,该目录还必须存在
       String[] arr=f.list();
       for(String s:arr)
           System.out.println(s);
    }
//筛选指定名称的文件,并打印
    public static void listDemo2(){
       File f=new File("E:\\java练习\\Item1\\src");
       String[] arr=f.list(new FilenameFilter(){//该接口只有一个方法,所以选用匿名内部内的方式
           public  boolean accept(File dir,String name){
//            System.out.println("dir:"+dir+"...name:"+name);//打印的是该目录名加上目录下的文件名
//            return true;如果返回ture则将该目录下的所有文件都返回给arr
              return name.endsWith(".java");
           }
       });
       System.out.println(arr.length);//8
       for(String s:arr)
           System.out.println(s);
    }
 
    public static void listFileDemo(){
       File f=new File("E:\\java练习\\Item1\\src");
       File[] files=f.listFiles();
       for(File ff:files)
           System.out.println(ff.getParent()+".."+ff.getName()+":::"+ff.length());
    }
}
import java.io.*;
/*   递归:函数自己调用自己
 需求:列出指定目录下的文件或者文件加,包含子目录中 的内容,也就是列出指定目录下所有内容
 
 因为目录中还有目录,只要使用同一个使用列出目录功能的函数完成即可
 在列出过程中出现的还是目录的话,还可以在此调用本功能,也就是调用自身
 这种表现形式,或者编程手法称之为:递归
 递归要注意的事项:
       1,限定条件
       2,限定递归次数,避免内存溢出  */
public class FileDemo3 {
    public static void main(String[] args){
       // TODO 自动生成的方法存根
       showDir(new File("D:\\迅雷"),0);
    }
    public static void showDir(File dir,int level){
       File[] arr=dir.listFiles();
       level++;
       for(int x=0;x<arr.length;x++){
           if(arr[x].isDirectory()){
              showDir(arr[x],level);
           }else
              System.out.println(getLevel(level-1)+arr[x]);
       }
    }
    public static String getLevel(int level){
       StringBuilder s=new StringBuilder();
       for(int x=0;x<level;x++){
           s.append("    ");
       }
       return s.toString();
    }
}
```
### 删除Directory
```java
import java.io.*;
/*  删除一个带内容的目录
 删除原理:在windows中删除目录是从里面往外面删除的
 既然是从里面往外面删除,所以就要用到递归  */
public class RemoveDir {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       removeDir(new File("E:\\Data1"));
    }
    public static void removeDir(File dir){
       if(dir.exists()){
           File[] files=dir.listFiles();
           for(int x=0;x<files.length;x++){
              if(files[x].isDirectory())
                  removeDir(files[x]);
              System.out.println(files[x]+"..file.."+files[x].delete());
           }
           System.out.println("dir::"+dir.delete());//dir这个目录必须为空,才能将该目录删除
       }
    }
}
import java.io.*;
import java.util.*;
/*  练习:将一个指定目录下的java文件的绝对路径,存储到一个文本文件中,建立一个java文件列表
思路:
    1,对指定目录进行递归
    2,获取递归过程中的java文件路径
    3,将这些路径存储到一个集合中
    4,将集合中的数据写入到一个文本文件中 */
public class JavaFileList {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
       MyMethod();
       TeacherMethod();
    }
    public static void TeacherMethod()throws IOException{
       File f=new File("E:\\新建文件夹");
       List<File> li=new ArrayList<File>();
       List<File> list=fileToList(f,li);
//     for(File file:list){
//         System.out.println(file.getAbsolutePath());
//     }
       writeToFile(list);
    }
    public static List fileToList(File f,List<File> list){
       File[] files=f.listFiles();
       for(File file:files){
           if(file.isDirectory())
              fileToList(file,list);
           list.add(file);
       }
       return list;
    }
    public static void writeToFile(List<File> list)throws IOException{
       BufferedWriter bufw=new BufferedWriter(new FileWriter("E:\\javalist1.txt"));
       for(File f:list){
           bufw.write(f.getAbsolutePath());
           bufw.newLine();
           bufw.flush();
       }  
       bufw.close();
    }
//---------------------------------------------------------------
    public static void  MyMethod()throws IOException{
       System.setOut(new PrintStream("E:\\javalist2.txt"));
       BufferedWriter bufw=new BufferedWriter(new OutputStreamWriter(System.out));
       javaFileList(new File("E:\\新建文件夹"),bufw);
    }
    public static void javaFileList(File dir,BufferedWriter bufw)throws IOException{
       File[] ff=dir.listFiles();
       for(int x=0;x<ff.length;x++){
           if(ff[x].isDirectory())
              javaFileList(ff[x],bufw);
           bufw.write(ff[x].getAbsolutePath());
           bufw.newLine();//再次记住,不要忘记加换行,否则,输出的文件没有分行
           bufw.flush();
       }
    }
}
```
### Properties:  集合与IO技术相结合的集合容器
```java
import java.util.*;
import java.io.*;
/*  Properties 是HashTable的子类,也就是说它具备Map集合的特点.而且它里面存储的键值对(要保证键的唯一性)都是字符串
 是集合中和IO技术相结合的集合容器
 该对象的特点:可以用于键值对形式的配置文件
 那么在加载数据时需要有固定格式 */
public class PropertiesDemo {
    public static void main(String[] args) throws Exception{
       // TODO 自动生成的方法存根
//     setAndGet();
//     method_1();
       method_2();
    }
    public static void setAndGet(){
       Properties pro=new Properties();
       pro.setProperty("zhangsan", "30");
       pro.setProperty("lisi", "20");
//     System.out.println(pro);//{zhangsan=30, lisi=20}
//  获取元素
//     String s=pro.getProperty("zhangsan");
//     sop(s);//30
//  设置元素
       pro.setProperty("lisi01", "24");//如果Properties中没有该键,则会将其作为一个新的键值对存进去
       sop(pro.getProperty("lisi"));//24
//  遍历元素
       Set<String> name=pro.stringPropertyNames();
       for(String s:name)
           sop(s+"::"+pro.getProperty(s));//zhangsan::30 lisi::20
    }
/*  演示,如何将流中的数据存储到集合中
 想要将E:\java练习\IO流\info.txt文件中的键值数据存到集合中进行操作
    1,用一个流和文件相关联
    2,读取一行数据,将该数据用"="进行切割
    3,将等号左边为键,右边为值,存入到Properties集合中即可  */
    public static void method_1() throws Exception{
       BufferedReader bufr=new BufferedReader(new FileReader("E:\\java练习\\IO流\\info.txt"));
       Properties pro=new Properties();
       String line=null;
       while((line=bufr.readLine())!=null){
           String[] str=line.split("=");
           pro.setProperty(str[0], str[1]);
       }
       bufr.close();
       sop(pro);
    }
//method_2方法中的load方法的原理就是method_1
    public static void method_2() throws Exception{
       Properties pro=new Properties();
       FileInputStream fis=new FileInputStream("E:\\java练习\\IO流\\info.txt");
        pro.load(fis);
       sop(pro);//{zhangsan=30, lisi=20, zhouwu=10}
    //发现zhouwu的年龄错了
       pro.setProperty("zhouwu", "44");
//     sop(pro);
       FileOutputStream fos=new FileOutputStream("E:\\java练习\\IO流\\info.txt");
       pro.store(fos, "haha");//将Properties表中的属性列表键值对写入输出字符,并带上注释
       pro.list(System.out);//将属性列表输出到指定的输出流
       fis.close();
       fos.close();
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
### RunCount 运行次数限定:
```java
import java.io.*;
import java.util.*;
/*  用于记录应用成语的运行次数,如果使用次数已到规定的次数,那么给出注册提示
 很容易想到的是计数器,可是该计数器定义在程序中,随着程序的运行而在内存中存在,并进行自增
 可是随着应用程序的退出,该计数器也在内存中消失了,下一次在启动改程序时,有重新开始计数,这样不是我们想要的.
 程序即使结束了,该计数器的值也存在,下次程序启动会先加载该计数器并加一后在重新存储起来,所以要建立一个配置文件,用于记录该软件的使用次数
 该配置文件使用键值对的形式存在,这样便于阅读,并操作数据
 键值对数据是Map集合,数据是以文件形式存储,使用IO技术
 那么 Map+IO--->Properties
  配置文件可以实现应用程序数据的共享 */
public class RunCountDemo {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
       Properties prop=new Properties();
       File f=new File("count.ini");//先把文件封装成对象
       if(!(f.exists()))
           f.createNewFile();
       BufferedReader bufr=new BufferedReader(new InputStreamReader(new FileInputStream(f)));
       prop.load(bufr);
       String value=prop.getProperty("time");
       int count=0;
       if(value!=null){
           count=Integer.parseInt(value);
           if(count>=5){
              System.out.println("您好,试用次数已到,请注册");
              return ;
           }
       }
       count++;
       prop.setProperty("time", count+"");
       BufferedWriter bufw=new BufferedWriter(new OutputStreamWriter(new FileOutputStream(f)));
       prop.store(bufw, "");
       bufw.close();
       bufr.close();
    }
}
```
### 打印流
```java
import java.io.*;
/* 打印流:
    1,字节打印流:PrintStream
       构造函数可以接受的参数类型
           1,File对象  File
           2,字符串路径  String
           3,字节输出流   OutputStream
    2,字符打印流PrintWriter
       构造函数可以接受的参数类型
           1,File对象  File
           2,字符串路径  String
           3,字节输出流   OutputStream
           4,字符输出流   Writer   */
public class PrintDemo {
    public static void main(String[] args) throws IOException{
       // TODO 自动生成的方法存根
       BufferedReader bufr=new BufferedReader(new InputStreamReader(System.in));  
//     PrintWriter pw=new PrintWriter(System.out,true);//将键盘录入问信息打印在控制台上,自带刷新功能
//     PrintWriter pw=new PrintWriter("printDemo.txt");//将键盘录入问信息,打印到指定目录下的文件中不带自动刷新
       PrintWriter pw=new PrintWriter(new FileWriter("printDemo1.txt"),true);//将键盘录入问信息,打印到指定目录下的文件中,并带自动刷新
       String line=null;
       while((line=bufr.readLine())!=null){
           if("over".equals(line))
              break;
           pw.println(line.toUpperCase());
//         pw.flush();
       }
       pw.close();
       bufr.close();
    }
}
```
### SequenceInputStream
```java
import java.io.*;
import java.util.*;
/*  它从输入流的有序集合开始，并从第一个输入流开始读取，直到到达文件末尾，接着从第二个输入流读取，依次类推，
 直到到达包含的最后一个输入流的文件末尾为止。
 如果有多个输入流,需要用到 Enumeration迭代器  */
public class SequenceDemo {
    public static void main(String[] args) throws IOException{
       // TODO 自动生成的方法存根
       Vector<FileInputStream> v=new Vector<FileInputStream>();
       v.add(new FileInputStream("E:\\java练习\\IO流\\1.txt"));
       v.add(new FileInputStream("E:\\java练习\\IO流\\2.txt"));
       v.add(new FileInputStream("E:\\java练习\\IO流\\3.txt"));
       Enumeration e=v.elements();
       SequenceInputStream sis=new SequenceInputStream(e);
       FileOutputStream fos=new FileOutputStream("E:\\java练习\\IO流\\4.txt");
       int num=0;
       while((num=sis.read())!=-1){
           fos.write(num);
       }
       fos.close();
       sis.close();
    }
}
```
### 切割文件
```java
import java.io.*;
import java.util.*;
//文件的切割和合并
public class SplitFileDemo {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
//     splitFile();
       combineFile();
    }
    public static void splitFile()throws IOException{
       FileInputStream fis=new FileInputStream("E:\\java练习\\一千个伤心的理由.mp3");
       FileOutputStream fos=null;
       byte[] buf=new byte[1024*1024];
       int num=0;
       int  count=1;
       while((num=fis.read(buf))!=-1){
           fos=new FileOutputStream("E:\\java练习\\part"+(count++)+".part");
           fos.write(buf, 0, num);
           fos.close();
       }
       fis.close();
    }
    public static void combineFile()throws IOException{
       Vector<FileInputStream> v=new Vector<FileInputStream>();
       v.add(new FileInputStream("E:\\java练习\\part1.part"));
       v.add(new FileInputStream("E:\\java练习\\part2.part"));
       v.add(new FileInputStream("E:\\java练习\\part3.part"));
       v.add(new FileInputStream("E:\\java练习\\part4.part"));
       v.add(new FileInputStream("E:\\java练习\\part5.part"));
       Enumeration<FileInputStream> e=v.elements();
       SequenceInputStream sis=new SequenceInputStream(e);
       FileOutputStream fos=new FileOutputStream("E:\\java练习\\歌曲.mp3");
       int len=0;
       while((len=sis.read())!=-1){
           fos.write(len);
       }
       fos.close();
       sis.close();
    }
}
```
### ObjectStream
```java
import java.io.*;
public class ObjectDemo {
    public static void main(String[] args)throws IOException, ClassNotFoundException {
//     writeObj();
       readObj();
    }
    public static void writeObj()throws IOException{
       ObjectOutputStream oos= new ObjectOutputStream(new FileOutputStream("obj.txt"));
       oos.writeObject(new Person("zhangsan",20));
       oos.close();
    }
    public static void readObj()throws IOException, ClassNotFoundException{
       ObjectInputStream ois=
              new ObjectInputStream(new FileInputStream("obj.txt"));
       Person p=(Person)ois.readObject();
       System.out.println(p);
       ois.close();
    }
}
import java.io.*;
/* 如果不实现这个接口,那么ObjectOutputStream在操作这个类是会报出
NotSerializableException 异常- 某个要序列化的对象不能实现 java.io.Serializable 接口。*/
public class Person implements Serializable{
//给这个可以序列化类化定义一个标识,不管成员修饰符以后变成什么,ObjectStrean操作对象的方法都能"认识"这个类
    static final long serialVersionUID = 42L;
    private String name;
    private int age;
    Person(String name,int age){
       this.name=name;
       this.age=age;
    }
    public String toString(){
       return name+"::"+age;
    }
}
```
### 管道流:是连接多线程与IO的接口
```java
import java.io.*;
//管道流,是连接多线程和IO的接口
public class PipeStream {
    public static void main(String[] args) throws Exception{
       // TODO 自动生成的方法存根
       PipedInputStream pis=new PipedInputStream();
       PipedOutputStream pos=new PipedOutputStream();
       pis.connect(pos);//使此管道输入流连接到管道输出流
       new Thread(new Read(pis)).start();
       new Thread(new Write(pos)).start();
    }
}
class Read implements Runnable{
    PipedInputStream pis;
    Read(PipedInputStream pis){
       this.pis=pis;
    }
    public void run(){
       try{
           System.out.println("管道输入流 ,正准备读取数据");
           byte[] buf=new byte[1024];
           int num=pis.read(buf);
           String s=new String(buf,0,num);
           System.out.println(s);
           pis.close();
       }catch(Exception e){
           System.out.println("管道输入流 ,无法读取数据");
       }
    }
}
class Write implements Runnable{
    PipedOutputStream pos;
    Write(PipedOutputStream pos){
       this.pos=pos;
    }
    public void run(){
       try{
           System.out.println("5秒后, 准备输出数据");
           Thread.sleep(5000);
           pos.write("管道输出流,来啦!哈哈!!".getBytes());
           pos.close();  
       }catch(Exception e){
           System.out.println("管道输出流 ,无法输出数据");
       }  
    }
}
```
### RandomAccessFile
```java
import java.io.*;
/*  RandomAccessFile
 该类不算是IO体系中的子类,而是直接继承自Object,但它是IO包中的成员,因为它具备读和写的功能.
 内部封装了一个数组,而且通过指针对数组的元素进行操作
 可以通过getFilePionter获取指针的位置,同时还可以通过seek改变指针的位置
 其实完成读写的原理就是内部封装了字节输入流和输出流
 通过构造函数可以看出,该类只能造作文件,而且操作文件还有模式 r rw rws rwd
 
 如果模式为只读 r,不会创建文件. 会去读取一个已经存在的文件,如果文件不存在,则会出现异常
 如果模式为读写 rw ,要操作的文件不存在,会自动创建一个新文件,如果存在则不会覆盖 */
public class RandomAccessFileDemo {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
//     writeFile();
//     readFile();
       writeFile_2();
    }
    public static void writeFile()throws IOException{
       RandomAccessFile raf=new RandomAccessFile("run.txt","rw");//模式是读写
       raf.write("李四".getBytes());
       raf.writeInt(65);
//     raf.write(258);//write方法,只写这个数(100000010)的最低八位数
       raf.write("王武".getBytes());
       raf.writeInt(65);//writeInt将一个数的高位的数也写出去
       raf.close();
    }
    public static void writeFile_2()throws IOException{
       RandomAccessFile raf=new RandomAccessFile("run.txt","rw");
       raf.seek(8*3);
       raf.write("周期".getBytes());
       raf.writeInt(65);
       raf.close();  
    }  
    public static void readFile()throws IOException{
       RandomAccessFile raf=new RandomAccessFile("run.txt","r");//模式是只读,就不能写了
//调整对象中的指针
//     raf.seek(8);
//跳过n个字节
//     raf.skipBytes(8);//王武..65
       byte[] buf=new byte[4];
       raf.read(buf);
       String name=new String(buf);
       int age=raf.readInt();
       System.out.println(name+".."+age);//李四..65
           //加上这句话后raf.seek(8);  结果是: 王武..65
       raf.close();
    }
}
```
### DataStream
```java
import java.io.*;
// DataInputStream和DataOutputStream可以用于操作基本数据类型的数据的流对象
public class DataStreamDemo {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
//     writeData();
//     readData();
//     writeUTF();
       readUTF();
    }
    public static void writeData()throws IOException{
       DataOutputStream dos=new DataOutputStream(new FileOutputStream("data.txt"));
       dos.writeInt(123);
       dos.writeBoolean(true);
       dos.writeDouble(123.123);
       dos.close();
    }
    public static void readData()throws IOException{
       DataInputStream dos=new DataInputStream(new FileInputStream("data.txt"));
       int x=dos.readInt();
       boolean b=dos.readBoolean();
       double d=dos.readDouble();
       System.out.println(x);
       System.out.println(b);
       System.out.println(d);
       dos.close();
    }
    public static void writeUTF()throws IOException{
       DataOutputStream dos=new DataOutputStream(new FileOutputStream("utf.txt"));
       dos.writeUTF("你好啊");//如果使用writeUTF方法写的只能用readUTF方法读取出来
       dos.close();
    }
    public static void readUTF()throws IOException{
       DataInputStream dis=new DataInputStream(new FileInputStream("utf.txt"));
       String s=dis.readUTF();
       System.out.println(s);
       dis.close();
    }
}
```
### ByteArrayStream
```java
import java.io.*;
/*  用于操作字节数组的流对象
 ByteArrayInputStream:在构造的时候需要接受数据源,而且数据源是一个字节数组
 ByteArrayOutputStream:在构造的时候不用定义数据目的,应为该对象中已经内部封装了可变长度的数组,这就是数据目的地
 因为这两个流对象都操作数组,并没有使用系统资源,所以不用进行close关闭
 在流操作数据讲解时:
 源设备: 键盘 System.in  硬盘 FileStream  内存 ArrayStream
 目的设备: 控制台 System.out 硬盘  FileStream  内存 ArrayStream
 用流的读写思想来操作数据   */
public class ByteArrayStream {
    public static void main(String[] args)throws IOException {
       // TODO 自动生成的方法存根
//     数据源:
       ByteArrayInputStream bai=new ByteArrayInputStream("ABCDEF".getBytes());
//     数据目的
       ByteArrayOutputStream bao=new ByteArrayOutputStream();
       int by=0;
       while((by=bai.read())!=-1){
           bao.write(by);
       }
       System.out.println(bao.size());//6
       System.out.println(bao.toString());//ABCDEF
       bao.writeTo(new FileOutputStream("a.txt"));//只有这一个方法抛出IO异常
    }
}
```
### 编码
```java
import java.io.*;
public class EncodeStream {
    public static void main(String[] args) throws IOException{
       // TODO 自动生成的方法存根
//     writeText();
       readText();
    }
    public static void writeText()throws IOException{
       OutputStreamWriter out=new OutputStreamWriter(new FileOutputStream("gbk.txt"));
       out.write("你好");//你好占4个字节
       out.close();
//     OutputStreamWriter out1=new OutputStreamWriter(new FileOutputStream("utf-8.txt"),"utf-8");
//     out1.write("你好");//你好占6个字节
//     out1.close();
    }
    public static void readText()throws IOException{
//     InputStreamReader in=new InputStreamReader(new FileInputStream("gbk.txt"),"gbk");
//     char[] buf=new char[10];
//     int num=in.read(buf);
//     System.out.println(new String(buf,0,num));
//     in.close();                                   //     utf-8  三个字节 gbk两个字节
       InputStreamReader in1=new InputStreamReader(new FileInputStream("utf-8.txt"),"gbk");//浣犲ソ
       int num1=0;
       char[] buf1=new char[4];
       while((num1=in1.read(buf1))!=-1){
           System.out.println(new String(buf1,0,num1));
       }
       in1.close();  
    }
}
 
import java.io.*;
import java.util.Arrays;
/*  编码: 字符串变成字节数组
         String--->byte[] :: str.getBytes(String charsetName);
    解码: 字节数组变成字符串
         byte[]--->String :: new String(byte[],charsetName);  */
public class EncodeDemo {
    public static void main(String[] args) throws UnsupportedEncodingException {
       // TODO 自动生成的方法存根
//GBK编码
//     String s="你好";
//     byte[] b=s.getBytes("gbk");
//     sop(Arrays.toString(b));//[-60, -29, -70, -61]
//     String s1=new String(b,"gbk");
//     sop(s1);//你好
//     String s2=new String(b,"utf-8");
//     sop(s2);//???
//UTF-8编码
//     String s="你好";
//     byte[] b=s.getBytes("utf-8");
//     sop(Arrays.toString(b));//[-28, -67, -96, -27, -91, -67]
//     String s1=new String(b,"gbk");
//     sop(s1);//浣犲ソ
//     String s2=new String(b,"utf-8");
//     sop(s2);//你好
//ISO8859-1编码
//     String s="你好";
//     byte[] b=s.getBytes("GBK");//先用GBK给"你好"编码
//     sop(Arrays.toString(b));//[-60, -29, -70, -61]
//     String s1=new String(b,"iso8859-1");//在用ISO8859-1解码,结果是乱码
//     sop(s1);//????
//     byte[] b2=s1.getBytes("iso8859-1");//再用ISO8859-1编码,将原来GBK编码的数在返回去
//     String s2=new String(b2,"GBK");//再用GBK解码,就过是 "你好"
//     sop(s2);//你好 
//联通:
       String lian="联通";
       byte[] by=lian.getBytes("GBK");
       for(byte b:by){
           System.out.println(Integer.toBinaryString(b&255));
//         11000001      这个编码的格式属于utf-8的编码格式   110****  10****** 110****  10******
//         10101010
//         11001101
//         10101000
       }
    }
    public static void sop(Object obj){
       System.out.println(obj);
    }
}
```
### 综合练习
```java
import java.io.*;
import java.util.*;
/*  有五个学生,每个学生有三门课程的 成绩,从键盘数据以上格式的数据(包括姓名 ,三门成绩),输入的格式是: 如,zhangsan,30,40,50,计算出总成绩,并把学生的信息和计算出来的总分高低存放在硬盘文件"study.txt"中
 1,描述学生对象
 2,定义一个可以操作学生对象的工具类
 思想:
    1,通过键盘录入一行数据,并将该行中的信息取出来封装成学生对象
    2,因为学生有很多,那么就需要存储,使用到集合中.因为要对学生的总分进行排序,所以使用TreeSet
    3,将集合中的信息写入到一个文件中 */
public class TestDemo {
    public static void main(String[] args) throws IOException {
       // TODO 自动生成的方法存根
//强行反转比较器,学生按照总分高低进行排序
       Comparator<Student> cmp=Collections.reverseOrder();
       Set<Student> set=StudentInfoTool.getStudents(cmp);
       StudentInfoTool.writeToStud(set);
    }
}
class Student implements Comparable<Student>{
    private String name;
    private int ch,en,ma;
    private int sum;
    Student(String name,int ch,int en,int ma){
       this.name=name;
       this.ch=ch;
       this.en=en;
       this.ma=ma;
       this.sum=ch+en+ma;
    }
    public String getName(){
       return name;
    }
    public int getSum(){
       return sum;
    }
    public int hashCode(){
       return name.hashCode()+sum*17;
    }
    public boolean equals(Object obj){
       if(!(obj instanceof Student))
           throw new ClassCastException("类型不匹配");
       Student s=(Student)obj;
       return this.name.equals(s.name)&&this.sum==s.sum;
    }
    public int compareTo(Student s){
       int num=new Integer(this.sum).compareTo(new Integer(s.sum));
       if(num==0)
           return this.name.compareTo(s.name);
       return num;
    }
    public String toString(){
       return "student["+ this.name+","+"ch:"+ch+",en:"+en+",ma:"+ma+"]";
    }
}
class StudentInfoTool  {
    public static Set<Student> getStudents() throws IOException{
       return getStudents(null);
    }
//  给集合传一个比较器进去,让其按照指定的方式排序
    public static Set<Student> getStudents(Comparator<Student> cmp) throws IOException{
       Set<Student> set=null;
       if(cmp==null)
           set=new TreeSet<Student>();
       else
           set=new TreeSet<Student>(cmp);
       BufferedReader bufr=new BufferedReader(new InputStreamReader(System.in));
       String s=null;
       while((s=bufr.readLine())!=null){
           if("over".equals(s))
              break;
           String[] arr=s.split(",");
           String name=arr[0];
           int ch=Integer.parseInt(arr[1]);
           int en=Integer.parseInt(arr[2]);
           int ma=Integer.parseInt(arr[3]);
           set.add(new Student(name,ch,en,ma));
       }
       bufr.close();
       return set;
    }
    public static void writeToStud(Set<Student> s) throws IOException{
       BufferedWriter bufw=new BufferedWriter(new OutputStreamWriter(new FileOutputStream("Study.txt")));
       Iterator<Student> it=s.iterator();
       while(it.hasNext()){
           Student stu=it.next();
           String info=stu.toString();
           bufw.write(info);
           bufw.write(stu.getSum()+"");
           bufw.newLine();
           bufw.flush();
       }
       bufw.close();
    }  
}
```
## 第十二章:GUI
```java
import java.awt.*;
import java.awt.event.*;
/* 创建图形化界面:
    1,创建Frame窗体
    2,对窗体进行基本的设置,   大小,位置,布局
    3,定义组建
    4.将组建同通过窗体的add方法添加到窗体中
    5,让窗体显示,通过setVisible(true);方法
 事件监听机制的特点:
    1,事件源: 就是awt包或者swing包中的那些图形界面组建
    2,事件: 每一个事件源都有自己特有的对应事件和共性事件
    3,监听器: 将可以触发某一事件的动作(不只一个)都已经封装到了监听器中
    4,事件处理:
    以上前三者,在java中都已经定义好了,直接获取其对象来用就可以了
    我们要做的事情就是对产生的动作进行处理 */
public class GUI_Demo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       Frame f=new Frame("Frame");
       f.setVisible(true);
       f.setSize(500, 400);//500横坐标,400纵坐标
       f.setLocation(400, 300);
      
       Button b=new Button("按钮,哈哈!");
       f.add(b);
       f.setLayout(new FlowLayout());
       f.addWindowListener(new WindowAdapter(){
           public void windowClosing(WindowEvent e){
//            System.out.println("window closing");
              System.exit(0);
           }
           public void windowActivated(WindowEvent e){
              System.out.println("windowActivated");//激活窗口时调用。
           }
           public void windowDeactivated(WindowEvent e){
              System.out.println("windowDeactivated");//停用窗口时调用
           }
       });
    }
}
```
### Frame
```java
import java.awt.*;
import java.awt.event.*;
public class FrameDemo {
    private Frame f;
    private Button but;
    FrameDemo(){
   
    }
    public void init(){
       f=new Frame("我的窗体");
       f.setBounds(300,200,500,400);
       f.setLayout(new FlowLayout());
       f.setVisible(true);
       but=new Button("我的按钮");
       f.add(but);
       myEvent();
    }
    public void myEvent(){
       f.addWindowListener(new WindowAdapter(){
           public void windowClosing(WindowEvent e){
              System.exit(0);
           }
       });
/* 让按钮具备退出程序的功能:那么按钮就是事件源,那么选择那么监听器呢?  通过关闭窗体事例了解到,
 想要知道那个组建具备什么样的特有监听器 ,需要查看该组件的功能,  通过查看Button的API描述发现按钮支持
 一个特有的监听器addActionListener  */
       but.addActionListener(new ActionListener(){
           public void actionPerformed(ActionEvent e){
              System.out.println("程序退出,按钮干的");
              System.exit(0);
           }
       });
    }
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       FrameDemo fd=new FrameDemo();
       fd.init();
    }
}
```
### MouseAndKeyEvent
```java
import java.awt.*;
import java.awt.event.*;
public class MouseAndKeyEvent {
    private Frame f;
    private Button but;
    private TextField tf;
    MouseAndKeyEvent(){
       init();
    }
    public void init(){
       f=new Frame("我的窗体");
       f.setBounds(300,200,500,400);
       f.setLayout(new FlowLayout());
       f.setVisible(true);
       but=new Button("我的按钮");
       tf=new TextField(20);
       f.add(tf);
       f.add(but);
       myEvent();
    }
    public void myEvent(){
       f.addWindowListener(new WindowAdapter(){
           public void windowClosing(WindowEvent e){
              System.exit(0);
           }
       });
    /*  but.addMouseListener(new MouseAdapter(){
           public void mouseClicked(MouseEvent e){
              System.out.println("鼠标单击了"+e.getClickCount()+"次");
           }
           public void mouseEntered(MouseEvent e){
              System.out.println("鼠标到此");
           }
       }); */
       but.addKeyListener(new KeyAdapter(){
           public void keyPressed(KeyEvent e){
//            System.out.println(e.getKeyChar()+"==="+e.getKeyCode());
//            if(e.getKeyCode()==KeyEvent.VK_ESCAPE){
//                System.exit(0);
              if(e.isControlDown()&&e.getKeyCode()==KeyEvent.VK_ENTER){
                  System.out.println(" control+enter  is  run");
              }
           }
       });
       tf.addKeyListener(new KeyAdapter(){
           public void keyPressed(KeyEvent e){
              int code=e.getKeyCode();
              if(!(code>=KeyEvent.VK_0&&code<=KeyEvent.VK_9)){
                  System.out.println((char)code+"是非法的");
                  e.consume();//取消该事件的原来该执行的事件,
//                   如:键盘按下和录入字符是该事件,则使用该方法后,
//                       将不会录入该字符,相当于屏蔽按键
              }
           }
       });
    }
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new MouseAndKeyEvent();
    }
}
```
### Window
```java
import java.awt.*;
import java.awt.event.*;
import java.io.File;
public class MyWindowDemo {
    private Frame f;
    private Button but;
    private TextField tf;
    private TextArea ta;
//窗口的初始化
    private Label label;
    private Button button;
    private Dialog d;
    MyWindowDemo(){
      
    }
    public void init(){
       f=new Frame("我的窗体");
       f.setBounds(300, 200, 600, 500);
       f.setLayout(new FlowLayout());
      
       tf=new TextField(60);
       f.add(tf);
       but=new Button("转到");
       f.add(but);
       ta=new TextArea(25,40);
       f.add(ta);
//添加一个错误提示窗口
       d=new Dialog(f,"错误提示!",true);
       d.setBounds(400,500,240, 200);
       d.setLayout(new FlowLayout());
       label=new Label();
       button=new Button("确定");
       d.add(label);
       d.add(button);
      
        f.setVisible(true);
       myEvent();
    }
    public void myEvent(){
       f.addWindowListener(new WindowAdapter(){
           public void windowClosing(WindowEvent e){
              System.exit(0);
           }
       });
       but.addActionListener(new ActionListener(){
           public void actionPerformed(ActionEvent e){
              show();
           }
       });
//  窗体事件
       button.addActionListener(new ActionListener(){
           public void actionPerformed(ActionEvent e){
              d.setVisible(false);
           }
       });
       d.addWindowListener(new WindowAdapter(){
           public void windowClosing(WindowEvent e){
              d.setVisible(false);
           }
       });
//  文本框的键盘事件
       tf.addKeyListener(new KeyAdapter(){
           public void keyPressed(KeyEvent e){
              if(e.getKeyCode()==KeyEvent.VK_ENTER){
                  show();
              }
           }
       });
    }
    private void show(){
       ta.setText("");
       String dirPath=tf.getText();
       File dir=new File(dirPath);
       if(dir.exists()&&dir.isDirectory()){
           String[] names=dir.list();
           for(String name:names){
              ta.append(name+"\r\n");
           }
       }else{
           label.setText("你输入的信息"+dirPath+"是错误的");
           d.setVisible(true);
       }
       tf.setText("");
    }
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new MyWindowDemo().init();
    }
}
```
### Menu
Frame类的setMenuBar方法可以向窗体中添加  菜单栏MenuBar
菜单栏  可以添加 :菜单Menu
菜单  中可以添加 :菜单(子菜单)  和  菜单项 MenuItem
```java
import java.awt.*;
import java.awt.event.*;
import java.io.*;
public class MyMenuDemo {
    private Frame f;
    private MenuBar menubar;
    private Menu filemenu,menu2,submenu,subsubmenu;
    private MenuItem close,start,save,open,menuItem;
    private FileDialog openfile ,savefile;
    private TextArea ta;
    private File file;
    MyMenuDemo(){
      
    }
    public void init(){
       f=new Frame("我的窗体");
       f.setBounds(300, 200, 600, 500);
//     f.setLayout(new FlowLayout());//如果不设置这个,默认就是边界布局
//  菜单栏
       menubar=new MenuBar();
//  菜单
       filemenu=new Menu("文件");
       menu2=new Menu("编辑");
       submenu=new Menu("子菜单");
       subsubmenu=new Menu("子子菜单");
//  菜单项 
       start=new MenuItem("开始");
       close=new MenuItem("退出");
       open=new MenuItem("打开");
       save=new MenuItem("保存");
       menuItem=new MenuItem("子菜单项");
//  菜单栏里面添加菜单
       menubar.add(filemenu);
       menubar.add(menu2);
       menubar.add(submenu);
//  菜单里面添加菜单项  
       filemenu.add(start);
       filemenu.add(open);
       filemenu.add(save);
       filemenu.add(close);
//  菜单里面添加子菜单  
       filemenu.add(submenu);
       submenu.add(menuItem);//子菜单里面添加菜单项
       submenu.add(subsubmenu);
      
       f.setMenuBar(menubar);
//  打开和保存文件所出现的对话框
       openfile=new FileDialog(f,"我要打开",FileDialog.LOAD);
       savefile=new FileDialog(f,"我要保存",FileDialog.SAVE);
      
       ta=new TextArea();
       ta.setSize(400,300);
       f.add(ta);
      
       f.setVisible(true);
       myEvent();
    }
    public void myEvent(){
       f.addWindowListener(new WindowAdapter(){
           public void windowClosing(WindowEvent e){
              System.exit(0);
           }
       });
       close.addActionListener(new ActionListener(){
           public void actionPerformed(ActionEvent e){
              System.exit(0);
           }
       });
       start.addActionListener(new ActionListener(){
           public void actionPerformed(ActionEvent e){
             
           }
       });
       open.addActionListener(new ActionListener(){
           public void actionPerformed(ActionEvent e){
              openfile.setVisible(true);
              String dir=openfile.getDirectory();
              String filename=openfile.getFile();
              if(dir==null&&filename==null)
                  return;
              ta.setText("");
              file=new File(dir,filename);
              BufferedReader bufr=null;
              try {
                  bufr=new BufferedReader(new FileReader(file));
                  String line=null;
                  while((line=bufr.readLine())!=null){
                     ta.append(line+"\r\n");
                    
                  }
                 
              } catch (IOException e1) {
                  // TODO 自动生成的 catch 块
                  e1.printStackTrace();
                 
              }finally{
                  try{
                     if(bufr!=null)
                         bufr.close();
                  }catch(IOException e1){
                     throw new RuntimeException("关闭失败");
                  }
              }
             
           }
       });
       save.addActionListener(new ActionListener(){
           public void actionPerformed(ActionEvent e){
              savefile.setVisible(true);
              if(file==null){
                  String dir=savefile.getDirectory();
                  String filename=savefile.getFile();
                  if(dir==null&&filename==null)
                     return;
                  file=new File(dir,filename);
              }
              try {
                  BufferedWriter bufw=new BufferedWriter(new FileWriter(file));
                  String text=ta.getText();
                  bufw.write(text);
                  bufw.close();
                 
                 
              } catch (IOException e1) {
                  // TODO 自动生成的 catch 块
                  throw new RuntimeException("写入失败");
              }
           }
       });
    }
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new MyMenuDemo().init();
    }
}
```
## 第十三章:网络编程
前提:
```java
import java.net.*;
/* 概述:网络编程的前提
    1,找到对方的IP
    2,数据要发送到对方指定的应用程序上.为了标识这些应用程序,所以给这些网络引用程序都用数字进行标识,
       为了方便称呼这个数字,叫做端口.或者逻辑端口
    3,定义通讯规则.这个通讯规则称之为  协议.  国际标准化组织定义了通用协议  TCP/IP
 IP:127.0.0.1  主机名  localhost
 OSI 网路传输参考模型: 数据封包
    应用层-->表示层-->回话层--> 传输层-->网络层(加IP)-->数据链路层-->物理层
 TCP/IP网络传输参考模型: 数据拆包
    应用层-->传输层-->网际层-->主机至网络层
 UDP:(视频会议,广播等)
    1,将数据及源和目的封装成数据包中,不需要建立连接
    2,每个数据的大小控制在64k之内
    3,因为无连接,是不可靠协议
    4,不需要建立连接
 TCP:(打电话等)
    1,建立连接,形成传输数据的通道
    2,在连接中进行大数据传输
    3,通过三次握手完成连接,是可靠协议
    4,必须建立连接,效率会稍低
 Socket:
    1,Socket就是为网络服务提供的一种机制
    2,通讯的两端都有Socket
    3,网络通信其实就是Socket间的通信
    4,数据在两个Socket之间通过IO传输 */
public class IPDemo {
    public static void main(String[] args) throws UnknownHostException {
       // TODO 自动生成的方法存根
       InetAddress i=InetAddress.getLocalHost();
//     System.out.println(i);//DELL-XPS13/127.0.0.1
//     System.out.println(i.getHostName()+'\n'+i.getHostAddress());
                         //DELL-XPS13         127.0.0.1
       InetAddress ia=InetAddress.getByName("127.0.0.1");//还可以输入名称
       System.out.println(ia.getHostName());//   DELL-XPS13
       System.out.println(ia.getHostAddress());//   127.0.0.1
    }
}
```
### UDP
```java
import java.net.*;
/* 需求:定义一个程序,用于接受UDP协议传输的数据并处理
 思路:
    1,定义一个UDPSocket服务. 通常会监听一个端口,其实就是给这个接受网络应用程序定义一个数字标识
       方便与明确那些数据过来该应用程序可以处理
    2,定一个数据包,因为要存储接收到的字节数据,因为数据包对象中有很多功能可以提取字节数据中的不同信息
    3,通过socket服务的receive方法将接收到的数据存入已经定义好的数据包中
    4,通过数据包对象的特有功能,将折这些不同的数据取出,打印在控制台上
    5,关闭资源  */
public class UDPReceiveDemo {
    public static void main(String[] args) throws Exception {
       // TODO 自动生成的方法存根
       DatagramSocket ds=new DatagramSocket(10005);
       while(true){
           byte[] buf=new byte[1024];
           DatagramPacket dp=new DatagramPacket(buf,buf.length);
           ds.receive(dp);
           String address=dp.getAddress().getHostAddress();
           String data=new String(dp.getData(),0,dp.getLength());
           int port=dp.getPort();
           System.out.println(address+"::"+port+"::"+data);
       }
//     ds.close();
    }
}
import java.net.*;
import java.io.*;
public class UDPDemo2 {
    public static void main(String[] args) throws Exception {
       // TODO 自动生成的方法存根
       DatagramSocket ds=new DatagramSocket();
       BufferedReader bufr=new BufferedReader(new InputStreamReader(System.in));
       String line=null;
       while((line=bufr.readLine())!=null){
           if("886".equals(line))
              break;
           byte[] buf=line.getBytes();
           DatagramPacket dp=new DatagramPacket(buf,buf.length,10005);
           ds.send(dp);
       }
       ds.close();
    }
    //使用UDPReceiveDemo这个类作为接受端,改端口为10005,
}
import java.net.*;
/*需求:通过UDP传输方式,将一段数据发送出去
 思路:  1,先建立UDP Socket端点
       2,提供数据,并将数据封装到数据包中
       3,通过socket服务的发送功能,将数据包发送出去
       4,关闭资源  */
public class UDPSendDemo {
    public static void main(String[] args) throws Exception{
       // TODO 自动生成的方法存根
       DatagramSocket ds=new DatagramSocket();
       byte[] data="UDP 哥们来了".getBytes();
       DatagramPacket dp=
              new DatagramPacket(data,data.length,InetAddress.getByName("127.0.0.255"),10002);
       for(int x=0;x<20;x++){
           Thread.sleep(300);
           ds.send(dp);
       }
       ds.close();
    }
}
import java.net.*;
import java.io.*;
public class ChatDemo {
    public static void main(String[] args) throws Exception {
       // TODO 自动生成的方法存根
       DatagramSocket ds=new DatagramSocket();
       DatagramSocket ds1=new DatagramSocket(8888);
       new Thread(new Send(ds)).start();
       new Thread(new Rece(ds1)).start();
    }
}
class Send implements Runnable{
    private DatagramSocket ds;
    Send(DatagramSocket ds){
       this.ds=ds;
    }
    public void run(){
       try{
           BufferedReader bufr=new BufferedReader(new InputStreamReader(System.in));
           String line=null;
           while((line=bufr.readLine())!=null){
              if("over".equals(line))
                  break;
              byte[] buf=line.getBytes();
              DatagramPacket dp=new DatagramPacket(buf,buf.length,InetAddress.getByName("127.0.0.255"),8888);
              ds.send(dp);
           }
           ds.close();
       }catch(Exception e){
           System.out.println("发送数据失败");
       }
    }
}
class Rece implements Runnable{
    private DatagramSocket ds;
    Rece(DatagramSocket ds){
       this.ds=ds;
    }
    public void run(){
       try{
           while(true){
              byte[] buf=new byte[1024];
              DatagramPacket dp=new DatagramPacket(buf,buf.length);
              ds.receive(dp);
              String id=dp.getAddress().getHostAddress();
              String data=new String(dp.getData(),0,dp.getLength());
              System.out.println(id+"::"+data);
           }
       }catch(Exception e){
           System.out.println("接收数据失败");
       }
    }
}
```
### TCP
```java
import java.net.*;
import java.io.*;
/* TCP传输: tcp分为客户端Socket和服务端ServerSocket
客户端:通过查阅socket对象,发现该对象在建立时,就可以去连接指定的主机,因为tcp是面向连接的,所以在建立socket服务时,就要有服务端存在,并连接成功. 形成通路后,在该通道进行数据的传输
需求:给服务端发送一个文本数据
步骤:1,创建Socket服务,并制定要连接的主机端口
 
需求:定义一个端点接收数据,并将数据打印在控制台上
服务端:
    1,建立服务端的socket服务,ServerSocket;并监听一个端口
    2,获取连接过来了客户端对象,通过ServerSocket的accept方法,没有连接就会等待,所以这个方法是阻塞式的
    3,客户端如果发过来数据,那么服务端要使用对应的客户端对象,并获取到该客户端对象的读取流来读取
       发过来的数据并将其打印在控制台上
    4,关闭客户端(可选) */
class ClientDemo implements Runnable{
    public void run(){
       try{
           client();
       }catch(Exception e){
           System.out.println("客户端");
       }
    }
    public  void client()  throws Exception{
//  创建客户端的socket服务,指定目的主机和端口
       Socket s=new Socket("127.0.0.1",10101);
//  为了发送数据,应该获取socket流中的输出流
       OutputStream out=s.getOutputStream();
       out.write("tcp  client ge men lai le ".getBytes());
       s.close();
    }
}
class ServerDemo implements Runnable{
    public void run(){
       try{
           server();
       }catch(Exception e){
           System.out.println("服务端");
       }
      
    }
    public void server()  throws Exception{
//  建立服务端Socket服务,并监听一个端口
       ServerSocket ss=new ServerSocket(10101);
//  通过accept方法获取连接过来的客户端
       Socket s=ss.accept();
       String ip=s.getInetAddress().getHostAddress();
       System.out.println(ip+"....connect");
//     获取客户端发送过来的数据,那么要使用客户端对象的读取流来读取数据
       InputStream in=s.getInputStream();
       byte[] buf=new byte[1024];
       int len=in.read(buf);
        System.out.println(new String(buf,0,buf.length));
       s.close();
       ss.close();
    }
}
public class TCP_Demo {
    public static void main(String[] args) throws Exception {
       // TODO 自动生成的方法存根
       new Thread(new ServerDemo()).start();
       new Thread(new ClientDemo()).start();
    }
}
import java.net.*;
import java.io.*;
/* 演示tcp的传输的客户端和服务端的互访
 需求:客户端给服务端发送数据,服务端收到后,给客户端反馈信息
 客户端:
    1,建立socket服务,指定要连接的主机和端口
    2,获取socket流中的输出流,将数据写到该流中.通过网络发送给服务端
    3,获取socket流中的输入流,将服务端反馈的数据获取到,并打印
    4,关闭客户端资源 */
class ClientDemo2 implements Runnable{
    public void run(){
       try{
           client();
       }catch(Exception e){
           System.out.println("客户端");
       }
    }
    public  void client()  throws Exception{
       Socket s=new Socket("127.0.0.1",10111);
       OutputStream out=s.getOutputStream();
       out.write("服务端你好".getBytes());
       InputStream in=s.getInputStream();
       byte[] buf=new byte[1024];
       int len=in.read(buf);
       System.out.println(new String(buf,0,buf.length));
       s.close();
    }
}
class ServerDemo2 implements Runnable{
    public void run(){
       try{
           server();
       }catch(Exception e){
           System.out.println("服务端");
       }
    }
    public void server()  throws Exception{
       ServerSocket ss=new ServerSocket(10111);
       Socket s=ss.accept();
      
       String ip=s.getInetAddress().getHostAddress();
       System.out.println(ip+"....connect");
      
       InputStream in=s.getInputStream();
       byte[] buf=new byte[1024];
       int len=in.read(buf);
       System.out.println(new String(buf,0,buf.length));
      
       OutputStream out=s.getOutputStream();
       out.write("客户端你好".getBytes());
      
       s.close();
       ss.close();
    }
}
public class TCP_Demo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new Thread(new ServerDemo2()).start();
       new Thread(new ClientDemo2()).start();
    }
}
import java.io.*;
import java.net.*;
/* 需求:建立一个文本转换服务器
 客户端给服务端发送文本,服务端将文本转成大写再返回给客户端,而且客户端可以不断的进行转换. 当客户端输入over时,转换结束
分析: 客户端:
    既然操作设备上的数据,那么就可以使用io技术,并按照io的操作规律来思考
       源:键盘录入
       目的:网络设备,网络输出流
       而且操作的是文本数据,可以选择字符流
    步骤:1,建立服务
       2,获取键盘录入
       3,将数据发给服务端
       4,后将服务端返回的大写数据
       5,结束,关闭资源
 都是文本数据,可以使用字符流进行操作,同时提高效率,加入缓冲区
 服务端:
    源:socket读取流
    目的:socket输出流
 该例子出现的问题
    现象:客户端和服务端都莫名的等待,  为什么呢?
    因为客户端和服务端都有阻塞式的方法,这些方法没有读到结束标记就会一直等待
    从而导致两端都在等待*/
class ClientDemo3 implements Runnable{
    public void run(){
       client();
    }
    public void client(){
       try{
           Socket s=new Socket("127.0.0.1",11111);
           BufferedReader bufr=new BufferedReader(new InputStreamReader(System.in));
           BufferedWriter bufOut=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
//可以将BufferedWriter这个话改成 打印流语句  PrintStream  该方法可以接收字节流和字符流而且还自带刷型功能
//  就是println方法
           BufferedReader bufIn=new BufferedReader(new InputStreamReader(s.getInputStream()));
           String line=null;
           while((line=bufr.readLine())!=null){
              if("over".equals(line))
                  break;
              bufOut.write(line);
              bufOut.newLine();
              bufOut.flush();
              String str=bufIn.readLine();
              System.out.println(str);
           }
           bufr.close();
           s.close();
       }catch(Exception e){
           System.out.println("客户端失败");
       }
    }
}
class ServerDemo3 implements Runnable{
    public void run(){
       server();
    }
    public void server(){
       try{
           ServerSocket ss=new ServerSocket(11111);
           Socket s=ss.accept();
           String ip=s.getInetAddress().getHostAddress();
           System.out.println(ip+"...connect");
//     读取客户端中的数据
           BufferedWriter bufOut=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
//     将信息在反馈给客户端          
           BufferedReader bufIn=new BufferedReader(new InputStreamReader(s.getInputStream()));
           String str=null;
           while((str=bufIn.readLine())!=null){
              System.out.println(str);
              bufOut.write(str.toUpperCase());
              bufOut.newLine();
              bufOut.flush();
           }
           s.close();
           ss.close();
       }catch(Exception e){
           System.out.println("服务端失败");
       }
    }
}
public class TCP_Test {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new Thread(new ClientDemo3()).start();
       new Thread(new ServerDemo3()).start();
    }
}
import java.io.*;
import java.net.*;
class TextClient implements Runnable{
    public void run(){
       client();
    }
    public void client(){
       try{
           Socket s=new Socket("127.0.0.1",11010);
           BufferedReader bufr=new BufferedReader(new FileReader("E:\\java练习\\13-网络编程\\src\\ChatDemo.java"));
           BufferedWriter bufOut=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
           String line=null;
           while((line=bufr.readLine())!=null){
              bufOut.write(line);
              bufOut.newLine();
              bufOut.flush();
           }
//服务端缺少标记,但是这个样写容易重复,可以添加时间戳,客户端可以先发送一个时间过来,服务端先读取一行作为标记
//         bufOut.write("over哈哈");//要在这句话后面加上结束标记,表示一行已经到头了,如果不加,服务端将认为这个句话没有到末尾,继续阻塞
//         bufOut.newLine();
//         bufOut.flush();
//     socket中已经定义号的结束标记,,服务端就用在判断自定义的标记  
           s.shutdownOutput();
           BufferedReader bufIn=new BufferedReader(new InputStreamReader(s.getInputStream()));
           String str=bufIn.readLine();
           System.out.println(str);
           bufr.close();
           s.close();
       }catch(Exception e){
           System.out.println("客户端失败");
       }
    }
}
class TextServer implements Runnable{
    public void run(){
       server();
    }
    public void server(){
       try{
           ServerSocket ss=new ServerSocket(11010);
           Socket s=ss.accept();
           String ip=s.getInetAddress().getHostAddress();
           System.out.println(ip+"...connect");
//     读取客户端中的数据
           BufferedReader bufIn=new BufferedReader(new InputStreamReader(s.getInputStream()));
           BufferedWriter bufw=new BufferedWriter(new OutputStreamWriter(new FileOutputStream("net.txt")));
           String str=null;
           while((str=bufIn.readLine())!=null){
//            if("over哈哈".equals(str))
//                break;
              bufw.write(str);
              bufw.newLine();
              bufw.flush();
           }
//         bufw.close();
//     将信息在反馈给客户端
           BufferedWriter bufOut=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
           bufOut.write("服务端收到");
           bufOut.newLine();
           bufOut.close();
           s.close();
           ss.close();
       }catch(Exception e){
           System.out.println("服务端失败");
       }
    }
}
public class Text {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new Thread(new TextClient()).start();
       new Thread(new TextServer()).start();
    }
}
import java.io.*;
import java.net.*;
//创建一个服务端,可以让多个客户端上传图片
class ServerD implements Runnable{
    private Socket s;
    ServerD(Socket s){
       this.s=s;
    }
    public void run(){
       String ip=s.getInetAddress().getHostAddress();
       System.out.println(ip+"...connect");
       try{
//     定义一个计数器
           int count=1;
           File f=new File(ip+"("+count+")"+".jpg");
           while(f.exists())
              f=new File(ip+"("+(count++)+")"+".jpg");
           InputStream bufIn=s.getInputStream();
           FileOutputStream out=new FileOutputStream(f);
           byte[] buf=new byte[1024];
           int line=0;
           while((line=bufIn.read(buf))!=-1){
              out.write(buf,0,line);
           }
           BufferedWriter bufOut=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
           String str="上传成功";
           bufOut.write(str);
           bufOut.flush();
           bufOut.close();
           out.close();
           s.close();
       }catch(Exception e){
           System.out.println("上传失败");
       }
    }
}
public class ServerSocketDemo {
    public static void main(String[] args) throws Exception {
       // TODO 自动生成的方法存根
       ServerSocket ss=new ServerSocket(20202);
       while(true){
           Socket s=ss.accept();
           new Thread(new ServerD(s)).start();;
       }
    }
}
import java.io.*;
import java.net.*;
//上传图片到服务端
class ClientPic implements Runnable{
    public void run(){
       client();
    }
    public void client(){
       try{
           Socket s=new Socket("127.0.0.1",20202);
           OutputStream bufOut=s.getOutputStream();
           FileInputStream in=new FileInputStream("E:\\java练习\\13-网络编程\\图片.jpg");
           byte[] buf=new byte[1024];
           int len=0;
           while((len=in.read(buf))!=-1){
              bufOut.write(buf,0,len);
           }
           s.shutdownOutput();
           BufferedReader bufIn=new BufferedReader(new InputStreamReader(s.getInputStream()));
           String line=bufIn.readLine();
           System.out.println(line);
           s.close();
           in.close();
       }catch(Exception e){
           System.out.println("客户端上传失败");
       }
    }
}
/*如果想要多个客户端能访问服务端,那么怎么办呢?
 服务端最好的办法就是将客户端封装到一个单独的线程中,这样就可以同时处理多个客户端请求*/
class ServerPic implements Runnable{ 
    public void run(){
       server();
    }
    public void server(){
       try{
           ServerSocket ss=new ServerSocket(12345);
           Socket s=ss.accept();
           String ip=s.getInetAddress().getHostAddress();
           System.out.println(ip+"...connect");
          
           InputStream bufIn=s.getInputStream();
           FileOutputStream out=new FileOutputStream("1.jpg");
           byte[] buf=new byte[1024];
           int line=0;
           while((line=bufIn.read(buf))!=-1){
              out.write(buf,0,line);
           }
           BufferedWriter bufOut=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
           String str="上传成功";
           bufOut.write(str);
           bufOut.flush();
           bufOut.close();
           out.close();
           s.close();
           ss.close();
       }catch(Exception e){
           System.out.println("服务端失败");
       }
    }
}
public class UploadPicture {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
//     new Thread(new ServerPic()).start();
       new Thread(new ClientPic()).start();
    }
}
import java.io.*;
import java.net.*;
/* 客户通过键盘录入用户名,服务端对这个用户进行校验
 如果该用户存在,服务端显示某某已登陆,并在客户端显示某某,欢迎光临
 如果用户不存在,在服务端显示某某尝试登录,并在客户端显示某某用户不存在
 最多登陆三次*/
class ClientDuan implements Runnable{
    public void run(){
       try{
           Socket s=new Socket("127.0.0.1",10115);
           BufferedReader bufr=new BufferedReader(new InputStreamReader(System.in));
           PrintWriter bufOut=new PrintWriter(s.getOutputStream(),true);
           BufferedReader bufIn=new BufferedReader(new InputStreamReader(s.getInputStream()));
           for(int x=0;x<3;x++){
              String line=bufr.readLine();
              if(line==null)
                  break;
              bufOut.println(line);
              String info=bufIn.readLine();
              System.out.println("info"+info);
              if(info.contains("欢迎"))
                  break;
           }
           bufr.close();
           s.close();
       }catch(Exception e){
           System.out.println(",,,,"+e.toString());
       }
    }
}
class ServerDuan implements Runnable{
    public void run(){
       try{
           ServerSocket ss=new ServerSocket(10115);
           while(true){
              Socket s=ss.accept();
              new Thread(new UserCheck(s)).start();
           }
       }catch(Exception e){
           System.out.println("....."+e.toString());
       }
    }
}
class UserCheck implements Runnable{
    private Socket s;
    UserCheck(Socket s){
       this.s=s;
    }
    public void run(){
       String ip=s.getInetAddress().getHostName();
       try{
           for(int x=0;x<3;x++){
              BufferedReader bufIn=new BufferedReader(new InputStreamReader(s.getInputStream()));
              String name=bufIn.readLine();
              if(name==null)
                  break;
              BufferedReader bufr=new BufferedReader(new FileReader("E:\\java练习\\13-网络编程\\user.txt"));
              PrintWriter bufOut=new PrintWriter(s.getOutputStream(),true);
              String str=null;
              boolean b=false;
              while((str=bufr.readLine())!=null){
                  if(str.equals(name)){
                     b=true;
                     break;
                  }
              }
              if(b){
                  System.out.println(ip+"::"+name+"已登陆");
                  bufOut.println(name+"欢迎光临");
                  break;
              }else{
                  System.out.println(ip+"::"+name+"正在尝试登陆");
                  bufOut.println(name+"用户不存在");
              }
           }
           s.close();
       }catch(Exception e){
           System.out.println("====="+e.toString());
       }
    }
}
public class LoginClientDemo {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       new Thread(new ClientDuan()).start();
       new Thread(new ServerDuan()).start();
    }
}
import java.io.*;
import java.net.*;
/*演示浏览器的客户端和服务端
 1,客户端:定义浏览器(telnet)
    服务端:自定义
 2,客户端:浏览器
    服务端:Tomcat服务器
 3,客户端:自定义
    服务端:Tomcat服务器
这是浏览器的客户端发送过来的请求消息头
 GET / HTTP/1.1
Accept: application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap,
Accept-Language: zh-CN
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729;
 .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0; .NET4.0C; .NET4.0E)
UA-CPU: AMD64
Accept-Encoding: gzip, deflate
Host: 127.0.0.1:11000
Connection: Keep-Alive
|   (这行和下一行都有空行)
|                        */
public class LiuLanQiDemo {
    public static void main(String[] args) throws Exception {
       // TODO 自动生成的方法存根
       ServerSocket ss=new ServerSocket(11001);
       Socket s=ss.accept();
       System.out.println(s.getInetAddress().getHostAddress());
//  打印客户端的请求:
       InputStream in=s.getInputStream();
       byte[] buf=new byte[1024];
       int len;
       while((len=in.read(buf))!=-1){
           System.out.println(new String(buf,0,len));
       }     
       PrintWriter pw=new PrintWriter(s.getOutputStream(),true);
//     pw.println("客户端你好");
       pw.println("<font color='red' size='7'>客户端你好</font>");
       s.close();
       ss.close();
    }
}
```
### URL
```java
import java.io.*;
import java.net.*;
/*String getFile() 获取此 URL 的文件名。
 String getHost() 获取此 URL 的主机名（如果适用）。
 String getPath() 获取此 URL 的路径部分。
 int getPort()  获取此 URL 的端口号。
 String getProtocol()  获取此 URL 的协议名称。
 String getQuery()  获取此 URL 的查询部分。 */
public class URL_Demo {
    public static void main(String[] args) throws MalformedURLException {
       // TODO 自动生成的方法存根
       URL url=new URL("http://127.0.0.1:11000//myweb//my.html?name=zhangsan&age=30");
      
       System.out.println("getProtocol::"+url.getProtocol());//getProtocol::http
       System.out.println("getHost::"+url.getHost());//getHost::127.0.0.1
       System.out.println("getPath::"+url.getPath());//getPath:://myweb//my.html
       System.out.println("getPort::"+url.getPort());//getPort::11000
    System.out.println("getFile::"+url.getFile());//getFile:://myweb//my.html?name=zhangsan&age=30
       System.out.println("getQuery::"+url.getQuery());//getQuery::name=zhangsan&age=30
    }
}
import java.io.*;
import java.net.*;
public class URLConnectionDemo {
    public static void main(String[] args) throws Exception {
       // TODO 自动生成的方法存根
//  由于这个路径不存在,所以下面的方法不一定行
       URL url=new URL("http://127.0.0.1:11000//myweb//my.html?name=zhangsan&age=30");
      
       URLConnection connection=url.openConnection();
       System.out.println(connection);
//  sun.net.www.protocol.http.HttpURLConnection:
//     http://127.0.0.1:11000//myweb//my.html?name=zhangsan&age=30
//  读取服务端传过来的响应,而且这个信息不带响应头(与请求头相对应)
       InputStream in=connection.getInputStream();
       int len=0;
       byte[] buf=new byte[1024];
       while((len=in.read(buf))!=-1){
           System.out.println(new String(buf,0,len));
       }
    }
}
```
## 第十四章:正则表达式
```java
/*
正则表达式:就是符合一定的规则的表达式
 作用:用于专门操作字符串
 特点:用于一些特定的符号来表示一些代码的操作,这样就可以简化书写所以学习正则表达式,就是在学习一些特殊符号的      使用
 好处:可以简化对字符串的操作
 弊端:符号定义越多,正则越长,阅读性越差
具体操作功能:
1,匹配:查阅方法  String 类中的 matches 方法,用规则匹配整个字符串,只要有一处不符合规则,匹配就结束返回false
2,切割: String类中的  split方法
3,替换:String replaceAll(String regex, String replacement)
需求:对Q号进行校验
 要求:5~15位,0不能开头,只能是数字*/
public class RegexDemo {
    public static void main(String[] args)throws Exception {
       // TODO 自动生成的方法存根
//     checkQQ();
//     checkQQ_1();
//     demo();
//     checkTel();
//     split();
       repleceAll(); 
    }
    public static void checkQQ_1()throws Exception{
       String qq="23526656";
//     String regex="[1-9][0-9]{4,14}";//下面简化
       String regex="[1-9]\\d{4,14}";
       boolean flag=qq.matches(regex);
       if(flag){
           System.out.println("qq号正确");
       }else{
           System.out.println("qq号不正确");
       }
    }
//这种方法是使用了String类中的方法,进行组合完成了需求,但是代码国语复杂
    public static void checkQQ(){
       String qq="23526656";
       int len=qq.length();
       if(len<=15&&len>=5){
           if(!(qq.startsWith("0"))){
              try{
                  long l=Long.parseLong(qq);
              }catch(Exception e){
                  System.out.println("出现非法字符");
              }
           /*  char[] chs=qq.toCharArray();
              boolean flag=true;
              for(int x=0;x<len;x++){
                  if(!(chs[x]>='0'&&chs[x]<='9')){
                     flag=false;
                     System.out.println(chs[x]+"不是0~9");
                     break;
                  }
              }
              if(flag)
                  System.out.println("QQ号正确");*/
           }else
              System.out.println("以0开头了");
       }else
           System.out.println("长度错误");
    }
    public static void demo(){
       String str="ab";
       String regex="[abcd][a-z]";//第一个字符必须是abcd 第二个字符是小写字符,不能超过规则的长度
        boolean flag=str.matches(regex);
       System.out.println(flag);//true
      
       String str1="ab9";
       String regex1="[abcd][a-z]\\d";
       boolean flag1=str1.matches(regex1);
       System.out.println(flag1);//true
    }
//匹配手机号:手机号段都是13***,或者是15***,或者是18***
    public static void checkTel(){
       String tel="13512312312";
       String regex="[1][358]\\d{9}";
       System.out.println(tel.matches(regex));//true
    }
//切割字符串
    public static void split(){
//     String str="zhangsan     lisi      wangwu";
//     String regex=",";//按照","切
//     String regex=" +";//按照空格切,空格出现一次或者多次
//  按照点切割
//     String str="zhangsan.lisi.wangwu";
//     String regex="\\.";
//  切"\"
//     String str ="c:\\abc\\bc";
//     String regex="\\\\";
//  按照叠词切割,第一位是任意字符,但是第二位要和第一位是相同字符
       String str ="akkkjvvabbbbvi";
       String regex="(.)\\1+";//为了让一规则的结果被重用,可以将规则封装成一个组
//  用()来表示. 组的出现都拥有编号,从1开始.想要使用已有的组可以通过\n()的形式来获取,n就是组的编号       //     ((()())()),想要知道有几组,可以看左边的括号,有几个代表几组,组的顺序也是看左括号
       String[] arr=str.split(regex);
       for(String s:arr)
           System.out.println(s);
    }
//替换
    public static void repleceAll(){
//     String str="wenrw2398409262fnbn408698";
//     String regex="\\d{5,}";
//     String s=str.replaceAll(regex, "#");
//     System.out.println(s);//wenrw#fnbn#
      
        String str="akkkjvvabbbbvi";
//     String regex="(.)\\1+";
//     String s=str.replaceAll(regex, "*");
//     System.out.println(s);//a*j*a*vi
        String regex="(.)\\1+";
        String s=str.replaceAll(regex, "$1");//$1表示获取第一个组的表示的符号
        System.out.println(s);//akjvabvi
    }
}
import java.util.regex.*;
/* 正则表达式:
 4,获取:将字符串中符合规则的子串取出
 操作步骤: 1,先将正则表达式风筝成对象
          2,让正则对象和要操作的字符串相关联
          3,关联后,获取正则匹配引擎
          4,通过引擎对字符串符合规则的子串进行操作,比如说获取   */
public class RegexDemo2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
       getDemo();
    }
    public  static void getDemo(){
       String s="ming tian jiu yao fang jia le";
       String regex="\\b[a-z]{3}\\b";//  \b是 单词边界
//  将正则封装成对象
       Pattern p=Pattern.compile(regex);
//  让正则对象和要作用的字符串相关联,获取匹配器对象
       Matcher m=p.matcher(s);
//     System.out.println(m.matches());//其实String类中的matches方法,用的就是Pattern和Matcher对象来完成的
    // 只不过被String类的方法封装后,用起来较为简单,但是功能却单一
//     boolean b=m.find();//将规则作用到字符串上,并进行符合规则的子串查找
//     System.out.println(b);
//     System.out.println(m.group());
       while(m.find()){
           System.out.println(m.group());
       }
    }
}
import java.util.TreeSet;
/*  正则表达式使用的规则:
 1,如果指向知道该字符串是对是错,使用匹配
 2,想要将已有的字符串变成另一个字符串,使用替换
 3,想要按照自己的方式将字符串变成多个字符串,切割.  获取规则以外的子串
 4,想要拿到符合规则的在字符串的子串,获取.  获取符合规则的子串
 
需求1:将下列字符串变成:我要学编程
    String s="我我..我我..我要..要要要....学学学..学学...编编编...程程..程";             
需求2:将ip地址进行地址段顺序的排序192.68.23.4   242.45.23.6   26.78.45.23  2.5.77.8
    1,还按照字符串的自然顺序,只要让他们每一段都是3位即可
    2,将每一段只保留3位.这样,所有的ip地址每一段都是3位
需求3:对邮件地址进行校验 */
public class RegexTest {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
//     test_1();
//     test_2();
       checkMail();
    }
    public static void test_1(){
       String s="我我..我我..我要..要要要....学学学..学学...编编编...程程..程";
       String regex="\\.+";
       String str=s.replaceAll(regex, "");
       System.out.println(str);//我我我我我要要要要学学学学学编编编程程程
       String regex1="(.)\\1+";
       String str1=str.replaceAll(regex1, "$1");
       System.out.println(str1);//我要学编程
    }
    public static void test_2(){
       String ip="192.68.23.4   242.45.23.6   26.78.45.23  2.5.77.8";
       ip=ip.replaceAll("(\\d+)", "00$1");
//     System.out.println(ip);//00192.0068.0023.004   00242.0045.0023.006   0026.0078.0045.0023  002.005.0077.008
       ip=ip.replaceAll("0*(\\d{3})", "$1");
//     System.out.println(ip);//192.068.023.004   242.045.023.006   026.078.045.023  002.005.077.008
       String[] arr=ip.split(" +");
       TreeSet<String> set=new TreeSet<String>();
       for(String i:arr)
           set.add(i);
       for(String s:set)
           System.out.println(s.replaceAll("0*(\\d+)", "$1"));
       /*  2.5.77.8
           26.78.45.23
           192.68.23.4
           242.45.23.6   */
    }
    public static void checkMail(){
       String mail="aba121@sina.com";
//     String regex="[a-zA-Z0-9]+@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)+";//这是比较精确的匹配
//     String regex="\\w+@\\w+(\\.\\w+)+";//相对不太精确的匹配
//     System.out.println(mail.matches(regex));
//     还有这种匹配方法   mail.indexOf("@")!=-1;最好不用
    }
}
import java.io.*;
import java.util.regex.*;
//网页爬虫(蜘蛛)
public class RegexTest2 {
    public static void main(String[] args) {
       // TODO 自动生成的方法存根
getMail();
    }
//获取指定的文档中的邮件地址,使用获取功能 Pattern Matcher
    public static void getMail() throws Exception{
       BufferedReader bufr=new BufferedReader(new FileReader("1.txt"));//由于文件不存在所以无法演示
       String line=null;
       String regex="[a-zA-Z0-9]+@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)+";
       while((line=bufr.readLine())!=null){
//         System.out.println(line);
           Pattern p=Pattern.compile(regex);
           Matcher m=p.matcher(line);
           while(m.find())
              System.out.println(m.group());
       }
    }
}
```
## 第十五章:反射技术
```java
import java.lang.reflect.*;
/* 应用陈股已经写好了,后期出现的接口的子类可以,向应用程序对外提供的配置文件中写入信息即可
 如果存储了指定的子类名,就根据具体的名称找该类并进行加载和对象的创建,这些动作在前期定义软件时就写好了
 没有类之前就将创建对象的动作完成了,这就是动态的获取指定的类,并使用类中的功能----这就是反射技术
 好处:反射的出现大大的提高了程序的扩展性
 class Class{//描述字节码文件的类
    Field field;(描述成员变量),将字段封装成对象类型Field
    Constructor cons;(将构造函数封装成对象类型Constructor
    Method method;
 (将类中的成员都封装成对象,提供了对这些成员的操作)
    getField();
    getConstructor();
    getMethod();
 }
想要获取字节码文件中的成员,必须先获取字节码文件对象,获取方式
    1,通过Object类中的getClass方法
       虽然通用,但是前提是必须有指定的类,并对该类进行对象的创建,才可以调用getClass方法
    2,使用任意数据类性的静态成员class,这是所有数据类型都具备的一个属性
    3,使用的是Class类中的forName();方法通过给定的类名来获取对应的字节码文件对象
       这种方式很爽,只要知道类的名字就可以了.获取字节码文件直接有forName方法自动完成
       这就是反射技术使用的获取字节码文件对象的方式 */
 
public class ReflectDemo {
    public static void main(String[] args) throws Exception {
//     getClass_1();
//     getClass_2();
       getClass_3();
    }
    private static void getClass_3() throws Exception {
//  这边的className右边对应的类名必须是全名,包名+类名
       String className="Person";
       Class class1=Class.forName(className);
//     System.out.println(class1);//class Person
//  字节码文件对象有了以后就可以创建,该字节码对象表示的类的实例
       Object obj=class1.newInstance();
       System.out.println(obj);//Person@6996db8
/*     Person p=new   Person();
       这句话做的事情:1,加载Person类
                    2,通过new创建Person对象
                    3,调用构造函数对对象进行初始化
       Object obj=class1.newInstance();
       这句话做的事情:1,通过上一步给定的类名称,加载对应的字节码文件,并封装成字节码文件对象Class
                     通过newInstance();就可以创建字节码文件对象所表示的新实例
                    2,通过new创建给定的类的实例
                    3,调用该类的构造函数
            通常被反射的类都会有提供空参数的构造函数,没有空参数的构造函数会报InstantiationException异常
            如果有空参数构造函数会发生IllegalAccessException异常  */
    }
    private static void getClass_2() {
       Class class1=Person.class;
       System.out.println(class1);//class Person
    }
    public static void getClass_1(){
       Person p1=new Person();
       Person p2=new Person();
       Class class1=p1.getClass();
       Class class2=p2.getClass();
       System.out.println(class1.getName());//获取类的名字   YanShi_Person
       System.out.println(class1==class2);//true  因为java中字节码文件对象只有一个,
//                          所以产生的class是相共同的
    }
}
import java.lang.reflect.*;
public class ReflectDemo2 {
    public static void main(String[] args)throws Exception {
       // TODO 自动生成的方法存根
//     getConstructor_1();
       getField_1();
    }
    public static void getConstructor_1()throws Exception{
/*     如果要通过指定的构造函数初始化对象该怎么办呢?
       思路:1,获取字节码文件对象
            2,在获取给定的构造函数
            3,通过构造函数初始化对象      
 */    String className="Person";
       Class class1=Class.forName(className);
//     获取指定的构造器. 获取Person类中两个参数 String int的构造函数
       @SuppressWarnings("unchecked")
       Constructor cons=class1.getConstructor(String.class,int.class);
       Object obj=cons.newInstance("zhangsan",12);//这里面的参数相当于 new Person("张三",21);
       System.out.println(obj);//zhangsan::12
    }
//  获取字段
    public static void getField_1()throws Exception{
       String className="Person";
       Class class1=Class.forName(className);
       String fieldName="age";
      
//     Field field=class1.getField(fieldName);//获取的是公共的字段
       Field field=class1.getDeclaredField(fieldName);//获取的是已经声明的字段
//  对其进行值设置,必须先获取到其对象
       Object obj=class1.newInstance();
//     field.set(obj, 20);//因为,age是private修饰的,所以不可以访问,抛出 IllegalAccessException异常
//  通过这个方法,访问被私有修饰的字段,这是      
       field.setAccessible(true);//取消权限检查,或者称为暴力访问;  一般不访问私有的成员
       field.set(obj, 30);
       System.out.println(field.get(obj));//30
//如果 getXXX():获取的是public 修饰的成员;如果是getDeclaredXXX();获取的已经声明的成员 
    }
}
public class Person {
    private String name;
    private int age;
    Person(){
       super();
    }
    //其他区的构造函数权限必须是public的
    public Person(String name,int age){
       super();
       this.name=name;
       this.age=age;
    }
    public void method(){
       System.out.println("haha");
    }
    public void show(String name,int age){
       System.out.println(name+"--"+age);
    }
    public static void staticShow(){
       System.out.println("staticShow   run");
    }
    public String toString(){
       return name+"::"+age;
    }
}
import java.lang.reflect.*;
public class ReflectDemo3 {
    public static void main(String[] args) throws Exception{
       // TODO 自动生成的方法存根
//     getMethod_1();
       staticShow();
    }
    public  static void getMethod_1()throws Exception{
       String className="Person";
       Class class1=Class.forName(className);
       String methodName="show";
       Method method=class1.getMethod(methodName,String.class,int.class);
       Object obj=class1.newInstance();
       method.invoke(obj, "zhangsan",20);//zhangsan--20
    }
    public  static void staticShow()throws Exception{
       String className="Person";
       Class class1=Class.forName(className);
       String methodName="staticShow";
       Method method=class1.getMethod(methodName, null);
//  因为是静态方法,所以可以直接用类名调用,也可以什么都不传
       method.invoke(class1);//staticShow   run   
       method.invoke(null,null);//staticShow   run
    }
}
 
import java.io.*;
import java.util.*;
public class NoteBookMain {
    public static void main(String[] args) throws Exception{
/*   案例一
        第一阶段:笔记本电脑运行.  NoteBook run();
        第二阶段:想要使用一些外围设备比如鼠标,键盘,....
           为了提高笔记本的扩展性,应该降低这些设备和笔记本的耦合性--需要接口
           只需要在设计之初,定义一个接口.而笔记本在使用这个接口
        后期有了USB设备后,需要不断的new对象才可以使用,每一次都要修改代码
        能不能不修改这个代码,就可以使用后期的设备呢?
           设备不能明确,而前期还要对其进行对象的建立,需要反射技术,对外提供配置文件 */
//     NoteBook book=new NoteBook();
//     book.run();
//     book.useUSB(null);
      
//  通过反射的方式,重新设计应用程序,以提高更好的扩展性
       NoteBook book=new NoteBook();
       book.run();
       File configFile=new File("usb.properties");
       if(!(configFile.exists())){
           configFile.createNewFile();
       }
//  读取配置文件
       FileReader fr=new FileReader(configFile);
//     为了获取其中的键值细腻方便,建立Properties
       Properties prop=new Properties();
       prop.load(fr);
       for(int x=1;x<=prop.size();x++){
           String className=prop.getProperty("usb"+x);
           Class class1=Class.forName(className);
           USB usb=(USB)class1.newInstance();
           book.useUSB(usb);
       }
       fr.close();
    }
}
-------------------
public class NoteBook {
//  电脑运行
    public void run(){
       System.out.println("notebook  run");
    }
//  使用usb设备
    public void useUSB(USB usb) {
       if(usb!=null){
           usb.open();
           usb.close();
       }
    }
}
------------------------------------
public interface USB {
//  开启
    public void open();
//  关闭
    public void close();
}
---------------------------------------------
public class USBMouse implements USB {
    public void open() {
       System.out.println("mouse  open");
    }
    public void close() {
       System.out.println("mouse  close");
    }
}
public class USBKey implements USB {
    public void open() {
       System.out.println("usbKey  open");
    }
    public void close() {
       System.out.println("usbKey  close");
    }
}
```
-----配置文件中的内容,要自己写进去---------
usb1=USBMouse
usb2=USBKey