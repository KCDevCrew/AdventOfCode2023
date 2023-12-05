package Day5;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

class DataEntry {
	long destStart;
	long sourceStart;
	long length;
	
	public DataEntry(long destStart, long sourceStart, long length) {
		this.destStart = destStart;
		this.sourceStart = sourceStart;
		this.length = length;
	}
}

class RangeEntry {
	long start;
	long length;
	
	public RangeEntry(long start, long length) {
		this.start = start;
		this.length = length;
	}
}

public class Day5_2023 {
	public static void main(String[] args) {
		System.out.println(getLowestLocationPartOne());
		System.out.println(getLowestLocationPartTwoBruteForceOfShame()); // takes ~5 minutes
	}

	private static long getLowestLocationPartOne() {
		Set<Long> seeds = new HashSet<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/seeds.txt"))) {
			while (scanner.hasNextLong()) {
				seeds.add(scanner.nextLong());
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		List<DataEntry> seedToSoil = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/seed_to_soil.txt"))) {
			while (scanner.hasNextLine()) {
				long soilStart = scanner.nextLong();
				long seedStart = scanner.nextLong();
				long length = scanner.nextLong();
				seedToSoil.add(new DataEntry(soilStart, seedStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> soilToFertilizer = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/soil_to_fertilizer.txt"))) {
			while (scanner.hasNextLine()) {
				long fertilizerStart = scanner.nextLong();
				long soilStart = scanner.nextLong();
				long length = scanner.nextLong();
				soilToFertilizer.add(new DataEntry(fertilizerStart, soilStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> fertilizerToWater = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/fertilizer_to_water.txt"))) {
			while (scanner.hasNextLine()) {
				long waterStart = scanner.nextLong();
				long fertilizerStart = scanner.nextLong();
				long length = scanner.nextLong();
				fertilizerToWater.add(new DataEntry(waterStart, fertilizerStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> waterToLight = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/water_to_light.txt"))) {
			while (scanner.hasNextLine()) {
				long lightStart = scanner.nextLong();
				long waterStart = scanner.nextLong();
				long length = scanner.nextLong();
				waterToLight.add(new DataEntry(lightStart, waterStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> lightToTemp = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/light_to_temp.txt"))) {
			while (scanner.hasNextLine()) {
				long tempStart = scanner.nextLong();
				long lightStart = scanner.nextLong();
				long length = scanner.nextLong();
				lightToTemp.add(new DataEntry(tempStart, lightStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> tempToHumidity = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/temp_to_humidity.txt"))) {
			while (scanner.hasNextLine()) {
				long humidityStart = scanner.nextLong();
				long tempStart = scanner.nextLong();
				long length = scanner.nextLong();
				tempToHumidity.add(new DataEntry(humidityStart, tempStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> humidityToLocation = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/humidity_to_location.txt"))) {
			while (scanner.hasNextLine()) {
				long locationStart = scanner.nextLong();
				long humidityStart = scanner.nextLong();
				long length = scanner.nextLong();
				humidityToLocation.add(new DataEntry(locationStart, humidityStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		long minLocation = Long.MAX_VALUE;
		for (long seed : seeds) {
			long soil = getMappedValue(seed, seedToSoil);
			long fertilizer = getMappedValue(soil, soilToFertilizer);
			long water = getMappedValue(fertilizer, fertilizerToWater);
			long light = getMappedValue(water, waterToLight);
			long temp = getMappedValue(light, lightToTemp);
			long humidity = getMappedValue(temp, tempToHumidity);
			long location = getMappedValue(humidity, humidityToLocation);
			minLocation = Math.min(location, minLocation);
		}
		return minLocation;
	}

	private static long getLowestLocationPartTwoBruteForceOfShame() {		
		List<RangeEntry> seeds = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/seeds.txt"))) {
			while (scanner.hasNextLong()) {
				long start = scanner.nextLong();
				long length = scanner.nextLong();
				seeds.add(new RangeEntry(start, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		List<DataEntry> seedToSoil = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/seed_to_soil.txt"))) {
			while (scanner.hasNextLine()) {
				long soilStart = scanner.nextLong();
				long seedStart = scanner.nextLong();
				long length = scanner.nextLong();
				seedToSoil.add(new DataEntry(soilStart, seedStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> soilToFertilizer = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/soil_to_fertilizer.txt"))) {
			while (scanner.hasNextLine()) {
				long fertilizerStart = scanner.nextLong();
				long soilStart = scanner.nextLong();
				long length = scanner.nextLong();
				soilToFertilizer.add(new DataEntry(fertilizerStart, soilStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> fertilizerToWater = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/fertilizer_to_water.txt"))) {
			while (scanner.hasNextLine()) {
				long waterStart = scanner.nextLong();
				long fertilizerStart = scanner.nextLong();
				long length = scanner.nextLong();
				fertilizerToWater.add(new DataEntry(waterStart, fertilizerStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> waterToLight = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/water_to_light.txt"))) {
			while (scanner.hasNextLine()) {
				long lightStart = scanner.nextLong();
				long waterStart = scanner.nextLong();
				long length = scanner.nextLong();
				waterToLight.add(new DataEntry(lightStart, waterStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> lightToTemp = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/light_to_temp.txt"))) {
			while (scanner.hasNextLine()) {
				long tempStart = scanner.nextLong();
				long lightStart = scanner.nextLong();
				long length = scanner.nextLong();
				lightToTemp.add(new DataEntry(tempStart, lightStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> tempToHumidity = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/temp_to_humidity.txt"))) {
			while (scanner.hasNextLine()) {
				long humidityStart = scanner.nextLong();
				long tempStart = scanner.nextLong();
				long length = scanner.nextLong();
				tempToHumidity.add(new DataEntry(humidityStart, tempStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> humidityToLocation = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/humidity_to_location.txt"))) {
			while (scanner.hasNextLine()) {
				long locationStart = scanner.nextLong();
				long humidityStart = scanner.nextLong();
				long length = scanner.nextLong();
				humidityToLocation.add(new DataEntry(locationStart, humidityStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		long minLocation = Long.MAX_VALUE;
	
		for (RangeEntry rangeEntry : seeds) {
			for (int i = 0; i < rangeEntry.length; i++) {
				long soil = getMappedValue(rangeEntry.start + i, seedToSoil);
				long fertilizer = getMappedValue(soil, soilToFertilizer);
				long water = getMappedValue(fertilizer, fertilizerToWater);
				long light = getMappedValue(water, waterToLight);
				long temp = getMappedValue(light, lightToTemp);
				long humidity = getMappedValue(temp, tempToHumidity);
				long location = getMappedValue(humidity, humidityToLocation);
				minLocation = Math.min(location, minLocation);
			}
		}
		return minLocation;
	}
	
	private static long getLowestLocationPartTwo() {
		List<RangeEntry> seeds = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/seeds.txt"))) {
			while (scanner.hasNextLong()) {
				long start = scanner.nextLong();
				long length = scanner.nextLong();
				seeds.add(new RangeEntry(start, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		List<DataEntry> seedToSoil = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/seed_to_soil.txt"))) {
			while (scanner.hasNextLine()) {
				long soilStart = scanner.nextLong();
				long seedStart = scanner.nextLong();
				long length = scanner.nextLong();
				seedToSoil.add(new DataEntry(soilStart, seedStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> soilToFertilizer = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/soil_to_fertilizer.txt"))) {
			while (scanner.hasNextLine()) {
				long fertilizerStart = scanner.nextLong();
				long soilStart = scanner.nextLong();
				long length = scanner.nextLong();
				soilToFertilizer.add(new DataEntry(fertilizerStart, soilStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> fertilizerToWater = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/fertilizer_to_water.txt"))) {
			while (scanner.hasNextLine()) {
				long waterStart = scanner.nextLong();
				long fertilizerStart = scanner.nextLong();
				long length = scanner.nextLong();
				fertilizerToWater.add(new DataEntry(waterStart, fertilizerStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> waterToLight = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/water_to_light.txt"))) {
			while (scanner.hasNextLine()) {
				long lightStart = scanner.nextLong();
				long waterStart = scanner.nextLong();
				long length = scanner.nextLong();
				waterToLight.add(new DataEntry(lightStart, waterStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> lightToTemp = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/light_to_temp.txt"))) {
			while (scanner.hasNextLine()) {
				long tempStart = scanner.nextLong();
				long lightStart = scanner.nextLong();
				long length = scanner.nextLong();
				lightToTemp.add(new DataEntry(tempStart, lightStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> tempToHumidity = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/temp_to_humidity.txt"))) {
			while (scanner.hasNextLine()) {
				long humidityStart = scanner.nextLong();
				long tempStart = scanner.nextLong();
				long length = scanner.nextLong();
				tempToHumidity.add(new DataEntry(humidityStart, tempStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		List<DataEntry> humidityToLocation = new ArrayList<>();
		try (final Scanner scanner = new Scanner(new File("src/Day5/humidity_to_location.txt"))) {
			while (scanner.hasNextLine()) {
				long locationStart = scanner.nextLong();
				long humidityStart = scanner.nextLong();
				long length = scanner.nextLong();
				humidityToLocation.add(new DataEntry(locationStart, humidityStart, length));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		long minLocation = Long.MAX_VALUE;
		List<RangeEntry> soil = getMappedRanges(seeds, seedToSoil);
		List<RangeEntry> fertilizer = getMappedRanges(soil, soilToFertilizer);
		List<RangeEntry> water = getMappedRanges(fertilizer, fertilizerToWater);
		List<RangeEntry> light = getMappedRanges(water, waterToLight);
		List<RangeEntry> temp = getMappedRanges(light, lightToTemp);
		List<RangeEntry> humidity = getMappedRanges(temp, tempToHumidity);
		List<RangeEntry> location = getMappedRanges(humidity, humidityToLocation);
		return minLocation;
	}
	
	private static List<RangeEntry> getMappedRanges(List<RangeEntry> sources, List<DataEntry> dataEntries) {
		List<RangeEntry> validRanges = new ArrayList<>();
		for (DataEntry dataEntry : dataEntries) {
			for (RangeEntry source : sources) {
				if (source.start >= dataEntry.sourceStart) {
					long overlapIndexFront = source.start - dataEntry.sourceStart;
					long overLapIndexEnd = source.start + source.length >= dataEntry.sourceStart + dataEntry.sourceStart ? 0 : source.start + source.length - (dataEntry.sourceStart + dataEntry.sourceStart);
					validRanges.add(new RangeEntry(dataEntry.destStart + overlapIndexFront, dataEntry.length - overLapIndexEnd));
//					System.out.println((dataEntry.destStart + overlapIndexFront) + " " + (dataEntry.length - overLapIndexEnd));
				}
			}
		}
		return validRanges;
	}
	
	private static long getMappedValue(long source, List<DataEntry> dataEntries) {
		for (DataEntry dataEntry : dataEntries) {
			if (source >= dataEntry.sourceStart && source <= dataEntry.sourceStart + dataEntry.length - 1) {
				long index = source - dataEntry.sourceStart;
				return dataEntry.destStart + index;
			}
		}
		return source;
	}
}
