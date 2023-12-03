namespace day2;

using System.IO;
using System.Text.RegularExpressions;

class CubeConundrum
{
  public const int MAX_RED = 12;
  public const int MAX_GREEN = 13;
  public const int MAX_BLUE = 14;
  private string fileName;
  public CubeConundrum(string fileName)
  {
    this.fileName = fileName;
  }

  public int getEligibleGamesTotal()
  {
    int eligibleGamesTotal = 0;
    try
    {
      string path = Directory.GetCurrentDirectory() + "/" + this.fileName;
      StreamReader sr = new StreamReader(path);

      //Read the first line of text
      String line = sr.ReadLine();

      //Continue to read until you reach end of file
      while (line != null)
      {

        eligibleGamesTotal += this.processGame(line);

        //Read the next line
        line = sr.ReadLine();
      }
      //close the file
      sr.Close();
    }
    catch (Exception e)
    {
      Console.WriteLine("Exception: " + e.Message);
    }
    return eligibleGamesTotal;
  }

  public int getSumOfPowerSets()
  {
    int sumOfSets = 0;
    try
    {
      string path = Directory.GetCurrentDirectory() + "/" + this.fileName;
      StreamReader sr = new StreamReader(path);

      //Read the first line of text
      String line = sr.ReadLine();

      //Continue to read until you reach end of file
      while (line != null)
      {

        sumOfSets += this.getGamePowerSet(line);

        //Read the next line
        line = sr.ReadLine();
      }
      //close the file
      sr.Close();
    }
    catch (Exception e)
    {
      Console.WriteLine("Exception: " + e.Message);
    }
    return sumOfSets;
  }

  private int processGame(string game)
  {
    bool eligibleGame = true;
    int gameId = Int32.Parse(game[5..game.IndexOf(":")]);
    string[] parsedGames = game.Substring(game.IndexOf(":") + 1)
      .Split(new Char [] {',' , ';' }, StringSplitOptions.RemoveEmptyEntries);

    foreach (string parsedGame in parsedGames) {
      if (parsedGame.Contains("blue") ) {
        int blueValue = Int32.Parse(Regex.Match(parsedGame, @"\d+").Value);
        if (blueValue > MAX_BLUE) eligibleGame = false;
      }
      else if (parsedGame.Contains("red") ) {
        int redValue = Int32.Parse(Regex.Match(parsedGame, @"\d+").Value);
        if (redValue > MAX_RED) eligibleGame = false;
      }
      else if (parsedGame.Contains("green") ) {
        int greenValue = Int32.Parse(Regex.Match(parsedGame, @"\d+").Value);
        if (greenValue > MAX_GREEN) eligibleGame = false;
      }
    }

    return eligibleGame ? gameId : 0;
  }

  private int getGamePowerSet(string game)
  {
    int gameId = Int32.Parse(game[5..game.IndexOf(":")]);
    string[] parsedGames = game.Substring(game.IndexOf(":") + 1)
      .Split(new Char [] {',' , ';' }, StringSplitOptions.RemoveEmptyEntries);
    int maxBlue = 0;
    int maxGreen = 0;
    int maxRed = 0;

    foreach (string parsedGame in parsedGames) {
      if (parsedGame.Contains("blue") ) {
        int blueValue = Int32.Parse(Regex.Match(parsedGame, @"\d+").Value);
        if (blueValue > maxBlue) maxBlue = blueValue;
      }
      else if (parsedGame.Contains("red") ) {
        int redValue = Int32.Parse(Regex.Match(parsedGame, @"\d+").Value);
        if (redValue > maxRed) maxRed = redValue;
      }
      else if (parsedGame.Contains("green") ) {
        int greenValue = Int32.Parse(Regex.Match(parsedGame, @"\d+").Value);
        if (greenValue > maxGreen) maxGreen = greenValue;
      }
    }

    return maxBlue * maxGreen * maxRed;
  }
}
