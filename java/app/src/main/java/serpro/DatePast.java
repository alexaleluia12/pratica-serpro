package serpro;

import java.time.*;
import java.time.format.DateTimeFormatter;

public class DatePast {
    public static void go() {
        LocalDate hoje = LocalDate.now();
        LocalDate tresDiasAtras = hoje.minusDays(3);
        DateTimeFormatter formatoBR = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.println(tresDiasAtras.format(formatoBR));
    }

    public static void run() {
        DatePast.go();
    }
}