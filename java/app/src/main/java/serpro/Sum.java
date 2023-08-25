package serpro;

public class Sum {
    /**
     * @return int soma de a e b se nehum deles for zero, caso contrario 1
     *
     * Exemplo: op(1, 4) -> 5; op(7, 0) -> 1
     */
    public int op(int a, int b) {
        if (a == 0 || b == 0)
            return 1;
        return a + b;
    }
}