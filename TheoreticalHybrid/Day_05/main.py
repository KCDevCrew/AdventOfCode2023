import time
from typing import List

USE_LOGGING = False
USE_DEMO = False
PART_ONE = False

class Map:
    def __init__(self, destinationRangeStart, sourceRangeStart, rangeLength):
        self.SourceStart = sourceRangeStart
        self.DestinationStart = destinationRangeStart
        self.RangeLength = rangeLength
        self.SourceEnd = self.SourceStart + self.RangeLength - 1
        self.Shift = self.DestinationStart - self.SourceStart

    def __repr__(self):
        return f'<{self.DestinationStart} {self.SourceStart} {self.RangeLength}>'

    def getMap(self, value):
        return value + self.Shift if self.SourceStart <= value <= self.SourceEnd else -1

SeedToSoilMaps: List[Map] = []
SoilToFertilizerMaps: List[Map] = []
FertilizerToWaterMaps: List[Map] = []
WaterToLightMaps: List[Map] = []
LightToTempMaps: List[Map] = []
TempToHumidityMaps: List[Map] = []
HumidityToLocationMaps: List[Map] = []

def getInput(fileName):
    global SeedToSoilMaps
    global SoilToFertilizerMaps
    global FertilizerToWaterMaps
    global WaterToLightMaps
    global LightToTempMaps
    global TempToHumidityMaps
    global HumidityToLocationMaps

    file = open(fileName, 'r')

    input = [block for block in file.read().split('\n\n')]

    if USE_LOGGING: print(input)

    seeds = []

    for block in input:
        key = block.split(':')[0].strip()
        value = block.split(':')[1].strip()

        mapList = [Map(int(map.split()[0]), int(map.split()[1]), int(map.split()[2])) for map in value.split('\n')]

        match key:
            case 'seeds':
                seeds = [int(s) for s in value.split()]
            case 'seed-to-soil map':
                SeedToSoilMaps = mapList
            case 'soil-to-fertilizer map':
                SoilToFertilizerMaps = mapList
            case 'fertilizer-to-water map':
                FertilizerToWaterMaps = mapList
            case 'water-to-light map':
                WaterToLightMaps = mapList
            case 'light-to-temperature map':
                LightToTempMaps = mapList
            case 'temperature-to-humidity map':
                TempToHumidityMaps = mapList
            case 'humidity-to-location map':
                HumidityToLocationMaps = mapList

    if USE_LOGGING:
        print(f'Seeds: {seeds}')
        print(f'S to S: {SeedToSoilMaps}')
        print(f'S to F: {SoilToFertilizerMaps}')
        print(f'F to W: {FertilizerToWaterMaps}')
        print(f'W to L: {WaterToLightMaps}')
        print(f'L to T: {LightToTempMaps}')
        print(f'T to H: {TempToHumidityMaps}')
        print(f'H to L: {HumidityToLocationMaps}')

    return seeds

def getMapValue(maps: List[Map], value):
    for map in maps:
        mapValue = map.getMap(value)
        if mapValue >= 0: return mapValue

    return value

def getSeedLocation(seed):
    soil = getMapValue(SeedToSoilMaps, seed)
    fertilizer = getMapValue(SoilToFertilizerMaps, soil)
    water = getMapValue(FertilizerToWaterMaps, fertilizer)
    light = getMapValue(WaterToLightMaps, water)
    temp = getMapValue(LightToTempMaps, light)
    humidity = getMapValue(TempToHumidityMaps, temp)
    location = getMapValue(HumidityToLocationMaps, humidity)
    
    if USE_LOGGING: print(f'{seed}->{soil}->{fertilizer}->{water}->{light}->{temp}->{humidity}->{location}')

    return location

def transform(maps: List[Map], rangeValues):
    newRangeValues = []

    rangeQueue = rangeValues

    while (rangeQueue):
        queueUpdate = []

        for seedRange in rangeQueue:
            rangeStart = seedRange[0]
            rangeEnd = seedRange[1]

            mapped = False

            for map in maps:
                if map.SourceStart <= rangeStart <= map.SourceEnd or map.SourceStart <= rangeEnd <= map.SourceEnd:
                    remainders = []
                    transformStart, transformEnd = None, None

                    if rangeStart < map.SourceStart:
                        transformStart = map.DestinationStart
                        if rangeStart < map.SourceStart: remainders.append((rangeStart, map.SourceStart - 1))
                    else:
                        transformStart = map.getMap(rangeStart)

                    if rangeEnd < map.SourceEnd:
                        transformEnd = map.getMap(rangeEnd)
                    else:
                        transformEnd = map.getMap(map.SourceEnd)
                        if rangeEnd > map.SourceEnd: remainders.append((map.SourceEnd + 1, rangeEnd))

                    queueUpdate = queueUpdate + remainders
                    newRangeValues.append((transformStart, transformEnd))
                    mapped = True

            if not mapped: newRangeValues.append(seedRange)
        
        rangeQueue = queueUpdate

    return set(newRangeValues) # Change to a set to get rid of duplicate values

def getLowestSeedLocation(input):    
    lowestSeedLocation = -1

    if PART_ONE:
        for seed in input:
            location = getSeedLocation(seed)

            if lowestSeedLocation < 0 or location < lowestSeedLocation:
                lowestSeedLocation = location
    else:
        # gonna try the brute force, but I doubt this is the way to go
        # yeah, no that won't work
        
        # startPoint, seedRange = 0, 0
        # for i, x in enumerate(input):
        #     if i % 2 == 0:
        #         startPoint = x
        #     else:
        #         seedRange = x
                
        #         for seed in range(startPoint, startPoint + seedRange):
        #             location = getSeedLocation(seed)

        #             if lowestSeedLocation < 0 or location < lowestSeedLocation:
        #                 lowestSeedLocation = location

        # another thought is maybe I should transform the ranges as I go, like change [79:92] to [81:94]
        startingNumber = 0
        ranges = []
        for i, x in enumerate(input):
            if i % 2 == 0:
                startingNumber = x
            else:
                ranges.append((startingNumber, startingNumber + x - 1))

        if USE_LOGGING: print(ranges)
        ranges = transform(SeedToSoilMaps, ranges)
        if USE_LOGGING: print(ranges)
        ranges = transform(SoilToFertilizerMaps, ranges)
        if USE_LOGGING: print(ranges)
        ranges = transform(FertilizerToWaterMaps, ranges)
        if USE_LOGGING: print(ranges)
        ranges = transform(WaterToLightMaps, ranges)
        if USE_LOGGING: print(ranges)
        ranges = transform(LightToTempMaps, ranges)
        if USE_LOGGING: print(ranges)
        ranges = transform(TempToHumidityMaps, ranges)
        if USE_LOGGING: print(ranges)
        ranges = transform(HumidityToLocationMaps, ranges)
        if USE_LOGGING: print(ranges)

        for pair in ranges:
            if lowestSeedLocation < 0 or pair[0] < lowestSeedLocation:
                lowestSeedLocation = pair[0]

    return lowestSeedLocation

startTime = time.time()

file = 'example.txt' if USE_DEMO else 'input1.txt'
input = getInput(file)
solution = getLowestSeedLocation(input)

endtime = time.time()
print(f'Solution: ', solution)
print ('Completion time: ', endtime - startTime)