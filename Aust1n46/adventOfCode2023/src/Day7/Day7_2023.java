package Day7;

import static java.util.stream.IntStream.range;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Scanner;

class Hand implements Comparable<Hand> {
	final String cards;
	final int bid;
	final boolean isJokerHand;
	final Map<Character, Integer> cardCounts = new HashMap<>();
	int tier = 1;

	Hand(final String cards, final int bid, final boolean isJokerHand) {
		this.cards = cards;
		this.bid = bid;
		this.isJokerHand = isJokerHand;
		for (char c : cards.toCharArray()) {
			cardCounts.put(c, cardCounts.getOrDefault(c, 0) + 1);
		}

		if (isJokerHand) {
			final int numJokers = Objects.requireNonNullElse(cardCounts.remove('J'), 0);
			if (numJokers == 5) {
				tier = 7;
				return;
			}
			final var maxCardCount = cardCounts.entrySet().stream().max(Comparator.comparing(Map.Entry::getValue)).get();
			cardCounts.put(maxCardCount.getKey(), maxCardCount.getValue() + numJokers);
		}

		boolean hasThreeOfKind = false;
		boolean hasPair = false;
		for (int v : cardCounts.values()) {
			if (v == 5) {
				tier = 7;
				return;
			} else if (v == 4) {
				tier = 6;
				return;
			} else if (v == 3) {
				hasThreeOfKind = true;
			} else if (v == 2) {
				if (hasPair) {
					tier = 3;
					return;
				}
				hasPair = true;
			}
		}
		if (hasThreeOfKind) {
			if (hasPair) {
				tier = 5;
			} else {
				tier = 4;
			}
		} else if (hasPair) {
			tier = 2;
		}
	}

	@Override
	public String toString() {
		return cards + "," + bid + "," + isJokerHand;
	}

	@Override
	public int compareTo(final Hand other) {
		if (other.tier == this.tier) {
			for (int i = 0; i < 5; i++) {
				final int thisCardValue = getCardValue(this.cards.charAt(i), isJokerHand);
				final int otherCardValue = getCardValue(other.cards.charAt(i), isJokerHand);
				if (otherCardValue == thisCardValue) {
					continue;
				}
				if (otherCardValue > thisCardValue) {
					return -1;
				} else {
					return 1;
				}
			}
		} else {
			if (other.tier > this.tier) {
				return -1;
			} else {
				return 1;
			}
		}
		return 0;
	}

	static int getCardValue(final char card, final boolean isJokerHand) {
		switch (card) {
		case 'A':
			return 14;
		case 'K':
			return 13;
		case 'Q':
			return 12;
		case 'J':
			return isJokerHand ? 1 : 11;
		case 'T':
			return 10;
		default:
			return Integer.parseInt(String.valueOf(card));
		}
	}
}

public class Day7_2023 {
	public static void main(String[] args) {
		System.out.println(getTotalPart(false));
		System.out.println(getTotalPart(true));
	}

	private static int getTotalPart(final boolean isJokerHand) {
		final List<Hand> hands = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day7/input.txt"))) {
			while (scanner.hasNextLine()) {
				final String line = scanner.nextLine();
				hands.add(new Hand(line.substring(0, 5), Integer.parseInt(line.substring(6)), isJokerHand));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		Collections.sort(hands);
		return range(0, hands.size()).reduce(0, (t, x) -> t + (hands.get(x).bid * (x + 1)));
	}
}
