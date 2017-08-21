using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeAbbey___ModularCalc
{
    class Program
    {
        static void Main(string[] args)
        {
            float n = float.Parse(Console.ReadLine());

            while (true)
            {
                string[] strArray = Console.ReadLine().Split(' ');
                float Operator = float.Parse(strArray[1]);
                //char[] charArray = Convert.ToChar(Console.ReadLine().Split(' '));
                if (strArray[0] == "+")
                {
                    n += Operator;
                }
                else if (strArray[0] == "*")
                {
                    n *= Operator;
                }
                else if (strArray[0] == "%")
                {
                    n = n % Operator;
                    break;
                }
            }
            Console.Clear();
            Console.WriteLine(n);
            Console.ReadLine();
        }
    }
}
