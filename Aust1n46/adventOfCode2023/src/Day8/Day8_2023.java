package Day8;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Node {
	final String value;
	final String left;
	final String right;

	Node(final String value, final String left, final String right) {
		this.value = value;
		this.left = left;
		this.right = right;
	}

	@Override
	public String toString() {
		return value + "," + left + "," + right;
	}
}

public class Day8_2023 {
	public static void main(String[] args) throws IOException {
		final List<String> input = Files.readAllLines(Path.of("src/Day8/input.txt"));
		System.out.println(getTotalPartOne(input));
		System.out.println(getTotalPartTwo(input));
	}

	private static int getTotalPartOne(final List<String> input) {
		final String instructions = input.get(0);
		final Map<String, Node> nodes = new HashMap<>();
		for (int i = 2; i < input.size(); i++) {
			final String line = input.get(i);
			final String value = line.substring(0, 3);
			final String left = line.substring(7, 10);
			final String right = line.substring(12, line.length() - 1);
			nodes.put(value, new Node(value, left, right));
		}
		Node curNode = nodes.get("AAA");
		int cursor = 0;
		int count = 1;
		while (true) {
			final char instruction = instructions.charAt(cursor);
			final String next;
			if (instruction == 'R') {
				next = curNode.right;
			} else {
				next = curNode.left;
			}
			if (next.equals("ZZZ")) {
				return count;
			}
			curNode = nodes.get(next);
			count++;
			cursor++;
			if (cursor >= instructions.length()) {
				cursor = 0;
			}
		}
	}

	private static long getTotalPartTwo(final List<String> input) {
		final String instructions = input.get(0);
		final Map<String, Node> nodes = new HashMap<>();
		for (int i = 2; i < input.size(); i++) {
			final String line = input.get(i);
			final String value = line.substring(0, 3);
			final String left = line.substring(7, 10);
			final String right = line.substring(12, line.length() - 1);
			nodes.put(value, new Node(value, left, right));
		}
		int cursor = 0;
		int count = 0;
		final List<Node> concurrentPaths = new ArrayList<>();
		nodes.entrySet().stream().filter(x -> x.getKey().charAt(2) == 'A')
				.forEach(x -> concurrentPaths.add(x.getValue()));
		final List<Integer> loopLengths = new ArrayList<>();
		while (true) {
			if (loopLengths.size() == concurrentPaths.size()) {
				long lcm = lcm(loopLengths.get(0), loopLengths.get(1));
				for (int i = 2; i < loopLengths.size(); i++) {
					lcm = lcm(lcm, loopLengths.get(i));
				}
				return lcm;
			}
			final char instruction = instructions.charAt(cursor);
			for (int i = 0; i < concurrentPaths.size(); i++) {
				final Node curNode = concurrentPaths.get(i);
				final String next;
				if (instruction == 'R') {
					next = curNode.right;
				} else {
					next = curNode.left;
				}
				if (next.charAt(2) == 'Z') {
					loopLengths.add(count + 1);
				}
				concurrentPaths.set(i, nodes.get(next));
			}
			count++;
			cursor++;
			if (cursor >= instructions.length()) {
				cursor = 0;
			}
		}
	}

	private static long gcd(final long a, final long b) {
		if (a == 0) {
			return b;
		}
		return gcd(b % a, a);
	}

	private static long lcm(final long a, final long b) {
		return (a / gcd(a, b)) * b;
	}
}
