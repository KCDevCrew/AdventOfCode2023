using day2;
class MainClass
{
    static void Main(string[] args)
    {
      Console.WriteLine("Advent of code Day 2");
      var cubeConundrum = new CubeConundrum("input.txt");
      int total = cubeConundrum.getEligibleGamesTotal();
      Console.WriteLine($"Total eligible games {total}");
    }
}
