from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class GenerateText:
    def __init__(self, context="I love it", text_length=10):
        torch.manual_seed(779)
        self.tkz = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.text_length = text_length
        self.context = context
        self.tokenized = self.tkz.encode(self.context, return_tensors='pt')

    def greedy(self):
        pred_greedy = self.model.generate(self.tokenized, max_length=self.text_length)
        seq = self.tkz.decode(pred_greedy[0], skip_special_tokens=True)
        return seq

    def beam(self):
        op_beam = self.model.generate(self.tokenized, max_length=self.text_length, num_beams=3,
                       num_return_sequences=3)
        for op_beam_cur in op_beam:
            print(self.tkz.decode(op_beam_cur, skip_special_tokens=True))

    def top_k(self, k=2):
        for i in range(3):
            torch.manual_seed(i)
            pred = self.model.generate(
                self.tokenized, 
                do_sample=True, 
                max_length=self.text_length, 
                top_k=k
            )
        seq = self.tkz.decode(op[0], skip_special_tokens=True)
        print(seq)