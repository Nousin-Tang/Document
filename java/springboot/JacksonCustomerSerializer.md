# Spring Boot Jackson 自定义序列化

```java
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.apache.commons.text.StringEscapeUtils;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.jackson.JsonComponent;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@SpringBootApplication
@RestController
public class SerializerApplication {

    public static void main(String[] args) {
        SpringApplication.run(SerializerApplication.class, args);
    }

    @GetMapping("/get")
    public ResultDto get(){
        return new ResultDto("code_&quot;1", "message_&quot;1", new Currency("sdww&quot;dd"));
    }

    @Data
    @AllArgsConstructor
    @NoArgsConstructor
    public static class ResultDto {
        private String code; // code
        private String message; // message
        private Currency currency; // message
    }

    @Data
    @AllArgsConstructor
    @NoArgsConstructor
    public static class Currency {
        private String country; // 国家
        private String identifier; // 标识符
        public Currency(String identifier){
            this.identifier = identifier;
        }
    }

    /**
     * @JsonComponent 之后就不需要手动将Jackson的序列化和反序列化手动加入ObjectMapper了.
     * (如果此类放在其他地方，需要被扫描到。实在没效果可以放在启动类下实施效果)
     */
    @JsonComponent
    public static class JacksonComponent {
        /**
         * TempDto 自定义序列化
         */
        public static class TempDtoJsonSerializer extends JsonSerializer<Currency> {
            @Override
            public void serialize(Currency dto, JsonGenerator jsonGenerator, SerializerProvider serializerProvider) throws IOException {
                String msg = StringEscapeUtils.unescapeHtml4(dto.getIdentifier());
                jsonGenerator.writeString(msg);
            }
        }

        /**
         * 序列化所有 String 字段的数据，如：code
         */
        public static class JsonStringSerializer extends JsonSerializer<String> {
            @Override
            public void serialize(String dto, JsonGenerator jsonGenerator, SerializerProvider serializerProvider) throws IOException {
                String msg = StringEscapeUtils.unescapeHtml4(dto);
                jsonGenerator.writeString(msg);
            
            }
        }
    }
}
```
调用接口返回值
```json
{
  "code": "code_\"1",
  "message": "message_\"1",
  "currency": "sdww\"dd"
}
```

