package serpro;


import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotSame;

import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class SumTest
{
    Sum s;

    @Test
    public void testNormalFlow()
    {
        s = new Sum();
        assertEquals(6, s.op(1,5));
        assertEquals(6, s.op(5,1));

    }

    @Test
    public void testEdgeCase()
    {
        s = new Sum();
        assertEquals(1, s.op(0, 2));
        assertEquals(1, s.op(2, 0));
    }
}
