package Day7;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.IntStream;

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
			final var maxCardCount = cardCounts.entrySet().stream().max(Comparator.comparing(Map.Entry::getValue))
					.get();
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
				return otherCardValue > thisCardValue ? -1 : 1;
			}
		} else {
			return other.tier > this.tier ? -1 : 1;
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
	public static void main(String[] args) throws IOException {
		System.out.println(getTotalPart(false));
		System.out.println(getTotalPart(true));
	}

	private static int getTotalPart(final boolean isJokerHand) throws IOException {
		final List<Hand> hands = new ArrayList<>();
		Files.lines(Path.of("src/Day7/input.txt"))
				.forEach(x -> hands.add(new Hand(x.substring(0, 5), Integer.parseInt(x.substring(6)), isJokerHand)));
		Collections.sort(hands);
		return IntStream.range(0, hands.size()).reduce(0, (t, x) -> t + (hands.get(x).bid * (x + 1)));
	}
}
