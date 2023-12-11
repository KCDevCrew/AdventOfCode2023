package Day4;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day4_2023 {
	public static void main(String[] args) throws IOException {
		final List<String> input = Files.readAllLines(Path.of("src/Day4/input.txt"));
		System.out.println(getSumPartOne(input));
		System.out.println(getSumPartTwo(input));
	}

	private static int getSumPartOne(final List<String> input) {
		int sum = 0;
		for (final String line : input) {
			final Set<String> winningNumbers = Stream
					.of(line.substring(line.indexOf(":"), line.indexOf("|")).trim().split("\\s+"))
					.collect(Collectors.toSet());
			final Set<String> ourNumbers = Stream
					.of(line.substring(line.indexOf("|") + 1, line.length()).trim().split("\\s+"))
					.collect(Collectors.toSet());
			sum += (int) Math.pow(2, ourNumbers.stream().filter(x -> winningNumbers.contains(x)).count() - 1);
		}
		return sum;
	}

	private static int getSumPartTwo(final List<String> input) {
		final Map<Integer, Integer> cards = new HashMap<>();
		for (final String line : input) {
			final int cardNumber = Integer.parseInt(line.substring(5, line.indexOf(":")).trim());
			cards.putIfAbsent(cardNumber, 1);
			final Set<String> winningNumbers = Stream
					.of(line.substring(line.indexOf(":"), line.indexOf("|")).trim().split("\\s+"))
					.collect(Collectors.toSet());
			final Set<String> ourNumbers = Stream
					.of(line.substring(line.indexOf("|") + 1, line.length()).trim().split("\\s+"))
					.collect(Collectors.toSet());
			final int numMatches = (int) ourNumbers.stream().filter(x -> winningNumbers.contains(x)).count();
			IntStream.range(cardNumber + 1, cardNumber + numMatches + 1)
					.forEach(x -> cards.put(x, cards.getOrDefault(x, 1) + cards.get(cardNumber)));
		}
		return cards.values().stream().mapToInt(Integer::intValue).sum();
	}
}
