import java.util.*;

public class oddities_260889983 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        for (int ct = sc.nextInt(); ct > 0; ct--) {
            int num = sc.nextInt();
            if (num % 2 == 0) {
                System.out.println(num + " is even");
            } else {
                System.out.println(num + " is odd");
            }
        }
        sc.close();
    }
}
