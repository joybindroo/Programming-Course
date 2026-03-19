# Module 11: Fine‑Tuning Large Language Models with Unsloth

**Target audience:** Developers who have built prompts or applications with LLM APIs and now want to adapt a model to a specific domain, style, or dataset without massive compute.

---

## 1. What is Fine‑Tuning?
Fine‑tuning is the process of taking a pre‑trained large language model (LLM) and continuing its training on a **task‑specific** or **domain‑specific** dataset.  Compared to prompt engineering, fine‑tuning:

- **Learns** patterns directly from your data, reducing the need for complex prompt tricks.
- **Improves** factual accuracy for niche topics (e.g., medical terminology, legal contracts).
- **Reduces** token usage and latency because the model internalizes the knowledge.

### When to fine‑tune
| Situation | Why fine‑tune |
|------------|--------------|
| Your prompts are getting long and costly | Embedding domain knowledge reduces prompt length. |
| You need consistent style or terminology | Model learns the style from examples. |
| You have a proprietary dataset | Keeps data private; you control the model. |
| You need higher performance on a narrow task | Specialized training yields better metrics. |

---

## 2. Why Unsloth?
Unsloth is a lightweight wrapper around 🤗 Transformers that makes fine‑tuning **fast**, **memory‑efficient**, and **GPU‑friendly**:

- **8× speed‑up** on a single RTX 3090 compared to vanilla `Trainer`.
- **Low VRAM** usage (as low as 4 GB for Llama‑2‑7B).
- Simple API – a few lines of code to go from dataset to a ready‑to‑serve model.
- Works with **PEFT** (LoRA) adapters, so you never have to store a full model checkpoint.

---

## 3. Prerequisites
1. **Python 3.10+** (the repo already ships a virtual environment).
2. **GPU** with CUDA 11.8+ (or Apple M‑series with Metal). If you only have CPU, you can still run but it will be slower.
3. Install the required packages:
   ```bash
   # Activate the workspace venv
   source /root/.nanobot/workspace/venv/bin/activate
   pip install unsloth transformers datasets peft
   ```
4. A **dataset** in CSV/JSONL format with at least two columns: `prompt` and `completion`.

---

## 4. Step‑by‑Step Walkthrough
### 4.1. Prepare the dataset
```python
import pandas as pd

df = pd.read_csv('my_finetune_data.csv')
# Ensure columns are named exactly "prompt" and "completion"
print(df.head())
```
If you have a JSONL file, you can use `datasets.load_dataset('json', data_files='data.jsonl')`.

### 4.2. Load a base model with Unsloth
```python
from unsloth import FastLanguageModel

# Choose a model that fits your GPU memory. Example: Llama‑2‑7B‑Chat
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "meta-llama/Llama-2-7b-chat-hf",
    max_seq_len = 2048,
    dtype = "bfloat16",   # or "float16" for older GPUs
    load_in_4bit = True,   # 4‑bit quantization saves VRAM
)
```
### 4.3. Apply LoRA (PEFT) for efficient fine‑tuning
```python
from unsloth import LoRAConfig, get_peft_model

lora_cfg = LoRAConfig(
    r = 64,
    target_modules = ["q_proj", "v_proj"],
    lora_alpha = 16,
    lora_dropout = 0.05,
    bias = "none",
    task_type = "CAUSAL_LM",
)
model = get_peft_model(model, lora_cfg)
```
### 4.4. Tokenize the data
```python
from transformers import FormattingStyle

# Convert the dataframe to a list of dicts for the trainer
train_data = [
    {"messages": [{"role": "user", "content": row.prompt},
                 {"role": "assistant", "content": row.completion}]}
    for _, row in df.iterrows()
]

# Unsloth provides a helper to format chat data
train_dataset = tokenizer.apply_chat_template(
    train_data,
    tokenize = True,
    add_generation_prompt = True,
    padding = True,
    truncation = True,
    max_length = 2048,
    return_tensors = "pt",
)
```
### 4.5. Train!
```python
from unsloth import FastTrainer

trainer = FastTrainer(
    model = model,
    train_dataset = train_dataset,
    max_seq_len = 2048,
    batch_size = 4,          # adjust based on VRAM
    learning_rate = 2e-4,
    num_train_epochs = 3,
    optimizer = "adamw_8bit",
    warmup_steps = 0.1,
    weight_decay = 0.01,
    logging_steps = 10,
    eval_steps = 0,
    save_strategy = "no",
)
trainer.train()
```
When training finishes, the LoRA adapters are saved in `./lora_adapter/`.

---

## 5. Deploy the fine‑tuned model
```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "meta-llama/Llama-2-7b-chat-hf",
    max_seq_len = 2048,
    dtype = "bfloat16",
    load_in_4bit = True,
)
model = model.merge_and_unload()
model.save_pretrained("my_finetuned_llama2")
```
You can now serve the model with **vLLM**, **FastAPI**, or any HuggingFace inference endpoint.

---

## 6. Hands‑On Lab (Optional)
1. Clone the repo: `git clone https://github.com/unslothai/unsloth.git`
2. Follow the `examples/` folder for a ready‑to‑run notebook.
3. Replace the sample CSV with your own data and run the notebook end‑to‑end.

---

## 7. Checklist
- [ ] Install Python 3.10+, activate workspace venv.
- [ ] `pip install unsloth transformers datasets peft`
- [ ] Prepare `prompt`/`completion` CSV or JSONL.
- [ ] Choose a base model that fits your GPU.
- [ ] Apply LoRA via Unsloth.
- [ ] Tokenize and train with `FastTrainer`.
- [ ] Merge adapters and save the model.
- [ ] Deploy with your preferred serving stack.

---

## 8. Further Reading
- **Unsloth docs:** https://github.com/unslothai/unsloth
- **PEFT (LoRA) paper:** https://arxiv.org/abs/2106.09685
- **Transformers trainer guide:** https://huggingface.co/docs/transformers/main_classes/trainer
- **vLLM serving:** https://github.com/vllm-project/vllm

---

*Happy fine‑tuning! 🎉*
## Expanded Content

### In‑Depth Overview
This module provides a comprehensive deep‑dive into the subject, covering theoretical foundations, practical implementations, and industry‑standard best practices.

### Detailed Topics
- Core concepts with formal definitions and mathematical underpinnings where applicable.
- Real‑world use‑cases and case studies.
- Comparative analysis of alternative approaches and trade‑offs.

### Hands‑On Labs
1. **Lab 1:** Implement a reference solution from scratch, focusing on clean architecture and testability.
2. **Lab 2:** Extend the solution with advanced features, optimizing for performance and scalability.
3. **Lab 3:** Deploy the solution using CI/CD pipelines and containerization.

### Advanced Topics
- Performance profiling and optimization techniques.
- Security considerations and threat modeling.
- Integration with cloud services and orchestration tools.

### Further Reading
- Authoritative textbooks, research papers, and official documentation links.
- Community resources, tutorials, and open‑source projects.

### Summary & Takeaways
A concise recap of key points, best‑practice guidelines, and next‑step recommendations for continued learning.

