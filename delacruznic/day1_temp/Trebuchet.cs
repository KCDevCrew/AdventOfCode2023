using System.IO;

namespace Day1 {
  class Trebuchet
  {
    string fileName;

    public Trebuchet(string fileName)
    {
        this.fileName = fileName;
    }
    private int getFirstNumber (string line, int index) {
      if (Char.IsDigit(line[index])) return int.Parse(line[index]);
      return getFirstNumber(line, index++);
    }

    private int getLastNumber (string line) {
      if (Char.IsDigit(line[index])) return int.Parse(line[index]);
      return getFirstNumber(line, index--);
    }
    public int getCalibration (string line) {
      int result = 0;
      try
      {
          string path = Directory.GetCurrentDirectory() + this.inputFileName;
          StreamReader sr = new StreamReader(path);

          //Read the first line of text
          line = sr.ReadLine();

          //Continue to read until you reach end of file
          while (line != null)
          {
              //write the line to console window
              result += this.getFirstNumber(line) + this.getLastNumber(line);

              //Read the next line
              line = sr.ReadLine();
          }
          //close the file
          sr.Close();
          Console.ReadLine();
      }
      catch(Exception e)
      {
          Console.WriteLine("Exception: " + e.Message);
      }
      return result;
    }
  }
}
