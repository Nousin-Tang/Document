package com.example.demo;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

/**
 * 数据库 dump 文件，insert 语句改成批量形式
 * 使用方式，将dump出来的SQL重命名为：dump.sql，并放在工程目录下。代码会自动获取该SQL执行。
 * （打包成jar后将文件放在jar同级目录下）
 *
 * <p>
 *     insert 记录开始结束要有 begin、commit 标识
 * </p>
 *
 * @author tangwc
 * @since 2021/7/2
 */
public class BatchOperation {

    public static final String insert_pre = "INSERT INTO"; //
    public static final String insert_val = "VALUES"; //
    public static final String sp = ");"; //
    public static final String sp_1 = "),"; //
    public static final String COMMIT = "COMMIT;"; //
    public static final String BEGIN = "BEGIN;"; //
    public static final String NEW_LINE = "\n";//
    public static final Integer MAX_LENGTH = 1<<13;//
    public static int i = 0;

    public static String CURRENT_TABLE = ""; //
    public static boolean IS_INSERT = false;
    private static final Map<String, Boolean> tableNameMap = new HashMap<>();

//    public static void main(String[] args) {
//        deal();
//    }

    public static void deal() {
        final String userDir = System.getProperty("user.dir");
        System.out.println(userDir);
        final File file = new File(userDir + "/dump.sql");
        if (!file.exists()) {
            System.out.println(file.getAbsoluteFile() + " 文件不存在");
            return;
        }
        dealSqlFile(userDir, file);
    }


    public static void dealSqlFile(String userDir, File file) {
        // 只允许读取相对目录文件
        String targetSql = userDir + "/dump_new.sql";
        // 不存在或者不是文件返回null
        if (!file.exists() || !file.isFile()) {
            return;
        }
        System.out.println("开始处理文件。。。" + LocalDateTime.now());
        try (BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(file), StandardCharsets.UTF_8));
             final OutputStreamWriter out = new OutputStreamWriter(new FileOutputStream(targetSql), StandardCharsets.UTF_8)) {
            String data = null;
            final StringBuilder sqlTemp = new StringBuilder();

            boolean start = false;
            boolean end = false;
            while ((data = br.readLine()) != null) {

                final String dealSql = dealSql(data);
                if (dealSql.equalsIgnoreCase(BEGIN)) {
                    start = true;
                }
                if (dealSql.equalsIgnoreCase(COMMIT)) {
                    end = true;
                }
                if (start) {
                    start = false;
                    sqlTemp.append(dealSql).append(NEW_LINE);
                    // 写文件，清空缓存
                    writeData(out, sqlTemp.toString());
                    clear(sqlTemp);
                    continue;
                }
                if (end) {
                    end = false;
                    if (sqlTemp.length() > 0) {
                        String s = sqlTemp.toString();
                        if (s.endsWith(sp_1 + NEW_LINE)) {
                            s = s.substring(0, s.length() - sp_1.length() - NEW_LINE.length()) + sp + NEW_LINE;
                        }
                        writeData(out, s);
                    }
                    writeData(out, COMMIT + NEW_LINE);
                    clear(sqlTemp);
                    continue;
                }
                sqlTemp.append(dealSql).append(NEW_LINE);
                if (IS_INSERT && i >= MAX_LENGTH) {
                    String s = sqlTemp.toString();
                    if (s.endsWith(sp_1 +  NEW_LINE)) {
                        s = s.substring(0, s.length() - sp_1.length() - NEW_LINE.length()) + sp + COMMIT + BEGIN + NEW_LINE;
                    }
                    writeData(out, s);
                    clear(sqlTemp);
                    CURRENT_TABLE = "";
                    i = 0;
                }
                if (IS_INSERT)
                    i++;
            }
            if (sqlTemp.length() >= 0) {
                writeData(out, sqlTemp.toString());
                clear(sqlTemp);
            }

        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("读取失败");
        }
        System.out.println("处理成功，时间" + LocalDateTime.now());
    }

    private static void writeData(OutputStreamWriter out, String sql) {
        try {
            out.write(sql);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void clear(StringBuilder sql) {
        sql.delete(0, sql.length());
    }

    private static String dealSql(String data) {
        IS_INSERT = false;
        if (!data.startsWith(insert_pre)) {
            return data;
        }
        if (!data.contains(insert_val)) {
            return data;
        }
        final String[] split = data.split(insert_val);
        if (split.length == 2) {
            IS_INSERT = true;
            String tableVal = split[0];
            String values = split[1];
            if (values.endsWith(sp)) {
                values = values.substring(0, values.length() - sp.length()) + sp_1;
            }
            final String tableName = tableVal.substring(insert_pre.length()).trim();
            if (!CURRENT_TABLE.equals("") && tableNameMap.containsKey(tableName)) {
                return values;
            } else {
                if (!tableNameMap.containsKey(tableName)) {
                    System.out.println("正在处理表：" + tableName);
                    tableNameMap.put(tableName, false);
                    i = 0;
                }
                CURRENT_TABLE = tableName;
                return tableVal + insert_val + values;
            }
        }
        return data;
    }
}
