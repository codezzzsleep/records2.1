package icu.zzzsleep.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCDemo {
    public static void main(String[] args) throws Exception {
        String url = "jdbc:mysql://127.0.0.1:3306/db1";
        String username = "root";
        String password = "123456";
        Connection con =  DriverManager.getConnection(url, username,password);
        Statement stat = con.createStatement();
        String sql = "update emp set salary = 10000 where name = '张三'";
        int count = stat.executeUpdate(sql);
        System.out.println(count);
    }
}
