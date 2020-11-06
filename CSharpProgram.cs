using System;

namespace TaskScores {

  static class globalVars {
    public static string[] Test1;
    public static string[] Test2;
    public static string[] Test3;
    public static string[] Names;

    public static int x;
    public static string StudentName; //for the line 28 for loop (to input student names)
  }

  class mainClass {
    public static void Main(string[] args) {
      Console.WriteLine("How many students are there? ");
      string Students = Console.ReadLine();
      if(Int32.TryParse(Students, out var x)) {
        string[] Test1 = new string[x]; 
        string[] Test2 = new string[x]; 
        string[] Test3 = new string[x];
        string[] Names = new string[x];
      } else {
        Console.WriteLine("Attempt to parse your input was unsuccessful.");
      }

      for(int i = 0; i <= x; i++) {
        Console.WriteLine("Student Name:");
        globalVar.StudentName = Console.ReadLine();
        globalVars.Names[i] = globalVar.StudentName;
        Console.WriteLine("\nTest 1 Score: ");
        string Test1Score = Console.ReadLine();
        globalVars.Test1[i] = Test1Score;
        Console.WriteLine("\nTest 2 Score: ");
        string Test2Score = Console.ReadLine();
        globalVars.Test2[i] = Test2Score;
        Console.WriteLine("\nTest 3 Score: ");
        string Test3Score = Console.ReadLine();
        globalVars.Test3[i] = Test3Score;
      }
      Console.WriteLine(globalVar.StudentName + "\n" + globalVar.Test1 + "\n" + globalVar.Test2 + "\n" + globalVar.Test3);
    }
  }
}
