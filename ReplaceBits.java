/*

Learned:
    1. Java '' for char, "" for string
    2. Bi to Dec: Integer.parseInt("101010101", 2)
       Dec to Bi: Integer.toBinaryString(4)
    3. Default int is 32-bit signed.
        all 1's = -1
*/



public class ReplaceBits{
    public static int updateBits(int n, int m, int i, int j) {
        int max = ~0;
        int left = max - ((1<<j) - 1);
        int right = (1<<i) -1;
        int mask = left | right;
        return (n & mask) | (m << i);
    }

    public static void main(String[] args) {
        int n = Integer.parseInt("10000000000", 2);
        int m = Integer.parseInt("10101", 2);
        int re = updateBits(n, m, 2, 6);
        System.out.println(Integer.toBinaryString(re));
    }
}
