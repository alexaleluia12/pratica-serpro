package serpro;

import java.util.LinkedList;
import java.util.Queue;
import static java.lang.System.out;

public class Fila {
    public static void run() {
        Queue lst = new LinkedList<Integer>();
        lst.add(3);
        lst.add(6);
        lst.add(68);

        out.println(lst);


        out.println(lst.poll());
        out.println(lst);
        out.println(lst.poll());
        out.println(lst.poll());
        out.println(lst);
        out.println(lst.poll()); // poll() -> null qnd a fila esta vazia
    }
}