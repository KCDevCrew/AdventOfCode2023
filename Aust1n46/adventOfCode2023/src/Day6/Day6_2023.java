package Day6;

import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;
import java.util.List;
import java.util.Scanner;

public class Day6_2023 {
	public static void main(String[] args) {
		System.out.println(getTotalPartOne());
		System.out.println(getTotalPartTwo());
		System.out.println(getTotalPartTwoProper());
	}

	private static int getTotalPartOne() {
		int total = 1;
		try (final Scanner scanner = new Scanner(new File("src/Day6/input.txt"))) {
			final List<String> times = List.of(scanner.nextLine().substring(5).trim().split("\\s+"));
			final List<String> distances = List.of(scanner.nextLine().substring(10).trim().split("\\s+"));
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
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return total;
	}

	private static long getTotalPartTwo() {
		long total = 1;
		try (final Scanner scanner = new Scanner(new File("src/Day6/input2.txt"))) {
			final long time = scanner.nextLong();
			final long distance = scanner.nextLong();
			int beatCount = 0;
			for (long j = 0; j < time; j++) {
				final long distanceTravelled = (time - j) * j;
				if (distanceTravelled > distance) {
					beatCount++;
				}
			}
			total = beatCount;
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return total;
	}

	private static String getTotalPartTwoProper() {
		String total = "";
		try (final Scanner scanner = new Scanner(new File("src/Day6/input2.txt"))) {
			final BigDecimal time = new BigDecimal(scanner.nextLong());
			final BigDecimal distance = new BigDecimal(scanner.nextLong());
			// sqrt(b^2 - 4ac)
			final BigDecimal determinant = time.pow(2).subtract(new BigDecimal(4).multiply(distance)).sqrt(MathContext.DECIMAL128);

			// (b + sqrt(b^2 - 4ac)) / 2
			final BigDecimal rightRoot = time.add(determinant).divide(new BigDecimal(2)).setScale(0, RoundingMode.FLOOR);

			// (b - sqrt(b^2 - 4ac)) / 2
			final BigDecimal leftRoot = time.subtract(determinant).divide(new BigDecimal(2)).setScale(0,
					RoundingMode.CEILING);

			// right - left + 1 to make range total inclusive
			total = rightRoot.subtract(leftRoot).add(BigDecimal.ONE).toString();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return total;
	}
}
