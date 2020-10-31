from transformers import AutoTokenizer, AutoModelWithLMHead


def preprocess_question(question):
    question += " [End_Question]"
    return question


def process_answer(answer, end_of_question):
    answer = answer[end_of_question+1:]

    special_tokens = [" [End_Question]", " [End_Answer]"]

    for token in special_tokens:
        while token in answer:
            answer = answer.replace(token, "")

    last_EOS = max(
        answer.rfind("."),
        answer.rfind("!"),
        answer.rfind("?"),
    )
    return answer[:last_EOS+1]


def generate_response(question, model, tokenizer):
    question = preprocess_question(question)
    end_of_question = len(question)
    input_ids = tokenizer.encode(question, return_tensors="pt")
    sample_output = model.generate(
        input_ids,
        do_sample=True,
        max_length=100,
        top_p=0.9,
        top_k=0,
    )
    answer = tokenizer.decode(sample_output[0], skip_special_tokens=True)
    answer = process_answer(answer, end_of_question)

    return answer


def load_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained("anonymous-german-nlp/german-gpt2")
    model = AutoModelWithLMHead.from_pretrained(model_path)
    return tokenizer, model


def main():
    while True:
        question = input("Your sentence:   ")
        if question == "exit":
            break
        answer = generate_response(question)
        print("Output:\n" + 100 * '-')
        print(answer)


if __name__ == "__main__":
    main()

