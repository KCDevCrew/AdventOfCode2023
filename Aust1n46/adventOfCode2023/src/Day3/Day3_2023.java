package Day3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Day3_2023 {
	private static final File INPUT = new File("src/Day3/input.txt");
	private static final Set<Character> SYMBOLS = Set.of('*', '#', '$', '+', '@', '%', '=', '/', '-', '&');
	private static final int[] NEIGHBORS = new int[] {0, -1, 0, 1, 1, -1, -1, 1, 0};

	public static void main(String[] args) {
		System.out.println(getSumPartOne());
		System.out.println(getSumPartTwo());
	}

	private static int getSumPartOne() {
		int gridSize = 140;
		int sum = 0;
		char[][] grid = new char[gridSize][gridSize];
		int row = 0;
		try (final Scanner scanner = new Scanner(INPUT)) {
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				for (int i = 0; i < line.length(); i++) {
					grid[row][i] = line.charAt(i);
				}
				row++;
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
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
					if (j == gridSize - 1 && !num.isEmpty() && hasSymbol) {
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

	private static int getSumPartTwo() {
		int gridSize = 140;
		int sum = 0;
		char[][] grid = new char[gridSize][gridSize];
		int row = 0;
		try (final Scanner scanner = new Scanner(INPUT)) {
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				for (int i = 0; i < line.length(); i++) {
					grid[row][i] = line.charAt(i);
				}
				row++;
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
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
					if (j == gridSize - 1 && !num.isEmpty() && hasSymbol) { // end of the row
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
