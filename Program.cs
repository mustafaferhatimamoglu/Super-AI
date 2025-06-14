using System;
using System.Threading.Tasks;

namespace SuperAI
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
            var superMfi = new SuperMFI(apiKey);
            var result = await superMfi.SuperMFIAsync();
            Console.WriteLine(result);
        }
    }
}
