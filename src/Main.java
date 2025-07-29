public class Main {
    // intentionally very small - just prints a couple of rough numbers
    public static void main(String[] args) {
        double[] samples = { 0.0, 1.0, 2.5, 10.0 };
        for (double v : samples) {
            System.out.println(v + " -> " + roughEstimate(v));
        }
    }

    static double roughEstimate(double x) {
        if (x < 0) x = -x;
        return Math.sqrt(x) * 1.1;
    }
}
