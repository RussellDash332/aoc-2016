import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split(", ");
        Set<String> v = new HashSet<String>();

        int[] pos = new int[4];
        int[] its = new int[4];
        int dir = 0;
        boolean found = false;

        for (int i = 0; i < line.length; i++) {
            if (line[i].charAt(0) == 'R') {
                dir = (dir + 1) % 4;
            } else {
                dir = (dir + 3) % 4;
            }
            for (int j = 0; j < Integer.parseInt(line[i].substring(1, line[i].length())); j++) {
                if (!v.contains((pos[0] - pos[2]) + "-" + (pos[1] - pos[3]))) {
                    v.add((pos[0] - pos[2]) + "-" + (pos[1] - pos[3]));
                } else if (!found) {
                    for (int k = 0; k < 4; k++) {
                        its[k] = pos[k];
                    }
                    found = true;
                }
                pos[dir]++;
            }
        }

        System.out.println("Part 1: " + (Math.abs(pos[0] - pos[2]) + Math.abs(pos[1] - pos[3])));
        System.out.println("Part 2: " + (Math.abs(its[0] - its[2]) + Math.abs(its[1] - its[3])));
    }
}