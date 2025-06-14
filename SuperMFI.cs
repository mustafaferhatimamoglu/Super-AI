using System;
using System.Text.Json;
using System.Threading.Tasks;
using OpenAI_API;
using OpenAI_API.Models;

public class SuperMFI
{
    private readonly OpenAIAPI api;

    public SuperMFI(string apiKey)
    {
        api = new OpenAIAPI(apiKey);
    }

    // call designPCB
    public async Task<string> DesignPCB(object parameters)
    {
        Console.WriteLine("designPCB start");
        string prompt = $"Design a PCB with params: {JsonSerializer.Serialize(parameters)}";
        var result = await api.Completions.CreateCompletionAsync(prompt, model: Model.DavinciCode, max_tokens: 100);
        return result.ToString().Trim();
    }

    // call simulateCircuit
    public async Task<string> SimulateCircuit(string circuit)
    {
        Console.WriteLine("simulateCircuit start");
        string prompt = $"Simulate circuit: {circuit}";
        var result = await api.Completions.CreateCompletionAsync(prompt, model: Model.DavinciCode, max_tokens: 100);
        return result.ToString().Trim();
    }

    // call analyzeErrors
    public async Task<bool> AnalyzeErrors(string simResult)
    {
        Console.WriteLine("analyzeErrors start");
        string prompt = $"Analyze simulation result for errors: {simResult}";
        var result = await api.Completions.CreateCompletionAsync(prompt, model: Model.DavinciCode, max_tokens: 50);
        return result.ToString().ToLower().Contains("error");
    }

    // call drawCircuitDiagram
    public async Task<string> DrawCircuitDiagram(string pcbData)
    {
        Console.WriteLine("drawCircuitDiagram start");
        string prompt = $"Draw circuit diagram for: {pcbData}";
        var result = await api.Completions.CreateCompletionAsync(prompt, model: Model.DavinciCode, max_tokens: 100);
        return result.ToString().Trim();
    }

    // orchestrator logic
    public async Task<string> SuperMFIAsync(object materialsList, object motorSpecs, object powerConfig)
    {
        Console.WriteLine("SuperMFI-AI orchestrator started");
        var pcb = await DesignPCB(new { materialsList, motorSpecs, powerConfig });
        var sim = await SimulateCircuit(pcb);
        var hasErrors = await AnalyzeErrors(sim);

        if (hasErrors)
        {
            Console.WriteLine("Errors detected. Redesigning PCB");
            pcb = await DesignPCB(new { materialsList, motorSpecs, powerConfig });
        }

        var diagram = await DrawCircuitDiagram(pcb);
        Console.WriteLine("Orchestration complete");
        return diagram;
    }
}
