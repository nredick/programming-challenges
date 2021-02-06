import java.util.Scanner;

public class Narrowartgallery_260889983 {
    static final int INFINITY = 10000; // an infinity val that works in the scope of this problem
    static int[][] art_gallery; // matrix to store the art gallery
    static Integer[][][] func; // 3d arr to store subsolutions to the problem

    public static int optimal_min(int k, int r) {
        // return the min of the left and right side subsolutions
        return Math.min(sub_min(k, r, 0), sub_min(k, r, 1));
    }

    public static int sub_min(int k, int r, int c) {
        if (k == 0) return 0; // reached number of rooms to close
        if (r < 0) return INFINITY;

        // return the val of this subproblem if it's already been calculated
        if (func[k][r][c] != null) return func[k][r][c];

        // return best val from from calculated partial problems
        return func[k][r][c] = Math.min(sub_min(k - 1, r - 1, c) + art_gallery[r][c],
                        optimal_min(k, r - 1));
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while (true) {
            // get inputs
            int rows = scan.nextInt();
            int rooms_to_close = scan.nextInt();

            if (rows == 0 && rooms_to_close == 0) break; // end of input

            art_gallery = new int[rows][2];
            func = new Integer[rooms_to_close + 1][rows][2];

            // fill the gallery and compute the total value of the gallery
            int sum = 0;
            for (int i = 0; i < rows; i++) {
                int index = rows - i - 1;
                art_gallery[index][0] = scan.nextInt(); // left side of gallery = 0
                art_gallery[index][1] = scan.nextInt(); // right side of gallery = 1
                sum += art_gallery[index][0] + art_gallery[index][1];
            }
            // call & return the funcs for calculating the solution
            System.out.println(sum - optimal_min(rooms_to_close, rows - 1));
        }
    }
}

