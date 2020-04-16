###将代码粘贴到 Preferences | Editor | Live Templates 下的分组中，选中分组然后粘贴；
```html
<template name="***" value="/**&#10; * $end$&#10; *&#10; * @author tangwc&#10; * @since $DATE$&#10; */" shortcut="ENTER" description="类注释" toReformat="false" toShortenFQNames="true">
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="DATE" expression="date()" defaultValue="" alwaysStopAt="false" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="ctl" value="collect(Collectors.toList());" description="自动补全java8生成List语法" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="ctm" value="collect(Collectors.toMap($end$, e -&gt; e, (k1, k2) -&gt; k1));" description="自动补全java8生成Map语法" toReformat="false" toShortenFQNames="true">
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="getMethod" value="/**&#10; * TODO&#10; * &#10; * @param param&#10; * @return&#10; */&#10;@RequestMapping(value=&quot;$requestPath$&quot;, method = RequestMethod.GET)&#10;public Object $requestPath$(@RequestParam String param){&#10;    Map&lt;String, Object&gt; resultMap = new HashMap&lt;&gt;();&#10;    $end$&#10;    return resultMap;&#10;}" description="自动生成Get请求方法" toReformat="false" toShortenFQNames="true">
  <variable name="requestPath" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="pb" value="private BigDecimal $name$; // $describtion$" description="私有BigDecimal类型成员变量" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="describtion" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="pd" value="private Date $name$; // $describtion$" description="私有Date类型成员变量" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="describtion" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="pi" value="private Integer $name$; // $describtion$" description="私有Integer类型成员变量" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="describtion" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="postMethod" value="/**&#10; * TODO&#10; *&#10; * @param requestDto&#10; * @return&#10; */&#10;@RequestMapping(value=&quot;$requestPath$&quot;, method = RequestMethod.POST)&#10;public Object $requestPath$(@RequestBody Object requestDto){&#10;    Map&lt;String, Object&gt; resultMap = new HashMap&lt;&gt;();&#10;    $end$&#10;    return resultMap;&#10;}" description="自动生成Post请求方法" toReformat="false" toShortenFQNames="true">
  <variable name="requestPath" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="ps" value="private String $name$; // $describtion$" description="私有String类型成员变量" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="describtion" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
```