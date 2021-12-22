import torch, csv, sys, tqdm, json
import numpy
from lm_scorer.models.auto import AutoLMScorer as LMScorer


examples = []
with open(sys.argv[1], "r") as input_f:
  for line in input_f:
      examples.append(line.strip())

batch_size = 64

device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_fname = sys.argv[2]
model_id = "gpt2" if len(sys.argv) < 4 else sys.argv[3]
scorer = LMScorer.from_pretrained(model_id, device=device, batch_size=batch_size)




example_objs = []

for sentence in tqdm.tqdm(examples):
  
  scores, ids, tokens = scorer.tokens_score(sentence, log=True)
  example_obj = {}
  example_obj["sentence"] = sentence
  example_obj["tokens"] = "|||".join(tokens)
  example_obj["log_probs"] = "|||".join([str(x) for x in scores])

  example_objs.append(example_obj)
   
#    sentences = []
#    for i in range(BATCH_SIZE):
#      full_sentence = examples[idx * BATCH_SIZE + i].replace(" ||| ", "").strip() + "<|endoftext|>"
#      sentences.append(full_sentence)
#    
#    encoding = tokenizer(sentences, padding=True, return_tensors='pt')
#    input_ids = encoding.input_ids.to(device)
#    attention_mask = encoding.attention_mask.to(device)
#    target_ids = input_ids.clone()
#    print(target_ids)
#    print(attention_mask)
    

#    with torch.no_grad():
#      #outputs = model(input_ids, attention_mask=attention_mask)
#      outputs = model(input_ids, attention_mask=attention_mask)
    
#    for i in range(BATCH_SIZE):
#      example_obj = {}
#      example_obj["sentence"] = sentences[i]
#      logits = outputs.logits[i]
#      print(outputs.logits.shape)
#      print(outputs.logits[0, 1, 1169])
#      scores = logits.gather(1, input_ids[i].unsqueeze(1)).squeeze(1)
#      #ppl = outputs.loss * len(input_ids[i])
#      log_probs = scores - logits.logsumexp(1)
#      example_obj["tokens"] = "|||".join([tokenizer._convert_id_to_token(t).replace("Ġ", "##") for t in input_ids[i]])
#      example_obj["log_probs"] = "|||".join([str(x) for x in log_probs.cpu().numpy()])
#      example_obj["scores"] = "|||".join([str(x) for x in scores.cpu().numpy()])
#      example_obj["sums"] = "|||".join([str(x) for x in logits.logsumexp(1).cpu().numpy()])
#      #example_obj["ppl"] = ppl
#      #example_obj["loss"] = outputs.loss
      
    
#      example_objs.append(example_obj)





with open(output_fname, "w") as csv_f:
  writer = csv.DictWriter(csv_f, fieldnames=example_objs[0].keys())
  writer.writeheader()
  writer.writerows(example_objs)
