const { OpenAI } = require('@openai/openai');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function designPCB(params) {
  console.log('designPCB start'); // call designPCB
  const res = await openai.createCompletion({
    model: 'code-davinci-002',
    prompt: `Design a PCB with params: ${JSON.stringify(params)}`,
    max_tokens: 100
  });
  return res.data.choices[0].text.trim();
}

async function simulateCircuit(circuit) {
  console.log('simulateCircuit start'); // call simulateCircuit
  const res = await openai.createCompletion({
    model: 'code-davinci-002',
    prompt: `Simulate circuit: ${circuit}`,
    max_tokens: 100
  });
  return res.data.choices[0].text.trim();
}

async function analyzeErrors(simResult) {
  console.log('analyzeErrors start'); // call analyzeErrors
  const res = await openai.createCompletion({
    model: 'code-davinci-002',
    prompt: `Analyze simulation result for errors: ${simResult}`,
    max_tokens: 50
  });
  return res.data.choices[0].text.includes('error');
}

async function drawCircuitDiagram(pcbData) {
  console.log('drawCircuitDiagram start'); // call drawCircuitDiagram
  const res = await openai.createCompletion({
    model: 'code-davinci-002',
    prompt: `Draw circuit diagram for: ${pcbData}`,
    max_tokens: 100
  });
  return res.data.choices[0].text.trim();
}

// orchestrator logic
async function superMFI(materialsList, motorSpecs, powerConfig) {
  console.log('SuperMFI-AI orchestrator started');
  let pcb = await designPCB({ materialsList, motorSpecs, powerConfig });
  let sim = await simulateCircuit(pcb);
  const hasErrors = await analyzeErrors(sim);

  if (hasErrors) {
    console.log('Errors detected. Redesigning PCB');
    pcb = await designPCB({ materialsList, motorSpecs, powerConfig });
  }

  const diagram = await drawCircuitDiagram(pcb);
  console.log('Orchestration complete');
  return diagram;
}

module.exports = { superMFI };
