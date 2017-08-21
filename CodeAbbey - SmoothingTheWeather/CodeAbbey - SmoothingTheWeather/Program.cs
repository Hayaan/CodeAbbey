using System;
using System.IO;
using System.Windows.Forms;

namespace CodeAbbey___SmoothingTheWeather
{
    class Program
    {
        [STAThreadAttribute]
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            double[] resultsArr = new double[n];
            // Increases the amount of data that can be entered into the Console ...
            // ... into a single line.
            int bufSize = 2048;
            Stream inStream = Console.OpenStandardInput(bufSize);
            Console.SetIn(new StreamReader(inStream, Console.InputEncoding, false, bufSize));

            string[] placeholderArr = Console.ReadLine().Split(' ');
            double[] inputArr = Array.ConvertAll<string, double>(placeholderArr, double.Parse);
            double first, last;

            // Moving the first and last values to the different double array, before the loop runs.
            first = inputArr[0]; last = inputArr[n - 1];
            resultsArr[0] = first; resultsArr[n - 1] = last;

            // Move all averages into a different double array, after putting them into a new ...
            // ... double on the stack. So as to not affect any subsequent calculations.
            for (int i = 1; i < n - 1; i++)
            {
                double moveToNewArr = (inputArr[i - 1] + inputArr[i] + inputArr[i + 1]) / 3;
                resultsArr[i] = moveToNewArr;
            }
            string endResult = "";
            foreach (double double_ in resultsArr)
            {
                endResult += double_.ToString() + " ";
            }
            // Allows you to copy+paste the answer.
            Clipboard.SetText(endResult.TrimEnd());
            Console.Clear();
            Console.WriteLine(endResult.TrimEnd());
            Console.ReadLine();
        }
    }
}
