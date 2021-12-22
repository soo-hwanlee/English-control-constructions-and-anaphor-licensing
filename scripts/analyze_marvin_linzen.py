import csv, argparse, sys




def get_critical_prob(result_obj1, result_obj2):
  tokens1 = result_obj1["tokens"].split("|||")
  log_probs1 = result_obj1["log_probs"].split("|||")
  tokens2 = result_obj2["tokens"].split("|||")
  log_probs2 = result_obj2["log_probs"].split("|||")
  idx = -1
  #assert(len(tokens1) == len(tokens2))
  for i in range(len(tokens1)):
    if tokens1[i] != tokens2[i]:
      idx = i
      break
  
  print(tokens1[idx], tokens2[idx])
  return float(log_probs1[idx])

def main():
  
  parser = argparse.ArgumentParser()
  parser.add_argument("--grammatical", required=True)
  parser.add_argument("--ungrammatical", required=True)
  
  args = parser.parse_args()
  
  grammatical_fname = args.grammatical
  ungrammatical_fname = args.ungrammatical
  
  
  results_objs = []
  accuracy_counter = 0.0
  accuracy_denom = 0.0 
  
  with open(grammatical_fname, "r") as g_f, open(ungrammatical_fname, "r") as u_f:
    g_reader = csv.DictReader(g_f)
    u_reader = csv.DictReader(u_f)
    for g_ex in g_reader:
      u_ex = next(u_reader)
      
      results_obj = {}
      results_obj["grammatical_sentence"] = g_ex["sentence"]
      results_obj["ungrammatical_sentence"] = u_ex["sentence"]
      
      results_obj["grammatical_log_prob"] = get_critical_prob(g_ex, u_ex)
      results_obj["ungrammatical_log_prob"] =  get_critical_prob(u_ex, g_ex)
  
      #results_obj["baseline_greater_than_ungrammatical"] = 1 if results_obj["baseline_pron_log_prob"] > results_obj["ungrammatical_pron_log_prob"] else 0
      #results_obj["distractor_greater_than_ungrammatical"] = 1 if results_obj["distractor_pron_log_prob"] > results_obj["ungrammatical_pron_log_prob"] else 0
      #results_obj["correct"] = 1 if results_obj["baseline_pron_log_prob"] > results_obj["ungrammatical_pron_log_prob"] and results_obj["distractor_pron_log_prob"] > results_obj["ungrammatical_pron_log_prob"] else 0
      results_obj["correct"] = 1 if results_obj["grammatical_log_prob"] > results_obj["ungrammatical_log_prob"] else 0
      results_objs.append(results_obj)
      accuracy_counter += results_obj["correct"] 
      accuracy_denom += 1.0
  
  
  writer = csv.DictWriter(sys.stdout, fieldnames = results_objs[0].keys())
  writer.writeheader()
  writer.writerows(results_objs)
   
  print(accuracy_counter/accuracy_denom)   
    
  
  



if __name__ == '__main__':
  main()

