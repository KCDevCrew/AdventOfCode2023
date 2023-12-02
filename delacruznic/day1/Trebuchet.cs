namespace day1;

using System.IO;
using System.Text.RegularExpressions;

class Trebuchet
{
  string fileName;

  private Dictionary<string,char> numberTable = new Dictionary<string,char>
  {
    {"one", '1'}, {"two", '2'}, {"three", '3'}, {"four", '4'},
    {"five", '5'}, {"six", '6'}, {"seven", '7'}, {"eight", '8'}, {"nine", '9'}
  };
  public Trebuchet(string fileName)
  {
      this.fileName = fileName;
  }
  private char getFirstNumber (string line, int index) {
    if (Char.IsDigit(line[index])) return line[index];
    int newIndex = index + 1;
    return this.getFirstNumber(line, newIndex);
  }

  private char? getFirstWordNum (string line) {
    char value = 'a';
    int index = line.Length;
    foreach(KeyValuePair<string, char> entry in numberTable)
    {
      if (line.IndexOf(entry.Key) < index && line.IndexOf(entry.Key) > -1) {
        index = line.IndexOf(entry.Key);
        value = entry.Value;
      }
    }
    if (value != 'a') return value;
    else return null;
  }

  private char? getLastWordNum (string line) {
    char value = 'a';
    int index = -1;
    foreach(KeyValuePair<string, char> entry in numberTable)
    {
      if (line.LastIndexOf(entry.Key) > index) {
        index = line.LastIndexOf(entry.Key);
        value = entry.Value;
      }
    }
    if (value != 'a') return value;
    else return null;
  }

  private char getLastNumber (string line,  int index) {
    if (Char.IsDigit(line[index-1])) return line[index-1];
    int newIndex = index - 1;
    return this.getLastNumber(line, newIndex);
  }


  public int getCalibration () {
    int result = 0;
    try
    {
        string path = Directory.GetCurrentDirectory() + "/" + this.fileName;
        StreamReader sr = new StreamReader(path);

        //Read the first line of text
        String line = sr.ReadLine();

        //Continue to read until you reach end of file
        while (line != null)
        {
            //write the line to console window
            char firstNum = this.getFirstNumber(line, 0);
            char lastNum = this.getLastNumber(line, line.Length);
            char? firstWordNum = this.getFirstWordNum(line.Substring(0, line.IndexOf(firstNum)));
            char? lastWordNum = this.getLastWordNum(line.Substring(line.LastIndexOf(lastNum)));

            char? firstValue = firstWordNum != null ? firstWordNum : firstNum;
            char? lastValue = lastWordNum != null ? lastWordNum : lastNum;

            int lineCalibration = Int32.Parse("" + firstValue + lastValue);
            result += lineCalibration;

            //Read the next line
            line = sr.ReadLine();
        }
        //close the file
        sr.Close();
    }
    catch(Exception e)
    {
        Console.WriteLine("Exception: " + e.Message);
    }
    return result;
  }
}
