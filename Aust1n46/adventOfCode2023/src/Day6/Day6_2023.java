package Day6;

import java.io.IOException;
import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Day6_2023 {
	public static void main(String[] args) throws IOException {
		final List<String> input = Files.readAllLines(Path.of("src/Day6/input.txt"));
		System.out.println(getTotalPartOne(input));
		final List<String> input2 = Files.readAllLines(Path.of("src/Day6/input2.txt"));
		System.out.println(getTotalPartTwo(input2));
		System.out.println(getTotalPartTwoProper(input2));
	}

	private static int getTotalPartOne(final List<String> input) {
		int total = 1;
		final List<String> times = List.of(input.get(0).substring(5).trim().split("\\s+"));
		final List<String> distances = List.of(input.get(1).substring(10).trim().split("\\s+"));
		for (int i = 0; i < times.size(); i++) {
			final int time = Integer.parseInt(times.get(i));
			final int distanceToBeat = Integer.parseInt(distances.get(i));
			int beatCount = 0;
			for (int j = 0; j < time; j++) {
				final int distanceTravelled = (time - j) * j;
				if (distanceTravelled > distanceToBeat) {
					beatCount++;
				}
			}
			total *= beatCount;
		}
		return total;
	}

	// brute force because it's faster than writing the optimal solution...
	private static long getTotalPartTwo(final List<String> input) {
		long total = 1;
		final long time = Long.parseLong(input.get(0));
		final long distance = Long.parseLong(input.get(1));
		int beatCount = 0;
		for (long j = 0; j < time; j++) {
			final long distanceTravelled = (time - j) * j;
			if (distanceTravelled > distance) {
				beatCount++;
			}
		}
		total = beatCount;
		return total;
	}

	// optimal solution O(1)
	private static String getTotalPartTwoProper(final List<String> input) {
		String total = "";
		final BigDecimal time = new BigDecimal(input.get(0));
		final BigDecimal distance = new BigDecimal(input.get(1));
		// sqrt(b^2 - 4ac)
		final BigDecimal determinant = time.pow(2).subtract(new BigDecimal(4).multiply(distance))
				.sqrt(MathContext.DECIMAL128);

		// (b + sqrt(b^2 - 4ac)) / 2
		final BigDecimal rightRoot = time.add(determinant).divide(new BigDecimal(2)).setScale(0, RoundingMode.FLOOR);

		// (b - sqrt(b^2 - 4ac)) / 2
		final BigDecimal leftRoot = time.subtract(determinant).divide(new BigDecimal(2)).setScale(0,
				RoundingMode.CEILING);

		// right - left + 1 to make range total inclusive
		total = rightRoot.subtract(leftRoot).add(BigDecimal.ONE).toString();
		return total;
	}
}
