package Day3;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Day3_2023 {
	private static final Set<Character> SYMBOLS = Set.of('*', '#', '$', '+', '@', '%', '=', '/', '-', '&');
	private static final int[] NEIGHBORS = new int[] { 0, -1, 0, 1, 1, -1, -1, 1, 0 };

	public static void main(String[] args) throws IOException {
		final List<String> input = Files.readAllLines(Path.of("src/Day3/input.txt"));
		System.out.println(getSumPartOne(input));
		System.out.println(getSumPartTwo(input));
	}

	private static int getSumPartOne(final List<String> input) {
		int gridSize = 140;
		int sum = 0;
		char[][] grid = new char[gridSize][gridSize];
		int row = 0;
		for (final String line : input) {
			for (int i = 0; i < line.length(); i++) {
				grid[row][i] = line.charAt(i);
			}
			row++;
		}
		for (int i = 0; i < gridSize; i++) {
			String num = "";
			boolean hasSymbol = false;
			for (int j = 0; j < gridSize; j++) {
				char c = grid[i][j];
				if (Character.isDigit(c)) {
					num += c;
					for (int k = 0; k < 8; k++) {
						int nrow = i + NEIGHBORS[k];
						int ncol = j + NEIGHBORS[k + 1];
						if (nrow >= 0 && ncol >= 0 && nrow < grid.length && ncol < grid[0].length) {
							if (SYMBOLS.contains(grid[nrow][ncol])) {
								hasSymbol = true;
								break;
							}
						}
					}
					if (j == gridSize - 1 && hasSymbol) {
						sum += Integer.parseInt(num);
					}
				} else {
					if (!num.isEmpty() && hasSymbol) {
						sum += Integer.parseInt(num);
					}
					hasSymbol = false;
					num = "";
				}
			}
		}
		return sum;
	}

	private static int getSumPartTwo(final List<String> input) {
		int gridSize = 140;
		int sum = 0;
		char[][] grid = new char[gridSize][gridSize];
		int row = 0;
		for (final String line : input) {
			for (int i = 0; i < line.length(); i++) {
				grid[row][i] = line.charAt(i);
			}
			row++;
		}
		Map<String, Integer> nums = new HashMap<>();
		for (int i = 0; i < gridSize; i++) {
			String num = "";
			boolean hasSymbol = false;
			String symbolIndex = "";
			for (int j = 0; j < gridSize; j++) {
				char c = grid[i][j];
				if (Character.isDigit(c)) {
					num += c;
					for (int k = 0; k < 8; k++) {
						int nrow = i + NEIGHBORS[k];
						int ncol = j + NEIGHBORS[k + 1];
						if (nrow >= 0 && ncol >= 0 && nrow < grid.length && ncol < grid[0].length) {
							if (grid[nrow][ncol] == '*') {
								symbolIndex = nrow + "," + ncol;
								hasSymbol = true;
								break;
							}
						}
					}
					if (j == gridSize - 1 && hasSymbol) { // end of the row
						final Integer existingNum = nums.get(symbolIndex);
						final int parsedNum = Integer.parseInt(num);
						if (existingNum != null) {
							sum += existingNum * parsedNum;
						} else {
							nums.put(symbolIndex, parsedNum);
						}
					}
				} else {
					if (!num.isEmpty() && hasSymbol) { // end of new digits
						final Integer existingNum = nums.get(symbolIndex);
						final int parsedNum = Integer.parseInt(num);
						if (existingNum != null) {
							sum += existingNum * parsedNum;
						} else {
							nums.put(symbolIndex, parsedNum);
						}
					}
					symbolIndex = "";
					hasSymbol = false;
					num = "";
				}
			}
		}
		return sum;
	}
}
