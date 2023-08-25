package serpro;

import java.sql.*;

public class DBConnection {
    public static void run() {

        // registro driver
        /*
        final String JDBC_DRIVER = "com.oracle.database.jdbc.OracleDriver";
        try {
            Class.forName(JDBC_DRIVER);
            //com.oracle.database.jdbc
        } catch(ClassNotFoundException e) {
            e.printStackTrace();
            System.out.println("Fim sem conecatar ao baco ");
            return;
        } */

        String connectionURI = "jdbc:oracle:thin:@localhost:1521/serpro_db";
        String user = "serpro";
        String password = "test123";
        try (Connection conn = DriverManager.getConnection(connectionURI, user, password)) {

            if (conn != null) {
                System.out.println("Connected to the database!");
            } else {
                System.out.println("Failed to make connection!");
            }

        } catch (SQLException e) {
            System.err.format("SQL State: %s\n%s", e.getSQLState(), e.getMessage());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}



