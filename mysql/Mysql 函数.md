# Mysql 函数

[参照](https://www.cnblogs.com/xuyulin/p/5468102.html)

## 字符串函数

[示例](#ASCII)

### 总览

| 函数                  | 描述                                                         | 示例          |
| --------------------- | ------------------------------------------------------------ | ------------- |
| ascii(s)       | 返回字符串 s 的第一个字符的 ASCII 码                         | [示例](#ascii) |
| conv(n,from_base,to_base) | 对数字n进制转换,并转换为字串返回<br/>（任何参数为null时返回null，进制范围为2-36进制，<br>当to_base是负数时n作为有符号数否则作无符号数，conv以64位点精度工作） | [示例](#conv) |
| bin(n)，oct(n)，hex(n) | 把n转为二/八/十六进制值并以字串返回(n是bigint数字,等价于conv(n,10,2/8/16)) | [示例](#bin) |
| char(n,...) | 返回由参数n,...对应的ascii代码字符组成的一个字串(参数是n,...是数字序列,null值被跳过) | [示例](#char) |
| concat(s1,s2...sn) | 字符串 s1,s2 等多个字符串合并为一个字符串 | [示例](#concat) |
| concat_ws(x, s1,s2...sn) | 同 CONCAT(s1,s2,...) 函数，但是每个字符串之间要加上 x，x 可以是分隔符 | [示例](#concat_ws) |
| length(s)<br/>octet_length(s) | 返回字符串 s 的字符数（按照**字节**来统计）                   | [示例](#length) |
| char_length(s)<br>character_length(s) | 返回字符串 s 的字符数（按照**字符**来统计）                         | [示例](#char_length) |
| locate(s1,s)<br/>position(s1 in s)    | 返回字符串s1在字符串s第一次出现的位置(s不包含s1时返回0)      | [示例](#locate)      |
| locate(s1,s,pos)                      | 返回字符串s1在字符串s的第pos个位置起第一次出现的位置(s不包含s1时返回0) | [示例](#locate)      |
| instr(s,s1)                           | 返回字符串s1在字符串s第一次出现的位置(s不包含s1时返回0)      | [示例](#instr)       |
| lpad(str,len,padstr)<br>rpad(str,len,padstr) | 用字符串padstr填补str左/右端直到字串长度为len并返回 | [示例](#lpad) |
| left(str,len)，right(str,len) | 返回字符串str的左/右端len个字符 | [示例](#left) |
| substring(str,pos,len)  <br>substring(str from pos for len)  <br>mid(str,pos,len) | 返回字符串str的位置pos起len个字符 | [示例](#substring) |
| substring(str,pos)  <br>substring(str from pos) | 返回字符串str的位置pos起的一个子串 | [示例](#substring) |
| substring_index(str,d,count) | 返回从字符串str的第count个出现的分隔符d之前的子串<br/>(count为正数时从左开始,否则从右开始) | [示例](#substring_index) |
| ltrim(str)，rtrim(str) | 返回删除了左/右空格的字符串str | [示例](#ltrim) |
| trim([\[both\|leading\|trailing\] [remstr] from] str) | 返回前缀或后缀remstr被删除了的字符串str<br/>(位置参数默认both,remstr默认值为空格) | [示例](#ltrim) |
| space(n) | 返回由n个空格字符组成的一个字符串 | [示例](#space) |
| replace(str,from_str,to_str) | 用字符串to_str替换字符串str中的子串from_str并返回 | [示例](#replace) |
| repeat(str,count) | 返回由count个字符串str连成的一个字符串<br/>(任何参数为null时返回null,count<=0时返回一个空字符串) | [示例](#repeat) |
| reverse(str) | 颠倒字符串str的字符顺序并返回 | [示例](#reverse) |
| insert(str,pos,len,newstr) | 把字符串str由位置pos起len个字符长的子串替换为字符串newstr并返回 | [示例](#insert) |
| elt(n,str1,str2,str3,...) | field(str,str1,str2,str3,...) | [示例](#elt) |
| field(str,str1,str2,str3,...) | 返回str等于其后的第n个字符串的序号(如果str没找到返回0) | [示例](#field) |
| find_in_set(str,strlist) | 返回str在字符串集strlist中的序号<br/>(任何参数是null则返回null,如果str没找到返回0,参数1包含","时工作异常) | [示例](#find_in_set) |
| lcase(str)，lower(str)<br/>ucase(str) ，upper(str) | 返回小/大写的字符串str | [示例](#lcase) |
| load_file(file_name) | 读入文件并且作为一个字符串返回文件内容<br/>(文件无法找到,路径不完整,没有权限,长度大于max_allowed_packet会返回null) | [示例](#load_file) |


### 示例

<a id="ascii">ascii</a>

```mysql
mysql> select ascii('2'); 
　　-> 50 
mysql> select ascii(2); 
　　-> 50 
mysql> select ascii('dete'); 
　　-> 100 
```

<a id="conv">conv</a>
```mysql
mysql> select conv("a",16,2); 
　　-> '1010'
mysql> select conv("6e",18,8); 
　　-> '172'
mysql> select conv(-17,10,-18); 
　　-> '-h'
mysql> select conv(10+"10"+'10'+0xa,10,10); 
　　-> '40' 
```

<a id="bin">bin，oct，hex</a>
```mysql
mysql> select bin(12); 
　　-> '1100' 
mysql> select oct(12); 
　　-> '14' 
mysql> select hex(255); 
　　-> 'ff' 
```

<a id="char">char</a>
```mysql
mysql> select char(77,121,83,81,'76'); 
　　-> 'mysql'
mysql> select char(77,77.3,'77.3'); 
　　-> 'mmm' 
```

<a id="concat">concat</a>
```mysql
mysql> select concat('my', 's', 'ql'); 
　　-> 'mysql'
mysql> select concat('my', null, 'ql'); 
　　-> null
mysql> select concat(14.3); 
　　-> '14.3' 
```

<a id="concat_ws">concat_ws</a>
```mysql
mysql> select concat_ws("-", "SQL", "Tutorial", "is", "fun!", null);
　　-> 'SQL-Tutorial-is-fun!'
```

<a id="length">length</a>
```mysql
-- utf8字符集中,一个汉字占3个字节,新的utf8mb4字符集中一个汉字占4个字节.
mysql> select length('text我');
　　-> 7
mysql> select octet_length('text我');
　　-> 7
```

<a id="char_length">char_length</a>

```mysql
-- utf8字符集中,一个汉字占3个字节,新的utf8mb4字符集中一个汉字占4个字节.
mysql> select char_length('text我');
　　-> 5 -- 中文占1个字符
mysql> select character_length('text我');
　　-> 5 -- 中文占1个字符
```

<a id="locate">locate</a>
```mysql
mysql> select locate('bar', 'foobarbar');
　　-> 4
mysql> select locate('xbar', 'foobar');
　　-> 0
mysql> select locate('bar', 'foobarbar',5);
　　-> 7
```

<a id="instr">instr</a>
```mysql
mysql> select instr('foobarbar', 'bar');
　　-> 4
mysql> select instr('xbar', 'foobar');
　　-> 0
```

<a id="lpad">lpad，rpad</a>
```mysql
mysql> select lpad('hi',4,'??'); 
　　-> '??hi'
mysql> select rpad('hi',5,'?'); 
　　-> 'hi???'
```

<a id="left">left，right</a>
```mysql
mysql> select left('foobarbar', 5);
　　-> 'fooba'
mysql> select right('foobarbar', 4);
　　-> 'rbar'
```

<a id="substring">substring</a>
```mysql
mysql> select substring('quadratically',5,6);
　　-> 'ratica'
mysql> select substring('quadratically',5);
　　-> 'ratically'
mysql> select substring('foobarbar' from 4);
　　-> 'barbar'
```

<a id="substring_index">substring_index</a>
```mysql
mysql> select substring_index('www.mysql.com', '.', 2);
　　-> 'www.mysql'
mysql> select substring_index('www.mysql.com', '.', -2);
　　-> 'mysql.com' 
```

<a id="ltrim">ltrim</a>
```mysql
mysql> select ltrim('  barbar');
　　-> 'barbar'
mysql> select rtrim('barbar   ');
　　-> 'barbar'

-- trim
mysql> select trim('  bar   ');
　　-> 'bar'
mysql> select trim(leading 'x' from 'xxxbarxxx');
　　-> 'barxxx'
mysql> select trim(both 'x' from 'xxxbarxxx');
　　-> 'bar'
mysql> select trim(trailing 'xyz' from 'barxxyz');
　　-> 'barx'
```

<a id="space">space</a>：
```mysql
mysql> select space(6);
　　-> '      '
```

<a id="replace">replace</a>
```mysql
mysql> select replace('www.mysql.com', 'w', 'ww');
　　-> 'wwwwww.mysql.com'
```

<a id="repeat">repeat</a>
```mysql
mysql> select repeat('mysql', 3);
　　-> 'mysqlmysqlmysql'
```

<a id="reverse">reverse</a>

```mysql
mysql> select reverse('abc');
　　-> 'cba'
```

<a id="insert">insert</a>
```mysql
mysql> select insert('quadratic', 3, 4, 'what');
　　-> 'quwhattic'
```

<a id="elt">elt</a>
```mysql
mysql> select elt(1, 'ej', 'heja', 'hej', 'foo'); 
　　-> 'ej'
mysql> select elt(4, 'ej', 'heja', 'hej', 'foo'); 
　　-> 'foo' 
```

<a id="field">field</a>

```mysql
mysql> select field('ej', 'hej', 'ej', 'heja', 'hej','foo');
　　-> 2
mysql> select field('fo', 'hej', 'ej', 'heja', 'hej','foo');
　　-> 0
```

<a id="find_in_set">find_in_set</a>
```mysql
mysql> select find_in_set('b','a,b,c,d');
　　-> 2
```

<a id="lcase">lcase，lower，ucase ，upper</a>

```mysql
mysql> select lower('quadratically'); 
　　-> 'quadratically'
mysql> select upper('quadratically'); 
　　-> 'quadratically' 
```

<a id="load_file">load_file</a>
```mysql
mysql> update table_name set blob_column=load_file("/tmp/picture") where id=1;
```


## 数字函数

### 总览
| 函数                  | 描述                                                         | 示例          |
| --------------------- | ------------------------------------------------------------ | ------------- |
| abs(n) | 返回n的绝对值 | [示例](#abs) |
| sign(n) | 返回参数的符号(为-1、0或1) | [示例](#sign) |
| mod(n,m) | 取模运算,返回n被m除的余数(同%操作符) | [示例](#mod) |
| floor(n) | 返回不大于n的最大整数值 | [示例](#floor) |
| ceiling(n) | 返回不小于n的最小整数值 | [示例](#ceiling) |
| round(n,d) | 返回n的四舍五入值,保留d位小数(d的默认值为0) | [示例](#round) |
| exp(n) | 返回值e的n次方(自然对数的底) | [示例](#exp) |
| log(n) | 返回n的自然对数 | [示例](#log) |
| log10(n) | 返回n以10为底的对数 | [示例](#log10) |
| pow(x,y)，power(x,y) | 返回值x的y次幂 | [示例](#pow) |
| sqrt(n) | 返回非负数n的平方根 | [示例](#sqrt) |
| pi() | 返回圆周率 | [示例](#pi) |
| cos(n) | 返回n的余弦值 | [示例](#cos) |
| sin(n) | 返回n的正弦值 | [示例](#sin) |
| tan(n)               | 返回n的正切值 | [示例](#tan) |
| acos(n) | 返回n反余弦(n是余弦值,在-1到1的范围,否则返回null) | [示例](#acos) |
| asin(n) | 返回n反正弦值 | [示例](#asin) |
| atan(n) | 返回n的反正切值 | [示例](#atan) |
| atan2(x,y) | 返回2个变量x和y的反正切(类似y/x的反正切,符号决定象限) | [示例](#atan2) |
| cot(n) | 返回x的余切 | [示例](#cot) |
| rand()，rand(n) | 返回在范围0到1.0内的随机浮点值(可以使用数字n作为初始值) | [示例](#rand) |
| degrees(n) | 把n从弧度变换为角度并返回 | [示例](#degrees) |
| radians(n) | 把n从角度变换为弧度并返回 | [示例](#radians) |
| truncate(n,d) | 保留数字n的d位小数并返回 | [示例](#truncate) |
| least(x,y,...) | 返回最小值<br>(如果返回值被用在整数上下文或所有参数都是整数则他们作为整数比较,否则按忽略大小写的字符串被比较)<br>> 整数(实数或大小敏感字串) | [示例](#least) |
| greatest(x,y,...) | 返回最大值(其余同least()) | [示例](#greatest) |


### 示例

<a id="abs">abs</a>
```mysql
mysql> select abs(2);   
　　-> 2   
mysql> select abs(-32);   
　　-> 32 
```

<a id="sign">sign</a>
```mysql
mysql> select sign(-32);   
　　-> -1   
mysql> select sign(0);   
　　-> 0   
mysql> select sign(234);   
　　-> 1  
```

<a id="mod">mod</a>
```mysql
mysql> select mod(234, 10);   
　　-> 4   
mysql> select 234 % 10;   
　　-> 4   
mysql> select mod(29,9);   
　　-> 2   
```

<a id="floor">floor</a>
```mysql
mysql> select floor(1.23);   
　　-> 1   
mysql> select floor(-1.23);   
　　-> -2    
```

<a id="ceiling">ceiling</a>
```mysql
mysql> select ceiling(1.23);   
　　-> 2   
mysql> select ceiling(-1.23);   
　　-> -1
```

<a id="round">round</a>
```mysql
mysql> select round(-1.23);   
　　-> -1   
mysql> select round(-1.58);   
　　-> -2   
mysql> select round(1.58);   
　　-> 2   
mysql> select round(1.298, 1);   
　　-> 1.3   
mysql> select round(1.298, 0);   
　　-> 1 
```

<a id="exp">exp</a>
```mysql
mysql> select exp(2);   
　　-> 7.389056   
mysql> select exp(-2);   
　　-> 0.135335   
```

<a id="log">log</a>
```mysql
mysql> select log(2);   
　　-> 0.693147   
mysql> select log(-2);   
　　-> null 
```

<a id="log10">log10</a>
```mysql
mysql> select log10(2);   
　　-> 0.301030   
mysql> select log10(100);   
　　-> 2.000000   
mysql> select log10(-100);   
　　-> null  
```

<a id="pow">pow</a>
```mysql
mysql> select pow(2,2);   
　　-> 4.000000   
mysql> select pow(2,-2);   
　　-> 0.250000 
```

<a id="sqrt">sqrt</a>
```mysql
mysql> select sqrt(4);   
　　-> 2.000000   
mysql> select sqrt(20);   
　　-> 4.472136  
```

<a id="pi">pi</a>
```mysql
mysql> select pi();   
　　-> 3.141593  
```

<a id="cos">cos</a>
```mysql
mysql> select cos(pi()); 
　　-> -1.000000
```

<a id="sin">sin</a>
```mysql
mysql> select sin(pi());   
　　-> 0.000000 
```

<a id="tan">tan</a>
```mysql
mysql> select tan(pi()+1);   
　　-> 1.557408 
```

<a id="acos">acos</a>
```mysql
mysql> select acos(1);   
　　-> 0.000000   
mysql> select acos(1.0001);   
　　-> null   
mysql> select acos(0);   
　　-> 1.570796  
```

<a id="asin">asin</a>
```mysql
mysql> select asin(0.2);   
　　-> 0.201358   
mysql> select asin('foo');   
　　-> 0.000000
```

<a id="atan">atan</a>
```mysql
mysql> select atan(2);   
　　-> 1.107149   
mysql> select atan(-2);   
　　-> -1.107149 
```

<a id="atan2">atan2</a>
```mysql
mysql> select atan(-2,2);   
　　-> -0.785398   
mysql> select atan(pi(),0);   
　　-> 1.570796
```

<a id="cot">cot</a>
```mysql
mysql> select cot(12);   
　　-> -1.57267341   
mysql> select cot(0);   
　　-> null
```

<a id="rand">rand</a>
```mysql
mysql> select rand();   
　　-> 0.5925   
mysql> select rand(20);   
　　-> 0.1811   
mysql> select rand(20);   
　　-> 0.1811   
mysql> select rand();   
　　-> 0.2079   
mysql> select rand();   
　　-> 0.7888
```

<a id="degrees">degrees</a>
```mysql
mysql> select degrees(pi());   
　　-> 180.000000 
```

<a id="radians">radians</a>
```mysql
mysql> select radians(90);   
　　-> 1.570796 
```

<a id="truncate">truncate</a>

```mysql
mysql> select truncate(1.223,1);   
　　-> 1.2   
mysql> select truncate(1.999,1);   
　　-> 1.9   
mysql> select truncate(1.999,0);   
　　-> 1 
```

<a id="least">least</a>
```mysql
mysql> select least(2,0);   
　　-> 0   
mysql> select least(34.0,3.0,5.0,767.0);   
　　-> 3.0   
mysql> select least("b","a","c");   
　　-> "a" 
```

<a id="greatest">greatest</a>

```mysql
mysql> select greatest(2,0);   
　　-> 2   
mysql> select greatest(34.0,3.0,5.0,767.0);   
　　-> 767.0   
mysql> select greatest("b","a","c");   
　　-> "c"
```

## 日期函数

### 总览
| 函数                  | 描述                                                         | 示例          |
| --------------------- | ------------------------------------------------------------ | ------------- |
| dayofweek(date) | 返回日期date是星期几(1=星期天,2=星期一,……7=星期六,odbc标准) | [示例](#dayofweek) |
| weekday(date) | 返回日期date是星期几(0=星期一,1=星期二,……6= 星期天)。 | [示例](#weekday) |
| dayofmonth(date) | 返回date是一月中的第几日(在1到31范围内) | [示例](#dayofmonth) |
| dayofyear(date) | 返回date是一年中的第几日(在1到366范围内) | [示例](#dayofyear) |
| month(date) | 返回date中的月份数值 | [示例](#month) |
| dayname(date) | 返回date是星期几(按英文名返回) | [示例](#dayname) |
| monthname(date) | 返回date是几月(按英文名返回) | [示例](#monthname) |
| quarter(date) | 返回date是一年的第几个季度 | [示例](#quarter) |
| week(date,first) | 返回date是一年的第几周(first默认值0,first取值1表示周一是周的开始,0从周日开始) | [示例](#week) |
| year(date) | 返回date的年份(范围在1000到9999) | [示例](#year) |
| hour(time) | 返回time的小时数(范围是0到23) | [示例](#hour) |
| minute(time) | 返回time的分钟数(范围是0到59) | [示例](#minute) |
| second(time) | 返回time的秒数(范围是0到59) | [示例](#second) |
| period_add(p,n) | 增加n个月到时期p并返回(p的格式yymm或yyyymm) | [示例](#period_add) |
| period_diff(p1,p2) | 返回在时期p1和p2之间月数(p1和p2的格式yymm或yyyymm) | [示例](#period_diff) |
| date_add(date,interval expr type) <br/>date_sub(date,interval expr type)   <br/>adddate(date,interval expr type)   <br/>subdate(date,interval expr type) | 对日期时间进行加减法运算 | [示例](#date_add) |
| to_days(date) | 返回日期date是西元0年至今多少天(不计算1582年以前) | [示例](#to_days) |
| from_days(n) | 给出西元0年至今多少天返回date值(不计算1582年以前) | [示例](#from_days) |
| date_format(date,format) | 根据format字符串格式化date值<br> | [示例](#date_format) |
| time_format(time,format) | 和date_format()类似,但time_format只处理小时、分钟和秒(其余符号产生一个null值或0) |  |
| curdate()    <br/>current_date() | 以'yyyy-mm-dd'或yyyymmdd格式返回当前日期值(根据返回值所处上下文是字符串或数字) | [示例](#curdate) |
| curtime()   <br/>current_time() | 以'hh:mm:ss'或hhmmss格式返回当前时间值(根据返回值所处上下文是字符串或数字) | [示例](#curtime) |
| now()   <br/>sysdate()   <br/>current_timestamp() | 以'yyyy-mm-dd hh:mm:ss'或yyyymmddhhmmss格式返回当前日期时间<br/>(根据返回值所处上下文是字符串或数字) | [示例](#now) |
| unix_timestamp()   <br/>unix_timestamp(date) | 返回一个unix时间戳(从'1970-01-01 00:00:00'gmt开始的秒数,date默认值为当前时间) | [示例](#unix_timestamp) |
| from_unixtime(unix_timestamp) | 以'yyyy-mm-dd hh:mm:ss'或yyyymmddhhmmss格式返回时间戳的值<br/>(根据返回值所处上下文是字符串或数字) | [示例](#from_unixtime) |
| from_unixtime(unix_timestamp,format) | 以format字符串格式返回时间戳的值 |  [示例](from_unixtime#)|
| sec_to_time(seconds) | 以'hh:mm:ss'或hhmmss格式返回秒数转成的time值<br/>(根据返回值所处上下文是字符串或数字) | [示例](#sec_to_time) |
| time_to_sec(time) | 返回time值有多少秒 | [示例](#time_to_sec) |

- date_add(date,interval expr type) 
> type值 含义 期望的expr格式: 
> 　second 秒 seconds 
> 　minute 分钟 minutes
> 　hour 时间 hours
> 　day 天 days 
> 　month 月 months
> 　year 年 years
> 　minute_second 分钟和秒 "minutes:seconds" 
> 　hour_minute 小时和分钟 "hours:minutes" 
> 　day_hour 天和小时 "days hours"
> 　year_month 年和月 "years-months"
> 　hour_second 小时, 分钟， "hours:minutes:seconds"
> 　day_minute 天, 小时, 分钟 "days hours:minutes"
> 　day_second 天, 小时, 分钟, 秒 "days
> hours:minutes:seconds"
> 　expr中允许任何标点做分隔符,如果所有是date值时结果是一个
> date值,否则结果是一个datetime值) 
> 　如果type关键词不完整,则mysql从右端取值,day_second因为缺
> 少小时分钟等于minute_second) 
> 　如果增加month、year_month或year,天数大于结果月份的最大天
> 数则使用最大天数) 


- date_format(date,format) 中 format 格式：
> 　%Y 年, 数字, 4 位
> 　%y 年, 数字, 2 位
> 　%m 月, 数字(01……12)
> 　%c 月, 数字(1……12)
> 　%M 月名字(january……december)
> 　%d 月份中的天数, 数字(00……31) 
> 　%e 月份中的天数, 数字(0……31)
> 　%W 星期名字(sunday……saturday) 
> 　%d 有英语前缀的月份的日期(1st, 2nd, 3rd, 等等
> 　%a 缩写的星期名字(sun……sat) 
> 　%b 缩写的月份名字(jan……dec) 
> 　%j 一年中的天数(001……366) 
> 　%h 小时(00……23) 
> 　%k 小时(0……23)
> 　%H 小时(01……12) 
> 　%i 小时(01……12) 
> 　%l 小时(1……12)
> 　%i 分钟, 数字(00……59) 
> 　%r 时间,12 小时(hh:mm:ss [ap]m) 
> 　%t 时间,24 小时(hh:mm:ss) 
> 　%s 秒(00……59) 
> 　%s 秒(00……59) 
> 　%p am或pm 
> 　%w 一个星期中的天数(0=sunday ……6=saturday ）
> 　%u 星期(0……52), 这里星期天是星期的第一天
> 　%u 星期(0……52), 这里星期一是星期的第一天
> 　%% 字符% 



### 示例




<a id="dayofweek">dayofweek</a>
```mysql
mysql> select dayofweek('1998-02-03');   
　　-> 3
```

<a id="weekday">weekday</a>
```mysql
mysql> select weekday('1997-10-04 22:23:00');   
　　-> 5   
mysql> select weekday('1997-11-05');   
　　-> 2  
```

<a id="dayofmonth">dayofmonth</a>
```mysql
mysql> select dayofmonth('1998-02-03');   
　　-> 3
```

<a id="dayofyear">dayofyear</a>
```mysql
mysql> select dayofyear('1998-02-03');   
　　-> 34 
```

<a id="month">month</a>
```mysql
mysql> select month('1998-02-03');   
　　-> 2
```

<a id="dayname">dayname</a>
```mysql
mysql> select dayname("1998-02-05");   
　　-> 'thursday'
```

<a id="monthname">monthname</a>
```mysql
mysql> select monthname("1998-02-05");   
　　-> 'february'
```

<a id="quarter">quarter</a>
```mysql
mysql> select quarter('98-04-01');   
　　-> 2
```

<a id="week">week</a>
```mysql
mysql> select week('1998-02-20');   
　　-> 7   
mysql> select week('1998-02-20',0);   
　　-> 7   
mysql> select week('1998-02-20',1);   
　　-> 8
```

<a id="year">year</a>
```mysql
mysql> select year('98-02-03');   
　　-> 1998
```

<a id="hour">hour</a>
```mysql
mysql> select hour('10:05:03');   
　　-> 10 
```

<a id="minute">minute</a>
```mysql
mysql> select minute('98-02-03 10:05:03');   
　　-> 5
```

<a id="second">second</a>
```mysql
mysql> select second('10:05:03');   
　　-> 3
```

<a id="period_add">period_add</a>
```mysql
mysql> select period_add(9801,2);   
　　-> 199803
```

<a id="period_diff">period_diff</a>
```mysql
mysql> select period_diff(9802,199703);   
　　-> 11
```

<a id="date_add">date_add</a>
```mysql
mysql> select "1997-12-31 23:59:59" + interval 1 second; 
　　-> 1998-01-01 00:00:00   
mysql> select interval 1 day + "1997-12-31";   
　　-> 1998-01-01   
mysql> select "1998-01-01" - interval 1 second;   
　　-> 1997-12-31 23:59:59   
mysql> select date_add("1997-12-31 23:59:59",interval 1 second);   
　　-> 1998-01-01 00:00:00   
mysql> select date_add("1997-12-31 23:59:59",interval 1 day);   
　　-> 1998-01-01 23:59:59   
mysql> select date_add("1997-12-31 23:59:59",interval "1:1" minute_second);   
　　-> 1998-01-01 00:01:00   
mysql> select date_sub("1998-01-01 00:00:00",interval "1 1:1:1" day_second);   
　　-> 1997-12-30 22:58:59   
mysql> select date_add("1998-01-01 00:00:00", interval "-1 10" day_hour); 
　　-> 1997-12-30 14:00:00   
mysql> select date_sub("1998-01-02", interval 31 day);   
　　-> 1997-12-02   
mysql> select extract(year from "1999-07-02");   
　　-> 1999   
mysql> select extract(year_month from "1999-07-02 01:02:03");   
　　-> 199907   
mysql> select extract(day_minute from "1999-07-02 01:02:03");   
　　-> 20102 
```

<a id="to_days">to_days</a>
```mysql
mysql> select to_days(950501);   
　　-> 728779   
mysql> select to_days('1997-10-07');   
　　-> 729669
```

<a id="from_days">from_days</a>
```mysql
mysql> select from_days(729669);   
　　-> '1997-10-07'
```

<a id="date_format">date_format</a>
```mysql
mysql> select date_format('1997-10-04 22:23:00','%W %M %Y');  
　　-> 'saturday october 1997'   
mysql> select date_format('1997-10-04 22:23:00','%:%i:%s');   
　　-> '22:23:00'   
mysql> select date_format('1997-10-04 22:23:00','%d %y %a %d %m %b %j');   
　　-> '4th 97 sat 04 10 oct 277'   
mysql> select date_format('1997-10-04 22:23:00','%h %k %i %r %t %s %w');   
　　-> '22 22 10 10:23:00 pm 22:23:00 00 6'
```

<a id="curdate">curdate</a>

```mysql
mysql> select curdate();   
　　-> '2020-08-26'   
mysql> select curdate() + 0;   
　　-> 20200826 
```

<a id="curtime">curtime</a>
```mysql
mysql> select curtime();   
　　-> '23:50:26'   
mysql> select curtime() + 0;   
　　-> 235026
```

<a id="now">now</a>
```mysql
mysql> select now();   
　　-> '2020-08-26 19:08:43'   
mysql> select now() + 0;   
　　-> 20200826190843
```

<a id="unix_timestamp">unix_timestamp</a>
```mysql
mysql> select unix_timestamp();   
　　-> 1598440157   
mysql> select unix_timestamp('2020-08-26 19:08:43');   
　　-> 1598440123
```

<a id="from_unixtime">from_unixtime</a>
```mysql
mysql> select from_unixtime(1598440123);   
　　-> '2020-08-26 19:08:43'   
mysql> select from_unixtime(1598440123) + 0;   
　　-> 20200826190843 
mysql> select from_unixtime(unix_timestamp(),'%Y-%d-%m %H:%i:%s');   
　　-> '2020-26-08 19:12:16'
```

<a id="sec_to_time">sec_to_time</a>
```mysql
mysql> select sec_to_time(2378);   
　　-> '00:39:38'   
mysql> select sec_to_time(2378) + 0;   
　　-> 3938
```

<a id="time_to_sec">time_to_sec</a>
```mysql
mysql> select time_to_sec('22:23:00');   
　　-> 80580   
mysql> select time_to_sec('00:39:38');   
　　-> 2378
```


## 高级函数

### 总览
| 函数                  | 描述                                                         | 示例          |
| --------------------- | ------------------------------------------------------------ | ------------- |
| cast(x as type) | 转换数据类型 | [示例](#) |
| coalesce(expr1, expr2, ...., expr_n) | 返回参数中的第一个非空表达式（从左向右） | [示例](#) |
| convert(s USING cs) | 函数将字符串 s 的字符集变成 cs | [示例](#) |
| if(expr,v1,v2) | 如果表达式 expr 成立，返回结果 v1；否则，返回结果 v2。 | [示例](#) |
| ifnull(v1,v2) | 如果 v1 的值不为 NULL，则返回 v1，否则返回 v2。 | [示例](#) |
| isnull(expression) | 判断表达式是否为 NULL |  |
| nullif(expr1, expr2) | 比较两个字符串，如果字符串 expr1 与 expr2 相等 返回 NULL，否则返回 expr1 | [示例](#) |
| CASE expression<br>WHEN condition1 THEN result1  <br>ELSE result END | CASE 表示函数开始，END 表示函数结束。如果 condition1 成立，则返回 result1<br>当全部不成立则返回 result，而当有一个成立之后，后面的就不执行了。 | [示例](#) |

### 示例
<a id="cast">cast</a>

```mysql
mysql> SELECT CAST("2017-08-29" AS DATE);
　　-> 2017-08-29
```
<a id="coalesce">coalesce</a>

```mysql
mysql> SELECT COALESCE(NULL, NULL, NULL, 'runoob.com', NULL, 'google.com');
　　-> 'runoob.com'
```
<a id="convert">convert</a>

```mysql
mysql> SELECT CHARSET(CONVERT('ABC' USING gbk))
　　-> 'gbk'
```
<a id="if">if</a>

```mysql
mysql> SELECT IF(1 > 0,'正确','错误')
　　-> '正确'
```
<a id="ifnull">ifnull</a>

```mysql
mysql> SELECT IFNULL(null,'Hello Word')
　　-> 'Hello Word'
```
<a id="isnull">isnull</a>
```mysql
mysql> SELECT ISNULL(NULL);
　　-> 1
```
<a id="nullif">nullif</a>

```mysql
mysql> SELECT NULLIF(25, 25);
　　-> 
```
<a id="CASE ">CASE </a>

```mysql
mysql> SELECT CASE  WHEN 1 > 0　THEN '1 > 0' WHEN 2 > 0　THEN '2 > 0' ELSE '3 > 0' END;
　　-> '1 > 0'
```
