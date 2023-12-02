using day1;
class TestClass
{
    static void Main(string[] args)
    {
      Console.WriteLine("Advent of code Day 1");
      var trebuchet = new Trebuchet("input.txt");
      int calibration = trebuchet.getCalibration();
      Console.WriteLine($"Part 1: Calculated calibration for trebuchet: {calibration}");
    }
}
