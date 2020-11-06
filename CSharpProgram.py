using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine("How many students are there? ");
    string Students = Console.ReadLine();
    int[] Test1 = new int[Students]; 
    int[] Test2 = new int[Students]; 
    int[] Test3 = new int[Students];
    string[] Names = new string[Students];

    for(int i = 0; i <= Students; i++) {
      Console.WriteLine("Student Name:");
      string StudentName = Console.ReadLine();
      Names[i] = StudentName;
      Console.WriteLine("\nTest 1 Score: ");
      int Test1Score = Console.ReadLine();
      Test1[i] = Test1Score;
      Console.WriteLine("\nTest 2 Score: ");
      int Test2Score = Console.ReadLine();
      Test2[i] = Test2Score;
      Console.WriteLine("\nTest 3 Score: ");
      int Test3Score = Console.ReadLine();
      Test3[i] = Test3Score;
    }

    Console.WriteLine(StudentName + "\n" + Test1Score + "\n" + Test2Score + "\n" + Test3Score);
  }
}
