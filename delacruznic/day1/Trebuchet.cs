namespace day1;

using System.IO;

class Trebuchet
{
  string fileName;

  private Dictionary<string,int> numberTable = new Dictionary<string,int>
  {
    {"zero",0},{"one",1},{"two",2},{"three",3},{"four",4},
    {"five",5},{"six",6},{"seven",7},{"eight",8},{"nine",9}
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
            int lineCalibration = Int32.Parse("" + firstNum + lastNum);
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
