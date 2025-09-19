from search import search_prompt

def main():
    question = input("Digite sua pergunta: ")
    answer = search_prompt(question)

    print(answer)
    
    pass

if __name__ == "__main__":
    main()