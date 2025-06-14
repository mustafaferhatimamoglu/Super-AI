import os
import openai
import asyncio

# client config
openai.api_key = os.getenv("OPENAI_API_KEY")

# designPCB agent
async def designPCB(params):
    prompt = f"Design a PCB with these specifications: {params}"
    response = await openai.Completion.acreate(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=150,
    )
    output = response.choices[0].text.strip()
    print("# call designPCB")
    print(output)
    return output

# simulateCircuit agent
async def simulateCircuit(circuit):
    prompt = f"Simulate the following circuit and report issues: {circuit}"
    response = await openai.Completion.acreate(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=150,
    )
    output = response.choices[0].text.strip()
    print("# call simulateCircuit")
    print(output)
    return output

# analyzeErrors agent
async def analyzeErrors(simResult):
    prompt = f"Analyze these simulation results for errors: {simResult}"
    response = await openai.Completion.acreate(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=100,
    )
    output = response.choices[0].text.strip()
    print("# call analyzeErrors")
    print(output)
    return output

# drawCircuitDiagram agent
async def drawCircuitDiagram(pcbData):
    prompt = f"Generate a detailed circuit diagram for: {pcbData}"
    response = await openai.Completion.acreate(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=150,
    )
    output = response.choices[0].text.strip()
    print("# call drawCircuitDiagram")
    print(output)
    return output

# orchestrator logic
async def superMFI(materialsList, motorSpecs, powerConfig):
    print("Starting SuperMFI-AI")
    params = {
        "materialsList": materialsList,
        "motorSpecs": motorSpecs,
        "powerConfig": powerConfig,
    }
    pcbData = await designPCB(params)
    simResult = await simulateCircuit(pcbData)

    errorReport = await analyzeErrors(simResult)
    if "error" in errorReport.lower():
        print("# redesign due to errors")
        pcbData = await designPCB({**params, "errorReport": errorReport})
        simResult = await simulateCircuit(pcbData)

    diagram = await drawCircuitDiagram(pcbData)
    print("SuperMFI-AI completed")
    return {
        "pcbData": pcbData,
        "simResult": simResult,
        "diagram": diagram,
    }

if __name__ == "__main__":
    asyncio.run(
        superMFI(
            ["motor", "resistors", "capacitors"],
            {"type": "dc", "rpm": 1000},
            {"voltage": "12V"},
        )
    )

