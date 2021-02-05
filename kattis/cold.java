import java.util.Scanner;

public class cold_260889983 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int num_args = scan.nextInt();
        int temp;
        int count = 0;

        for (int i = 0; i < num_args; i++){
            temp = scan.nextInt();
            if (temp < 0){
                count++;
            }
        }
        System.out.println(count);
        scan.close();
    }
}
