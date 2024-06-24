# 📚 **Documenting Code Snippets for Neural Networks** 

Welcome! In this section, I will document the various code snippets used in my NN's. 

### **Snippet 1: Counting Parameters of Model**

snippet that prints the total number of parameters in the Iron Man model:

```python
print(sum(p.numel() for p in model_name.parameters()))
```
