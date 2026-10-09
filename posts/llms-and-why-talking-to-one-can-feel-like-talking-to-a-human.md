---
title: LLMs and Why Talking to One Can Feel Like Talking to a Human
date: 2026-10-09
slug: llms-and-why-talking-to-one-can-feel-like-talking-to-a-human
---

## Imagine if the conversation went something like this

**Me:**  

My dog died today.

**LLM:**

1. Create Query, Key, and Value vectors.
2. Compute similarity scores between queries and keys.
3. Turn them into weights with softmax.
4. Take a weighted average of the values.

---

It wouldn't feel much like a natural conversation, would it? 😀

## So what actually happens?

When you send a message to an LLM:

1. **Tokenisation:** Your text is broken into tokens, each with a numerical ID.
2. **Numerical representations:** The token IDs are converted into vectors (collections of numbers) that the model can process.
3. **Self-attention:** This mechanism helps the model use relationships between tokens and their context, rather than treating every word independently.
4. **Text generation:** Using patterns learned during training, the model predicts and generates a response, one token at a time. The output tokens are converted back into readable text.

Fortunately, rather than explaining its internal calculations, the LLM might respond with something like this:

**Me:**  

My dog died today.

**LLM:**  

I'm sorry to hear that. Would you like to tell me about your dog?

---

# Why does it feel like a conversation?

Because the model has learned patterns of human language, including how people respond to questions, express sympathy, explain ideas and maintain a conversation.

When an LLM says something like "Something you said stood out to me", it's using a familiar conversational expression.

That doesn't mean it necessarily experienced curiosity or noticed something in the human sense.

The important distinction is that an LLM can generate language that resembles human conversation, even though the computational process behind it is very different from human thinking.