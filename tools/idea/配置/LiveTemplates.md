### 将代码粘贴到 Preferences | Editor | Live Templates 下的分组中，选中分组然后粘贴；
```html
<template name="***" value="/**&#10; * $end$&#10; * &#10; * @author tangwc&#10; * @since $date$&#10; */" shortcut="ENTER" description="类注释" toReformat="false" toShortenFQNames="true">
  <variable name="end" expression="" defaultValue="" alwaysStopAt="false" />
  <variable name="date" expression="date()" defaultValue="" alwaysStopAt="false" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="fin" value="public static final String $name$ = &quot;$value$&quot;; // $end$" description="常量类定义" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="value" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="getMethod" value="/**&#10; * TODO&#10; * &#10; * @param param 请求参数&#10; * @return ResultDto&#10; */&#10;@GetMapping(&quot;$requestPath$&quot;)&#10;public ResultDto&lt;Object&gt; $methodName$(@RequestParam String param){&#10;    $end$&#10;    return ResultUtil.success();&#10;}&#10;" description="生成GET请求的方法" toReformat="false" toShortenFQNames="true">
  <variable name="requestPath" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="methodName" expression="" defaultValue="requestPath.replace(&quot;/&quot;,&quot;&quot;)" alwaysStopAt="false" />
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="group" value="collect(Collectors.groupingBy($end$))" description="自动补全java8生成分组语法" toReformat="true" toShortenFQNames="true">
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="gs" value="@Getter&#10;@Setter" description="生成Getter与Setter" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="method" value="public void $method$(String param){&#10;    $end$&#10;}" description="自动生成方法" toReformat="false" toShortenFQNames="true">
  <variable name="method" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="pb" value="private BigDecimal $name$; // $describtion$" description="私有BigDecimal成员" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="describtion" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="pd" value="private Date $name$; // $describtion$" description="私有Date成员" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="describtion" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="pi" value="private Integer $name$; // $describtion$" description="私有Integer成员" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="describtion" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="postMethod" value="/**&#10; * TODO&#10; *&#10; * @param requestDto 请求参数&#10; * @return ResultDto&#10; */&#10;@PostMapping(&quot;$requestPath$&quot;)&#10;public ResultDto&lt;Object&gt; $methodName$(@RequestBody Object requestDto){&#10;    $end$&#10;    return ResultUtil.success();&#10;}&#10;" description="生成Request请求方法" toReformat="false" toShortenFQNames="true">
  <variable name="requestPath" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="methodName" expression="" defaultValue="requestPath.replace(&quot;/&quot;,&quot;&quot;)" alwaysStopAt="false" />
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="ps" value="private String $name$; // $describtion$" description="私有String成员变量" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="describtion" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="step" value="// STEP $val$: $end$" description="步骤" toReformat="false" toShortenFQNames="true">
  <variable name="val" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
    <option name="JAVA_SCRIPT" value="true" />
  </context>
</template>
<template name="tolist" value="collect(Collectors.toList())" description="自动补全java8生成List语法" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
<template name="tomap" value="collect(Collectors.toMap($end$, e -&gt; e, (k1, k2) -&gt; k1))" description="自动补全java8生成Map语法" toReformat="true" toShortenFQNames="true">
  <variable name="end" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
```
