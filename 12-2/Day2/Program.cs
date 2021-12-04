using System;
using System.IO;

namespace Day2
{
    class Program
    {
        static int X = 0;
        static int Depth = 0;
        static int Aim = 0;

        static void Main(string[] args)
        {
            foreach (string line in File.ReadLines(@"..\..\..\..\input.txt"))
            {
                ReadOnlySpan<char> spanLine = line.AsSpan();
                int space = spanLine.IndexOf(" ");
                string command = spanLine[..space].ToString();
                int amount = int.Parse(spanLine[(space + 1)..]);

                PerformCommandPt2(command, amount);
            }

            Console.WriteLine((X, Depth));
            Console.WriteLine(X * Depth);
        }

        private static void PerformCommandPt1(string command, int amount)
        {
            switch (command)
            {
                case "forward":
                {
                    X += amount;
                }
                break;
                case "down":
                {
                    Depth += amount;
                }
                break;
                case "up":
                {
                    amount = Math.Min(amount, Depth);
                    Depth -= amount;
                }
                break;
            }
        }

        private static void PerformCommandPt2(string command, int amount)
        {
            switch (command)
            {
                case "forward":
                {
                    X += amount;
                    int depthChange = amount * Aim;
                    Depth += depthChange;
                }
                break;
                case "down":
                {
                    Aim += amount;
                }
                break;
                case "up":
                {
                    Aim -= amount;
                }
                break;
            }
        }
    }
}
