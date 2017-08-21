using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Maximum_of_array___CodeAbbey
{
    class Program
    {
        static void Main(string[] args)
        {
            //int[] myArray = new int[3000];
            //myArray
            string values = Console.ReadLine();
            string correctValues = values.Replace(" ", ", ");
            int[] myArray = { Convert.ToInt32(correctValues) };
            int result = myArray.Max;
            Console.WriteLine("{0} {1}", myArray.Min, myArray.Max);
            Console.ReadLine();
        }
    }
}
