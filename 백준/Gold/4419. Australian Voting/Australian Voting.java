import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<String> names = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            names.add(br.readLine().trim());
        }

        List<int[]> votes = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            String[] tokens = line.split(" ");
            int[] vote = new int[tokens.length];
            for (int i = 0; i < tokens.length; i++) {
                vote[i] = Integer.parseInt(tokens[i]) - 1;
            }
            votes.add(vote);
        }

        List<Integer> winners = solve(n, votes);
        for (int winner : winners) {
            System.out.println(names.get(winner));
        }
    }

    public static List<Integer> solve(int numCandidates, List<int[]> votes) {
        int numPeople = votes.size();
        int threshold = numPeople / 2 + 1;

        boolean[] eliminated = new boolean[numCandidates];
        while (true) {
            int[] counts = new int[numCandidates];
            for (int[] vote : votes) {
                for (int candidate : vote) {
                    if (!eliminated[candidate]) {
                        counts[candidate]++;
                        break;
                    }
                }
            }

            int minCount = Integer.MAX_VALUE;
            int maxCount = Integer.MIN_VALUE;
            for (int count : counts) {
                if (count > 0) {
                    minCount = Math.min(minCount, count);
                    maxCount = Math.max(maxCount, count);
                }
            }

            if (maxCount >= threshold) {
                List<Integer> winners = new ArrayList<>();
                for (int i = 0; i < counts.length; i++) {
                    if (counts[i] == maxCount) {
                        winners.add(i);
                    }
                }
                return winners;
            }

            if (minCount == maxCount) {
                List<Integer> winners = new ArrayList<>();
                for (int i = 0; i < counts.length; i++) {
                    if (counts[i] > 0) {
                        winners.add(i);
                    }
                }
                return winners;
            }

            for (int i = 0; i < counts.length; i++) {
                if (counts[i] == minCount) {
                    eliminated[i] = true;
                }
            }
        }
    }
}