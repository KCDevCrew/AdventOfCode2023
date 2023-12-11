using day2;
class MainClass
{
    static void Main(string[] args)
    {
      Console.WriteLine("Advent of code Day 2");
      var cubeConundrum = new CubeConundrum("input.txt");
      int total = cubeConundrum.getEligibleGamesTotal();
      int setSum = cubeConundrum.getSumOfPowerSets();
      Console.WriteLine($"Part 1: Total eligible games: {total}");
      Console.WriteLine($"Part 2: Set of sums: {setSum}");
    }
}
