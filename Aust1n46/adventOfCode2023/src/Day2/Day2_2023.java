package Day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Day2_2023 {
	private static final File INPUT = new File("src/Day2/input.txt");
	private static final Map<String, Integer> COLORS = Map.of("red", 12, "green", 13, "blue", 14);

	public static void main(String[] args) {
		System.out.println(getSumPartOne());
		System.out.println(getSumPartTwo());
	}

	private static int getSumPartOne() {
		int sum = 0;
		try (final Scanner scanner = new Scanner(INPUT)) {
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				final String id = line.substring(5, line.indexOf(":"));
				line = line.substring(7 + id.length());
				boolean isPossible = true;
				outerLoop:
				for (final String subset : List.of(line.split(";"))) {
					for (String colorSet : List.of(subset.trim().split(","))) {
						colorSet = colorSet.trim();
						String value = colorSet.substring(0, colorSet.indexOf(" "));
						String color = colorSet.substring(1 + value.length());
						if (Integer.parseInt(value) > COLORS.get(color)) {
							isPossible = false;
							break outerLoop;
						}
					}
				}
				if (isPossible) {
					sum += Integer.parseInt(id);
				}
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return sum;
	}

	private static int getSumPartTwo() {
		int sum = 0;
		try (final Scanner scanner = new Scanner(INPUT)) {
			while (scanner.hasNextLine()) {
				final Map<String, Integer> maxColors = new HashMap<>(Map.of("red", 1, "green", 1, "blue", 1));
				String line = scanner.nextLine();
				final String id = line.substring(5, line.indexOf(":"));
				line = line.substring(7 + id.length());
				for (final String subset : List.of(line.split(";"))) {
					for (String colorSet : List.of(subset.trim().split(","))) {
						colorSet = colorSet.trim();
						final String value = colorSet.substring(0, colorSet.indexOf(" "));
						final String color = colorSet.substring(1 + value.length());
						maxColors.put(color, Math.max(maxColors.get(color), Integer.parseInt(value)));
					}
				}
				sum += maxColors.values().stream().mapToInt(Integer::intValue).reduce(1, Math::multiplyExact);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return sum;
	}
}
