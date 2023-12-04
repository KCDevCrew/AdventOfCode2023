package Day4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day4_2023 {
	private static final File INPUT = new File("src/Day4/input.txt");

	public static void main(String[] args) {
		System.out.println(getSumPartOne());
		System.out.println(getSumPartTwo());
	}

	private static int getSumPartOne() {
		int sum = 0;
		try (final Scanner scanner = new Scanner(INPUT)) {
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				line = line.substring(line.indexOf(":") + 1).trim();
				final String winningNumbersString = line.substring(0, line.indexOf("|")).trim();
				final String ourNumbersString = line.substring(line.indexOf("|") + 1, line.length()).trim();
				final Set<String> winningNumbers = Stream.of(winningNumbersString.split("\\s+"))
						.collect(Collectors.toSet());
				final Set<String> ourNumbers = Stream.of(ourNumbersString.split("\\s+"))
						.collect(Collectors.toSet());
				sum += (int) Math.pow(2, ourNumbers.stream().filter(x -> winningNumbers.contains(x)).count() - 1);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return sum;
	}
	
	private static int getSumPartTwo() {
		final Map<Integer, Integer> cards = new HashMap<>();
		try (final Scanner scanner = new Scanner(INPUT)) {
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				final int cardNumber = Integer.parseInt(line.substring(5, line.indexOf(":")).trim());
				cards.putIfAbsent(cardNumber, 1);
				line = line.substring(line.indexOf(":") + 1).trim();
				final String winningNumbersString = line.substring(0, line.indexOf("|")).trim();
				final String ourNumbersString = line.substring(line.indexOf("|") + 1, line.length()).trim();
				final Set<String> winningNumbers = Stream.of(winningNumbersString.split("\\s+"))
						.collect(Collectors.toSet());
				final Set<String> ourNumbers = Stream.of(ourNumbersString.split("\\s+"))
						.collect(Collectors.toSet());
				final int numMatches = (int) ourNumbers.stream().filter(x -> winningNumbers.contains(x)).count();
				IntStream.range(cardNumber + 1, cardNumber + numMatches + 1).forEach(x -> cards.put(x, cards.getOrDefault(x, 1) + cards.get(cardNumber)));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return cards.values().stream().mapToInt(Integer::intValue).sum();
	}
}
