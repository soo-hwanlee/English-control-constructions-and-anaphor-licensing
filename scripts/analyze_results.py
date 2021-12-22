import csv, argparse, sys


REFLEXIVE_PRONOUN_TOKEN = "Ġhimself"


def get_pronoun_prob(result_obj):
  tokens = result_obj["tokens"].split("|||")
  log_probs = result_obj["log_probs"].split("|||")
  idx = tokens.index(REFLEXIVE_PRONOUN_TOKEN)
  return float(log_probs[idx])

def main():
  
  parser = argparse.ArgumentParser()
  parser.add_argument("--baseline", required=True)
  parser.add_argument("--distractor", required=True)
  parser.add_argument("--ungrammatical", required=True)
  
  args = parser.parse_args()
  
  baseline_fname = args.baseline
  distractor_fname = args.distractor
  ungrammatical_fname = args.ungrammatical
  
  
  results_objs = []
  
  with open(baseline_fname, "r") as b_f, open(distractor_fname, "r") as d_f, open(ungrammatical_fname, "r") as u_f:
    b_reader = csv.DictReader(b_f)
    d_reader = csv.DictReader(d_f)
    u_reader = csv.DictReader(u_f)
    for b_ex in b_reader:
      d_ex = next(d_reader)
      u_ex = next(u_reader)
      
      results_obj = {}
      results_obj["verb"] = b_ex["sentence"].split(" ")[2]
      results_obj["baseline_sentence"] = b_ex["sentence"]
      results_obj["distractor_sentence"] = d_ex["sentence"]
      results_obj["ungrammatical_sentence"] = u_ex["sentence"]
      
      results_obj["baseline_pron_log_prob"] = get_pronoun_prob(b_ex)
      results_obj["distractor_pron_log_prob"] = get_pronoun_prob(d_ex)
      results_obj["ungrammatical_pron_log_prob"] = get_pronoun_prob(u_ex)
  
      results_obj["baseline_greater_than_ungrammatical"] = 1 if results_obj["baseline_pron_log_prob"] > results_obj["ungrammatical_pron_log_prob"] else 0
      results_obj["distractor_greater_than_ungrammatical"] = 1 if results_obj["distractor_pron_log_prob"] > results_obj["ungrammatical_pron_log_prob"] else 0
      results_obj["correct"] = 1 if results_obj["baseline_pron_log_prob"] > results_obj["ungrammatical_pron_log_prob"] and results_obj["distractor_pron_log_prob"] > results_obj["ungrammatical_pron_log_prob"] else 0
      
      results_objs.append(results_obj)
  
  
  writer = csv.DictWriter(sys.stdout, fieldnames = results_objs[0].keys())
  writer.writeheader()
  writer.writerows(results_objs)
      
    
  
  



if __name__ == '__main__':
  main()

