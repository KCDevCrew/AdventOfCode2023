package Day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;

public class Day1_2023 {
	private static final Map<String, String> DIGITS = Map.of("one", "1", "two", "2", "three", "3", "four", "4", "five",
			"5", "six", "6", "seven", "7", "eight", "8", "nine", "9");

	public static void main(String[] args) throws IOException {
		final List<String> input = Files.readAllLines(Path.of("src/Day1/input.txt"));
		System.out.println(getCalibrationValuesPartOne(input));
		System.out.println(getCalibrationValuesPartTwo(input));
	}

	private static int getCalibrationValuesPartOne(final List<String> input) {
		int sum = 0;
		for (final String line : input) {
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
		return sum;
	}

	private static int getCalibrationValuesPartTwo(final List<String> input) {
		int sum = 0;
		for (final String line : input) {
			String firstDigit = "";
			String lastDigit = "";
			String word3 = "";
			String word4 = "";
			String word5 = "";
			for (char c : line.toCharArray()) {
				word3 += c;
				word4 += c;
				word5 += c;
				if (word3.length() > 3) {
					word3 = word3.substring(1);
				}
				if (word4.length() > 4) {
					word4 = word4.substring(1);
				}
				if (word5.length() > 5) {
					word5 = word5.substring(1);
				}
				if (c > 57) { // not a number
					for (final String s : List.of(word3, word4, word5)) {
						if (DIGITS.containsKey(s)) {
							final String digit = DIGITS.get(s);
							if (firstDigit.isEmpty()) {
								firstDigit = digit;
							} else {
								lastDigit = digit;
							}
							break;
						}
					}
				} else {
					word3 = "";
					word4 = "";
					word5 = "";
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
		return sum;
	}
}
