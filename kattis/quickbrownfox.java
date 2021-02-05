import java.util.*;

public class quickbrownfox_260889983 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int num_args = scan.nextInt();
        scan.nextLine();
        String[] line;

        for (int i = 0; i < num_args; i++){

            line = scan.nextLine().toLowerCase().split("");

            List<String> noDuplicates = new ArrayList<String>(50);
            for (String s : line){
                if (!noDuplicates.contains(s) && (int)s.charAt(0) <= 123 && (int)s.charAt(0) >= 97){
                    noDuplicates.add(s);
                }
            }

            if(noDuplicates.size() != 26 && noDuplicates.size() > 0){ //not pangram, find missing chars
                Collections.sort(noDuplicates); //sort alphabetically

                StringBuilder out = new StringBuilder();
                for (int j = 97; j <= 122; j++){ //ascii indexes for a-z
                    if(!noDuplicates.contains(String.valueOf((char)(j)))) {
                        out.append((char)(j));
                    }
                }
                System.out.println("missing " + out.toString());
            }else{ //is pangram
                System.out.println("pangram");
            }
        }
        scan.close();
    }
}
