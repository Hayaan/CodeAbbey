using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CodeAbbey___BMI
{
    class Program
    {
        [STAThreadAttribute]
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string result = "";

            for (int i = 0; i < n; i++)
            {
                string[] strArr = Console.ReadLine().Split(' ');
                float[] loopArr = Array.ConvertAll<string, float>(strArr, float.Parse);

                float BMI = loopArr[0] / (loopArr[1] * loopArr[1]);

                if (BMI < 18.5)
                    result += "under ";
                else if (18.5 <= BMI && BMI < 25.0)
                    result += "normal ";
                else if (25.0 <= BMI && BMI < 30.0)
                    result += "over ";
                else if (BMI >= 30.0)
                    result += "obese ";
            }
            Clipboard.SetText(result.TrimEnd());
            Console.WriteLine(result.TrimEnd());
            Console.ReadLine();
        }
    }
}
