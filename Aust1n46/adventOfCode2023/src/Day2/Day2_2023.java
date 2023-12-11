package Day2;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day2_2023 {
	private static final Map<String, Integer> COLORS = Map.of("red", 12, "green", 13, "blue", 14);

	public static void main(String[] args) throws IOException {
		final List<String> input = Files.readAllLines(Path.of("src/Day2/input.txt"));
		System.out.println(getSumPartOne(input));
		System.out.println(getSumPartTwo(input));
	}

	private static int getSumPartOne(final List<String> input) {
		int sum = 0;
		for (String line : input) {
			final String id = line.substring(5, line.indexOf(":"));
			line = line.substring(7 + id.length());
			boolean isPossible = true;
			outerLoop: for (final String subset : List.of(line.split(";"))) {
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
		return sum;
	}

	private static int getSumPartTwo(final List<String> input) {
		int sum = 0;
		for (String line : input) {
			final Map<String, Integer> maxColors = new HashMap<>(Map.of("red", 1, "green", 1, "blue", 1));
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
		return sum;
	}
}
