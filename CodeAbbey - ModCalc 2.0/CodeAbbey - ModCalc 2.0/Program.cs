using System;

namespace CodeAbbey___ModCalc_2._0
{
    class Program
    {
        static void Main(string[] args)
        {
            ulong n = Convert.ToUInt64(Console.ReadLine());
            while (true)
            {
                string[] dataArray = Console.ReadLine().Split(' ');
                if (dataArray[0] == "+")
                {
                    n += Convert.ToUInt64(dataArray[1]);
                    Console.WriteLine(n);
                }
                else if (dataArray[0] == "*")
                {
                    n *= Convert.ToUInt64(dataArray[1]);
                    Console.WriteLine(n);
                }
                else if (dataArray[0] == "%")
                {
                    n = n%Convert.ToUInt64(dataArray[1]);
                    break;
                }
            }
            Console.WriteLine(Convert.ToUInt64(n));
            Console.ReadLine();
        }
    }
}
