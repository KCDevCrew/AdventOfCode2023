package Day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Day1_2023 {
	private static final File INPUT = new File("src/Day1/input.txt");
	private static final Map<String, String> DIGITS = Map.of("one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9");

	public static void main(String[] args) {
		System.out.println(getCalibrationValuesPartOne());
		System.out.println(getCalibrationValuesPartTwo());
	}

	private static int getCalibrationValuesPartOne() {
		int sum = 0;
		try (Scanner scanner = new Scanner(INPUT)) {
			while (scanner.hasNextLine()) {
				final String line = scanner.nextLine();
				String firstDigit = "";
				String lastDigit = "";
				for (char c : line.toCharArray()) {
					if (c > 57) { // not a number
						continue;
					}
					if (firstDigit.isEmpty()) {
						firstDigit = String.valueOf(c);
					} else {
						lastDigit = String.valueOf(c);
					}
				}
				if (lastDigit.isEmpty()) {
					lastDigit = firstDigit;
				}
				sum += Integer.parseInt(firstDigit + lastDigit);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return sum;
	}

	private static int getCalibrationValuesPartTwo() {
		int sum = 0;
		try (Scanner scanner = new Scanner(INPUT)) {
			while (scanner.hasNextLine()) {
				final String line = scanner.nextLine();
				String firstDigit = "";
				String lastDigit = "";
				String word = "";
				for (char c : line.toCharArray()) {
					word += String.valueOf(c);
					if (word.length() > 5) {
						word = word.substring(1);
					}
					if (c > 57) { // not a number
						if (word.length() < 3) {
							continue;
						}
						for (String s : getWordOptions(word)) {
							if (DIGITS.containsKey(s)) {
								if (firstDigit.isEmpty()) {
									firstDigit = DIGITS.get(s);
								} else {
									lastDigit = DIGITS.get(s);
								}
							}
						}
					} else {
						word = "";
						if (firstDigit.isEmpty()) {
							firstDigit = String.valueOf(c);
						} else {
							lastDigit = String.valueOf(c);
						}
					}
				}
				if (lastDigit.isEmpty()) {
					lastDigit = firstDigit;
				}
				sum += Integer.parseInt(firstDigit + lastDigit);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return sum;
	}

	private static List<String> getWordOptions(final String word) {
		if (word.length() == 3) {
			return List.of(word);
		}
		if (word.length() == 4) {
			return List.of(word, word.substring(0, 3), word.substring(1));
		}
		return List.of(word, word.substring(0, 4), word.substring(0, 3), word.substring(1), word.substring(2), word.substring(1, 4));
	}
}
