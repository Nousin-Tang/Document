# Mysql 函数

[参照](https://www.cnblogs.com/xuyulin/p/5468102.html)

## 字符串函数

[示例](#ASCII)

### 总览

| 函数                  | 描述                                                         | 示例          |
| --------------------- | ------------------------------------------------------------ | ------------- |
| ascii(s)       | 返回字符串 s 的第一个字符的 ASCII 码                         | [示例](#ascii) |
| conv(n,from_base,to_base) | 对数字n进制转换,并转换为字串返回（任何参数为null时返回null，进制范围为2-36进制，<br>当to_base是负数时n作为有符号数否则作无符号数，conv以64位点精度工作） | [示例](#conv) |
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
| substring_index(str,d,count) | 返回从字符串str的第count个出现的分隔符d之前的子串(count为正数时从左开始,否则从右开始) | [示例](#substring_index) |
| ltrim(str)，rtrim(str) | 返回删除了左/右空格的字符串str | [示例](#ltrim) |
| trim([\[both\|leading\|trailing\] [remstr] from] str) | 返回前缀或后缀remstr被删除了的字符串str(位置参数默认both,remstr默认值为空格) | [示例](#ltrim) |
| space(n) | 返回由n个空格字符组成的一个字符串 | [示例](#space) |
| replace(str,from_str,to_str) | 用字符串to_str替换字符串str中的子串from_str并返回 | [示例](#replace) |
| repeat(str,count) | 返回由count个字符串str连成的一个字符串<br/>(任何参数为null时返回null,count<=0时返回一个空字符串) | [示例](#repeat) |
| reverse(str) | 颠倒字符串str的字符顺序并返回 | [示例](#) |
| insert(str,pos,len,newstr) | 把字符串str由位置pos起len个字符长的子串替换为字符串newstr并返回 | [示例](#) |
| elt(n,str1,str2,str3,...) | field(str,str1,str2,str3,...) | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |
|                       |                                                              | [示例](#) |

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















## 数字函数

### 总览

### 示例


## 日期函数

### 总览

### 示例

## 高级函数

### 总览

### 示例
