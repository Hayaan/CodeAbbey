using System;
using System.Windows.Forms;

namespace CodeAbbey___SavingsCalculator
{
    class Program
    {
        [STAThreadAttribute]
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            string endResult = "";
            for (int i = 0; i < n; i++)
            {
                float[] currentLineFloat = Array.ConvertAll<string, float>(Console.ReadLine().Split(' '), float.Parse);
                // Starting/current sum             // Required sum
                float reqSum = currentLineFloat[1]; float currSum = currentLineFloat[0]; 
                int yearCount = 0;
                while (currSum < reqSum)
                {
                    ++yearCount;
                    currSum *= (1 + currentLineFloat[2] / 100);
                }
                endResult += yearCount.ToString() + " ";
            }
            Clipboard.SetText(endResult);
            Console.WriteLine(endResult.Trim());
            Console.ReadLine();
        }
    }
}
